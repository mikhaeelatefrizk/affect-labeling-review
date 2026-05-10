# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

For any release, the canonical archive of record is the corresponding Zenodo deposit; the concept DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595) always resolves to the latest version.

---

## [v1.0.0] — 2026-05-10

First reproducibility-complete release. The manuscript, data, code, and tooling form a self-contained open-research package.

### Manuscript and pre-registration

- **Added.** Full ~14,000-word manuscript at `manuscript/manuscript.md`, with structured Abstract, IMRaD body, Limitations, Future directions, Conclusion, Figures, Supplementary materials index, Data and Code Availability, and References.
- **Added.** PROSPERO-compatible structured pre-registration at `prereg/PROSPERO_preregistration.md`, with all 30 sections fully populated. Single-coder execution deviation from two-reviewer protocol documented honestly in §5, §19, §20.

### Reproducibility infrastructure

- **Added.** `Makefile` with targets `install` / `analysis` / `prisma` / `rob` / `figures` / `derive` / `quality` / `validate` / `all` / `verify` / `sha` / `clean`.
- **Added.** Pinned-version `requirements.txt` (Python 3.11 + numpy 1.26.4 + pandas 2.1.4 + scipy 1.11.4 + matplotlib 3.8.2 + requests 2.31.0 + bibtexparser 1.4.1 + jsonschema 4.20.0 + frictionless 5.16.0).
- **Added.** Conda alternative `environment.yml` mirroring `requirements.txt`.
- **Added.** GitHub Actions CI workflow at `.github/workflows/ci.yml` — currently disabled on auto-trigger pending account-level billing-flag resolution by GitHub Support; workflow body is fully tested locally and re-enabled by uncommenting two lines.

### Data layer (CC-BY-4.0)

- **Added.** Structured machine-readable PRISMA counts at `prisma/prisma_counts.csv` (19 rows, single source of truth for every flow number cited in the manuscript). Internal arithmetic consistency asserted by `prisma/build_prisma.py`.
- **Added.** PRISMA-S compliant search strategy report at `data/searches/search_strategy.md` + `.csv`.
- **Added.** Exclusion-reason codebook at `data/exclusion_reason_codebook.md` defining the 6 full-text exclusion codes plus 4 broader title/abstract codes.
- **Added.** JSON Schema 2020-12 specification for the screening log at `data/screening/screening_log.schema.json`. Validates with `jsonschema` or `frictionless`.
- **Added.** Empty template `data/screening/screening_log.template.csv` with one example row, ready for second-coder re-screening.
- **Added.** Canonical-identifiable included-papers CSV at `data/screening/included_papers.csv`, enumerating 22 of 100 included studies with subset assignments. (78 of 100 are cited in manuscript prose without per-paper structure; documented as a known limitation.)
- **Added.** Derived PubMed corpus at `data/screening/derived_corpus.csv`, regenerated from the pre-registered query (n = 3,892).
- **Added.** Derived labelled screening log at `data/screening/derived_screening_log.csv`, joining the corpus against the included list (positive-unlabelled framing; 14 confirmed positives).
- **Added.** Auto-generated quality report at `data/QUALITY_REPORT.md` documenting canonical vs. derived counts, year and journal distributions, recall of canonical includes in the PubMed re-query, and class balance.

### Tooling

- **Added.** `scripts/extract_included_list.py` — emits `included_papers.csv` from analysis code + bibtex.
- **Added.** `scripts/build_derived_corpus.py` — queries PubMed E-utilities; emits `derived_corpus.csv`.
- **Added.** `scripts/build_derived_screening_log.py` — joins corpus with includes; emits `derived_screening_log.csv`.
- **Added.** `scripts/build_quality_report.py` — emits `data/QUALITY_REPORT.md`.
- **Added.** `scripts/validate_screening_log.py` — schema validation + reconciliation with canonical PRISMA counts.
- **Refactored.** `prisma/build_prisma.py` to read counts from `prisma_counts.csv` instead of hardcoding (single source of truth principle).

### Reporting standards

- **Added.** PRISMA 2020 27-item checklist at `prisma/PRISMA_2020_checklist.md` with per-item pointers. All 42 sub-items reported.
- **Added.** PRISMA-S 16-item search-reporting checklist at `data/searches/PRISMA-S_checklist.md`.
- **Added.** Per-study risk-of-bias rationale at `supplementary/risk_of_bias_explanation.md` — narrative justification for every domain code in the CSV.

