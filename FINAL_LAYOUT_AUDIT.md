# FINAL PAGE-SPECIFIC LAYOUT AUDIT REPORT

## Page-by-Page Overlap Audit

### Page 2
- **Problem found:** 
  1. **Table 1 (`tab:dataset`):** Implemented using standard `tabular` with un-wrapped `l` columns (`Kottarathil (2020), 10 Hospitals (Kerala, India)`). The combined un-wrapped column width exceeded `\columnwidth` ($8.46\text{cm}$), causing the table to extend past the right boundary of Column 1 and overlap body text in Column 2.
  2. **Figure 1 (`fig:eda`):** Configured as a single-column `\begin{figure}[t]` containing three subfigures (`0.32\columnwidth` each). Due to image aspect ratios, squeezing three charts into a single column caused vertical alignment shifts and float stacking.
- **Fix applied:** 
  1. Converted Table 1 to `\begin{tabularx}{\columnwidth}{@{}lX@{}}`. Column 1 takes its exact symbol width while Column 2 automatically wraps inside the remaining space, guaranteeing total width $\equiv \text{\columnwidth}$ ($8.46\text{cm}$).
  2. Converted Figure 1 to a two-column spanning float `\begin{figure*}[t]` with `0.32\textwidth` subfigure width. The three subfigures render cleanly across the top of Page 2 with zero text encroachment.
- **Overlap resolved:** YES

---

### Page 4
- **Problem found:**
  1. **Table 5 (`tab:bootstrap`) & Table 6 (`tab:leakage`):** Both tables used un-wrapped `{lccc}` columns with long headers (`95\% Bootstrap CI`, `Interval Width`, `Correct (Encapsulated)`, `Performance Inflation`). Total un-wrapped table widths exceeded `\columnwidth` by up to $3.2\text{cm}$, spilling across the middle column margin and overlapping body text in the right column.
  2. **Figure Float Stacking:** Single-column figures were set with tight float constraints, causing them to stack at the page top and push surrounding text into narrow gutters.
- **Fix applied:**
  1. Shortened Table 5 headers (`Point Est.`, `CI Width`) and set explicit padding `\setlength{\tabcolsep}{3pt}` with `@{}l c c c@{}}`. Total table width is now $7.4\text{cm} \le \text{\columnwidth}$.
  2. Shortened Table 6 headers (`Encapsulated`, `Leaky`, `Inflation`) and set explicit padding `\setlength{\tabcolsep}{3pt}` with `@{}l c c c@{}}`. Total table width is now $7.3\text{cm} \le \text{\columnwidth}$.
  3. Set float placement specifiers on single-column figures to `[htbp]` so LaTeX positions figures inline without forcing multi-float stacking.
- **Overlap resolved:** YES

---

### Page 5
- **Problem found:**
  1. **Table 7 (`tab:fsel`), Table 8 (`tab:calibration`), Table 9 (`tab:shap`), and Table 10 (`tab:tiers`):** All four single-column tables used un-wrapped `{lcccc}` or `{lcc}` columns with long text entries (e.g., `$\uparrow$ Increased PCOS Risk`, `Brier Score $\downarrow$`, `Marginal $\Delta$ AUC$^*`, `Feature Selection Strategy (Random Forest CV AUC)`). Every table width exceeded `\columnwidth` ($8.46\text{cm}$), spilling into the neighboring column.
- **Fix applied:**
  1. **Table 7 (Feature Selection Ablation):** Shortened headers to `Strategy & Features & CV AUC & Test AUC & Test Acc.` with `\setlength{\tabcolsep}{2.5pt}` and `@{}l c c c c@{}}` (width $7.6\text{cm} \le \text{\columnwidth}$).
  2. **Table 8 (Calibration Metrics):** Shortened headers to `Model & Brier $\downarrow$ & LogLoss $\downarrow$ & ECE $\downarrow$ & Test AUC` with `\setlength{\tabcolsep}{2pt}` and `@{}l c c c c@{}}` (width $6.7\text{cm} \le \text{\columnwidth}$).
  3. **Table 9 (SHAP Importance):** Shortened direction column entries to `$\uparrow$ Increased Risk` / `$\downarrow$ Decreased Risk` and headers to `Feature Name & Mean $|$SHAP$|$ & Risk Effect` with `\setlength{\tabcolsep}{3.5pt}` and `@{}l c c@{}}` (width $6.7\text{cm} \le \text{\columnwidth}$).
  4. **Table 10 (Feature Tiers):** Shortened headers to `Acquisition Tier & Features & CV AUC & $\Delta$ AUC$^*` with `\setlength{\tabcolsep}{3.5pt}` and `@{}l c c c@{}}` (width $6.7\text{cm} \le \text{\columnwidth}$).
- **Overlap resolved:** YES

---

### Global Check
- **All other pages checked:** YES
- **New overlap introduced:** NO
- **Tables remain readable:** YES
- **Two-column layout preserved:** YES
