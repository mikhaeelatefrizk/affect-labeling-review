# Risk-of-bias judgments — per-study rationale

> Companion document to [`risk_of_bias.csv`](risk_of_bias.csv). For each study assessed, this document explains the rationale behind the per-domain ratings and the overall judgment, so that any reader (especially a re-screener) can verify, contest, or extend the assessment.

The instruments used:

- **RoB 2** (Sterne et al., 2019, *BMJ*, 366, l4898) for randomised trials, with five domains: D1 randomisation; D2 deviations from intended interventions; D3 missing outcome data; D4 outcome measurement; D5 selective reporting.
- **ROBINS-I** (Sterne et al., 2016, *BMJ*, 355, i4919) for non-randomised intervention studies, with seven domains; collapsed to five for compactness.
- **Adapted NRSI tool** for within-subjects experimental designs (no validated tool exists for AL within-subjects fMRI), focusing on order/fatigue confounding, measurement, and reporting.

Ratings: **L** = Low risk · **S** = Some concerns · **M** = Moderate · **H** = High risk · **−** = Not applicable.

---

## Randomised controlled trials (RCTs)

### Kircanski, Lieberman, & Craske (2012) · *Psychological Science*

- **D1 Randomisation: L.** Random allocation reported with 1:1 between-subjects design across labelling, reappraisal, distraction, and exposure-only arms. Allocation concealment is plausible given the lab setting but not described in detail.
- **D2 Deviations: L.** Manipulation was a single-session task; deviations from intended condition would be detectable and were not reported.
- **D3 Missing data: L.** One-week follow-up retention is reported and complete-case analysis is appropriate at this scale.
- **D4 Measurement: S.** SCR is an objective physiological measure (low subjectivity), but outcome assessor blinding to condition during the live-tarantula session is not explicitly described. Marked S rather than L for transparency.
- **D5 Reporting: L.** The pre-registered outcomes are reported; sensitivity analyses across follow-up windows are presented.
- **Overall: S** (driven by D4). The study is an important and methodologically sound demonstration; the "some concerns" rating reflects unspecified outcome-assessor blinding rather than substantive evidence of bias.

### Tabibnia, Lieberman, & Craske (2008), Experiment 2 · *Emotion*

- **D1 Randomisation: L.** Random assignment to negative-label vs. exposure-only is confirmed.
- **D2 Deviations: S.** Brief windows of incomplete blinding are plausible because the labelling instructions cue participants to the manipulation. Marked S for transparency.
- **D3 Missing data: L.** Low attrition reported.
- **D4 Measurement: L.** SCR is objective.
- **D5 Reporting: L.** All registered outcomes presented.
- **Overall: S.**

### Niles, Craske, Lieberman, & Hur (2015) · *Behaviour Research and Therapy*

- **D1 Randomisation: L.** Random assignment confirmed.
- **D2 Deviations: S.** Pre-registration was not located by the review team. The protocol-execution match is plausible but not externally verifiable. Marked S.
- **D3 Missing data: L.** Reasonable retention.
- **D4 Measurement: L.** Non-specific SCR (NS-SCR) is objective.
- **D5 Reporting: S.** Outcome reporting is scattered across measures (NS-SCR during recovery is a specific, narrow window). Marked S because the most-cited result is the recovery-window contrast, which raises the question of selective emphasis.
- **Overall: S.**

### Plaisted, Waite, & Creswell (2022) · *Behaviour Research and Therapy*

- **D1–D5: All L.**
- **Overall: L.** This is the only adequately-powered adolescent RCT in the literature, pre-registered, with faithful reporting of a **null** finding on heart rate, self-rated anxiety, and observer-rated anxiety. It is the highest-quality study in the body of work and an important counterweight to the UCLA-axis affirmative literature.

---

## Non-randomised intervention study (ROBINS-I)

### Burklund, Davies, Niles, Torre, Brown, Vinograd, Lieberman, & Craske (2024) — PTSD pilot · *Frontiers in Psychology*

