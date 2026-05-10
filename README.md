# Putting feelings into words: a systematic review and meta-analysis of affect labeling

[![License: code MIT](https://img.shields.io/badge/code-MIT-blue.svg)](LICENSE-CODE)
[![License: manuscript CC-BY-4.0](https://img.shields.io/badge/manuscript-CC--BY--4.0-lightgrey.svg)](LICENSE-MANUSCRIPT)
[![License: data CC-BY-4.0](https://img.shields.io/badge/data-CC--BY--4.0-lightgrey.svg)](LICENSE-DATA)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20109595.svg)](https://doi.org/10.5281/zenodo.20109595)
[![Cite this repository](https://img.shields.io/badge/cite-CITATION.cff-green.svg)](CITATION.cff)
[![ORCID](https://img.shields.io/badge/ORCID-0009--0006--1069--9558-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0006-1069-9558)

This repository is the full open-research package for a pre-registered (PROSPERO) systematic review and random-effects meta-analysis of **affect labeling** — the psychological and neuroscientific phenomenon, originating in Lieberman et al. (2007), in which putting feelings into words attenuates emotional responses.

> **Status: Preprint / working paper. Not yet peer-reviewed.** All findings are provisional and subject to revision pending external review.

## Headline result

Random-effects meta-analysis of nine peripheral-physiology effect sizes from seven independent studies:

- **Pooled Hedges' g = −0.43, 95% CI [−0.68, −0.18], p < .001**
- 95% prediction interval [−1.13, +0.27] **crosses zero**
- I² = 48.3%, τ² = 0.070

Pre-specified lab-stratified moderator analysis:

- **UCLA Lieberman/Craske axis only:** g = **−0.74**, 95% CI [−1.02, −0.47], k = 5, I² = 0%
- **Independent laboratories only:** g = **−0.13**, 95% CI [−0.41, +0.14], k = 4, I² = 27.8% — non-significant; CI crosses zero

The 0.61 g-unit gap between lab strata is larger than most moderators in the published literature and is consistent with structural author non-independence rather than incidental variation.

## For data scientists and ML researchers

The screening corpus is published as a labeled dataset suitable for training and evaluating AI-assisted SLR screening systems (see [`data/screening/`](data/screening/)). Quick orientation:

| You want… | File | Note |
|-----------|------|------|
| The 100 included papers (positive class) | `data/screening/included_papers.csv` | Generated from `references.bib` + manuscript |
| The candidate corpus (~1,800 papers) with `included` 0/1 labels | `data/screening/derived_screening_log.csv` | **The training file.** Re-derived from PubMed using the pre-registered query |
| The pre-registered query and search strategy | [`data/searches/search_strategy.md`](data/searches/search_strategy.md) | PRISMA-S compliant |
| The exclusion-reason taxonomy | [`data/exclusion_reason_codebook.md`](data/exclusion_reason_codebook.md) | The 6 full-text exclusion codes used in the original review |
| Aggregate PRISMA counts | [`prisma/prisma_counts.csv`](prisma/prisma_counts.csv) | Structured form of the published flow |

**Important honesty up front.** The derived screening log is a *re-derivation*, not the original per-paper screening record (which was not preserved in shareable form). It collapses the title/abstract vs. full-text decision distinction into a single binary label, and exclusion reasons are aggregated rather than per-paper. See [`data/screening/README.md`](data/screening/README.md) for the full caveats.

## Data Availability

All data needed to reproduce, re-analyze, or extend this review is in this repository under [`LICENSE-DATA`](LICENSE-DATA) (CC-BY-4.0). No external archive is currently used; the [`.zenodo.json`](.zenodo.json) configures a DOI mint on the next tagged release.

| Layer | Where | Source of truth? |
|-------|-------|------------------|
| Manuscript and figures | `manuscript/`, `figures/` | Yes |
| Pre-registration | `prereg/PROSPERO_preregistration.md` | Yes (canonical inclusion/exclusion criteria) |
| PRISMA flow and counts | `prisma/prisma_counts.csv` (structured), `prisma/prisma_counts.txt` (legacy) | Yes |
| Effect sizes | `meta-analysis/extracted_effect_sizes.csv` | Yes |
| Risk-of-bias assessments | `supplementary/risk_of_bias.csv` | Yes |
| Search strategy | `data/searches/` | Yes (restructured from PROSPERO) |
| Included papers list | `data/screening/included_papers.csv` | Derived from `references.bib` + manuscript |
| Candidate corpus + labels | `data/screening/derived_screening_log.csv` | Derived from PubMed re-query |

**What is *not* available.** The original per-paper screening decisions (1,571 title/abstract decisions and 282 full-text decisions) were not preserved in a shareable form. Derived labels are the closest reproducible substitute. See [`data/screening/README.md`](data/screening/README.md).

## Documentation guide

This repository ships with extended documentation under [`docs/`](docs/) for readers who want to *use* the package — not just cite it. Pick your path:

| You are… | Start here |
|---|---|
| A reader who wants the gist | [`README.md`](README.md) (this file) → [`manuscript/manuscript.md`](manuscript/manuscript.md) |
| A peer reviewer or thesis committee | [`prisma/PRISMA_2020_checklist.md`](prisma/PRISMA_2020_checklist.md) → [`supplementary/risk_of_bias_explanation.md`](supplementary/risk_of_bias_explanation.md) → [`docs/methodology-deep-dive.md`](docs/methodology-deep-dive.md) |
| A reproducer | [`docs/reproducibility-guide.md`](docs/reproducibility-guide.md) → run `make all` → [`docs/troubleshooting.md`](docs/troubleshooting.md) if anything fails |
| An ML / NLP researcher building a screening model | [`docs/for-ml-researchers.md`](docs/for-ml-researchers.md) → [`data/screening/derived_screening_log.csv`](data/screening/derived_screening_log.csv) |
| A master's student building an AI screening pipeline | [`docs/for-masters-students.md`](docs/for-masters-students.md) → [`docs/for-ml-researchers.md`](docs/for-ml-researchers.md) |
| Someone unfamiliar with SLR terminology | [`docs/glossary.md`](docs/glossary.md) (5 minutes) |
| Someone wanting to contribute back | [`docs/extending-the-corpus.md`](docs/extending-the-corpus.md) → [`CONTRIBUTING.md`](CONTRIBUTING.md) |
| A search-strategy peer reviewer | [`data/searches/PRISMA-S_checklist.md`](data/searches/PRISMA-S_checklist.md) |

## Repository structure

```
affect-labeling-review/
├── README.md                              ← this file
├── CHANGELOG.md                           ← versioned change history
├── LICENSE                                ← multi-license pointer
├── LICENSE-CODE                           ← MIT (source files)
├── LICENSE-MANUSCRIPT                     ← CC-BY-4.0 (manuscript + figures)
├── LICENSE-DATA                           ← CC-BY-4.0 (data files)
├── CITATION.cff                           ← machine-readable citation
├── .zenodo.json                           ← DOI metadata (Zenodo)
├── CONTRIBUTING.md                        ← how to report errata, propose corrections
├── CODE_OF_CONDUCT.md                     ← Contributor Covenant 2.1
├── SECURITY.md                            ← vulnerability disclosure policy
├── .editorconfig                          ← cross-editor code-style consistency
├── Makefile                               ← reproducibility entry point — run `make all`
├── requirements.txt                       ← pinned Python deps
├── environment.yml                        ← conda alternative
├── references.bib                         ← BibTeX for all references
│
├── manuscript/                            ← the manuscript and its README
│   └── manuscript.md                      ← full ~14,000-word paper
│
├── prereg/                                ← pre-registration
│   └── PROSPERO_preregistration.md        ← PROSPERO-compatible structured protocol
│
├── meta-analysis/                         ← random-effects meta-analysis
│   ├── run_meta_analysis.py               ← analysis code
│   ├── extracted_effect_sizes.csv         ← effect-size dataset (canonical)
│   ├── leave_one_out.csv                  ← LOO sensitivity output
│   └── results_summary.txt                ← plain-text summary
│
├── prisma/                                ← PRISMA 2020 flow + reporting
│   ├── build_prisma.py                    ← PRISMA flow generator
│   ├── prisma_counts.csv                  ← structured counts (canonical)
│   ├── prisma_counts.txt                  ← legacy human-readable counts
│   └── PRISMA_2020_checklist.md           ← 27-item reporting checklist
│
├── supplementary/                         ← risk-of-bias artifacts
│   ├── risk_of_bias.csv                   ← RoB 2 / ROBINS-I judgments
│   ├── build_rob_figure.py                ← traffic-light figure code
│   └── risk_of_bias_explanation.md        ← per-study rationale narrative
│
├── data/                                  ← labeled datasets (CC-BY-4.0)
│   ├── README.md                          ← dataset index + data dictionary
│   ├── exclusion_reason_codebook.md       ← 6 full-text exclusion codes
│   ├── QUALITY_REPORT.md                  ← canonical-vs-derived comparison
│   ├── searches/                          ← PRISMA-S search strategy
│   │   ├── search_strategy.md/.csv        ← canonical query, dates, hits
│   │   └── PRISMA-S_checklist.md          ← 16-item search-reporting checklist
│   └── screening/                         ← screening log (schema, template, derived)
│       ├── screening_log.schema.json      ← JSON Schema 2020-12
│       ├── screening_log.template.csv     ← empty template + 1 example row
│       ├── included_papers.csv            ← 22 canonical-identifiable includes
│       ├── derived_corpus.csv             ← 3,892 PubMed-derived records
│       └── derived_screening_log.csv      ← labelled corpus (PU framing)
│
├── scripts/                               ← derivation + validation tooling
│   ├── extract_included_list.py           ← parse references.bib → included_papers.csv
│   ├── build_derived_corpus.py            ← re-query PubMed → derived_corpus.csv
│   ├── build_derived_screening_log.py     ← join → derived_screening_log.csv
│   ├── build_quality_report.py            ← QUALITY_REPORT.md
│   └── validate_screening_log.py          ← schema + reconciliation check
│
├── docs/                                  ← extended documentation for reproducers and reusers
│   ├── README.md                          ← reading orders + table of contents
│   ├── reproducibility-guide.md           ← clone → byte-identical outputs
│   ├── for-ml-researchers.md              ← detailed PU-learning guide
│   ├── for-masters-students.md            ← concrete onboarding letter for ML-screening thesis work
│   ├── methodology-deep-dive.md           ← analytic-choice justifications
│   ├── glossary.md                        ← ~50 SLR / meta-analysis / ML terms
│   ├── troubleshooting.md                 ← top 10 reproducer issues + fixes
│   └── extending-the-corpus.md            ← second-coder + database-broadening guide
│
├── figures/                               ← rendered outputs (PNG + PDF)
│   ├── prisma_flow.png / .pdf             ← PRISMA 2020 flow diagram
│   ├── rob_summary.png / .pdf             ← risk-of-bias traffic light
│   ├── forest_plot.png / .pdf             ← random-effects forest plot
│   └── funnel_plot.png / .pdf             ← funnel plot
│
└── .github/
    ├── workflows/ci.yml                   ← reproducibility CI (auto-trigger temporarily off; see CHANGELOG)
    ├── ISSUE_TEMPLATE/                    ← erratum, repro, data-correction forms
    └── PULL_REQUEST_TEMPLATE.md
```

Every directory has a `README.md` orienting you to its contents and regeneration command.

## Reproducing the analyses

```bash
git clone https://github.com/mikhaeelatefrizk/affect-labeling-review.git
cd affect-labeling-review
make install       # pinned Python deps (Python 3.11)
make all           # regenerate every output: figures, counts, derived dataset
make verify        # assert outputs match the committed versions
```

Without `make` (Windows without WSL):

```powershell
pip install -r requirements.txt
python meta-analysis/run_meta_analysis.py
python prisma/build_prisma.py
python supplementary/build_rob_figure.py
python scripts/extract_included_list.py
python scripts/build_derived_corpus.py
python scripts/build_derived_screening_log.py
python scripts/build_quality_report.py
python scripts/validate_screening_log.py
```

`make all` from a fresh clone with the pinned dependency set (Python 3.11.x, see [`requirements.txt`](requirements.txt)) reproduces every output byte-for-byte. Drift on a different version stack is reported but not necessarily an error — see [`Makefile`](Makefile) target `sha` for a SHA-256 receipt.

## Re-deriving the screening corpus

`make derive` re-queries PubMed via the NCBI E-utilities API using the pre-registered Boolean query, fetches each candidate's metadata, joins against the included-papers list, and writes the labeled corpus to `data/screening/derived_screening_log.csv`. The whole derivation is deterministic given a PubMed snapshot.

Because PubMed continues to grow, today's hit count will exceed the canonical 1,842 records reported in the original PRISMA flow. This drift is reported in [`data/QUALITY_REPORT.md`](data/QUALITY_REPORT.md) (regenerated by `make quality`) and is informational, not error.

## What's verified, what's flagged

The reference list was verified against PubMed, the journal of record, and where available the original published PDFs. **Five citations were corrected** during verification, and **one fabricated reference was removed**:

- Removed: Isaacowitz & Eldesouky (2024) — could not be located in any database; closest real entity is a 2023 conference symposium.
- Corrected: "Wong et al. (2022)" → Plaisted, Waite, & Creswell (2022), *Behaviour Research and Therapy*, 148, 103997. This is a key **null finding** and the only adequately powered adolescent RCT.
- Corrected: Vlasenko et al. (2021) coauthors → Vlasenko, V. V., Rogers, E. G., & Waugh, C. E. (Wake Forest).
- Corrected: Vives et al. (2021) title → "Foreign Language Processing Undermines Affect Labeling."
- Corrected: Givon, Meiran, & Goldenberg (2025) for the *Trends in Cognitive Sciences* piece (was misattributed).
- Several DOIs and article numbers corrected.

The Burklund et al. (2024) PTSD pilot trial is flagged for a **commercial conflict of interest**: the lead author is an independent contractor at NeuroGen Technologies Inc., a private company developing affect-labeling-based PTSD interventions. This disclosure is also reflected in the risk-of-bias assessment as "high."

## Limitations explicitly acknowledged in the manuscript

1. Many original fMRI studies did not report d or g, precluding fully harmonized quantitative synthesis without re-analysis of original data.
2. Single-laboratory concentration in the affect labeling fMRI literature limits independence of the supportive evidence base; addressed by lab-stratified moderator analysis but the underlying problem requires direct multisite replication.
3. The dissociation between physiological and self-report measures means effect-size estimates depend on outcome choice in ways flagged but not fully resolved.
4. The meta-analysis includes nine effect sizes from seven studies — adequate for detecting a moderate pooled effect but underpowered for many moderator analyses.
5. Inclusion criteria excluded studies in non-English without translation.
6. **Screening was performed by a single coder.** Inter-rater agreement statistics are not available. The derived screening log (`data/screening/derived_screening_log.csv`) reproduces a binary label per paper from public sources, but the original per-paper screening decisions and exclusion reasons were not preserved.

## How to cite

The canonical citation is in [`CITATION.cff`](CITATION.cff) (machine-readable). Plain text:

```
Wahba, M. A. R. (2026). Putting feelings into words: A systematic review
and meta-analysis of affect labeling (v1.0.0).
Zenodo. https://doi.org/10.5281/zenodo.20109595
```

The repository has a permanent Zenodo DOI: [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595). GitHub also renders a "Cite this repository" button on the project page using `CITATION.cff`.

## License

Three licenses by content category:

- **Code** (`*.py`, `Makefile`, CI configs, schemas): MIT — see [`LICENSE-CODE`](LICENSE-CODE).
- **Manuscript and figures**: CC-BY-4.0 — see [`LICENSE-MANUSCRIPT`](LICENSE-MANUSCRIPT).
- **Data files**: CC-BY-4.0 — see [`LICENSE-DATA`](LICENSE-DATA).

See [`LICENSE`](LICENSE) for the at-a-glance map.

## Contributing

Errata, reproducibility issues, and data corrections are welcome. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the workflow and the issue templates under [`.github/ISSUE_TEMPLATE/`](.github/ISSUE_TEMPLATE/).

## Contact

Open an issue on this repository, or use the email in [`CITATION.cff`](CITATION.cff) for matters that aren't suitable for a public issue. ORCID: [0009-0006-1069-9558](https://orcid.org/0009-0006-1069-9558).
