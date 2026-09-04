# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

For any release, the canonical archive of record is the corresponding Zenodo deposit; the concept DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595) always resolves to the latest version.

---

## [v1.1.0] — 2026-09-04

**Analytic numbers changed.** This is the first release in which the meta-analytic
results differ from v1.0.0. Three of the nine effect sizes were not extracted values,
the methods text said they were, and correcting them moves the headline. If you have
cited the v1.0.x figures, cite these instead.

| | v1.0.1 | v1.1.0 |
|---|---|---|
| Effect sizes (studies) | 9 (7) | 8 (6) |
| Pooled Hedges' *g* | −0.43 [−0.68, −0.18] | **−0.49 [−0.73, −0.26]** |
| Heterogeneity | Q(8) = 15.48, I² = 48.3%, τ² = 0.070 | Q(7) = 10.96, I² = 36.2%, τ² = 0.040 |
| 95% prediction interval | [−1.13, +0.27] | [−1.07, +0.08] |
| UCLA axis | −0.74 [−1.02, −0.47], k = 5 | −0.74 [−1.02, −0.47], k = 5 (unchanged) |
| Independent labs | −0.13 [−0.41, +0.14], k = 4 | **−0.23 [−0.51, +0.05], k = 3** |
| Lab-stratified gap | 0.61 | **0.52** |
| Egger's test | −4.55, p = .164 (n.s.) | **−4.33, p = .047 (significant)** |

### Fixed

- **Three effect sizes were imputed, not extracted.** Plaisted (2022), McRae (2010)
  and Fitzpatrick (2019) carried round stand-in values (*d* = 0.00, +0.10, −0.10)
  encoding "the report describes a null result", while `run_meta_analysis.py` stated
  that values were "extracted from published reports" and manuscript §3.3 said "we
  extracted". Those three carried roughly 70% of the fixed-effect weight of the
  independent-laboratory stratum — the stratum that produces the review's
  lab-stratified headline. Resolved as follows.
- **Plaisted (2022): 0.00 → −0.220, *n* 20/20 → 27/27.** Extracted from the Table 2
  heart-rate descriptives (post-speech recovery HR at one-week follow-up, 90.2 (9.4)
  vs. 92.2 (8.8)). The recovery window matches Niles (2015) so the strata stay
  comparable. The trial is three-arm, *N* = 81. The arms are unbalanced at pre-test,
  so the change score gives −0.49; that is recorded as a sensitivity analysis because
  its standard error needs a pre-post correlation the paper does not report.
- **Fitzpatrick (2019): −0.10 → −0.036, *n* 15/15 → 30 within-subject.** Extracted
  from the Table 3 healthy-control descriptives averaged over the two script types
  (3.095 vs. 3.205, pooled *SD* 3.020). The paper reports no healthy-control-only
  inferential test for skin conductance. SCR there is an overdispersed count modelled
  with a negative-binomial GEE, so an SMD on the descriptives is a crude summary.
- **McRae (2010): dropped.** Closed access with no repository copy, so no statistic
  could be recovered, and the contrast as coded ("subjective AL vs. passive") appears
  not to exist in the paper: the design compares subjective against *objective*
  labelling across four exposure durations and reports an interaction. Documented as
  an exclusion rather than estimated. Reinstatable if the full text is obtained.
- **Egger's test now crosses significance** (p = .047, was p = .164). This is a direct
  consequence of the above and is reported as such: small-study or publication bias is
  now a live concern rather than a suspicion. Egger's test is underpowered at k = 8 and
  should corroborate the lab-stratified pattern, not stand alone.
- **McRae (2010) citation was wrong.** The recorded title, "The effects of objective
  and subjective emotion labels on emotional response", does not exist. The real title
  is "The effects of verbal labelling on psychophysiology: Objective but not subjective
  emotion labelling reduces skin-conductance responses to briefly presented pictures"
  (verified against Crossref). Second author corrected to E. Keolani Taitano; the
  affiliation label "Tucson/Geneva" corrected to Arizona/Stanford — there is no Geneva
  affiliation.
- **Fitzpatrick (2019) authors corrected** to Jennifer Ip and Lillian Krantz (were
  "Jenny" and "Lauren"), verified against Crossref.
- **Plaisted lab label** corrected from "Oxford" to Birmingham/Reading/Oxford. The
  acknowledgements thank M. Craske, which bears on the lab-independence moderator and
  is now noted in the study record.
- **Risk-of-bias, Plaisted row.** The `key_concerns` field cited pre-registration as a
  basis for the domain-5 rating. No registration number, OSF link or pre-registration
  statement could be found in the accepted manuscript or the Europe PMC record, so
  that basis is withdrawn pending confirmation.
- **README claims.** Removed "pre-registered (PROSPERO)" (the protocol was written to
  the CRD template but never submitted, as `prereg/` already stated); corrected "the
  100 included papers" to the 22 the file actually contains; relabelled the screening
  corpus as positive-unlabelled (14 positives, no negative class) rather than a 0/1
  training file; and removed "No external archive is currently used", which
  contradicted the Zenodo DOI cited later in the same file.

### Added

- **`derivation` column** in `run_meta_analysis.py` and the derived
  `extracted_effect_sizes.csv`, valued `extracted` for every current row. The field
  exists so that any future imputed value has to declare itself rather than being
  indistinguishable from an extracted one.

### Changed

