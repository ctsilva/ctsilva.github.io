---
title: "Exercise 3: Model Assessment Visualization"
permalink: /2025-VisML-CSE/assignments/exercise3
author_profile: true
---

# Exercise 3: Model Assessment Visualization

**CS-GY 9223: Visualization for Machine Learning - Fall 2025**

**Released:** September 22, 2025  
**Due:** September 29, 2025 (11:59 PM EST)  
**Weight:** 8.33% of final grade

---

## Overview

Model assessment is fundamental to machine learning practice. This assignment focuses on creating comprehensive visualizations for evaluating and comparing machine learning models. You will build an interactive dashboard that presents classification and regression metrics in intuitive, actionable ways.

## Learning Objectives

By completing this exercise, you will:
- Understand key performance metrics for classification and regression
- Design effective visualizations for confusion matrices and ROC analysis
- Create interactive comparisons between multiple models
- Implement cross-validation visualization techniques
- Build reusable components for model assessment workflows

---

## Assignment Tasks

### Task 1: Classification Metrics Dashboard (40%)

Build comprehensive visualizations for classification model assessment:

#### Confusion Matrix Visualization
- **Interactive Heatmap:** Hoverable confusion matrix with detailed statistics
- **Normalization Options:** Toggle between count, row-normalized, and column-normalized views
- **Multi-class Support:** Handle 2-10 classes effectively
- **Drill-down Capability:** Click cells to see example misclassifications

#### ROC and Precision-Recall Curves
- **Multi-class ROC:** One-vs-rest or one-vs-one curve display
- **PR Curves:** Precision-Recall curves with AUC calculations
- **Threshold Analysis:** Interactive threshold slider with metric updates
- **Comparison Mode:** Overlay multiple models on same plot

#### Classification Report Visualization
- **Metric Summary Table:** Precision, Recall, F1-score per class
- **Visual Metric Comparison:** Bar charts or radar charts for easy comparison
- **Macro/Micro Averages:** Clear display of aggregated metrics
- **Class Imbalance Awareness:** Visualization of support per class

### Task 2: Regression Metrics Dashboard (25%)

Create visualizations for regression model evaluation:

#### Residual Analysis
- **Residual Plots:** Residuals vs predicted values with trend lines
- **Q-Q Plots:** Normal probability plots for residual distribution
- **Histogram Overlay:** Residual distribution with normality tests
- **Outlier Highlighting:** Interactive identification of extreme residuals

#### Prediction Quality Visualization
- **Predicted vs Actual:** Scatter plot with perfect prediction line
- **Error Distribution:** Histogram of prediction errors
- **Metric Summary:** MAE, MSE, RMSE, R² with visual representations
- **Feature Impact:** Residuals colored by key feature values

### Task 3: Model Comparison Interface (25%)

Implement side-by-side model comparison capabilities:

#### Comparative Metrics
- **Side-by-side Tables:** Direct metric comparison across models
- **Difference Visualization:** Heatmaps showing metric differences
- **Statistical Significance:** Tests for significant performance differences
- **Ranking Display:** Model ranking with confidence intervals

#### Cross-Validation Visualization
- **CV Score Distributions:** Box plots or violin plots of cross-validation scores
- **Fold-by-Fold Analysis:** Performance across individual CV folds
- **Stability Metrics:** Variance and standard deviation across folds
- **Learning Curves:** Performance vs training set size (if data available)

### Task 4: Interactive Features and Usability (10%)

Enhance user experience with interactive capabilities:

#### Data Filtering and Selection
- **Class Filtering:** Show/hide specific classes in multi-class problems
- **Confidence Thresholding:** Filter predictions by confidence level
- **Sample Selection:** Interactive selection of data subsets for analysis

#### Export and Sharing
- **Report Generation:** Export comprehensive model assessment reports
- **Visualization Export:** SVG/PNG export of individual charts
- **Data Export:** CSV export of calculated metrics and statistics

---

## Technical Requirements

### Implementation Stack
- **D3.js v7+** for all visualizations
- **HTML5/CSS3** for responsive dashboard layout
- **JavaScript ES6+** with modular organization
- **SVG** for scalable, high-quality charts

