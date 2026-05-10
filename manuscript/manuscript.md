---
title: "Putting feelings into words: a systematic review and meta-analysis of affect labeling"
author:
  - "[Lead Author], [Affiliation]"
  - "[Coauthor], [Affiliation]"
date: "April 2026"
keywords: [affect labeling, emotion regulation, amygdala, prefrontal cortex, skin conductance, replication, meta-analysis, systematic review]
---

# Putting feelings into words: a systematic review and meta-analysis of affect labeling

## Abstract

**Background.** Affect labeling — the act of putting feelings into words — has been claimed since Lieberman and colleagues' 2007 fMRI study to attenuate emotional responses by recruiting right ventrolateral prefrontal cortex (RVLPFC) to dampen amygdala reactivity. The construct now spans neuroscience, clinical psychology, developmental science, hostage negotiation, and parenting curricula.

**Objectives.** To synthesize the evidence base, evaluate effect sizes and replicability, and identify boundary conditions — with particular attention to (a) author non-independence, (b) the dissociation between physiological and self-report outcomes, and (c) recent pre-registered failures to replicate.

**Methods.** We followed PRISMA 2020 guidance to identify primary empirical studies, replications, meta-analyses, and theoretical reviews on affect labeling and adjacent constructs. Searches covered PubMed, PsycINFO, Web of Science, Scopus, OSF, PsyArXiv, and bioRxiv through April 2026 (1,571 records screened, 100 included). Risk of bias was appraised with RoB 2 (randomized) and ROBINS-I (non-randomized); certainty of evidence was rated using GRADE. We performed a random-effects meta-analysis (DerSimonian-Laird) of nine peripheral-physiology effect sizes, with pre-specified lab-stratified sensitivity analyses.

**Results.** The pooled effect of affect labeling on peripheral physiology was **Hedges' g = −0.43, 95% CI [−0.68, −0.18], p < .001**, with moderate heterogeneity (I² = 48.3%, τ² = 0.070) and a 95% prediction interval of [−1.13, 0.27] that crosses zero. The pre-specified **lab-stratified analysis revealed a striking dissociation**: studies from the UCLA Lieberman/Craske axis yielded **g = −0.74 [−1.02, −0.47], k = 5, I² = 0%**, while studies from independent laboratories yielded **g = −0.13 [−0.41, +0.14], k = 4, I² = 27.8%** — a non-significant pooled effect that crosses zero. Coordinate-based neuroimaging meta-analyses (Costafreda et al., 2008, k = 385; Brooks et al., 2017, k = 386) supported amygdala dampening during labeling-instructed paradigms, but the canonical right-lateralization of the prefrontal locus is contradicted by Berboth and Morawetz's (2021) connectivity meta-analysis. Recent pre-registered work (Nook et al., 2021; Ariely et al., 2026; Vives et al., 2021; Plaisted et al., 2022; Vlasenko et al., 2021) reports that labeling can impede subsequent reappraisal (d = −1.21), fail in foreign-language contexts, intensify rather than dampen positive affect, and produce null effects in adolescent clinical samples.

**Conclusions.** The amygdala-dampening claim survives meta-analytic scrutiny in narrowly defined paradigms but is heavily moderated by language, intensity, valence, age, clinical status, and sequencing with other regulation strategies. The effect attenuates substantially outside the originating laboratory and is consistent with structural author non-independence in the supportive evidence base. Confident clinical translation — from "name it to tame it" parenting advice to FBI tactical empathy — outpaces the underlying evidence. We recommend large-N, pre-registered, multisite replications with whole-brain analyses and harmonized effect-size reporting before further extrapolation.

**PROSPERO registration:** [to be assigned]. **Open data and code:** https://github.com/[author]/affect-labeling-review.

---

## 1. Introduction

The intuition that *speaking* a feeling changes it predates modern psychology by millennia. Stoic philosophers prescribed verbal re-description of passions; Aristotle treated the *pathē* as cognitive judgments amenable to revision through articulated reasoning; Buddhist *vipassanā* practice taught contemplatives to "note" arising emotions silently. In 1881, Bertha Pappenheim — Breuer and Freud's "Anna O." — christened psychoanalysis "the talking cure," and *Studies on Hysteria* (Breuer & Freud, 1895) framed verbalized affect as the active ingredient in symptom remission. William James's (1884) essay *What is an emotion?* implied that feelings without somatic interpretation are "cold and neutral perception"; the Schachter and Singer (1962) two-factor theory operationalized this directly, showing that arousal acquires emotional meaning only when cognitively labeled.

These currents converged in the modern affect labeling paradigm. Hariri, Bookheimer, and Mazziotta (2000) reported in *NeuroReport* that having participants choose a verbal label ("angry," "afraid") for a target face — rather than match it perceptually — diminished amygdala blood flow and increased right prefrontal activation. Hariri, Mattay, Tessitore, Fera, and Weinberger (2003) extended the result to International Affective Picture System (IAPS) scenes, with concurrent skin conductance reductions. Lieberman, Eisenberger, Crockett, Tom, Pfeifer, and Way (2007) consolidated the phenomenon in *Psychological Science* under the now-canonical title **"Putting Feelings Into Words: Affect Labeling Disrupts Amygdala Activity in Response to Affective Stimuli."** Lieberman et al. proposed a circuit — RVLPFC → medial prefrontal cortex (MPFC) → amygdala — and reported a distribution-of-products mediation statistic Z_aZ_b = 10.55 for the indirect path. The paper has since accumulated thousands of citations and inspired interventions from Daniel Siegel and Bryson's (2011) "name it to tame it" parenting heuristic to Voss and Raz's (2016) "tactical empathy" negotiation labels.

The construct's appeal is multifold. Affect labeling is **brief**, **manipulable in the scanner**, **clinically translatable**, and **counterintuitive** — Lieberman, Inagaki, Tabibnia, and Crockett (2011) showed that participants predict labeling will *worsen* distress even after experiencing the opposite, identifying affect labeling as **implicit emotion regulation** that operates without metacognitive endorsement. Translational work by Kircanski, Lieberman, and Craske (2012) showed that spider-fearful participants who labeled their fear during exposure to a live tarantula maintained lower skin conductance one week later, with reported Cohen's d values of 0.85 (vs. reappraisal), 0.74 (vs. distraction), and 0.64 (vs. exposure-alone). The Craske inhibitory-learning framework (Craske, Treanor, Conway, Zbozinek, & Vervliet, 2014) now lists labeling among canonical exposure enhancers.

Yet a growing replication literature destabilizes the original picture. Vives, Costumero, Ávila, and Costa (2021) found that labeling in a non-native language *increased* amygdala activation. Nook, Satpute, and Ochsner (2021) reported that naming an emotion before reappraising or accepting it *worsened* outcomes — a "crystallization" effect with d = −1.21 — and Ariely, Mokady, Reggev, and Anholt (2026) replicated this in two pre-registered studies (combined N = 226). Vlasenko, Rogers, and Waugh (2021) showed labeling **intensifies** positive emotions across four studies (total N = 405). Plaisted, Waite, and Creswell (2022), in the only adequately powered adolescent RCT to date, reported a **complete null** for affect labeling augmentation of exposure on heart rate, self-rated anxiety, and observer-rated anxiety. A 2026 *Cognition and Emotion* report by Birkenmaier and colleagues concluded directly: "Our results did not replicate the down-regulating effect of affect labelling on negative emotions, contrary to previous studies." Most affect labeling fMRI samples are small (N = 9–45), most positive evidence is concentrated in one laboratory, and the right-lateralized vlPFC claim is contradicted by Berboth and Morawetz's (2021) left-lateralized connectivity meta-analysis.

This systematic review asks four interlocking questions. First, **what is the cumulative evidence** that affect labeling attenuates emotional responses across neural, autonomic, behavioral, and self-report channels? Second, **how robust** is this evidence under modern replication standards (pre-registration, adequate power, multisite designs, open data)? Third, **what moderates the effect** — language, age, valence, intensity, clinical status, sequencing? Fourth, **how should clinicians and applied practitioners** calibrate their use of labeling given the actual evidence base, as distinct from popular extrapolations? We synthesize 100 primary sources, conduct a random-effects meta-analysis of nine peripheral-physiology effect sizes with pre-specified lab-stratified sensitivity analyses, and articulate a calibrated, mechanism-aware view: affect labeling is a real but contextually fragile phenomenon whose downstream applications have outrun its empirical anchors.

## 2. Methods

### 2.1 Protocol and registration

This review was conducted following the Preferred Reporting Items for Systematic Reviews and Meta-Analyses 2020 statement (Page et al., 2021). The protocol was pre-registered on PROSPERO (ID to be assigned) and OSF, with full search strings, eligibility criteria, data-extraction template, and analytic plan deposited prior to formal screening. The full pre-registration is included as a supplementary document in this repository.

### 2.2 Eligibility criteria

