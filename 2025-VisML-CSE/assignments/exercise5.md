---
title: "Exercise 5: Dimensionality Reduction Dashboard"
permalink: /2025-VisML-CSE/assignments/exercise5
author_profile: true
---

# Exercise 5: Dimensionality Reduction Dashboard

**CS-GY 9223: Visualization for Machine Learning - Fall 2025**

**Released:** October 20, 2025  
**Due:** October 27, 2025 (11:59 PM EST)  
**Weight:** 8.33% of final grade

---

## Overview

High-dimensional data analysis is fundamental to modern machine learning. This assignment focuses on building an interactive dashboard for exploring dimensionality reduction techniques including PCA, t-SNE, and UMAP. You will create tools that help users understand how these methods work, compare their results, and tune parameters effectively.

## Learning Objectives

By completing this exercise, you will:
- Understand the strengths and weaknesses of different dimensionality reduction methods
- Implement interactive parameter tuning interfaces for PCA, t-SNE, and UMAP
- Create effective visualizations for high-dimensional data exploration
- Build comparison tools for evaluating reduction quality
- Design interfaces for understanding embedding neighborhoods and clusters

---

## Assignment Tasks

### Task 1: Multi-Method Comparison Dashboard (40%)

Build a comprehensive interface comparing multiple dimensionality reduction techniques:

#### Side-by-Side Method Comparison
- **PCA Implementation:** Interactive 2D/3D principal component projections
- **t-SNE Integration:** Real-time t-SNE with perplexity parameter tuning
- **UMAP Visualization:** Interactive UMAP with n_neighbors and min_dist controls
- **Method Switching:** Quick toggle between methods with synchronized views

#### Parameter Exploration Interface
- **Interactive Controls:** Sliders and inputs for key parameters (perplexity, n_neighbors, etc.)
- **Real-time Updates:** Live visualization updates as parameters change
- **Parameter History:** Track parameter combinations and their results
- **Preset Configurations:** Quick access to common parameter settings

#### Quality Assessment Metrics
- **Preservation Metrics:** Local and global structure preservation measures
- **Stress Calculations:** Kruskal stress and other embedding quality metrics
- **Neighborhood Preservation:** Measure how well local neighborhoods are maintained
- **Comparative Rankings:** Score and rank different parameter combinations

### Task 2: Interactive Exploration Tools (30%)

Create tools for deep exploration of high-dimensional data:

#### Neighborhood Analysis
- **K-Nearest Neighbors:** Visualize original vs embedded space neighborhoods
- **Distance Preservation:** Compare original distances with embedded distances
- **Cluster Validation:** Assess how well clusters are preserved in low dimensions
- **Outlier Detection:** Identify points that behave differently in reduced space

#### Brushing and Linking
- **Point Selection:** Select points in 2D embedding to highlight in other views
- **Feature Correlation:** Show how original features correlate with embeddings
- **Cluster Exploration:** Interactive clustering with adjustable parameters
- **Time-series Tracking:** For iterative methods, show embedding evolution

#### Multi-View Coordination
- **Original Feature Space:** Parallel coordinates or other high-D visualization
- **Embedding Space:** 2D/3D scatter plots with customizable styling
- **Feature Importance:** Show which original features contribute to embedding axes
- **Projection Matrix:** Visualize PCA loadings or other transformation matrices

### Task 3: Algorithm Understanding Tools (20%)

Implement educational visualizations to explain how methods work:

#### PCA Explanation Interface
- **Variance Explanation:** Bar chart showing variance explained per component
- **Component Vectors:** Visualize principal component directions in original space
- **Reconstruction Error:** Show data reconstruction from reduced dimensions
- **Eigenface/Component Display:** Visual representation of principal components

#### t-SNE Process Visualization
- **Optimization Progress:** Show cost function decrease during optimization
- **Gradient Flow:** Visualize how points move during t-SNE iterations
- **Perplexity Effects:** Interactive demonstration of perplexity parameter impact
- **Early vs Late Exaggeration:** Show effects of different optimization phases

