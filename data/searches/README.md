# `data/searches/` — pre-registered search strategy

The pre-registered search strategy and its execution record.

## Year filter — the single most-asked question

> **No year filter was applied at the database level.**
>
> Per PROSPERO §7: *"From inception through the date of the final search; re-run within 14 days of manuscript submission."* The final search window was **Q1–Q2 2026**. No date or language restrictions were applied at any database. Language exclusions were made later, at the eligibility stage.
>
> **If you are re-running the searches** to reproduce or extend this work, apply **no year filter** — or, if your database interface requires an upper bound, cap at **30 June 2026** to match the original search window. Records published after that date are out-of-scope for matching against the published inclusion labels.
>
> Database coverage windows (each one is "from-inception through Q1–Q2 2026"):
>
> | Database | Coverage start |
> |---|---|
> | PubMed | 1966 |
> | PsycINFO | 1887 |
> | Web of Science Core Collection | 1900 |
> | Scopus | 1970 |
> | Cochrane Central | 1996 |
> | ClinicalTrials.gov | 2000 |
> | OSF Registries | 2014 |
> | PsyArXiv | 2017 |
> | bioRxiv | 2013 |

## What's here

| File | Description |
|------|-------------|
| `search_strategy.md` | PRISMA-S compliant human-readable report: every database, interface, query string, and (where preserved) date and hit count. |
| `search_strategy.csv` | Structured machine-readable form of the same information. |
| `PRISMA-S_checklist.md` | 16-item PRISMA-S checklist (reporting standard for SLR search strategies). |

## Source of truth

The canonical query string is in [`prereg/PROSPERO_preregistration.md`](../../prereg/PROSPERO_preregistration.md), Section 7. The files here are restructured copies for tooling — values match the preregistration exactly.

## What is *not* here

The original raw search exports (the .ris / .ciw / .csv files exported from each database at search time) were not retained. The aggregate count of 1,842 records identified through database searching is in `prisma/prisma_counts.csv` and is reported as the canonical figure in the manuscript.

For ML researchers who want a downloadable corpus of candidate papers, the closest reproducible artifact is `data/screening/derived_corpus.csv`, which is regenerated on demand by re-running the canonical PubMed query via the PubMed E-utilities API. See [`data/screening/README.md`](../screening/README.md).

## Re-running a database search

The `search_strategy.csv` file lists the exact query for each database. To re-run a search:

1. Open the database's interface.
2. Paste the canonical Boolean query verbatim (it's reproduced in `search_strategy.md` §"Search query").
3. **Apply no year filter** (see above). If forced to set an upper bound, use `2026/06/30`.
4. Apply no language filter at this stage; language exclusion happens at eligibility.
5. Export results in the database's standard format.

Hit counts will differ from the canonical 1,842 because the databases have grown since the original search. The drift is informational, not error.

## License

CC-BY-4.0 — see [`LICENSE-DATA`](../../LICENSE-DATA).