### Data Format Support
- **JSON Format:** Structured model predictions and ground truth
- **CSV Import:** Support for uploaded evaluation datasets
- **Multiple Models:** Ability to load and compare 2-5 models simultaneously

### Performance Requirements
- **Responsive Design:** Works on desktop, tablet, and mobile
- **Fast Rendering:** Smooth interactions with datasets up to 10,000 samples
- **Memory Efficiency:** Handles multiple models without browser slowdown

---

## Required Visualizations

### 1. Enhanced Confusion Matrix
```javascript
// Example structure - implement with D3.js
const confusionMatrix = {
    classes: ["Class A", "Class B", "Class C"],
    matrix: [[85, 3, 2], [4, 88, 1], [2, 1, 91]],
    normalization: "none" | "row" | "column"
};
```

### 2. Interactive ROC Curves
- Multiple curves on single plot
- AUC values displayed prominently
- Threshold markers with optimal point highlighting
- Zoom and pan functionality

### 3. Model Comparison Dashboard
- Tabular metrics with sortable columns
- Radar chart overlaying key metrics
- Statistical significance indicators
- Performance improvement/degradation highlighting

### 4. Cross-Validation Analysis
- Box plots showing metric distributions
- Individual fold performance scatter plots
- Stability ranking across models
- Outlier fold identification

---

## Datasets Provided

You will work with three evaluation scenarios:

### 1. Binary Classification: Credit Approval
- **Task:** Predict loan approval decisions
- **Metrics Focus:** ROC-AUC, Precision-Recall, Class balance considerations
- **Models Provided:** Logistic Regression, Random Forest, SVM

### 2. Multi-class Classification: Image Recognition
- **Task:** Classify images into 5 categories  
- **Metrics Focus:** Confusion matrices, per-class performance
- **Models Provided:** CNN, ResNet, Vision Transformer

### 3. Regression: House Price Prediction
- **Task:** Predict real estate prices
- **Metrics Focus:** Residual analysis, prediction intervals
- **Models Provided:** Linear Regression, Gradient Boosting, Neural Network

---

## Deliverables

### 1. Interactive Web Dashboard
Deploy a comprehensive model assessment tool featuring:
- **All required visualizations** implemented and functional
- **Three dataset scenarios** with real model evaluation results
- **Responsive design** that works across devices
- **Professional styling** with consistent design language

### 2. Technical Documentation (4-5 pages)
Submit a detailed report covering:

**Introduction (0.5 pages)**
- Importance of model assessment visualization
- Overview of implemented features and capabilities

**Design Rationale (1.5 pages)**
- Justification for visualization choices
- User experience design decisions
- Handling of edge cases and error conditions

**Implementation Details (1.5 pages)**
- Technical architecture and D3.js usage
- Performance optimization strategies
- Cross-browser compatibility considerations

**Evaluation Results (1 page)**
- Analysis of the three provided model scenarios
- Insights gained from visualization exploration
- Comparative assessment of model performance

**Future Enhancements (0.5 pages)**
- Limitations of current implementation
- Proposed improvements and extensions
- Integration possibilities with ML workflows

### 3. Code Repository and Demo
Create a professional GitHub repository with:
- **Complete source code** with modular organization
- **Comprehensive README** with setup and usage instructions
- **Live demo link** hosted on GitHub Pages or similar
- **Data processing scripts** for converting model outputs to required format

---

## Evaluation Criteria

### Visualization Quality (30%)
- **Chart Effectiveness:** Clear, accurate representation of metrics
- **Visual Design:** Professional appearance with consistent styling
- **Information Density:** Optimal balance of detail and clarity
- **Color Usage:** Effective and accessible color schemes

### Interactive Functionality (25%)
- **User Experience:** Intuitive navigation and interaction patterns
- **Feature Completeness:** All required interactive elements functional
- **Performance:** Smooth interactions without lag or crashes
- **Responsiveness:** Proper behavior across different screen sizes

### Technical Implementation (20%)
- **Code Quality:** Clean, modular, well-documented code
- **D3.js Mastery:** Effective use of D3 patterns and best practices
- **Architecture:** Logical organization and separation of concerns
- **Browser Compatibility:** Works in modern browsers

