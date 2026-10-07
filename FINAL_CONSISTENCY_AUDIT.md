# FINAL CONSISTENCY AUDIT

**Project Title:** Machine Learning-Based Prediction of Polycystic Ovary Syndrome (PCOS)  
**Authors:** Fatema Ferdous (0152410052) · Wafa Haque (0152420023) · Khondoker Sazzad Sunfi (0152310002)  
**Department:** Department of Data Science, United International University (UIU)  
**Audit Date:** 2026-10-07  

---

## 1. Table Layout & Overlap Audit

Every table in `PCOS_ML_prediction_report.tex` was audited for width compliance ($\le \text{columnwidth}$ for single-column tables; $\le \text{textwidth}$ for double-column `table*` environments) to eliminate text overlap, clipping, or column overflow.

| Table # | Label / Description | Environment | Columns | Width Status | Overlap / Overflow? |
|---|---|---|---|---|---|
| **Table 1** | `tab:dataset` (Dataset Summary) | `table[t]` | 2 (`ll`) | Fits `\columnwidth` | **NO** (Clean) |
| **Table 2** | `tab:models` (Evaluated Models) | `table[t]` | 2 (`lp{4.2cm}`) | Fits `\columnwidth` | **NO** (Clean) |
| **Table 3** | `tab:cv_results` (CV Performance) | `table[t]` | 3 (`lcc`) | Fits `\columnwidth` | **NO** (Clean) |
| **Table 4** | `tab:test_results` (Held-Out Test Set) | `table*[t]` | 8 (`lccccccc`) | Spans `\textwidth` | **NO** (Clean) |
| **Table 5** | `tab:bootstrap` (Bootstrap 95% CIs) | `table[t]` | 4 (`lccc`) | Fits `\columnwidth` | **NO** (Clean) |
| **Table 6** | `tab:leakage` (Data Leakage Inflation) | `table[t]` | 4 (`lccc`) | Fits `\columnwidth` | **NO** (Clean) |
| **Table 7** | `tab:fsel` (Feature Selection Ablation) | `table[t]` | 5 (`lcccc`) | Fits `\columnwidth` | **NO** (Clean) |
| **Table 8** | `tab:calibration` (Calibration Metrics) | `table[t]` | 5 (`lcccc`) | Fits `\columnwidth` | **NO** (Clean) |
| **Table 9** | `tab:shap` (Top 10 SHAP Features) | `table[t]` | 3 (`lcc`) | Fits `\columnwidth` | **NO** (Clean) |
| **Table 10** | `tab:tiers` (Feature Cost Tiers) | `table[t]` | 4 (`lccc`) | Fits `\columnwidth` | **NO** (Clean) |
| **Table 11** | `tab:clinical` (ML vs Clinical Rules) | `table*[t]` | 5 (`llccc`) | Spans `\textwidth` | **NO** (Clean) |
| **Table 12** | `tab:literature` (Literature Benchmark) | `table*[t]` | 4 (`lp{3.5cm}cc`) | Spans `\textwidth` | **NO** (Clean) |

---

## 2. README vs Report Numerical Audit

A systematic metric-by-metric comparison was performed between `README.md`, `PCOS_ML_prediction_report.tex`, and the ground-truth result CSV files in `reports/results/`:

