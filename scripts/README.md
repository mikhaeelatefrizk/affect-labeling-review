# `scripts/`

Tooling for the open-research package. Distinct from the analysis scripts in `meta-analysis/`, `prisma/`, and `supplementary/`, which are tied to the manuscript's analyses. The scripts here are *infrastructure*: derivation of the screening corpus, validation, and quality reporting.

## Contents

| File | Purpose | Inputs | Outputs |
|---|---|---|---|
| [`extract_included_list.py`](extract_included_list.py) | Cross-reference the analysis-code lists (`run_meta_analysis.py` + `build_rob_figure.py`) with `references.bib` and emit the 22 canonical-identifiable included papers. | `references.bib` | `data/screening/included_papers.csv` |
| [`build_derived_corpus.py`](build_derived_corpus.py) | Re-run the pre-registered Boolean query against PubMed via NCBI E-utilities; download title + abstract + DOI + PMID + journal + year for each hit. | None (queries PubMed) | `data/screening/derived_corpus.csv` |
| [`build_derived_screening_log.py`](build_derived_screening_log.py) | Join the derived corpus against the canonical-identifiable include list to produce a labelled binary screening log. | `derived_corpus.csv` + `included_papers.csv` | `data/screening/derived_screening_log.csv` |
| [`build_quality_report.py`](build_quality_report.py) | Compare canonical vs. derived counts; report year/journal distributions, identifier presence, recall of canonical includes in the PubMed re-query, and class balance. | All of the above | `data/QUALITY_REPORT.md` |
| [`validate_screening_log.py`](validate_screening_log.py) | Schema-validate every screening log CSV against `data/screening/screening_log.schema.json`; reconcile counts with `prisma/prisma_counts.csv`; emit row-level errors. | All screening logs + the schema + the canonical PRISMA CSV | exit 0 if valid, exit 1 with row-level errors |
| `__init__.py` | Empty marker so `scripts/` is a package. | — | — |

## Module structure

Every script is a single self-contained Python file with:

1. A module-level docstring explaining inputs / outputs / honest disclosures.
2. A `main()` function returning an exit code.
3. An `if __name__ == "__main__": raise SystemExit(main())` entry point.

This means each script can be imported (e.g., for testing) without side effects, and each can be run as a standalone CLI.

## Dependencies

All scripts depend only on what is in the top-level [`requirements.txt`](../requirements.txt). No script requires its own venv or extra installs.

The `build_derived_corpus.py` script optionally uses an `NCBI_API_KEY` environment variable to bump the rate limit from 3 req/s to 10 req/s; without it the script still runs, just slower.

## How to extend

Adding a new script:

1. Create `scripts/your_script.py` with the module structure above.
2. Add a target to [`Makefile`](../Makefile).
3. Add a row to this table.
4. If your script writes to `data/`, add a column to `validate_screening_log.py` (or write a sibling validator) so its outputs are schema-checked.

## Honest disclosures (per script)

- **`build_derived_corpus.py`** queries PubMed only (the other 4 databases require institutional access). The retrieved corpus is broader than the canonical 1,842 records reported in the manuscript because PubMed has continued to be indexed and its automatic term mapping is generous. This drift is reported in `data/QUALITY_REPORT.md`.
- **`build_derived_screening_log.py`** produces a positive-unlabelled (PU) labelling. 14 of 22 canonical-identifiable includes match against the derived corpus by DOI / fuzzy title; ~78 unidentified canonical includes may sit in the unlabelled pool. See [`docs/for-ml-researchers.md`](../docs/for-ml-researchers.md) for the full implication.
- **`extract_included_list.py`** identifies 22 of the 100 canonical includes — the meta-analysed and risk-of-bias-assessed subsets. The other 78 are cited in the manuscript prose without per-paper structure and are not enumerated here.

## License

All code in this directory is MIT-licensed. See [`LICENSE-CODE`](../LICENSE-CODE).