- **D1 Randomisation: H.** Open-label single-arm pilot trial; no random allocation, no control arm.
- **D2 Deviations: H.** Open-label design means the manipulation is fully unblinded; expectancy effects cannot be separated from the affect-labelling-specific mechanism.
- **D3 Missing data: S.** ~13 completers reported; selective inclusion of completers in main analyses noted.
- **D4 Measurement: S.** Self-report and clinician-rated outcomes are not blinded to condition.
- **D5 Reporting: H.** Selective focus on within-subject pre-post effect sizes; selective emphasis given that the study is also flagged for **commercial conflict of interest** — the lead author is an independent contractor at NeuroGen Technologies Inc., a private company developing affect-labelling-based PTSD interventions.
- **Overall: H.** This study is included for narrative completeness in the clinical-applications section but should not be treated as evidence for affect labelling's clinical efficacy in PTSD.

---

## Within-subjects fMRI / neurophysiology (adapted NRSI tool)

### Lieberman, Eisenberger, Crockett, Tom, Pfeifer, & Way (2007) · *Psychological Science*

- **D1 Selection / order: M.** Within-subjects fMRI block design with N = 30. The sample size is small for fMRI inference (Button et al. 2013); confounding from order effects is partially counterbalanced. Marked M to reflect small-sample inferential limits.
- **D2 Deviations: L.** Within-subjects task is straightforward.
- **D3 Missing data: L.** Excluded scans are documented.
- **D4 Measurement: L.** BOLD signal in pre-defined ROIs is objective.
- **D5 Reporting: M.** Cluster thresholds pre-date Eklund et al. (2016) cluster-failure correction; ROI definition was not pre-registered. Marked M to acknowledge the era's analytic standards.
- **Overall: M.** Foundational paper; the result is plausibly replicable but with smaller effect sizes and tighter inference under modern standards.

### Hariri, Bookheimer, & Mazziotta (2000) · *NeuroReport*

- **D1: M.** N = 11, very small even for the era.
- **D2: L.** D3: L. D4: L.
- **D5: M.** Reported correlations may be inflated (Vul et al. 2009 *voodoo correlations* concern).
- **Overall: M.** Foundational; treat effect-size estimates with skepticism due to small-sample inferential limits.

### Hariri, Mattay, Tessitore, Fera, & Weinberger (2003) · *Biological Psychiatry*

- **D1–D5: All L.**
- **Overall: L.** N = 11 is small, but concurrent SCR cross-validates the fMRI signal and provides a second data stream that is less susceptible to fMRI-specific inference issues.

### Torrisi, Lieberman, Bookheimer, & Altshuler (2013) — DCM · *NeuroImage*

- **D1: M.** Dynamic causal modelling involves substantial researcher degrees of freedom in model selection.
- **D2: L.** D3: L. D4: L.
- **D5: M.** Partial reanalysis of prior data; selective model reporting is plausible.
- **Overall: M.**

### Burklund, Creswell, Irwin, & Lieberman (2014) · *Frontiers in Psychology*

- **D1: M.** Modest N; same lab as the foundational Lieberman 2007 paper.
- **D2: L.** D3: L. D4: L.
- **D5: M.** ROI strategy partially data-driven.
- **Overall: M.**

### Vives, Costumero, Ávila, & Costa (2021) · *Affective Science*

- **D1–D5: All L.**
- **Overall: L.** Independent lab; clear language manipulation (foreign-language vs. native); pre-specified ROI strategy. Reports the opposite-direction effect (foreign-language labelling increases amygdala activation) — a substantive, well-documented contradiction of the canonical claim.

---

## Behavioural / self-report (within-subjects, validated tasks)

### Nook, Satpute, & Ochsner (2021) · *Affective Science*

- **D1–D5: All L.**
- **Overall: L.** Independent lab; clean design; replicated in two studies; data and code on OSF. Reports that emotion naming **impedes** subsequent reappraisal and acceptance — a substantive, well-replicated contradiction of the construct's clinical optimism.

