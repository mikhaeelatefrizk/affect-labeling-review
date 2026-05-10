# `docs/` — extended documentation

This directory holds documentation that goes deeper than the top-level README, written for readers who want to *use* the open-research package — not just cite it. Master's and PhD readers from outside the systematic-review world should find everything they need to reproduce, extend, or re-use the dataset starting here.

## Contents

| File | Audience | What it covers |
|---|---|---|
| [`reproducibility-guide.md`](reproducibility-guide.md) | Anyone reproducing the analysis | Step-by-step from clone to byte-identical outputs, on Linux/macOS/Windows. Pinned Python, container option, common failure modes, SHA-256 receipts. |
| [`for-ml-researchers.md`](for-ml-researchers.md) | ML / NLP researchers building screening models | Detailed positive-unlabeled framing, class balance, suggested baselines, evaluation protocol, recommended PU-learning methods, expected ceilings. |
| [`methodology-deep-dive.md`](methodology-deep-dive.md) | SLR methodologists, peer reviewers | Full reasoning behind the lab-stratified moderator analysis, the choice of Hedges' *g* over Cohen's *d*, the τ² estimator selection, and the GRADE simplification. |
| [`extending-the-corpus.md`](extending-the-corpus.md) | Researchers who want to add their own data | How to publish a second-coder screening pass, how to run the search at a different database (PsycINFO / WoS / Scopus / Cochrane), how to merge a new effect size into the meta-analysis. |
| [`glossary.md`](glossary.md) | Anyone unfamiliar with SLR terminology | Plain-language definitions for affect labelling, PRISMA, RoB 2, Hedges' *g*, prediction interval, PU learning, and ~30 other terms used in the package. |
| [`troubleshooting.md`](troubleshooting.md) | Reproducers hitting an error | Top 10 issues and fixes — Python version mismatches, matplotlib backend errors on headless servers, PubMed E-utilities rate limiting, encoding issues on Windows, and more. |

## Reading order for a new master's / PhD reader

1. **Top-level [`README.md`](../README.md)** — project overview, headline result, badges.
2. **[`docs/glossary.md`](glossary.md)** — five minutes to align on terminology.
3. **[`prereg/PROSPERO_preregistration.md`](../prereg/PROSPERO_preregistration.md)** — the protocol authoring intent and the post-completion update.
4. **[`manuscript/manuscript.md`](../manuscript/manuscript.md)** — the full ~14,000-word paper.
5. **[`docs/methodology-deep-dive.md`](methodology-deep-dive.md)** — the *why* behind the analytic choices.
6. **[`docs/reproducibility-guide.md`](reproducibility-guide.md)** — clone, build, verify.
7. **[`docs/for-ml-researchers.md`](for-ml-researchers.md)** — only if you want to build an SLR screening model.

## Reading order for a thesis-committee member or peer reviewer

1. **[`prisma/PRISMA_2020_checklist.md`](../prisma/PRISMA_2020_checklist.md)** — every PRISMA 2020 reporting item with pointer.
2. **[`data/searches/PRISMA-S_checklist.md`](../data/searches/PRISMA-S_checklist.md)** — every PRISMA-S search-reporting item.
3. **[`supplementary/risk_of_bias_explanation.md`](../supplementary/risk_of_bias_explanation.md)** — per-study RoB rationale.
4. **[`manuscript/manuscript.md`](../manuscript/manuscript.md)** — the headline document.
5. **[`docs/methodology-deep-dive.md`](methodology-deep-dive.md)** — analytic-choice justifications.

## Reading order for a journal editor

The package was assembled with the PRISMA 2020 + PRISMA-S reporting standards specifically in mind. Two PRISMA-required artifacts that journals routinely request — the PRISMA 2020 flow diagram and the 27-item PRISMA 2020 checklist — are at [`figures/prisma_flow.pdf`](../figures/prisma_flow.pdf) and [`prisma/PRISMA_2020_checklist.md`](../prisma/PRISMA_2020_checklist.md). The structured machine-readable PRISMA counts are at [`prisma/prisma_counts.csv`](../prisma/prisma_counts.csv).

## License

All files in `docs/` are released under [CC-BY-4.0](../LICENSE-MANUSCRIPT) (treated as part of the manuscript / scholarly content for licensing purposes).
