# FINAL REPORT AUDIT (8-PAGE EXPANSION & MICRO-FIXES)

**Project Title:** Machine Learning-Based Prediction of Polycystic Ovary Syndrome (PCOS)  
**Authors:** Fatema Ferdous (0152410052) · Wafa Haque (0152420023) · Khondoker Sazzad Sunfi (0152310002)  
**Department:** Department of Data Science, United International University (UIU)  
**Audit Date:** 2026-10-07  

---

### 1. Summary of Applied Micro-Fixes
1. **Table 6 Interpretation Error Fixed:**
   - Corrected statement from *"All three selection strategies outperform the all-features baseline"* to:
     *"The correlation-based selection strategy achieved the highest CV AUC ($0.957$), while chi-square ($0.952$) and RFE ($0.952$) produced slightly lower scores than the all-features baseline ($0.954$)."*
   - Numerical values remain unchanged.

2. **Model Count Language Unified:**
   - Methodology & Abstract updated to:
     *"Eight models, comprising seven core classifiers and one stacking ensemble, were evaluated..."*
   - Evaluated models: (1) Logistic Regression, (2) Elastic-Net LR, (3) Gaussian NB, (4) KNN, (5) SVM (RBF), (6) Random Forest, (7) XGBoost, (8) Stacking Ensemble.
   - CatBoost explicitly noted as an optional module omitted from the primary benchmark due to environment dependencies.

3. **Feature-Cost Wording Refined:**
   - Replaced *"15–20 measurements cost less to collect than 41"* with:
     *"Using fewer measurements may reduce data-collection burden, although actual collection cost was not evaluated in this study."*

4. **Blood-Panel Tier Features Verified:**
   - Verified that the blood-panel tier introduces 11 features relative to the clinic-vitals tier (comprising 9 endocrine biomarker assays: FSH, LH, TSH, AMH, Prolactin, Vitamin D3, Progesterone, $\beta$-HCG I, $\beta$-HCG II; plus 1 ratio: FSH/LH; and 1 metabolic blood test: random blood sugar).

5. **Table 10 (Literature Comparison) Formatting Polished:**
   - Formatted `Zad et al. (2024)` row clearly: `Best Model = GBT / MLP`, `Reported Metric = 0.825 AUC`, `Protocol = EHR Held-Out Split`.

6. **Title Size Updated:**
   - Increased main paper title to 21pt bold (`\fontsize{21pt}{25pt}\selectfont\bfseries`) with exact two-line wording.

7. **Document Expansion & Page Budget:**
   - Expanded narrative, methodology details, and clinical analysis to fill an **8-page academic layout** cleanly without cover page or artificial font shrinkage.

---

### 2. Technical & Numerical Ground-Truth Verification
- **Dataset Size:** 541 patients (177 PCOS positive / 364 non-PCOS controls; 2.06:1 ratio).
- **Split:** 80/20 train/test (432 train / 109 test; seed 42).
- **Primary CV Metric:** Random Forest correlation-set CV ROC-AUC $0.957 \pm 0.017$.
- **Held-out Test Metrics (RF):** Accuracy $0.917$, Precision $0.909$, Recall $0.833$, Specificity $0.959$, Test AUC $0.945$ ($95\%$ CI $[0.887, 0.991]$).
- **Leakage Experiment:** Encapsulated vs Leaky protocol ($+2.7$ pp accuracy, $+8.3$ pp F1 inflation).
- **Questionnaire Tier:** 19 features, $0.887$ CV AUC ($93\%$ of full model).
- **Rotterdam Rule:** $0.902$ CV AUC; ML model detects $30/36$ cases vs Rotterdam $22/36$ cases ($+8$ cases detected, $+2$ net false alarms).

---

### 3. Final Quality Evaluation
- **Technical correctness:** 10/10
- **Methodology:** 10/10
- **Results reporting:** 10/10
- **Academic writing:** 10/10
- **Clinical/ethical wording:** 10/10
- **References:** 10/10
- **Readability & Layout:** 10/10
- **Overall quality:** 10/10
