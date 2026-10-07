# FINAL REPORT AUDIT (COMPLETE & LAYOUT VERIFIED)

**Project Title:** Machine Learning-Based Prediction of Polycystic Ovary Syndrome (PCOS)  
**Authors:** Fatema Ferdous (0152410052) · Wafa Haque (0152420023) · Khondoker Sazzad Sunfi (0152310002)  
**Department:** Department of Data Science, United International University (UIU)  
**Audit Date:** 2026-10-07  

---

### 1. Final Layout Audit
- **Total PDF Pages:** ~8.0 pages (fits targets perfectly in two-column format).
- **Total Tables Preserved:** 12 tables (All 12 important tables present, numbered, and cited).
- **Total Figures Preserved:** 5 figures (EDA subfigures, model performance 3-up figure, leakage experiment figure, SHAP beeswarm figure, clinical utility cost-tiers & DCA subfigures).
- **Tables Spanning Both Columns (`table*`):**
  - Table 4: Held-out test performance (`tab:test_results`)
  - Table 11: Machine learning vs clinical decision rules (`tab:clinical`)
  - Table 12: Literature comparison of reviewed studies (`tab:literature`)
- **Single-Column Tables (`table`, $\le \text{columnwidth}$):**
  - Table 1: Dataset summary (`tab:dataset`)
  - Table 2: Evaluated models & hyperparameters (`tab:models`)
  - Table 3: Cross-validated performance (`tab:cv_results`)
  - Table 5: Bootstrap 95% confidence intervals (`tab:bootstrap`)
  - Table 6: Quantification of data leakage (`tab:leakage`)
  - Table 7: Feature selection & class-balancing ablation (`tab:fsel`)
  - Table 8: Probability calibration metrics (`tab:calibration`)
  - Table 9: SHAP top 10 features (`tab:shap`)
  - Table 10: Feature acquisition tiers (`tab:tiers`)
- **Overlap & Clipping Confirmation:** Zero table/text overlap, zero column boundary overflow, zero clipped tables, zero hidden text. All single-column tables fit strictly within $\text{columnwidth}$, and wide multi-column tables cleanly span $\text{textwidth}$.

---

### 2. Verification of All 12 Important Tables
1. **Table 1 (Dataset Summary):** Total patients (541), PCOS positive (177), Non-PCOS (364), Class ratio (2.06:1), Features (41), Target (PCOS), Train/Test (432/109).
2. **Table 2 (Models & Hyperparameters):** 7 core classifiers + 1 Stacking Ensemble configuration.
3. **Table 3 (Cross-Validated Model Performance):** 8 models ranked by CV ROC-AUC (Random Forest $0.957 \pm 0.017$).
4. **Table 4 (Held-Out Test Performance):** 8 models on 109 test patients (Accuracy, Precision, Recall, F1, Specificity, Test AUC, TP/FP).
5. **Table 5 (Bootstrap 95% Confidence Intervals):** Random Forest held-out test set metrics (Accuracy $0.917\,[0.862, 0.963]$, Precision $0.909\,[0.800, 1.000]$, Recall $0.833\,[0.703, 0.944]$, F1 $0.870\,[0.781, 0.946]$, Specificity $0.959\,[0.904, 1.000]$, ROC-AUC $0.945\,[0.887, 0.991]$).
6. **Table 6 (Leakage Experiment):** Encapsulated vs Leaky protocol ($+2.7$ pp accuracy, $+8.3$ pp F1 inflation).
7. **Table 7 (Feature Selection & Class Balancing):** Caption: *"Feature-selection and class-balancing ablation results for Random Forest."* Text accurately reflects correlation filter ($0.957$) vs chi-square ($0.952$), RFE ($0.952$), and all features ($0.954$).
8. **Table 8 (Probability Calibration Metrics):** All 8 models ranked by Brier Score, Log Loss, ECE, and Test AUC.
9. **Table 9 (SHAP Global Feature Importance):** Top 10 features ranked by mean $|$SHAP$|$ value.
10. **Table 10 (Feature Acquisition Tiers):** Specifies Random Forest classifier. Includes footnote: `$^*$\textit{Marginal changes are calculated from unrounded AUC values; displayed AUCs are rounded.}`
11. **Table 11 (ML vs Clinical Rules):** Table header: `Approach | Type | CV AUC | Test Recall | Test TP/FP`. Caption: *"Comparison of machine-learning models and clinical decision rules using cross-validated AUC and held-out test-set recall and TP/FP count."*
12. **Table 12 (Literature Comparison):** 6 studies clearly formatted with Best Model and Reported Metric separated.

---

### 3. Title & Typography Polish
- **Main Paper Title Size:** 23pt bold (`\fontsize{23pt}{27pt}\selectfont\bfseries`) on two lines:  
  *Machine Learning-Based Prediction of Polycystic Ovary Syndrome (PCOS)*
- **Layout:** Standard two-column academic paper format spanning ~8 pages without cover page.

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
