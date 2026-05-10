# Glossary

Plain-language definitions for terms used throughout the open-research package. Useful for students from outside systematic-review methodology, machine-learning researchers new to evidence synthesis, and clinicians reading the manuscript.

Terms are grouped by topic and listed alphabetically within each group.

---

## The construct itself

**Affect labelling.** The act of producing or selecting a verbal label (e.g., "afraid," "frustrated," "elated") for an affective stimulus or felt internal state. In psychology and neuroscience, "affect labelling" specifically denotes a *manipulation* — instructing or inviting a participant to label, then measuring whether labelling changes a downstream emotional outcome.

**Amygdala.** A small almond-shaped subcortical structure (one in each hemisphere) implicated in detecting and responding to emotionally salient stimuli, especially threat. The canonical claim of the affect-labelling literature is that labelling reduces amygdala BOLD response.

**Cognitive reappraisal.** A different emotion-regulation strategy in which the *meaning* of a stimulus is reinterpreted (e.g., re-framing a threatening picture as fictional). Distinct from affect labelling but compared to it in many studies.

**Implicit emotion regulation.** Emotion regulation that occurs without metacognitive awareness or deliberate strategy use. Lieberman et al. (2011) framed affect labelling as implicit emotion regulation: people predict labelling will worsen distress but it actually reduces it.

**vlPFC / RVLPFC.** Ventrolateral prefrontal cortex / right ventrolateral prefrontal cortex. The cortical region the canonical affect-labelling circuit posits as the source of top-down regulation (RVLPFC → mPFC → amygdala).

---

## Systematic-review methodology

**GRADE.** Grading of Recommendations Assessment, Development and Evaluation. A framework for rating certainty in a body of evidence (high / moderate / low / very low).