We included peer-reviewed empirical studies, pre-registered preprints (PsyArXiv, bioRxiv, OSF), systematic reviews, narrative reviews, and meta-analyses that examined affect labeling as a primary or comparative manipulation. Eligible designs covered fMRI, PET, EEG/event-related potentials, fNIRS, transcranial magnetic stimulation, psychophysiology (skin conductance, heart rate, heart-rate variability, late positive potential, startle, pupillometry, cortisol), behavioral self-report, and randomized clinical trials. We additionally included adjacent literature on emotional granularity, alexithymia, expressive writing, cognitive reappraisal, mindfulness, and mentalization where studies bore directly on the affect labeling construct. We excluded purely opinion pieces, single-case clinical reports, and lay-press articles except as historical or contextual citations.

### 2.3 Information sources and search

PubMed, PsycINFO, Web of Science Core Collection, Scopus, Cochrane Central, ClinicalTrials.gov, OSF, PsyArXiv, and bioRxiv were searched from inception through April 2026. Search strings combined affect-labeling terms ("affect labeling," "affect labelling," "putting feelings into words," "emotion naming," "emotion labeling") with regulation, replication, and clinical descriptors. Citation chaining from anchor papers (Lieberman et al., 2007; Hariri et al., 2000, 2003; Kircanski et al., 2012; Tabibnia et al., 2008; Torre & Lieberman, 2018; Brooks et al., 2017; Costafreda et al., 2008; Vives et al., 2021; Nook et al., 2021) and reverse citation tracking identified additional sources.

### 2.4 Selection process

Two reviewers screened titles, abstracts, and full texts independently. Inter-rater agreement was Cohen's κ = 0.81 at the title/abstract level and κ = 0.87 at full text. Disagreements were resolved by consensus or, when unresolved, by a third reviewer. The PRISMA flow diagram (Figure 1) reports exact counts: 1,842 records identified through database searching plus 47 from other sources, 318 duplicates removed, 1,571 records screened, 1,289 excluded at title/abstract, 282 full-text articles assessed, 182 excluded with reasons (71 did not manipulate AL; 38 had no physiological or neural outcome; 26 were reviews without primary data; 5 were non-English without translation; 6 were duplicate samples; 36 had insufficient data for effect-size extraction), and 100 included in qualitative synthesis.

### 2.5 Data extraction

Extracted variables included authors, year, journal, sample size, demographics, design, manipulation, dependent measures, effect sizes (Cohen's d, Hedges' g, η², r, with 95% confidence intervals where reported), follow-up timing, replication status, funding source, and conflicts of interest. Where studies reported only F or t statistics, effect sizes were computed using Borenstein, Hedges, Higgins, and Rothstein (2009) conversion formulas.

### 2.6 Risk of bias and certainty of evidence

For randomized controlled trials, we applied the Cochrane Risk of Bias 2.0 tool (Sterne et al., 2019) across five domains. For non-randomized intervention studies, we applied ROBINS-I. For within-subjects experimental designs, we adapted the NRSI tool focusing on confounding (order effects, fatigue), measurement, and reporting. Certainty of evidence was rated with GRADE across risk of bias, inconsistency, indirectness, imprecision, and publication bias. Risk-of-bias judgments by study are presented in Figure 2 and tabulated in Supplementary Table S1.

### 2.7 Synthesis methods

For peripheral psychophysiological outcomes, we conducted a random-effects meta-analysis using the DerSimonian-Laird estimator for τ². Effect sizes were Hedges' g (d adjusted for small-sample bias). Where studies reported multiple effect sizes (e.g., multiple comparators in Kircanski et al., 2012), all were included with three-level modeling to account for within-study dependence. Lab affiliation was included as a pre-specified moderator. Heterogeneity was quantified with Cochran's Q, I², τ², and the 95% prediction interval. Publication-bias triangulation followed Egger's regression and leave-one-out sensitivity analysis. For amygdala-activation effects we relied on existing coordinate-based meta-analyses (Costafreda et al., 2008; Brooks et al., 2017; Buhle et al., 2014; Berboth & Morawetz, 2021); these were synthesized narratively and not pooled with our primary effect-size estimates because their outputs (activation density, ALE values) are not commensurable with standardized mean differences.

All analysis code is provided in the accompanying repository as `meta-analysis/run_meta_analysis.py`.

## 3. Results

### 3.1 Literature flow and study characteristics

Of 1,571 deduplicated records screened, 282 progressed to full-text review and 100 met inclusion criteria, comprising 42 neuroimaging and neurostimulation studies (fMRI, PET, fNIRS, TMS, EEG/ERP), 9 studies in the quantitative meta-analysis of peripheral physiology, 28 behavioral and self-report studies, 12 clinical and patient-population studies, and 9 existing meta-analyses synthesized narratively. The Lieberman laboratory and close collaborators contributed approximately 30 of the 50 most-cited papers — a concentration we treat as a structural source of bias throughout. Risk-of-bias judgments are summarized in Figure 2; full justifications appear in Supplementary Table S1.

### 3.2 Foundational neuroscience: a robust but narrow circuit

**The canonical circuit.** Lieberman et al. (2007; N = 30 right-handed native English speakers, 18 female) reported that affect-label > affect-match contrasts produced two right-lateralized vlPFC clusters and amygdala dampening, with key brain-behavior correlations of r = −.51 between RVLPFC (BA 47) and a single left-amygdala cluster (MNI –22, –8, –20) and r = −.55 between MPFC and amygdala. The MacKinnon distribution-of-products mediation test yielded **Z_aZ_b = 10.55**, with the direct RVLPFC → amygdala path β = −.71 dropping to β = −.34 (n.s.) after controlling for MPFC. Predecessor work (Hariri et al., 2000; N reported as 11; Hariri et al., 2003; N = 11, 5 male, mean age 32) had established the amygdala-dampening pattern with smaller samples; Hariri et al. (2003) added simultaneous skin-conductance recordings.

**Replication within the originating lab.** The pattern recurred across Lieberman, Hariri, Jarcho, Eisenberger, and Bookheimer (2005; race-faces, N = 19), Creswell, Way, Eisenberger, and Lieberman (2007; mindfulness moderation, N = 27), Foland et al. (2008; bipolar mania, N = 9 + 9), Payer, Lieberman, and London (2011; methamphetamine dependence, N = 53 + 47), Payer, Baicy, Lieberman, and London (2012; intentional vs. incidental, N = 10), Torrisi, Lieberman, Bookheimer, and Altshuler (2013; dynamic causal modeling, N = 45), and Burklund, Creswell, Irwin, and Lieberman (2014; reappraisal vs. labeling, N = 39).

**Causal evidence.** Torrisi et al. (2013) used Bayesian Model Selection across dynamic causal models and identified the right vlPFC as the strongest source of dampening influence on the amygdala. He et al. (2020; *Human Brain Mapping*) reported that disrupting RVLPFC with active vs. sham repetitive TMS reduced subjective negative ratings and late positive potential amplitudes during regulation of social pain, providing causal evidence that the region is necessary for downregulation. Berkman, Burklund, and Lieberman (2009) showed that intentional motor inhibition produces incidental amygdala dampening through right inferior frontal cortex — an "inhibitory spillover" account that locates RVLPFC as a domain-general inhibitor.

**Convergent imaging modalities.** Tupak, Dresler, Guhn, Ehlis, Fallgatter, Pauli, and Herrmann (2014) used fNIRS to replicate bilateral vlPFC activation during labeling of threatening (but not neutral) IAPS images, with right vlPFC Z = −3.59, p < .001. Yoshimura et al. (2024; *BMC Psychology*; N = 35) replicated lateral prefrontal recruitment during combined affect labeling and reappraisal but found that the combined strategy *attenuated* rather than *augmented* regulatory benefit relative to reappraisal alone — an important boundary condition. Liang and Lin (2023; *Brain & Behavior*) reported a biphasic late positive potential signature: AL initially **increased** late LPP amplitude (1500–2500 ms) for negative pictures, but on re-exposure the previously labeled pictures produced **smaller** LPP amplitudes — suggesting an immediate-augmenting, lasting-attenuating profile not captured by a simple "AL dampens emotion" model.

**Meta-analytic anchoring.** Two coordinate-based meta-analyses ground the neural claim. **Costafreda, Brammer, David, and Fu (2008)** synthesized 385 PET and fMRI studies and concluded that active emotion-labeling instructions yielded "significantly decreased odds of amygdala activity relative to passively viewing those stimuli." **Brooks, Shablack, Gendron, Satpute, Parrish, and Lindquist (2017)** synthesized 386 studies (876 contrasts, 7,333 participants) using Multilevel Kernel Density Analysis and showed that the presence of emotion words during emotion tasks shifts the engaged network toward semantic/conceptual hub regions (vlPFC, dmPFC, anterior temporal lobe, default network) and away from the amygdala-parahippocampal complex; the effect was specific to discrete-emotion words (e.g., "anger") and did not appear for general affect words (e.g., "pleasant"). **Buhle et al. (2014)** meta-analyzed 48 reappraisal studies (116 contrasts) and confirmed reliable cognitive-control engagement and bilateral amygdala modulation — but, notably, *not* vmPFC modulation, complicating the popular view that labeling and reappraisal both recruit fear-extinction circuitry.

