---
title: "Exercise 1: Visualization Critique"
permalink: /2025-VisML-CSE/assignments/exercise1
author_profile: true
---

# Exercise 1: Visualization Critique

**CS-GY 9223: Visualization for Machine Learning - Fall 2025**

**Released:** September 8, 2025  
**Due:** September 15, 2025 (11:59 PM EST)  
**Weight:** 5% of final grade

---

## Overview

This assignment introduces you to critical evaluation of machine learning visualizations. You will analyze existing visualization tools and techniques, developing skills to identify effective design choices and areas for improvement. This critical analysis foundation will inform your design decisions in subsequent assignments.

## Learning Objectives

By completing this exercise, you will:
- Develop critical analysis skills for visualization evaluation
- Understand design principles specific to ML visualization
- Practice identifying strengths and weaknesses in existing tools
- Learn to articulate design rationale and improvement suggestions
- Gain familiarity with the current landscape of ML visualization tools

---

## Assignment Tasks

### Task 1: Tool Selection and Analysis (60%)

Choose **three (3) different** machine learning visualization tools or systems from the provided list or find your own (with instructor approval). For each tool, conduct a comprehensive analysis covering:

#### Technical Analysis
- **Purpose and Scope:** What ML tasks does it address?
- **Data Types:** What kinds of data does it visualize?
- **Interaction Capabilities:** How can users interact with the visualizations?
- **Technical Implementation:** What technologies does it use?

#### Design Evaluation
- **Visual Encoding:** How effectively does it map data to visual elements?
- **Color Usage:** Is color used effectively and accessibly?
- **Layout and Composition:** How well is screen space utilized?
- **Affordances:** Are interaction possibilities clear to users?

#### Usability Assessment
- **User Experience:** Is it intuitive to use?
- **Learning Curve:** How much training is required?
- **Error Handling:** How does it handle edge cases or errors?
- **Performance:** Does it handle large datasets effectively?

### Task 2: Comparative Analysis (25%)

Compare the three tools across common dimensions:
- **Strengths and Weaknesses:** What does each tool do well/poorly?
- **Use Cases:** When would you choose each tool?
- **Target Audiences:** Who are the intended users?
- **Innovation:** What novel approaches does each tool take?

### Task 3: Design Recommendations (15%)

For **one** of the analyzed tools, propose specific improvements:
- **Identify 3-5 specific problems** with the current design
- **Propose concrete solutions** with design rationale
- **Consider implementation feasibility** and trade-offs
- **Sketch or mockup** proposed changes (hand-drawn or digital)

---

## Suggested Tools

