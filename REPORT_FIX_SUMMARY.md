# REPORT FIX SUMMARY
**Project:** Machine Learning-Based Prediction of Polycystic Ovary Syndrome (PCOS)  
**Group 5:** Fatema Ferdous (0152410052) · Wafa Haque (0152420023) · Khondoker Sazzad Sunfi (0152310002)  
**Audit Date:** 2026-10-07

---

## 1. PROBLEMS FOUND IN THE ORIGINAL REPORT

### Critical Errors
| # | Problem | Location | Evidence |
|---|---|---|---|
| 1 | **Wrong best model** — old report stated "Stacking Ensemble" as best model with CV AUC 0.956 ± 0.028 | Abstract, Results | `summary.json`: `"best_model": "Random Forest"`, `"cv_roc_auc": 0.9566`. `cv_results.csv`: RF 0.9566 > Stacking 0.9508 |
| 2 | **Wrong CV AUC std** — old report said ± 0.028 for Stacking | Table 1 | `cv_results.csv`: Stacking std = 0.0205, RF std = 0.0172 |
| 3 | **Inflated leakage numbers** — old report claimed "+3.2 points accuracy, +9.0 F1" | Section 4.3 | `leakage_experiment.csv`: actual inflation = +0.027 accuracy (2.7 pp), +0.083 F1 (8.3 pp). +9.0 applies to F1 is approximately correct but the accuracy figure was overstated as 3.2 vs actual 2.7 |
| 4 | **Wrong false alarm count** — old report said "2 false alarms" for ML | Clinical comparison | `value_added_by_ml.json`: RF has 3 false positives (FP=3), Rotterdam has 1. Extra = 2 (net), but absolute ML FP = 3 |
| 5 | **No CatBoost in test results** — CatBoost was listed in old report's Table 1 but not in `test_results.csv` | Table 1 | `test_results.csv` contains only 8 models (no CatBoost row) |
| 6 | **Incorrect leakage recall figure** — old report stated "+9.8 recall" | Abstract | `leakage_experiment.csv`: inflation recall = +0.0977 (9.77 pp ≈ 9.8 is fine; F1 = 8.3 pp, not 9.0) |
| 7 | **Missing title page** — old report had no dedicated title page with student IDs and emails | Title | User requirement |
| 8 | **`\uppercase` in titlesec** — caused `\@icentercr` Overleaf error | LaTeX | Stack trace from user |
| 9 | **Wrong bibliography format** — used `enumerate` list instead of `\bibitem` | References | Caused `[?]` undefined citation errors |
| 10 | **Seed sweep "8 of 9 won"** — old report used README figure; actual CSV shows 4 of 8 won | Section 4.2 | `seed_sweep_wins.csv`: Gaussian NB 40%, RF 30%, Stacking 20%, Elastic-Net 10%; others = 0 |
| 11 | **Missing calibration discussion** — "Stacking best calibrated" was stated without Brier/ECE values in text | Results | `calibration_metrics.csv` has full table |
| 12 | **Missing subsections** — no EDA section, no Clinical Utility section, no Ethical section, no Future Work | Structure | User requirement, proposal |
| 13 | **Wrong feature count in correlation set** — stated "20 features" but listed only partial names | Methods | `selected_features.json`: exactly 20 features for correlation selector |
| 14 | **Figures after References** — many figures were displaced to after the reference list | LaTeX float | `stfloats` not configured, `\dbltopfraction` not set |

---

## 2. CORRECTIONS MADE

### Numerical Corrections
| Metric | Old Value | New (Verified) Value | Source |
|---|---|---|---|
| Best model (CV) | Stacking Ensemble | **Random Forest** | `summary.json`, `cv_results.csv`, `significance_tests.csv` |
| RF CV ROC-AUC | 0.956 ± 0.028 | **0.957 ± 0.017** | `cv_results.csv` |
| Stacking CV ROC-AUC | 0.956 ± 0.028 | **0.951 ± 0.020** | `cv_results.csv` |
| Leakage accuracy inflation | +3.2 pp | **+2.7 pp** | `leakage_experiment.csv` |
| Leakage F1 inflation | +9.0 pp | **+8.3 pp (≈ 9.0 was slightly overstated)** | `leakage_experiment.csv` |
| Leakage recall inflation | +9.8 pp | **+9.8 pp ✓** | `leakage_experiment.csv` |
| RF test accuracy | 0.927 | **0.917** | `test_results.csv` |
| Stacking test accuracy | 0.927 | **0.927 ✓** | `test_results.csv` |
| Stacking recall | 0.833 ✓ | **0.833 ✓** | `test_results.csv` |
| Stacking specificity | 0.973 ✓ | **0.973 ✓** | `test_results.csv` |
| Bootstrap CI (recall) | [0.703, 0.944] | **[0.703, 0.944] ✓** | `bootstrap_ci.csv` |
| Bootstrap CI (AUC) | [0.886, 0.989] | **[0.887, 0.991]** | `bootstrap_ci.csv` |
| Questionnaire AUC | 0.887 ✓ | **0.887 ✓** | `cost_tiers.csv` |
| Rotterdam rule CV AUC | 0.903 | **0.902** | `clinical_rule_comparison.csv` |
| Rotterdam rule % of ML AUC | 94.8% | **94.3%** | `value_added_by_ml.json` |
| SHAP #1 feature | Follicle count R (0.128) ✓ | **0.128 ✓** | `shap_importance.csv` |
| Calibration best (Brier) | Stacking 0.081 ✓ | **0.0807 ✓** | `calibration_metrics.csv` |
| Calibration worst (Brier) | Gaussian NB 0.109 ✓ | **0.1090 ✓** | `calibration_metrics.csv` |
| Nested CV optimism | 0.0017 ✓ | **0.0017 ✓** | `nested_cv.json` |
| AutoML AUC gain | +0.0004 ✓ | **+0.0004 ✓** | `automl_comparison.csv` |
| Seed sweep distinct winners | "8 of 9" (README) | **4 of 8 (from CSV)** | `seed_sweep_wins.csv` |
| Blood panel AUC gain | +0.011 ✓ | **+0.011 ✓** | `cost_tiers.csv` |
| Ultrasound AUC gain | +0.062 ✓ | **+0.062 ✓** | `cost_tiers.csv` |

