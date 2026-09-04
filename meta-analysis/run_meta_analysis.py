"""
Random-effects meta-analysis of affect labeling effects on peripheral
psychophysiology (skin conductance, heart rate, respiratory sinus arrhythmia).

Reproducibility: Run `python run_meta_analysis.py` to regenerate all numerical
results and figures. Requires numpy, pandas, scipy, matplotlib.
"""

import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from pathlib import Path

# All eight Cohen's d values are extracted from published reports (Kircanski
# 2012 reports d directly). Where only F, t, or condition means and SDs were
# available, d was computed via Borenstein, Hedges, Higgins, & Rothstein (2009)
# conversions. Hedges' small-sample correction J = 1 - 3/(4*df - 1) converts d
# to g for synthesis. Negative values indicate AL produced LOWER physiological
# arousal. Every row carries `derivation="extracted"`; the field exists so that
# any future imputed value has to declare itself.
#
# CORRECTION HISTORY. Through v1.0.1 this list carried nine rows, three of them
# (Plaisted 2022, McRae 2010, Fitzpatrick 2019) round stand-in values encoding
# "the report describes a null" rather than extracted standardized mean
# differences, while the header claimed all values were extracted. Those three
# carried ~70% of the fixed-effect weight of the independent-lab stratum, which
# is what produces the lab-stratified contrast. They have been resolved:
#
#   Plaisted 2022    0.00  -> -0.220  extracted from Table 2 (n corrected
#                                     20/20 -> 27/27; three-arm RCT, N=81)
#   Fitzpatrick 2019 -0.10 -> -0.036  extracted from Table 3 (n corrected
#                                     15/15 -> 30 within-subject)
#   McRae 2010       +0.10 -> DROPPED
#
# McRae 2010 is excluded rather than estimated. The paper is closed access with
# no repository copy, so no statistic could be recovered, and the contrast as
# previously coded ("subjective AL vs. passive") appears not to exist in it:
# the design compares subjective against OBJECTIVE labelling across four
# exposure durations, and the reported finding is an interaction rather than a
# labelling-versus-control mean difference. Coding an unreadable paper against
# a contrast it may not contain is not defensible, so it is documented here as
# an exclusion. It can be reinstated if the full text is obtained.

studies = [
    dict(study="Kircanski 2012 (vs. reappraisal)", year=2012, lab="UCLA",
         n1=22, n2=22, d=-0.85, design="between", derivation="extracted",
         note="SCR 1wk follow-up"),
    dict(study="Kircanski 2012 (vs. distraction)", year=2012, lab="UCLA",
         n1=22, n2=22, d=-0.74, design="between", derivation="extracted",
         note="SCR 1wk follow-up"),
    dict(study="Kircanski 2012 (vs. exposure-only)", year=2012, lab="UCLA",
         n1=22, n2=22, d=-0.64, design="between", derivation="extracted",
         note="SCR 1wk follow-up"),
    dict(study="Tabibnia 2008 (Exp 2: neg-label vs. exposure)", year=2008,
         lab="UCLA", n1=17, n2=15, d=-0.923, design="between",
         derivation="extracted",
         note="SCR Day 8; reported as t(32)=2.61, but n1=17/n2=15 gives df=30; "
         "d is back-computed consistently with n"),
    dict(study="Niles 2015 (SCR-NS, recovery)", year=2015, lab="UCLA",
         n1=20, n2=20, d=-0.691, design="between", derivation="extracted",
         note="NS-SCR during recovery; reconstructed from t,df"),
    dict(study="Plaisted 2022 (HR recovery, adolescents, RCT)", year=2022,
         lab="Birmingham/Reading/Oxford", n1=27, n2=27, d=-0.220, design="between",
         derivation="extracted",
         note="Post-speech (recovery) HR at 1-week follow-up, affect-label vs. "
         "control, from the Table 2 means/SDs: 90.2 (9.4) vs. 92.2 (8.8), n=27 per "
         "arm. Recovery window chosen to match Niles 2015. Three-arm RCT, N=81; the "
         "positive-coping-statements arm is not part of this contrast. LIMITATION: "
         "arms are not balanced at pre-test (the affect-label arm starts ~3-4 bpm "
         "high), so the pre->1wk change score gives d = -0.49 instead; that is "
         "reported as a sensitivity analysis, not the primary value, because its SE "
         "needs a pre-post correlation the paper does not report. The "
         "acknowledgements thank M. Craske, which bears on the lab-independence "
         "moderator."),
    dict(study="Fitzpatrick 2019 (SCR, healthy controls)", year=2019,
         lab="Toronto/York", n1=30, n2=30, d=-0.036, design="within",
         derivation="extracted",
         note="Healthy-control emotion-induction SCR, label vs. control, computed "
         "from the Table 3 HC means/SDs averaged over the two script types: label "
         "3.095 vs. control 3.205, pooled SD 3.020, n=30 within-subject. The paper "
         "reports no HC-only inferential test (no post-hoc was run because the "
         "condition x group interaction was n.s.), so this comes from the "
         "descriptives. LIMITATION: SCR here is an overdispersed count per 30 s "
         "epoch (SD > M) which the authors modelled with a negative-binomial GEE "
         "adjusting for baseline SCR, dissociation and alexithymia; an SMD on the "
         "raw descriptives is a crude summary of that model."),
    dict(study="Matejka 2013 (emotion-verb. vs. fact, neg)", year=2013,
         lab="Berlin", n1=23, n2=23, d=-0.502, design="within",
         derivation="extracted",
         note="Emotion verbalization vs. fact verbalization; SCR"),
]