### Model Interpretation Tools
- **LIME** ([GitHub](https://github.com/marcotcr/lime))
- **SHAP** ([GitHub](https://github.com/slundberg/shap))
- **What-If Tool** ([Google AI](https://pair-code.github.io/what-if-tool/))
- **Alibi Explain** ([Seldon](https://docs.seldon.io/projects/alibi/en/stable/))

### Neural Network Visualization
- **TensorBoard** ([TensorFlow](https://www.tensorflow.org/tensorboard))
- **Netron** ([GitHub](https://github.com/lutzroeder/netron))
- **ConvNetJS** ([Stanford](https://cs.stanford.edu/people/karpathy/convnetjs/))
- **TensorSpace** ([GitHub](https://github.com/tensorspace-team/tensorspace))

### Dimensionality Reduction & Clustering
- **Embedding Projector** ([TensorFlow](https://projector.tensorflow.org/))
- **t-SNE Explorer** ([Distill](https://distill.pub/2016/misread-tsne/))
- **UMAP Plot** ([UMAP-learn](https://umap-learn.readthedocs.io/en/latest/plotting.html))

### General ML Dashboards
- **MLflow UI** ([MLflow](https://mlflow.org/))
- **Weights & Biases** ([W&B](https://wandb.ai/))
- **Neptune** ([Neptune.ai](https://neptune.ai/))
- **Streamlit** ML apps ([Streamlit](https://streamlit.io/))

### Research Tools
- **Manifold** ([Uber](https://github.com/uber/manifold))
- **Facets** ([Google PAIR](https://pair-code.github.io/facets/))
- **Yellowbrick** ([Scikit-learn](https://www.scikit-yb.org/en/latest/))

*You may also propose other tools not on this list with instructor approval.*

---

## Deliverables

### 1. Written Report (3-4 pages)
Submit a well-structured report in PDF format containing:

**Introduction (0.5 pages)**
- Brief overview of ML visualization importance
- Your selection criteria for chosen tools

**Tool Analyses (2-2.5 pages)**
- Detailed analysis of each tool (~0.75 pages each)
- Use screenshots and examples to illustrate points
- Follow the analysis framework provided above

**Comparative Analysis (0.5 pages)**
- Cross-tool comparison table or matrix
- Discussion of relative strengths/weaknesses

**Design Recommendations (0.5 pages)**
- Specific improvement proposals for one tool
- Include sketches or mockups
- Justify design decisions

### 2. Presentation Slides (5-8 slides)
Create slides summarizing your findings:
- Tool overview and selection rationale
- Key findings from analysis
- Most significant insights or surprises
- Top 3 design recommendations

### 3. GitHub Repository
Create a public GitHub repository containing:
- Your written report (PDF)
- Presentation slides (PDF or PowerPoint)
- Screenshots and supporting materials
- README with tool links and usage notes

---

## Evaluation Criteria

### Technical Analysis (25%)
- **Depth of Analysis:** Thorough examination of technical capabilities
- **Accuracy:** Correct understanding of tool functionality
- **Coverage:** All required aspects addressed

### Design Evaluation (25%)
- **Design Principles:** Application of visualization design principles
- **Critical Thinking:** Insightful observations about design choices
- **Visual Examples:** Effective use of screenshots and examples

### Comparative Analysis (20%)
- **Framework Consistency:** Systematic comparison approach
- **Insight Quality:** Meaningful insights about tool differences
- **Use Case Understanding:** Clear articulation of when to use each tool

### Design Recommendations (20%)
- **Problem Identification:** Clear articulation of design problems
- **Solution Quality:** Feasible and well-reasoned improvement proposals
- **Visual Communication:** Effective use of sketches/mockups

### Presentation Quality (10%)
- **Writing Clarity:** Clear, professional communication
- **Organization:** Logical structure and flow
- **Visual Design:** Effective use of formatting and visuals

---

## Submission Instructions

1. **Create GitHub Repository:** Name it `visml-exercise1-[username]`
2. **Upload Materials:** Include report PDF, slides, and supporting files
3. **Submit via NYU Classes:** Provide your GitHub repository URL
4. **Email Notification:** Send repository link to TA via Discord

**Late Policy:** 20% deduction per day, maximum 5 days late

---

## Resources

### Design Principles
- Munzner, "Visualization Analysis and Design" (Chapters 5-6)
- Tufte, "The Visual Display of Quantitative Information"
- Few, "Information Dashboard Design"

### ML Visualization Literature
- Hohman et al., "Visual Analytics in Deep Learning: An Interrogative Survey" (2018)
- Liu et al., "Towards Better Analysis of Machine Learning Models" (2017)
- Rauber et al., "Visualizing the Hidden Activity of Artificial Neural Networks" (2017)

### Online Resources
- [Visualization Analysis and Design Course](http://www.cs.ubc.ca/~tmm/vadbook/)
- [D3.js Gallery](https://observablehq.com/@d3/gallery)
- [Distill ML Visualization Articles](https://distill.pub/)

---

## Getting Help

- **Discord Questions:** Use #exercise1 channel for public discussion
- **Office Hours:** Schedule one-on-one help via Discord
- **Tool Access Issues:** Contact TA if you have trouble accessing any tools
- **Scope Questions:** Ask early if unsure about tool selection or analysis depth

---

## Academic Integrity

- **Individual Work:** This is an individual assignment
- **Tool Exploration:** You must actually use/explore each tool, not just read about it
- **Citation Required:** Properly cite all sources, including tool documentation
- **Original Analysis:** Your insights and recommendations must be original

---

*Questions? Post in Discord #exercise1 channel or contact the teaching team.*