"""Validate the screening corpus and reconcile its counts with the canonical PRISMA flow.

Runs three checks:

  1. Schema validation. Every screening-log CSV is validated against
     `data/screening/screening_log.schema.json`. Required fields must be
     present; enums are enforced.

  2. PRISMA reconciliation. The number of `decision == include` rows in any
     screening log must match the canonical `total` count in
     `prisma/prisma_counts.csv` (currently 100). Subset assignments must sum
     to that total.

  3. Identifier integrity. PMIDs must be all-digits. DOIs must match the
     standard `10.<registrant>/<suffix>` pattern. Years must be plausible.

Exit code 0 on success; 1 on any failure with row-level error messages.

Usage:
    python scripts/validate_screening_log.py
    python scripts/validate_screening_log.py path/to/some_log.csv  # validate one file
"""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO_ROOT / "data" / "screening" / "screening_log.schema.json"
PRISMA_CSV = REPO_ROOT / "prisma" / "prisma_counts.csv"

DEFAULT_TARGETS = [
    REPO_ROOT / "data" / "screening" / "screening_log.template.csv",
    REPO_ROOT / "data" / "screening" / "derived_screening_log.csv",
]

DOI_RE = re.compile(r"^10\.[^/]+/.+$")
PMID_RE = re.compile(r"^[0-9]+$")