### Ariely, Mokady, Reggev, & Anholt (2026) · *Affective Science*

- **D1–D5: All L.**
- **Overall: L.** Pre-registered conceptual replication of Nook et al. (2021); independent lab; combined N = 226 across two studies.

### Vlasenko, Rogers, & Waugh (2021) · *Cognition and Emotion*

- **D1–D5: All L.**
- **Overall: L.** Independent lab; four studies with consistent direction (labelling **intensifies** positive emotion); total N = 405.

### Levy-Gigi & Shamay-Tsoory (2022) · *PLOS ONE*

- **D1–D5: All L.**
- **Overall: L.** Independent lab; intensity moderator clearly tested.

---

## Coordinate-based / image-based meta-analyses (synthesised narratively)

### Costafreda, Brammer, David, & Fu (2008) — k = 385 · *Brain Research Reviews*

- **D4 Measurement: L.** D5 Reporting: L.
- **Overall: L.** Large k; predictor coding documented. Caveat: between-study heterogeneity inherent to ALE meta-analyses bounds the certainty of the synthesis.

### Brooks, Shablack, Gendron, Satpute, Parrish, & Lindquist (2017) — k = 386 · *SCAN*

- **D4: L.** D5: L. **Overall: L.** Large k; clear inclusion criteria; outputs are activation density rather than effect size — affects how to integrate with the present meta-analysis (used as a narrative anchor only).

### Buhle, Silvers, Wager, Lopez, Onyemekwu, Kober, Weber, & Ochsner (2014) · *Cerebral Cortex*

- **D4: L.** D5: L. **Overall: L.** Reappraisal-focused; affect labelling is not directly synthesised but is informative for context on the broader emotion-regulation neural circuit.

### Berboth & Morawetz (2021) · *Neuropsychologia*

- **D4: L.** D5: L. **Overall: L.** PPI connectivity meta-analysis; left-vlPFC convergence is directly relevant for the lateralisation claim made by Lieberman et al. (2007). The contradiction is noted in the manuscript as a structural challenge to the canonical RVLPFC story.

---

## Cross-study summary of bias signals

| Bias signal | Affected studies | Implication |
|-------------|------------------|-------------|
| Single-laboratory concentration | Lieberman 2007, Hariri 2000, Hariri 2003, Burklund 2014, Burklund 2024, Niles 2015, Tabibnia 2008, Kircanski 2012, Torrisi 2013 (UCLA / collaborators) | The lab-stratified moderator analysis (g = −0.74 UCLA vs. g = −0.13 independent) treats this as a structural, not incidental, feature. |
| Small-sample fMRI | Lieberman 2007, Hariri 2000, Hariri 2003, Torrisi 2013, Burklund 2014 | Effect-size estimates may be inflated; whole-brain power to detect the canonical circuit at modern standards is limited. |
| Commercial COI | Burklund 2024 | Excluded from quantitative synthesis; included only narratively in clinical applications with COI flag. |
| Pre-registration absent | Lieberman 2007, Hariri 2000/2003, Niles 2015 | Selective-reporting risk; all moderate-confidence findings should be re-examined when high-quality replications appear. |

## How to use this document

- For **journal peer reviewers**: this is the source of truth for per-study RoB rationales. The CSV is machine-readable; this markdown is the reasoning.
- For **second-coder re-screeners**: please contest any judgment by opening a [data correction issue](https://github.com/mikhaeelatefrizk/affect-labeling-review/issues/new?template=data_correction.yml). Provide the alternative judgment with supporting evidence; the rationale here will be updated and the CSV regenerated.
- For **ML researchers**: the per-domain codes (`L`, `S`, `M`, `H`) are stable categorical labels suitable for downstream modelling (e.g., predicting RoB from full-text features).

---

*This document is part of the open-research package archived at Zenodo DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595). Last updated for v1.0.0 (May 2026).*
