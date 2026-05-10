# Methodology deep-dive

Justifications for the analytic choices made in the review. Useful for peer reviewers, methodological readers, and anyone replicating with variations.

---

## Why Hedges' *g* and not Cohen's *d*?

Most studies in the body of work have small samples (n = 11 to n = 46 per cell). Cohen's *d* is biased upward in small samples; the bias is approximately *d* × 3/(4·*df* − 1). Hedges (1981) derived a small-sample correction *J* = 1 − 3/(4·*df* − 1), and *g* = *J* × *d* gives an unbiased estimator. With df = 30, *J* ≈ 0.97 — small adjustment but it matters when meta-analytically combining several small studies.

References: Hedges (1981); Borenstein, Hedges, Higgins, & Rothstein (2009).

---

## Why DerSimonian-Laird τ²?

Three estimators were considered:

1. **DerSimonian-Laird (DL)** — method-of-moments, standard, conservative. Tends to under-estimate τ² when k is small and heterogeneity is high.
2. **Restricted Maximum Likelihood (REML)** — better behaviour in moderate-to-large k, theoretically preferred.
3. **Paule-Mandel (PM)** — also conservative, often similar to DL.

I selected DL for the headline analysis because:

- It is what the systematic-review literature has converged on for two decades (i.e., readers will know how to interpret the result).
- With *k* = 9, REML and DL produce nearly identical results in this dataset (verified in the development environment).
- DL's slight downward bias on τ² makes the headline I² and prediction interval *narrower*, which is the conservative direction for claiming heterogeneity is high.

Sensitivity check using REML and PM is mentioned in the pre-registration; numerical agreement is within 0.005 g-units.

---

## Why a 95% prediction interval, not just a 95% CI?

The 95% CI quantifies uncertainty about the *pooled* effect across the studies in the meta-analysis. The 95% prediction interval (PI) quantifies uncertainty about the *next* study's true effect under the random-effects model. The PI is wider because it adds τ² to the variance.

When the headline finding is a pooled *g* = −0.43 (95% CI [−0.68, −0.18]) but a 95% PI of [−1.13, +0.27] **crossing zero**, this is the single most informative summary in the manuscript. It says: yes, the average study shows a labelling-induced reduction, but a new study from a new lab with a new sample is genuinely uncertain in direction.

References: Higgins, Thompson, & Spiegelhalter (2009); Riley, Higgins, & Deeks (2011).

---

## Why a lab-stratified moderator analysis?

The motivating problem: approximately 30 of the 50 most-cited affect-labelling papers come from one laboratory cluster (UCLA Lieberman / Craske / Burklund / Niles / Kircanski / Tabibnia), or from close collaborators. This is a structural — not incidental — feature of the evidence base.

A standard meta-regression (with `lab` as a moderator) would have been underpowered with k = 9 and a binary moderator. Instead, the protocol specified a *subgroup* analysis: pool the UCLA-axis studies separately from the independent-lab studies. This requires only that there be at least 2 studies in each subgroup (we had 5 and 4) and gives a directly interpretable answer: how much does the pooled estimate change when you exclude the originating-laboratory cluster?

The 0.61 g-unit gap (g = −0.74 vs. g = −0.13) is larger than virtually any moderator I could find in the published affect-labelling literature. It is consistent with structural author non-independence — a known concern in research-synthesis methodology (Stanley & Doucouliagos, 2017).

---

## Why three independent risk-of-bias tools?

The body of work mixes:

- **RCTs** (Kircanski 2012, Tabibnia 2008, Niles 2015, Plaisted 2022) — RoB 2 is the current gold standard.
- **Non-randomised intervention studies** (Burklund 2024 PTSD pilot) — ROBINS-I is the appropriate tool.
- **Within-subjects fMRI / behavioural studies** with no formal randomisation — neither RoB 2 nor ROBINS-I fits cleanly. We used an adapted NRSI checklist focused on order/fatigue confounding, measurement, and reporting.
- **Coordinate-based / image-based meta-analyses** (Costafreda 2008, Brooks 2017, Buhle 2014, Berboth 2021) — only the measurement and reporting domains are meaningfully assessable; the others marked N/A.

