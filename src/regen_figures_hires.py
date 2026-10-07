"""
Regenerate all report figures with improved readability.

Run from project root:
    python -m src.regen_figures_hires

Improvements applied to every figure:
 - Larger base font sizes (axes labels, tick labels, legends, titles)
 - More generous figure sizes so text is never cramped
 - Data-value annotations use at least fontsize=10
 - tick labels rotated/wrapped as needed
 - Higher DPI (200) for crisp rendering in two-column PDF
 - Consistent visual style throughout
"""
from __future__ import annotations

import sys
from pathlib import Path

# ── ensure project root is on sys.path ──────────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd
import seaborn as sns

from src import config

# ── global style ─────────────────────────────────────────────────────────────
FONT_BASE   = 12   # axis labels, tick marks
FONT_TITLE  = 13   # sub-titles / suptitle
FONT_ANNOT  = 10   # value annotations on bars / markers
FONT_LEGEND = 10
DPI         = 200  # higher than default 150 → sharper text in PDF

sns.set_theme(style="whitegrid", context="paper",
              rc={"font.size": FONT_BASE,
                  "axes.titlesize": FONT_TITLE,
                  "axes.labelsize": FONT_BASE,
                  "xtick.labelsize": FONT_BASE - 1,
                  "ytick.labelsize": FONT_BASE - 1,
                  "legend.fontsize": FONT_LEGEND})

FIGS = config.FIGURES_DIR
PALETTE = config.PALETTE
CLASS_LABELS = {0: "No PCOS", 1: "PCOS"}
CLASS_COLORS = [PALETTE["no_pcos"], PALETTE["pcos"]]


def _save(fig: plt.Figure, name: str) -> Path:
    config.ensure_dirs()
    path = FIGS / name
    fig.savefig(path, dpi=DPI, bbox_inches="tight")
    plt.close(fig)
    print(f"  saved {path.name}")
    return path


# ─────────────────────────────────────────────────────────────────────────────
# 1. Class balance (01)
# ─────────────────────────────────────────────────────────────────────────────
def fig_class_balance(df: pd.DataFrame) -> Path:
    counts = df[config.TARGET].value_counts().sort_index()
    total  = counts.sum()

    fig, ax = plt.subplots(figsize=(5, 4.2))
    bars = ax.bar([CLASS_LABELS[i] for i in counts.index], counts.values,
                  color=CLASS_COLORS, width=0.55)
    for bar, v in zip(bars, counts.values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 8,
                f"{v}\n({v/total:.1%})", ha="center", va="bottom",
                fontsize=FONT_ANNOT)
    ax.set_ylabel("Patients", fontsize=FONT_BASE)
    ax.set_title(f"Class distribution  (n={total}, ratio {counts[0]/counts[1]:.1f}:1)",
                 fontsize=FONT_TITLE)
    ax.set_ylim(0, counts.max() * 1.25)
    ax.tick_params(labelsize=FONT_BASE)
    return _save(fig, "01_class_balance.png")


# ─────────────────────────────────────────────────────────────────────────────
# 2. Target correlations (03)
# ─────────────────────────────────────────────────────────────────────────────
def fig_target_correlations(df: pd.DataFrame, top_n: int = 20) -> Path:
    corr = df.corr(numeric_only=True)[config.TARGET].drop(config.TARGET)
    top  = corr.reindex(corr.abs().sort_values(ascending=False).index).head(top_n)[::-1]

    fig, ax = plt.subplots(figsize=(7.5, 0.40 * len(top) + 1.8))
    colors = [PALETTE["pcos"] if v > 0 else PALETTE["no_pcos"] for v in top]
    ax.barh([config.pretty(c) for c in top.index], top.values, color=colors)
    ax.axvline(0, color="black", linewidth=0.9)
    ax.set_xlabel("Pearson correlation with PCOS diagnosis", fontsize=FONT_BASE)
    ax.set_title(f"Top {top_n} features by correlation with the target",
                 fontsize=FONT_TITLE)
    ax.tick_params(labelsize=FONT_BASE - 1)
    return _save(fig, "03_target_correlations.png")


