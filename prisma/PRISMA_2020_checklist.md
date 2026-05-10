# PRISMA 2020 Checklist

> Page, M. J., McKenzie, J. E., Bossuyt, P. M., et al. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ*, 372, n71. https://doi.org/10.1136/bmj.n71

This checklist documents how each PRISMA 2020 item is reported in the open-research package. "Reported on" columns reference the manuscript and supplementary files in the [`mikhaeelatefrizk/affect-labeling-review`](https://github.com/mikhaeelatefrizk/affect-labeling-review) repository. All file paths are relative to the repository root.

---

## TITLE

| # | Item | Reported on | Notes |
|---|------|-------------|-------|
| 1 | Identify the report as a systematic review. | `manuscript/manuscript.md` line 10; `README.md` H1 | "A systematic review and meta-analysis of affect labeling" appears in the title. |

## ABSTRACT

| # | Item | Reported on | Notes |
|---|------|-------------|-------|
| 2 | Provide a structured abstract that includes (as applicable) background, objectives, data sources, study eligibility criteria, participants and interventions, study appraisal and synthesis methods, results, limitations, conclusions and implications, and registration. | `manuscript/manuscript.md` §"Abstract" | Structured: Background / Methods / Results / Conclusions / Pre-registration / Open data and code. |

## INTRODUCTION

| # | Item | Reported on | Notes |
|---|------|-------------|-------|
| 3 | Describe the rationale for the review in the context of existing knowledge. | `manuscript/manuscript.md` §1 | Six paragraphs trace the construct from Stoic philosophy through Schachter & Singer (1962), Hariri (2000, 2003), Lieberman et al. (2007), and the modern replication crisis literature. |
| 4 | Provide an explicit statement of the objective(s) or question(s) the review addresses. | `manuscript/manuscript.md` §1 final paragraph; `prereg/PROSPERO_preregistration.md` §6 | Four interlocking questions: cumulative evidence, robustness, moderators, clinical calibration. |

## METHODS

| # | Item | Reported on | Notes |
|---|------|-------------|-------|
| 5 | Specify the inclusion and exclusion criteria for the review and how studies were grouped for the syntheses. | `manuscript/manuscript.md` §2.2; `prereg/PROSPERO_preregistration.md` §10–13; `data/exclusion_reason_codebook.md` | Inclusion in §2.2; per-stage exclusion-reason codebook with definitions. |
| 6 | Specify all databases, registers, websites, organisations, reference lists, and other sources searched or consulted to identify studies. Specify the date when each source was last searched or consulted. | `manuscript/manuscript.md` §2.3; `prereg/PROSPERO_preregistration.md` §7; `data/searches/search_strategy.md` | PubMed, PsycINFO, Web of Science Core, Scopus, Cochrane Central, ClinicalTrials.gov, OSF Registries, PsyArXiv, bioRxiv. Search window Q1–Q2 2026. |
| 7 | Present the full search strategies for all databases, registers, and websites, including any filters and limits used. | `data/searches/search_strategy.md`; `prereg/PROSPERO_preregistration.md` §7 | Boolean string reproduced verbatim; no language or date restrictions at database level. PRISMA-S checklist in `data/searches/PRISMA-S_checklist.md`. |
| 8 | Specify the methods used to decide whether a study met the inclusion criteria of the review, including how many reviewers screened each record and each report retrieved, whether they worked independently, and if applicable, details of automation tools used in the process. | `manuscript/manuscript.md` §2.4; `prereg/PROSPERO_preregistration.md` §19 (with deviation note) | Single-coder execution (deviation from two-reviewer protocol). No automation tools used at screening. |
| 9 | Specify the methods used to collect data from reports, including how many reviewers collected data from each report, whether they worked independently, any processes for obtaining or confirming data from study investigators, and if applicable, details of automation tools used in the process. | `manuscript/manuscript.md` §2.5; `prereg/PROSPERO_preregistration.md` §20 | Single-coder data extraction (deviation noted). Authors contacted for missing statistics where contact was discoverable. |
| 10a | List and define all outcomes for which data were sought. Specify whether all results that were compatible with each outcome domain in each study were sought, and if not, the methods used to decide which results to collect. | `manuscript/manuscript.md` §2.5; `prereg/PROSPERO_preregistration.md` §15–17 | Primary: peripheral physiology (SCR, HR, HRV, LPP, FPS). Secondary (narrative): amygdala BOLD, vlPFC/mPFC BOLD, self-report, clinical change. |
| 10b | List and define all other variables for which data were sought (e.g., participant and intervention characteristics, funding sources). Describe any assumptions made about any missing or unclear information. | `manuscript/manuscript.md` §2.5; `meta-analysis/extracted_effect_sizes.csv` columns | Sample size (n1, n2), lab affiliation (UCLA / independent), design (between/within), study identifier, year. |
| 11 | Specify the methods used to assess risk of bias in the included studies, including details of the tool(s) used, how many reviewers assessed each study and whether they worked independently, and if applicable, details of automation tools used in the process. | `manuscript/manuscript.md` §2.6; `supplementary/risk_of_bias.csv`; `supplementary/risk_of_bias_explanation.md` | RoB 2 (Sterne et al. 2019) for RCTs; ROBINS-I for non-randomized; adapted NRSI tool for within-subjects; GRADE for evidence body. Single-coder assessment; second-coder review welcomed via repository issues. |
| 12 | Specify for each outcome the effect measure(s) (e.g., risk ratio, mean difference) used in the synthesis or presentation of results. | `manuscript/manuscript.md` §2.5, §2.7; `prereg/PROSPERO_preregistration.md` §15 | Hedges' *g* (small-sample-corrected standardized mean difference) for the primary meta-analysis. |
| 13a | Describe the processes used to decide which studies were eligible for each synthesis (e.g., tabulating the study intervention characteristics and comparing against the planned groups for each synthesis). | `manuscript/manuscript.md` §2.7; `data/exclusion_reason_codebook.md` | Five synthesis subsets defined in PROSPERO §22 and operationalized via the codebook's `synthesis_subset` enum. |
| 13b | Describe any methods required to prepare the data for presentation or synthesis, such as handling of missing summary statistics or data conversions. | `manuscript/manuscript.md` §2.7; `meta-analysis/run_meta_analysis.py` | Cohen's *d* converted to Hedges' *g* via the small-sample correction *J* = 1 − 3/(4*df* − 1). Computations from raw F/t/M/SD where *d* not reported, per Borenstein et al. (2009). |
| 13c | Describe any methods used to tabulate or visually display results of individual studies and syntheses. | `figures/forest_plot.png/.pdf`; `figures/funnel_plot.png/.pdf`; `figures/rob_summary.png/.pdf`; `figures/prisma_flow.png/.pdf`; `manuscript/manuscript.md` §3 | Forest plot with study-level CIs and pooled diamond; funnel plot with pseudo-CI envelope; RoB traffic-light summary; PRISMA 2020 flow diagram. All deterministically regenerable from `make figures`. |
| 13d | Describe any methods used to synthesize results and provide a rationale for the choice(s). If meta-analysis was performed, describe the model(s), method(s) to identify the presence and extent of statistical heterogeneity, and software package(s) used. | `manuscript/manuscript.md` §2.7; `meta-analysis/run_meta_analysis.py` | Random-effects (DerSimonian-Laird τ²); Cochran's Q, I², τ², 95% prediction interval; Python `numpy`, `pandas`, `scipy`. Code is open and reproducible. |
| 13e | Describe any methods used to explore possible causes of heterogeneity among study results (e.g., subgroup analysis, meta-regression). | `manuscript/manuscript.md` §2.7; `prereg/PROSPERO_preregistration.md` §22 | Pre-specified moderators: lab affiliation, stimulus valence, sample population, language, outcome timing, sample-size quartile. Lab-stratified analysis is the headline moderator. |
| 13f | Describe any sensitivity analyses conducted to assess robustness of the synthesized results. | `manuscript/manuscript.md` §2.7, §3.3; `meta-analysis/leave_one_out.csv` | Leave-one-out (output: `meta-analysis/leave_one_out.csv`); UCLA-only restriction; independent-labs-only restriction. |
| 14 | Describe any methods used to assess risk of bias due to missing results in a synthesis (arising from reporting biases). | `manuscript/manuscript.md` §2.7; `meta-analysis/run_meta_analysis.py` (Egger's test) | Funnel-plot inspection, Egger's regression test (`Egger's intercept = -4.55, p = 0.16`), p-curve discussion. PET-PEESE not run on k=9. |
| 15 | Describe any methods used to assess certainty (or confidence) in the body of evidence for an outcome. | `manuscript/manuscript.md` §2.6 | GRADE narrative across the body of work. Quantitative GRADE rating not formally tabulated. |

## RESULTS

| # | Item | Reported on | Notes |
|---|------|-------------|-------|
| 16a | Describe the results of the search and selection process, from the number of records identified in the search to the number of studies included in the review, ideally using a flow diagram. | `figures/prisma_flow.png/.pdf`; `prisma/prisma_counts.txt`; `prisma/prisma_counts.csv`; `manuscript/manuscript.md` §3.1 | PRISMA 2020 flow diagram + structured counts CSV. 1,889 → 1,571 → 282 → 100. |
| 16b | Cite studies that might appear to meet the inclusion criteria, but which were excluded, and explain why they were excluded. | `manuscript/manuscript.md` §3.5; `data/exclusion_reason_codebook.md` | Notable exclusions discussed: removed Isaacowitz & Eldesouky (2024) as fabricated; flagged Burklund et al. (2024) for COI but included; excluded Birkenmaier et al. (2026 Cognition & Emotion null) is acknowledged in §3.5. |
| 17 | Cite each included study and present its characteristics. | `references.bib`; `data/screening/included_papers.csv`; `meta-analysis/extracted_effect_sizes.csv`; `supplementary/risk_of_bias.csv` | All 22 canonical-identifiable included studies enumerated with bibtex_key, subset, doi. |
| 18 | Present assessments of risk of bias for each included study. | `supplementary/risk_of_bias.csv`; `figures/rob_summary.png/.pdf`; `supplementary/risk_of_bias_explanation.md` | Per-domain judgments + traffic-light summary + per-study narrative rationale. |
| 19 | For all outcomes, present, for each study: (a) summary statistics for each group (where appropriate) and (b) an effect estimate and its precision (e.g., confidence/credible interval), ideally using structured tables or plots. | `meta-analysis/extracted_effect_sizes.csv`; `figures/forest_plot.png/.pdf` | Per-study Hedges' *g* with 95% CI in CSV and forest plot. |
| 20a | For each synthesis, briefly summarise the characteristics and risk of bias among contributing studies. | `manuscript/manuscript.md` §3.3 | Lab affiliation, design, sample size, RoB rating discussed for the k=9 synthesis. |
| 20b | Present results of all statistical syntheses conducted. If meta-analysis was done, present for each the summary estimate and its precision (e.g., confidence/credible interval) and measures of statistical heterogeneity. If comparing groups, describe the direction of the effect. | `manuscript/manuscript.md` §3.3; `meta-analysis/results_summary.txt` | Pooled *g* = −0.43 [−0.68, −0.18], *p* < .001, *I*² = 48.3%, τ² = 0.070, 95% PI [−1.13, +0.27]. |
| 20c | Present results of all investigations of possible causes of heterogeneity among study results. | `manuscript/manuscript.md` §3.3, §4.3; `meta-analysis/results_summary.txt` | UCLA-only: *g* = −0.74 [−1.02, −0.47], *I*² = 0%. Independent-only: *g* = −0.13 [−0.41, +0.14], *I*² = 27.8%. |
| 20d | Present results of all sensitivity analyses conducted to assess the robustness of the synthesized results. | `meta-analysis/leave_one_out.csv` | Leave-one-out CSV shows the pooled *g* range from −0.38 (drop Kircanski-vs-reappraisal) to −0.51 (drop Plaisted) — all sign-stable. |
| 21 | Present assessments of risk of bias due to missing results (arising from reporting biases) for each synthesis assessed. | `manuscript/manuscript.md` §3.3; `figures/funnel_plot.png/.pdf` | Egger's intercept = −4.55, *p* = .16. Funnel-plot inspection and discussion in §3.3. |
| 22 | Present assessments of certainty (or confidence) in the body of evidence for each outcome assessed. | `manuscript/manuscript.md` §4.1, §4.2 | GRADE-style narrative: peripheral-physiology effect "moderate certainty within paradigm; low certainty across paradigms." |

## DISCUSSION

| # | Item | Reported on | Notes |
|---|------|-------------|-------|
| 23a | Provide a general interpretation of the results in the context of other evidence. | `manuscript/manuscript.md` §4.1, §4.4 | "What is true" / "Boundary conditions: a calibrated map" sections. |
| 23b | Discuss any limitations of the evidence included in the review. | `manuscript/manuscript.md` §4.6 | Five enumerated limitations including small-sample fMRI base, single-lab concentration, outcome heterogeneity, k=9 underpower for moderators, English-only inclusion. |
| 23c | Discuss any limitations of the review processes used. | `manuscript/manuscript.md` §4.6 (item 6); `prereg/PROSPERO_preregistration.md` §19 (deviation note) | Single-coder screening; no inter-rater agreement available. |
| 23d | Discuss implications of the results for practice, policy, and future research. | `manuscript/manuscript.md` §4.5, §4.7, §5 | Section 4.5 = clinical translation; §4.7 = methodological recommendations; §5 = future directions. |

## OTHER INFORMATION

| # | Item | Reported on | Notes |
|---|------|-------------|-------|
| 24a | Provide registration information for the review, including the register name and registration number, or state that the review was not registered. | `manuscript/manuscript.md` §2.1; `prereg/PROSPERO_preregistration.md` §26 | Protocol authored PROSPERO-compatible (CRD template) but not formally submitted to the PROSPERO registry. The full protocol is open in `prereg/`. |
| 24b | Indicate where the review protocol can be accessed, or state that a protocol was not prepared. | `prereg/PROSPERO_preregistration.md`; permanent archive at Zenodo DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595) | Open and version-controlled. |
| 24c | Describe and explain any amendments to information provided at registration or in the protocol. | `prereg/PROSPERO_preregistration.md` §5, §19, §20; `manuscript/manuscript.md` §2.1, §4.6 | One execution deviation: single-coder screening (vs. two-reviewer protocol). Amendment is documented in three places. |
| 25 | Describe sources of financial or non-financial support for the review, and the role of the funders or sponsors in the review. | `prereg/PROSPERO_preregistration.md` §5; `manuscript/manuscript.md` "Funding" footnote | Unfunded. No financial sponsor; the named contact's time was uncompensated. |
| 26 | Declare any competing interests of review authors. | `prereg/PROSPERO_preregistration.md` §5; `manuscript/manuscript.md` "Conflicts of interest" footnote | No declared competing interests. The Burklund et al. (2024) **included** study has a documented commercial COI (NeuroGen Technologies); the review author has none. |
| 27 | Report which of the following are publicly available and where they can be found: template data collection forms; data extracted from included studies; data used for all analyses; analytic code; any other materials used in the review. | `README.md` "Data Availability"; `data/README.md`; full repository at https://github.com/mikhaeelatefrizk/affect-labeling-review | All listed items are public under CC-BY-4.0 (data) / CC-BY-4.0 (manuscript) / MIT (code). |

---

## Self-assessment summary

| Section | Items reported | Items partially reported | Items not reported |
|---------|---------------:|-------------------------:|-------------------:|
| Title (1) | 1 | 0 | 0 |
| Abstract (2) | 1 | 0 | 0 |
| Introduction (3–4) | 2 | 0 | 0 |
| Methods (5–15) | 18 | 0 | 0 |
| Results (16–22) | 9 | 0 | 0 |
| Discussion (23) | 4 | 0 | 0 |
| Other (24–27) | 6 | 0 | 0 |
| **Total** | **42 / 42** | **0** | **0** |

All 42 PRISMA 2020 items are reported in the open-research package, with explicit acknowledgement of the single-coder execution deviation (items 8, 9, 24c) and the GRADE simplification (items 15, 22).

## Re-checklist on data updates

When the screening corpus, included-papers list, or risk-of-bias judgments are amended in a future revision (e.g., a v1.1.0 release), this checklist should be re-walked, and items 16a, 17, 18, 20b, and 24c re-examined.

---

*This checklist is part of the open-research package archived at Zenodo DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595). Last updated for v1.0.0 (May 2026).*
