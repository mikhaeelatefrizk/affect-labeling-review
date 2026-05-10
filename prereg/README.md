# `prereg/`

The pre-registered protocol for the systematic review and meta-analysis.

## Contents

- [`PROSPERO_preregistration.md`](PROSPERO_preregistration.md) — full PROSPERO-compatible structured pre-registration in CRD-template format. 30 sections covering review questions, eligibility criteria, search strategy, selection process, extraction template, risk-of-bias methods, synthesis methods, dissemination plans, and final-report identifiers.

## Status

The protocol was authored using the PROSPERO CRD template but **was not formally submitted to the PROSPERO registry**. The completed review and full open-research package are permanently archived on Zenodo with concept DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595).

The document is updated post-completion (header reflects this): every "to be assigned" / "to be completed" placeholder has been replaced with a real value, and one execution deviation from the original protocol is documented honestly: screening and extraction were carried out by a single reviewer rather than the two-reviewer scheme originally specified.

## Why pre-registration matters

Pre-registration in the PROSPERO style or equivalent does three things:

1. **Locks in the eligibility criteria** before the screener sees the search results, removing the temptation to re-write criteria to match desired conclusions.
2. **Locks in the analytic plan** before the data are seen, distinguishing pre-specified from exploratory analyses.
3. **Creates a public commitment** that the review will be carried out in a particular way, which other researchers can hold the team to.

The execution deviation (single coder rather than two) is documented in three places: this file's Section 19 / 20, the manuscript's Limitations section, and `data/screening/README.md`. This is consistent with how the systematic-review methodology community handles necessary protocol deviations.

## How this file relates to the rest of the package

| Pre-registration section | Realised in |
|---|---|
| §6 Review questions | Manuscript §1 (final paragraph) |
| §7 Searches | [`data/searches/search_strategy.md`](../data/searches/search_strategy.md) |
| §10–13 Eligibility | [`data/exclusion_reason_codebook.md`](../data/exclusion_reason_codebook.md), Manuscript §2.2 |
| §15 Main outcome | Manuscript §3.3, [`meta-analysis/results_summary.txt`](../meta-analysis/results_summary.txt) |
| §19 Selection process | [`prisma/prisma_counts.csv`](../prisma/prisma_counts.csv) (aggregate); [`data/screening/derived_screening_log.csv`](../data/screening/derived_screening_log.csv) (derived per-record) |
| §21 Risk of bias | [`supplementary/risk_of_bias.csv`](../supplementary/risk_of_bias.csv) + [`supplementary/risk_of_bias_explanation.md`](../supplementary/risk_of_bias_explanation.md) |
| §22 Synthesis methods | [`meta-analysis/run_meta_analysis.py`](../meta-analysis/run_meta_analysis.py) |

## License

CC-BY-4.0. See [`LICENSE-MANUSCRIPT`](../LICENSE-MANUSCRIPT).
