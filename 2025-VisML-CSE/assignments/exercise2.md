---
title: "Exercise 2: Color Palette Design"
permalink: /2025-VisML-CSE/assignments/exercise2
author_profile: true
---

# Exercise 2: Color Palette Design

**CS-GY 9223: Visualization for Machine Learning - Fall 2025**

**Released:** September 15, 2025  
**Due:** September 22, 2025 (11:59 PM EST)  
**Weight:** 5% of final grade

---

## Overview

Color is one of the most powerful yet challenging aspects of data visualization. This assignment focuses on creating effective color palettes specifically for machine learning data visualization. You will learn about color theory, perceptual uniformity, accessibility, and cultural considerations while building practical color tools.

## Learning Objectives

By completing this exercise, you will:
- Understand color theory principles for data visualization
- Create perceptually uniform and accessible color palettes
- Implement color scales using D3.js color interpolation
- Test color palettes for accessibility and cultural sensitivity
- Build reusable color tools for ML visualization contexts

---

## Assignment Tasks

### Task 1: Color Theory Research (20%)

Research and document color theory principles relevant to ML visualization:

#### Perceptual Color Spaces
- **CIELAB and CIELUV:** Understand perceptually uniform color spaces
- **HCL (Hue-Chroma-Luminance):** Learn why HCL is better than HSL/HSV
- **Color Difference Metrics:** Research CIEDE2000 and other perceptual distance measures

#### ML-Specific Considerations
- **Class Distinction:** Colors for categorical data (classification classes)
- **Continuous Gradients:** Color scales for continuous values (probabilities, scores)
- **Diverging Scales:** Colors for data with meaningful center points
- **Multi-dimensional Color:** Using color for multiple variables simultaneously

### Task 2: Accessibility Analysis (20%)

Evaluate color accessibility across different conditions:

#### Color Vision Deficiency Testing
- Test palettes for protanopia, deuteranopia, and tritanopia
- Use simulation tools to verify accessibility
- Implement alternative encodings (patterns, shapes) where needed

#### Contrast and Readability
- Ensure sufficient contrast ratios (WCAG 2.1 guidelines)
- Test readability across different backgrounds
- Consider low-vision and aging-related vision changes

#### Cultural Sensitivity
- Research color meanings across cultures
- Consider global audience implications
- Avoid problematic color associations

### Task 3: Palette Implementation (40%)

Create four distinct color palettes using D3.js:

#### 1. Sequential Palette
- **Use Case:** Model confidence scores, probabilities, feature importance
- **Requirements:** Perceptually uniform progression, colorblind-friendly
- **Implementation:** D3 interpolation with custom domain mapping

#### 2. Diverging Palette  
- **Use Case:** Model prediction errors, feature correlations, residuals
- **Requirements:** Clear neutral center, symmetric progression
- **Implementation:** Two-sided color interpolation

#### 3. Categorical Palette
- **Use Case:** Classification classes, model types, algorithm families
- **Requirements:** Maximally distinguishable colors, accessible
- **Implementation:** Discrete color selection with perceptual spacing

#### 4. Multi-Class Confusion Matrix Palette
- **Use Case:** Confusion matrix visualization with 3+ classes
- **Requirements:** Diagonal emphasis, off-diagonal distinction
- **Implementation:** 2D color mapping with perceptual gradients

### Task 4: Interactive Color Tool (20%)

Build an interactive web application that demonstrates your palettes:

#### Features Required
- **Live Palette Editor:** Adjust parameters and see real-time updates
- **Accessibility Simulator:** Toggle different types of color vision deficiency
- **Export Functionality:** Generate CSS, D3.js, and hex code outputs
- **Comparison Tool:** Side-by-side palette comparison

#### ML Data Visualization Examples
- Show each palette applied to realistic ML visualization scenarios
- Include at least one confusion matrix, one ROC curve, and one feature importance plot
- Demonstrate how color choices affect interpretation

---

## Technical Requirements

### Implementation Stack
- **D3.js v7+** for color interpolation and scaling
- **HTML5/CSS3** for interface design
- **JavaScript ES6+** for application logic
- **SVG** for scalable color visualization

### Color Libraries to Explore
- **D3-scale-chromatic:** Built-in D3 color schemes
- **Chroma.js:** Color manipulation library
- **Colorbrewer:** Cartographic color schemes
- **Viz Palette:** ML-specific color tools

### Accessibility Testing Tools
- **Coblis:** Color blindness simulator
- **Contrast Checker:** WCAG contrast validation
- **Colour Contrast Analyser:** Comprehensive accessibility testing

---

## Deliverables

### 1. Interactive Web Application
Host a live demonstration of your color tool with:
- **Four implemented color palettes** with customization controls
- **Accessibility testing features** (simulation, contrast checking)
- **ML visualization examples** showing palettes in context
- **Export functionality** for developers to use your palettes

### 2. Technical Report (3-4 pages)
Submit a comprehensive report covering:

**Color Theory Background (1 page)**
- Summary of perceptual color space principles
- ML-specific color requirements
- Accessibility and cultural considerations