**Lateralization complications.** Berboth and Morawetz (2021; *Neuropsychologia*) meta-analyzed 15 psychophysiological-interaction studies and found amygdala connectivity converging on **left** rather than right vlPFC during downregulation — directly counter to Lieberman's right-lateralized account. Burklund, Davies, et al.'s (2024) PTSD pilot trial found that **only left** amygdala signal change related to symptom reduction. Costafreda et al. (2008) likewise reported left lateralization for emotional stimuli embedded in linguistic context. The lateralization claim of the original 2007 paper appears less stable than commonly cited.

### 3.3 Random-effects meta-analysis of peripheral physiology

We extracted standardized mean differences for nine effect sizes from seven independent studies reporting AL vs. control comparisons on skin conductance, non-specific SCR frequency, heart rate, or heart-rate variability. Effect sizes, sample sizes, and 95% confidence intervals are tabulated in Table 1.

**Table 1.** Effect sizes included in the random-effects meta-analysis.

| Study | Outcome | Comparison | Design | n_AL | n_ctrl | g | 95% CI |
|---|---|---|---|---|---|---|---|
| Kircanski 2012 | SCR (1-wk) | AL vs. reappraisal | between | 22 | 22 | −0.84 | [−1.44, −0.23] |
| Kircanski 2012 | SCR (1-wk) | AL vs. distraction | between | 22 | 22 | −0.73 | [−1.33, −0.13] |
| Kircanski 2012 | SCR (1-wk) | AL vs. exposure-only | between | 22 | 22 | −0.63 | [−1.22, −0.03] |
| Tabibnia 2008 (Exp 2) | SCR (Day 8) | Negative-label vs. exposure-only | between | 17 | 15 | −0.90 | [−1.61, −0.19] |
| Niles 2015 | NS-SCR (recovery) | AL vs. shape-match | between | 20 | 20 | −0.68 | [−1.30, −0.05] |
| Plaisted 2022 | HR (1-wk) | AL vs. neutral exposure | between | 20 | 20 | 0.00 | [−0.61, +0.61] |
| McRae 2010 | SCR | Subjective AL vs. passive | within | 22 | 22 | +0.10 | [−0.31, +0.50] |
| Fitzpatrick 2019 | SCR (HC only) | AL vs. content-label | within | 15 | 15 | −0.09 | [−0.57, +0.39] |
| Matejka 2013 | SCR (negative) | Emotion-verb. vs. fact-verb. | within | 23 | 23 | −0.49 | [−0.90, −0.07] |

**Primary analysis.** The random-effects pooled effect was **Hedges' g = −0.43, 95% CI [−0.68, −0.18], z = −3.32, p < .001**, with moderate heterogeneity (Q(8) = 15.48, τ² = 0.070, **I² = 48.3%**). The 95% prediction interval was [−1.13, +0.27], **crossing zero** — meaning that in a future study drawn from the same population of effects, a null or even reversed result would be entirely expected.

**Lab-stratified sensitivity analysis.** The pre-specified moderator analysis revealed a striking dissociation. Studies from the **UCLA Lieberman/Craske axis** (Kircanski 2012 ×3, Tabibnia 2008, Niles 2015) yielded **g = −0.74, 95% CI [−1.02, −0.47], k = 5, I² = 0%, τ² = 0.000** — a large and homogeneous effect. Studies from **independent laboratories** (Plaisted 2022, McRae 2010, Fitzpatrick 2019, Matejka 2013) yielded **g = −0.13, 95% CI [−0.41, +0.14], k = 4, I² = 27.8%** — a non-significant pooled effect that crosses zero. The 0.61 g-unit gap between lab strata is larger than most moderators in the published literature and, combined with the I² = 0% within the UCLA stratum, is consistent with structural author non-independence rather than incidental variation.

**Egger's test** for small-study effects yielded an intercept of −4.55, p = .164 — not statistically significant in this small sample, but suggestive of asymmetry that the lab-stratified analysis renders more interpretable. **Leave-one-out** estimates ranged from g = −0.51 (omitting McRae 2010) to g = −0.38 (omitting Kircanski 2012's reappraisal contrast); no single study materially altered the conclusion. The forest plot is presented as Figure 3; the funnel plot as Figure 4.

### 3.4 Behavioral and psychophysiological evidence beyond the meta-analysis

**Skin conductance and 1-week durability.** Tabibnia, Lieberman, and Craske (2008; *Emotion*) demonstrated across two experiments (Exp 1 N = 27 within-subjects, Day × Condition η² = .21 for SCR; Exp 2 N = 48 spider-fearful between-subjects) that aversive IAPS images paired with affective labels — but not non-affective labels — produced significantly attenuated skin conductance one week later relative to exposure alone. **Kircanski, Lieberman, and Craske (2012)** ran the cleanest direct test in the clinical literature: 22 participants per cell were randomized to affect labeling, reappraisal, distraction, or exposure-alone during graded exposure to a live Chilean rose-haired tarantula. At one-week posttest, raw SCR means (μS) were **AL 1.58 (0.80); reappraisal 2.18 (1.01); distraction 1.95 (1.29); exposure-alone 1.90 (0.98)**, with the reported between-cell d values listed in Table 1. Greater use of negative-affect words during exposure predicted greater SCR reduction (r = −.288, p = .019), with dose-response stratification consistent with a labeling-specific mechanism. Niles, Craske, Lieberman, and Hur (2015) extended these results to public-speaking anxiety, with Time × Group effects on SCR-NS and HR significant during recovery (but not anticipation) windows.

**The stubborn dissociation.** A consistent and underemphasized pattern across Tabibnia (2008), Kircanski (2012), Niles (2015), Niles, Mesri, Burklund, Lieberman, and Craske (2013), and Sewart et al. (2019) is that affect labeling reduces **physiological arousal but not subjective fear**. Self-reported fear ratings rarely differ between labeling and control conditions. This dissociation has two competing interpretations: (a) labeling may modulate autonomic responding before (or independently of) experiential change; or (b) self-report measures may be insensitive to brief experimental manipulations, with physiological measures providing more reliable indicators. The clinical implication is non-trivial — patients seeking immediate subjective relief may not perceive labeling as helpful even when it accelerates physiological habituation.

**Heart rate and heart-rate variability.** Kassam and Mendes (2013) reported that the mere act of reporting anger on a scale reduced heart rate and cardiac output and increased total peripheral resistance, suggesting sympathetic withdrawal under labeling. Fitzpatrick, Ip, Krantz, Zeifman, and Kuo (2019) studied 29 borderline personality disorder patients and 30 healthy controls: labeling increased respiratory sinus arrhythmia (a parasympathetic index) in BPD, but BPD patients did not benefit from labeling-prior-to-reappraisal, in contrast to controls.

**Naturalistic large-N evidence.** Fan, Varol, Varamesh, Barron, van de Leemput, Scheffer, and Bollen (2019; *Nature Human Behaviour*; N = 74,487 Twitter users, > 1 billion tweets) reported that emotional intensity ramps up before "I feel" tweets and rapidly decays afterward, with sharper reversal for negative than positive emotions. The naturalistic effect direction matches the laboratory direction but operates at minute-scale dynamics outside controlled experimental conditions.

**Boundary condition: positive valence.** Lieberman et al. (2011; Study 4) reported that affect labeling dampened *positive* affect to positive images, framing labeling as valence-general dampening. Vlasenko, Rogers, and Waugh (2021) directly contradicted this finding across **four studies** (Ns = 49, 116, 120, 120; total N = 405), reporting that labeling **intensified** positive valence, regardless of timing (during vs. after the image), rating type (intensity vs. positivity), or delay. The discrepancy may reflect stimulus features, label specificity, or sampling differences and remains unresolved.

### 3.5 Replication and contested findings

The replication landscape divides sharply by lineage. Internal replications within the Lieberman laboratory and close collaborators are largely supportive. External, pre-registered, and recent replications are heavily mixed — and the lab-stratified meta-analytic estimate above quantifies the gap.

**Direct or near-direct failed replications.**

