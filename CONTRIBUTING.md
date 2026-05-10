# Contributing

Thanks for your interest in this systematic review. The repository is intended both as a permanent record of the published work and as a living artifact that can be corrected, extended, or reused.

This document is short by design. If something here doesn't cover your situation, open an issue and ask.

## Ways to contribute

The repository is **single-author** and not actively soliciting code contributions. The most welcome contributions are:

1. **Errata.** A wrong citation, a wrong DOI, a wrong number in a table. File an issue using the **Erratum** template; pull requests with a fix are welcome.
2. **Data corrections.** A study that should/shouldn't have been included, an effect size you compute differently, a missing risk-of-bias signal. Use the **Data correction** issue template. Provide your computation so it's reproducible.
3. **Reproducibility failures.** `make all` doesn't reproduce the committed outputs on your machine. Use the **Reproducibility issue** template and include your platform, Python version, and the diff between your output and the committed file.
4. **Re-derivation issues.** The PubMed re-query in `scripts/build_derived_corpus.py` returns a hit count wildly different from what's documented. This is expected to drift over time as PubMed grows; large drifts (>30%) may indicate a query encoding issue worth investigating.
5. **New evidence.** A new study that would change the meta-analytic conclusions. Open an issue rather than a PR; substantive scientific updates require a manuscript revision, not a code merge.

## What this repo is not

- **Not a venue for original research debate.** Disagreements with the manuscript's interpretation belong in peer review, journal commentaries, or your own paper.
- **Not a place to add unrelated affect-labeling resources.** Keep PRs scoped to the systematic review itself.
- **Not a place to relitigate exclusion decisions** for individual papers without new evidence.

## How to make a code or data change

```bash
git clone https://github.com/mikhaeelatefrizk/affect-labeling-review.git
cd affect-labeling-review
make install               # installs pinned dependencies
make all                   # regenerates every output; should be a no-op diff
git checkout -b your-fix
# ... edit files ...
make verify                # re-runs everything and asserts no unintended drift
git commit -am "Fix X (closes #NN)"
git push -u origin your-fix
```

Open a pull request describing what you changed and why. Reference the issue if there is one.

## Style

- **Python.** Follow PEP 8. Format with `black`, lint with `ruff`. Functions get type hints; comments explain *why*, not *what*.
- **Markdown.** Wrap soft at ~100 characters where natural. Tables for structured data.
- **Commit messages.** Imperative mood, present tense. First line under 72 chars. If the change touches data, include the SHA-256 of the changed file in the body.

## Methodological note

This review was screened by a single coder. Inter-rater agreement statistics are not available. This is documented in the manuscript and in `data/screening/README.md`. Future re-screening with a second independent coder is welcome and should be reported as a separate, dated screening pass alongside the existing log rather than overwriting it.

## Conduct

By contributing you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

## Contact

For anything that doesn't fit above: open an issue. For private matters, the maintainer's email is in `CITATION.cff`.