**Inter-rater agreement (Cohen's κ).** A statistic measuring agreement between two or more raters' classification decisions, corrected for chance agreement. κ ≥ 0.70 is a common threshold for "substantial agreement"; the pre-registered protocol required κ ≥ 0.70 for screening to proceed.

**PRISMA 2020.** Preferred Reporting Items for Systematic Reviews and Meta-Analyses, 2020 update. The reporting standard for systematic reviews. The 27-item checklist tells journals what a high-quality systematic review report must contain. See [`prisma/PRISMA_2020_checklist.md`](../prisma/PRISMA_2020_checklist.md).

**PRISMA flow diagram.** A standardised diagram showing how records moved through identification, screening, eligibility, and inclusion stages of a systematic review. See [`figures/prisma_flow.pdf`](../figures/prisma_flow.pdf).

**PRISMA-S.** PRISMA Search reporting extension. Adds detailed reporting requirements for the search strategy itself, beyond what PRISMA 2020 requires. See [`data/searches/PRISMA-S_checklist.md`](../data/searches/PRISMA-S_checklist.md).

**PROSPERO.** International Prospective Register of Systematic Reviews, hosted by the University of York. Protocol pre-registration registry for systematic reviews and meta-analyses.

**Risk of bias (RoB).** A judgment about whether a specific study's design, conduct, or analysis introduces systematic error that could affect its results. Evaluated per-domain (e.g., randomisation, blinding) and overall, using validated tools like RoB 2 for RCTs.

**RoB 2.** Risk of Bias 2 (Sterne et al., 2019). The current gold-standard tool for assessing risk of bias in randomised trials, with five domains.

**ROBINS-I.** Risk Of Bias In Non-randomised Studies of Interventions. The tool used for non-randomised studies (Sterne et al., 2016).

**Title/abstract screening.** The first stage of study selection in a systematic review: rapidly judging from the title and abstract alone whether a record is potentially eligible. Records that pass move on to full-text assessment.

---

## Meta-analysis statistics

**Cohen's *d*.** A standardised mean difference: the difference between two group means divided by their pooled standard deviation. *d* = 0.2 / 0.5 / 0.8 are conventional small / medium / large benchmarks.

**Confidence interval (95% CI).** A range of values such that, under repeated sampling, 95% of intervals constructed this way would contain the true value. **Not** the same as "95% probability the true value is in this interval" (that's a Bayesian credible interval).

**DerSimonian-Laird estimator.** A method-of-moments estimator for τ² (between-study heterogeneity) in random-effects meta-analysis. Standard, conservative.

**Egger's test.** A regression-based test for funnel-plot asymmetry, often used as evidence for small-study effects or publication bias. Underpowered with small *k*; we report its result for completeness but interpret cautiously.

**Fixed-effect vs. random-effects.** Two assumptions for combining studies. Fixed-effect assumes one true underlying effect across all studies; random-effects allows the true effect to vary across studies and explicitly models that variance (τ²). Random-effects is the appropriate default when studies vary in population, intervention details, or measurement.

**Forest plot.** A graphical display of effect sizes from multiple studies, with each study's CI as a horizontal line and the pooled estimate as a diamond at the bottom. See [`figures/forest_plot.pdf`](../figures/forest_plot.pdf).

**Funnel plot.** A scatter of effect size (x-axis) vs. precision (y-axis, often inverse standard error). Asymmetry in the funnel can suggest publication bias or genuine heterogeneity. See [`figures/funnel_plot.pdf`](../figures/funnel_plot.pdf).

**Hedges' *g*.** A small-sample-corrected version of Cohen's *d*. Used in this review because most studies have small samples (n < 50). Computed as *g* = *d* × *J*, where *J* = 1 − 3/(4·*df* − 1).

**Heterogeneity.** Variation in true effects across studies in a meta-analysis. Quantified by τ² (variance), I² (proportion of variance due to heterogeneity), and the 95% prediction interval.

**I² (I-squared).** The proportion of total variance in a meta-analysis attributable to between-study heterogeneity (vs. within-study sampling variance). 25% / 50% / 75% are conventional thresholds for low / moderate / high heterogeneity.

**Leave-one-out (LOO) analysis.** A sensitivity analysis: drop each study in turn and re-compute the pooled effect. If the result depends critically on a single study, the meta-analysis is fragile.

**Meta-regression.** A regression of effect sizes on study-level moderators (e.g., year, sample size, lab affiliation). Used to explain heterogeneity. With small *k*, meta-regression is underpowered and we relied instead on lab-stratified subgroup analysis.

**95% prediction interval (PI).** The interval into which the true effect of a *new* study is expected to fall, with 95% probability under the random-effects model. Wider than the CI because it incorporates between-study heterogeneity. A PI that crosses zero means a new study could plausibly observe an effect in either direction.

**P-curve.** A distribution of *p*-values from a body of studies, used to detect publication bias and *p*-hacking. Not run in this review (k = 9 is too small).

**PET-PEESE.** Two regression-based small-study-bias adjustments. Not run on k = 9.

**Pooled effect size.** The summary estimate from a meta-analysis, weighted by precision (1/variance for fixed-effect; 1/(variance + τ²) for random-effects).

**τ² (tau-squared).** The estimated variance of the true effect across studies in random-effects meta-analysis. Square root τ is the standard deviation of the true effect distribution.

---

## Machine-learning terminology (used in `for-ml-researchers.md`)

**BALD.** Bayesian Active Learning by Disagreement. An active-learning query strategy: select instances that maximise the expected reduction in posterior uncertainty.

**Class weighting.** In imbalanced classification, multiplying the loss for minority-class examples by a factor inversely proportional to class frequency. Used as a baseline when working with PU or heavily-imbalanced data.

**Focal loss.** A modified cross-entropy loss that down-weights easy examples; helpful for severe class imbalance.

**nnPU.** Non-negative positive-unlabelled learning (Kiryo et al., 2017). A PU-learning method that constrains an empirical risk estimator to be non-negative, addressing instability of the unbiased PU loss with small positive priors.

**Positive-unlabelled (PU) learning.** A classification setup in which only some positives are labelled and all negatives are mixed in with unlabelled positives in the "unlabelled" pool. Standard supervised learning is a special case where the unlabelled set is fully negative.

**Precision @ K.** The fraction of the top-K ranked candidates that are true positives. Common in screening / triage settings where a human reviews the top-K and effort is bounded.

**PubMedBERT / SciBERT / BioBERT.** Domain-pretrained transformer language models. Pretrained on biomedical or scientific abstracts; produce better representations for SLR-screening tasks than general-purpose BERT.

**TF-IDF.** Term frequency–inverse document frequency. A classic vector representation of text: word counts re-weighted to down-weight common words. A reasonable baseline before neural methods.

---

## Project-specific terms

**Canonical-identifiable include.** A study that I can confidently identify as one of the 100 canonical includes, because it is enumerated in structured form in either `meta-analysis/run_meta_analysis.py` (the k = 9 effect sizes) or `supplementary/build_rob_figure.py` (the 19 RoB-assessed studies). Fewer than 100 because the original review preserved per-paper structure only for the meta-analysed and RoB-assessed subsets.

**Concept DOI vs. version DOI.** Zenodo issues two DOIs per archived release: a concept DOI (e.g., 10.5281/zenodo.20109595) that always resolves to the latest version, and a version DOI (e.g., 10.5281/zenodo.20109596) that points at one specific version. Use the concept DOI in citations unless the version is load-bearing.

**Derived corpus.** The set of records re-retrieved from PubMed today by re-running the pre-registered Boolean query via the NCBI E-utilities API. Distinct from the canonical 1,842 records originally retrieved across five databases (which were not preserved per-record).

**Derived screening log.** The derived corpus joined against the canonical-identifiable include list, with each row tagged `decision = "include"` or `decision = "unknown"`. This is the file ML researchers train on.

**Lab-stratified analysis.** A pre-specified moderator analysis dividing the meta-analytic studies by laboratory affiliation: UCLA Lieberman/Craske axis (and close collaborators) vs. independent laboratories. The headline finding is a 0.61 g-unit gap between the two strata (g = −0.74 vs. g = −0.13).

**UCLA axis.** Shorthand for the Lieberman / Craske / Burklund / Niles / Kircanski / Tabibnia laboratory cluster at UCLA. Approximately 30 of the 50 most-cited affect-labelling papers come from this axis or close collaborators.

---

## License

This glossary is released under [CC-BY-4.0](../LICENSE-MANUSCRIPT). Suggestions for additional entries are welcomed via repository issues.
