# FAQ — frequently asked questions about the affect-labeling-review dataset

This page answers the questions readers most often ask after a first pass through the repository. Each answer is a direct pointer to the canonical source.

---

## 1) What year filter was applied to the database searches?

**None.** Per PROSPERO §7: *"From inception through the date of the final search; re-run within 14 days of manuscript submission."* The final search window was **Q1–Q2 2026**. No date or language restrictions were applied at any of the nine databases.

If you are re-running the searches, **apply no year filter** — or, if your interface requires an upper bound, cap at **30 June 2026** to match the original window. Records published after that date are out-of-scope for matching against the published inclusion labels.

Database coverage windows:

| Database | Coverage start |
|---|---|
| PubMed | 1966 |
| PsycINFO | 1887 |
| Web of Science Core Collection | 1900 |
| Scopus | 1970 |
| Cochrane Central | 1996 |
| ClinicalTrials.gov | 2000 |
| OSF Registries | 2014 |
| PsyArXiv | 2017 |
| bioRxiv | 2013 |

**Canonical source:** [`data/searches/search_strategy.md`](../data/searches/search_strategy.md) and [`prereg/PROSPERO_preregistration.md`](../prereg/PROSPERO_preregistration.md) §7.

---

## 2) Where is the full list of 100 included papers?

The PRISMA flow records **100 included papers** at the synthesis stage, broken down as 42 neuroimaging/neurostimulation studies, 9 effect-size contributions from 7 unique studies in the meta-analysis, 28 behavioral/self-report studies, 12 clinical/patient-population studies, and 9 prior meta-analyses synthesized narratively (`prisma/prisma_counts.csv`).

A **per-paper enumeration of all 100 does not exist** in machine-readable form. This is the load-bearing limitation of the public dataset:

- The original per-paper screening decisions for the 1,571 title/abstract records and the 282 full-text records were **not preserved** in a shareable form.
- Of the 100 final includes, only **22 are unambiguously identifiable** from the analysis code (`meta-analysis/run_meta_analysis.py` for the 7 meta-analysis studies; `supplementary/build_rob_figure.py` for the 19 risk-of-bias studies; 4 overlap = 22 unique).
- The remaining **78 are cited in the manuscript prose** but the boundary between "included study" and "background citation" was not flagged per-entry in `references.bib`.

What you can use:

| File | Rows | What it gives you |
|---|---:|---|
| [`data/screening/included_papers.csv`](../data/screening/included_papers.csv) | 22 | Gold-standard positives — the 22 confidently-identifiable includes, with subset, title, authors, DOI. |
| [`data/screening/all_references.csv`](../data/screening/all_references.csv) | 86 | Every entry in `references.bib`, with `is_confirmed_include` (1 for the 22, 0 for the other 64) and `manuscript_mentions` (count of how often the paper is cited in the manuscript prose). High `manuscript_mentions` ⇒ very likely an included study. |
| [`data/screening/derived_screening_log.csv`](../data/screening/derived_screening_log.csv) | 3,892 | The PubMed re-derived candidate corpus joined against the included list. Positive-unlabelled (PU) framing: 14 confirmed positives, 3,878 unknowns. |

Full discussion: [`data/screening/README.md`](../data/screening/README.md) §"Why 22 and not 100".

---

## 3) How do I label my own re-run corpus using your data?

If you have re-run the canonical search across multiple databases and want to label your merged corpus, the recommended workflow is a three-tier match:

1. **Strict positives (n = 22):** match rows of your corpus by DOI or fuzzy title against [`included_papers.csv`](../data/screening/included_papers.csv). These are gold-standard positives.
2. **Soft / candidate positives:** match against [`all_references.csv`](../data/screening/all_references.csv) rows where `is_confirmed_include = 0` AND `manuscript_mentions ≥ 2`. These are highly likely to be additional included studies or topically-relevant background citations. Verify per-paper; roughly half should be true positives.
3. **Unlabeled:** everything in your corpus that doesn't match either CSV. Standard PU framing applies; the [`derived_screening_log.csv`](../data/screening/derived_screening_log.csv) quantifies the expected hidden-positive contamination rate at approximately 2%.

Concrete training approaches (TF-IDF + logistic regression baseline, PubMedBERT fine-tuning, PU-aware methods like Elkan & Noto 2008 or nnPU) are detailed in [`docs/for-ml-researchers.md`](for-ml-researchers.md). A worked walkthrough for a master's thesis on AI-powered SLR screening is in [`docs/for-masters-students.md`](for-masters-students.md).

---

## 4) The published PRISMA flow says 1,842 records, but re-running the query today gives more. Why?

PubMed (and other databases) are living indices — new records continue to be added daily. The canonical **1,842** in `prisma/prisma_counts.csv` reflects the corpus state at the original search date in Q1–Q2 2026. Today's re-query will retrieve more records.

The drift is informational, not error, and is reported transparently in [`data/QUALITY_REPORT.md`](../data/QUALITY_REPORT.md). For ML training, the additional records are useful (more unlabelled candidates) rather than harmful.

---

## 5) Why was screening done by a single coder?

The pre-registered protocol described a two-reviewer scheme. One protocol-execution deviation is acknowledged in the manuscript (§2.1, §4.6): screening and data extraction were carried out by a single reviewer, so inter-rater agreement statistics (Cohen's κ) are unavailable.

If you re-screen the corpus with an independent coder, please publish the second screening pass as a separate, dated CSV (e.g., `screening_log__second_screen_2026.csv`) rather than overwriting the existing data — see [`docs/extending-the-corpus.md`](extending-the-corpus.md) for the workflow. Cohen's κ between the two passes can then be computed reproducibly.

---

## 6) What licenses apply?

- **Source code** (Python scripts, build scripts, CI): MIT — see [`LICENSE-CODE`](../LICENSE-CODE).
- **Manuscript and figures:** CC-BY-4.0 — see [`LICENSE-MANUSCRIPT`](../LICENSE-MANUSCRIPT).
- **Data files** (every CSV and BibTeX/JSON resource under `data/`, `prisma/`, `meta-analysis/`, `supplementary/`): CC-BY-4.0 — see [`LICENSE-DATA`](../LICENSE-DATA).

All three licenses permit research, teaching, and ML-training use including commercial, with attribution per [`CITATION.cff`](../CITATION.cff) at the repository root.

---

## 7) How do I cite this work?

> Wahba, M. A. R. (2026). *Putting feelings into words: A systematic review and meta-analysis of affect labeling* (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.20109595

`CITATION.cff` is machine-readable — Zotero, EndNote, and Mendeley all consume it directly.

---

## 8) Something's still unclear — how do I ask?

Open an issue on the repository: <https://github.com/mikhaeelatefrizk/affect-labeling-review/issues>. There are dedicated templates for data corrections, reproducibility problems, and errata in [`.github/ISSUE_TEMPLATE/`](../.github/ISSUE_TEMPLATE/). For substantive questions, public issues are preferred because the answer becomes a reference for future researchers reusing the dataset.