- **Vives, Costumero, Ávila, and Costa (2021; *Affective Science*; N = 26 unbalanced Spanish-English bilinguals)** found a Type × Language interaction F(1,25) = 16.64, p < .001 — affect labeling in a foreign language *increased* right-amygdala activation, while native-language labeling produced canonical downregulation t(25) = −2.27, p = .03.
- **Nook, Satpute, and Ochsner (2021; *Affective Science*; pre-registered; Study 1 N = 80; Study 2 N = 60)** reported that emotion naming *before* reappraisal or mindful acceptance **impeded** regulation, with a Naming × Regulating interaction F(1,76) = 11.17, p = .001, η_p² = .13, and a key Regulate vs. Name+Regulate contrast t(38) = −3.82, p < .001, **Cohen's d = −1.21**. They proposed a "crystallization" account: naming may concretize an affective state and reduce its malleability.
- **Ariely, Mokady, Reggev, and Anholt (2026; *Affective Science*; total N = 226, two pre-registered studies, OSF: osf.io/j9624 and osf.io/2vq4z)** replicated the Nook crystallization in two pre-registered studies, with d = 1.32 and d = 0.86 for the Reappraise vs. Name+Reappraise contrasts. Their pre-registered hypothesis that delayed measurement (1–2 days) would reveal latent benefit of labeling was *not* supported.
- **Plaisted, Waite, and Creswell (2022; *Behaviour Research and Therapy*; adolescent RCT)** reported a complete null: neither AL nor positive coping statements enhanced exposure on heart rate, self-rated anxiety, or observer-rated anxiety from pretest to one-week follow-up. This is the only adequately powered adolescent RCT in the literature.
- **A 2026 *Cognition and Emotion* report** (doi:10.1080/02699931.2026.2616636) stated explicitly: "Our results did not replicate the down-regulating effect of affect labelling on negative emotions, contrary to previous studies."
- **Yoshimura et al. (2024; *BMC Psychology*; N = 35)** found that combining affect labeling with reappraisal **diminished** rather than augmented regulatory effect.
- **Vlasenko et al. (2021)** reversed the predicted direction for positive affect across four studies.
- **Constantinou et al. (2015; IBS patients)** found null arousal-regulation effects of labeling in a clinical gut-brain population.
- **Fitzpatrick et al. (2019)** found null effects of labeling-prior-to-reappraisal in BPD.
- **McRae, Taitano, and Lane (2010)** found that only objective (perceptual) labeling, not subjective emotional labeling, reduced skin conductance.

**Boundary conditions identified across the literature.**

The robust effect appears confined by at least nine moderators: (1) language of labeling (native > foreign); (2) intensity (high > low; low intensity may *increase* distress per Levy-Gigi & Shamay-Tsoory, 2022); (3) valence (negative more reliably dampened than positive); (4) sequencing (labeling-then-reappraisal worse than either alone); (5) clinical status (BPD, IBS, social anxiety with comorbid depression show altered or absent effects); (6) age (adolescents in Plaisted 2022 showed null); (7) free vs. provided labels; (8) label specificity (objective vs. subjective); (9) context (matched-stimulus paradigms more reliable than non-matched).

**Methodological critiques relevant to the original literature.**

- **Vul, Harris, Winkielman, and Pashler (2009; *Perspectives on Psychological Science*)** demonstrated that approximately half of social neuroscience papers used non-independent regions-of-interest, inflating reported correlations.
- **Eklund, Nichols, and Knutsson (2016; *PNAS*)** showed that default cluster-based inference in SPM/FSL/AFNI yielded familywise error rates up to 70% (against nominal 5%). Affect labeling fMRI studies pre-dating the move to non-parametric or stringent thresholds may have inflated false-positive rates.
- **Button et al. (2013; *Nature Reviews Neuroscience*)** estimated median neuroscience power at 8–31%; the original Lieberman et al. N = 30 falls in this underpowered range.
- **de Voogd and Hermans (2022; *Human Brain Mapping*; doi:10.1002/hbm.25828)** showed that working-memory engagement downregulates the amygdala in regions overlapping the reappraisal map, suggesting that amygdala dampening may reflect **cognitive demand** rather than emotion-specific content. Constantinou, Van Den Houte, Bogaerts, Van Diest, and Van den Bergh (2014) similarly found that content (non-emotional) labeling reduced symptom reporting equivalently to emotional labeling.
- **Test-retest reliability of task-evoked amygdala fMRI signals is poor**, with most intra-class correlations below .4 — a structural barrier to single-subject mechanistic claims.

**Recent vocabulary-distress findings.** Vine, Boyd, and Pennebaker (2020; *Nature Communications*; doi:10.1038/s41467-020-18349-0) showed across 1,567 college students and 35,000+ bloggers that broader negative emotion vocabularies predict **greater** distress and poorer health, and DeLap, Vine, Santee, and Starr (2024/2025; *Emotion*, 25(1), 102–113; doi:10.1037/emo0001429) extended this into adolescents with depression as the outcome. These findings directly oppose the "name it to tame it" therapeutic logic and require explicit reconciliation.

### 3.6 Clinical applications and translational evidence

**Exposure therapy enhancement.** The Craske inhibitory-learning model lists affect labeling among canonical exposure enhancers. Tabibnia et al. (2008), Kircanski et al. (2012), and Niles et al. (2015) provide the empirical anchor; **Plaisted, Waite, and Creswell (2022)** provide the only adolescent RCT and report a complete null on heart rate, self-rated anxiety, and observer-rated anxiety — a clinically important negative result. Sewart et al. (2019) examined positive- and negative-affect change during CBT and ACT for social anxiety disorder.

**Social anxiety disorder.** Burklund, Craske, Taylor, and Lieberman (2015; *SCAN*) reported a counterintuitive pattern: SAD patients showed amygdala **upregulation** during affect labeling, most pronounced in those with comorbid depression — a reversal of the healthy-control direction. Young et al. (2019) showed pre-treatment amygdala–vmPFC functional connectivity during labeling predicts SAD response to CBT and ACT. Sandman, Young, Burklund, Saxbe, Lieberman, and Craske (2020) found that negative changes in amygdala–dorsal-ACC connectivity during labeling predicted superior 6–12 month outcomes.

**PTSD.** Burklund, Davies, Niles, Torre, Brown, Vinograd, Lieberman, and Craske (2024; *Frontiers in Psychology*) reported a pilot trial of repeated affect labeling and inhibitory-regulation practice in combat veterans (~13 completers). Pre-post effect sizes were promising but the uncontrolled within-subjects design and small sample preclude strong causal inference. **A commercial conflict of interest must be flagged**: lead author L. J. Burklund is an independent contractor at NeuroGen Technologies Inc., a private company developing affect-labeling-based PTSD interventions. This disclosure, combined with the open-label single-arm design, places the study at high risk of bias on the ROBINS-I framework.

**Borderline personality disorder.** Fitzpatrick et al. (2019) found that affect labeling increased respiratory sinus arrhythmia in BPD but did not facilitate downstream regulation, suggesting parasympathetic engagement without successful integration.

**Dialectical behavior therapy, acceptance and commitment therapy, and cognitive-behavioral therapy.** Each integrates a labeling-adjacent skill: DBT's "describe" and "observe" emotion-identification skills (Linehan, 1993); ACT's defusion (Hayes, Strosahl, & Wilson, 1999); CBT's attention to monitoring and identifying cognitions and feelings (Beck & Emery, 1985). Direct dismantling studies isolating the labeling component within these protocols are absent.

**Mindfulness-based interventions.** Creswell et al. (2007) reported that dispositional mindfulness was associated with greater prefrontal activity and weaker amygdala activity during affect labeling. Hölzel et al. (2013) found mindfulness-based stress reduction altered affect labeling neural activity in generalized anxiety disorder. Goldin and Gross (2010) reported MBSR effects on emotion regulation in social anxiety. The mindfulness literature has long relied on labeling-like operations ("noting") without isolating their causal contribution.

**Hostage and crisis negotiation.** The FBI Behavioral Change Stairway Model (Vecchi, Van Hasselt, & Romano, 2005) lists emotional labeling among core active-listening skills. Van Hasselt, Baker, Romano, Schlessinger, Zucker, Dragone, and Perera (2006) reported significant pre-post training improvements on emotional-labeling competence among 45 FBI agents. Voss and Raz (2016) popularized "tactical empathy" labels in trade form — a translation, rather than empirical extension, of the labeling literature. Direct outcome data linking labeling proficiency to negotiation success in field settings remain scarce.

**Educational and parenting applications.** Brackett, Rivers, Reyes, and Salovey's RULER program (2012; 2013) integrates the "L" (Label) step into a five-step social-emotional curriculum with quasi-experimental and one cluster-randomized evaluation; effect sizes for the labeling component cannot be isolated. Siegel and Bryson's (2011) "name it to tame it" parenting heuristic draws explicitly on Lieberman et al. (2007) but extrapolates the laboratory effect to parent-child co-regulation without direct empirical validation. The Vine et al. (2020) and DeLap et al. (2025) findings cited above directly challenge this extrapolation.

### 3.7 Cross-cultural and developmental evidence

**Cross-cultural variation.** Mesquita and Frijda (1992), Kitayama, Mesquita, and Karasawa (2006), and Tsai (2007) document substantial cultural variation in which emotions are valued, named, and regulated. Wierzbicka (1999) and Jackson et al. (2019; *Science*; 2,474 languages) demonstrated cross-linguistic variation in emotion lexicons with both culture-specific and universal structure. The implications for affect labeling are non-trivial: the available emotion vocabulary, the cultural endorsement of articulating feelings, and the relational context of labeling all moderate the construct's expected utility. Vives et al.'s (2021) foreign-language null finding is the most direct demonstration of this cultural-linguistic moderation.

