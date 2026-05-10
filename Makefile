# =============================================================================
# affect-labeling-review — reproducibility Makefile
# =============================================================================
# Quick start:
#     make install     # install Python dependencies
#     make all         # regenerate every output in the repo
#     make verify      # check outputs match committed versions (CI uses this)
#     make clean       # remove generated files
#
# Each target is idempotent and writes outputs deterministically.
# All paths are relative to the repository root.
# =============================================================================

PY := python
PIP := $(PY) -m pip

.PHONY: help install analysis prisma rob figures derive screening-log quality validate all verify clean sha

help:
	@echo "Targets:"
	@echo "  install        - pip install -r requirements.txt"
	@echo "  analysis       - run meta-analysis/run_meta_analysis.py"
	@echo "  prisma         - run prisma/build_prisma.py (regenerates counts + figure)"
	@echo "  rob            - run supplementary/build_rob_figure.py"
	@echo "  figures        - alias for analysis + prisma + rob"
	@echo "  derive         - run derivation chain (PubMed re-query -> screening log)"
	@echo "  screening-log  - alias for derive"
	@echo "  quality        - generate data/QUALITY_REPORT.md"
	@echo "  validate       - schema-validate all CSVs in data/"
	@echo "  all            - install + figures + derive + quality + validate"
	@echo "  verify         - run all and assert no files changed (for CI)"
	@echo "  sha            - print SHA-256 of every generated output"
	@echo "  clean          - remove generated outputs"

install:
	$(PIP) install -r requirements.txt

analysis:
	$(PY) meta-analysis/run_meta_analysis.py

prisma:
	$(PY) prisma/build_prisma.py

rob:
	$(PY) supplementary/build_rob_figure.py

figures: analysis prisma rob

derive screening-log:
	$(PY) scripts/extract_included_list.py
	$(PY) scripts/build_derived_corpus.py
	$(PY) scripts/build_derived_screening_log.py

quality: derive
	$(PY) scripts/build_quality_report.py

validate:
	$(PY) scripts/validate_screening_log.py

all: install figures derive quality validate sha
	@echo ""
	@echo "[OK] Full build complete."

verify: all
	@git diff --exit-code -- '*.csv' '*.txt' '*.png' '*.pdf' '*.md' || \
		(echo "FAIL: outputs changed; commit the regenerated files."; exit 1)

sha:
	@echo "=== SHA-256 of generated outputs (paste into release notes) ==="
	@$(PY) -c "import hashlib, pathlib; \
	paths = sorted(p for p in pathlib.Path('.').rglob('*') if p.is_file() \
	    and any(s in str(p) for s in ['meta-analysis/', 'prisma/', 'supplementary/', 'figures/', 'data/']) \
	    and not str(p).startswith('.git')); \
	[print(hashlib.sha256(p.read_bytes()).hexdigest()[:16], p) for p in paths]"

clean:
	rm -f figures/*.png figures/*.pdf
	rm -f meta-analysis/extracted_effect_sizes.csv
	rm -f meta-analysis/leave_one_out.csv
	rm -f meta-analysis/results_summary.txt
	rm -f prisma/prisma_counts.txt
	rm -f prisma/prisma_counts.csv
	rm -f data/screening/included_papers.csv
	rm -f data/screening/derived_corpus.csv
	rm -f data/screening/derived_screening_log.csv
	rm -f data/QUALITY_REPORT.md
	@echo "[OK] Cleaned generated outputs."
