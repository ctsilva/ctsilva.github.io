---
title: "Exercise 4: Interactive Explainer"
permalink: /2025-VisML-CSE/assignments/exercise4
author_profile: true
---

# Exercise 4: Interactive Explainer

**CS-GY 9223: Visualization for Machine Learning - Fall 2025**

**Released:** September 29, 2025  
**Due:** October 6, 2025 (11:59 PM EST)  
**Weight:** 8.33% of final grade

---

## Overview

Understanding black-box machine learning models is crucial for trust, debugging, and regulatory compliance. This assignment focuses on building interactive explanation systems that make complex models interpretable through visualization. You will implement both local and global explanation techniques using LIME, SHAP, or similar methods.

## Learning Objectives

By completing this exercise, you will:
- Understand the difference between local and global model explanations
- Implement interactive explanation interfaces for black-box models
- Create visualizations for feature importance and model behavior
- Design what-if analysis tools for model exploration
- Build trust through transparent model interpretation systems

---

## Assignment Tasks

### Task 1: Local Explanation System (35%)

Build an interactive system for explaining individual predictions:

#### LIME-style Local Explanations
- **Feature Contribution Visualization:** Bar charts showing positive/negative feature impacts
- **Instance Perturbation:** Show how changing features affects predictions
- **Confidence Intervals:** Display uncertainty in explanations
- **Neighborhood Analysis:** Visualize local decision boundary approximation

#### Interactive Prediction Explorer
- **Input Manipulation:** Sliders/controls to modify feature values in real-time
- **Prediction Updates:** Live prediction updates as features change
- **Explanation Refresh:** Dynamic explanation updates with feature changes
- **Counterfactual Generation:** Find minimal changes needed to flip prediction

#### Visual Explanation Formats
- **Feature Importance Plots:** Horizontal bar charts with clear positive/negative distinction
- **Waterfall Charts:** Show cumulative feature contributions to final prediction
- **Heat Maps:** For image/spatial data, show pixel-level importance
- **Text Highlighting:** For text data, highlight important words/phrases

### Task 2: Global Model Analysis (30%)

Create visualizations for understanding overall model behavior:

#### Feature Importance Dashboard
- **Global Feature Rankings:** Overall feature importance across entire dataset
- **Feature Interaction Detection:** Identify and visualize feature interactions
- **Partial Dependence Plots:** Show feature effects while marginalizing others
- **Feature Distribution Analysis:** Show how predictions vary with feature distributions

#### Model Behavior Mapping
- **Decision Boundary Visualization:** 2D projections of decision boundaries
- **Prediction Landscapes:** Contour plots showing prediction confidence regions
- **Activation Patterns:** For neural networks, show layer activation patterns
- **Rule Extraction:** Extract and visualize approximate decision rules

#### Comparative Analysis
- **Model vs Model:** Compare explanation patterns between different models
- **Instance vs Population:** Compare local explanations to global patterns
- **Feature Stability:** Show consistency of feature importance across samples

### Task 3: What-If Analysis Interface (25%)

Implement interactive exploration capabilities:

#### Counterfactual Explorer
- **Minimal Change Calculator:** Find smallest changes to flip prediction
- **Multi-objective Optimization:** Balance prediction change with realism/cost
- **Path Visualization:** Show trajectory from original to counterfactual instance
- **Constraint Satisfaction:** Respect domain constraints in counterfactual generation

#### Scenario Analysis
- **Feature Group Manipulation:** Change multiple related features simultaneously
- **Sensitivity Analysis:** Show prediction sensitivity to each feature
- **Robustness Testing:** Explore prediction stability under perturbations
- **Adversarial Examples:** Generate and visualize adversarial inputs

#### Interactive Controls
- **Multi-dimensional Sliders:** Control multiple features with linked interactions
- **Constraint Panels:** Set bounds and relationships between features
- **Preset Scenarios:** Quick access to common what-if scenarios
- **History Tracking:** Save and compare multiple exploration sessions

### Task 4: User Experience and Trust (10%)

Design for interpretability and user trust:

#### Explanation Quality Indicators
- **Confidence Scores:** Show how reliable each explanation is
- **Coverage Metrics:** Indicate what percentage of behavior is explained
- **Stability Indicators:** Show consistency of explanations across similar instances
- **Uncertainty Visualization:** Represent epistemic and aleatoric uncertainty

#### Interactive Documentation
- **Method Descriptions:** Clear explanations of explanation techniques used
- **Limitation Warnings:** Communicate known limitations and assumptions
- **Validation Results:** Show explanation validation on known ground truth
- **Tutorial System:** Guide users through explanation interpretation

---

## Technical Requirements

### Implementation Stack
- **D3.js v7+** for all visualizations and interactions
- **HTML5/CSS3** for responsive interface design
- **JavaScript ES6+** with modern async/await patterns
- **Web Workers** (optional) for computationally intensive explanations