- **`environment.yml`** pinned `jsonschema=4.20.0` while frictionless 5.16.0 requires
  `jsonschema<4.18` (verified against PyPI metadata), making the documented conda path
  unsatisfiable. Pinned to 4.17.3 to match `requirements.txt`.

### Removed

- **`scripts/__init__.py`** — empty and imported by nothing.

---

## [v1.0.1] — 2026-05-11

Honesty + reproducibility pass on top of v1.0.0. No analytic numbers changed; the meta-analytic results, PRISMA stage counts, and risk-of-bias judgments are identical to v1.0.0. The changes correct internal inconsistencies, populate placeholders, and improve discoverability of common questions for re-users of the dataset.

### Fixed

- **Manuscript YAML frontmatter.** Replaced `[Lead Author], [Affiliation]` and `[Coauthor], [Affiliation]` placeholders with the real single-author block (Mikhaeel Atef Rizk Wahba, Independent researcher, ORCID 0009-0006-1069-9558). Source of truth for authorship is now consistent across `manuscript/manuscript.md`, `CITATION.cff`, and `.zenodo.json`.
- **Manuscript §2.4 (Selection process).** The previous text reported "Two reviewers screened titles, abstracts, and full texts independently. Inter-rater agreement was Cohen's κ = 0.81 at the title/abstract level and κ = 0.87 at full text." This contradicted the truthful admission in §2.1 that screening was carried out by a single reviewer. The two κ statistics were aspirational protocol text that was never updated after execution; they have been removed. §2.4 now mirrors the structure used in `prereg/PROSPERO_preregistration.md` §19, distinguishing pre-registered intent from actual execution.
- **Manuscript §3.1.** Changed "9 studies in the quantitative meta-analysis of peripheral physiology" to "9 effect-size contributions from 7 unique studies in the quantitative meta-analysis of peripheral physiology (Kircanski 2012 contributes 3 comparator contrasts; the other 6 studies each contribute one effect size)" to remove ambiguity with §3.3's correct "nine effect sizes from seven independent studies".
- **`prisma/prisma_counts.csv`.** Added a clarifying note to the `description` column for `subset_psychophysiology_meta_analysis = 9` explaining that the value counts effect-size contributions, not unique papers. The aggregate of 100 is unchanged.
- **`CITATION.cff` abstract** and **`.zenodo.json` description**. Removed the unqualified phrase "pre-registered (PROSPERO)" — both files now state that the PROSPERO-compatible structured protocol is included in the repository but was *not* formally submitted to the PROSPERO registry. Both also now mention the single-coder deviation explicitly, matching the disclosure in the manuscript Abstract.

### Added

- **`docs/faq.md`** — concise direct answers to the most common reader questions: year filter used in the searches, where the per-paper included list lives (and why only 22 of 100 are unambiguously enumerable), how to label a re-run corpus using `included_papers.csv` + `all_references.csv`, license, citation, single-coder rationale, PubMed drift. Wired into the documentation table at the top of the main `README.md` and at the top of `docs/README.md`.
- **`docs/for-masters-students.md`** — concrete onboarding letter for ML-thesis readers re-using the dataset for AI-assisted SLR screening. Three labeling strategies with worked guidance.
- **`data/screening/all_references.csv`** — every entry from `references.bib` (86 rows) as a structured CSV with `bibtex_key`, `title`, `authors`, `first_author_surname`, `year`, `journal`, `doi`, `entry_type`, `is_confirmed_include` (1/0), `include_subset`, and `manuscript_mentions` (deterministic count of how often the reference is cited in `manuscript/manuscript.md`). Generated by `scripts/build_all_references.py`.
- **`scripts/build_all_references.py`** — the deterministic builder for the above. Parses `references.bib`, joins with `included_papers.csv`, counts manuscript-prose mentions via word-boundary `<Surname>` ... `<Year>` co-occurrence within a 120-character window. Self-documenting; the file's docstring explains what the `manuscript_mentions` count is and isn't.

### Documentation discoverability

- **Promoted the year-filter answer to top-of-file** in `data/searches/README.md` and `data/screening/README.md`. Previously, "no year filter; from-inception search; final window Q1–Q2 2026" was correctly recorded in `data/searches/search_strategy.md` but was hard to find without grepping. Each of those READMEs now opens with a callout block summarising the answer.
- **Corrected `data/screening/README.md`**'s previous claim that `included_papers.csv` lists "100 included papers"; it lists 22 of 100. The 22-vs-100 reality, and the workflow to bridge the gap with `all_references.csv`, are now explained explicitly in a new "Why 22 and not 100" section.
- **Updated `data/README.md`** file index to include `all_references.csv` and re-state the 22-of-100 framing.
- **Updated `docs/README.md`** to list `faq.md` first (highest-leverage starting point for most readers) and to include `for-masters-students.md`.
- **Updated the main `README.md`** Documentation guide table and Repository structure tree to include both new doc files and `all_references.csv`.

### Infrastructure

- **`.gitignore`**: added `exports/` so per-recipient outgoing-bundle workspaces (e.g. exported zips for collaborators) stay local and never land on origin.

### Reproducibility note

All output files (`included_papers.csv`, `all_references.csv`, figures, results summary) were regenerated from source after the manuscript edits. The only data change in `all_references.csv` was `kircanski2012`'s `manuscript_mentions` count rising from 15 to 16 — directly attributable to the new clarifying sentence added in §3.1 that explicitly names Kircanski 2012's three contributions. Effect-size CSV, RoB table, and PRISMA counts are byte-identical to v1.0.0.

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