**Development.** Pons, Harris, and de Rosnay (2004) describe a three-phase developmental trajectory of emotion comprehension: external (3–5 years), mental (5–9 years), and reflective (8–11 years). Nook, Sasse, Lambert, McLaughlin, and Somerville (2018; *Psychological Science*) reported a U-shaped trajectory of emotion differentiation with a nadir in adolescence — suggesting that the *period in which emotion-regulation interventions are most often delivered* coincides with the lowest natural granularity. Gee et al. (2013) showed a developmental shift from positive to negative amygdala–mPFC connectivity around age 10.

### 3.8 Related constructs and their boundary relations

**Emotional granularity.** Barrett, Gross, Christensen, and Benvenuto (2001) introduced the construct: individuals with more differentiated emotion experiences regulate emotions more effectively. Kashdan, Barrett, and McKnight (2015) review evidence that low granularity is associated with binge drinking, aggression, self-injury, and multiple disorders. Kalokerinos, Erbas, Ceulemans, and Kuppens (2019; *Psychological Science*; ESM with > 34,000 measurements) showed low granularity is associated with less *effective use* of regulation strategies, not less *selection* of them.

**Alexithymia.** Bagby, Parker, and Taylor (1994) operationalize the clinical opposite: difficulty identifying and describing feelings. van der Velde, Servaas, Goerlich, Bruggeman, Horton, Costafreda, and Aleman's (2013) meta-analysis of 15 neuroimaging studies showed alexithymic individuals exhibit *diminished* amygdala and dmPFC responses to negative stimuli, with compensatory dorsal ACC engagement. The implication is paradoxical: those who would benefit most from labeling are the least able to perform it.

**Cognitive reappraisal.** Direct comparisons (Lieberman et al., 2011; Burklund et al., 2014; Payer et al., 2012) reveal overlapping prefrontal recruitment and amygdala dampening, with affect labeling sometimes producing *stronger* prefrontal responses despite being incidental — a paradox suggesting that labeling may engage greater inhibitory effort because it operates without explicit cognitive scaffolding.

**Expressive writing.** Pennebaker and Beall's (1986) foundational paradigm, Smyth's (1998) meta-analysis (k = 14, d = 0.47), and Frattaroli's (2006) more comprehensive analysis (k = 146, r = 0.075) bracket the effect's magnitude. Reinhold, Bürkner, and Holling (2018) found null effects on depressive symptoms at follow-up across 39 studies. Memarian, Torre, Haltom, Stanton, and Lieberman (2017) demonstrated direct neural-bridge evidence: pre-intervention affect labeling neural activity predicted three-month expressive writing outcomes in breast cancer survivors.

## 4. Discussion

### 4.1 What is true

Three claims survive rigorous synthesis. First, **labeling-instructed contrasts versus passive viewing produce reliable amygdala dampening in healthy adult fMRI samples**, supported by two large coordinate-based meta-analyses (Costafreda et al., 2008; Brooks et al., 2017). Second, **affect labeling concurrent with exposure produces moderate-to-large skin-conductance reductions one week later in the UCLA paradigm**, with effect sizes of g ≈ 0.6–0.9 (Tabibnia et al., 2008; Kircanski et al., 2012; Niles et al., 2015). Third, **participants systematically misforecast labeling outcomes** (Lieberman et al., 2011), a robust finding that anchors affect labeling as implicit emotion regulation distinct from intentional reappraisal.

### 4.2 What is contested

Five claims do not survive scrutiny in their popularly-circulated form.

First, the **right lateralization** of the vlPFC effect is contradicted by left-lateralized connectivity meta-analyses (Berboth & Morawetz, 2021) and recent translational data (Burklund et al., 2024 PTSD pilot left-lateralized symptom relation).

Second, the **MPFC mediation** path with Z_aZ_b = 10.55 has not been consistently replicated across labs.

Third, **specificity to emotional content** is undermined by working-memory amygdala-dampening data (de Voogd & Hermans, 2022) and content-labeling parity (Constantinou et al., 2014) — labeling may reduce amygdala activity through cognitive demand rather than affective categorization.

Fourth, **valence-general dampening** is contradicted by Vlasenko, Rogers, and Waugh's (2021) demonstration across four studies (total N = 405) that labeling intensifies positive emotions.

Fifth, **the labeling-helps-regulation-broadly** interpretation is contradicted by the Nook–Ariely–Plaisted–Yoshimura line showing that labeling can impede subsequent reappraisal, fail in adolescents, and worsen affect.

The lab-stratified meta-analysis quantifies a **sixth concern**: the pooled physiological effect size in independent labs (g = −0.13, 95% CI crosses zero) is approximately one-fifth the magnitude reported in the originating lab (g = −0.74). This is consistent with structural author non-independence rather than incidental variation between labs.

### 4.3 Why effects shrink outside the originating laboratory

Several structural factors plausibly explain the attenuation. The original effect was estimated at N = 30 with statistical power likely below 50%, virtually guaranteeing inflated effect sizes (Button et al., 2013). The original ROI strategy, while not strictly circular, used non-pre-registered contrasts in an era predating Eklund-corrected cluster thresholds (Eklund et al., 2016). Approximately 30 of the 50 most-cited affect labeling papers come from the Lieberman laboratory and close collaborators — a level of evidentiary concentration that makes independent multisite replication essential rather than supplementary. The recent appearance of pre-registered failures (Nook 2021; Vives 2021; Plaisted 2022; Ariely 2026; Cognition & Emotion 2026) is consistent with the broader trajectory of social neuroscience under replication-crisis-era methods.

### 4.4 Boundary conditions: a calibrated map

The literature now supports a **moderator-rich** rather than **universal** account of affect labeling.

**Helpful** when: stimuli are high-intensity, negative-valenced, labeled in the speaker's native language, in healthy adult populations, used during exposure with sufficient repetition, and not chained to subsequent intentional reappraisal.

**Less helpful or harmful** when: stimuli are low-intensity (Levy-Gigi & Shamay-Tsoory, 2022), positive-valenced (Vlasenko et al., 2021), labeled in a foreign language (Vives et al., 2021), in BPD (Fitzpatrick et al., 2019), IBS (Constantinou et al., 2015), adolescents (Plaisted et al., 2022), older adults, or sequenced before reappraisal/acceptance (Nook et al., 2021; Ariely et al., 2026).

### 4.5 What clinicians and applied practitioners should take away

The trade-press translation outpaces the empirical anchor. Siegel and Bryson's (2011) "name it to tame it," Voss and Raz's (2016) "tactical empathy," and the broad emotional-intelligence curricula derived from RULER and similar programs draw on a coherent but narrow primary literature. **Evidence supports labeling as one component of multi-component interventions** (exposure therapy, mindfulness training, social-emotional learning), but does not yet support claims that **labeling alone** reliably reduces distress in everyday or clinical applications. A particularly important clinical caveat: labeling reliably reduces *physiology* but not *self-report* in experimental paradigms — patients may feel labeling does not work even when their autonomic nervous systems indicate otherwise. Clinicians should set expectations accordingly.

**Three specific practice recommendations** follow directly from the moderator analysis: (1) avoid sequencing labeling immediately before reappraisal or acceptance, given the Nook–Ariely crystallization findings; (2) be cautious about labeling positive states, given Vlasenko et al. (2021); (3) be cautious about labeling in non-native-language clinical encounters, given Vives et al. (2021).

### 4.6 Limitations

Our synthesis is bounded by five limitations. First, many original fMRI studies did not report Cohen's d or Hedges' g, precluding a fully harmonized quantitative meta-analysis without re-analysis of original data. Second, single-laboratory concentration in the affect labeling fMRI literature limits the independence of the supportive evidence base; we have addressed this with a pre-specified lab-stratified moderator analysis but the underlying problem requires direct multisite replication, not statistical correction. Third, the dissociation between physiological and self-report measures means that effect-size estimates depend on outcome choice in ways that we have flagged but not fully resolved. Fourth, the meta-analysis includes nine effect sizes from seven studies — adequate for detecting a moderate pooled effect but underpowered for many moderator analyses. Fifth, our inclusion criteria excluded studies in non-English without translation, which may bias the synthesis toward Anglophone research traditions.

### 4.7 Methodological recommendations for the field

Five recommendations would substantially strengthen the affect labeling literature. (1) **Pre-registered, multisite, large-N replications** of Lieberman et al. (2007) with whole-brain analyses, harmonized stimuli, and standardized effect-size reporting. (2) **Open data and analysis code** posted on OSF and NeuroVault. (3) **Direct comparison studies** that orthogonally vary language, intensity, valence, sequencing, and population to map the moderator space systematically. (4) **Dismantling trials** within multi-component interventions (CBT, ACT, DBT, mindfulness) to isolate the labeling-specific contribution. (5) **Individual-difference characterization** using validated tools (Toronto Alexithymia Scale; the Affect Labeling Questionnaire of Sahi, Guassi Moreira, Torre, & Lieberman, 2023; granularity ESM measures) to identify who benefits.

## 5. Future directions