### Documentation (`docs/`)

- **Added.** `docs/README.md` — table of contents and audience-specific reading orders.
- **Added.** `docs/reproducibility-guide.md` — step-by-step from clone to byte-identical outputs, on Linux/macOS/Windows, with a containerised option.
- **Added.** `docs/for-ml-researchers.md` — extended guide for ML / NLP researchers building SLR screening models on this corpus, with PU-learning recommendations and evaluation protocol.
- **Added.** `docs/methodology-deep-dive.md` — analytic-choice justifications (Hedges' *g*, DerSimonian-Laird τ², lab-stratified moderator, three RoB tools, GRADE simplification).
- **Added.** `docs/glossary.md` — plain-language definitions for ~50 SLR / meta-analysis / ML terms.
- **Added.** `docs/troubleshooting.md` — top 10 reproducer issues with concrete fixes.
- **Added.** `docs/extending-the-corpus.md` — how to contribute a second-coder pass, broaden database coverage, add a study, run new analyses.

### Per-folder READMEs

- **Added.** Substantive READMEs in `manuscript/`, `prereg/`, `meta-analysis/`, `prisma/`, `supplementary/`, `figures/`, `scripts/` — each describes the directory's contents, regeneration command, license, and relationship to the rest of the package.

### Citation, archiving, identity

- **Added.** Machine-readable `CITATION.cff` (CFF v1.2.0) with concept DOI, ORCID, affiliation, and preferred-citation block.
- **Added.** Zenodo deposit metadata at `.zenodo.json` for automated DOI minting.
- **Permanent archive.** v1.0.0 deposited on Zenodo with concept DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595) (resolves to latest) and version DOI 10.5281/zenodo.20109596.
- **Author ORCID.** [0009-0006-1069-9558](https://orcid.org/0009-0006-1069-9558) plumbed through `CITATION.cff`, `.zenodo.json`, README badge, and Contact section.

### Licensing

- **Added.** Three-license split: `LICENSE-CODE` (MIT, source files), `LICENSE-MANUSCRIPT` (CC-BY-4.0, manuscript and figures), `LICENSE-DATA` (CC-BY-4.0, all data files). The top-level `LICENSE` is the multi-license pointer.

### Community infrastructure

- **Added.** `CONTRIBUTING.md` describing how to report errata, propose corrections, raise reproducibility issues, contribute a second-coder pass.
- **Added.** `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1).
- **Added.** Structured GitHub issue templates: `erratum.yml`, `data_correction.yml`, `reproducibility.yml`, plus `config.yml` for external-link discoverability.
- **Added.** Pull-request template at `.github/PULL_REQUEST_TEMPLATE.md`.
- **Added.** `SECURITY.md` describing the (academic-repo-appropriate) vulnerability-disclosure expectations.
- **Added.** `.editorconfig` for consistent code-style across editors.

### Notes on this release

- Single-coder execution: screening and data extraction were carried out by one reviewer rather than the two specified in the protocol. Inter-rater agreement statistics are therefore not available. This deviation is documented in three places (`prereg/PROSPERO_preregistration.md` §19/§20, `manuscript/manuscript.md` §4.6, `data/screening/README.md`).
- The derived screening log is positive-unlabelled (PU): 14 confirmed positives matched against canonical includes by DOI or title-fuzzy; ~3,800 unlabelled with ~2% upper-bound noise rate from unidentified canonical includes. ML researchers using the corpus should use PU-aware methods or report metrics over the verified-positive subset only.
- The CI workflow auto-trigger is temporarily disabled because the account-level billing flag prevents Actions from running. The workflow body itself is correct and reproduces locally; re-enable by uncommenting two lines in `.github/workflows/ci.yml` once the billing flag is lifted.

---

## [Unreleased]

Roadmap items welcomed as PRs (see [`docs/extending-the-corpus.md`](docs/extending-the-corpus.md)):

- Second independent coder screening pass (highest-value contribution).
- Database coverage broadening (PsycINFO, Web of Science, Scopus, Cochrane).
- Filling in the 78 unidentified canonical includes to bring `included_papers.csv` from 22/100 to 100/100.
- Bayesian random-effects sensitivity analysis.
- Multi-level random-effects modelling of within-study dependence.
- CLEF eHealth TAR benchmark wrapping for direct comparability with other published SLR ML benchmarks.

---

[v1.0.0]: https://github.com/mikhaeelatefrizk/affect-labeling-review/releases/tag/v1.0.0
