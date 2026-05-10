# Extending the corpus

How to contribute back to the open-research package — by adding a second-coder pass, broadening the database coverage, or adding a study that should have been included. Welcomed as PRs and issues.

---

## A. Second-coder screening pass — the most valuable addition

The single highest-value contribution to this package would be a second independent screening pass over the corpus. The pre-registered protocol called for two coders; in execution, only one was available. Adding a second coder's decisions retrospectively would let Cohen's κ be computed and the dataset move from positive-unlabelled to fully-labelled.

### What to do

1. Clone the repo and locate [`data/screening/screening_log.template.csv`](../data/screening/screening_log.template.csv). It's a single-row template that defines the column shape.
2. Re-screen the 3,892 PubMed-derived records (in [`data/screening/derived_corpus.csv`](../data/screening/derived_corpus.csv)) against the eligibility criteria in [`prereg/PROSPERO_preregistration.md`](../prereg/PROSPERO_preregistration.md) §10–13.
3. Save your decisions as `data/screening/screening_log__second_screen_<your-name>_<YYYY-MM-DD>.csv`, one row per record, conformant to [`data/screening/screening_log.schema.json`](../data/screening/screening_log.schema.json).
4. Open a PR with your CSV. Use the `data` issue template if you have questions.

### Schema fields you must populate

- `record_id` — match the existing `record_id` from `derived_corpus.csv` (this is how the join happens).
- `title`, `decision` — required.
- `decision_stage` — `title_abstract` (most realistic) or `combined`.
- `screener_id` — your initials or a stable identifier (e.g., `MA-Wahba-2026-T2`).
- `screening_date` — ISO date.
- `exclusion_reason` — if `decision = exclude`, pick from the codebook ([`data/exclusion_reason_codebook.md`](../data/exclusion_reason_codebook.md)).
- `notes` — free text for borderline cases. Strongly encouraged.

### What happens when the PR is merged

- A new file `scripts/build_inter_rater_agreement.py` will be added to compute Cohen's κ between your screen and the canonical-include subset.
- The `data/QUALITY_REPORT.md` will gain an "Inter-rater agreement" section with κ, percent agreement, and a confusion matrix.
- The PROSPERO file Section 19 will be updated to reflect the realised inter-rater statistic.

### What you'll be cited for

The screening-log file you contribute will be co-authored on any future paper that uses the resulting κ statistic, with a contributor entry in `CITATION.cff`. Master's-thesis-level effort = master's-thesis-level acknowledgement.

---

## B. Broadening database coverage beyond PubMed

The PubMed-derived corpus (n = 3,892) is the only programmatically accessible substitute for the canonical 1,842-record retrieval (which used five databases). PsycINFO, Web of Science Core, Scopus, and Cochrane Central require institutional or paid API access, which the maintainer doesn't have. If you do, you can add their records to broaden the unlabelled pool.

### What to do

1. Paste the canonical Boolean query from [`data/searches/search_strategy.md`](../data/searches/search_strategy.md) into your institution's interface for one of the four blocked databases.
2. Export results as RIS / .ciw / CSV / BibTeX as appropriate.
3. Convert to the `derived_corpus.csv` schema (columns: `record_id`, `pmid`, `doi`, `title`, `abstract`, `year`, `authors`, `journal`, `source_database`).
4. Set `source_database` to one of: `psycinfo`, `web_of_science`, `scopus`, `cochrane_central`.
5. Save as `data/screening/<database>_corpus.csv` (e.g., `psycinfo_corpus.csv`).
6. Open a PR.

### What gets added

- The new database CSV is committed.
- A new `scripts/merge_corpora.py` (will be added on first such PR) will combine the database CSVs into `data/screening/multi_database_corpus.csv` and de-duplicate by DOI / title fuzzy match.
- The QUALITY_REPORT will gain per-database hit counts and overlap statistics.

---

## C. Adding a study that should be in `included_papers.csv`

The 22 canonical-identifiable includes do not exhaust the 100 included papers in the published manuscript. The remaining 78 are cited in the manuscript prose without per-paper structure.

If you can identify one of those 78 in the manuscript (cite the section / page), open a [data correction issue](https://github.com/mikhaeelatefrizk/affect-labeling-review/issues/new?template=data_correction.yml) with:

- The paper's DOI
- The manuscript section where the paper is cited
- Your inferred `subset` (psychophys / neuroimaging_neurostim / behavioral_self_report / clinical_patient_populations / prior_meta_analyses)

The maintainer will confirm the subset assignment and add the row to `included_papers.csv`. Goal: get to 100 / 100 over time.

---

## D. Adding a new effect size to the meta-analysis

If a new study meets the meta-analytic eligibility criteria (peripheral physiology outcome; affect-labelling vs. control comparison; sufficient statistics for *g* extraction), you can add it.

### What to do

1. Compute Hedges' *g* using the conversion formulas in `meta-analysis/run_meta_analysis.py`.
2. Add a row to the `studies = [...]` list at the top of `run_meta_analysis.py`.
3. Run `python meta-analysis/run_meta_analysis.py` — every CSV and figure regenerates.
4. Run `python prisma/build_prisma.py` to update the count if the study should be reflected in the PRISMA flow.
5. Update `prisma/prisma_counts.csv` to increment the appropriate subset.
6. Open a PR.

This will change the headline pooled *g* and the heterogeneity metrics. The maintainer will review the inclusion judgment carefully (these are substantive scientific changes, not tooling changes).

---

## E. Translating the manuscript or PROSPERO into another language

The PROSPERO §25 limitation is that non-English papers were excluded if no translated full text was available. A translation of the *manuscript* into another language would substantially broaden access for non-English-speaking researchers.

Open a [data] issue describing your proposed translation (target language, scope: manuscript only or full package, your translation credentials). The maintainer can advise on file naming and licensing. Translations remain under CC-BY-4.0.

---

## F. Adding new analyses

The package is designed to be extended:

- **Bayesian random-effects.** A natural extension. The data are in `meta-analysis/extracted_effect_sizes.csv`; a `scripts/bayesian_meta_analysis.py` would be a welcome addition.
- **Coordinate-based ALE meta-analysis** of the neuroimaging subset. Would require supplementing with peak coordinates from each fMRI paper.
- **Multi-level random-effects** to formally model within-study dependence (Kircanski 2012's three contrasts). Currently treated as independent in the headline analysis; sensitivity should be checked.
- **Prediction-interval-driven sample-size calculation** for a planned multi-site replication.

Each of these would warrant a sibling script under `scripts/` and a corresponding section in the manuscript.

---

## License for contributed content

By opening a PR you agree that your contribution is licensed under the same terms as the rest of the repository: source code under MIT, narrative content under CC-BY-4.0, data under CC-BY-4.0. See `LICENSE-CODE`, `LICENSE-MANUSCRIPT`, `LICENSE-DATA`.

---

*This guide is part of the open-research package archived at Zenodo DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595). Last updated for v1.0.0 (May 2026).*
