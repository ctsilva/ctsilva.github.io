---
title: "CS-GY 6313: Information Visualization - Fall 2025"
permalink: /2025-InfoVis-CSE/
author_profile: true
---

**Instructor:** Claudio Silva (csilva@nyu.edu)
**TA (Labs):** Ryan Kim ([rkim.dev](https://www.rkim.dev))
**Grader:** Hashmmath Shaik (hs5544@nyu.edu)
**Meeting Times:** Fridays 11:00 AM - 1:30 PM
**Classroom:** Jacobs Hall, Room 215, Brooklyn Campus

[Course Syllabus](/2025-InfoVis-CSE/syllabus) | [Detailed Schedule](/2025-InfoVis-CSE/schedule) | [Resources](/2025-InfoVis-CSE/resources)

## Announcements

**Week 13 Materials Ready (Nov 26):** Visualizing Network Data lecture is now available! Comprehensive coverage of network fundamentals, force-directed layouts, matrix representations, and tree visualizations (treemaps, sunburst/icicle plots). See [slides](/2025-InfoVis-CSE/slides/week13-network-data.html).

**Week 12 Materials Ready (Nov 21):** Clustering and Dimensionality Reduction lecture is now available! Covers K-means, hierarchical clustering, PCA, t-SNE, and UMAP with critical visualization principles. See [slides](/2025-InfoVis-CSE/slides/week12-clustering-dimreduction.html).

**Week 11 Materials Ready (Nov 13):** Visualizing Time-Oriented Data lecture is now available! Comprehensive coverage of temporal data types, time structures, line chart best practices (Banking to 45°), interaction techniques, heat maps, periodic patterns, horizon charts, and sparklines. See [slides](/2025-InfoVis-CSE/slides/week11-temporal-data.html).

*Course materials will be posted as the semester progresses*

## Upcoming Classes

### Week 1 (Sept 5) - Introduction and Evaluation
- **Slides:** [Course Introduction & Syllabus](/2025-InfoVis-CSE/slides/week1-syllabus.html) | [Lab: Observable & Vega-Lite](/2025-InfoVis-CSE/labs/week1-lab.html)
- **Topics:** Course overview, What is visualization?, Evaluation frameworks
- **Lab:** Setup Observable accounts, Create first Vega-Lite charts
- **Assignment:** Exercise 1 - Visualization critique and basic Vega-Lite charts (due Sept 11)
- **Readings:** [Card & Mackinlay (1999) - Using Vision to Think](/2025-InfoVis-CSE/refs/Card_Mackinlay_Shneiderman_1999_Using_Vision_to_Think_Chapter1.pdf)

### Week 2 (Sept 12) - Analytical Questions and Data Transformation
- **Slides:** [Analytical Questions and Data Transformation](/2025-InfoVis-CSE/slides/week2-data-transformation.html) | [Lab: Intro to Vega-Lite Data Transformations...](/2025-InfoVis-CSE/labs/week2-lab.html)
- **Topics:** Visual queries, Data types, Transformation operations
- **Lab:** Vega-Lite data transformations, Working with real datasets
- **Assignment:** Exercise 2 - Data questions and transformations (due Sept 18)
- **Readings:** [Shneiderman (1996) - The Eyes Have It](/2025-InfoVis-CSE/refs/Shneiderman_1996_The_Eyes_Have_It.pdf); [Wickham (2014) - Tidy Data](/2025-InfoVis-CSE/refs/Wickham_2014_Tidy_Data.pdf)

### Week 3 (Sept 19) - Fundamental Graphs and Visual Encoding
- **Slides:** [Fundamental Graphs and Visual Encoding](/2025-InfoVis-CSE/slides/week3-fundamental-graphs.html) | [Lab: Fundamental Graphs and Visual Encoding](/2025-InfoVis-CSE/labs/week3-lab.html)
- **Topics:** Five fundamental chart types, Marks and channels, Expressiveness and effectiveness, Scale choices
- **Lab:** Chart comparison and design exercises, Scale choice scenarios
- **Assignment:** Exercise 3 - Chart design and encoding alternatives (due Sept 25)
- **Readings:** Tufte Ch 1-2 (Graphical Excellence & Integrity)

### Week 4 (Sept 26) - Visual Perception and D3 Foundations
- **Slides:** [Visual Perception and D3 Foundations](/2025-InfoVis-CSE/slides/week4-perception.html) | [Lab: First D3 programming session, DOM manipulation, Data binding](/2025-InfoVis-CSE/labs/week4-lab.html)
- **Topics:** Pre-attentive processing, Gestalt principles, Perceptual accuracy, D3.js introduction
- **Lab:** First D3 programming session, DOM manipulation, Data binding
- **Assignment:** Exercise 4 - Perception-based design + D3 implementation (due Oct 2)
- **Readings:** Franconeri et al. (2021); Kennedy Elliott - 39 Studies
- **Optional Reference:** *Visual Thinking for Information Design* (2nd Ed.) by Colin Ware - Chapters on perception

### Week 5 (Oct 3) - Color Theory and D3 Scales
- **Slides:** [Color Theory and D3 Scales](/2025-InfoVis-CSE/slides/week5-color.html) | [Lab: Color scale exercises, Choropleth maps, Accessibility testing](/2025-InfoVis-CSE/labs/week5-lab.html)
- **Topics:** Color perception (biology/physics), Color spaces (RGB, HSL, LAB), Sequential/diverging/categorical scales, Color accessibility, D3 scale implementation
- **Lab:** Color scale exercises, Choropleth maps, Accessibility testing
- **Assignment:** Exercise 5 - Color scale design and implementation (due Oct 9)
- **Required Readings:**
  - [Which Color Scale to Use](https://blog.datawrapper.de/which-color-scale-to-use-in-data-vis/) - Lisa Charlotte Rost
  - [Modeling Color Difference](https://doi.org/10.1109/TVCG.2017.2744359) - Szafir (2018)
  - [D3 Scale Chromatic](https://observablehq.com/@d3/color-schemes) - Observable notebook
- **Optional Reference:** *Visual Thinking for Information Design* (2nd Ed.) by Colin Ware - Chapters on color

### Week 6 (Oct 10) - Group Projects and Design Ethics
- **Slides:** [Group Projects](/2025-InfoVis-CSE/slides/week6-group-projects.html) | [Lab: Intro to Interactions and Deceptive Visualizations](/2025-InfoVis-CSE/labs/week6-lab.html)
- **Topics:** Group project overview, 5 milestones (Proposal through Final), Team formation, Dataset selection, Deceptive visualization and ethics
- **Lab:** Team formation activities, Dataset exploration, Project brainstorming
- **Action Items:**
  - Form teams by Oct 17 (use Discord #project-teams)
  - Browse datasets for project ideas
  - Exercise 6 - Misleading vs. honest visualization (due Oct 16)
  - **Project Proposal due Oct 20**
- **Required Readings:**
  - Tufte Ch 2 - Graphical Integrity
  - [Misinformed by Visualization](https://arxiv.org/pdf/2104.14332.pdf) - Lo, Gupta & Shigyo (EuroVis 2022)

### Week 7 (Oct 17) - Interaction in Visualization
- **Slides:** [Interactivity in Information Visualization](/2025-InfoVis-CSE/slides/week7-interaction.html) | [Lab: Building Interactive Visualizations](/2025-InfoVis-CSE/labs/week7-lab.html)
- **Topics:** Why interaction matters, Shneiderman's Mantra, 12 interactive dynamics (Visualize, Filter, Sort, Derive, Select, Navigate, Coordinate, Organize, Record, Annotate, Share, Guide), Modern interaction frameworks (Libra)
- **Lab:** Interactive D3 techniques, Brushing and linking, Dynamic queries
- **Assignment:** Exercise 7 - Interactive visualization design and implementation (due Oct 23)
- **Required Readings:**
  - [Shneiderman (1996) - The Eyes Have It](/2025-InfoVis-CSE/refs/Shneiderman_1996_The_Eyes_Have_It.pdf)
  - [Heer & Shneiderman (2012) - Interactive Dynamics for Visual Analysis](/2025-InfoVis-CSE/refs/Heer_Shneiderman_2012_Interactive_Dynamics_Visual_Analysis.pdf)
- **Recommended Readings:**
  - [Yi et al. (2007) - Toward a Deeper Understanding of Interaction](/2025-InfoVis-CSE/refs/Yi_2007_Toward_Deeper_Understanding_Interaction.pdf)
  - [Pike et al. (2009) - The Science of Interaction](/2025-InfoVis-CSE/refs/Pike_2009_Science_of_Interaction.pdf)
  - [Zhao et al. (2025) - Libra: Composable Interactions](/2025-InfoVis-CSE/refs/Zhao_2025_Libra_Composable_Interactions.pdf)

### Week 8 (Oct 24) - Foundations of Geovisualization: 2D Maps
- **Slides:** [Foundations of Geovisualization](/2025-InfoVis-CSE/slides/week8-geovis-2d-maps.html) | [Live Demo: Leaflet.js](/2025-InfoVis-CSE/slides/examples/leaflet_example.html) | **Lab:** [Plotting and Troubleshooting GeoJSON with D3](/2025-InfoVis-CSE/labs/week8-lab.html)
- **Topics:** Map projections (Mercator, Albers, Azimuthal), Choropleth pitfalls (normalization, classification, color, MAUP), Map taxonomy (choropleth, proportional symbol, cartogram, flow), GeoJSON/TopoJSON formats, Leaflet.js implementation
- **Lab:** Creating interactive geographic visualizations with Leaflet and D3
- **Assignment:** Exercise 8 - Geographic visualization with proper normalization and projection (due Oct 30)
- **Required Readings:**
  - [Datawrapper Guide to Choropleth Maps](https://www.datawrapper.de/blog/choroplethmaps)
  - [When Maps Shouldn't Be Maps](https://www.ericson.net/content/2011/10/when-maps-shouldnt-be-maps/) - Matthew Ericson (NYT)
- **Recommended Resources:**
  - [The True Size Of...](https://thetruesize.com/) - Interactive projection demo
  - [Reuters: The True Size of Africa](https://www.reuters.com/graphics/AFRICA-MAP/lgpdaqrdyvo/)
  - [Tissot's Indicatrix Explorer](https://mgimond.github.io/tissot/)
- **Supplemental Material:** GeoJSON format, TopoJSON optimization, Data classification methods (Equal Interval, Quantile, Jenks), Leaflet.js tutorial

### Week 9 (Oct 31) - Urban Visualization I: Flows, Time & Interactivity **[WIP - DRAFT]**
- **Slides:** [Urban Visualization I](/2025-InfoVis-CSE/slides/week9-urban-flows-interactivity.html) *(draft - figures needed)* | **Lab:** [Building interactive spatio-temporal visualization](/2025-InfoVis-CSE/labs/week9-lab.html)
- **Topics:** Urban data characteristics (scale, density, complexity, dynamism), Visual query models, TaxiVis case study (brushing & linking, temporal/spatial queries, origin-destination flows), Performance optimization (k-d trees, LOD rendering), Case studies (social inequality, transportation hubs, Hurricane Sandy)
- **Lab:** Building interactive spatio-temporal visualizations, Implementing linked views
- **Assignment:** Exercise 9 - Urban data exploration and visual queries (due Nov 6)
- **Required Readings:**
  - Ferreira et al. (2013) - [TaxiVis: An Interactive Visualization System for Taxi Trajectories](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/TaxiVis.pdf) - IEEE VAST 2013
  - [NYC Taxi Open Data](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- **Recommended Resources:**
  - [Hägerstrand's Space-Time Cube](https://en.wikipedia.org/wiki/Space-time_cube)
  - [Peuquet's Triad Framework](https://doi.org/10.1111/j.1538-4632.1994.tb00302.x)
- **Supplemental Material:** Visual analytics framework, Confirmatory vs exploratory analysis, Real-time data indexing

### Week 10 (Nov 7) - Urban Visualization II: 3D Form, Design & Simulation **[WIP - DRAFT]**
- **Slides:** [Urban Visualization II](/2025-InfoVis-CSE/slides/week10-urban-3d-simulation.html) *(draft - figures needed)* | **Lab:** [3D Visualization: Transformations](/2025-InfoVis-CSE/labs/week10-lab.html)
- **Topics:** Kevin Lynch's "Image of the City", 3D urban planning challenges, Urbane framework (linking 3D city models with 2D data views), Interactive impact analysis (sky exposure, shadows, viewsheds), Performance-driven design (exploring thousands of building variants), Critical reflection on when to use 3D
- **Lab:** 3D Visualization: Transformations, Matrix Operations, Model-View-Projections
- **Assignment:** Exercise 10 - 3D urban visualization and impact analysis (due Nov 13)
- **Required Readings:**
  - Poco et al. (2015) - [Exploring the Design Space of Interactive Urban Visualization](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/urbane-2015.pdf) - IEEE VIS 2015
  - Lynch (1960) - The Image of the City (excerpts)
- **Recommended Resources:**
  - [CesiumJS](https://cesium.com/platform/cesiumjs/) - 3D geospatial visualization
  - [Deck.gl](https://deck.gl/) - GPU-powered visualization layers
  - [3D Building Models](https://www.openstreetmap.org/#map=5/38.007/-95.844)
- **Supplemental Material:** When to use 2D vs 3D, Hybrid visualization approaches, Precomputation for real-time queries

### Week 11 (Nov 14) - Visualizing Time-Oriented Data
- **Slides:** [Visualizing Time-Oriented Data](/2025-InfoVis-CSE/slides/week11-temporal-data.html) | **Lab:** [Building temporal visualizations, Time series analysis with D3](/2025-InfoVis-CSE/labs/week11-lab.html)
- **Topics:** Temporal data fundamentals (event vs measurement data), Time structures (sequential, cyclic, hierarchical), Line charts and aspect ratios (Banking to 45°), Multiple time series (spaghetti plots, small multiples), Stacked area charts and limitations, Interaction techniques (semantic vs geometric zoom), Heat maps and calendar visualizations, Periodic patterns (radial layouts, spirals), Horizon charts and sparklines
- **Lab:** Building temporal visualizations, Time series analysis with D3
- **Assignment:** Exercise 11 - Temporal data visualization (due Nov 20)
- **Required Readings:**
  - Cleveland et al. (1988) - [The Shape Parameter of a Two-Variable Graph](https://doi.org/10.1080/01621459.1988.10478613) - JASA
  - Heer et al. (2009) - [Sizing the Horizon: Chart Size and Layering Effects](https://doi.org/10.1145/1518701.1518897) - CHI
- **Recommended Resources:**
  - [WSJ Vaccine Impact Visualization](http://graphics.wsj.com/infectious-diseases-and-vaccines/) - Famous heat map example
  - [D3 Time Scales Documentation](https://github.com/d3/d3-scale#time-scales)
  - Weber et al. (2001) - [Visualizing Time-Series on Spirals](https://doi.org/10.1109/INFVIS.2001.963273) - IEEE InfoVis
- **Supplemental Material:** Aggregation trade-offs, Baseline bias in stacked charts, When to use radial vs linear layouts

### Week 12 (Nov 21) - Clustering and Dimensionality Reduction
- **Slides:** [Clustering and Dimensionality Reduction](/2025-InfoVis-CSE/slides/week12-clustering-dimreduction.html) | **Lab:** [Dimensionality Reduction with D3](/2025-InfoVis-CSE/labs/week12-lab.html)
- **Topics:** Clustering visualization (K-means, hierarchical clustering, comparing methods), Dimensionality reduction fundamentals, Linear methods (PCA), Non-linear methods (t-SNE, UMAP), Critical visualization principles for high-dimensional data
- **Lab:** Implementing PCA and t-SNE visualizations with D3
- **Assignment:** Exercise 12 - Clustering and dimensionality reduction visualization (due Nov 27)
- **Required Readings:**
  - van der Maaten & Hinton (2008) - [Visualizing Data using t-SNE](https://jmlr.org/papers/v9/vandermaaten08a.html) - JMLR
  - Wattenberg et al. (2016) - [How to Use t-SNE Effectively](https://distill.pub/2016/misread-tsne/) - Distill
- **Recommended Resources:**
  - [Understanding UMAP](https://pair-code.github.io/understanding-umap/) - Google PAIR
  - [PCA Explained Visually](https://setosa.io/ev/principal-component-analysis/)
- **Supplemental Material:** Curse of dimensionality, Cluster validation metrics, Choosing perplexity parameters

### Week 13 (Nov 26) - Visualizing Network Data
- **Slides:** [Visualizing Network Data](/2025-InfoVis-CSE/slides/week13-network-data.html)
- **Topics:** Network fundamentals (nodes, edges, degree, paths), Force-directed layouts, Fixed layouts and edge bundling, Matrix representations, Clutter reduction techniques, Tree visualization (node-link diagrams, dendrograms, treemaps, sunburst/icicle plots)
- **Lab:** Building network visualizations with D3 force simulation
- **Assignment:** Exercise 13 - Network and tree visualization (due Dec 4)
- **Required Readings:**
  - Munzner (2014) - Visualization Analysis & Design, Chapter 9 (Networks)
  - Bostock - [D3 Force-Directed Graph](https://observablehq.com/@d3/force-directed-graph)
- **Recommended Resources:**
  - [Force-Directed Graph Gallery](https://observablehq.com/@d3/gallery#networks)
  - [Hierarchical Edge Bundling](https://observablehq.com/@d3/hierarchical-edge-bundling)
- **Supplemental Material:** Force simulation parameters, Layout algorithms comparison, When to use matrices vs node-link diagrams

### Week 14 (Dec 5) - Final Project Presentations
- **Topics:** Group project presentations (Milestone 5)
- **Final Deliverables:**
  - Project website with complete interactive visualizations
  - Process documentation and design rationale
  - 10-minute team presentation
  - Individual reflection submissions
- **Note:** Dec 12 is Reading Day (no class)

## Assignments

### Exercises (35% of grade)
- Exercise 1: Visualization critique and basic Vega-Lite charts - *Due Sept 11*
- Exercise 2: Data questions and transformations - *Due Sept 18*
- Exercise 3: Chart design and encoding alternatives - *Due Sept 25*
- Exercise 4: Perception-based design + D3 implementation - *Due Oct 2*
- Exercise 5: Color scale design and implementation - *Due Oct 9*
- More exercises TBA

### Mini-Projects (35% of grade)
- Mini-Project 1: Geographic data visualization - *Details TBA*
- Mini-Project 2: Temporal data visualization - *Details TBA*
- Mini-Project 3: Network data visualization - *Details TBA*

### Group Project (25% of grade)
- **Milestone 1:** Project Proposal - *Due Oct 20*
- **Milestone 2:** Data Analysis & Sketches - *Due Nov 3*
- **Milestone 3:** First Draft (D3 implementations) - *Due Nov 17*
- **Milestone 4:** Second Draft (Complete article) - *Due Dec 1*
- **Milestone 5:** Final Submission & Presentations - *Due Dec 8* (Presentations Dec 5 & 12)

## Quick Links

- **Discord:** [Join Course Discord](https://discord.gg/sTEv3PnP)
- **Brightspace:** [Course materials and submissions]
- **Observable:** [Create account at observablehq.com]
- **Office Hours:**
    - **Ryan Kim (TA)**: Wednesdays @ 2-3pm, 8th floor common area @ 370 Jay Street, Brooklyn (also [Online @ Zoom](https://nyu.zoom.us/j/92815268504))
    - **Hashmmath Shaik (Grading TA)**: Mondays @ 1-2pm, only [Online @ Zoom](https://nyu.zoom.us/j/2817596431)

