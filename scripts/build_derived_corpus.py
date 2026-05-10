"""Re-derive the candidate corpus from PubMed using the pre-registered query.

Calls the NCBI E-utilities API (ESearch + EFetch) with the Boolean query
documented in `prereg/PROSPERO_preregistration.md`. Writes one row per
retrieved PubMed record to `data/screening/derived_corpus.csv`.

Honest disclosure:

  - The original PRISMA flow records 1,842 records identified across five
    databases (PubMed + PsycINFO + Web of Science + Scopus + Cochrane).
    This script re-queries PubMed only, because PsycINFO/WoS/Scopus/Cochrane
    require institutional or paid API access. PubMed alone covers the
    majority of biomedical/psychology research and is the standard public
    re-derivation target.
  - Hit counts will differ from the canonical 1,842 because: (a) databases
    other than PubMed are excluded, and (b) PubMed continues to be indexed
    over time. This drift is expected and reported in QUALITY_REPORT.md.

Provenance is embedded in the output: a header comment in the CSV records
the exact query, retrieval date, and tool version.

Usage:
    python scripts/build_derived_corpus.py [--max N] [--api-key KEY]

Environment:
    NCBI_API_KEY        Optional. Higher rate limits with a key (10 req/s
                        vs. 3 req/s). Get one free at
                        https://www.ncbi.nlm.nih.gov/account/.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
import time
import urllib.parse
from datetime import date, datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

import requests

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_CSV = REPO_ROOT / "data" / "screening" / "derived_corpus.csv"

# Canonical query from prereg/PROSPERO_preregistration.md §7. We submit the
# query to PubMed exactly as written (no [All Fields] qualifier and no
# explicit MeSH mapping), which lets PubMed apply its standard automatic
# term mapping. Empirically this returns ~3,900 records in 2026, broader
# than the original 1,842 figure (combined across 5 databases) because:
#   1. PubMed has grown since the original search.
#   2. Automatic term mapping expands "anxiety" and similar clinical
#      terms via MeSH.
# This drift is expected and reported in QUALITY_REPORT.md.
PUBMED_QUERY = (
    '("affect labeling" OR "affect labelling" OR "putting feelings into words" '
    'OR "emotion naming" OR "emotion labeling" OR "emotion labelling" '
    'OR "verbalizing emotion" OR "verbal labeling") '
    'AND '
    '("emotion regulation" OR "amygdala" OR "ventrolateral prefrontal" '
    'OR "skin conductance" OR "heart rate" OR "heart rate variability" '
    'OR "respiratory sinus arrhythmia" OR "late positive potential" '
    'OR "exposure therapy" OR "anxiety")'
)

ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

TOOL_NAME = "affect-labeling-review"
EMAIL = "mikhaeelatefrizk@proton.me"
TOOL_VERSION = "1.0.0"


def esearch(query: str, retmax: int, api_key: str | None) -> tuple[int, str, str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": retmax,
        "usehistory": "y",
        "retmode": "json",
        "tool": TOOL_NAME,
        "email": EMAIL,
    }
    if api_key:
        params["api_key"] = api_key
    r = requests.get(ESEARCH_URL, params=params, timeout=60)
    r.raise_for_status()
    data = r.json()["esearchresult"]
    return int(data["count"]), data["webenv"], data["querykey"]


def efetch_batch(webenv: str, query_key: str, retstart: int, retmax: int,
                 api_key: str | None) -> bytes:
    params = {
        "db": "pubmed",
        "WebEnv": webenv,
        "query_key": query_key,
        "retstart": retstart,
        "retmax": retmax,
        "retmode": "xml",
        "rettype": "abstract",
        "tool": TOOL_NAME,
        "email": EMAIL,
    }
    if api_key:
        params["api_key"] = api_key
    r = requests.get(EFETCH_URL, params=params, timeout=120)
    r.raise_for_status()
    return r.content


def parse_articles(xml_bytes: bytes) -> list[dict[str, str]]:
    root = ET.fromstring(xml_bytes)
    rows = []
    for article in root.findall(".//PubmedArticle"):
        pmid_el = article.find(".//MedlineCitation/PMID")
        pmid = pmid_el.text if pmid_el is not None and pmid_el.text else ""

        title_el = article.find(".//ArticleTitle")
        title = "".join(title_el.itertext()).strip() if title_el is not None else ""

        # Abstract — concatenate all AbstractText elements (label + text)
        abstract_parts = []
        for abs_el in article.findall(".//Abstract/AbstractText"):
            label = abs_el.get("Label")
            text = "".join(abs_el.itertext()).strip()
            if label:
                abstract_parts.append(f"{label}: {text}")
            else:
                abstract_parts.append(text)
        abstract = " ".join(abstract_parts)

        # Authors
        author_list = []
        for au in article.findall(".//AuthorList/Author"):
            last = au.findtext("LastName") or au.findtext("CollectiveName") or ""
            initials = au.findtext("Initials") or ""
            if last:
                author_list.append(f"{last}{(' ' + initials) if initials else ''}")
        authors = "; ".join(author_list)

        # Journal
        journal = article.findtext(".//Journal/Title") or ""

        # Year (prefer ArticleDate, fall back to PubDate)
        year = ""
        for path in (".//ArticleDate/Year", ".//PubDate/Year"):
            y = article.findtext(path)
            if y:
                year = y
                break
        if not year:
            medline_date = article.findtext(".//PubDate/MedlineDate") or ""
            if medline_date:
                # e.g. "2007 Jan-Feb"
                year = medline_date.split()[0][:4]

        # DOI
        doi = ""
        for ai in article.findall(".//ArticleIdList/ArticleId"):
            if ai.get("IdType") == "doi" and ai.text:
                doi = ai.text.strip()
                break

        rows.append({
            "record_id": f"pub-{pmid}",
            "pmid": pmid,
            "doi": doi,
            "title": title,
            "abstract": abstract,
            "year": year,
            "authors": authors,
            "journal": journal,
            "source_database": "pubmed",
        })
    return rows


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Re-derive PubMed corpus.")
    parser.add_argument("--max", type=int, default=10000, help="Max records to retrieve.")
    parser.add_argument("--batch", type=int, default=200, help="EFetch batch size.")
    parser.add_argument("--api-key", default=os.environ.get("NCBI_API_KEY"),
                        help="NCBI API key (or set NCBI_API_KEY env var).")
    args = parser.parse_args(argv[1:])

    delay = 0.12 if args.api_key else 0.34  # respect rate limits

    print(f"[+] ESearch: query length {len(PUBMED_QUERY)} chars, retmax={args.max}")
    try:
        total, webenv, query_key = esearch(PUBMED_QUERY, args.max, args.api_key)
    except requests.RequestException as e:
        print(f"FAIL: ESearch network error: {e}")
        return 2
    except Exception as e:
        print(f"FAIL: ESearch returned unexpected response: {e}")
        return 2

    print(f"[+] PubMed reports {total} matching records.")
    fetch_n = min(total, args.max)
    print(f"[+] EFetching {fetch_n} records in batches of {args.batch}...")

    all_rows: list[dict[str, str]] = []
    for retstart in range(0, fetch_n, args.batch):
        try:
            xml_bytes = efetch_batch(webenv, query_key, retstart,
                                      min(args.batch, fetch_n - retstart),
                                      args.api_key)
            batch_rows = parse_articles(xml_bytes)
            all_rows.extend(batch_rows)
            print(f"    fetched {retstart + len(batch_rows)}/{fetch_n}", flush=True)
        except requests.RequestException as e:
            print(f"    WARN: batch starting at {retstart} failed: {e}; retrying once after 5s")
            time.sleep(5)
            xml_bytes = efetch_batch(webenv, query_key, retstart,
                                      min(args.batch, fetch_n - retstart),
                                      args.api_key)
            batch_rows = parse_articles(xml_bytes)
            all_rows.extend(batch_rows)
        time.sleep(delay)

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["record_id", "pmid", "doi", "title", "abstract",
                  "year", "authors", "journal", "source_database"]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        # Provenance header (CSV comments are non-standard; we use a sentinel row.)
        provenance = (
            f"# Generated by scripts/build_derived_corpus.py v{TOOL_VERSION} on "
            f"{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}.\n"
            f"# PubMed reported {total} matching records; fetched {len(all_rows)}.\n"
            f"# Canonical PRISMA flow recorded 1842 database records (5 databases combined); "
            f"this re-derivation queries PubMed only.\n"
            f"# Query: {PUBMED_QUERY}\n"
        )
        fh.write(provenance)
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_rows:
            writer.writerow(row)

    print(f"[OK] Wrote {OUT_CSV.relative_to(REPO_ROOT)} ({len(all_rows)} records, "
          f"{total} reported by PubMed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