### LaTeX Fixes
- Removed `\uppercase` from `\titleformat` (caused `\@icentercr` error)
- Replaced `enumerate` bibliography with standard `\thebibliography` + `\bibitem`
- All `\cite{}` keys now match corresponding `\bibitem{...}` entries
- Added `\stfloats` + proper `\dbltopfraction`, `\dblfloatpagefraction` settings
- Replaced `\\[0.35em]` with `\par` + `\vspace{}` in `\twocolumn[...]` header
- Added `lmodern` + `microtype` for professional typography
- Used `tabularx` for responsive table widths

---

## 3. NEW SECTIONS ADDED

| Section | Description |
|---|---|
| **Dedicated Title Page** | One-column professional title page with UIU branding, author table, student IDs, clickable emails, and headline metrics summary box |
| **Section 3: Exploratory Data Analysis** | Standalone EDA section with Cohen's d table for top discriminating features, follicle analysis discussion, 3 EDA figures |
| **Section 7: Clinical Utility Analysis** | Full section covering feature cost tiers, clinical rule comparison (5 rules), decision curve analysis, and subgroup analysis |
| **Section 9: Limitations** | 8-item detailed limitation list including predictor-label circularity, unblinded assessment, hospital sampling bias, no external validation |
| **Section 10: Ethical and Clinical Considerations** | Dedicated ethical section: non-substitution principle, external validation requirement, equity, data protection, uncertainty communication |
| **Section 12: Future Work** | 6-item realistic future work section |
| **Table 2: Cohen's d** | Top-10 discriminating features from `summary_statistics.csv` |
| **Table 4: Significance Tests** | Pairwise statistical vs. practical separability from `significance_tests.csv` |
| **Table 5 (full)**: Test results | Expanded to 8 columns including average precision, all models |
| **Table 6: Feature selection** | Comparison of all 4 feature set strategies from `feature_set_comparison.csv` |
| **Table 7: Class imbalance ablation** | 3-strategy comparison from `imbalance_ablation.csv` |
| **Table 8: Calibration** | Full Brier/log-loss/ECE/AUC from `calibration_metrics.csv` |
| **Table 9: Clinical rules** | 8-row comparison of ML vs. clinical rules from `clinical_rule_comparison.csv` |
| **Table 10: Literature** | 6-row comparison with prior papers from `literature_comparison.csv` |

---

## 4. REMOVED / REWRITTEN CONTENT

| Item | Action | Reason |
|---|---|---|
| Textbook ML formula dump (Stacking formula) | **Removed** | Not implemented as described; stacking parameters are documented via code reference |
| "100% accurate", "perfect" language | **Replaced** | Academically inappropriate |
| "Diagnoses PCOS" phrasing | **Replaced** with "screening and prediction" | Model is not a diagnostic device |
| Generic reference list without DOIs | **Replaced** | Full IEEE-style references with DOIs from README |
| CatBoost row in Table 1 (not in test_results.csv) | **Moved** to CV-only note | CatBoost not in held-out test results CSV |
| "8 of 9 models won" | **Corrected** to "4 of 8" | `seed_sweep_wins.csv` is the ground truth |
| Old inline-style references `[1], [2]` | **Replaced** with `\cite{}` | Proper LaTeX citation system |
| Blank first-page space | **Fixed** | `\twocolumn[...]` structure with proper float settings |

---

## 5. VERIFIED FINAL METRICS

All values below are directly traceable to project output files.

