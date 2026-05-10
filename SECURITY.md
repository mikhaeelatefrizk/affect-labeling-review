# Security policy

## Scope

This is an academic open-research package. The threat surface is small:

- Python scripts that run *locally* on a maintainer's or reproducer's machine.
- A network call to `eutils.ncbi.nlm.nih.gov` (NCBI's PubMed API) from `scripts/build_derived_corpus.py`.
- A GitHub Actions workflow that runs the analysis scripts on push.

There is no web service, no database, no authentication system, and no user data. The repository contains only public, citable scientific content under CC-BY-4.0 / MIT licenses.

That said, the repository may grow, and the following policy applies.

## Reporting a vulnerability

If you discover a security issue, please **do not open a public issue**. Instead:

1. Email the maintainer directly: `mikhaeelatefrizk@proton.me`.
2. Subject line: `[SECURITY] <one-line summary>`.
3. Include reproduction steps, the affected file(s) and version (commit SHA or tag), and your assessment of severity.

The maintainer will acknowledge within 7 days and aim to publish a fix within 30 days. After the fix is public, you'll be credited in the commit message and (with your consent) in this file.

## What counts as a vulnerability

For this repository, vulnerabilities of interest include:

- **Code execution.** A way for a malicious input to cause script execution beyond the intended computation (e.g., a malformed CSV that triggers an injection in a downstream tool).
- **Sensitive-data exfiltration.** A way for the scripts to leak local files, environment variables, or credentials. None of the scripts read credentials by design; reports of accidental credential exposure are welcomed.
- **Network mis-direction.** A way to redirect the PubMed E-utilities call to a malicious server (e.g., via TLS verification skipping).
- **Supply-chain.** A pinned dependency in `requirements.txt` that has a published CVE relevant to how this code uses it.

## What is *not* a vulnerability

- Disagreement with a methodological choice — open a [data correction issue](https://github.com/mikhaeelatefrizk/affect-labeling-review/issues/new?template=data_correction.yml) or an [erratum issue](https://github.com/mikhaeelatefrizk/affect-labeling-review/issues/new?template=erratum.yml) instead.
- An academic critique of a result — peer review channels are appropriate.
- A reproducibility failure — open a [reproducibility issue](https://github.com/mikhaeelatefrizk/affect-labeling-review/issues/new?template=reproducibility.yml).

## Supported versions

| Version | Supported |
|---|---|
| v1.0.x | ✅ Yes |
| Pre-1.0 | ❌ No |

## Scope of fixes

For an academic repository this small, security fixes will be issued as patch releases (v1.0.x). The current pinned dependency set is reviewed against published CVEs at each release.
