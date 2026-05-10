# `data/searches/` — pre-registered search strategy

The pre-registered search strategy and its execution record.

## What's here

| File | Description |
|------|-------------|
| `search_strategy.md` | PRISMA-S compliant human-readable report: every database, interface, query string, and (where preserved) date and hit count. |
| `search_strategy.csv` | Structured machine-readable form of the same information. |

## Source of truth

The canonical query string is in [`prereg/PROSPERO_preregistration.md`](../../prereg/PROSPERO_preregistration.md), Section 7. The files here are restructured copies for tooling — values match the preregistration exactly.

## What is *not* here

The original raw search exports (the .ris / .ciw / .csv files exported from each database at search time) were not retained. The aggregate count of 1,842 records identified through database searching is in `prisma/prisma_counts.txt` and is reported as the canonical figure in the manuscript.

For ML researchers who want a downloadable corpus of candidate papers, the closest reproducible artifact is `data/screening/derived_corpus.csv`, which is regenerated on demand by re-running the canonical PubMed query via the PubMed E-utilities API. See [`data/screening/README.md`](../screening/README.md).

## Re-running a database search

The `search_strategy.csv` file lists the exact query for each database. To re-run a search, paste the query into the database's interface and export results. Hit counts will differ from the canonical 1,842 because the databases have grown since the original search. The drift is informational, not error.

## License

CC-BY-4.0 — see [`LICENSE-DATA`](../../LICENSE-DATA).
