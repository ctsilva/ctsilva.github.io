---
title: "DS-GA 3001: Special Topics in Data Science - Visualization for Machine Learning"
permalink: /2026-VisML-CDS/
author_profile: true
---

**Instructor:** Claudio Silva (csilva@nyu.edu)  
**Session Leader (Labs) & Grader:** Bhavya Matam (bm3792@nyu.edu)  
**Lecture (DS-GA 3001.001):** Tuesdays 4:55 PM - 6:55 PM  
**Lab (DS-GA 3001.002):** Tuesdays 7:10 PM - 8:00 PM (same room, right after the lecture)  
**Classroom:** 60 Fifth Avenue, Room 150, Washington Square Campus (both sessions)  
**Semester:** September 8 - December 8, 2026

[Course Syllabus](/2026-VisML-CDS/syllabus) | [Detailed Schedule](/2026-VisML-CDS/schedule) | [Resources](/2026-VisML-CDS/resources)

## Announcements

**Welcome to Fall 2026!** We meet Tuesdays: lecture 4:55-6:55 PM, then lab 7:10-8:00 PM in the same room. Our first class is Tuesday, September 8. All 14 Tuesday sessions meet as scheduled — Labor Day and Fall Break both fall on Mondays, so this course loses no meetings. Materials will be posted here as the semester progresses.

⚠️ **Work in progress:** This site is **tentative** and is being actively updated ahead of and during the semester. Schedule, lab sessions, assignments, and posted materials may all change. Students will be notified via Discord and course announcements.

## Schedule

### Week 1 — Tuesday, Sept 8
- **Topics:** Course Introduction, Syllabus, Introduction to Visualization, Hands-on Vega-Lite
- **Materials:**
  - [Course Introduction & Syllabus](/2026-VisML-CDS/slides/week2-intro.html)
  - [Information Visualization Introduction](/2026-VisML-CDS/slides/week2-infovis.html)
  - [Vega-Lite Lab](/2026-VisML-CDS/labs/week2-lab.html)
- **Assignment:** TBD

### Week 2 — Tuesday, Sept 15
- **Topics:** Perception for Design, Color Theory for Visualization
- **Materials:**
  - [Perception for Design](/2026-VisML-CDS/slides/week3-perception.html)
  - [Color Theory for Visualization](/2026-VisML-CDS/slides/week3-color.html)
  - [Lab: Perception and Color in Practice](/2026-VisML-CDS/labs/week3-slides.html)
- **Action Item:** Form project teams this week

### Week 3 — Tuesday, Sept 22
- **Topics:** Model Assessment and Evaluation
- **Materials:**
  - [Model Assessment and Evaluation](/2026-VisML-CDS/slides/week4-model-assessment.html)
  - Lab: Model Assessment in Practice — *materials in preparation, to be posted*
- **Recommended Readings:**
  - [Squares: Supporting Interactive Performance Analysis for Multiclass Classifiers](/2026-VisML-CDS/refs/Ren_Amershi_Lee_Suh_Williams_2016_Squares_Interactive_Performance_Analysis.pdf) (Ren et al., 2016)
  - [Neo: Generalizing Confusion Matrix Visualization to Hierarchical and Multi-Output Labels](/2026-VisML-CDS/refs/Goertler_Hohman_Moritz_2022_Neo_Confusion_Matrix.pdf) (Görtler et al., 2022)
- **Content:**
  - Confusion Matrices and ROC Curves
  - Visual Analytics Systems for Model Performance
  - Calibration Theory and Practice

### Week 4 — Tuesday, Sept 29
- **Topics:** Visualization for White-box Machine Learning Models
- **Materials:**
  - [White-box Model Interpretation](/2026-VisML-CDS/slides/week5-white-box.html)
  - [Lab: Interpretable ML Methods](/2026-VisML-CDS/labs/week5-lab.html)