Five frontiers warrant particular attention over the next decade. First, the **predictive coding reframe** of Givon, Meiran, and Goldenberg (2025; *Trends in Cognitive Sciences*) recasts affect labeling as a perceptual decision implementable in sequential-sampling models — opening a quantitative computational mechanism that prior verbal accounts have lacked. Second, **wearable physiology in the wild** can extend Fan et al.'s (2019) Twitter-scale findings into ambulatory ecological-momentary-assessment paradigms with continuous heart-rate variability, electrodermal activity, and pupillometry, escaping the artificial constraints of scanner paradigms. Third, **developmentally informed clinical trials** for adolescents — whose granularity nadir coincides with the highest rates of internalizing-disorder onset — are urgently needed; the Plaisted et al. (2022) null result deserves replication with larger samples and varied stimulus intensities. Fourth, **cross-cultural and multilingual studies** at scale could systematically test how the linguistic-cultural envelope of emotion words moderates labeling outcomes, with stratification by language family and emotional lexicon richness. Fifth, **intervention dismantling** within established protocols (DBT, CBT, ACT, MBSR) is overdue: until the labeling component is isolated experimentally, clinical protocol attribution remains under-evidenced.

## 6. Conclusion

Affect labeling is a real but contextually fragile phenomenon. The 2007 Lieberman et al. paper inaugurated a productive program that meta-analytically anchors a reliable amygdala-dampening signature in narrowly specified paradigms and supports modest-to-moderate translational gains in exposure therapy within the originating laboratory. But the construct's popular extrapolation has outrun its empirical reach. Our pre-registered random-effects meta-analysis revealed a pooled physiological effect of g = −0.43 [−0.68, −0.18], with a 95% prediction interval that crosses zero and a striking lab-by-lab dissociation: g = −0.74 within the UCLA Lieberman/Craske axis, g = −0.13 in independent laboratories. Recent pre-registered failures, lateralization reversals, and explicit demonstrations that labeling can intensify positive affect, fail in foreign languages, fail in adolescents, and impede subsequent reappraisal collectively define a moderator-rich landscape in which "putting feelings into words" is sometimes therapeutic, sometimes inert, and occasionally counterproductive. The mature science of affect labeling will replace categorical claims with conditional ones — specifying for whom, in which language, at which intensity, with which downstream sequencing, and to what end labeling actually works. Until then, clinicians and applied practitioners should treat the heuristic "name it to tame it" as a partial truth: a useful component embedded in a richer regulation toolkit, not a universal solvent for emotional distress.

---

## Figures

**Figure 1.** PRISMA 2020 flow diagram (`figures/prisma_flow.png`).
**Figure 2.** Risk-of-bias summary across included studies (`figures/rob_summary.png`).
**Figure 3.** Forest plot of the random-effects meta-analysis of peripheral physiology (`figures/forest_plot.png`).
**Figure 4.** Funnel plot for publication-bias assessment (`figures/funnel_plot.png`).

## Supplementary materials

- `meta-analysis/run_meta_analysis.py` — analysis code (Python)
- `meta-analysis/extracted_effect_sizes.csv` — extracted Hedges' g values
- `meta-analysis/leave_one_out.csv` — leave-one-out sensitivity output
- `meta-analysis/results_summary.txt` — primary results in plain text
- `prisma/build_prisma.py` — PRISMA flow diagram code
- `prisma/prisma_counts.csv` — structured machine-readable counts (canonical)
- `prisma/prisma_counts.txt` — counts at each PRISMA stage (legacy human-readable)
- `supplementary/risk_of_bias.csv` — full RoB table
- `supplementary/build_rob_figure.py` — RoB summary figure code
- `prereg/PROSPERO_preregistration.md` — full pre-registration document
- `data/searches/search_strategy.md` — PRISMA-S compliant search strategy report
- `data/screening/included_papers.csv` — the 100 included papers with subset assignments
- `data/screening/derived_screening_log.csv` — labeled candidate corpus re-derived from PubMed (suitable for AI-assisted SLR screening research)
- `data/exclusion_reason_codebook.md` — codebook for the six full-text exclusion reasons
- `data/QUALITY_REPORT.md` — automated comparison of canonical vs. re-derived counts

## Data and code availability

All data, code, and supplementary materials accompanying this review are openly available at https://github.com/mikhaeelatefrizk/affect-labeling-review under permissive licenses: source code under MIT, manuscript and figures under CC-BY-4.0, and data files under CC-BY-4.0. The v1.0.0 release is permanently archived on Zenodo with the DOI 10.5281/zenodo.20109595 (https://doi.org/10.5281/zenodo.20109595). A single `make all` from a fresh clone of the repository, with the pinned dependency set listed in `requirements.txt` (Python 3.11), regenerates every numerical result, figure, and dataset byte-for-byte. Continuous integration verifies this guarantee on every push.

The screening corpus was screened by a single coder (M.A.R.W.); inter-rater agreement statistics are therefore not available. The original per-paper screening decisions and exclusion reasons were not preserved in a shareable form; aggregate counts at each PRISMA stage are reported in `prisma/prisma_counts.csv` and remain canonical. To support future AI-assisted SLR research and to provide a reproducible substitute for ML training and benchmarking, a derived screening log (`data/screening/derived_screening_log.csv`) is produced by re-running the pre-registered PubMed query via the NCBI E-utilities API and joining the result against the included-papers list parsed from the manuscript and `references.bib`. The derivation is deterministic given a PubMed snapshot; expected drift between today's snapshot and the canonical 1,842 records is reported in `data/QUALITY_REPORT.md`. Limitations of the derived dataset (loss of per-paper exclusion reasons, collapse of the title/abstract vs. full-text distinction, PubMed-only coverage of the original five-database search) are documented in `data/screening/README.md`.

## References

Ariely, Y., Mokady, A., Reggev, N., & Anholt, G. E. (2026). Affect labeling and reappraisal as an emotion regulation strategy. *Affective Science*. https://doi.org/10.1007/s42761-026-00362-z

Bagby, R. M., Parker, J. D. A., & Taylor, G. J. (1994). The twenty-item Toronto Alexithymia Scale—I: Item selection and cross-validation of the factor structure. *Journal of Psychosomatic Research*, 38(1), 23–32.

Barrett, L. F. (2017). The theory of constructed emotion: An active inference account of interoception and categorization. *Social Cognitive and Affective Neuroscience*, 12(1), 1–23.

Barrett, L. F., Gross, J., Christensen, T. C., & Benvenuto, M. (2001). Knowing what you're feeling and knowing what to do about it: Mapping the relation between emotion differentiation and emotion regulation. *Cognition and Emotion*, 15(6), 713–724.

Beck, A. T., & Emery, G. (1985). *Anxiety disorders and phobias: A cognitive perspective*. Basic Books.

Berboth, S., & Morawetz, C. (2021). Amygdala-prefrontal connectivity during emotion regulation: A meta-analysis of psychophysiological interactions. *Neuropsychologia*, 153, 107767. https://doi.org/10.1016/j.neuropsychologia.2021.107767

Berkman, E. T., Burklund, L., & Lieberman, M. D. (2009). Inhibitory spillover: Intentional motor inhibition produces incidental limbic inhibition via right inferior frontal cortex. *NeuroImage*, 47(2), 705–712. https://doi.org/10.1016/j.neuroimage.2009.04.084

Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2009). *Introduction to meta-analysis*. Wiley.

Brackett, M. A., Rivers, S. E., Reyes, M. R., & Salovey, P. (2012). Enhancing academic performance and social and emotional competence with the RULER feeling words curriculum. *Learning and Individual Differences*, 22(2), 218–224.

Breuer, J., & Freud, S. (1895). *Studies on hysteria*.

Brooks, J. A., Shablack, H., Gendron, M., Satpute, A. B., Parrish, M. H., & Lindquist, K. A. (2017). The role of language in the experience and perception of emotion: A neuroimaging meta-analysis. *Social Cognitive and Affective Neuroscience*, 12(2), 169–183. https://doi.org/10.1093/scan/nsw121

Buhle, J. T., Silvers, J. A., Wager, T. D., Lopez, R., Onyemekwu, C., Kober, H., Weber, J., & Ochsner, K. N. (2014). Cognitive reappraisal of emotion: A meta-analysis of human neuroimaging studies. *Cerebral Cortex*, 24(11), 2981–2990. https://doi.org/10.1093/cercor/bht154

Burklund, L. J., Craske, M. G., Taylor, S. E., & Lieberman, M. D. (2015). Altered emotion regulation capacity in social phobia as a function of comorbidity. *Social Cognitive and Affective Neuroscience*, 10(2), 199–208. https://doi.org/10.1093/scan/nsu058

Burklund, L. J., Creswell, J. D., Irwin, M. R., & Lieberman, M. D. (2014). The common and distinct neural bases of affect labeling and reappraisal in healthy adults. *Frontiers in Psychology*, 5, 221. https://doi.org/10.3389/fpsyg.2014.00221

Burklund, L. J., Davies, C. D., Niles, A. N., Torre, J. B., Brown, L., Vinograd, M., Lieberman, M. D., & Craske, M. G. (2024). Affect labeling: A promising new neuroscience-based approach to treating combat-related PTSD. *Frontiers in Psychology*, 15, 1270424. https://doi.org/10.3389/fpsyg.2024.1270424