| Metric | Value | Source File |
|---|---|---|
| Dataset size | 541 patients | `summary.json` |
| PCOS positive | 177 (32.7%) | `summary.json` |
| Non-PCOS | 364 (67.3%) | `summary.json` |
| Features after cleaning | 41 | `summary.json` |
| Train size | 432 | config.py (80%) |
| Test size | 109 (73 neg, 36 pos) | `test_results.csv` |
| CV folds × repeats | 10 × 3 | `config.py` |
| Random seed | 42 | `config.py` |
| Best model (CV AUC) | Random Forest | `summary.json`, `significance_tests.csv` |
| RF CV ROC-AUC | 0.957 ± 0.017 | `cv_results.csv` |
| RF CV Accuracy | 0.891 ± 0.025 | `cv_results.csv` |
| RF Test Accuracy | 0.917 | `test_results.csv` |
| RF Test Precision | 0.909 | `test_results.csv` |
| RF Test Recall | 0.833 | `test_results.csv` |
| RF Test F1 | 0.870 | `test_results.csv` |
| RF Test Specificity | 0.959 | `test_results.csv` |
| RF Test ROC-AUC | 0.945 | `test_results.csv` |
| Bootstrap CI (AUC) | [0.887, 0.991] | `bootstrap_ci.csv` |
| Bootstrap CI (Recall) | [0.703, 0.944] | `bootstrap_ci.csv` |
| Correlation features selected | 20 | `selected_features.json` |
| Leakage accuracy inflation | +0.027 (2.7 pp) | `leakage_experiment.csv` |
| Leakage F1 inflation | +0.083 (8.3 pp) | `leakage_experiment.csv` |
| SHAP #1 feature | Follicle count R (0.128) | `shap_importance.csv` |
| Stacking Brier score | 0.081 | `calibration_metrics.csv` |
| Stacking ECE | 0.032 | `calibration_metrics.csv` |
| Gaussian NB ECE | 0.100 (worst) | `calibration_metrics.csv` |
| Rotterdam rule CV AUC | 0.902 | `clinical_rule_comparison.csv` |
| Rotterdam rule test recall | 0.611 (22/36) | `clinical_rule_comparison.csv` |
| ML test recall | 0.833 (30/36) | `test_results.csv` |
| Extra cases by ML | 8 | `value_added_by_ml.json` |
| Extra false alarms (net) | 2 | `value_added_by_ml.json` |
| Questionnaire CV AUC | 0.887 | `cost_tiers.csv` |
| Questionnaire % of full | 93% | `summary.json` |
| Blood panel marginal gain | +0.011 AUC | `cost_tiers.csv` |
| Ultrasound marginal gain | +0.062 AUC | `cost_tiers.csv` |
| Nested CV optimism | 0.0017 AUC | `nested_cv.json` |
| AutoML AUC gain | +0.0004 | `automl_comparison.csv` |
| Learning curve slope | +0.0003 AUC/100 patients | `summary.json` |
| Distinct seed-sweep winners | 4 of 8 models | `seed_sweep_wins.csv` |

---

## 6. REMAINING ISSUES (Require Manual Verification)

| Item | Status | Note |
|---|---|---|
| CatBoost test results | ⚠️ Not in `test_results.csv` | CatBoost may have failed to import at pipeline runtime; CV results include it if available |
| Reference for Paper 4 (anonymous 2024) | ⚠️ No DOI/author | Exact publication not identifiable from project files |
| `Cycle length(days)` semantics | ⚠️ Ambiguous | Median=5, range 2–12; likely bleeding duration not cycle interval; Kaggle docs silent |
| External validation AUC | ⚠️ Not included | Only 8 features shared with Tunisian cohort; restricted model (~0.65 AUC); kept out of report as per project README guidance |
| Subgroup analysis (small n) | ⚠️ Low power | Age <25 (n=9) and BMI Underweight (n=7) marked unreliable; not reported in main text |
| Isotonic calibration result | ✅ Reported as negative | Brier -0.0009, log loss +0.150, ECE +0.010 — documented in calibration discussion |

---

## 7. FILES MODIFIED

| File | Action |
|---|---|
| `PCOS_ML_prediction_report.tex` | Complete rewrite — publication-grade, verified numbers |
| `reports/PCOS_ML_prediction_report.tex` | Synced copy |
| `REPORT_FIX_SUMMARY.md` | Created — this file |
| `C:\Users\User\Desktop\overleaf_upload.zip` | Rebuilt with updated .tex + all 29 figures |

---

*Audit performed by inspecting: `summary.json`, `test_results.csv`, `cv_results.csv`, `leakage_experiment.csv`, `shap_importance.csv`, `calibration_metrics.csv`, `bootstrap_ci.csv`, `nested_cv.json`, `clinical_rule_comparison.csv`, `value_added_by_ml.json`, `cost_tiers.csv`, `feature_set_comparison.csv`, `imbalance_ablation.csv`, `seed_sweep_wins.csv`, `automl_comparison.csv`, `literature_comparison.csv`, `significance_tests.csv`, `summary_statistics.csv`, `selected_features.json`, `data_quality_report.csv`, `src/config.py`, `src/data.py`, `src/models.py`, `src/features.py`, `README.md`.*
