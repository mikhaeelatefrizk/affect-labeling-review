"""Build `data/screening/all_references.csv` — every bibliography entry as a structured row.

Parses `references.bib` (86 entries at time of writing), joins with
`data/screening/included_papers.csv` to flag the confidently-identified
included papers, and counts how many times each reference is mentioned in
the manuscript prose. The result is a single CSV that researchers re-using
the corpus can join against their own merged dataset by DOI or fuzzy title.

Columns:
    bibtex_key            stable identifier matching @key{...} in references.bib
    title                 article/book title
    authors               full author string from BibTeX
    first_author_surname  surname of the first listed author (e.g., "Lieberman")
    year                  publication year
    journal               journal/booktitle/publisher (whichever applies)
    doi                   DOI when present in BibTeX
    entry_type            bib entry type: article, book, incollection, etc.
    is_confirmed_include  1 if the bibtex_key appears in included_papers.csv, else 0
    include_subset        synthesis-subset assignment for confirmed includes; "" otherwise
    manuscript_mentions   number of times the reference is cited in manuscript prose
                          (counted by matching `<Surname>` ... `<Year>` co-occurrences
                          within a 120-character window; this is a usage-frequency
                          signal, not an inclusion label).

What the manuscript_mentions column is and isn't.
    It IS a real, deterministic count of how often the manuscript text mentions
    each reference. It is useful as a signal: references with many mentions in
    the Results section are almost certainly included studies; references with
    a single mention in the Methods section are usually methodology citations.
    It IS NOT a per-paper inclusion label. The original per-paper screening
    decisions for the 1,571 title/abstract records and the 282 full-text
    records were not preserved in a shareable form — that limitation is
    documented in `data/screening/README.md`.

Usage:
    python scripts/build_all_references.py
"""
from __future__ import annotations

import csv
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REFERENCES_BIB = REPO_ROOT / "references.bib"
INCLUDED_CSV = REPO_ROOT / "data" / "screening" / "included_papers.csv"
MANUSCRIPT = REPO_ROOT / "manuscript" / "manuscript.md"
OUT_CSV = REPO_ROOT / "data" / "screening" / "all_references.csv"


def parse_bib(text: str) -> list[dict]:
    """Parse @entry{key, field = {value}, ...} blocks into dicts."""
    entries: list[dict] = []
    for m in re.finditer(r"@(\w+)\s*\{\s*([^,\s]+)\s*,(.*?)\n\}", text, flags=re.DOTALL):
        kind, key, body = m.group(1), m.group(2), m.group(3)
        fields: dict[str, str] = {"entry_type": kind, "bibtex_key": key}
        for fm in re.finditer(r"(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\})*)\}", body, flags=re.DOTALL):
            name = fm.group(1).strip().lower()
            value = re.sub(r"\s+", " ", fm.group(2).strip())
            value = value.replace("{", "").replace("}", "")
            fields[name] = value
        entries.append(fields)
    return entries


def first_author_surname(author_field: str) -> str:
    """Return the first listed author's surname from a BibTeX `author` field.

    BibTeX author fields use either `Surname, Given` or `Given Surname`, with
    multiple authors separated by ` and `. We take the first author and
    extract the surname under both conventions.
    """
    if not author_field:
        return ""
    first = author_field.split(" and ")[0].strip()
    if "," in first:
        return first.split(",", 1)[0].strip()
    parts = first.split()
    return parts[-1] if parts else ""


def load_confirmed() -> dict[str, str]:
    """Return {bibtex_key: include_subset} from included_papers.csv."""
    confirmed: dict[str, str] = {}
    with INCLUDED_CSV.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            confirmed[row["bibtex_key"]] = row["subset"]
    return confirmed


def count_mentions(text: str, surname: str, year: str) -> int:
    """Count how often `<surname>` and `<year>` co-occur within 120 characters.

    Both orders are accepted (`Surname ... Year` and `Year ... Surname`), so
    the count includes parenthetical citations like `(Surname et al., Year)`
    as well as narrative citations like `Surname et al. (Year)`. Matches are
    word-bounded to avoid partial matches (e.g., year 2007 inside 20074).
    """
    if not surname or not year:
        return 0
    s = re.escape(surname)
    y = re.escape(year)
    # surname ... year (within 120 chars)
    pat_fwd = re.compile(rf"\b{s}\b[\s\S]{{0,120}}?\b{y}\b")
    # year ... surname (within 120 chars)
    pat_rev = re.compile(rf"\b{y}\b[\s\S]{{0,120}}?\b{s}\b")
    return len(pat_fwd.findall(text)) + len(pat_rev.findall(text))


def main() -> None:
    bib_text = REFERENCES_BIB.read_text(encoding="utf-8")
    entries = parse_bib(bib_text)
    confirmed = load_confirmed()
    manuscript_text = MANUSCRIPT.read_text(encoding="utf-8")

    rows = []
    for e in entries:
        key = e.get("bibtex_key", "")
        surname = first_author_surname(e.get("author", ""))
        year = e.get("year", "")
        rows.append({
            "bibtex_key": key,
            "title": e.get("title", ""),
            "authors": e.get("author", ""),
            "first_author_surname": surname,
            "year": year,
            "journal": e.get("journal", "") or e.get("booktitle", "") or e.get("publisher", ""),
            "doi": e.get("doi", ""),
            "entry_type": e.get("entry_type", ""),
            "is_confirmed_include": 1 if key in confirmed else 0,
            "include_subset": confirmed.get(key, ""),
            "manuscript_mentions": count_mentions(manuscript_text, surname, year),
        })

    # Sort: confirmed includes first (by key), then others by manuscript_mentions desc.
    rows.sort(key=lambda r: (
        -r["is_confirmed_include"],
        -r["manuscript_mentions"] if r["is_confirmed_include"] == 0 else 0,
        r["bibtex_key"],
    ))

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(
            fh,
            fieldnames=[
                "bibtex_key", "title", "authors", "first_author_surname",
                "year", "journal", "doi", "entry_type",
                "is_confirmed_include", "include_subset", "manuscript_mentions",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)

    total = len(rows)
    confirmed_n = sum(1 for r in rows if r["is_confirmed_include"] == 1)
    cited_in_ms = sum(1 for r in rows if r["manuscript_mentions"] > 0)
    print(
        f"Wrote {OUT_CSV.relative_to(REPO_ROOT)}: "
        f"{total} rows, "
        f"{confirmed_n} confirmed includes, "
        f"{cited_in_ms} cited in manuscript prose."
    )


if __name__ == "__main__":
    main()