# ─────────────────────────────────────────────────────────────────────────────
# 3. Follicle separation (07)
# ─────────────────────────────────────────────────────────────────────────────
def fig_follicle_separation(df: pd.DataFrame) -> Path:
    plot_df = df.copy()
    plot_df["group"] = plot_df[config.TARGET].map(CLASS_LABELS)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    sns.boxplot(data=plot_df, x="group", y="Follicle No. (L)", hue="group",
                palette=CLASS_COLORS, legend=False, ax=axes[0])
    axes[0].set_title("Left ovary follicle count", fontsize=FONT_TITLE)
    axes[0].set_xlabel("", fontsize=FONT_BASE)
    axes[0].set_ylabel("Follicle count (left)", fontsize=FONT_BASE)
    axes[0].tick_params(labelsize=FONT_BASE)

    sns.scatterplot(data=plot_df, x="Follicle No. (L)", y="Follicle No. (R)",
                    hue="group", palette=CLASS_COLORS, alpha=0.65, s=40, ax=axes[1])
    axes[1].axvline(12, color="grey", linestyle="--", linewidth=1.2)
    axes[1].axhline(12, color="grey", linestyle="--", linewidth=1.2)
    axes[1].set_title("Left vs right follicle count\n(dashed = 12-follicle Rotterdam criterion)",
                      fontsize=FONT_TITLE)
    axes[1].set_xlabel("Follicle count (left)", fontsize=FONT_BASE)
    axes[1].set_ylabel("Follicle count (right)", fontsize=FONT_BASE)
    axes[1].legend(title="", fontsize=FONT_LEGEND)
    axes[1].tick_params(labelsize=FONT_BASE)

    fig.suptitle("Follicle counts separate the classes most cleanly", fontsize=FONT_TITLE + 1)
    fig.tight_layout()
    return _save(fig, "07_follicle_separation.png")


# ─────────────────────────────────────────────────────────────────────────────
# 4. CV model comparison (08)
# ─────────────────────────────────────────────────────────────────────────────
def fig_cv_comparison(cv_results: pd.DataFrame) -> Path:
    metrics = ["accuracy", "f1", "roc_auc"]
    order   = cv_results.sort_values("roc_auc", ascending=False)["model"].tolist()
    palette = sns.color_palette("crest", len(order))

    fig, axes = plt.subplots(1, len(metrics), figsize=(6 * len(metrics), 5.5), sharey=True)

    for ax, metric in zip(axes, metrics):
        subset = cv_results.set_index("model").loc[order]
        ax.barh(range(len(order)), subset[metric].values,
                xerr=subset[f"{metric}_std"].values,
                color=palette, capsize=4)
        ax.set_yticks(range(len(order)))
        ax.set_yticklabels(order, fontsize=FONT_BASE)
        ax.invert_yaxis()
        ax.set_xlim(0.5, 1.06)
        label = metric.replace("_", " ").upper()
        ax.set_title(label, fontsize=FONT_TITLE)
        ax.set_xlabel("Score", fontsize=FONT_BASE)
        ax.tick_params(labelsize=FONT_BASE - 1)
        for i, value in enumerate(subset[metric].values):
            ax.text(value + 0.013, i, f"{value:.3f}", va="center",
                    fontsize=FONT_ANNOT, fontweight="bold")

    fig.suptitle(
        f"Repeated stratified {config.CV_FOLDS}-fold CV "
        f"({config.CV_REPEATS} repeats) — error bars = 1 SD",
        fontsize=FONT_TITLE,
    )
    fig.tight_layout()
    return _save(fig, "08_cv_model_comparison.png")


