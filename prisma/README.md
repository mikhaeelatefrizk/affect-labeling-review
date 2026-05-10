# `prisma/`

The PRISMA 2020 flow — the canonical record of how records moved from identification through inclusion.

## Contents

| File | What it is |
|---|---|
| [`build_prisma.py`](build_prisma.py) | Generator script. Reads canonical counts from `prisma_counts.csv`, asserts internal arithmetic consistency, and emits both the legacy text counts file and the PRISMA flow figure. |
| [`prisma_counts.csv`](prisma_counts.csv) | **Canonical, machine-readable.** 19 rows: stage / sub_stage / count / description. The single source of truth for every PRISMA number quoted in the manuscript. |
| [`prisma_counts.txt`](prisma_counts.txt) | Legacy human-readable format. Generated from `prisma_counts.csv`; byte-identical to the manuscript-cited values. |
| `prisma_counts.derived.txt` | Side-by-side comparison of canonical vs. derived (PubMed re-query) counts. Generated when `data/screening/derived_screening_log.csv` exists. |
| [`PRISMA_2020_checklist.md`](PRISMA_2020_checklist.md) | The full 27-item PRISMA 2020 reporting checklist with per-item pointers to where in the package each item is reported. Required by major systematic-review journals. |

## Headline numbers

```
Records identified (databases)        : 1842
Records identified (other sources)    : 47
Duplicates removed                    : 318
Records screened (title/abstract)     : 1571
Excluded at title/abstract            : 1289
Full-text assessed                    : 282
Full-text excluded total              : 182
  - did not manipulate AL             : 71
  - no physiological/neural outcome   : 38
  - review without primary data       : 26
  - non-English                       : 5
  - duplicate sample                  : 6
  - insufficient data for ES          : 36
Included in synthesis                 : 100
  Neuroimaging/neurostim              : 42
  Psychophysiology (meta-analysis)    : 9
  Behavioral/self-report              : 28
  Clinical & patient populations      : 12
  Existing meta-analyses              : 9
```

## Internal consistency

Every count is verified arithmetically by `build_prisma.py`:

- `records_screened == identified_databases + identified_other_sources − duplicates_removed`
- `full_text_assessed == records_screened − records_excluded_at_ti_ab`
- `full_text_excluded == sum of the 6 specific exclusion reasons`
- `total included == full_text_assessed − full_text_excluded == sum of the 5 synthesis subsets`

Any future change to a single count that breaks one of these assertions causes `build_prisma.py` to fail loudly.

## How to re-run

```bash
python prisma/build_prisma.py
```

Regenerates `prisma_counts.txt`, `figures/prisma_flow.png`, and `figures/prisma_flow.pdf`. Byte-identical reruns on the pinned environment.

## License

Code (`build_prisma.py`): MIT. Data (`prisma_counts.csv`, `prisma_counts.txt`): CC-BY-4.0. Documentation (`PRISMA_2020_checklist.md`, this README): CC-BY-4.0.