### Model Assessment Insights (15%)
- **Analytical Depth:** Meaningful insights from model comparisons
- **Metric Understanding:** Correct interpretation and presentation of metrics
- **Edge Case Handling:** Proper treatment of special cases (perfect classifiers, etc.)
- **Statistical Rigor:** Appropriate use of statistical concepts

### Documentation and Communication (10%)
- **Report Quality:** Clear, professional technical writing
- **Code Documentation:** Comprehensive inline and README documentation
- **Reproducibility:** Others can run and extend your implementation
- **User Guidelines:** Clear instructions for using the dashboard

---

## Bonus Opportunities (+10% each, max +20%)

### Advanced Statistical Features
- **Bootstrap Confidence Intervals:** Calculate and visualize confidence intervals for metrics
- **Statistical Significance Testing:** Implement McNemar's test or similar for model comparison
- **Power Analysis:** Visualize statistical power of model comparisons

### Machine Learning Pipeline Integration
- **Real-time Updates:** Connect to live model training/evaluation
- **Hyperparameter Sensitivity:** Visualize metric sensitivity to hyperparameters
- **Feature Importance Integration:** Correlate poor predictions with feature values

---

## Submission Instructions

1. **Deploy Dashboard:** Host on GitHub Pages, Netlify, or similar platform
2. **Create Repository:** Name it `visml-exercise3-[username]`
3. **Prepare Submission:**
   - Live dashboard URL
   - GitHub repository link  
   - Technical documentation (PDF)
   - Brief video demo (3-5 minutes)
4. **Submit via NYU Classes:** Upload all materials and links

**Late Policy:** 20% deduction per day, maximum 5 days late

---

## Resources

### Machine Learning Metrics
- Hastie et al., "The Elements of Statistical Learning" Chapter 7
- James et al., "An Introduction to Statistical Learning" Chapter 5
- Flach, "Machine Learning: The Art and Science of Algorithms" Chapter 15

### Visualization References
- Few, "Information Dashboard Design"
- Cairo, "The Functional Art" Chapter 9
- Munzner, "Visualization Analysis and Design" Chapter 13

### Technical Documentation
- [D3.js Scales Documentation](https://github.com/d3/d3-scale)
- [SVG Path Tutorial](https://www.dashingd3js.com/svg-paths-and-d3js)
- [Bootstrap Grid System](https://getbootstrap.com/docs/5.1/layout/grid/)

### Model Assessment Tools
- [Scikit-learn Model Selection](https://scikit-learn.org/stable/model_selection.html)
- [MLxtend Model Evaluation](http://rasbt.github.io/mlxtend/user_guide/evaluate/)
- [Yellowbrick Visualization](https://www.scikit-yb.org/en/latest/)

---

## Example Code Snippets

### Confusion Matrix Heatmap
```javascript
function drawConfusionMatrix(data, container) {
    const margin = {top: 50, right: 50, bottom: 100, left: 100};
    const width = 400 - margin.left - margin.right;
    const height = 400 - margin.top - margin.bottom;
    
    // Create scales and draw heatmap
    const colorScale = d3.scaleSequential(d3.interpolateBlues)
        .domain([0, d3.max(data.matrix.flat())]);
        
    // Implementation details here...
}
```

### ROC Curve Visualization
```javascript
function drawROCCurve(rocData, container) {
    const svg = d3.select(container)
        .append("svg")
        .attr("width", 500)
        .attr("height", 500);
        
    const line = d3.line()
        .x(d => xScale(d.fpr))
        .y(d => yScale(d.tpr))
        .curve(d3.curveLinear);
        
    // Draw ROC curve and AUC calculation...
}
```

---

## Getting Help

- **Discord Support:** Use #exercise3 channel for technical questions
- **Office Hours:** Schedule help with D3.js implementation
- **Data Format Questions:** Example data files provided in course repository
- **Statistical Concepts:** TA available for metrics interpretation help

---

## Academic Integrity

- **Individual Work:** Complete this assignment independently
- **Code Attribution:** Credit external libraries and code snippets
- **Data Usage:** Only use provided datasets or clearly cite external sources
- **Original Analysis:** Your insights and interpretations must be original

---

*Questions? Post in Discord #exercise3 channel or contact the teaching team.*