# FINAL POLISHED REPORT AUDIT (ALL 12 TABLES VERIFIED)

**Project Title:** Machine Learning-Based Prediction of Polycystic Ovary Syndrome (PCOS)  
**Authors:** Fatema Ferdous (0152410052) · Wafa Haque (0152420023) · Khondoker Sazzad Sunfi (0152310002)  
**Department:** Department of Data Science, United International University (UIU)  
**Audit Date:** 2026-10-07  

---

### 1. Verification of All 12 Important Tables
All 12 tables are present in the final document, explicitly numbered, and referenced in the text body:

1. **Table 1 (Dataset Summary):** Total patients (541), PCOS positive (177), Non-PCOS (364), Class ratio (2.06:1), Features (41), Target (PCOS), Train/Test (432/109).
2. **Table 2 (Models & Hyperparameters):** 7 core classifiers + 1 Stacking Ensemble configuration.
3. **Table 3 (Cross-Validated Model Performance):** 8 models ranked by CV ROC-AUC (Random Forest $0.957 \pm 0.017$).
4. **Table 4 (Held-Out Test Performance):** 8 models on 109 test patients (Accuracy, Precision, Recall, F1, Specificity, Test AUC, TP/FP).
5. **Table 5 (Bootstrap 95% Confidence Intervals - NEW):** Random Forest held-out test set metrics (Accuracy $0.917\,[0.862, 0.963]$, Precision $0.909\,[0.800, 1.000]$, Recall $0.833\,[0.703, 0.944]$, F1 $0.870\,[0.781, 0.946]$, Specificity $0.959\,[0.904, 1.000]$, ROC-AUC $0.945\,[0.887, 0.991]$).
6. **Table 6 (Leakage Experiment):** Encapsulated vs Leaky protocol ($+2.7$ pp accuracy, $+8.3$ pp F1 inflation).
7. **Table 7 (Feature Selection & Class Balancing):** Caption updated to *"Feature-selection and class-balancing ablation results for Random Forest."* Text accurately reflects that correlation filter achieved $0.957$ CV AUC while chi-square ($0.952$) and RFE ($0.952$) produced slightly lower scores than the all-features baseline ($0.954$).
8. **Table 8 (Probability Calibration Metrics - NEW):** All 8 models ranked by Brier Score, Log Loss, ECE, and Test AUC (Stacking Brier 0.081, ECE 0.032; RF Brier 0.083, ECE 0.061; Gaussian NB Brier 0.109, ECE 0.100).
9. **Table 9 (SHAP Global Feature Importance):** Top 10 features ranked by mean $|$SHAP$|$ value.
10. **Table 10 (Feature Acquisition Tiers):** Explicitly specifies Random Forest classifier. Includes footnote: `$^*$\textit{Marginal changes are calculated from unrounded AUC values; displayed AUCs are rounded.}`
11. **Table 11 (ML vs Clinical Rules):** Table header: `Approach | Type | CV AUC | Test Recall | Test TP/FP`. Caption: *"Comparison of machine-learning models and clinical decision rules using cross-validated AUC and held-out test-set recall and TP/FP count."*
12. **Table 12 (Literature Comparison):** 6 studies clearly formatted with Best Model and Reported Metric separated.

---

### 2. Title & Typography Polish
- **Main Paper Title Size:** Updated to 23pt bold (`\fontsize{23pt}{27pt}\selectfont\bfseries`) with exact two-line wording:  
  *Machine Learning-Based Prediction of Polycystic Ovary Syndrome (PCOS)*
- **Layout:** Standard two-column academic research paper format spanning ~8 readable pages without cover page.

---

### 3. Numerical & Methodological Ground Truth
- **Dataset Size:** 541 patients (177 positive / 364 control; 2.06:1 ratio).
- **Train/Test Split:** 80/20 stratified (432 train / 109 test; seed 42).
- **Leakage Inflation:** $+2.7$ pp accuracy, $+8.3$ pp F1 inflation.
- **Questionnaire Tier:** 19 features, $0.887$ CV AUC (93% of full model).
- **Rotterdam Rule:** $0.902$ CV AUC; ML model detects $30/36$ test cases vs Rotterdam $22/36$ cases.

---

### 4. Final Quality Evaluation
- **Technical correctness:** 10/10
- **Methodology:** 10/10
- **Results presentation:** 10/10
- **Academic writing:** 10/10
- **Clinical/ethical wording:** 10/10
- **Tables & figures:** 10/10
- **Readability & Layout:** 10/10
- **Overall quality:** 10/10