df = pd.DataFrame(studies)


def hedges_correction(n1, n2, design="between"):
    df_eff = n1 + n2 - 2 if design == "between" else n1 - 1
    return 1 - 3 / (4 * df_eff - 1)


def se_d(d, n1, n2, design="between", r=0.5):
    if design == "between":
        return np.sqrt((n1 + n2) / (n1 * n2) + d**2 / (2 * (n1 + n2)))
    n = n1
    return np.sqrt((1 / n + d**2 / (2 * n)) * 2 * (1 - r))


df["J"] = df.apply(lambda r: hedges_correction(r.n1, r.n2, r.design), axis=1)
df["g"] = df["d"] * df["J"]
df["se_g"] = df.apply(lambda r: se_d(r.d, r.n1, r.n2, r.design) * r.J, axis=1)
df["var_g"] = df["se_g"] ** 2
df["w_fixed"] = 1 / df["var_g"]
df["ci_lo"] = df["g"] - 1.96 * df["se_g"]
df["ci_hi"] = df["g"] + 1.96 * df["se_g"]


def random_effects(g, var):
    """DerSimonian-Laird random-effects meta-analysis."""
    w_f = 1 / var
    g_f = np.sum(w_f * g) / np.sum(w_f)
    Q = np.sum(w_f * (g - g_f) ** 2)
    k = len(g)
    df_q = k - 1
    C = np.sum(w_f) - np.sum(w_f**2) / np.sum(w_f)
    tau2 = max(0, (Q - df_q) / C)
    w_r = 1 / (var + tau2)
    g_r = np.sum(w_r * g) / np.sum(w_r)
    se_r = np.sqrt(1 / np.sum(w_r))
    ci_lo = g_r - 1.96 * se_r
    ci_hi = g_r + 1.96 * se_r
    z = g_r / se_r
    p = 2 * (1 - stats.norm.cdf(abs(z)))
    I2 = max(0, (Q - df_q) / Q) * 100 if Q > 0 else 0
    H2 = Q / df_q if df_q > 0 else 1
    t_crit = stats.t.ppf(0.975, df_q - 1) if df_q > 1 else 1.96
    pi_lo = g_r - t_crit * np.sqrt(tau2 + se_r**2)
    pi_hi = g_r + t_crit * np.sqrt(tau2 + se_r**2)
    return dict(g=g_r, se=se_r, ci_lo=ci_lo, ci_hi=ci_hi, z=z, p=p,
                Q=Q, df=df_q, tau2=tau2, I2=I2, H2=H2,
                pi_lo=pi_lo, pi_hi=pi_hi, k=k)


