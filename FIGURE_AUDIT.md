# FIGURE AUDIT

**Project Title:** Machine Learning-Based Prediction of Polycystic Ovary Syndrome (PCOS)  
**Total PNG Graphs Found:** 29 PNG files in `reports/figures/`  
**Total Figures Selected & Integrated:** 14 distinct high-value PNG files grouped into 7 multi-panel figure environments  
**Audit Date:** 2026-10-07  

---

## 1. Complete Inventory of 29 PNG Graphs

| # | Filename | Size (KB) | Category / Experiment | Inclusion Status & Reason |
|---|---|---|---|---|
| 1 | `01_class_balance.png` | 30.5 KB | EDA: Target class ratio | **INCLUDED** (Fig 1a — shows 2.06:1 control-to-case ratio) |
| 2 | `02_missingness.png` | 52.7 KB | EDA: Feature missingness | Excluded (missingness is $<1\%$ per feature, detailed in text) |
| 3 | `03_target_correlations.png` | 77.5 KB | EDA: Target correlation ranking | **INCLUDED** (Fig 1c — illustrates univariate correlation strength) |
| 4 | `04_correlation_heatmap.png` | 194.5 KB | EDA: Pairwise correlation heatmap | Excluded (41$\times$41 matrix too dense for 2-column paper layout) |
| 5 | `05_key_distributions.png` | 284.0 KB | EDA: Feature histograms | Excluded (synthesized into text summary statistics) |
| 6 | `06_symptom_prevalence.png` | 62.7 KB | EDA: Clinical symptom prevalence | Excluded (symptom impact covered in SHAP beeswarm) |
| 7 | `07_follicle_separation.png` | 103.7 KB | EDA: Follicle count separation | **INCLUDED** (Fig 1b — demonstrates primary $d=1.70$ separation) |
| 8 | `08_cv_model_comparison.png` | 74.9 KB | Results: 30-fold CV ROC-AUC | **INCLUDED** (Fig 2a — primary CV model comparison boxplot) |
| 9 | `09_feature_set_comparison.png` | 106.4 KB | Results: Feature selection ablation | **INCLUDED** (Fig 3b — feature selection strategy comparison) |
| 10 | `10_roc_curves.png` | 78.4 KB | Results: Held-out test ROC curves | **INCLUDED** (Fig 2b — held-out test ROC curves for 8 models) |
| 11 | `11_pr_curves.png` | 74.4 KB | Results: Precision-Recall curves | Excluded (ROC curves & test table cover discriminative performance) |
| 12 | `12_confusion_matrix.png` | 36.8 KB | Results: RF test confusion matrix | **INCLUDED** (Fig 2c — Random Forest test confusion matrix: 30 TP, 3 FP) |
| 13 | `13_leakage_experiment.png` | 53.6 KB | Results: Leakage inflation comparison | **INCLUDED** (Fig 3a — measures $+2.7$ pp accuracy, $+8.3$ pp F1 inflation) |
| 14 | `14_threshold_sweep.png` | 86.4 KB | Results: Decision threshold sweep | Excluded (Decision Curve Analysis provides comprehensive utility) |
| 15 | `15_paper_comparison.png` | 71.9 KB | Discussion: Literature comparison | **INCLUDED** (Fig 7 — benchmarks reported accuracies vs leak-free protocol) |
| 16 | `16_shap_global_importance.png` | 90.3 KB | SHAP: Global mean $|$SHAP$|$ bar plot | Excluded (Table 9 provides exact mean $|$SHAP$|$ numeric values) |
| 17 | `17_shap_beeswarm.png` | 150.1 KB | SHAP: Global beeswarm plot | **INCLUDED** (Fig 5a — global feature attribution beeswarm) |
| 18 | `18_shap_waterfall_no_pcos_case.png` | 116.8 KB | SHAP: Local non-PCOS waterfall | **INCLUDED** (Fig 5c — patient-level explanation for non-PCOS control) |
| 19 | `18_shap_waterfall_pcos_case.png` | 113.7 KB | SHAP: Local PCOS case waterfall | **INCLUDED** (Fig 5b — patient-level explanation for PCOS patient) |
| 20 | `19_calibration_curves.png` | 207.0 KB | Results: Probability calibration | **INCLUDED** (Fig 4a — reliability diagram for probability calibration) |
| 21 | `20_significance_boxplot.png` | 75.8 KB | Results: Pairwise statistical tests | Excluded (statistically summarized in Table 3 narrative) |
| 22 | `22_nested_cv.png` | 37.0 KB | Results: Flat vs Nested CV | Excluded (selection bias $0.0017$ reported in text) |
| 23 | `23_seed_sweep.png` | 117.1 KB | Results: 10-seed winner sweep | Excluded (4-winner distribution detailed in text) |
| 24 | `24_learning_curve.png` | 67.7 KB | Results: Training size learning curve | **INCLUDED** (Fig 4b — demonstrates performance scaling with dataset size) |
| 25 | `25_bootstrap_ci.png` | 50.5 KB | Results: Bootstrap distributions | Excluded (Table 5 provides exact 95% CIs and widths) |
| 26 | `26_decision_curve.png` | 76.8 KB | Clinical: Decision Curve Analysis | **INCLUDED** (Fig 6b — net benefit curves across 5--80% thresholds) |
| 27 | `27_cost_tiers.png` | 81.6 KB | Clinical: Feature acquisition tiers | **INCLUDED** (Fig 6a — AUC progression across 4 acquisition tiers) |
| 28 | `28_subgroup_performance.png` | 62.9 KB | Robustness: Subgroup performance | Excluded (low subgroup sample sizes noted in limitations) |
| 29 | `29_clinical_rule_baseline.png` | 127.9 KB | Clinical: Rule baseline ROC comparison | Excluded (Table 11 provides complete numerical rule comparison) |

---

## 2. Integrated Multi-Panel Figure Layout

- **Figure 1 (EDA & Separability):** `01_class_balance.png` + `07_follicle_separation.png` + `03_target_correlations.png` [Section 2]
- **Figure 2 (Model Performance & Evaluation):** `08_cv_model_comparison.png` + `10_roc_curves.png` + `12_confusion_matrix.png` [Section 4]
- **Figure 3 (Data Leakage & Feature Selection):** `13_leakage_experiment.png` + `09_feature_set_comparison.png` [Section 4]
- **Figure 4 (Probability Calibration & Scaling):** `19_calibration_curves.png` + `24_learning_curve.png` [Section 4]
- **Figure 5 (Explainable AI & Local Interpretability):** `17_shap_beeswarm.png` + `18_shap_waterfall_pcos_case.png` + `18_shap_waterfall_no_pcos_case.png` [Section 5]
- **Figure 6 (Clinical Utility & Decision Curves):** `27_cost_tiers.png` + `26_decision_curve.png` [Section 6]
- **Figure 7 (Literature Benchmark Comparison):** `15_paper_comparison.png` [Section 7]