#### UMAP Mechanics
- **Graph Construction:** Visualize fuzzy simplicial complex construction
- **Neighbor Relationships:** Show k-nearest neighbor graphs at different scales
- **Optimization Dynamics:** Display force-directed layout optimization process
- **Parameter Sensitivity:** Interactive exploration of UMAP hyperparameters

### Task 4: Application Case Studies (10%)

Demonstrate the dashboard with three different datasets:

#### High-Dimensional Image Data
- **Dataset:** Fashion-MNIST or similar image dataset
- **Challenge:** Visualizing 784-dimensional pixel data
- **Analysis:** Compare how different methods preserve visual similarity

#### Text Embeddings
- **Dataset:** Word2Vec, GloVe, or document embeddings
- **Challenge:** Exploring semantic relationships in embedding space
- **Analysis:** Evaluate preservation of semantic neighborhoods

#### Scientific Data
- **Dataset:** Gene expression, chemical compounds, or similar
- **Challenge:** Understanding complex multidimensional relationships
- **Analysis:** Validate dimensionality reduction against known biological/chemical groups

---

## Technical Requirements

### Implementation Stack
- **D3.js v7+** for all interactive visualizations
- **HTML5/CSS3** for responsive dashboard layout
- **JavaScript ES6+** with modern async/await patterns
- **WebGL** (optional) for high-performance scatter plots with large datasets

### Dimensionality Reduction Implementation
Choose **one** of these approaches:
- **Python Backend:** Flask/FastAPI with scikit-learn, umap-learn integration
- **JavaScript Libraries:** ML-Matrix, t-SNE-js, or similar client-side libraries
- **Pre-computed Embeddings:** Focus on visualization of pre-calculated results
- **Hybrid Approach:** Pre-compute expensive algorithms, implement PCA client-side

### Performance Requirements
- **Responsive Design:** Smooth interactions on datasets with 1,000-10,000 points
- **Progressive Loading:** Handle large datasets without blocking the interface
- **Memory Management:** Efficient handling of multiple embeddings simultaneously
- **Real-time Updates:** Parameter changes reflected within 1-2 seconds

---

## Required Features

### 1. Method Comparison Interface
```javascript
// Example structure for embedding comparison
const embeddingComparison = {
    methods: ["pca", "tsne", "umap"],
    parameters: {
        pca: {n_components: 2},
        tsne: {perplexity: 30, learning_rate: 200},
        umap: {n_neighbors: 15, min_dist: 0.1}
    },
    quality_metrics: {
        pca: {explained_variance: 0.68, stress: 0.15},
        tsne: {kl_divergence: 2.1, trustworthiness: 0.85},
        umap: {fuzzy_set_cross_entropy: 1.3, connectivity: 0.92}
    }
};
```

### 2. Interactive Parameter Controls
- **Slider Controls:** Smooth parameter adjustment with live preview
- **Input Validation:** Prevent invalid parameter combinations
- **Reset Functionality:** Return to default parameter settings
- **Batch Processing:** Queue multiple parameter changes for efficient computation

### 3. Quality Assessment Dashboard
- **Metric Visualization:** Bar charts, line plots for quality metrics
- **Comparative Analysis:** Side-by-side metric comparison across methods
- **Historical Tracking:** Plot metric changes as parameters are adjusted
- **Statistical Significance:** Error bars and confidence intervals where applicable

---

## Datasets Provided

Work with **all three** of these datasets for comprehensive evaluation:

### 1. MNIST Digits (Subset)
- **Size:** 5,000 samples × 784 features
- **Ground Truth:** 10 digit classes for validation
- **Challenge:** Preserving digit similarity in 2D
- **Evaluation Focus:** Class separation and within-class clustering

### 2. Wine Quality Dataset
- **Size:** 4,898 samples × 11 features  
- **Ground Truth:** Wine quality scores
- **Challenge:** Understanding feature relationships
- **Evaluation Focus:** Feature importance and quality correlation