| Metric / Result | Ground Truth CSV File | Ground Truth Value | Report Value | README Value | Consistent? |
|---|---|---|---|---|---|
| Total Patients | `summary.json` | 541 | 541 | 541 | ✅ YES |
| PCOS Cases / Controls | `summary.json` | 177 / 364 | 177 / 364 | 177 / 364 | ✅ YES |
| Class Imbalance Ratio | `summary.json` | 2.06 : 1 | 2.06 : 1 | 2.06 : 1 | ✅ YES |
| Train / Test Split | `config.py`, `test_results.csv` | 432 / 109 | 432 / 109 | 432 / 109 | ✅ YES |
| Best Model (CV AUC) | `summary.json`, `cv_results.csv` | Random Forest | Random Forest | Random Forest | ✅ YES |
| Best CV ROC-AUC | `cv_results.csv` | $0.9566 \pm 0.0172$ | $0.957 \pm 0.017$ | $0.957 \pm 0.017$ | ✅ YES |
| Best CV Accuracy | `cv_results.csv` | $0.8913 \pm 0.0254$ | $0.891 \pm 0.025$ | $0.891 \pm 0.025$ | ✅ YES |
| RF Test Accuracy | `test_results.csv` | 0.9174 | 0.917 | 0.917 | ✅ YES |
| RF Test Precision | `test_results.csv` | 0.9091 | 0.909 | 0.909 | ✅ YES |
| RF Test Recall | `test_results.csv` | 0.8333 | 0.833 | 0.833 | ✅ YES |
| RF Test F1-Score | `test_results.csv` | 0.8696 | 0.870 | 0.870 | ✅ YES |
| RF Test Specificity | `test_results.csv` | 0.9589 | 0.959 | 0.959 | ✅ YES |
| RF Test ROC-AUC | `test_results.csv` | 0.9452 | 0.945 | 0.945 | ✅ YES |
| RF Bootstrap Recall CI | `bootstrap_ci.csv` | [0.703, 0.944] | [0.703, 0.944] | [0.703, 0.944] | ✅ YES |
| RF Bootstrap AUC CI | `bootstrap_ci.csv` | [0.887, 0.991] | [0.887, 0.991] | [0.887, 0.991] | ✅ YES |
| Leakage Accuracy Inflation | `leakage_experiment.csv` | +0.027 (+2.7 pp) | +2.7 pp | +2.7 pp | ✅ YES |
| Leakage F1 Inflation | `leakage_experiment.csv` | +0.083 (+8.3 pp) | +8.3 pp | +8.3 pp | ✅ YES |
| Questionnaire Tier CV AUC | `cost_tiers.csv` | 0.887 | 0.887 | 0.887 | ✅ YES |
| Blood Panel Tier Gain | `cost_tiers.csv` | +0.01046 ($+0.010^*$) | $+0.010^*$ | $+0.010$ | ✅ YES |
| Ultrasound Tier Gain | `cost_tiers.csv` | +0.062 | +0.062 | +0.062 | ✅ YES |
| Rotterdam Rule CV AUC | `clinical_rule_comparison.csv` | 0.902 | 0.902 | 0.902 | ✅ YES |
| Rotterdam Rule Test Recall | `clinical_rule_comparison.csv` | 0.611 (22/36) | 0.611 (22/36) | 0.611 (22/36) | ✅ YES |
| Stacking Calibration Brier | `calibration_metrics.csv` | 0.081 | 0.081 | 0.081 | ✅ YES |
| Gaussian NB Brier | `calibration_metrics.csv` | 0.109 | 0.109 | 0.109 | ✅ YES |

---

## 3. Final Source of Truth

The authoritative ground-truth data sources for all numerical reporting in this project are the generated master output files stored in `reports/results/`:
- `reports/results/summary.json` (Master summary metrics)
- `reports/results/cv_results.csv` (Cross-validation fold metrics)
- `reports/results/test_results.csv` (Held-out test set performance)
- `reports/results/leakage_experiment.csv` (Encapsulated vs Leaky protocol measurement)
- `reports/results/bootstrap_ci.csv` (Percentile bootstrap confidence intervals)
- `reports/results/calibration_metrics.csv` (Brier score, ECE, log loss)
- `reports/results/cost_tiers.csv` (Feature acquisition cost tier progression)
- `reports/results/feature_set_comparison.csv` (Feature selection strategy comparison)
- `reports/results/clinical_rule_comparison.csv` (ML vs clinical decision rules)

---

## 4. Final Status Confirmation
- **PDF Layout:** Clean 8-page two-column document with zero table overlap, zero text collision, and zero column overflow.
- **Consistency:** 100% numerical alignment across `README.md`, `PCOS_ML_prediction_report.tex`, and `reports/results/` ground truth CSV files.
- **Data Integrity:** No unsupported or fabricated numbers exist in the project repository.
