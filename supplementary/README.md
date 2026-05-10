# `supplementary/`

Risk-of-bias assessments, the figure that visualises them, and the per-study reasoning behind each judgment.

## Contents

| File | What it is |
|---|---|
| [`risk_of_bias.csv`](risk_of_bias.csv) | 19 rows × 9 columns. Per-study risk-of-bias ratings across 5 domains plus an overall judgment, plus a key-concerns narrative column. Covers RCTs, NRSI, within-subjects fMRI, and four meta-analyses synthesised narratively. |
| [`build_rob_figure.py`](build_rob_figure.py) | Generator script for the traffic-light summary figure. |
| [`risk_of_bias_explanation.md`](risk_of_bias_explanation.md) | Per-study, per-domain rationale for every RoB judgment in the CSV. The reasoning behind the codes. **The CSV is the data; this markdown is the why.** |

## Tools used

| Design type | Tool |
|---|---|
| Randomised controlled trials | RoB 2 (Sterne et al., 2019, *BMJ*, 366, l4898) |
| Non-randomised intervention studies | ROBINS-I (Sterne et al., 2016, *BMJ*, 355, i4919) |
| Within-subjects experimental fMRI / behavioural | Adapted NRSI tool (no validated tool exists; we focused on order/fatigue confounding, measurement, and reporting) |
| Coordinate-based / image-based meta-analyses | Only the measurement and reporting domains assessed (others marked N/A) |
| Whole evidence body | GRADE narrative |

The choice of three-tools-plus-narrative is justified in [`docs/methodology-deep-dive.md`](../docs/methodology-deep-dive.md) §"Why three independent risk-of-bias tools".

## Coding scheme

| Code | Meaning |
|---|---|
| `L` | Low risk |
| `S` | Some concerns |
| `M` | Moderate |
| `H` | High risk |
| `−` (em-dash) | Not applicable |

Symbols in the figure: `+` (Low) / `−` (Some/Moderate) / `x` (High) / `?` (N/A).

## How to re-run

```bash
python supplementary/build_rob_figure.py
```

Regenerates `figures/rob_summary.png` and `figures/rob_summary.pdf`. Byte-identical reruns on the pinned environment.

## How to contest a judgment

Open a [data correction issue](https://github.com/mikhaeelatefrizk/affect-labeling-review/issues/new?template=data_correction.yml) with the proposed alternative judgment and supporting evidence. The narrative in `risk_of_bias_explanation.md` will be updated, the CSV regenerated, the figure rebuilt.

## License

Code (`build_rob_figure.py`): MIT. Data (`risk_of_bias.csv`): CC-BY-4.0. Documentation (`risk_of_bias_explanation.md`, this README): CC-BY-4.0.