**Palette Design Rationale (1.5 pages)**
- Detailed explanation of each palette design
- Perceptual testing results and validation
- Trade-offs and design decisions

**Implementation Details (1 page)**
- Technical approach and challenges
- D3.js implementation strategies
- Performance and browser compatibility

**Evaluation and Testing (0.5 pages)**
- Accessibility testing results
- User feedback (if collected)
- Comparative analysis with existing tools

### 3. Code Repository
Create a well-documented GitHub repository with:
- **Complete source code** with clear organization
- **README** with setup and usage instructions
- **Color palette JSON exports** for reuse
- **Live demo link** (GitHub Pages or similar)

---

## Evaluation Criteria

### Color Theory Application (25%)
- **Perceptual Uniformity:** Palettes show smooth perceptual progression
- **Appropriate Color Spaces:** Correct use of HCL/LAB color spaces
- **ML Context Awareness:** Colors suit specific ML visualization needs

### Accessibility Implementation (25%)
- **Color Vision Deficiency:** Palettes work for all types of color blindness
- **Contrast Standards:** Meet or exceed WCAG 2.1 guidelines
- **Alternative Encodings:** Provide non-color distinctions where needed

### Technical Quality (25%)
- **D3.js Implementation:** Effective use of D3 color functions
- **Code Organization:** Clean, modular, well-documented code
- **Performance:** Smooth interactions and fast rendering

### Interactive Tool Design (15%)
- **User Experience:** Intuitive interface for palette exploration
- **Feature Completeness:** All required functionality implemented
- **Visual Design:** Professional appearance and layout

### Documentation Quality (10%)
- **Report Clarity:** Clear explanation of design decisions
- **Code Documentation:** Comprehensive inline and README documentation
- **Reproducibility:** Others can build and extend your work

---

## Bonus Opportunities (+10% each, max +20%)

### Advanced Color Features
- **Perceptual Color Difference Metrics:** Implement CIEDE2000 calculations
- **Dynamic Palette Generation:** Algorithm to generate palettes automatically
- **3D Color Space Visualization:** Interactive 3D color space exploration

### ML-Specific Innovations
- **Attention-Weighted Coloring:** Color scales based on model attention
- **Uncertainty-Aware Palettes:** Incorporate prediction uncertainty into color
- **Class-Imbalance Palettes:** Specialized colors for imbalanced datasets

---

## Submission Instructions

1. **Deploy Web Application:** Host on GitHub Pages, Netlify, or similar
2. **Create GitHub Repository:** Name it `visml-exercise2-[username]`
3. **Submit Materials:**
   - Live application URL
   - GitHub repository link
   - Technical report (PDF)
4. **Submit via NYU Classes:** Provide all links and files

**Late Policy:** 20% deduction per day, maximum 5 days late

---

## Resources

### Color Theory References
- Ware, "Information Visualization" Chapter 4 (Color)
- Munzner, "Visualization Analysis and Design" Chapter 10
- Healey & Enns, "Attention and Visual Memory in Visualization and Computer Graphics"

### Technical Documentation
- [D3-scale-chromatic Documentation](https://github.com/d3/d3-scale-chromatic)
- [Chroma.js Documentation](https://gka.github.io/chroma.js/)
- [ColorBrewer 2.0](https://colorbrewer2.org/)

### Accessibility Guidelines
- [WCAG 2.1 Color Guidelines](https://www.w3.org/WAI/WCAG21/Understanding/use-of-color.html)
- [WebAIM Color Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [Color Universal Design](https://jfly.uni-koeln.de/color/)

### ML Visualization Examples
- [Distill Color Articles](https://distill.pub/2017/research-debt/)
- [Observable Color Notebooks](https://observablehq.com/collection/@d3/color)
- [TensorBoard Color Usage](https://www.tensorflow.org/tensorboard)

---

## Example Applications

### Sequential Palette Example
```javascript
const confidenceScale = d3.scaleSequential()
    .domain([0, 1])
    .interpolator(d3.interpolateViridis);

// Apply to confidence heatmap
d3.selectAll(".confidence-cell")
    .style("fill", d => confidenceScale(d.confidence));
```

### Categorical Palette Example
```javascript
const classColors = d3.scaleOrdinal()
    .domain(["class_a", "class_b", "class_c"])
    .range(["#1f77b4", "#ff7f0e", "#2ca02c"]);

// Apply to scatter plot
d3.selectAll(".data-point")
    .style("fill", d => classColors(d.predicted_class));
```

---

## Getting Help

- **Discord Questions:** Use #exercise2 channel for public discussion
- **Color Theory Help:** Office hours available for conceptual questions
- **Technical Issues:** TA available for D3.js implementation help
- **Accessibility Testing:** Guidance available for testing tools and procedures

---

## Academic Integrity

- **Individual Work:** Complete this assignment independently
- **Resource Citation:** Cite all color theory sources and tools used
- **Code Attribution:** Credit any external code libraries or examples
- **Original Design:** Your color palettes must be originally designed

---

*Questions? Post in Discord #exercise2 channel or contact the teaching team.*