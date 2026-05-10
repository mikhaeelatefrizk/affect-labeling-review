# Search strategy (PRISMA-S compliant)

> Restructured from the canonical record at [`prereg/PROSPERO_preregistration.md`](../../prereg/PROSPERO_preregistration.md), Section 7. No values changed.

## Information sources

| # | Database | Interface | Coverage | Date searched | Hits |
|---|----------|-----------|----------|---------------|------|
| 1 | PubMed | NCBI Web | 1966–present | — | — |
| 2 | PsycINFO | APA PsycNET | 1887–present | — | — |
| 3 | Web of Science Core Collection | Clarivate | 1900–present | — | — |
| 4 | Scopus | Elsevier | 1970–present | — | — |
| 5 | Cochrane Central Register of Controlled Trials | Cochrane Library | 1996–present | — | — |
| 6 | ClinicalTrials.gov | NIH | 2000–present | — | — |
| 7 | OSF Registries | OSF | 2014–present | — | — |
| 8 | PsyArXiv | OSF | 2017–present | — | — |
| 9 | bioRxiv | CSHL | 2013–present | — | — |
|   | **Database total (combined)** | | | Q1–Q2 2026 | **1,842** |
|   | Other sources (citation tracking) | Reference chaining | n/a | n/a | **47** |
|   | **Grand total** | | | | **1,889** |

**Note on per-database hits.** The original search log preserved only the combined 1,842 figure across the five primary databases (PubMed + PsycINFO + Web of Science + Scopus + Cochrane Central); the em-dashes above mark per-database fields that the canonical record does not break out individually. To compute per-database counts, re-run the queries below at each interface; expect drift since the original search because the databases continue to grow.

## Search dates

> "From inception through the date of the final search; re-run within 14 days of manuscript submission."

— PROSPERO §7

The canonical record reports the search window as Q1–Q2 2026 (consistent with the manuscript and preregistration "Last updated: April 2026" timestamp). The original search log did not preserve a single exact ISO date for the final search.

## Search query (canonical)

```
("affect labeling" OR "affect labelling" OR "putting feelings into words"
 OR "emotion naming" OR "emotion labeling" OR "emotion labelling"
 OR "verbalizing emotion" OR "verbal labeling")
AND
("emotion regulation" OR "amygdala" OR "ventrolateral prefrontal"
 OR "skin conductance" OR "heart rate" OR "heart rate variability"
 OR "respiratory sinus arrhythmia" OR "late positive potential"
 OR "exposure therapy" OR "anxiety")
```

No date or language restrictions at the database level. Language exclusions made at the eligibility stage.

## Reference chaining

Forward and backward citation tracking from anchor papers:

- Lieberman et al. (2007) — *Psychological Science*
- Hariri et al. (2000, 2003) — *NeuroReport / Biological Psychiatry*
- Kircanski et al. (2012) — *Psychological Science*
- Tabibnia et al. (2008) — *Emotion*
- Torre & Lieberman (2018) — *Emotion Review*
- Brooks et al. (2017) — *SCAN*
- Costafreda et al. (2008) — *Brain Research Reviews*
- Vives et al. (2021) — *Affective Science*
- Nook et al. (2021) — *Affective Science*

These chains contributed the **47 records** marked "other sources" in the PRISMA flow.

## Programmatic re-derivation (PubMed)

`scripts/build_derived_corpus.py` re-runs an equivalent PubMed query via the NCBI E-utilities API and emits `data/screening/derived_corpus.csv`. The script's query is documented in its module docstring; differences from the canonical query (database-specific syntax, e.g., MeSH expansion) are noted explicitly.

## License

CC-BY-4.0 — see [`LICENSE-DATA`](../../LICENSE-DATA).