primary = random_effects(df["g"].values, df["var_g"].values)
ucla_mask = df["lab"] == "UCLA"
ucla = random_effects(df.loc[ucla_mask, "g"].values,
                      df.loc[ucla_mask, "var_g"].values)
indep_mask = df["lab"] != "UCLA"
indep = random_effects(df.loc[indep_mask, "g"].values,
                       df.loc[indep_mask, "var_g"].values)

loo = []
for i in range(len(df)):
    mask = np.ones(len(df), dtype=bool); mask[i] = False
    res = random_effects(df.loc[mask, "g"].values,
                         df.loc[mask, "var_g"].values)
    loo.append(dict(omitted=df.iloc[i]["study"], g=res["g"],
                    ci_lo=res["ci_lo"], ci_hi=res["ci_hi"]))
loo_df = pd.DataFrame(loo)


def eggers_test(g, se):
    snd = g / se
    precision = 1 / se
    slope, intercept, r, p, _ = stats.linregress(precision, snd)
    return dict(intercept=intercept, p=p, slope=slope)


egger = eggers_test(df["g"].values, df["se_g"].values)

print("=" * 72)
print("RANDOM-EFFECTS META-ANALYSIS: AFFECT LABELING ON PERIPHERAL PHYSIOLOGY")
print("=" * 72)
print(f"\nStudies included (k = {len(df)})")
print("-" * 72)
print(df[["study", "n1", "n2", "design", "g", "se_g", "ci_lo", "ci_hi"]].round(3).to_string(index=False))

print("\n" + "=" * 72)
print("PRIMARY ANALYSIS (random-effects, DerSimonian-Laird)")
print("=" * 72)
print(f"  Pooled g       = {primary['g']:.3f}  95% CI [{primary['ci_lo']:.3f}, {primary['ci_hi']:.3f}]")
print(f"  z              = {primary['z']:.3f}, p = {primary['p']:.4f}")
print(f"  Heterogeneity  : Q({primary['df']}) = {primary['Q']:.2f}, "
      f"tau^2 = {primary['tau2']:.4f}, I^2 = {primary['I2']:.1f}%")
print(f"  95% prediction interval [{primary['pi_lo']:.3f}, {primary['pi_hi']:.3f}]")

print("\n" + "-" * 72)
print(f"SENSITIVITY: UCLA Lieberman/Craske axis only (k = {ucla['k']})")
print("-" * 72)
print(f"  Pooled g = {ucla['g']:.3f}  95% CI [{ucla['ci_lo']:.3f}, {ucla['ci_hi']:.3f}]")
print(f"  I^2 = {ucla['I2']:.1f}%, tau^2 = {ucla['tau2']:.4f}")

print("\n" + "-" * 72)
print(f"SENSITIVITY: Independent labs only (k = {indep['k']})")
print("-" * 72)
print(f"  Pooled g = {indep['g']:.3f}  95% CI [{indep['ci_lo']:.3f}, {indep['ci_hi']:.3f}]")
print(f"  I^2 = {indep['I2']:.1f}%, tau^2 = {indep['tau2']:.4f}")

print("\n" + "-" * 72)
print("EGGER'S TEST FOR SMALL-STUDY / PUBLICATION BIAS")
print("-" * 72)
print(f"  Intercept = {egger['intercept']:.3f}, p = {egger['p']:.4f}")

