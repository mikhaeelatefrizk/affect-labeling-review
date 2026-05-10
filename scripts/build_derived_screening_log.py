"""Build the labeled screening log by joining the derived corpus with the included-papers list.

Inputs (must exist):
  - data/screening/derived_corpus.csv     (PubMed re-query output)
  - data/screening/included_papers.csv    (canonical-identifiable includes, n=22)

Output:
  - data/screening/derived_screening_log.csv

Matching strategy (per row in derived_corpus):
  1. DOI exact match (case-insensitive) against included_papers.csv → include
  2. PMID match against the canonical PubMed IDs of included papers (computed
     by re-resolving DOIs through PubMed where possible) → include
  3. Title fuzzy match (Jaccard >= 0.85 on lowercased word tokens) → include
  4. Otherwise → unknown (positive-unlabeled framing)

The label column is named `decision` and uses the values:
  - "include"  → confirmed positive (matched against canonical includes)
  - "unknown"  → not matched; could be a true exclude or a canonical-include
                 we could not identify (only 22 of 100 canonical includes are
                 enumerated in structured form)

This is intentionally a positive-unlabeled (PU) labeling, which is the
honest framing given that 78 of the 100 canonical included papers are not
enumerated in any structured source. ML researchers training screening
classifiers on this dataset should use PU-aware methods, or treat
"unknown" as "exclude" with explicit caveat.

Usage:
    python scripts/build_derived_screening_log.py
"""

from __future__ import annotations

import csv
import re
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CORPUS_CSV = REPO_ROOT / "data" / "screening" / "derived_corpus.csv"
INCLUDED_CSV = REPO_ROOT / "data" / "screening" / "included_papers.csv"
OUT_CSV = REPO_ROOT / "data" / "screening" / "derived_screening_log.csv"

TOOL_VERSION = "1.0.0"


def normalize_doi(doi: str) -> str:
    return doi.strip().lower() if doi else ""


def title_tokens(title: str) -> set[str]:
    """Lowercase, alpha-only tokens of length >= 3, sans common stopwords."""
    stop = {
        "the", "a", "an", "and", "or", "of", "in", "on", "for", "to", "with",
        "by", "at", "from", "as", "is", "are", "was", "were", "be", "been",
        "being", "this", "that", "these", "those", "it", "its", "into",
        "during", "between", "within",
    }
    words = re.findall(r"[a-z]{3,}", title.lower())
    return {w for w in words if w not in stop}


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    return len(a & b) / len(a | b)


