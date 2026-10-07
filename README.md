# Machine Learning-Based Prediction of Polycystic Ovary Syndrome (PCOS)

**Group 5** — Fatema Ferdous (0152410052) · Wafa Haque (0152420023) · Khondoker Sazzad Sunfi (0152310002)

An end-to-end machine learning study predicting PCOS from clinical, hormonal and physical measurements, built to address the gaps identified in our literature review of five recent papers.

---

## Headline result

| Property | Value |
|---|---|
| **Best model** | **Random Forest** (SMOTE + correlation-based feature selection, 20 features) |
| **Cross-validated ROC-AUC** | **0.957 ± 0.017** (10-fold × 3 repeats) |
| **Held-out test accuracy** | **0.917** |
| **Held-out test ROC-AUC** | **0.945** — 95% CI **[0.887, 0.991]** |
| **Test recall / specificity** | **0.833 / 0.959** |

### The key findings of this project

| Finding | Result |
|---|---|
| **A leaky protocol manufactures performance** | **+2.7 points** accuracy, **+8.3 points** F1 — same model, same data, same folds |
| **CV ranking is split-sensitive** | 8 models evaluated; KNN shows the main practical deficit. Across a 10-seed sweep, **4 distinct models win at least once** (Gaussian NB 40%, RF 30%, Stacking 20%, Elastic-Net 10%) |
| **A free questionnaire gets you most of the way** | **0.887 CV AUC** with no clinician, lab or ultrasound — **93%** of the full model. The entire blood panel adds **+0.010** |
| **AutoML finds no headroom** | **+0.0004 ROC-AUC** gain from a 120s architecture + hyperparameter search |
| **A 2003 clinical rule gets 94% of the way** | "Follicles ≥ 12" reaches **0.902 CV AUC with zero learned parameters** — detects 22 of 36 cases, where the ML model detects 30 |

---

## The leakage experiment

Papers 4 and 5 report 98.9–99.3% accuracy on the same 541-row dataset. Our correctly validated pipeline reaches ~91.7% test accuracy. Rather than speculate about the gap, we measured it.

The same classifier, the same data and the same folds were run under two protocols that differ in exactly one respect — **where SMOTE and feature selection happen**:

| Protocol | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Correct (SMOTE + selection inside CV) | 0.900 | 0.856 | 0.836 | 0.845 | 0.949 |
| Leaky (SMOTE + selection before CV) | 0.927 | 0.923 | 0.934 | 0.928 | 0.975 |
| **Inflation** | **+0.027** | **+0.067** | **+0.098** | **+0.083** | **+0.025** |

When SMOTE runs before the split, synthetic minority rows interpolated from training patients end up in the validation fold — the model is partly scored on points derived from its own training data. When RFE runs before the split, the selector has already read every label, including the test labels.

What it shows is that a 98–99% headline on this dataset is **reachable through methodology alone**, so such numbers cannot be taken at face value without a stated protocol.

---

## Model comparison (repeated stratified 10-fold CV, training split only)

Values below match the verified project outputs in `reports/results/cv_results.csv`:

| Model | CV ROC-AUC | CV Accuracy | CV Recall | CV F1 |
|---|---|---|---|---|
| **Random Forest** | **0.957 ± 0.017** | 0.891 ± 0.025 | 0.809 ± 0.042 | 0.831 ± 0.028 |
| Stacking Ensemble | 0.951 ± 0.020 | 0.896 ± 0.034 | 0.830 ± 0.038 | 0.840 ± 0.047 |
| Gaussian NB | 0.951 ± 0.023 | 0.864 ± 0.045 | 0.851 ± 0.082 | 0.804 ± 0.058 |
| Elastic-Net LR | 0.948 ± 0.016 | 0.889 ± 0.026 | 0.851 ± 0.025 | 0.835 ± 0.032 |
| Logistic Regression | 0.947 ± 0.017 | 0.880 ± 0.035 | 0.844 ± 0.016 | 0.823 ± 0.044 |
| XGBoost | 0.944 ± 0.018 | 0.887 ± 0.040 | 0.802 ± 0.034 | 0.825 ± 0.050 |
| SVM (RBF) | 0.939 ± 0.022 | 0.882 ± 0.054 | 0.851 ± 0.027 | 0.829 ± 0.065 |
| KNN | 0.929 ± 0.037 | 0.873 ± 0.044 | 0.858 ± 0.039 | 0.818 ± 0.056 |

---

## Feature selection

Values below match the verified project outputs in `reports/results/feature_set_comparison.csv`:

| Strategy | Features kept | Mean CV ROC-AUC |
|---|---|---|
| **Correlation Filter** | **20** | **0.957** |
| All features baseline | 41 | 0.954 |
| Chi-Square | 15 | 0.952 |
| RFE | 15 | 0.952 |

---

## What does each tier of testing buy?

Features are grouped by what they cost to obtain, and a model is trained on each cumulative tier (`reports/results/cost_tiers.csv`):

| Tier | What it needs | Features | CV ROC-AUC | Marginal gain |
|---|---|---|---|---|
| **Questionnaire** | Form, scale, tape measure | 19 | **0.887** | — |
| + Clinic vitals | Nurse, 5 minutes | 25 | 0.880 | −0.007 |
| + Blood panel | Venous draw, 11 lab assays | 36 | 0.890 | **+0.010** |
| + Ultrasound | Sonographer, pelvic scan | 41 | **0.952** | **+0.062** |

---

## Repository Structure

```
PCOS_ML/
├── data/
│   └── raw/                   # Raw Kaggle PCOS dataset
├── reports/
│   ├── figures/               # Generated high-resolution plots (29 PNGs)
│   ├── results/               # Master CSV/JSON evaluation outputs
│   └── PCOS_ML_prediction_report.tex # Final LaTeX report source
├── src/
│   ├── config.py              # Constants, paths, hyperparameter grids
│   ├── data.py                # Dataset loading, cleaning, validation
│   ├── features.py            # Feature selection transformers
│   └── models.py              # Classifier pipeline builders
├── PCOS_ML_prediction_report.tex # Root LaTeX source
├── FINAL_CONSISTENCY_AUDIT.md # Systematic numerical & layout audit
└── README.md                  # Project overview and ground-truth summary
```