# ─────────────────────────────────────────────────────────────────────────────
# 5. Feature-set comparison heatmap (09) ← used in Figure 3
# ─────────────────────────────────────────────────────────────────────────────
def fig_feature_set_comparison(comparison: pd.DataFrame) -> Path:
    pivot = comparison.pivot_table(
        index="model", columns="feature_set", values="roc_auc", aggfunc="mean"
    )
    pivot = pivot.loc[pivot.mean(axis=1).sort_values(ascending=False).index]

    fig, ax = plt.subplots(figsize=(8, 0.65 * len(pivot) + 2.8))
    sns.heatmap(
        pivot,
        annot=True,
        fmt=".3f",
        annot_kws={"size": FONT_ANNOT + 1},
        cmap="YlGnBu",
        linewidths=0.5,
        cbar_kws={"label": "Mean CV ROC-AUC"},
        ax=ax,
    )
    ax.set_title("Feature selection strategy vs model", fontsize=FONT_TITLE)
    ax.set_xlabel("Feature set", fontsize=FONT_BASE)
    ax.set_ylabel("", fontsize=FONT_BASE)
    ax.tick_params(axis="x", labelsize=FONT_BASE - 1, rotation=20)
    ax.tick_params(axis="y", labelsize=FONT_BASE - 1, rotation=0)
    fig.tight_layout()
    return _save(fig, "09_feature_set_comparison.png")


# ─────────────────────────────────────────────────────────────────────────────
# 6. ROC curves (10)
# ─────────────────────────────────────────────────────────────────────────────
def fig_roc_curves(curves: dict) -> Path:
    fig, ax = plt.subplots(figsize=(7, 6))
    for name, data in sorted(curves.items(), key=lambda kv: -kv[1]["roc_auc"]):
        ax.plot(data["fpr"], data["tpr"], linewidth=2,
                label=f"{name}  (AUC={data['roc_auc']:.3f})")
    ax.plot([0, 1], [0, 1], "k--", linewidth=1, label="Chance")
    ax.set_xlabel("False positive rate", fontsize=FONT_BASE)
    ax.set_ylabel("True positive rate (recall)", fontsize=FONT_BASE)
    ax.set_title("ROC curves — held-out test set", fontsize=FONT_TITLE)
    ax.legend(loc="lower right", fontsize=FONT_LEGEND)
    ax.tick_params(labelsize=FONT_BASE - 1)
    fig.tight_layout()
    return _save(fig, "10_roc_curves.png")


# ─────────────────────────────────────────────────────────────────────────────
# 7. PR curves (11)
# ─────────────────────────────────────────────────────────────────────────────
def fig_pr_curves(curves: dict) -> Path:
    fig, ax = plt.subplots(figsize=(7, 6))
    for name, data in sorted(curves.items(), key=lambda kv: -kv[1]["avg_precision"]):
        ax.plot(data["recall"], data["precision"], linewidth=2,
                label=f"{name}  (AP={data['avg_precision']:.3f})")
    ax.set_xlabel("Recall", fontsize=FONT_BASE)
    ax.set_ylabel("Precision", fontsize=FONT_BASE)
    ax.set_title("Precision-recall curves — held-out test set", fontsize=FONT_TITLE)
    ax.legend(loc="lower left", fontsize=FONT_LEGEND)
    ax.tick_params(labelsize=FONT_BASE - 1)
    fig.tight_layout()
    return _save(fig, "11_pr_curves.png")