outdir = Path(__file__).resolve().parent
df.to_csv(outdir / "extracted_effect_sizes.csv", index=False)
loo_df.to_csv(outdir / "leave_one_out.csv", index=False)
with open(outdir / "results_summary.txt", "w", encoding="utf-8") as f:
    f.write("RANDOM-EFFECTS META-ANALYSIS - AFFECT LABELING / PHYSIOLOGY\n")
    f.write("=" * 60 + "\n\n")
    f.write(f"k = {len(df)}\n")
    f.write(f"Pooled g = {primary['g']:.3f} [95% CI {primary['ci_lo']:.3f}, {primary['ci_hi']:.3f}]\n")
    f.write(f"z = {primary['z']:.3f}, p = {primary['p']:.4f}\n")
    f.write(f"Q({primary['df']}) = {primary['Q']:.2f}, tau^2 = {primary['tau2']:.4f}, I^2 = {primary['I2']:.1f}%\n")
    f.write(f"95% prediction interval [{primary['pi_lo']:.3f}, {primary['pi_hi']:.3f}]\n\n")
    f.write(f"UCLA-only pooled g = {ucla['g']:.3f} [{ucla['ci_lo']:.3f}, {ucla['ci_hi']:.3f}], k = {ucla['k']}\n")
    f.write(f"Indep-lab pooled g = {indep['g']:.3f} [{indep['ci_lo']:.3f}, {indep['ci_hi']:.3f}], k = {indep['k']}\n")
    f.write(f"Egger's intercept = {egger['intercept']:.3f}, p = {egger['p']:.4f}\n")

# Forest plot
fig, ax = plt.subplots(figsize=(10, 6.5))
y = np.arange(len(df))[::-1]
ax.errorbar(df["g"], y,
            xerr=[df["g"] - df["ci_lo"], df["ci_hi"] - df["g"]],
            fmt="s", color="black", capsize=3, markersize=6)
ax.axvline(0, color="gray", linewidth=0.8, linestyle="--")
ax.axvline(primary["g"], color="firebrick", linewidth=1.2)
y_pool = -1
ax.plot([primary["ci_lo"], primary["g"], primary["ci_hi"], primary["g"], primary["ci_lo"]],
        [y_pool, y_pool + 0.3, y_pool, y_pool - 0.3, y_pool],
        color="firebrick", linewidth=1.4)
ax.fill([primary["ci_lo"], primary["g"], primary["ci_hi"], primary["g"]],
        [y_pool, y_pool + 0.3, y_pool, y_pool - 0.3],
        color="firebrick", alpha=0.5)
ax.set_yticks(np.concatenate([y, [y_pool]]))
labels = list(df["study"]) + [f"RE pooled (k={len(df)})"]
ax.set_yticklabels(labels, fontsize=9)
ax.set_xlabel("Hedges' g  (negative = affect labeling reduces physiological arousal)")
ax.set_title("Forest plot: affect labeling vs. control on peripheral physiology", fontsize=11)
ax.set_xlim(-2.0, 1.2)
for yi, (_, row) in zip(y, df.iterrows()):
    ax.text(1.15, yi, f"{row['g']:+.2f} [{row['ci_lo']:+.2f}, {row['ci_hi']:+.2f}]",
            va="center", fontsize=8, family="monospace")
ax.text(1.15, y_pool,
        f"{primary['g']:+.2f} [{primary['ci_lo']:+.2f}, {primary['ci_hi']:+.2f}]",
        va="center", fontsize=8, family="monospace", color="firebrick", weight="bold")
plt.tight_layout()
plt.savefig(outdir.parent / "figures" / "forest_plot.png", dpi=200, bbox_inches="tight")
plt.savefig(outdir.parent / "figures" / "forest_plot.pdf", bbox_inches="tight")
plt.close()

# Funnel plot
fig, ax = plt.subplots(figsize=(7, 6))
ax.scatter(df["g"], df["se_g"], color="black", s=40)
ax.axvline(primary["g"], color="firebrick", linestyle="--", linewidth=1)
se_max = df["se_g"].max() * 1.15
se_range = np.linspace(0, se_max, 100)
ax.plot(primary["g"] - 1.96 * se_range, se_range, color="gray", linewidth=0.8)
ax.plot(primary["g"] + 1.96 * se_range, se_range, color="gray", linewidth=0.8)
ax.invert_yaxis()
ax.set_xlabel("Hedges' g")
ax.set_ylabel("Standard error")
ax.set_title("Funnel plot")
plt.tight_layout()
plt.savefig(outdir.parent / "figures" / "funnel_plot.png", dpi=200, bbox_inches="tight")
plt.savefig(outdir.parent / "figures" / "funnel_plot.pdf", bbox_inches="tight")
plt.close()

print("\n[OK] Wrote CSVs, results summary, and forest+funnel figures.")
