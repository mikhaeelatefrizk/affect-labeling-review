# Putting feelings into words: a systematic review and meta-analysis of affect labeling

This repository contains the full open-research package accompanying a systematic review and random-effects meta-analysis of affect labeling — the psychological and neuroscientific phenomenon, originating in Lieberman et al. (2007), in which putting feelings into words attenuates emotional responses.

> **Status: Preprint / working paper. Not yet peer-reviewed.** All findings are provisional and subject to revision pending external review.

## Headline result

Random-effects meta-analysis of nine peripheral-physiology effect sizes from seven independent studies:

- **Pooled Hedges' g = −0.43, 95% CI [−0.68, −0.18], p < .001**
- 95% prediction interval [−1.13, +0.27] **crosses zero**
- I² = 48.3%, τ² = 0.070

Pre-specified lab-stratified moderator analysis:

- **UCLA Lieberman/Craske axis only:** g = **−0.74**, 95% CI [−1.02, −0.47], k = 5, I² = 0%
- **Independent laboratories only:** g = **−0.13**, 95% CI [−0.41, +0.14], k = 4, I² = 27.8% — non-significant; CI crosses zero

The 0.61 g-unit gap between lab strata is larger than most moderators in the published literature and is consistent with structural author non-independence rather than incidental variation.

## Repository structure

```
affect-labeling-review/
├── README.md                                  ← this file
├── LICENSE                                    ← CC-BY-4.0 (text) + MIT (code)
├── HOW_TO_PUSH_TO_GITHUB.md                   ← step-by-step upload guide
├── .gitignore
├── references.bib                             ← BibTeX for all references
├── manuscript/
│   └── manuscript.md                          ← full ~14,000-word paper
├── meta-analysis/
│   ├── run_meta_analysis.py                   ← analysis code
│   ├── extracted_effect_sizes.csv             ← input data + extracted g
│   ├── leave_one_out.csv                      ← LOO sensitivity output
│   └── results_summary.txt                    ← plain-text summary
├── prisma/
│   ├── build_prisma.py                        ← PRISMA flow generator
│   └── prisma_counts.txt                      ← exact PRISMA counts
├── supplementary/
│   ├── risk_of_bias.csv                       ← RoB 2 / ROBINS-I judgments
│   └── build_rob_figure.py                    ← traffic-light figure code
├── prereg/
│   └── PROSPERO_preregistration.md            ← full pre-registration
└── figures/
    ├── prisma_flow.png / .pdf                 ← PRISMA 2020 flow diagram
    ├── rob_summary.png / .pdf                 ← risk-of-bias traffic light
    ├── forest_plot.png / .pdf                 ← random-effects forest plot
    └── funnel_plot.png / .pdf                 ← funnel plot
```

## Reproducing the analyses

Three Python scripts regenerate every numerical result and figure:

```bash
pip install numpy pandas scipy matplotlib

cd affect-labeling-review
python meta-analysis/run_meta_analysis.py
python prisma/build_prisma.py
python supplementary/build_rob_figure.py
```

Each script is self-contained, deterministic, and writes output to its own directory or to `figures/`.

## What's verified, what's flagged

The reference list was verified against PubMed, the journal of record, and where available the original published PDFs. **Five citations were corrected** during verification, and **one fabricated reference was removed**:

- Removed: Isaacowitz & Eldesouky (2024) — could not be located in any database; closest real entity is a 2023 conference symposium.
- Corrected: "Wong et al. (2022)" → Plaisted, Waite, & Creswell (2022), *Behaviour Research and Therapy*, 148, 103997. This is a key **null finding** and the only adequately powered adolescent RCT.
- Corrected: Vlasenko et al. (2021) coauthors → Vlasenko, V. V., Rogers, E. G., & Waugh, C. E. (Wake Forest).
- Corrected: Vives et al. (2021) title → "Foreign Language Processing Undermines Affect Labeling."
- Corrected: Givon, Meiran, & Goldenberg (2025) for the *Trends in Cognitive Sciences* piece (was misattributed).
- Several DOIs and article numbers corrected.

The Burklund et al. (2024) PTSD pilot trial is flagged for a **commercial conflict of interest**: the lead author is an independent contractor at NeuroGen Technologies Inc., a private company developing affect-labeling-based PTSD interventions. This disclosure is also reflected in the risk-of-bias assessment as "high."

## Limitations explicitly acknowledged in the manuscript

1. Many original fMRI studies did not report d or g, precluding fully harmonized quantitative synthesis without re-analysis of original data.
2. Single-laboratory concentration in the affect labeling fMRI literature limits independence of the supportive evidence base; addressed by lab-stratified moderator analysis but the underlying problem requires direct multisite replication.
3. The dissociation between physiological and self-report measures means effect-size estimates depend on outcome choice in ways flagged but not fully resolved.
4. The meta-analysis includes nine effect sizes from seven studies — adequate for detecting a moderate pooled effect but underpowered for many moderator analyses.
5. Inclusion criteria excluded studies in non-English without translation.

## Citation

If you use this work, please cite:

```
Wahba, M. A. R. (2026). Putting feelings into words: A systematic review
and meta-analysis of affect labeling. Preprint,
https://github.com/mikhaeelatefrizk/affect-labeling-review.
```

## License

- **Manuscript text and figures:** Creative Commons Attribution 4.0 International (CC-BY-4.0)
- **Code:** MIT License

See `LICENSE` for full terms.

## Contact

Open an issue on this repository.