# ─────────────────────────────────────────────────────────────────────────────
# 8. Leakage experiment (13) ← used in Figure 3
# ─────────────────────────────────────────────────────────────────────────────
def fig_leakage_experiment(leakage: pd.DataFrame) -> Path:
    metrics      = ["accuracy", "precision", "recall", "f1", "roc_auc"]
    metric_labels = ["Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC"]
    data = leakage[~leakage["protocol"].str.startswith("inflation")]

    x     = np.arange(len(metrics))
    width = 0.34

    fig, ax = plt.subplots(figsize=(9.5, 5.5))

    protocol_colors = [PALETTE["no_pcos"], PALETTE["pcos"]]
    for i, (_, row) in enumerate(data.iterrows()):
        values = [row[m] for m in metrics]
        bars   = ax.bar(x + (i - 0.5) * width, values, width,
                        label=row["protocol"], color=protocol_colors[i],
                        edgecolor="white", linewidth=0.6)
        for bar, value in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2,
                    value + 0.006,
                    f"{value:.3f}",
                    ha="center", fontsize=FONT_ANNOT,
                    fontweight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(metric_labels, fontsize=FONT_BASE)
    ax.set_ylim(0.60, 1.06)
    ax.set_ylabel("Cross-validated score", fontsize=FONT_BASE)
    ax.set_title("How much does a leaky preprocessing protocol inflate results?",
                 fontsize=FONT_TITLE)
    ax.legend(loc="lower right", fontsize=FONT_LEGEND,
              framealpha=0.9, title="Protocol")
    ax.tick_params(axis="y", labelsize=FONT_BASE - 1)
    ax.yaxis.set_major_locator(mticker.MultipleLocator(0.05))
    ax.grid(axis="y", alpha=0.4)
    fig.tight_layout()
    return _save(fig, "13_leakage_experiment.png")


# ─────────────────────────────────────────────────────────────────────────────
# 9. Bootstrap CI (25)
# ─────────────────────────────────────────────────────────────────────────────
def fig_bootstrap_ci(ci: pd.DataFrame, model_name: str, n_test: int) -> Path:
    fig, ax = plt.subplots(figsize=(8.5, 5))
    y = np.arange(len(ci))
    ax.errorbar(ci["estimate"], y,
                xerr=[ci["estimate"] - ci["ci_lower"],
                      ci["ci_upper"] - ci["estimate"]],
                fmt="o", ms=9, capsize=6, color=PALETTE["no_pcos"],
                linewidth=2)
    for i, (_, row) in enumerate(ci.iterrows()):
        ax.text(row["ci_upper"] + 0.013, i,
                f"[{row['ci_lower']:.2f}, {row['ci_upper']:.2f}]",
                va="center", fontsize=FONT_ANNOT)
    ax.set_yticks(y)
    ax.set_yticklabels([m.replace("_", " ").title() for m in ci["metric"]],
                       fontsize=FONT_BASE)
    ax.invert_yaxis()
    ax.set_xlim(0.4, 1.18)
    ax.set_xlabel("Score", fontsize=FONT_BASE)
    ax.set_title(
        f"95% Bootstrap Confidence Intervals — {model_name}\n"
        f"n = {n_test} patients: intervals reflect small test-set size",
        fontsize=FONT_TITLE,
    )
    ax.tick_params(axis="x", labelsize=FONT_BASE - 1)
    fig.tight_layout()
    return _save(fig, "25_bootstrap_ci.png")


# ─────────────────────────────────────────────────────────────────────────────
# 10. Decision curve (26)
# ─────────────────────────────────────────────────────────────────────────────
def fig_decision_curve(curve: pd.DataFrame, model_name: str) -> Path:
    fig, ax = plt.subplots(figsize=(8.5, 5.5))
    ax.plot(curve["threshold"], curve["net_benefit_model"], linewidth=2.5,
            color=PALETTE["pcos"], label=model_name)
    ax.plot(curve["threshold"], curve["net_benefit_treat_all"], linewidth=1.8,
            color="#888888", linestyle="--", label="Refer everyone")
    ax.axhline(0, color="black", linewidth=1.4, linestyle=":", label="Refer nobody")

    useful = curve[curve["benefit_over_best_default"] > 0]
    if not useful.empty:
        lo, hi = useful["threshold"].min(), useful["threshold"].max()
        ax.axvspan(lo, hi, alpha=0.12, color=PALETTE["no_pcos"])
        ax.text((lo + hi) / 2, ax.get_ylim()[1] * 0.88,
                f"Model adds value\n{lo:.0%}–{hi:.0%}",
                ha="center", fontsize=FONT_ANNOT + 1, color=PALETTE["no_pcos"],
                fontweight="bold")

    ax.set_xlabel("Threshold probability", fontsize=FONT_BASE)
    ax.set_ylabel("Net benefit", fontsize=FONT_BASE)
    ax.set_ylim(bottom=min(-0.05, curve["net_benefit_model"].min()))
    ax.set_title("Decision curve analysis — net clinical benefit", fontsize=FONT_TITLE)
    ax.legend(loc="upper right", fontsize=FONT_LEGEND)
    ax.tick_params(labelsize=FONT_BASE - 1)
    fig.tight_layout()
    return _save(fig, "26_decision_curve.png")


