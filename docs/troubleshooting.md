# Troubleshooting

Top issues a reproducer is likely to hit, with concrete fixes.

---

## 1. `pip install -r requirements.txt` fails with version conflicts

**Symptom:** pip resolver complains about incompatible versions.

**Cause:** You probably already have a different version of numpy / pandas / matplotlib in the active environment.

**Fix:** Use a fresh virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 2. `python prisma/build_prisma.py` produces a different PNG than committed

**Symptom:** `git diff figures/prisma_flow.png` shows changes after running.

**Cause:** matplotlib version mismatch. The committed PNGs were generated with matplotlib 3.8.2. matplotlib 3.10.x produces visually identical but byte-different PNGs.

**Fix (if you need byte-identical PNGs):**

```bash
pip install matplotlib==3.8.2
python prisma/build_prisma.py
```

**Alternative:** ignore PNG drift; the underlying numerical content (`prisma/prisma_counts.txt`) is byte-identical regardless of matplotlib version.

---

## 3. `python scripts/build_derived_corpus.py` is very slow or times out

**Symptom:** EFetch batches take 30+ seconds each; the script runs for 10+ minutes.

**Cause:** PubMed E-utilities rate-limits unauthenticated requests to 3/sec. With 3,892 records and batch size 200, this is ~20 batches at ~0.34 s/req plus EFetch's per-batch latency, which can take 2–5 minutes.

**Fix:** Get a free NCBI API key at https://www.ncbi.nlm.nih.gov/account/ and set:

```bash
export NCBI_API_KEY=your_key_here       # Linux/macOS
$env:NCBI_API_KEY="your_key_here"       # Windows PowerShell
```

The script auto-detects the env var and bumps the rate limit to 10/sec, dropping total runtime to ~30 seconds.

---

## 4. Encoding error on Windows: `'charmap' codec can't decode byte 0x...`

**Symptom:** Python error reading a CSV with non-ASCII characters (e.g., Vives' co-author Costumero, or Vlasenko's first name with diacritics).

**Cause:** Default Windows encoding is cp1252, not UTF-8.

**Fix:** All scripts in this repo open files with `encoding="utf-8"` explicitly. If you wrote a custom one-off script, do the same:

```python
with open(path, encoding="utf-8") as fh:
    ...
```

---

## 5. `make` not found on Windows

**Symptom:** `'make' is not recognized as an internal or external command`.

**Cause:** Windows does not ship `make`.

**Fix:** Three options:

- Use WSL2 (recommended, no other changes needed).
- Install via `chocolatey install make` or `winget install GnuWin32.Make`.
- Skip `make` entirely and run scripts directly. The full sequence is in [`reproducibility-guide.md`](reproducibility-guide.md) "Without `make`".

---

## 6. matplotlib backend error on a headless server

**Symptom:** `_tkinter.TclError: no display name and no $DISPLAY environment variable`.

**Cause:** matplotlib trying to use an interactive backend on a server without a display.

**Fix:** Set the non-interactive Agg backend before any matplotlib import:

```bash
export MPLBACKEND=Agg
python prisma/build_prisma.py
```

Or in the script (already done in our scripts via `matplotlib.use("Agg")` — should not happen).

---

## 7. `validate_screening_log.py` reports schema errors on `derived_screening_log.csv`

**Symptom:** Many "missing required field 'record_id'" errors.

**Cause:** The validator can't skip the provenance comment lines at the top of `derived_screening_log.csv` (the lines starting with `#`).

**Fix:** This was a v1.0.0-rc1 bug, fixed before release. If you see it, ensure you're on the v1.0.0 release tag:

```bash
git fetch --tags
git checkout v1.0.0
```

---

## 8. CI badge shows "failing" on the repo's main page

**Symptom:** Red CI badge.

**Cause:** As of v1.0.0 (May 2026), the maintainer's GitHub account has a temporary platform-level billing flag preventing GitHub Actions from running. The workflow file itself is correct and runs successfully on any other account.

**Fix:** Not a code issue. The CI badge has been removed from the README in v1.0.0 to avoid the misleading "failing" indicator until the billing block is lifted. The auto-trigger has been disabled in [`.github/workflows/ci.yml`](../.github/workflows/ci.yml). To verify locally, use `make verify` or follow [`reproducibility-guide.md`](reproducibility-guide.md).

---

## 9. `pip install` succeeds but `python -c "import pandas"` fails

**Symptom:** `ImportError: cannot import name 'X' from 'pandas'`.

**Cause:** You have multiple pandas installations on PATH, or a system pandas is shadowing the venv pandas.

**Fix:**

```bash
which python   # Linux/macOS — confirm it's the venv Python
where python   # Windows
python -c "import pandas; print(pandas.__file__, pandas.__version__)"
```

If the path doesn't include `.venv/`, your venv isn't activated. Re-activate.

---

## 10. `python scripts/build_derived_corpus.py` returns 0 records

**Symptom:** PubMed reports `0 matching records`.

**Cause:** Network connectivity, or a transient NCBI E-utilities outage.

**Fix:** Check NCBI status at https://www.ncbi.nlm.nih.gov/ and retry. If you're behind a corporate firewall blocking eutils.ncbi.nlm.nih.gov, you'll need to whitelist that domain.

---

## Still stuck?

Open a [reproducibility issue](https://github.com/mikhaeelatefrizk/affect-labeling-review/issues/new?template=reproducibility.yml) with:

- Your platform (OS + version)
- Python version (`python --version`)
- `pip freeze` output
- The full error traceback
- The output of `git diff --stat` after `make all`

The reproducibility issue template walks you through this.

---

*This troubleshooting guide is part of the open-research package archived at Zenodo DOI [10.5281/zenodo.20109595](https://doi.org/10.5281/zenodo.20109595). Last updated for v1.0.0 (May 2026).*
