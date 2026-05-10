# Exclusion reason codebook

Authoritative definitions for the codes used in the `exclusion_reason` field of the screening log. Counts shown are from `prisma/prisma_counts.txt` (full-text exclusions only — title/abstract exclusions were not categorized per-paper in the original review).

## Full-text exclusion codes

| Code | Plain-language definition | Canonical count | Source-of-truth wording |
|------|---------------------------|-----------------|--------------------------|
| `no_al_manipulation` | The study did not include an affect-labeling manipulation as defined in PROSPERO §11. Examples: study reports affect labeling as an observed correlate but never instructs participants to label; or the "labeling" is of stimulus features (e.g., shape) rather than emotion. | 71 | "did not manipulate AL" |
| `no_phys_neural_outcome` | No physiological (skin conductance, heart rate, HRV, RSA, late positive potential, fear-potentiated startle) or neural (BOLD, EEG, MEG, fNIRS) outcome was measured. Self-report-only studies that meet other criteria are still included for the narrative synthesis. | 38 | "no physiological/neural outcome" |
| `review_without_primary_data` | The article is a literature review, narrative review, or commentary without primary empirical data. Existing meta-analyses are *not* excluded under this code — they form their own synthesis subset. | 26 | "review without primary data" |
| `non_english` | The full text is not available in English and no professionally translated version could be located. Per PROSPERO §25 this is a known limitation of the review. | 5 | "non-English" |
| `duplicate_sample` | The article reports on a sample that was already represented by another included study. The included study is the earliest/canonical report; later reports of the same sample are excluded under this code. | 6 | "duplicate sample" |
| `insufficient_data_for_extraction` | The article meets all eligibility criteria but does not report sufficient statistics to extract or compute Hedges' g (no d, F, t, raw means/SDs, or 95% CIs available). The authors were contacted where contact information was discoverable. | 36 | "insufficient data for ES" |
| | **Total full-text exclusions** | **182** | |

## Title/abstract exclusion codes

The 1,289 title/abstract exclusions in the original review were not categorized per-paper. For new screening passes (e.g., a future double-coded re-screen), the following broader codes are recommended:

| Code | Plain-language definition |
|------|---------------------------|
| `off_topic` | Title and abstract make clear the paper has nothing to do with affect labeling, emotion regulation, or the listed outcome modalities. |
| `wrong_population` | Children under 10, non-human animals, or clinical populations excluded by PROSPERO §10. |
| `wrong_design` | Single-case clinical reports; editorial/theoretical papers without primary data; lay-press articles. |
| `other` | Any other reason; record specifics in the `notes` column. |

`other` is intentionally broad — when used, the screener must record specifics in the `notes` field.

## Inclusion-side note

A paper that survives both screening stages is recorded with `decision = include` and assigned a `synthesis_subset` value:

| Subset | Count | Used in |
|--------|-------|---------|
| `psychophysiology_meta_analysis` | 9 | Quantitative random-effects meta-analysis |
| `neuroimaging_neurostim` | 42 | Narrative synthesis (foundational neuroscience) |
| `behavioral_self_report` | 28 | Narrative synthesis (behavioral evidence) |
| `clinical_patient_populations` | 12 | Narrative synthesis (clinical applications) |
| `prior_meta_analyses` | 9 | Existing-meta-analyses synthesis |
| **Total** | **100** | |

## License

CC-BY-4.0 — see [`LICENSE-DATA`](../LICENSE-DATA).
