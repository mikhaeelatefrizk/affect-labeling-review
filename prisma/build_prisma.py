"""PRISMA 2020 flow diagram + plain-text counts file.

Reads canonical counts from `prisma/prisma_counts.csv` (the structured source
of truth) and emits two outputs:

    1. `prisma/prisma_counts.txt` — legacy human-readable format
    2. `figures/prisma_flow.png` and `.pdf` — the PRISMA flow diagram

If `data/screening/derived_screening_log.csv` exists (produced by the Phase-2
derivation chain), the script also emits a `prisma_counts.derived.txt` with
the screening log's counts for comparison. Drift between canonical and
derived counts is informational, not error.

Usage:
    python prisma/build_prisma.py

Reproducibility:
    Outputs are byte-deterministic. If `make verify` reports a diff after
    running this, the canonical CSV was edited and the txt+figures need to
    be regenerated and committed.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import matplotlib.patches as patches
import matplotlib.pyplot as plt

REPO_ROOT = Path(__file__).resolve().parent.parent
COUNTS_CSV = REPO_ROOT / "prisma" / "prisma_counts.csv"
COUNTS_TXT = REPO_ROOT / "prisma" / "prisma_counts.txt"
FIGURES_DIR = REPO_ROOT / "figures"
DERIVED_LOG = REPO_ROOT / "data" / "screening" / "derived_screening_log.csv"
DERIVED_TXT = REPO_ROOT / "prisma" / "prisma_counts.derived.txt"


def load_counts(csv_path: Path) -> dict[str, int]:
    """Return a flat mapping of sub_stage -> count from the canonical CSV."""
    counts: dict[str, int] = {}
    with csv_path.open(encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            counts[row["sub_stage"]] = int(row["count"])
    return counts


def assert_internal_consistency(c: dict[str, int]) -> None:
    """Sanity-check that the canonical counts are arithmetically consistent."""
    expected_screened = (
        c["records_identified_databases"]
        + c["records_identified_other_sources"]
        - c["duplicates_removed"]
    )
    assert c["records_screened"] == expected_screened, (
        f"records_screened ({c['records_screened']}) != "
        f"identified - duplicates ({expected_screened})"
    )

    expected_full_text = c["records_screened"] - c["records_excluded_at_ti_ab"]
    assert c["full_text_assessed"] == expected_full_text, (
        f"full_text_assessed ({c['full_text_assessed']}) != "
        f"screened - excluded_ti_ab ({expected_full_text})"
    )

    breakdown_keys = [
        "no_al_manipulation",
        "no_phys_neural_outcome",
        "review_without_primary_data",
        "non_english",
        "duplicate_sample",
        "insufficient_data_for_extraction",
    ]
    breakdown_sum = sum(c[k] for k in breakdown_keys)
    assert c["full_text_excluded"] == breakdown_sum, (
        f"full_text_excluded ({c['full_text_excluded']}) != "
        f"sum of 6 breakdown reasons ({breakdown_sum})"
    )

    subset_keys = [
        "subset_neuroimaging_neurostim",
        "subset_psychophysiology_meta_analysis",
        "subset_behavioral_self_report",
        "subset_clinical_patient_populations",
        "subset_prior_meta_analyses",
    ]
    subset_sum = sum(c[k] for k in subset_keys)
    expected_total = c["full_text_assessed"] - c["full_text_excluded"]
    assert c["total"] == expected_total == subset_sum, (
        f"included total ({c['total']}) != "
        f"full-text minus excluded ({expected_total}) "
        f"or subset sum ({subset_sum})"
    )


def write_text_counts(c: dict[str, int], out: Path) -> None:
    """Write the legacy human-readable counts file."""
    lines = [
        "PRISMA 2020 counts - affect labeling systematic review",
        "=" * 60,
        f"Records identified (databases)        : {c['records_identified_databases']}",
        f"Records identified (other sources)    : {c['records_identified_other_sources']}",
        f"Duplicates removed                    : {c['duplicates_removed']}",
        f"Records screened (title/abstract)     : {c['records_screened']}",
        f"Excluded at title/abstract            : {c['records_excluded_at_ti_ab']}",
        f"Full-text assessed                    : {c['full_text_assessed']}",
        f"Full-text excluded total              : {c['full_text_excluded']}",
        f"  - did not manipulate AL             : {c['no_al_manipulation']}",
        f"  - no physiological/neural outcome   : {c['no_phys_neural_outcome']}",
        f"  - review without primary data       : {c['review_without_primary_data']}",
        f"  - non-English                       : {c['non_english']}",
        f"  - duplicate sample                  : {c['duplicate_sample']}",
        f"  - insufficient data for ES          : {c['insufficient_data_for_extraction']}",
        f"Included in synthesis                 : {c['total']}",
        f"  Neuroimaging/neurostim              : {c['subset_neuroimaging_neurostim']}",
        f"  Psychophysiology (meta-analysis)    : {c['subset_psychophysiology_meta_analysis']}",
        f"  Behavioral/self-report              : {c['subset_behavioral_self_report']}",
        f"  Clinical & patient populations      : {c['subset_clinical_patient_populations']}",
        f"  Existing meta-analyses              : {c['subset_prior_meta_analyses']}",
    ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def render_figure(c: dict[str, int], outdir: Path) -> None:
    """Render the PRISMA 2020 flow diagram to PNG + PDF."""
    fig, ax = plt.subplots(figsize=(10, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 14)
    ax.axis("off")

    def box(x, y, w, h, text, color="#f0f0f0", edge="black"):
        rect = patches.FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.05",
            linewidth=1.2, edgecolor=edge, facecolor=color,
        )
        ax.add_patch(rect)
        ax.text(x + w / 2, y + h / 2, text, ha="center", va="center",
                fontsize=9, wrap=True)

    def arrow(x1, y1, x2, y2):
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", lw=1.2, color="black"))

    phase_x, phase_w = 0.0, 0.4
    ax.text(phase_x + phase_w / 2, 12.6, "Identification",
            fontsize=10, weight="bold", rotation=90, va="center")
    ax.text(phase_x + phase_w / 2, 9.5, "Screening",
            fontsize=10, weight="bold", rotation=90, va="center")
    ax.text(phase_x + phase_w / 2, 6.0, "Eligibility",
            fontsize=10, weight="bold", rotation=90, va="center")
    ax.text(phase_x + phase_w / 2, 1.15, "Included",
            fontsize=10, weight="bold", rotation=90, va="center")

    box(2.2, 12.0, 3.0, 1.4,
        f"Records identified through\ndatabase searching\n(n = {c['records_identified_databases']})",
        color="#e8f0fe")
    box(5.6, 12.0, 3.0, 1.4,
        f"Additional records identified\nthrough other sources\n(n = {c['records_identified_other_sources']})",
        color="#e8f0fe")

    box(3.5, 9.8, 4.2, 1.3,
        f"Records after duplicates removed\n(n = {c['records_screened']})",
        color="#fff4e6")
    arrow(3.7, 12.0, 4.5, 11.1)
    arrow(7.1, 12.0, 6.5, 11.1)

    box(3.5, 7.6, 4.2, 1.3,
        f"Records screened\n(title and abstract)\n(n = {c['records_screened']})",
        color="#fff4e6")
    arrow(5.6, 9.8, 5.6, 8.9)
    box(8.0, 7.6, 1.8, 1.3,
        f"Records excluded\n(n = {c['records_excluded_at_ti_ab']})",
        color="#fce4ec")
    arrow(7.7, 8.25, 8.0, 8.25)

    box(3.5, 5.4, 4.2, 1.3,
        f"Full-text articles\nassessed for eligibility\n(n = {c['full_text_assessed']})",
        color="#fff4e6")
    arrow(5.6, 7.6, 5.6, 6.7)

    excl_text = (
        f"Full-text excluded\n(n = {c['full_text_excluded']}):\n"
        f"- No AL manip. ({c['no_al_manipulation']})\n"
        f"- No physiol/neural ({c['no_phys_neural_outcome']})\n"
        f"- Review only ({c['review_without_primary_data']})\n"
        f"- Non-English ({c['non_english']})\n"
        f"- Duplicate sample ({c['duplicate_sample']})\n"
        f"- Insuff. data ({c['insufficient_data_for_extraction']})"
    )
    box(8.0, 4.5, 1.85, 2.6, excl_text, color="#fce4ec")
    arrow(7.7, 6.05, 8.0, 6.05)

    box(3.5, 3.0, 4.2, 1.3,
        f"Studies included in qualitative\nsynthesis (n = {c['total']})",
        color="#e6f4ea")
    arrow(5.6, 5.4, 5.6, 4.3)

    box(0.6, 0.5, 1.7, 1.3,
        f"Neuroimaging\n& neurostim.\n(n = {c['subset_neuroimaging_neurostim']})",
        color="#e6f4ea")
    box(2.45, 0.5, 1.7, 1.3,
        f"Psychophys.\nmeta-analysis\n(n = {c['subset_psychophysiology_meta_analysis']})",
        color="#e6f4ea")
    box(4.3, 0.5, 1.7, 1.3,
        f"Behavioral &\nself-report\n(n = {c['subset_behavioral_self_report']})",
        color="#e6f4ea")
    box(6.15, 0.5, 1.7, 1.3,
        f"Clinical &\npatient pops.\n(n = {c['subset_clinical_patient_populations']})",
        color="#e6f4ea")
    box(8.0, 0.5, 1.7, 1.3,
        f"Existing meta-\nanalyses synth.\n(n = {c['subset_prior_meta_analyses']})",
        color="#e6f4ea")
    for x in [1.45, 3.3, 5.15, 7.0, 8.85]:
        arrow(5.6, 3.0, x, 1.8)

    ax.set_title("PRISMA 2020 flow diagram", fontsize=12, weight="bold", pad=10)

    outdir.mkdir(exist_ok=True)
    plt.savefig(outdir / "prisma_flow.png", dpi=200, bbox_inches="tight")
    plt.savefig(outdir / "prisma_flow.pdf", bbox_inches="tight")
    plt.close()


def maybe_compare_with_derived(canonical: dict[str, int]) -> None:
    """If the derived screening log exists, write a side-by-side comparison."""
    if not DERIVED_LOG.exists():
        return

    with DERIVED_LOG.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))

    derived_total_records = len(rows)
    derived_included = sum(1 for r in rows if r.get("decision") == "include")
    derived_excluded = sum(1 for r in rows if r.get("decision") == "exclude")

    lines = [
        "PRISMA counts - canonical vs. derived comparison",
        "=" * 60,
        "Numbers labelled 'canonical' are from prisma_counts.csv (manuscript-of-record).",
        "Numbers labelled 'derived' come from data/screening/derived_screening_log.csv,",
        "regenerated today by re-running the PROSPERO query against PubMed.",
        "Drift is expected because PubMed continues to grow.",
        "",
        f"Records (canonical, identified-databases) : {canonical['records_identified_databases']}",
        f"Records (derived, total in corpus)        : {derived_total_records}",
        f"Included (canonical, all subsets)         : {canonical['total']}",
        f"Included (derived, label=include)         : {derived_included}",
        f"Excluded (canonical, ti-ab + full-text)   : "
        f"{canonical['records_excluded_at_ti_ab'] + canonical['full_text_excluded']}",
        f"Excluded (derived, label=exclude)         : {derived_excluded}",
    ]
    DERIVED_TXT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    if not COUNTS_CSV.exists():
        sys.stderr.write(f"FAIL: {COUNTS_CSV} not found\n")
        return 1

    counts = load_counts(COUNTS_CSV)
    assert_internal_consistency(counts)
    write_text_counts(counts, COUNTS_TXT)
    render_figure(counts, FIGURES_DIR)
    maybe_compare_with_derived(counts)

    print(f"[OK] Wrote {COUNTS_TXT.relative_to(REPO_ROOT)}")
    print(f"[OK] Wrote {(FIGURES_DIR / 'prisma_flow.png').relative_to(REPO_ROOT)}")
    print(f"[OK] Wrote {(FIGURES_DIR / 'prisma_flow.pdf').relative_to(REPO_ROOT)}")
    if DERIVED_LOG.exists():
        print(f"[OK] Wrote {DERIVED_TXT.relative_to(REPO_ROOT)} (canonical vs. derived)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