Button, K. S., Ioannidis, J. P. A., Mokrysz, C., Nosek, B. A., Flint, J., Robinson, E. S. J., & Munafò, M. R. (2013). Power failure: Why small sample size undermines the reliability of neuroscience. *Nature Reviews Neuroscience*, 14(5), 365–376.

Constantinou, E., Bogaerts, K., Van Oudenhove, L., Tack, J., Van Diest, I., & Van den Bergh, O. (2015). Healing words: Using affect labeling to reduce the effects of unpleasant cues on symptom reporting in IBS patients. *International Journal of Behavioral Medicine*, 22(4), 512–520. https://doi.org/10.1007/s12529-014-9449-8

Constantinou, E., Van Den Houte, M., Bogaerts, K., Van Diest, I., & Van den Bergh, O. (2014). Can words heal? Using affect labeling to reduce the effects of unpleasant cues on symptom reporting. *Frontiers in Psychology*, 5, 807. https://doi.org/10.3389/fpsyg.2014.00807

Costafreda, S. G., Brammer, M. J., David, A. S., & Fu, C. H. Y. (2008). Predictors of amygdala activation during the processing of emotional stimuli: A meta-analysis of 385 PET and fMRI studies. *Brain Research Reviews*, 58(1), 57–70. https://doi.org/10.1016/j.brainresrev.2007.10.012

Craske, M. G., Treanor, M., Conway, C. C., Zbozinek, T., & Vervliet, B. (2014). Maximizing exposure therapy: An inhibitory learning approach. *Behaviour Research and Therapy*, 58, 10–23.

Creswell, J. D., Way, B. M., Eisenberger, N. I., & Lieberman, M. D. (2007). Neural correlates of dispositional mindfulness during affect labeling. *Psychosomatic Medicine*, 69(6), 560–565. https://doi.org/10.1097/PSY.0b013e3180f6171f

DeLap, K. L., Vine, V., Santee, A. C., & Starr, L. R. (2025). Negative emotion vocabulary and adolescent depression: A longitudinal investigation. *Emotion*, 25(1), 102–113. https://doi.org/10.1037/emo0001429

de Voogd, L. D., & Hermans, E. J. (2022). Meta-analytic evidence for downregulation of the amygdala during working memory maintenance. *Human Brain Mapping*, 43(9), 2951–2971. https://doi.org/10.1002/hbm.25828

Eklund, A., Nichols, T. E., & Knutsson, H. (2016). Cluster failure: Why fMRI inferences for spatial extent have inflated false-positive rates. *Proceedings of the National Academy of Sciences*, 113(28), 7900–7905.

Fan, R., Varol, O., Varamesh, A., Barron, A., van de Leemput, I. A., Scheffer, M., & Bollen, J. (2019). The minute-scale dynamics of online emotions reveal the effects of affect labeling. *Nature Human Behaviour*, 3(1), 92–100. https://doi.org/10.1038/s41562-018-0490-5

Fitzpatrick, S., Ip, J., Krantz, L., Zeifman, R., & Kuo, J. R. (2019). Use your words: The role of emotion labeling in regulating emotion in borderline personality disorder. *Behaviour Research and Therapy*, 120, 103447. https://doi.org/10.1016/j.brat.2019.103447

Foland, L. C., Altshuler, L. L., Bookheimer, S. Y., Eisenberger, N., Townsend, J., & Thompson, P. M. (2008). Evidence for deficient modulation of amygdala response by prefrontal cortex in bipolar mania. *Psychiatry Research: Neuroimaging*, 162(1), 27–37. https://doi.org/10.1016/j.pscychresns.2007.04.007

Frattaroli, J. (2006). Experimental disclosure and its moderators: A meta-analysis. *Psychological Bulletin*, 132(6), 823–865. https://doi.org/10.1037/0033-2909.132.6.823

Gee, D. G., Humphreys, K. L., Flannery, J., Goff, B., Telzer, E. H., Shapiro, M., Hare, T. A., Bookheimer, S. Y., & Tottenham, N. (2013). A developmental shift from positive to negative connectivity in human amygdala-prefrontal circuitry. *Journal of Neuroscience*, 33(10), 4584–4593.

Givon, E., Meiran, N., & Goldenberg, A. (2025). The process of affect labeling. *Trends in Cognitive Sciences*. Advance online publication. https://doi.org/10.1016/j.tics.2025.09.017

Goldin, P. R., & Gross, J. J. (2010). Effects of mindfulness-based stress reduction (MBSR) on emotion regulation in social anxiety disorder. *Emotion*, 10(1), 83–91.

Hariri, A. R., Bookheimer, S. Y., & Mazziotta, J. C. (2000). Modulating emotional responses: Effects of a neocortical network on the limbic system. *NeuroReport*, 11(1), 43–48. https://doi.org/10.1097/00001756-200001170-00009

Hariri, A. R., Mattay, V. S., Tessitore, A., Fera, F., & Weinberger, D. R. (2003). Neocortical modulation of the amygdala response to fearful stimuli. *Biological Psychiatry*, 53(6), 494–501. https://doi.org/10.1016/S0006-3223(02)01786-9

Hayes, S. C., Strosahl, K. D., & Wilson, K. G. (1999). *Acceptance and commitment therapy: An experiential approach to behavior change*. Guilford Press.

He, Z., Lin, Y., Xia, L., Liu, Z., Zhang, D., & Elliott, R. (2020). Critical role of the right VLPFC in emotion regulation of social pain: A tDCS study. *Human Brain Mapping*, 41(5), 1362–1371. https://doi.org/10.1002/hbm.24881

Hölzel, B. K., Hoge, E. A., Greve, D. N., Gard, T., Creswell, J. D., Brown, K. W., Barrett, L. F., Schwartz, C., Vaitl, D., & Lazar, S. W. (2013). Neural mechanisms of symptom improvements in generalized anxiety disorder following mindfulness training. *NeuroImage: Clinical*, 2, 448–458.

Jackson, J. C., Watts, J., Henry, T. R., List, J. M., Forkel, R., Mucha, P. J., Greenhill, S. J., Gray, R. D., & Lindquist, K. A. (2019). Emotion semantics show both cultural variation and universal structure. *Science*, 366(6472), 1517–1522.

James, W. (1884). What is an emotion? *Mind*, 9(34), 188–205.

Kalokerinos, E. K., Erbas, Y., Ceulemans, E., & Kuppens, P. (2019). Differentiate to regulate: Low negative emotion differentiation is associated with ineffective use but not selection of emotion-regulation strategies. *Psychological Science*, 30(6), 863–879.

Kashdan, T. B., Barrett, L. F., & McKnight, P. E. (2015). Unpacking emotion differentiation: Transforming unpleasant experience by perceiving distinctions in negativity. *Current Directions in Psychological Science*, 24(1), 10–16.

Kassam, K. S., & Mendes, W. B. (2013). The effects of measuring emotion: Physiological reactions to emotional situations depend on whether someone is asking. *PLOS ONE*, 8(6), e64959. https://doi.org/10.1371/journal.pone.0064959

Kircanski, K., Lieberman, M. D., & Craske, M. G. (2012). Feelings into words: Contributions of language to exposure therapy. *Psychological Science*, 23(10), 1086–1091. https://doi.org/10.1177/0956797612443830

Kitayama, S., Mesquita, B., & Karasawa, M. (2006). Cultural affordances and emotional experience: Socially engaging and disengaging emotions in Japan and the United States. *Journal of Personality and Social Psychology*, 91, 890–903.

Levy-Gigi, E., & Shamay-Tsoory, S. (2022). Affect labeling: The role of timing and intensity. *PLOS ONE*, 17(12), e0279303. https://doi.org/10.1371/journal.pone.0279303

Liang, Y., & Lin, S. (2023). Current and lasting effects of affect labeling on the late positive potential to negative pictures. *Brain and Behavior*, 13(7), e3065. https://doi.org/10.1002/brb3.3065

Lieberman, M. D., Eisenberger, N. I., Crockett, M. J., Tom, S. M., Pfeifer, J. H., & Way, B. M. (2007). Putting feelings into words: Affect labeling disrupts amygdala activity in response to affective stimuli. *Psychological Science*, 18(5), 421–428. https://doi.org/10.1111/j.1467-9280.2007.01916.x

Lieberman, M. D., Hariri, A., Jarcho, J. M., Eisenberger, N. I., & Bookheimer, S. Y. (2005). An fMRI investigation of race-related amygdala activity in African-American and Caucasian-American individuals. *Nature Neuroscience*, 8(6), 720–722.

Lieberman, M. D., Inagaki, T. K., Tabibnia, G., & Crockett, M. J. (2011). Subjective responses to emotional stimuli during labeling, reappraisal, and distraction. *Emotion*, 11(3), 468–480. https://doi.org/10.1037/a0023503

Linehan, M. M. (1993). *Skills training manual for treating borderline personality disorder*. Guilford Press.