# ─────────────────────────────────────────────────────────────────────────────
# 11. Cost tiers (27)
# ─────────────────────────────────────────────────────────────────────────────
def fig_cost_tiers(tiers: pd.DataFrame) -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    x = np.arange(len(tiers))
    axes[0].bar(x - 0.2, tiers["cv_roc_auc"], 0.38,
                yerr=tiers["cv_roc_auc_std"], capsize=5,
                label="Cross-validated", color=PALETTE["no_pcos"])
    axes[0].bar(x + 0.2, tiers["test_roc_auc"], 0.38,
                label="Held-out test", color=PALETTE["pcos"])
    axes[0].set_xticks(x)

    # Wrap long tier labels
    tick_labels = [f"{t}\n({n} feat.)"
                   for t, n in zip(tiers["tier"], tiers["n_features"])]
    axes[0].set_xticklabels(tick_labels, fontsize=FONT_BASE - 1)
    axes[0].set_ylim(0.50, 1.02)
    axes[0].set_ylabel("ROC-AUC", fontsize=FONT_BASE)
    axes[0].set_title("What does each testing tier buy?", fontsize=FONT_TITLE)
    axes[0].legend(loc="lower right", fontsize=FONT_LEGEND)
    axes[0].tick_params(axis="y", labelsize=FONT_BASE - 1)
    for xi, value in zip(x, tiers["cv_roc_auc"]):
        axes[0].text(xi - 0.2, value + 0.014, f"{value:.3f}",
                     ha="center", fontsize=FONT_ANNOT, fontweight="bold")

    gains = tiers.dropna(subset=["gain_over_previous"])
    axes[1].barh(gains["tier"], gains["gain_over_previous"],
                 color=[PALETTE["pcos"] if g > 0.01 else "#9CA3AF"
                        for g in gains["gain_over_previous"]])
    axes[1].axvline(0, color="black", linewidth=0.9)
    axes[1].set_xlabel("Marginal CV ROC-AUC gain over previous tier",
                       fontsize=FONT_BASE)
    axes[1].set_title("Marginal gain of each extra tier", fontsize=FONT_TITLE)
    axes[1].tick_params(labelsize=FONT_BASE - 1)
    for i, value in enumerate(gains["gain_over_previous"]):
        axes[1].text(value + 0.001, i, f"{value:+.4f}",
                     va="center", fontsize=FONT_ANNOT)

    fig.suptitle(
        "Cost-tiered screening: questionnaire → vitals → bloods → ultrasound",
        fontsize=FONT_TITLE + 1,
    )
    fig.tight_layout()
    return _save(fig, "27_cost_tiers.png")