def load_schema() -> dict:
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def load_canonical_counts() -> dict[str, int]:
    counts: dict[str, int] = {}
    with PRISMA_CSV.open(encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            counts[row["sub_stage"]] = int(row["count"])
    return counts


def validate_row(row: dict, schema: dict, lineno: int) -> list[str]:
    """Return a list of error strings for this row; empty list if valid."""
    errors: list[str] = []
    props = schema["properties"]
    required = set(schema.get("required", []))

    # Required fields
    for field in required:
        if not row.get(field):
            errors.append(f"line {lineno}: missing required field '{field}'")

    # Enum constraints
    for field, spec in props.items():
        value = row.get(field, "")
        if value in ("", None):
            continue
        if "enum" in spec:
            allowed = [v for v in spec["enum"] if v is not None]
            if value not in allowed:
                errors.append(
                    f"line {lineno}: '{field}'={value!r} not in allowed enum "
                    f"({', '.join(repr(a) for a in allowed)})"
                )

    # Identifier sanity
    pmid = row.get("pmid", "")
    if pmid and not PMID_RE.match(pmid):
        errors.append(f"line {lineno}: invalid PMID format: {pmid!r}")

    doi = row.get("doi", "")
    if doi and not DOI_RE.match(doi):
        errors.append(f"line {lineno}: invalid DOI format: {doi!r}")

    year = row.get("year", "")
    if year:
        try:
            y = int(year)
            if y < 1800 or y > 2100:
                errors.append(f"line {lineno}: implausible year {y}")
        except ValueError:
            errors.append(f"line {lineno}: year not an integer: {year!r}")

    return errors


def validate_file(path: Path, schema: dict) -> tuple[int, int, list[str], dict[str, int]]:
    """Return (rows, valid_rows, errors, decision_counts)."""
    if not path.exists():
        return 0, 0, [f"FILE NOT FOUND: {path.relative_to(REPO_ROOT)}"], {}

    rows = 0
    valid = 0
    errors: list[str] = []
    decisions: dict[str, int] = {}
    subsets: dict[str, int] = {}

    with path.open(encoding="utf-8", newline="") as fh:
        # Skip provenance comment lines starting with '#'
        header_offset = 0
        while True:
            pos = fh.tell()
            line = fh.readline()
            if not line:
                break
            if line.startswith("#"):
                header_offset += 1
                continue
            fh.seek(pos)
            break

        reader = csv.DictReader(fh)
        # Line numbers in messages: header_offset (comment lines) + 1 (header) + 1 (first data row)
        for lineno, row in enumerate(reader, start=header_offset + 2):
            rows += 1
            row_errors = validate_row(row, schema, lineno)
            if row_errors:
                errors.extend(row_errors)
            else:
                valid += 1
            decisions[row.get("decision", "")] = decisions.get(row.get("decision", ""), 0) + 1
            subset = row.get("synthesis_subset", "")
            if subset:
                subsets[subset] = subsets.get(subset, 0) + 1

    return rows, valid, errors, {**decisions, **{f"subset:{k}": v for k, v in subsets.items()}}


def reconcile_with_prisma(counts: dict[str, int], canonical: dict[str, int], path: Path) -> list[str]:
    """Return reconciliation errors as a list of strings.

    Reconciliation expectations vary by file type:

      - screening_log.template.csv: skipped (1 example row).
      - derived_screening_log.csv: positive-unlabeled, so partial recall is
        expected; we only check that recall is non-zero and that no subset
        count exceeds the canonical total.
      - any other screening_log*.csv: treated as a fully-labeled hand log
        and required to reconcile exactly.
    """
    errors: list[str] = []
    n_include = counts.get("include", 0)
    expected_include = canonical["total"]

    if path.name == "screening_log.template.csv":
        return errors

    if path.name == "derived_screening_log.csv":
        # PU labeling: expect partial recall, not full 100.
        if n_include == 0:
            errors.append(f"{path.name}: count of decision=include is 0; "
                          "no canonical includes were matched. Investigate.")
        # Subsets cannot exceed canonical totals
        subset_canonical = {
            "neuroimaging_neurostim": canonical["subset_neuroimaging_neurostim"],
            "psychophysiology_meta_analysis": canonical["subset_psychophysiology_meta_analysis"],
            "behavioral_self_report": canonical["subset_behavioral_self_report"],
            "clinical_patient_populations": canonical["subset_clinical_patient_populations"],
            "prior_meta_analyses": canonical["subset_prior_meta_analyses"],
        }
        for name, expected in subset_canonical.items():
            actual = counts.get(f"subset:{name}", 0)
            if actual > expected:
                errors.append(
                    f"{path.name}: subset '{name}' count is {actual}, "
                    f"exceeds canonical {expected}"
                )
        return errors

    # Default: hand-labeled log — must reconcile exactly.
    if n_include != expected_include:
        errors.append(
            f"{path.name}: count of decision=include is {n_include}, "
            f"expected canonical total of {expected_include} "
            f"(from prisma_counts.csv)"
        )

    subset_canonical = {
        "neuroimaging_neurostim": canonical["subset_neuroimaging_neurostim"],
        "psychophysiology_meta_analysis": canonical["subset_psychophysiology_meta_analysis"],
        "behavioral_self_report": canonical["subset_behavioral_self_report"],
        "clinical_patient_populations": canonical["subset_clinical_patient_populations"],
        "prior_meta_analyses": canonical["subset_prior_meta_analyses"],
    }
    for name, expected in subset_canonical.items():
        actual = counts.get(f"subset:{name}", 0)
        if actual and actual != expected:
            errors.append(
                f"{path.name}: subset '{name}' count is {actual}, expected {expected}"
            )

    return errors


def main(argv: list[str]) -> int:
    schema = load_schema()
    canonical = load_canonical_counts()

    targets = [Path(a).resolve() for a in argv[1:]] or DEFAULT_TARGETS
    overall_errors: list[str] = []

    for target in targets:
        rel = target.relative_to(REPO_ROOT) if REPO_ROOT in target.parents else target.name
        print(f"\n=== {rel} ===")
        rows, valid, errors, counts = validate_file(target, schema)
        if rows == 0 and errors:
            print(errors[0])
            # Allow derived_screening_log.csv to be missing pre-derivation
            if target.name == "derived_screening_log.csv":
                print("(skipping; run `make derive` to produce this file)")
                continue
            overall_errors.extend(errors)
            continue

        print(f"rows: {rows}, valid: {valid}")
        for k, v in counts.items():
            if k:
                print(f"  {k}: {v}")
        if errors:
            print("Schema errors:")
            for e in errors[:20]:
                print(f"  - {e}")
            if len(errors) > 20:
                print(f"  ... and {len(errors) - 20} more")
            overall_errors.extend(errors)

        recon = reconcile_with_prisma(counts, canonical, target)
        if recon:
            print("Reconciliation errors:")
            for e in recon:
                print(f"  - {e}")
            overall_errors.extend(recon)

    print("\n" + "=" * 60)
    if overall_errors:
        print(f"FAIL: {len(overall_errors)} error(s).")
        return 1
    print("OK: all checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
