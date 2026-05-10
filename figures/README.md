# `figures/`

The four figures referenced in the manuscript, each in PNG (display) and PDF (vector) formats.

## Contents

| File | Generator script | What it shows |
|---|---|---|
| `prisma_flow.{png,pdf}` | [`prisma/build_prisma.py`](../prisma/build_prisma.py) | PRISMA 2020 flow diagram: 1,889 records identified → 1,571 screened → 282 full-text → 100 included, with breakdown into the 5 synthesis subsets. |
| `forest_plot.{png,pdf}` | [`meta-analysis/run_meta_analysis.py`](../meta-analysis/run_meta_analysis.py) | Forest plot of the *k* = 9 effect sizes with 95% CIs and the random-effects pooled diamond at *g* = −0.43 [−0.68, −0.18]. |
| `funnel_plot.{png,pdf}` | [`meta-analysis/run_meta_analysis.py`](../meta-analysis/run_meta_analysis.py) | Funnel plot for publication-bias inspection. Pseudo-CI envelope drawn around the pooled estimate. |
| `rob_summary.{png,pdf}` | [`supplementary/build_rob_figure.py`](../supplementary/build_rob_figure.py) | Traffic-light summary of risk-of-bias judgments across the 19 RoB-assessed studies and 5 domains. |

## Format choice

PNG (200 DPI) for screen reading and quick GitHub previews. PDF for vector-quality printing and journal submissions. Both are regenerated together by the generator scripts.

## Reproducibility note

The committed PNGs and PDFs were generated with matplotlib 3.8.2 on Python 3.11. Re-running with the pinned environment produces byte-identical files. Re-running with newer matplotlib (e.g., 3.10.x) produces visually identical but byte-different files; this is expected and not a code error.

The byte-identical CI check explicitly excludes `figures/*.png` and `figures/*.pdf` to allow for matplotlib-version drift across local development environments. The numerical inputs to each figure (the CSVs and the prisma counts file) are byte-checked.

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
