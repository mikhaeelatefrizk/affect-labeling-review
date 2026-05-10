"""Extract the included-papers list from the canonical analysis sources.

Reads authoritative source-of-truth lists from:
  - meta-analysis/run_meta_analysis.py    (the 7 psychophysiology studies, k=9 effect sizes)
  - supplementary/build_rob_figure.py     (the 19 studies in the RoB summary)

Cross-references each entry against `references.bib` to enrich with DOI,
title, authors, and journal.

Writes:
  - data/screening/included_papers.csv

Honest disclosure: the canonical PRISMA flow records 100 included studies,
but only ~22 are explicitly enumerated in the analysis code. The remaining
~78 included studies are cited throughout the manuscript prose without a
structured per-paper record, and are therefore *not* listed here. The
aggregate count of 100 in `prisma/prisma_counts.csv` remains canonical;
this CSV documents the reliably identifiable subset only. See
`data/screening/README.md` for the full caveat.

Usage:
    python scripts/extract_included_list.py
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REFERENCES_BIB = REPO_ROOT / "references.bib"
OUT_CSV = REPO_ROOT / "data" / "screening" / "included_papers.csv"

# ---------------------------------------------------------------------------
# Canonical identifiable include list. Sourced from:
#   - run_meta_analysis.py: study list (psychophys subset)
#   - build_rob_figure.py: studies list (RoB summary)
# When those analysis scripts change, update this mapping accordingly.
# ---------------------------------------------------------------------------
INCLUDED = [
    # (bibtex_key, subset, source_in_repo)
    # --- Psychophysiology meta-analysis subset (k=9 effect sizes, 7 unique studies) ---
    ("kircanski2012",  "psychophysiology_meta_analysis", "meta-analysis/run_meta_analysis.py + supplementary/build_rob_figure.py"),
    ("tabibnia2008",   "psychophysiology_meta_analysis", "meta-analysis/run_meta_analysis.py + supplementary/build_rob_figure.py"),
    ("niles2015",      "psychophysiology_meta_analysis", "meta-analysis/run_meta_analysis.py + supplementary/build_rob_figure.py"),
    ("plaisted2022",   "psychophysiology_meta_analysis", "meta-analysis/run_meta_analysis.py + supplementary/build_rob_figure.py"),
    ("mcrae2010",      "psychophysiology_meta_analysis", "meta-analysis/run_meta_analysis.py"),
    ("fitzpatrick2019","psychophysiology_meta_analysis", "meta-analysis/run_meta_analysis.py"),
    ("matejka2013",    "psychophysiology_meta_analysis", "meta-analysis/run_meta_analysis.py"),

    # --- Neuroimaging / neurostimulation subset (subset of the 42 canonical) ---
    ("lieberman2007",  "neuroimaging_neurostim", "supplementary/build_rob_figure.py"),
    ("hariri2000",     "neuroimaging_neurostim", "supplementary/build_rob_figure.py"),
    ("hariri2003",     "neuroimaging_neurostim", "supplementary/build_rob_figure.py"),
    ("torrisi2013",    "neuroimaging_neurostim", "supplementary/build_rob_figure.py"),
    ("burklund2014",   "neuroimaging_neurostim", "supplementary/build_rob_figure.py"),
    ("vives2021",      "neuroimaging_neurostim", "supplementary/build_rob_figure.py"),

    # --- Behavioral / self-report subset (subset of the 28 canonical) ---
    ("nook2021",       "behavioral_self_report", "supplementary/build_rob_figure.py"),
    ("ariely2026",     "behavioral_self_report", "supplementary/build_rob_figure.py"),
    ("vlasenko2021",   "behavioral_self_report", "supplementary/build_rob_figure.py"),
    ("levygigi2022",   "behavioral_self_report", "supplementary/build_rob_figure.py"),

    # --- Clinical / patient populations subset (subset of the 12 canonical) ---
    ("burklund2024",   "clinical_patient_populations", "supplementary/build_rob_figure.py"),

    # --- Prior meta-analyses subset (subset of the 9 canonical) ---
    ("costafreda2008", "prior_meta_analyses", "supplementary/build_rob_figure.py"),
    ("brooks2017",     "prior_meta_analyses", "supplementary/build_rob_figure.py"),
    ("buhle2014",      "prior_meta_analyses", "supplementary/build_rob_figure.py"),
    ("berboth2021",    "prior_meta_analyses", "supplementary/build_rob_figure.py"),
]

CANONICAL_SUBSET_TOTALS = {
    "psychophysiology_meta_analysis": 9,
    "neuroimaging_neurostim": 42,
    "behavioral_self_report": 28,
    "clinical_patient_populations": 12,
    "prior_meta_analyses": 9,
}


def parse_bibtex_entries(text: str) -> dict[str, dict[str, str]]:
    """Tiny BibTeX parser sufficient for this repo's flat references.bib.

    Avoids the bibtexparser dependency for the common path so this script
    works on a clean install before requirements are installed.
    """
    entries: dict[str, dict[str, str]] = {}
    # Split on top-level @article{key, ...} or @book{key, ...}, etc.
    # We rely on the convention: each entry starts with '@' at column 0.
    raw_entries = re.split(r"(?m)^@", text)
    for raw in raw_entries:
        raw = raw.strip()
        if not raw or "{" not in raw:
            continue
        m = re.match(r"(\w+)\s*\{\s*([^,\s]+)\s*,\s*(.*)\}\s*$", raw, flags=re.DOTALL)
        if not m:
            continue
        entry_type, key, body = m.group(1).lower(), m.group(2), m.group(3)
        fields: dict[str, str] = {"_type": entry_type}
        # Field parsing: name = {value} or name = "value", with brace-aware splitting.
        i = 0
        while i < len(body):
            field_match = re.match(r"\s*(\w+)\s*=\s*", body[i:])
            if not field_match:
                break
            field_name = field_match.group(1).lower()
            i += field_match.end()
            if i >= len(body):
                break
            opener = body[i]
            if opener == "{":
                depth = 1
                i += 1
                start = i
                while i < len(body) and depth > 0:
                    if body[i] == "{":
                        depth += 1
                    elif body[i] == "}":
                        depth -= 1
                    i += 1
                value = body[start : i - 1]
            elif opener == '"':
                i += 1
                start = i
                while i < len(body) and body[i] != '"':
                    i += 1
                value = body[start:i]
                i += 1
            else:
                # Bare numeric / identifier value (rare in this file)
                m2 = re.match(r"([^,]+)", body[i:])
                value = m2.group(1).strip() if m2 else ""
                i += len(value)
            # Skip trailing comma + whitespace
            m_comma = re.match(r"\s*,\s*", body[i:])
            if m_comma:
                i += m_comma.end()
            # Strip protective braces and normalize whitespace
            value = re.sub(r"\s+", " ", value).strip()
            value = value.replace("{", "").replace("}", "")
            fields[field_name] = value
        entries[key] = fields
    return entries


def main() -> int:
    bib_text = REFERENCES_BIB.read_text(encoding="utf-8")
    entries = parse_bibtex_entries(bib_text)

    rows = []
    missing_keys = []
    for key, subset, source in INCLUDED:
        entry = entries.get(key)
        if entry is None:
            missing_keys.append(key)
            continue
        rows.append({
            "record_id": f"canonical-{key}",
            "bibtex_key": key,
            "subset": subset,
            "title": entry.get("title", ""),
            "authors": entry.get("author", ""),
            "year": entry.get("year", ""),
            "journal": entry.get("journal", entry.get("publisher", "")),
            "doi": entry.get("doi", ""),
            "source_in_repo": source,
        })

    if missing_keys:
        print(f"WARN: {len(missing_keys)} keys not found in references.bib:")
        for k in missing_keys:
            print(f"  - {k}")

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["record_id", "bibtex_key", "subset", "title", "authors",
                  "year", "journal", "doi", "source_in_repo"]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)

    # Subset breakdown
    by_subset: dict[str, int] = {}
    for r in rows:
        by_subset[r["subset"]] = by_subset.get(r["subset"], 0) + 1

    print(f"[OK] Wrote {OUT_CSV.relative_to(REPO_ROOT)} ({len(rows)} rows)")
    print()
    print("Identifiable-vs-canonical breakdown by subset:")
    print(f"  {'subset':<40} {'identified':>11} {'canonical':>10} {'gap':>6}")
    for subset, canonical in CANONICAL_SUBSET_TOTALS.items():
        identified = by_subset.get(subset, 0)
        gap = canonical - identified
        print(f"  {subset:<40} {identified:>11} {canonical:>10} {gap:>6}")
    total_id = sum(by_subset.values())
    total_canonical = sum(CANONICAL_SUBSET_TOTALS.values())
    print(f"  {'TOTAL':<40} {total_id:>11} {total_canonical:>10} {total_canonical - total_id:>6}")
    print()
    print("The gap (papers cited in the manuscript prose but not enumerated in")
    print("a structured form) is documented in data/screening/README.md and")
    print("data/QUALITY_REPORT.md. The aggregate of 100 in prisma_counts.csv")
    print("remains canonical.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
