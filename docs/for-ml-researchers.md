# For ML researchers — building SLR screening models on this corpus

This guide is for someone who wants to *train and evaluate* an AI-assisted screening model using the open dataset. It assumes familiarity with binary classification and standard NLP transformer pipelines (BERT/SciBERT/PubMedBERT-class models).

The README has a brief orientation section; this document is the deep dive.

---

## What you have access to

| File | Rows | Use |
|---|---:|---|
| [`data/screening/derived_corpus.csv`](../data/screening/derived_corpus.csv) | 3,892 | Candidate corpus: title + abstract + DOI + year + journal for every record retrieved from PubMed using the pre-registered Boolean query. |
| [`data/screening/included_papers.csv`](../data/screening/included_papers.csv) | 22 | Canonical-identifiable inclusions, with `subset` tagging (psychophys / neuro / behav / clinical / prior-MA). |
| [`data/screening/derived_screening_log.csv`](../data/screening/derived_screening_log.csv) | 3,892 | The corpus joined against the included list, with `decision` ∈ {`include`, `unknown`}. **This is the file you train on.** |
| [`data/screening/screening_log.schema.json`](../data/screening/screening_log.schema.json) | — | JSON Schema 2020-12 for the screening log. |
| [`prereg/PROSPERO_preregistration.md`](../prereg/PROSPERO_preregistration.md) | — | The eligibility criteria — the natural-language definition of "include" that your model is trying to learn. |
| [`data/exclusion_reason_codebook.md`](../data/exclusion_reason_codebook.md) | — | The 6 full-text exclusion reasons + 4 broader title/abstract reasons used in the original review. Suitable as a multi-class extension target. |
| [`data/QUALITY_REPORT.md`](../data/QUALITY_REPORT.md) | — | Honest report of canonical vs. derived counts, recall of canonical includes in the PubMed re-query, year/journal distributions, and class balance. |

---

## The labelling framing — read this before anything else

The dataset is **positive-unlabelled (PU)**, not fully labelled. This is non-negotiable and stems from a real-world data limitation, not a stylistic choice. Specifically:

- **`decision == "include"` rows (n = 14):** confirmed positives. Each row matched against one of the 22 canonical-identifiable includes by DOI (n=13) or title-fuzzy match (Jaccard ≥ 0.85, n=1).
- **`decision == "unknown"` rows (n = 3,878):** unlabelled. Most are true negatives, but **approximately 78 of the 100 canonical included papers were not enumerated in structured form** in the original review (they appear in the manuscript prose without per-paper extraction). A subset of those 78 papers may be in the PubMed-derived corpus and are therefore mislabelled as "unknown" when they are in fact "include." Upper-bound noise rate on the unknown class: ~78 / 3,878 ≈ 2%.

**Why this happened:** the original review preserved aggregate PRISMA counts (canonical) and the per-paper records for the meta-analysed subset (k = 9 effect sizes from 7 studies) and the risk-of-bias table (19 studies; 4 overlap with psychophys), but did not preserve a structured per-paper inclusion log for the full 100 included studies. The honest, non-fabricated reconstruction is what you have.

**Implications for training:**

1. **Do not treat `unknown` as `exclude`** without acknowledging the ~2% label noise. If you do, your reported recall on the full (100-paper) inclusion set is upper-bounded by the 14/100 = 14% that you can verify, which is misleadingly low.
2. **Use PU-aware methods.** See "Recommended approaches" below.
3. **Report metrics over the verified-positive subset.** Precision and recall computed against `decision == "include"` are well-defined and honest. Precision is best — your model returning a small number of high-confidence positives can be checked against the 14 known positives. Recall on the full universe of 100 includes is *not* directly measurable from this dataset alone.

---

## Class balance and difficulty

| Class | Count | % | Notes |
|---|---:|---:|---|
| `include` | 14 | 0.36% | Confirmed positives. |
| `unknown` | 3,878 | 99.64% | Mostly true negatives + ~78 hidden positives. |

The 0.36% positive rate is realistic for SLR title/abstract screening — typical SLRs filter ~1–10% of retrieved records. Your model should be tuned with severe class weighting (e.g., positive-class weight ≈ 100×) or use focal loss.

---

## Recommended approaches

### Baseline 1 — keyword + logistic regression

Build a TF-IDF representation of `title + abstract` and train a regularised logistic regression, treating `unknown` as `exclude`:

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold

