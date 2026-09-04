# `figures/`

The four figures referenced in the manuscript, each in PNG (display) and PDF (vector) formats.

## Contents

| File | Generator script | What it shows |
|---|---|---|
| `prisma_flow.{png,pdf}` | [`prisma/build_prisma.py`](../prisma/build_prisma.py) | PRISMA 2020 flow diagram: 1,889 records identified → 1,571 screened → 282 full-text → 100 included, with breakdown into the 5 synthesis subsets. |
| `forest_plot.{png,pdf}` | [`meta-analysis/run_meta_analysis.py`](../meta-analysis/run_meta_analysis.py) | Forest plot of the *k* = 8 effect sizes with 95% CIs and the random-effects pooled diamond at *g* = −0.49 [−0.73, −0.26]. |
| `funnel_plot.{png,pdf}` | [`meta-analysis/run_meta_analysis.py`](../meta-analysis/run_meta_analysis.py) | Funnel plot for publication-bias inspection. Pseudo-CI envelope drawn around the pooled estimate. |
| `rob_summary.{png,pdf}` | [`supplementary/build_rob_figure.py`](../supplementary/build_rob_figure.py) | Traffic-light summary of risk-of-bias judgments across the 17 primary studies in the RoB table and 5 domains (the table's four narratively synthesised meta-analyses are not plotted; two rows, Fitzpatrick 2019 and Matejka 2013, are shown as "Not assessed" pending formal assessment). |

## Format choice

PNG (200 DPI) for screen reading and quick GitHub previews. PDF for vector-quality printing and journal submissions. Both are regenerated together by the generator scripts.

## Reproducibility note

The committed PNGs and PDFs were generated with matplotlib 3.8.2 on Python 3.11. Re-running with the pinned environment produces byte-identical files. Re-running with newer matplotlib (e.g., 3.10.x) produces visually identical but byte-different files; this is expected and not a code error.

Neither CI nor `make verify` byte-checks `figures/*.png` or `figures/*.pdf`: PDF timestamps and font rendering differ across matplotlib builds and platforms, so the bytes differ while the plotted content is identical. Both gate the same set of tabular outputs instead — `meta-analysis/*.csv`, `meta-analysis/*.txt`, `prisma/prisma_counts.txt`, `prisma/prisma_counts.csv`, `prisma/prisma_counts.derived.txt`, `data/screening/included_papers.csv`, `data/screening/all_references.csv` — which are the numerical inputs to every figure.

## License

CC-BY-4.0 (treated as part of the manuscript / scholarly content for licensing purposes). See [`LICENSE-MANUSCRIPT`](../LICENSE-MANUSCRIPT).

## How to re-render

```bash
python meta-analysis/run_meta_analysis.py     # forest + funnel
python prisma/build_prisma.py                 # prisma flow
python supplementary/build_rob_figure.py      # rob summary
```

Or all together:

```bash
make figures
```