### 3. Single Cell RNA-seq (Subset)
- **Size:** 2,000 cells × 1,000 genes
- **Ground Truth:** Cell type annotations
- **Challenge:** Biological interpretation of cell relationships
- **Evaluation Focus:** Biological pathway preservation and cell type clustering

---

## Deliverables

### 1. Interactive Dashboard Application
Deploy a comprehensive dimensionality reduction exploration tool with:
- **Multi-method comparison** with synchronized parameter controls
- **Real-time quality assessment** with multiple metrics
- **Educational visualizations** explaining algorithm behavior
- **Three case study demonstrations** with different data types

### 2. Technical Report (4-5 pages)
Submit a detailed analysis covering:

**Introduction and Background (0.5 pages)**
- Importance of dimensionality reduction in ML workflows
- Overview of implemented methods and their trade-offs
- Dashboard design philosophy and user experience goals

**Method Implementation and Comparison (2 pages)**
- Technical details of PCA, t-SNE, and UMAP implementations
- Parameter tuning strategies and default selections
- Quality metric calculations and interpretation
- Performance optimization for real-time interaction

**Case Study Analysis (1.5 pages)**
- Detailed analysis of each dataset using the dashboard
- Comparison of method performance across different data types
- Parameter sensitivity analysis and recommendations
- Insights discovered through interactive exploration

**User Interface Design and Evaluation (1 page)**
- Design rationale for interactive controls and layout
- Usability considerations and accessibility features
- Performance evaluation and scalability analysis
- Future enhancements and integration possibilities

### 3. Code Repository and Documentation
Create a professional GitHub repository including:
- **Complete source code** with modular, documented architecture
- **Comprehensive README** with setup, usage, and API documentation
- **Live demo deployment** with all three datasets available
- **Data preprocessing scripts** for converting datasets to required formats
- **Parameter tuning guidelines** for different data types

---

## Evaluation Criteria

### Technical Implementation (25%)
- **Algorithm Integration:** Correct implementation of all three DR methods
- **Parameter Control:** Smooth, responsive parameter adjustment interfaces
- **Performance Optimization:** Efficient handling of real-time updates
- **Code Quality:** Clean, modular, well-documented implementation

### Visualization Design (25%)
- **Visual Clarity:** Effective encoding of high-dimensional relationships
- **Interactive Design:** Intuitive controls and responsive feedback
- **Comparative Display:** Clear side-by-side method comparisons
- **Information Density:** Optimal balance of detail and clarity

### Analysis and Insights (25%)
- **Method Understanding:** Deep insights into DR algorithm behavior
- **Parameter Sensitivity:** Thorough analysis of parameter effects
- **Quality Assessment:** Meaningful evaluation of embedding quality
- **Dataset Insights:** Domain-specific discoveries through exploration

### User Experience (15%)
- **Interface Usability:** Intuitive navigation and control layout
- **Educational Value:** Effective explanation of DR concepts
- **Performance:** Smooth interactions without lag or crashes
- **Accessibility:** Consideration for users with different abilities

### Documentation and Communication (10%)
- **Report Quality:** Clear, professional technical writing
- **Code Documentation:** Comprehensive inline and external documentation
- **Reproducibility:** Complete instructions for setup and usage
- **User Guidelines:** Clear guidance for interpreting results

---

## Bonus Opportunities (+10% each, max +20%)

### Advanced Features
- **3D Visualization:** Interactive 3D embeddings with WebGL rendering
- **Animation and Transitions:** Smooth transitions between parameter settings
- **Custom Metrics:** Implementation of additional quality measures (e.g., co-ranking matrix)

### Extended Analysis
- **Manifold Learning Methods:** Add Isomap, LLE, or other manifold techniques
- **Ensemble Embeddings:** Combine multiple DR methods for robust visualization
- **Time-series DR:** Handle temporal high-dimensional data

### User Experience Enhancements
- **Collaborative Features:** Share parameter settings and discoveries
- **Export Capabilities:** High-quality figure export and embedding data download
- **Tutorial System:** Interactive tutorial for DR method selection and tuning

---

## Submission Instructions