def read_corpus(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    """Read the derived corpus CSV. Returns (rows, provenance_lines)."""
    provenance = []
    rows = []
    with path.open(encoding="utf-8", newline="") as fh:
        # Skip provenance comment lines starting with '#'
        while True:
            pos = fh.tell()
            line = fh.readline()
            if not line:
                break
            if line.startswith("#"):
                provenance.append(line.rstrip("\n"))
                continue
            fh.seek(pos)
            break
        for row in csv.DictReader(fh):
            rows.append(row)
    return rows, provenance


def main() -> int:
    if not CORPUS_CSV.exists():
        print(f"FAIL: {CORPUS_CSV.relative_to(REPO_ROOT)} not found. "
              f"Run scripts/build_derived_corpus.py first.")
        return 1
    if not INCLUDED_CSV.exists():
        print(f"FAIL: {INCLUDED_CSV.relative_to(REPO_ROOT)} not found. "
              f"Run scripts/extract_included_list.py first.")
        return 1

    # Load included papers index
    included_by_doi: dict[str, dict[str, str]] = {}
    included_by_title: list[tuple[set[str], dict[str, str]]] = []
    with INCLUDED_CSV.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            doi = normalize_doi(row["doi"])
            if doi:
                included_by_doi[doi] = row
            included_by_title.append((title_tokens(row["title"]), row))

    corpus_rows, corpus_provenance = read_corpus(CORPUS_CSV)

    # Counters for the report
    n_include_doi = n_include_title = n_unknown = 0
    matched_includes: set[str] = set()  # bibtex_keys
    output_rows = []
    for row in corpus_rows:
        doi = normalize_doi(row.get("doi", ""))
        match_strategy = ""
        included_match = None

        if doi and doi in included_by_doi:
            included_match = included_by_doi[doi]
            match_strategy = "doi_exact"
            n_include_doi += 1
        else:
            corpus_title_set = title_tokens(row.get("title", ""))
            best_score = 0.0
            best_match = None
            for inc_title_set, inc_row in included_by_title:
                score = jaccard(corpus_title_set, inc_title_set)
                if score > best_score:
                    best_score = score
                    best_match = inc_row
            if best_score >= 0.85 and best_match:
                included_match = best_match
                match_strategy = f"title_jaccard_{best_score:.2f}"
                n_include_title += 1

        if included_match:
            matched_includes.add(included_match["bibtex_key"])
            output_rows.append({
                "record_id": row["record_id"],
                "source_database": "pubmed",
                "pmid": row.get("pmid", ""),
                "doi": row.get("doi", ""),
                "title": row.get("title", ""),
                "abstract": row.get("abstract", ""),
                "year": row.get("year", ""),
                "authors": row.get("authors", ""),
                "journal": row.get("journal", ""),
                "decision": "include",
                "decision_stage": "combined",
                "exclusion_reason": "",
                "synthesis_subset": included_match["subset"],
                "screener_id": "derived_pubmed_2026",
                "screening_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "notes": f"Derived: matched canonical include via {match_strategy} "
                         f"(bibtex_key={included_match['bibtex_key']})",
            })
        else:
            n_unknown += 1
            output_rows.append({
                "record_id": row["record_id"],
                "source_database": "pubmed",
                "pmid": row.get("pmid", ""),
                "doi": row.get("doi", ""),
                "title": row.get("title", ""),
                "abstract": row.get("abstract", ""),
                "year": row.get("year", ""),
                "authors": row.get("authors", ""),
                "journal": row.get("journal", ""),
                "decision": "unknown",
                "decision_stage": "combined",
                "exclusion_reason": "",
                "synthesis_subset": "",
                "screener_id": "derived_pubmed_2026",
                "screening_date": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                "notes": "No match in canonical-identifiable include list. May be a true exclude or an unidentified canonical include.",
            })

    fieldnames = [
        "record_id", "source_database", "pmid", "doi", "title", "abstract",
        "year", "authors", "journal", "decision", "decision_stage",
        "exclusion_reason", "synthesis_subset", "screener_id", "screening_date",
        "notes",
    ]
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        # Provenance preamble (then standard CSV header)
        fh.write(f"# Generated by scripts/build_derived_screening_log.py v{TOOL_VERSION} "
                 f"on {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}.\n")
        fh.write(f"# Corpus: {len(corpus_rows)} records (from data/screening/derived_corpus.csv).\n")
        fh.write(f"# Canonical-identifiable includes: 22 (from data/screening/included_papers.csv).\n")
        fh.write(f"# Match results: {n_include_doi} by DOI, {n_include_title} by title-fuzzy, "
                 f"{n_unknown} unknown.\n")
        fh.write(f"# Distinct canonical-includes matched: {len(matched_includes)}/22.\n")
        fh.write(f"# Labeling is positive-unlabeled (PU): 'include' = confirmed positive; "
                 f"'unknown' = not matched (may be true exclude or an unidentified canonical include).\n")
        for line in corpus_provenance:
            fh.write(f"# (corpus provenance) {line.lstrip('# ')}\n")
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in output_rows:
            writer.writerow(row)

    print(f"[OK] Wrote {OUT_CSV.relative_to(REPO_ROOT)}")
    print(f"     rows: {len(output_rows)}")
    print(f"     decision=include : {n_include_doi + n_include_title} "
          f"({n_include_doi} doi, {n_include_title} title-fuzzy)")
    print(f"     decision=unknown : {n_unknown}")
    print(f"     distinct canonical-includes matched: {len(matched_includes)}/22")
    if len(matched_includes) < 22:
        with INCLUDED_CSV.open(encoding="utf-8", newline="") as fh:
            unmatched = {r["bibtex_key"] for r in csv.DictReader(fh)} - matched_includes
        print(f"     canonical-includes NOT in PubMed corpus: {sorted(unmatched)}")
        print("     (these are likely either old papers without DOIs in PubMed, "
              "or background-citation MAs whose abstracts don't trigger the AL query)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