### Model Integration
Choose **one** of these approaches:
- **Python Backend:** Flask/FastAPI server with LIME/SHAP integration
- **JavaScript Models:** TensorFlow.js or client-side model inference
- **Pre-computed Explanations:** Static explanation data with interactive exploration
- **Mock Models:** Simplified models for demonstration purposes

### Explanation Libraries (if using Python backend)
- **LIME:** Local Interpretable Model-agnostic Explanations
- **SHAP:** SHapley Additive exPlanations  
- **Alibi:** Machine learning model inspection and interpretation
- **InterpretML:** Microsoft's interpretation library

---

## Required Features

### 1. Local Explanation Interface
```javascript
// Example structure for local explanations
const localExplanation = {
    instance_id: "sample_123",
    prediction: 0.85,
    confidence: 0.92,
    feature_contributions: [
        {feature: "age", value: 45, contribution: 0.12},
        {feature: "income", value: 75000, contribution: 0.08},
        {feature: "credit_score", value: 720, contribution: -0.03}
    ],
    counterfactuals: [
        {feature_changes: {age: 35}, new_prediction: 0.62}
    ]
};
```

### 2. Global Analysis Dashboard
- **Feature importance ranking** with confidence intervals
- **Partial dependence plots** for top 5-10 features
- **Feature interaction heatmap** showing pairwise interactions
- **Model summary statistics** and performance metrics

### 3. What-If Analysis Tool
- **Real-time prediction updates** as features change
- **Constraint handling** for realistic scenarios
- **Multi-step exploration** with undo/redo functionality
- **Export capabilities** for scenarios and results

---

## Datasets and Models

Choose **one** of these scenarios for your implementation:

### 1. Credit Approval (Tabular Data)
- **Model:** Random Forest or Gradient Boosting classifier
- **Features:** Age, income, credit score, employment history, debt ratio
- **Task:** Explain loan approval/rejection decisions
- **Focus:** Feature contributions, counterfactuals, fairness analysis

### 2. Medical Diagnosis (Mixed Data)
- **Model:** Neural network or ensemble classifier  
- **Features:** Patient demographics, symptoms, test results, medical history
- **Task:** Explain diagnostic predictions and recommendations
- **Focus:** Uncertainty quantification, confidence intervals, risk analysis

### 3. Text Classification (NLP)
- **Model:** BERT or similar transformer model
- **Features:** Document content, metadata, contextual embeddings
- **Task:** Explain document classification (e.g., sentiment, topic)
- **Focus:** Word-level importance, attention visualization, semantic analysis

### 4. Image Classification (Computer Vision)
- **Model:** Convolutional Neural Network (CNN)
- **Features:** Pixel values, spatial patterns, learned representations
- **Task:** Explain image classification decisions
- **Focus:** Saliency maps, super-pixel importance, layer activation

---

## Deliverables

### 1. Interactive Explanation System
Deploy a comprehensive explainability tool featuring:
- **Local explanation interface** with real-time updates
- **Global model analysis dashboard** with multiple visualization types
- **What-if analysis capabilities** with constraint handling
- **Professional UI/UX design** with clear information hierarchy

### 2. Technical Report (4-5 pages)
Submit a detailed analysis covering:

**Introduction and Background (1 page)**
- Importance of model explainability and interpretability
- Overview of chosen scenario and explanation methods
- Related work and existing explanation tools

**Method Implementation (1.5 pages)**
- Detailed description of explanation algorithms used
- Technical architecture and design decisions
- Integration approach (backend/frontend separation)

**User Interface Design (1 page)**
- Explanation visualization design rationale
- User experience considerations and testing
- Accessibility and usability features

**Case Study Analysis (1 page)**
- Detailed analysis of 3-5 specific prediction examples
- Insights gained through explanation exploration
- Model behavior patterns discovered through global analysis

**Evaluation and Limitations (0.5 pages)**
- Validation of explanation quality and faithfulness
- Known limitations and areas for improvement
- Future enhancement opportunities

### 3. Code Repository and Documentation
Create a professional repository with:
- **Complete source code** with modular architecture
- **Setup instructions** for reproducing the system
- **API documentation** (if using backend services)
- **User manual** with explanation interpretation guidelines
- **Live demo** hosted online with sample data

---

## Evaluation Criteria

### Explanation Quality (25%)
- **Faithfulness:** Explanations accurately reflect model behavior
- **Stability:** Consistent explanations for similar instances
- **Comprehensiveness:** Covers important aspects of model decisions
- **Actionability:** Explanations support decision-making

### Interactive Design (25%)
- **User Experience:** Intuitive navigation and clear information presentation
- **Real-time Performance:** Smooth interactions without significant delays
- **Visual Clarity:** Effective use of visual encoding for explanation data
- **Feature Completeness:** All required interactive elements implemented

