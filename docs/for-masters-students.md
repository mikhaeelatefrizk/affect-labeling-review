# Materials for your master's thesis on AI-powered SLR screening

Hi,

Thank you for your message about my systematic review and meta-analysis of affect labeling. The complete open-research package is now publicly archived, and below is a direct, honest mapping from each item you asked for to a downloadable file.

- **Repository:** https://github.com/mikhaeelatefrizk/affect-labeling-review
- **Permanent archive (Zenodo, DOI):** https://doi.org/10.5281/zenodo.20109595
- **License:** Source code MIT; manuscript and figures CC-BY-4.0; **all data files CC-BY-4.0**. You may use them freely for research, teaching, and ML training (commercial or non-commercial), with attribution.

---

## 1) The initial retrieved papers list

You asked for the raw export from academic databases (CSV/RIS/etc.).

**What I have:** the original five-database raw exports (PubMed + PsycINFO + Web of Science + Scopus + Cochrane Central, totalling 1,842 records as reported in the published PRISMA flow) were **not preserved as exported files**. Aggregate per-stage counts are canonical; per-database raw dumps are not.

**What is in the repository as a substitute:**

| File | What it is | Rows |
|---|---|---|
| [`data/screening/derived_corpus.csv`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/data/screening/derived_corpus.csv) | A clean re-derivation: I re-ran the pre-registered PubMed query through NCBI E-utilities and downloaded title + abstract + DOI + PMID + journal + year for every hit. | **3,892 records** |
| [`data/searches/search_strategy.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/data/searches/search_strategy.md) | PRISMA-S compliant search strategy. The exact Boolean query, all nine information sources, and the canonical aggregate hit counts. You can re-run the queries verbatim against your institution's database access if you want PsycINFO / Web of Science / Scopus / Cochrane records too. | — |
| [`prisma/prisma_counts.csv`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/prisma/prisma_counts.csv) | Structured PRISMA flow counts (records identified, screened, full-text assessed, excluded by reason, included). | 19 rows |

**Why the derived corpus is more than 1,842:** PubMed has continued to be indexed since the original search, and PubMed's automatic term mapping is broader than the simple Boolean. The drift is reported transparently in [`data/QUALITY_REPORT.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/data/QUALITY_REPORT.md). For ML training this drift is helpful (more candidates), not harmful.

---

## 2) The inclusion and exclusion criteria

This part is fully preserved:

| File | What it covers |
|---|---|
| [`prereg/PROSPERO_preregistration.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/prereg/PROSPERO_preregistration.md) | Full PROSPERO-format pre-registration. **Section 10** = participants/population (include/exclude). **Section 11** = intervention/exposure definition. **Section 12** = comparators. **Section 13** = study types (include/exclude). **Section 25** = language. |
| [`data/exclusion_reason_codebook.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/data/exclusion_reason_codebook.md) | Authoritative codebook for the six full-text exclusion-reason codes used in the screening, plus broader title/abstract codes recommended for any future re-screen: `no_al_manipulation`, `no_phys_neural_outcome`, `review_without_primary_data`, `non_english`, `duplicate_sample`, `insufficient_data_for_extraction`, `off_topic`, `wrong_population`, `wrong_design`, `other`. |
| [`data/searches/search_strategy.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/data/searches/search_strategy.md) | The Boolean search query (the eligibility *gate* before screening even starts). |

For ML training you will likely want to encode the criteria as natural-language prompts or as a labeled rubric — the PROSPERO file gives you exact wording you can paste into either.

---

## 3) The final list of included papers, with inclusion/exclusion remarks

This is the honest part of the answer that I want to be upfront about.

**What's preserved per-paper:**

| File | What it contains | Rows |
|---|---|---|
| [`data/screening/included_papers.csv`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/data/screening/included_papers.csv) | 22 of the 100 included studies, identified with confidence from the analysis code (the 9-effect-size meta-analysis input + the 19-study risk-of-bias table). Each row has: `record_id`, `bibtex_key`, `subset` (psychophys / neuro / behavioral / clinical / prior-MA), `title`, `authors`, `year`, `journal`, `doi`. | 22 |
| [`data/screening/derived_screening_log.csv`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/data/screening/derived_screening_log.csv) | The 3,892 PubMed-derived candidates joined against the included list. Each row has `decision = "include"` (matched against canonical includes by DOI or fuzzy-title) or `decision = "unknown"` (unmatched). 14 confirmed positives, 3,878 unknowns. | 3,892 |
| [`data/screening/screening_log.schema.json`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/data/screening/screening_log.schema.json) | JSON Schema 2020-12 specifying the screening-log structure. Validates with `jsonschema` or `frictionless`. | — |
| [`data/QUALITY_REPORT.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/data/QUALITY_REPORT.md) | Auto-generated quality report comparing canonical vs. derived counts, recall of canonical includes in the PubMed re-query, year/journal distributions, and class balance. | — |

**What is not preserved:**