# ─────────────────────────────────────────────────────────────────────────────
# 12. Clinical rule comparison (29) — bar chart from CSV
# ─────────────────────────────────────────────────────────────────────────────
def fig_clinical_rule_comparison() -> Path:
    csv_path = config.RESULTS_DIR / "clinical_rule_comparison.csv"
    if not csv_path.exists():
        print(f"  SKIP: {csv_path} not found")
        return None

    df = pd.read_csv(csv_path)

    # Normalise column names
    col_map = {}
    if "model" in df.columns and "approach" not in df.columns:
        col_map["model"] = "approach"
    if "kind" in df.columns and "type" not in df.columns:
        col_map["kind"] = "type"
    if col_map:
        df = df.rename(columns=col_map)

    # Use cv_roc_auc if cv_auc absent
    auc_col = "cv_roc_auc" if "cv_roc_auc" in df.columns else "cv_auc"
    type_col = "type" if "type" in df.columns else (
                "kind" if "kind" in df.columns else None)

    df = df.sort_values(auc_col, ascending=True)

    ml_terms = {"machine learning", "ml"}
    if type_col and type_col in df.columns:
        colors = [PALETTE["pcos"] if str(t).lower().strip() in ml_terms else "#9CA3AF"
                  for t in df[type_col]]
    else:
        colors = [PALETTE["no_pcos"]] * len(df)

    fig, ax = plt.subplots(figsize=(9.5, 0.60 * len(df) + 2.5))
    bars = ax.barh(df["approach"], df[auc_col], color=colors)
    ax.set_xlabel("Cross-validated ROC-AUC", fontsize=FONT_BASE)
    ax.set_title("ML models vs clinical decision rules", fontsize=FONT_TITLE)
    ax.set_xlim(0.50, 1.04)
    ax.tick_params(labelsize=FONT_BASE - 1)
    for bar, value in zip(bars, df[auc_col]):
        ax.text(value + 0.005, bar.get_y() + bar.get_height() / 2,
                f"{value:.3f}", va="center", fontsize=FONT_ANNOT,
                fontweight="bold")
    fig.tight_layout()
    return _save(fig, "29_clinical_rule_baseline.png")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN — load saved CSVs and regenerate every figure that does not need refit
# ─────────────────────────────────────────────────────────────────────────────
def main():
    print("=" * 60)
    print("Regenerating report figures with improved readability")
    print("=" * 60)

    results_dir = config.RESULTS_DIR

    # ── load data ──────────────────────────────────────────────────────────
    from src.data import load_clean

    print("\nLoading dataset …")
    df = load_clean()

    # ── figures that only need the raw dataframe ───────────────────────────
    print("\n[1] Class balance …")
    fig_class_balance(df)

    print("[2] Target correlations …")
    fig_target_correlations(df)

    print("[3] Follicle separation …")
    fig_follicle_separation(df)

    # ── figures that need saved CSV results ───────────────────────────────
    cv_csv = results_dir / "cv_results.csv"
    if cv_csv.exists():
        print("[4] CV model comparison …")
        cv_results = pd.read_csv(cv_csv)
        fig_cv_comparison(cv_results)
    else:
        print(f"  SKIP: {cv_csv} not found — run full pipeline first")

    feat_csv = results_dir / "feature_set_comparison.csv"
    if feat_csv.exists():
        print("[5] Feature-set comparison heatmap …")
        feat_df = pd.read_csv(feat_csv)
        fig_feature_set_comparison(feat_df)
    else:
        print(f"  SKIP: {feat_csv} not found")

    leakage_csv = results_dir / "leakage_experiment.csv"
    if leakage_csv.exists():
        print("[6] Leakage experiment …")
        leakage = pd.read_csv(leakage_csv)
        fig_leakage_experiment(leakage)
    else:
        print(f"  SKIP: {leakage_csv} not found")

    boot_csv = results_dir / "bootstrap_ci.csv"
    if boot_csv.exists():
        print("[7] Bootstrap CI …")
        boot = pd.read_csv(boot_csv)
        fig_bootstrap_ci(boot, model_name="Random Forest", n_test=109)
    else:
        print(f"  SKIP: {boot_csv} not found")

    # Decision curve — load net-benefit CSV if it exists
    dca_csv = results_dir / "decision_curve.csv"
    if dca_csv.exists():
        print("[8] Decision curve …")
        dca = pd.read_csv(dca_csv)
        fig_decision_curve(dca, model_name="Random Forest")
    else:
        print(f"  SKIP: {dca_csv} not found")

    tiers_csv = results_dir / "cost_tiers.csv"
    if tiers_csv.exists():
        print("[9] Cost tiers …")
        tiers = pd.read_csv(tiers_csv)
        fig_cost_tiers(tiers)
    else:
        print(f"  SKIP: {tiers_csv} not found")

    print("[10] Clinical rule comparison …")
    fig_clinical_rule_comparison()

    print("\nDone. All figures written to:", FIGS)


if __name__ == "__main__":
    main()