### Technical Implementation (20%)
- **Code Quality:** Clean, modular, well-documented implementation
- **Architecture:** Appropriate separation of concerns and scalability
- **Integration:** Effective connection between ML models and visualization
- **Performance:** Efficient computation and rendering

### Analysis and Insights (20%)
- **Model Understanding:** Deep insights into model behavior patterns
- **Case Study Quality:** Thorough analysis of explanation examples  
- **Comparative Analysis:** Meaningful comparison between local and global explanations
- **Problem Domain Knowledge:** Understanding of domain-specific interpretation needs

### Communication and Documentation (10%)
- **Report Quality:** Clear, professional technical writing
- **Code Documentation:** Comprehensive inline and external documentation
- **User Guidelines:** Clear instructions for interpreting explanations
- **Reproducibility:** Complete setup and usage instructions

---

## Bonus Opportunities (+10% each, max +20%)

### Advanced Explanation Methods
- **Counterfactual Explanation Generation:** Implement advanced counterfactual algorithms
- **Multi-model Comparison:** Explain differences between multiple models
- **Temporal Explanations:** For time-series models, show how explanations evolve

### Enhanced User Experience
- **Explanation Personalization:** Adapt explanations to user expertise level
- **Interactive Tutorials:** Guided exploration of explanation concepts
- **Collaborative Features:** Share and discuss explanations with other users

### Validation and Testing
- **Human Subject Evaluation:** Conduct user studies on explanation effectiveness
- **Explanation Benchmarking:** Compare explanation quality against ground truth
- **Adversarial Testing:** Evaluate explanation robustness against adversarial examples

---

## Submission Instructions

1. **Deploy System:** Host complete system online (Heroku, AWS, etc.)
2. **Create Repository:** Name it `visml-exercise4-[username]`
3. **Prepare Submission Package:**
   - Live system URL with demo data
   - GitHub repository link
   - Technical report (PDF)
   - 5-7 minute video demonstration
4. **Submit via NYU Classes:** Upload all materials and links

**Late Policy:** 20% deduction per day, maximum 5 days late

---

## Resources

### Explainability Literature
- Ribeiro et al., "Why Should I Trust You? Explaining the Predictions of Any Classifier" (LIME)
- Lundberg & Lee, "A Unified Approach to Interpreting Model Predictions" (SHAP)
- Molnar, "Interpretable Machine Learning" (online book)
- Guidotti et al., "A Survey of Methods for Explaining Black Box Models" (2018)

### Technical Resources
- [LIME Documentation](https://github.com/marcotcr/lime)
- [SHAP Documentation](https://shap.readthedocs.io/)
- [Alibi Documentation](https://docs.seldon.io/projects/alibi/)
- [TensorFlow.js Models](https://www.tensorflow.org/js/models)

### Visualization Examples
- [SHAP Plots Documentation](https://shap.readthedocs.io/en/latest/example_notebooks/overviews/An%20introduction%20to%20explainable%20AI%20with%20Shapley%20values.html)
- [Google's What-If Tool](https://pair-code.github.io/what-if-tool/)
- [Microsoft InterpretML](https://interpret.ml/)

### UI/UX Design
- [Material Design Guidelines](https://material.io/design)
- [Nielsen's Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [Visualization Dashboard Design](https://www.tableau.com/learn/articles/dashboard-design-principles)

---

## Example Code Structure

### Local Explanation Visualization
```javascript
class LocalExplainer {
    constructor(container, model) {
        this.container = container;
        this.model = model;
        this.setupUI();
    }
    
    explainInstance(instance) {
        // Generate LIME/SHAP explanation
        const explanation = this.generateExplanation(instance);
        this.visualizeExplanation(explanation);
    }
    
    visualizeExplanation(explanation) {
        // Create feature importance bar chart
        // Add interactive controls for perturbation
        // Display counterfactual suggestions
    }
}
```

### What-If Analysis Interface
```javascript
class WhatIfAnalyzer {
    constructor(container, model, explanation_service) {
        this.model = model;
        this.explainer = explanation_service;
        this.setupControls();
    }
    
    async updatePrediction(feature_changes) {
        const new_prediction = await this.model.predict(feature_changes);
        const new_explanation = await this.explainer.explain(feature_changes);
        this.updateVisualization(new_prediction, new_explanation);
    }
}
```

---

## Getting Help

- **Discord Support:** Use #exercise4 channel for questions and discussion
- **Office Hours:** Available for explanation algorithm and implementation help
- **Model Integration:** TA support for connecting ML models to visualizations
- **UX Design:** Feedback available on interface design and user experience

---

## Academic Integrity

- **Individual Work:** Complete independently unless collaboration explicitly permitted
- **Model Attribution:** Credit any pre-trained models or explanation libraries used
- **Code Reuse:** Cite external code snippets and adapt appropriately
- **Original Analysis:** Your insights and interface design must be original work

---

*Questions? Post in Discord #exercise4 channel or contact the teaching team.*