X_text = df["title"].fillna("") + " " + df["abstract"].fillna("")
y = (df["decision"] == "include").astype(int)
vec = TfidfVectorizer(max_features=50_000, ngram_range=(1, 2), min_df=2)
X = vec.fit_transform(X_text)
clf = LogisticRegression(class_weight="balanced", max_iter=1000)
# Stratified 5-fold; report mean precision @ top-50, top-100
```

Expected ceiling: precision @ top-50 ≈ 0.20–0.30 (recovers 10–15 of 14 known positives); recall @ top-200 ≈ 0.85+ on the *known-positive* subset.

### Baseline 2 — PubMedBERT fine-tune

Use a domain-pretrained transformer (PubMedBERT, BioBERT, SciBERT). Fine-tune for binary classification with class weighting. Expected ceiling: precision @ top-50 ≈ 0.40–0.50.

### Honest method — PU learning

The framing matches the **positive-unlabelled (PU)** setting exactly. Three concrete PU methods that fit this dataset size:

- **Elkan & Noto (2008)** — train a non-traditional classifier on (P + U), then calibrate with the assumption *P(s = 1 | y = 1) = c* estimated from a held-out positive set. With only 14 positives, the held-out set is tiny; report uncertainty. Reference: https://cseweb.ucsd.edu/~elkan/posonly.pdf
- **nnPU (Kiryo, Niu, du Plessis, Sugiyama, 2017)** — non-negative PU learning that handles small *π* (positive prior) more stably than the unbiased PU loss. Reference: https://arxiv.org/abs/1703.00593
- **PU bagging** — bag the unlabelled set into many "treat-as-negative" subsets, train a binary classifier per bag, average predictions. Robust but compute-heavy.

For this dataset size (n ≈ 4,000), PU bagging with 100 bags + a small transformer is feasible on a single GPU.

### Active-learning extension

The intended downstream use case is *human-in-the-loop screening*: the model surfaces high-uncertainty candidates for human review. The 14 known positives anchor the precision side; the unknowns are the human-review queue. A standard expected-information-gain or BALD-style query strategy works well here.

---

## Suggested evaluation protocol

Because of the PU framing, you cannot report a clean F1 on the full universe. Instead, report:

1. **Precision @ top-K** where K ∈ {25, 50, 100, 200}. Honest because only positives need ground-truth labels.
2. **Recall on the verified-positive subset** (i.e., what fraction of the 14 known positives appear in the top-K).
3. **Cohort agreement at k = 22** (the canonical-identifiable include count). If your model's top 22 candidates include all 14 known positives, the additional 8 are likely the unidentified canonical positives — a candidate way to *recover* the missing labels.
4. **Score-distribution sanity checks** versus year and subset distributions. If your top-K is dominated by a single year or subset, you may have fit confounders rather than the construct.

For cross-validation, use **stratified 5-fold by `decision`** with the seed fixed. The 14 positives split into ≈3 per fold; small but workable.

---

## Augmenting beyond what's published

Three concrete ways to add labelled data:

### A — re-run the search at a different database

The pre-registered query is in [`data/searches/search_strategy.md`](../data/searches/search_strategy.md). Paste it into PsycINFO / Web of Science Core / Scopus / Cochrane Central via your institutional access; export the .ris/.csv; merge into `derived_corpus.csv`. Expect 30–50% overlap with PubMed; the non-overlap rows substantially expand the unlabelled pool.

### B — second-coder pass

Re-screen the 3,892 PubMed records against the PROSPERO criteria. Drop your screening log alongside the existing one (`screening_log__second_screen_2026.csv`) using the same schema. Cohen's κ between your screen and any future third-coder screen is then directly computable. This is academically valuable and welcomed via repository PR.

### C — fill in the 78 hidden positives

Open a [data correction issue](https://github.com/mikhaeelatefrizk/affect-labeling-review/issues/new?template=data_correction.yml) per paper, citing the manuscript section where the paper is discussed. The maintainer will confirm `subset` and add the row to `included_papers.csv`. Once the structured include list reaches 100 / 100, the dataset becomes fully labelled and the PU framing is no longer needed.

---

## Citation

If your thesis / paper uses this dataset, please cite:

> Wahba, M. A. R. (2026). *Putting feelings into words: A systematic review and meta-analysis of affect labelling* (v1.0.0). Zenodo. https://doi.org/10.5281/zenodo.20109595

`CITATION.cff` is machine-readable for Zotero / Mendeley / EndNote.

## License recap

Data files are CC-BY-4.0. You can use them in any project (research, teaching, ML training, commercial), with attribution.

---

## Open questions / extensions where contributions are most welcome

- **A second-coder screening pass.** This is the single highest-value addition to the dataset. With two coders' decisions, Cohen's κ becomes computable and the corpus moves from PU-labelled to fully-labelled.
- **A CLEF-eHealth-style benchmark wrapping.** Wrapping this dataset in the CLEF eHealth TAR (Technologically Assisted Reviews) format would make it directly comparable to other published SLR benchmarks (CLEF 2017–2019, SYNERGY).
- **Multi-class extension.** Most current SLR ML benchmarks frame screening as binary (include/exclude). With the [`exclusion_reason_codebook.md`](../data/exclusion_reason_codebook.md), this corpus could support a more useful multi-class formulation (which exclusion reason).

If you build any of the above on this corpus and publish, please open an issue so we can link your work back from the README.

---

*This guide is part of the open-research package archived at Zenodo DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595). Last updated for v1.0.0 (May 2026).*