1. **Deploy Dashboard:** Host complete application on GitHub Pages, Netlify, or similar
2. **Create Repository:** Name it `visml-exercise5-[username]`
3. **Prepare Submission Package:**
   - Live dashboard URL with all three datasets
   - GitHub repository link with complete source code
   - Technical report (PDF format)
   - 5-7 minute video demonstration showcasing key features
4. **Submit via NYU Classes:** Upload all materials and provide links

**Late Policy:** 20% deduction per day, maximum 5 days late

---

## Resources

### Dimensionality Reduction Literature
- Van der Maaten & Hinton, "Visualizing Data using t-SNE" (2008)
- McInnes et al., "UMAP: Uniform Manifold Approximation and Projection" (2018)
- Jolliffe, "Principal Component Analysis" (2nd Edition)
- Lee & Verleysen, "Nonlinear Dimensionality Reduction" (2007)

### Technical Implementation
- [Scikit-learn Manifold Learning](https://scikit-learn.org/stable/modules/manifold.html)
- [UMAP Documentation](https://umap-learn.readthedocs.io/)
- [t-SNE FAQ and Tips](https://distill.pub/2016/misread-tsne/)
- [D3.js Scales and Axes](https://observablehq.com/@d3/learn-d3-scales)

### Quality Metrics and Evaluation
- Venna & Kaski, "Neighborhood Preservation in Nonlinear Projection Methods" (2006)
- Gracia et al., "A Comparison of Extrinsic Clustering Evaluation Metrics" (2014)
- Lueks et al., "How to Evaluate Dimensionality Reduction?" (2011)

### Visualization Examples
- [Embedding Projector](https://projector.tensorflow.org/)
- [UMAP Interactive Explorer](https://github.com/GrantRVD/umap-explorer)
- [Distill t-SNE Examples](https://distill.pub/2016/misread-tsne/)

---

## Example Code Snippets

### Real-time Parameter Update
```javascript
class DimensionalityReductionDashboard {
    constructor(container) {
        this.container = container;
        this.methods = ['pca', 'tsne', 'umap'];
        this.setupParameterControls();
    }
    
    async updateParameters(method, parameters) {
        // Show loading indicator
        this.showLoading(method);
        
        // Compute new embedding
        const embedding = await this.computeEmbedding(method, parameters);
        
        // Update visualization
        this.updateEmbeddingView(method, embedding);
        
        // Calculate and display quality metrics
        const metrics = this.calculateQualityMetrics(embedding);
        this.updateMetricsDisplay(method, metrics);
    }
}
```

### Quality Metrics Visualization
```javascript
function drawQualityMetrics(metrics, container) {
    const svg = d3.select(container)
        .append('svg')
        .attr('width', 400)
        .attr('height', 300);
        
    // Create bar chart for different quality measures
    const measures = ['trustworthiness', 'continuity', 'stress'];
    const scale = d3.scaleLinear().domain([0, 1]).range([0, 200]);
    
    svg.selectAll('.metric-bar')
        .data(measures)
        .enter()
        .append('rect')
        .attr('class', 'metric-bar')
        .attr('x', 50)
        .attr('y', (d, i) => i * 40 + 20)
        .attr('width', d => scale(metrics[d]))
        .attr('height', 30)
        .style('fill', '#69b3a2');
}
```

---

## Getting Help

- **Discord Support:** Use #exercise5 channel for technical questions and discussions
- **Office Hours:** Available for algorithm implementation and optimization help
- **Mathematical Concepts:** TA support for understanding DR algorithm mathematics
- **Performance Issues:** Help available for optimizing real-time parameter updates
- **Visualization Design:** Feedback on effective DR result presentation

---

## Academic Integrity

- **Individual Work:** Complete this assignment independently
- **Library Usage:** Properly credit any DR libraries or implementations used
- **Code Attribution:** Cite external code snippets and visualization examples
- **Original Analysis:** Your insights and interface design must be original
- **Dataset Usage:** Only use provided datasets or clearly cite external sources

---

*Questions? Post in Discord #exercise5 channel or contact the teaching team.*