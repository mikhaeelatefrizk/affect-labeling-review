"""Risk-of-bias 'traffic light' summary figure (Cochrane-style)."""
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from pathlib import Path

studies = [
    ("Kircanski 2012",            "RCT", ["L","L","L","S","L"], "S"),
    ("Tabibnia 2008 (Exp 2)",     "RCT", ["L","S","L","L","L"], "S"),
    ("Niles 2015",                "RCT", ["L","S","L","L","S"], "S"),
    ("Plaisted 2022",             "RCT", ["L","L","L","L","L"], "L"),
    ("Burklund 2024 (PTSD)",      "NRSI",["H","H","S","S","H"], "H"),
    ("Lieberman 2007",            "fMRI",["M","L","L","L","M"], "M"),
    ("Hariri 2000",               "fMRI",["M","L","L","L","M"], "M"),
    ("Hariri 2003",               "fMRI",["L","L","L","L","L"], "L"),
    ("Torrisi 2013",              "DCM", ["M","L","L","L","M"], "M"),
    ("Burklund 2014",             "fMRI",["M","L","L","L","M"], "M"),
    ("Vives 2021",                "fMRI",["L","L","L","L","L"], "L"),
    ("Nook 2021",                 "Beh", ["L","L","L","L","L"], "L"),
    ("Ariely 2026",               "Beh", ["L","L","L","L","L"], "L"),
    ("Vlasenko 2021",             "Beh", ["L","L","L","L","L"], "L"),
    ("Levy-Gigi 2022",            "Beh", ["L","L","L","L","L"], "L"),
]

domains = ["D1\nRandomization /\nselection",
           "D2\nDeviations /\nintended",
           "D3\nMissing\noutcome data",
           "D4\nOutcome\nmeasurement",
           "D5\nSelective\nreporting",
           "Overall"]

color = {"L": "#2ca02c", "S": "#ffcc00", "M": "#ff9900",
         "H": "#d62728", "-": "#bbbbbb"}
symbol = {"L": "+", "S": "-", "M": "-", "H": "x", "-": "?"}

fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, len(domains) + 4.5)
ax.set_ylim(0, len(studies) + 1.5)
ax.invert_yaxis()
ax.axis("off")

col_offset = 4.0
for j, dom in enumerate(domains):
    ax.text(j + col_offset, 0.5, dom, ha="center", va="center",
            fontsize=8, weight="bold")

for i, (name, design, doms, overall) in enumerate(studies):
    ax.text(0.05, i + 1.5, f"{name} [{design}]",
            ha="left", va="center", fontsize=9)
    for j, d in enumerate(doms + [overall]):
        c = Circle((j + col_offset, i + 1.5), 0.32, facecolor=color[d],
                   edgecolor="black", linewidth=0.7)
        ax.add_patch(c)
        ax.text(j + col_offset, i + 1.5, symbol[d], ha="center", va="center",
                fontsize=10, color="white", weight="bold")

legend_y = len(studies) + 1.0
legend_items = [("L", "Low risk"), ("S", "Some concerns"),
                ("M", "Moderate"), ("H", "High risk"), ("-", "Not applicable")]
for k, (code, lab) in enumerate(legend_items):
    cx = col_offset + k * 1.6
    c = Circle((cx, legend_y), 0.22, facecolor=color[code],
               edgecolor="black", linewidth=0.7)
    ax.add_patch(c)
    ax.text(cx + 0.35, legend_y, lab, va="center", fontsize=8)

plt.title("Risk of bias assessment (RoB 2 / ROBINS-I / NRSI synthesis)",
          fontsize=11, weight="bold")

outdir = Path(__file__).resolve().parent.parent / "figures"
outdir.mkdir(exist_ok=True)
plt.savefig(outdir / "rob_summary.png", dpi=200, bbox_inches="tight")
plt.savefig(outdir / "rob_summary.pdf", bbox_inches="tight")
plt.close()
print("[OK] RoB summary figure written.")