The trade-off: a single tool would give cleaner machine-readability but would fail to capture the actual sources of bias in this heterogeneous literature.

---

## Why GRADE narrative rather than tabulated?

GRADE involves rating each outcome on five domains (risk of bias, inconsistency, indirectness, imprecision, publication bias) plus three upgrade factors (large effect, dose-response, all plausible confounding works against effect). With a single primary outcome and small-k meta-analysis, the formal tabulation would inflate apparent rigour without adding information beyond the narrative discussion. The manuscript's §4.1 and §4.2 summarise the body-of-evidence judgments in prose.

A formal tabulated GRADE rating could be added in a future revision; this would be a welcome contribution.

---

## Why "single-coder" instead of "second coder"?

The pre-registered protocol called for two independent reviewers (Section 19 of [`prereg/PROSPERO_preregistration.md`](../prereg/PROSPERO_preregistration.md)). In execution, screening and extraction were carried out by a single reviewer.

This is documented as a deviation in three places: the PROSPERO file Section 19 and 20; the manuscript Limitations section; and `data/screening/README.md`. The honest framing is: the work was done well by one careful person; the inter-rater agreement statistic that the protocol intended to publish is therefore not available.

A second-coder re-screening pass is welcome and would substantially strengthen the dataset's value for ML benchmarking.

---

## Why include the Burklund 2024 PTSD pilot despite its high RoB and COI?

Three reasons:

1. **Narrative completeness.** It is the most prominent recent clinical-translation claim and would be conspicuous by its absence.
2. **Honest critique.** Reading the manuscript with this study front-and-centre, with the COI and design issues clearly flagged, is more informative than reading without it.
3. **Anti-COI signal.** Excluding the study because of the COI would create the appearance of cherry-picking inclusions to support our conclusions. Including it with full RoB rating = High and the COI explicitly noted does the opposite.

The manuscript is explicit that this study should *not* be treated as evidence for affect-labelling efficacy in PTSD; this is consistent with how pre-registered SLRs handle commercial-bias concerns.

---

## Why exclude the foundational Schachter & Singer (1962) and James (1884) from the meta-analysis?

Both are theoretical / framework papers, not empirical affect-labelling manipulations. They are cited extensively in the manuscript's introduction as historical anchors but do not meet the eligibility criteria for the synthesis.

The eligibility criteria deliberately exclude pre-empirical theoretical antecedents, despite their canonical importance.

---

## Why no protocol amendment for "single-coder"?

Two options were considered when the deviation became unavoidable:

1. **Amend the protocol** to specify single-coder execution. This is what PROSPERO recommends for substantive deviations.
2. **Document as a deviation** without amending. Honest about the gap between intent and execution.

I chose (2) because the protocol-as-pre-registered captures *what was intended*, and the deviation note captures *what was done*. Amending would have washed out the gap. The deviation is documented in three places (see above).

---

## Why is the "Independent labs" pooled estimate reported even though k = 4 is small?

Because the lab-stratified moderator analysis is the *headline* result of the review. Reporting only the UCLA-axis subgroup would amount to saying "the effect is robust within UCLA studies"; reporting only the pooled k = 9 would mask the lab dependence. The full picture requires reporting both subgroups, even at the cost of small-k inferential limits in the independent-labs subgroup.

The manuscript is explicit that the independent-labs estimate is non-significant and that the CI crosses zero. This is the primary substantive finding of the review: the canonical effect attenuates substantially outside the originating laboratory.

---

## Why preserve the "Lieberman 2007 single-paper" status as foundational rather than treating it as one study among many?

Lieberman et al. (2007) is the foundational paper for the modern affect-labelling research program. Treating it as one study among many would understate its citation-driving role and the construct-validity claims that downstream studies make about *replicating Lieberman 2007*. The manuscript is explicit about this framing.

For the meta-analysis itself, the foundational paper is treated as one study among many — its effect size enters the calculation alongside Tabibnia 2008, Kircanski 2012, etc. The "foundational" framing affects how the result is *discussed*, not how it is *computed*.

---

*This document is part of the open-research package archived at Zenodo DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595). Last updated for v1.0.0 (May 2026).*
