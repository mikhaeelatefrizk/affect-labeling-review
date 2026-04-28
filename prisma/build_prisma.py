"""PRISMA 2020 flow diagram for the affect labeling systematic review."""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from pathlib import Path

identified_db = 1842
identified_other = 47
duplicates = 318
screened = identified_db + identified_other - duplicates
excluded_title_abstract = 1289
full_text_assessed = screened - excluded_title_abstract
excl_no_AL = 71
excl_no_outcome = 38
excl_review = 26
excl_lang = 5
excl_dup_sample = 6
excl_no_extract = 36
total_excl_full = (excl_no_AL + excl_no_outcome + excl_review +
                   excl_lang + excl_dup_sample + excl_no_extract)
included_total = full_text_assessed - total_excl_full

included_neuro = 42
included_psychophys = 9
included_behavioral = 28
included_clinical = 12
included_review = 9
assert (included_neuro + included_psychophys + included_behavioral +
        included_clinical + included_review) == included_total

fig, ax = plt.subplots(figsize=(10, 12))
ax.set_xlim(0, 10); ax.set_ylim(0, 14); ax.axis("off")


def box(x, y, w, h, text, color="#f0f0f0", edge="black"):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05",
                                  linewidth=1.2, edgecolor=edge, facecolor=color)
    ax.add_patch(rect)
    ax.text(x + w/2, y + h/2, text, ha="center", va="center",
            fontsize=9, wrap=True)


def arrow(x1, y1, x2, y2):
    ax.annotate("", xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", lw=1.2, color="black"))


phase_x = 0.0; phase_w = 0.4
ax.text(phase_x + phase_w/2, 12.6, "Identification", fontsize=10, weight="bold", rotation=90, va="center")
ax.text(phase_x + phase_w/2, 9.5, "Screening", fontsize=10, weight="bold", rotation=90, va="center")
ax.text(phase_x + phase_w/2, 6.0, "Eligibility", fontsize=10, weight="bold", rotation=90, va="center")
ax.text(phase_x + phase_w/2, 1.15, "Included", fontsize=10, weight="bold", rotation=90, va="center")

box(2.2, 12.0, 3.0, 1.4, f"Records identified through\ndatabase searching\n(n = {identified_db})", color="#e8f0fe")
box(5.6, 12.0, 3.0, 1.4, f"Additional records identified\nthrough other sources\n(n = {identified_other})", color="#e8f0fe")

box(3.5, 9.8, 4.2, 1.3, f"Records after duplicates removed\n(n = {screened})", color="#fff4e6")
arrow(3.7, 12.0, 4.5, 11.1)
arrow(7.1, 12.0, 6.5, 11.1)

box(3.5, 7.6, 4.2, 1.3, f"Records screened\n(title and abstract)\n(n = {screened})", color="#fff4e6")
arrow(5.6, 9.8, 5.6, 8.9)
box(8.0, 7.6, 1.8, 1.3, f"Records excluded\n(n = {excluded_title_abstract})", color="#fce4ec")
arrow(7.7, 8.25, 8.0, 8.25)

box(3.5, 5.4, 4.2, 1.3, f"Full-text articles\nassessed for eligibility\n(n = {full_text_assessed})", color="#fff4e6")
arrow(5.6, 7.6, 5.6, 6.7)

excl_text = (f"Full-text excluded\n(n = {total_excl_full}):\n"
             f"- No AL manip. ({excl_no_AL})\n"
             f"- No physiol/neural ({excl_no_outcome})\n"
             f"- Review only ({excl_review})\n"
             f"- Non-English ({excl_lang})\n"
             f"- Duplicate sample ({excl_dup_sample})\n"
             f"- Insuff. data ({excl_no_extract})")
box(8.0, 4.5, 1.85, 2.6, excl_text, color="#fce4ec")
arrow(7.7, 6.05, 8.0, 6.05)

box(3.5, 3.0, 4.2, 1.3, f"Studies included in qualitative\nsynthesis (n = {included_total})", color="#e6f4ea")
arrow(5.6, 5.4, 5.6, 4.3)

box(0.6, 0.5, 1.7, 1.3, f"Neuroimaging\n& neurostim.\n(n = {included_neuro})", color="#e6f4ea")
box(2.45, 0.5, 1.7, 1.3, f"Psychophys.\nmeta-analysis\n(n = {included_psychophys})", color="#e6f4ea")
box(4.3, 0.5, 1.7, 1.3, f"Behavioral &\nself-report\n(n = {included_behavioral})", color="#e6f4ea")
box(6.15, 0.5, 1.7, 1.3, f"Clinical &\npatient pops.\n(n = {included_clinical})", color="#e6f4ea")
box(8.0, 0.5, 1.7, 1.3, f"Existing meta-\nanalyses synth.\n(n = {included_review})", color="#e6f4ea")
for x in [1.45, 3.3, 5.15, 7.0, 8.85]:
    arrow(5.6, 3.0, x, 1.8)

ax.set_title("PRISMA 2020 flow diagram", fontsize=12, weight="bold", pad=10)

outdir = Path(__file__).resolve().parent.parent / "figures"
outdir.mkdir(exist_ok=True)
plt.savefig(outdir / "prisma_flow.png", dpi=200, bbox_inches="tight")
plt.savefig(outdir / "prisma_flow.pdf", bbox_inches="tight")
plt.close()

with open(Path(__file__).resolve().parent / "prisma_counts.txt", "w", encoding="utf-8") as f:
    f.write("PRISMA 2020 counts - affect labeling systematic review\n")
    f.write("=" * 60 + "\n")
    f.write(f"Records identified (databases)        : {identified_db}\n")
    f.write(f"Records identified (other sources)    : {identified_other}\n")
    f.write(f"Duplicates removed                    : {duplicates}\n")
    f.write(f"Records screened (title/abstract)     : {screened}\n")
    f.write(f"Excluded at title/abstract            : {excluded_title_abstract}\n")
    f.write(f"Full-text assessed                    : {full_text_assessed}\n")
    f.write(f"Full-text excluded total              : {total_excl_full}\n")
    f.write(f"  - did not manipulate AL             : {excl_no_AL}\n")
    f.write(f"  - no physiological/neural outcome   : {excl_no_outcome}\n")
    f.write(f"  - review without primary data       : {excl_review}\n")
    f.write(f"  - non-English                       : {excl_lang}\n")
    f.write(f"  - duplicate sample                  : {excl_dup_sample}\n")
    f.write(f"  - insufficient data for ES          : {excl_no_extract}\n")
    f.write(f"Included in synthesis                 : {included_total}\n")
    f.write(f"  Neuroimaging/neurostim              : {included_neuro}\n")
    f.write(f"  Psychophysiology (meta-analysis)    : {included_psychophys}\n")
    f.write(f"  Behavioral/self-report              : {included_behavioral}\n")
    f.write(f"  Clinical & patient populations      : {included_clinical}\n")
    f.write(f"  Existing meta-analyses              : {included_review}\n")
print("[OK] PRISMA flow + counts written.")
