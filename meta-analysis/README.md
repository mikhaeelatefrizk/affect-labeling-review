# `meta-analysis/`

The random-effects meta-analysis of peripheral psychophysiology — the single quantitative synthesis in the review.

## Contents

| File | What it is |
|---|---|
| [`run_meta_analysis.py`](run_meta_analysis.py) | The analysis script. Pure Python (numpy, pandas, scipy, matplotlib). Runs in <2 seconds. Idempotent. |
| [`extracted_effect_sizes.csv`](extracted_effect_sizes.csv) | The 8 effect sizes from 6 studies, with study identifier, year, lab, sample sizes, design, computed Hedges' *g*, standard error, variance, fixed-effect weight, and 95% CI. |
| [`leave_one_out.csv`](leave_one_out.csv) | Sensitivity analysis: pooled estimate (and 95% CI) when each study is dropped in turn. Ranges from −0.59 (omitting Fitzpatrick 2019) to −0.45 (omitting Kircanski 2012's reappraisal contrast), all sign-stable. |
| [`results_summary.txt`](results_summary.txt) | Plain-text summary of the primary, UCLA-only, and independent-only pooled estimates plus heterogeneity statistics and Egger's test. |

## Headline result

Random-effects meta-analysis (DerSimonian-Laird τ²) of *k* = 8 effect sizes from 6 studies on peripheral psychophysiological response (skin conductance, non-specific SCR frequency, heart rate, heart-rate variability):

- **Pooled Hedges' *g* = −0.49, 95% CI [−0.73, −0.26], *p* < .001**
- 95% prediction interval [−1.07, +0.08] **crosses zero** — a new study could plausibly observe an effect in either direction.
- *I*² = 36.2%; τ² = 0.040

Pre-specified lab-stratified moderator analysis:

- **UCLA Lieberman/Craske axis only:** *g* = **−0.74**, 95% CI [−1.02, −0.47], *k* = 5, *I*² = 0%
- **Independent laboratories only:** *g* = **−0.23**, 95% CI [−0.51, +0.05], *k* = 3, *I*² = 23.6% — non-significant; CI crosses zero

The 0.52 g-unit gap between strata is the single most informative result in the review. See [`docs/methodology-deep-dive.md`](../docs/methodology-deep-dive.md) for the full reasoning behind the lab-stratified analysis.

## How to re-run

```bash
python meta-analysis/run_meta_analysis.py
```

Output: regenerates the two CSVs and `results_summary.txt`, plus the forest and funnel plots in [`figures/`](../figures/). Byte-identical re-run on the pinned environment.

## How to add a new study

See [`docs/extending-the-corpus.md`](../docs/extending-the-corpus.md) §D. In short: add a row to the `studies = [...]` list at the top of `run_meta_analysis.py`, re-run.

## Relationship to the rest of the package

The 8 effect sizes here come from 6 unique studies, all of which appear in [`data/screening/included_papers.csv`](../data/screening/included_papers.csv) under `subset = psychophysiology_meta_analysis`. The risk-of-bias judgments for these studies are in [`supplementary/risk_of_bias.csv`](../supplementary/risk_of_bias.csv) and explained in [`supplementary/risk_of_bias_explanation.md`](../supplementary/risk_of_bias_explanation.md).

## License

Code (`run_meta_analysis.py`): MIT (see [`LICENSE-CODE`](../LICENSE-CODE)). Data files (`*.csv`, `*.txt`): CC-BY-4.0 (see [`LICENSE-DATA`](../LICENSE-DATA)).