- **Recommended Readings:**
  - [A Partition-Based Framework for Building and Validating Regression Models](https://doi.org/10.1109/TVCG.2013.125) (Mühlbacher & Piringer, 2013) - **Best Paper Award, IEEE VAST 2013**
  - [Gamut: A Design Probe to Understand How Data Scientists Understand Machine Learning Models](https://doi.org/10.1145/3290605.3300809) (Hohman et al., 2019)
  - [BaobabView: Interactive Construction and Analysis of Decision Trees](https://doi.org/10.1109/VAST.2011.6102453) (van den Elzen & van Wijk, 2011)
- **Content:**
  - Linear Regression and Visual Analytics Systems
  - Generalized Additive Models (GAMs) and Explainable Boosting Machines
  - Tree-based Models and Visualization Techniques
  - Decision Rules and Global Surrogate Models
- **Milestone:** Project Proposal (4-page writeup) due

### Week 5 — Tuesday, Oct 6
- **Topics:** Black-box Model Interpretation, Project Discussion
- **Materials:**
  - [Black-box Model Interpretation](/2026-VisML-CDS/slides/week6-black-box.html)
  - [Lab: Black-box Explainability Methods](/2026-VisML-CDS/labs/week6-lab/VisML-Lab-Week6-slides.html)
  - [Project Discussion](/2026-VisML-CDS/slides/week6-project-discussion.html)
- **Recommended Readings:**
  - ["Why Should I Trust You?" Explaining the Predictions of Any Classifier](https://doi.org/10.1145/2939672.2939778) (Ribeiro et al., 2016, KDD)
  - [SHAP Book: A Unified Approach to Interpreting Model Predictions](https://christophmolnar.com/books/shap) (Molnar, 2024)
- **Content:**
  - Partial Dependence Plots (PDP)
  - Local Interpretable Model-agnostic Explanations (LIME)
  - SHAP (SHapley Additive exPlanations)
  - Project Ideas and Guidelines

### Week 6 — Tuesday, Oct 13
- **Topics:** Clustering and Dimensionality Reduction, Default Project Details
- **Materials:**
  - [Clustering and Dimensionality Reduction](/2026-VisML-CDS/slides/week8-clustering.html)
  - [Default Project: Visual Analytics for AI-Generated Urban Infrastructure Maps](/2026-VisML-CDS/slides/default-project.html)
  - [Lab: Dimensionality Reduction](/2026-VisML-CDS/labs/week7-lab/VisML-Lab-Week7-slides.html)
- **Recommended Readings:**
  - [Wolfram Clustering Tutorial](https://www.wolfram.com/language/introduction-machine-learning/clustering/) - **Required**
  - [A Tutorial on Principal Component Analysis](https://arxiv.org/abs/1404.1100) (Shlens, 2014)
  - [Scikit-learn PCA User Guide](https://scikit-learn.org/stable/modules/decomposition.html#pca)
  - [Mapping the walk: A scalable computer vision approach for generating sidewalk network datasets from aerial imagery](https://doi.org/10.1016/j.compenvurbsys.2023.101950) (Hosseini et al., 2023)
- **Content:**
  - Introduction to Unsupervised Learning
  - K-means Clustering and DBSCAN
  - The Manifold Hypothesis and Intrinsic Dimensionality
  - Principal Component Analysis (PCA)
  - Eigenvectors, Eigenvalues, and Covariance Matrices
  - Singular Value Decomposition (SVD)
  - Local Linear Embedding (LLE)
  - Default Project Overview and Ideas

### Week 7 — Tuesday, Oct 20
- **Topics:** Dimensionality Reduction (continued)
- **Materials:**
  - [Dimensionality Reduction (continued)](/2026-VisML-CDS/slides/week9-dimensionality.html)
  - [Lab: Dimensionality Reduction in Practice](/2026-VisML-CDS/labs/week8-lab/VisML-Lab-Week8-slides.html)
- **Recommended Readings:**
  - [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/) (Wattenberg, Viégas, Johnson, 2016) - **Required**
  - [Visualizing Data using t-SNE](https://www.jmlr.org/papers/v9/vandermaaten08a.html) (van der Maaten & Hinton, 2008)
  - [UMAP: Uniform Manifold Approximation and Projection](https://arxiv.org/abs/1802.03426) (McInnes, Healy, Melville, 2018)
  - [Understanding UMAP](https://pair-code.github.io/understanding-umap/) (Coenen & Pearce)
- **Content:**
  - t-SNE: Theory and Pitfalls
  - UMAP: Uniform Manifold Approximation and Projection
  - Topomap: Topologically-Constrained Dimensionality Reduction
  - Interactive Dimensionality Reduction Techniques
- **Milestone:** Project Update (1-page writeup) due

### Week 8 — Tuesday, Oct 27
- **Topics:** Deep Learning Visualization Fundamentals
- **Materials:**
  - [Deep Learning Visualization](/2026-VisML-CDS/slides/week7-deep-learning.html)
  - [Lab: Deep Learning Visualization](/2026-VisML-CDS/labs/week9-lab/VisML-Lab-Week9-slides.html)
- **Recommended Readings:**
  - [Understanding Deep Learning](https://udlbook.github.io/udlbook/) (Prince, 2023) - Chapters 2-4
  - [TensorFlow Playground](https://playground.tensorflow.org) - Interactive neural network visualization
  - [CNN Explainer](https://poloclub.github.io/cnn-explainer/) - Interactive CNN visualization
- **Content:**
  - Deep Learning Terminology and Foundations
  - Linear Models and Loss Functions
  - Shallow Neural Networks and Activation Functions
  - Deep Neural Networks and Composition
  - Interactive Visualization Tools

### Week 9 — Tuesday, Nov 3
- **Topics:** Visualization for NLP and Large Language Models
- **Materials:**
  - [NLP and LLM Visualization](/2026-VisML-CDS/slides/week11-nlp.html)
  - [Lab: NLP Visualization](/2026-VisML-CDS/labs/week11-lab/VisML-Lab-Week11-slides.html)
- **Recommended Readings:**
  - [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/)
  - [Efficient estimation of word representations in vector space](https://arxiv.org/abs/1301.3781)
  - [Attention is All You Need](https://arxiv.org/abs/1706.03762) (Vaswani et al., 2017) - **Foundational**
  - [BertViz: A Tool for Visualizing Multi-Head Self-Attention](https://arxiv.org/abs/1908.08593) (Vig, 2019)
  - [LSTMVis: A Tool for Visual Analysis of Hidden State Dynamics in RNNs](https://doi.org/10.1109/TVCG.2017.2744158) (Strobelt et al., 2017)
  - [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165) (Brown et al., 2020) - GPT-3 Paper
  - [Transformer Explainer](https://poloclub.github.io/transformer-explainer/) - Interactive Transformer visualization
- **Content:**
  - NLP basics
  - General Text Visualization
  - Model agnostic explanation
  - Examples of RNN Visualization
  - Examples of LLM Visualization

### Week 10 — Tuesday, Nov 10
- **Topics:** Topological Data Analysis
- **Materials:**
  - [Topological Data Analysis](/2026-VisML-CDS/slides/week10-tda.html)
  - [Lab: TDA in Practice](/2026-VisML-CDS/labs/week12-lab/VisML-Lab-Week12-slides.html)
- **Recommended Readings:**
  - [An Introduction to Topological Data Analysis: Fundamental and Practical Aspects for Data Scientists](https://doi.org/10.3389/frai.2021.667963) (Chazal & Michel, 2021) - **Required**
  - [Computational Topology: An Introduction](https://doi.org/10.1090/mbk/069) (Edelsbrunner & Harer, 2022)
  - [Topological Data Analysis for Machine Learning](https://bastian.rieck.me/talks/ecml_pkdd_2020/) (Rieck, 2020 Tutorial)
- **Content:**
  - Introduction to Topology and Betti Numbers
  - Persistence Diagrams and Homology
  - Simplicial Complexes and Vietoris-Rips Construction
  - The Mapper Algorithm
  - Applications in Biology, Chemistry, and Machine Learning
  - TDA Software: GUDHI, scikit-tda, Ripser, KeplerMapper

### Week 11 — Tuesday, Nov 17
- **Topics:** TBA
- **Materials:** *To be posted*

### Week 12 — Tuesday, Nov 24
- **Topics:** TBA
- **Materials:** *To be posted*

### Week 13 — Tuesday, Dec 1
- **Topics:** Final Project Presentations I

### Week 14 — Tuesday, Dec 8
- **Topics:** Final Project Presentations II and Course Wrap-up

## Assignments

### Weekly Assignments (50% of grade)
- Assignments will be posted as the semester progresses
- Programming exercises will be given throughout the first half of the semester

### Research Project (45% of grade)
- **Team formation** - *Week 2 (Sept 15)*
- **Project Proposal** (4-page writeup) - *Week 4 (Sept 29)* - 10%
- **Project Updates** (1-page writeup) - *Week 7 (Oct 20)* - 10%
- **Final Project** (8-page writeup + presentation) - *Weeks 13-14 (Dec 1 & 8)*; report due Dec 14 - 25%

### Class Participation (5% of grade)

## Quick Links

- **Discord:** Invite link to be posted before the first class
- **Brightspace:** [Course materials and submissions]
- **Office Hours:** Fridays 1:30-2:30 PM, 370 Jay Street, Room 1153

## Course Description

This course explores the intersection of visualization and machine learning, focusing on how visualization techniques can help understand, debug, and improve machine learning models. Students will learn to create visual analytics systems for model assessment, feature analysis, and result interpretation. Topics include visualization for model performance, feature importance, clustering, dimensionality reduction, deep learning architectures, and interpretable AI.

## Prerequisites

- Solid programming skills (Python and JavaScript)
- Basic knowledge of machine learning concepts
- Familiarity with web technologies (HTML, CSS) helpful but not required
