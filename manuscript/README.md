# `manuscript/`

The full ~14,000-word manuscript and any future revisions.

## Contents

- [`manuscript.md`](manuscript.md) — the complete manuscript: Abstract, Introduction, Methods (2.1–2.7), Results (3.1–3.8), Discussion (4.1–4.7), Future directions, Conclusion, Figures, Supplementary materials index, Data and Code Availability statement, References.

## Format

Markdown for openness and diffability. Pandoc-friendly:

```bash
pandoc manuscript.md -o manuscript.pdf --pdf-engine=xelatex
pandoc manuscript.md -o manuscript.docx
```

If submitting to a journal that requires a specific format (Word, LaTeX), convert via pandoc on the day of submission so the source remains the authoritative version.

## How this file relates to the rest of the package

| In the manuscript | Authoritative file in the repo |
|---|---|
| Headline pooled effect (g = −0.43) | [`meta-analysis/results_summary.txt`](../meta-analysis/results_summary.txt) |
| §3.1 PRISMA flow numbers | [`prisma/prisma_counts.txt`](../prisma/prisma_counts.txt) + [`prisma/prisma_counts.csv`](../prisma/prisma_counts.csv) |
| §2.7 meta-analytic methods | [`meta-analysis/run_meta_analysis.py`](../meta-analysis/run_meta_analysis.py) |
| §2.6 Risk of bias | [`supplementary/risk_of_bias.csv`](../supplementary/risk_of_bias.csv) + [`supplementary/risk_of_bias_explanation.md`](../supplementary/risk_of_bias_explanation.md) |
| §2.2 Eligibility criteria | [`prereg/PROSPERO_preregistration.md`](../prereg/PROSPERO_preregistration.md) §10–13 |
| §2.3 Search strategy | [`data/searches/search_strategy.md`](../data/searches/search_strategy.md) |
| Figures 1–4 | [`figures/`](../figures/) |
| References | [`references.bib`](../references.bib) |
| Supplementary materials list | [`SUPPLEMENTARY MATERIALS`](manuscript.md#supplementary-materials) section |

## License

CC-BY-4.0. See [`LICENSE-MANUSCRIPT`](../LICENSE-MANUSCRIPT).
