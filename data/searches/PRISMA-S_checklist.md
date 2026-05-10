# PRISMA-S Checklist

> Rethlefsen, M. L., Kirtley, S., Waffenschmidt, S., et al. (2021). PRISMA-S: An extension to the PRISMA statement for reporting literature searches in systematic reviews. *Systematic Reviews*, 10, 39. https://doi.org/10.1186/s13643-020-01542-z

PRISMA-S is the search-strategy reporting extension to PRISMA 2020. This checklist documents how each of the 16 PRISMA-S items is reported in the open-research package.

---

## Information Sources & Methods

| # | Item | Reported on | Notes |
|---|------|-------------|-------|
| 1 | Database name | `data/searches/search_strategy.md` Information sources table; `prereg/PROSPERO_preregistration.md` §7 | PubMed, PsycINFO, Web of Science Core Collection, Scopus, Cochrane Central Register of Controlled Trials, ClinicalTrials.gov, OSF Registries, PsyArXiv, bioRxiv. |
| 2 | Multi-database searching | `data/searches/search_strategy.md`; `data/searches/search_strategy.csv` | Five primary databases searched independently then aggregated; per-database hit counts not preserved (combined total: 1,842). |
| 3 | Study registries | `data/searches/search_strategy.md` row 6 | ClinicalTrials.gov searched in addition to journal-indexing databases. |
| 4 | Online resources and browsing | `data/searches/search_strategy.md` rows 7–9 | OSF Registries, PsyArXiv, bioRxiv (preprint and registration browsing). |
| 5 | Citation searching | `data/searches/search_strategy.md` "Reference chaining" §; `prereg/PROSPERO_preregistration.md` §7 | Forward + backward citation tracking from 9 anchor papers (Lieberman 2007, Hariri 2000/2003, Kircanski 2012, Tabibnia 2008, Torre & Lieberman 2018, Brooks 2017, Costafreda 2008, Vives 2021, Nook 2021). Yielded **47** "other sources" records before deduplication. |
| 6 | Contacts | Not used | No expert contacts were used at the search stage. The review's reference list was verified against PubMed and journals of record, but no original-author correspondence was used to identify additional records. |
| 7 | Other methods | `manuscript/manuscript.md` §2.3 | None beyond the database + reference-chaining methods above. |

## Search Strategies

| # | Item | Reported on | Notes |
|---|------|-------------|-------|
| 8 | Full search strategies | `data/searches/search_strategy.md` "Search query" §; `prereg/PROSPERO_preregistration.md` §7 | Boolean query reproduced verbatim. The query was applied identically across the five primary databases; database-specific syntax adaptations (e.g., MeSH expansion for PubMed) were left to each interface's automatic term mapping. |
| 9 | Limits and restrictions | `data/searches/search_strategy.md`; `prereg/PROSPERO_preregistration.md` §7 | No date or language restrictions at the database level. Language exclusions made at eligibility (PROSPERO §25; manuscript §2.2). |
| 10 | Search filters | None used | No published methodological filters (e.g., Cochrane RCT filter) applied at the database level. Design eligibility enforced at title/abstract and full-text stages. |
| 11 | Prior work | Not applicable | No earlier version of this search strategy. The pilot work informed the construction of the eligibility criteria but did not produce a published prior search. |
| 12 | Updates | `manuscript/manuscript.md` §2.3; `prereg/PROSPERO_preregistration.md` §7 | "From inception through the date of the final search; re-run within 14 days of manuscript submission." Search window canonical record: Q1–Q2 2026. |
| 13 | Dates of searches | `data/searches/search_strategy.md`; `prereg/PROSPERO_preregistration.md` §7 | The exact ISO date of the final search was not preserved in the canonical record; the Q1–Q2 2026 window aligns with the manuscript "Last updated: April 2026" timestamp. |

## Peer Review

| # | Item | Reported on | Notes |
|---|------|-------------|-------|
| 14 | Peer review | Not formally peer-reviewed | The search strategy was not peer-reviewed using a formal tool such as PRESS (Peer Review of Electronic Search Strategies). External peer review of the strategy is welcomed via repository issues. |

## Managing Records

| # | Item | Reported on | Notes |
|---|------|-------------|-------|
| 15 | Total records | `prisma/prisma_counts.txt`; `prisma/prisma_counts.csv`; `figures/prisma_flow.png/.pdf` | 1,842 records from 5 primary databases + 47 from citation tracking = 1,889 records identified before deduplication. |
| 16 | Deduplication | `prisma/prisma_counts.csv` row "duplicates_removed" | 318 duplicates removed before screening; 1,571 unique records progressed to title/abstract screening. |

---

## Reproducibility note

The Boolean search query in `data/searches/search_strategy.md` is paste-ready for re-execution at any of the five database interfaces. For PubMed specifically, the canonical query is also embedded in [`scripts/build_derived_corpus.py`](../../scripts/build_derived_corpus.py); a single `python scripts/build_derived_corpus.py` re-runs the search via the NCBI E-utilities API and produces a fresh `data/screening/derived_corpus.csv`. Hit counts will exceed the canonical 1,842 because PubMed continues to be indexed; this drift is reported in `data/QUALITY_REPORT.md` and is informational, not error.

---

*This checklist is part of the open-research package archived at Zenodo DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595). Last updated for v1.0.0 (May 2026).*