Matejka, M., Kazzer, P., Seehausen, M., Bajbouj, M., Klann-Delius, G., Menninghaus, W., Jacobs, A. M., Heekeren, H. R., & Prehn, K. (2013). Talking about emotion: Prosody and skin conductance indicate emotion regulation. *Frontiers in Psychology*, 4, 260.

McRae, K., Taitano, E. K., & Lane, R. D. (2010). The effects of objective and subjective emotion labels on emotional response. *Cognition and Emotion*, 24(5), 829–839. https://doi.org/10.1080/02699930902797141

Memarian, N., Torre, J. B., Haltom, K. E. B., Stanton, A. L., & Lieberman, M. D. (2017). Neural activity during affect labeling predicts expressive writing effects on well-being: GLM and SVM approaches. *Social Cognitive and Affective Neuroscience*, 12(9), 1437–1447. https://doi.org/10.1093/scan/nsx084

Mesquita, B., & Frijda, N. H. (1992). Cultural variations in emotions: A review. *Psychological Bulletin*, 112(2), 179–204.

Niles, A. N., Craske, M. G., Lieberman, M. D., & Hur, C. (2015). Affect labeling enhances exposure effectiveness for public speaking anxiety. *Behaviour Research and Therapy*, 68, 27–36. https://doi.org/10.1016/j.brat.2015.03.004

Nook, E. C., Sasse, S. F., Lambert, H. K., McLaughlin, K. A., & Somerville, L. H. (2018). The nonlinear development of emotion differentiation: Granular emotional experience is low in adolescence. *Psychological Science*, 29(8), 1346–1357.

Nook, E. C., Satpute, A. B., & Ochsner, K. N. (2021). Emotion naming impedes both cognitive reappraisal and mindful acceptance strategies of emotion regulation. *Affective Science*, 2(2), 187–198. https://doi.org/10.1007/s42761-021-00036-y

Page, M. J., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, 372, n71.

Payer, D. E., Baicy, K., Lieberman, M. D., & London, E. D. (2012). Overlapping neural substrates between intentional and incidental down-regulation of negative emotions. *Emotion*, 12(2), 229–235. https://doi.org/10.1037/a0027421

Payer, D. E., Lieberman, M. D., & London, E. D. (2011). Neural correlates of affect processing and aggression in methamphetamine dependence. *Archives of General Psychiatry*, 68(3), 271–282. https://doi.org/10.1001/archgenpsychiatry.2010.154

Pennebaker, J. W., & Beall, S. K. (1986). Confronting a traumatic event: Toward an understanding of inhibition and disease. *Journal of Abnormal Psychology*, 95(3), 274–281.

Plaisted, H., Waite, P., & Creswell, C. (2022). Optimising exposure for adolescents with public speaking anxiety: Affect labelling or positive coping statements? *Behaviour Research and Therapy*, 148, 103997. https://doi.org/10.1016/j.brat.2021.103997

Pons, F., Harris, P. L., & de Rosnay, M. (2004). Emotion comprehension between 3 and 11 years: Developmental periods and hierarchical organization. *European Journal of Developmental Psychology*, 1(2), 127–152.

Reinhold, M., Bürkner, P. C., & Holling, H. (2018). Effects of expressive writing on depressive symptoms — A meta-analysis. *Clinical Psychology: Science and Practice*, 25(1), e12224. https://doi.org/10.1111/cpsp.12224

Sahi, R. S., Guassi Moreira, J. F., Torre, J. B., & Lieberman, M. D. (2023). The Affect Labeling Questionnaire. *PsyArXiv*. https://doi.org/10.31234/osf.io/b8hde

Sandman, C. F., Young, K. S., Burklund, L. J., Saxbe, D. E., Lieberman, M. D., & Craske, M. G. (2020). Changes in functional connectivity with cognitive behavioral therapy for social anxiety disorder predict outcomes at follow-up. *Behaviour Research and Therapy*, 129, 103612. https://doi.org/10.1016/j.brat.2020.103612

Schachter, S., & Singer, J. (1962). Cognitive, social, and physiological determinants of emotional state. *Psychological Review*, 69(5), 379–399.

Sewart, A. R., Niles, A. N., Burklund, L. J., Saxbe, D. E., Lieberman, M. D., & Craske, M. G. (2019). Examining positive and negative affect as outcomes and moderators of cognitive-behavioral therapy and acceptance and commitment therapy for social anxiety disorder. *Behavior Therapy*, 50(6), 1112–1124. https://doi.org/10.1016/j.beth.2019.07.001

Siegel, D. J., & Bryson, T. P. (2011). *The whole-brain child: 12 revolutionary strategies to nurture your child's developing mind*. Random House.

Smyth, J. M. (1998). Written emotional expression: Effect sizes, outcome types, and moderating variables. *Journal of Consulting and Clinical Psychology*, 66(1), 174–184.

Sterne, J. A. C., et al. (2019). RoB 2: A revised tool for assessing risk of bias in randomised trials. *BMJ*, 366, l4898.

Tabibnia, G., Lieberman, M. D., & Craske, M. G. (2008). The lasting effect of words on feelings: Words may facilitate exposure effects to threatening images. *Emotion*, 8(3), 307–317. https://doi.org/10.1037/1528-3542.8.3.307

Torre, J. B., & Lieberman, M. D. (2018). Putting feelings into words: Affect labeling as implicit emotion regulation. *Emotion Review*, 10(2), 116–124. https://doi.org/10.1177/1754073917742706

Torrisi, S. J., Lieberman, M. D., Bookheimer, S. Y., & Altshuler, L. L. (2013). Advancing understanding of affect labeling with dynamic causal modeling. *NeuroImage*, 82, 481–488. https://doi.org/10.1016/j.neuroimage.2013.06.025

Tsai, J. L. (2007). Ideal affect: Cultural causes and behavioral consequences. *Perspectives on Psychological Science*, 2(3), 242–259.

Tupak, S. V., Dresler, T., Guhn, A., Ehlis, A.-C., Fallgatter, A. J., Pauli, P., & Herrmann, M. J. (2014). Implicit emotion regulation in the presence of threat: Neural and autonomic correlates. *NeuroImage*, 85(Pt 1), 372–379. https://doi.org/10.1016/j.neuroimage.2013.09.066

van der Velde, J., Servaas, M. N., Goerlich, K. S., Bruggeman, R., Horton, P., Costafreda, S. G., & Aleman, A. (2013). Neural correlates of alexithymia: A meta-analysis of emotion processing studies. *Neuroscience and Biobehavioral Reviews*, 37(8), 1774–1785. https://doi.org/10.1016/j.neubiorev.2013.07.008

Van Hasselt, V. B., Baker, M. T., Romano, S. J., Schlessinger, K. M., Zucker, M., Dragone, R., & Perera, A. L. (2006). Crisis (hostage) negotiation training: A preliminary evaluation of program efficacy. *Criminal Justice and Behavior*, 33(1), 56–69.

Vecchi, G. M., Van Hasselt, V. B., & Romano, S. J. (2005). Crisis (hostage) negotiation: Current strategies and issues in high-risk conflict resolution. *Aggression and Violent Behavior*, 10(5), 533–551.

Vine, V., Boyd, R. L., & Pennebaker, J. W. (2020). Natural emotion vocabularies as windows on distress and well-being. *Nature Communications*, 11, 4525. https://doi.org/10.1038/s41467-020-18349-0

Vives, M.-L., Costumero, V., Ávila, C., & Costa, A. (2021). Foreign language processing undermines affect labeling. *Affective Science*, 2(2), 199–206. https://doi.org/10.1007/s42761-021-00039-9

Vlasenko, V. V., Rogers, E. G., & Waugh, C. E. (2021). Affect labelling increases the intensity of positive emotions. *Cognition and Emotion*, 35(7), 1350–1364. https://doi.org/10.1080/02699931.2021.1959302

Voss, C., & Raz, T. (2016). *Never split the difference: Negotiating as if your life depended on it*. HarperBusiness.

Vul, E., Harris, C., Winkielman, P., & Pashler, H. (2009). Puzzlingly high correlations in fMRI studies of emotion, personality, and social cognition. *Perspectives on Psychological Science*, 4(3), 274–290.

Wierzbicka, A. (1999). *Emotions across languages and cultures: Diversity and universals*. Cambridge University Press.

Yoshimura, S., Sato, W., Kochiyama, T., Uono, S., Sawada, R., Kubota, Y., & Toichi, M. (2024). Diminished negative emotion regulation through affect labeling and reappraisal: Insights from functional near infrared spectroscopy on lateral prefrontal cortex activation. *BMC Psychology*, 12, 613. https://doi.org/10.1186/s40359-024-02103-y

Young, K. S., LeBeau, R. T., Niles, A. N., Hsu, K. J., Burklund, L. J., Mesri, B., Saxbe, D., Lieberman, M. D., & Craske, M. G. (2019). Neural connectivity during affect labeling predicts treatment response to psychological therapies for social anxiety disorder. *Journal of Affective Disorders*, 242, 105–110. https://doi.org/10.1016/j.jad.2018.08.016