- The original **per-paper screening decisions and exclusion reasons** for the 1,571 records screened at title/abstract were not retained in a shareable form. Aggregate counts are canonical (1,289 excluded at TI/AB, 182 at full-text broken into the six reasons in `prisma_counts.csv`); per-paper rationales are not.
- The other **78 of the 100 included papers** are cited in the manuscript prose without a structured per-paper list — they exist in [`references.bib`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/references.bib) interleaved with methods/background citations, but the boundary between "included study" and "background citation" was not flagged per-entry.

This is the load-bearing limitation. The derived screening log is therefore a **positive-unlabeled (PU) dataset**, not a fully labeled one. I want to be upfront about this rather than fabricate per-paper labels I don't have.

---

## How to actually use this for your AI screening model

I wrote a detailed guide for exactly your use case, with three concrete training approaches (TF-IDF + LR baseline, PubMedBERT fine-tune, PU learning), an honest evaluation protocol, and three concrete data-augmentation paths:

> **[`docs/for-ml-researchers.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/docs/for-ml-researchers.md)** — read this if you only have time for one extra file.

The short version, in increasing order of effort:

### Option A — train a PU classifier on what's published

Treat `data/screening/derived_screening_log.csv` as PU-labeled:

- **Positive class** (n=14): `decision == "include"` rows. Use these as gold-standard positives.
- **Unlabeled** (n=3,878): `decision == "unknown"` rows. Most are true negatives, but ~78 are unidentified positives ("hidden positives"), so label noise on the negative class is roughly 2%.
- **Approach:** PU-aware methods such as [Elkan & Noto 2008](https://cseweb.ucsd.edu/~elkan/posonly.pdf), nnPU (Kiryo et al. 2017), or PU bagging. Or train a standard binary classifier with class weights and treat the 2% noise as an upper bound on recall loss.

### Option B — augment with the manuscript citation list

Programmatically parse [`references.bib`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/references.bib) and treat every cited paper as a candidate "included study," then ask me (via a GitHub issue) to confirm which subset each belongs to. This would lift you from 22 of 100 enumerated includes toward the full 100. See [`docs/extending-the-corpus.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/docs/extending-the-corpus.md) §C for the workflow.

### Option C — re-screen the corpus yourself (highest-value contribution)

The corpus + criteria + codebook are in your hands. Re-screen the 3,892 PubMed candidates against the PROSPERO criteria, using your AI model in the loop, and publish the resulting screening log alongside mine as a second-coder pass. The schema in `screening_log.schema.json` is designed for exactly this. With two coders' decisions, Cohen's κ becomes computable and the dataset moves from positive-unlabelled to fully-labelled.

If you do option C and publish the result, please open a PR — I'll merge and credit you on the dataset.

---

## Other resources you may find useful

These weren't on your list but are directly relevant to a thesis at the intersection of AI and SLR methodology:

- **[`prisma/PRISMA_2020_checklist.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/prisma/PRISMA_2020_checklist.md)** — completed 27-item PRISMA 2020 reporting checklist with file pointers. Useful as a template for your own thesis.
- **[`data/searches/PRISMA-S_checklist.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/data/searches/PRISMA-S_checklist.md)** — 16-item PRISMA-S search-reporting checklist.
- **[`supplementary/risk_of_bias_explanation.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/supplementary/risk_of_bias_explanation.md)** — per-study, per-domain RoB rationale. Useful as a model for how to document RoB judgments transparently.
- **[`docs/glossary.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/docs/glossary.md)** — ~50 terms across SLR methodology, meta-analysis statistics, and PU learning.
- **[`docs/methodology-deep-dive.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/docs/methodology-deep-dive.md)** — analytic-choice justifications (why Hedges' *g*, why DerSimonian-Laird, why three RoB tools, why include Burklund 2024).
- **[`docs/reproducibility-guide.md`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/docs/reproducibility-guide.md)** — clone → byte-identical outputs, with a containerised option and NCBI API-key acceleration.

## Citation (please use this exact form)

> Wahba, M. A. R. (2026). *Putting feelings into words: A systematic review and meta-analysis of affect labeling* (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.20109595

`CITATION.cff` at the repository root is machine-readable — Zotero, EndNote, and Mendeley all consume it directly.

---

## License recap

- **Source code:** MIT — see [`LICENSE-CODE`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/LICENSE-CODE).
- **Manuscript + figures:** CC-BY-4.0 — see [`LICENSE-MANUSCRIPT`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/LICENSE-MANUSCRIPT).
- **Data files:** CC-BY-4.0 — see [`LICENSE-DATA`](https://github.com/mikhaeelatefrizk/affect-labeling-review/blob/main/LICENSE-DATA).

Free for academic, teaching, and ML-training use, including commercial. Attribution per the citation above is the only requirement.

---

## Contact

- **Email:** mikhaeelatefrizk@proton.me
- **GitHub:** https://github.com/mikhaeelatefrizk
- **ORCID:** [0009-0006-1069-9558](https://orcid.org/0009-0006-1069-9558)

For substantive questions, please open an issue on the repository — that way the answer becomes a public reference for any future researcher reusing the dataset. For matters that aren't suitable for a public issue, email is fine.

Best of luck with the thesis. The intersection of AI and SLR automation is exactly where systematic-review methodology needs to go next, and this dataset is yours to use.

— Mikhaeel Atef Rizk Wahba
