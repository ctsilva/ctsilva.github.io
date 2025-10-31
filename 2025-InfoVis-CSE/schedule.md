---
title: "CS-GY 6313: Information Visualization - Fall 2025 Detailed Schedule"
permalink: /2025-InfoVis-CSE/schedule
author_profile: true
---

[← Back to Course Home](/2025-InfoVis-CSE/) | [Course Syllabus](/2025-InfoVis-CSE/syllabus) | [Resources](/2025-InfoVis-CSE/resources)

## Detailed Schedule

### **Week 1** (Sept 5) - Introduction and Evaluation
**Learning Objectives:** Understand what visualization is, when to use it, and how to evaluate effectiveness

**Lecture:** [Week 1 - Course Introduction & Syllabus](slides/week1-syllabus.html)
- Course overview and expectations
- What is information visualization? 
- Visualization taxonomy and design space
- Evaluation frameworks and criteria
- Introduction to tools landscape (Vega-Lite, D3, Tableau, etc.)

**Required Readings:**
- [Chapter 1: Information Visualization](https://courses.cs.washington.edu/courses/cse512/25sp/uwnetid/readings/value/CMS-Chap1.pdf), in Readings in Information Visualization. Card, Mackinlay, and Shneiderman. 1999.
- [Introduction to Vega-Lite](https://observablehq.com/@uwdata/introduction-to-vega-lite-json) (Observable notebook)

**Optional Reading:**
- [Decision to Launch the Challenger](https://courses.cs.washington.edu/courses/cse512/25sp/uwnetid/readings/value/Tufte-Challenger.pdf), in Visual Explanations. Edward Tufte.

**Lab:** [Week 1 Lab - Introduction to Observable and Vega-Lite](labs/week1-lab.html)
- Setup Observable accounts
- Create first basic charts in Vega-Lite
- Explore provided datasets
- Chart gallery exploration

**Assignment:** Exercise 1 - Visualization critique and basic Vega-Lite charts (due Sept 11)

### **Week 2** (Sept 12) - Analytical Questions and Data Transformation  
**Learning Objectives:** Transform questions into visual queries; understand data transformation pipelines

**Lecture:** [Week 2 - Analytical Questions and Data Transformation](slides/week2-data-transformation.html) 
- From questions to visual mappings
- Data types and structures
- Data transformation operations (filter, aggregate, derive)
- Query-based visualization systems
- Introduction to Observable notebooks

**Required Readings:**
- [Data Types, Graphical Marks, and Visual Encoding Channels](https://observablehq.com/@uwdata/data-types-graphical-marks-encoding-channels-json) (Observable)
- [Polaris: A System for Query, Analysis and Visualization of Multi-dimensional Relational Databases](https://courses.cs.washington.edu/courses/cse512/25sp/uwnetid/readings/multidimensional/Stolte_Polaris_TVCG.pdf). Stolte, Tang, and Hanrahan. IEEE TVCG 2002.

**Optional Reading:**
- [The Eyes Have It: A Task by Data Type Taxonomy](https://courses.cs.washington.edu/courses/cse512/25sp/uwnetid/readings/models/shneiderman96eyes.pdf), Shneiderman. 1996.

**Lab:** [Week 2 Lab - Intro to Vega-Lite Data Transformations, Working with Real Datasets](labs/week2-lab.html) 
- Vega-Lite data transformations
- Working with real datasets in Observable
- Data aggregation and filtering
- Creating derived fields

**Assignment:** Exercise 2 - Data questions and transformations using Vega-Lite (due Sept 18)

### **Week 3** (Sept 19) - Fundamental Graphs and Visual Encoding
**Learning Objectives:** Master basic chart types and understand when to use each; apply grammar of graphics

**Lecture:** 
- Chart types and their purposes
- Marks and channels theory
- Grammar of graphics principles
- Comparison strategies
- When to use different chart types

**Materials:**
- [Fundamental Graphs and Visual Encoding](/2025-InfoVis-CSE/slides/week3-fundamental-graphs.html)

**Required Readings:**
- Chapter 1: Graphical Excellence, in The Visual Display of Quantitative Information. Tufte.
- Chapter 2: Graphical Integrity, in The Visual Display of Quantitative Information. Tufte.
- [Multi-View Composition](https://observablehq.com/@uwdata/multi-view-composition-json) (Observable)

**Optional Reading:**
- [Vega-Lite: A Grammar of Interactive Graphics](https://www.youtube.com/watch?v=9uaHRWj04D4). Wongsuphasawat et al. OpenVis Conf 2017.

**Lab:** [Lab: Fundamental Graphs and Visual Encoding](/2025-InfoVis-CSE/labs/week3-lab.html) 
- Creating multiple chart types in Vega-Lite
- Exploring encoding alternatives for same data
- Small multiples and faceting
- Combining multiple views

**Assignment:** Exercise 3 - Chart design and encoding alternatives (due Sept 25)

### **Week 4** (Sept 26) - Visual Perception and D3 Foundations
**Learning Objectives:** Understand human visual perception principles; begin D3 programming

**Lecture:**
- Pre-attentive processing and visual attention
- Gestalt principles in visualization
- Color perception and accessibility
- Introduction to D3.js: concepts and architecture
- DOM manipulation basics

**Required Readings:**
- [The Science of Visual Data Communication: What Works](https://journals.sagepub.com/doi/full/10.1177/15291006211051956). Franconeri et al. Psychological Science in the Public Interest. 2021.
- [39 Studies About Human Perception in 30 Minutes](https://medium.com/@kennelliott/39-studies-about-human-perception-in-30-minutes-4728f9e31a73). Kennedy Elliott.

**Optional Reading:**
- [Graphical Perception: Theory, Experimentation and Application](https://courses.cs.washington.edu/courses/cse512/25sp/uwnetid/readings/perception/Cleveland_GraphicalPerception.pdf). Cleveland & McGill. 1984.

**Lab:** [Lab: First D3 programming session, DOM manipulation, Data binding](/2025-InfoVis-CSE/labs/week4-lab.html)
- First D3 programming session
- DOM manipulation exercises
- Data binding concepts
- Create simple bar chart in D3

**Assignment:** Exercise 4 - Perception-based design decisions + D3 implementation (due Oct 2)

### **Week 5** (Oct 3) - Color and D3 Scales
**Learning Objectives:** Master color theory for visualization; implement D3 scales and color schemes

**Lecture:**
- Color theory fundamentals
- Perceptual color spaces (RGB, HSL, LAB)
- Colorblindness and accessibility
- Color palette design strategies
- D3 scales: linear, ordinal, time, color

**Required Readings:**
- [Which color scale to use when visualizing data](https://blog.datawrapper.de/which-color-scale-to-use-in-data-vis/). Lisa Charlotte Rost.
- [Modeling Color Difference for Visualization Design](https://courses.cs.washington.edu/courses/cse512/25sp/uwnetid/readings/color/szafir2017modeling.pdf). Danielle Szafir. IEEE TVCG, 2017.

**Optional Readings:**
- [Somewhere Over the Rainbow: An Empirical Assessment of Quantitative Colormaps](http://idl.cs.washington.edu/papers/quantitative-color/). Liu & Heer. ACM CHI 2018.
- [Color Use Guidelines for Mapping and Visualization](https://courses.cs.washington.edu/courses/cse512/25sp/uwnetid/readings/color/Brewer_1994b.pdf). Cynthia Brewer. 1994.

**Lab:** [Color scale exercises, Choropleth maps, Accessibility testing](/2025-InfoVis-CSE/labs/week5-lab.html)
- D3 scales implementation
- Color scheme creation and testing
- Accessibility testing tools
- Apply color theory to previous D3 examples

**Assignment:** Exercise 5 - Color design with D3 scales (due Oct 9)

### **Week 6** (Oct 10) - Group Projects and Design Ethics
**Learning Objectives:** Understand group project requirements and milestones; identify misleading visualizations; recognize ethical design principles

**Lecture:** [Week 6 - Group Projects](slides/week6-group-projects.html)
- Group project overview and timeline
- Five milestones: Proposal, Data & Sketches, First Draft, Second Draft, Final
- Team formation and collaboration strategies
- Choosing topics and datasets (focus on NYC urban data)
- Example projects and evaluation criteria
- **Plus:** Deceptive visualization and design ethics discussion

**Required Readings:**
- Chapter 2: Graphical Integrity, in *The Visual Display of Quantitative Information*. Edward Tufte. 2001.
- [Misinformed by Visualization: What Do We Learn From Misinformative Visualizations?](https://arxiv.org/pdf/2104.14332.pdf). Lo, Gupta & Shigyo. EuroVis 2022.

**Optional Readings:**
- [Truncating the Y-Axis: Threat or Menace?](https://arxiv.org/pdf/1907.02035.pdf). Correll, Bertini & Franconeri. 2020.
- [Viral Visualizations: How Coronavirus Skeptics Use Orthodox Data Practices to Promote Unorthodox Science Online](https://arxiv.org/pdf/2101.07993.pdf). Lee et al. ACM CHI 2021.

**Lab:** [Lab: Intro to Interactions and Deceptive Visualizations](/2025-InfoVis-CSE/labs/week6-lab.html)
- Team formation activities
- NYC Open Data exploration
- Project brainstorming and proposal planning
- Start forming teams on Discord #project-teams

**Assignment:**
- Form teams by Oct 17
- Browse NYC Open Data for project ideas
- Exercise 6 - Design misleading vs. honest versions of same data (due Oct 16)

### **Fall Break** (Oct 11-13) - **NO CLASS**

### **Week 7** (Oct 17) - Interaction in Visualization
**Learning Objectives:** Understand why interaction is essential for data exploration; master the 12 interactive dynamics; design effective interactive visualizations

**Lecture:** [Week 7 - Interactivity in Information Visualization](slides/week7-interaction.html)
- Why interaction matters: From presentation to exploration
- Bridging the gulfs (HCI concepts)
- Shneiderman's Visual Information Seeking Mantra
- The 12 interactive dynamics (Heer & Shneiderman taxonomy):
  - **Data & View Specification:** Visualize, Filter, Sort, Derive
  - **View Manipulation:** Select, Navigate, Coordinate, Organize
  - **Process & Provenance:** Record, Annotate, Share, Guide
- Modern interaction frameworks (Libra)
- Case studies: FilmFinder, VisTrails, TaxiVis

**Required Readings:**
- [The Eyes Have It: A Task by Data Type Taxonomy](/2025-InfoVis-CSE/refs/Shneiderman_1996_The_Eyes_Have_It.pdf). Shneiderman. IEEE VIS 1996.
- [Interactive Dynamics for Visual Analysis](/2025-InfoVis-CSE/refs/Heer_Shneiderman_2012_Interactive_Dynamics_Visual_Analysis.pdf). Heer & Shneiderman. ACM Queue 2012.

**Recommended Readings:**
- [Toward a Deeper Understanding of the Role of Interaction in Information Visualization](/2025-InfoVis-CSE/refs/Yi_2007_Toward_Deeper_Understanding_Interaction.pdf). Yi et al. IEEE TVCG 2007.
- [The Science of Interaction](/2025-InfoVis-CSE/refs/Pike_2009_Science_of_Interaction.pdf). Pike et al. Information Visualization 2009.
- [Libra: Composable Interactions](/2025-InfoVis-CSE/refs/Zhao_2025_Libra_Composable_Interactions.pdf). Zhao et al. CHI 2025.

**Lab:** [Lab: Building Interactive Visualizations](labs/week7-lab.html)
- D3 event handling (hover, click, brush)
- Implementing filtering and dynamic queries
- Tooltip and details-on-demand
- Brushing and linking across multiple views
- Creating coordinated visualizations

**Assignment:** Exercise 7 - Interactive visualization design and implementation (due Oct 23)

### **Week 8** (Oct 24) - Geographic and Urban Visualization I
**Learning Objectives:** Understand map projections and geographic data; create effective choropleth and point maps

**Lecture:** 
- Map projections and their trade-offs
- Geographic data formats (GeoJSON, TopoJSON, Shapefiles)
- Choropleth map design principles
- Point mapping and density visualization
- Multi-scale geographic visualization

**Required Readings:**
- [GeoLinter: A Linting Framework for Choropleth Maps](https://arxiv.org/pdf/2310.13707). Lei, Fan, MacEachren & Maciejewski. IEEE TVCG 2023.
- [Research Challenges in Geovisualization](https://www.researchgate.net/publication/313573280_Research_challenges_in_geovisualization_Cartography_Geograph). MacEachren & Kraak. Cartography and Geographic Information Science 2001.

**Optional Readings:**
- [When Maps Shouldn't Be Maps](http://uxblog.idvsolutions.com/2011/10/when-maps-shouldnt-be-maps.html). Matthew Ericson. 2011.
- [Surprise! Bayesian Weighting for De-Biasing Thematic Maps](https://idl.cs.washington.edu/files/2013-BayesianSurpriseMaps-InfoVis.pdf). Correll & Heer. IEEE InfoVis 2017.
  
**Lab:** [Plotting and Troubleshooting GeoJSON with D3](/2025-InfoVis-CSE/labs/week8-lab.html)
- D3 geo projection setup
- Loading and displaying maps
- Creating choropleth maps with real data
- Point mapping exercises

**Assignment:** **Mini-project 1 begins** - Geographic visualization (due Nov 6)

### **Week 9** (Oct 31) - Temporal Data and Urban Dynamics
**Learning Objectives:** Design effective time series visualizations; understand temporal patterns in urban data

**Lecture:** 
- Time series design principles
- Temporal data types and structures
- Animation vs. static temporal representation
- Seasonal and cyclical patterns
- Urban temporal dynamics

**Required Readings:**
- [Visual Exploration of Big Spatio-Temporal Urban Data: A Study of New York City Taxi Trips](https://ieeexplore.ieee.org/document/6634127/). Ferreira, Poco, Vo, Freire & Silva. IEEE TVCG 2013.
- [Urbane: A 3D Framework to Support Data Driven Decision Making in Urban Development](https://hvo.github.io/papers/urbane.pdf). Ferreira et al. IEEE VIS 2015.

**Optional Readings:**
- [Graphical Perception of Multiple Time Series](https://idl.cs.washington.edu/files/2009-GraphicalPerceptionMultiple-InfoVis.pdf). Heer, Kong & Agrawala. IEEE InfoVis 2009.
- [The Connected Scatterplot for Presenting Paired Time Series](https://eagereyes.org/papers/the-connected-scatterplot-for-presenting-paired-time-series). Haroz, Kosara & Franconeri. IEEE TVCG 2016.

**Lab:** [Building interactive spatio-temporal visualization](/2025-InfoVis-CSE/labs/week9-lab.html)
- D3 time scales and axes
- Line charts and area charts for time series
- Brushing and zooming for temporal data
- Small multiples for temporal comparison

**Assignment:** **Mini-project 2 begins** - Temporal visualization (due Nov 20)

### **Week 10** (Nov 7) - Uncertainty and Data Quality
**Learning Objectives:** Represent uncertainty visually; assess and communicate data quality issues

**Lecture:** 
- Types of uncertainty in data
- Visual encoding of uncertainty
- Error bars and confidence intervals
- Alternative uncertainty representations
- Data quality assessment and communication

**Required Readings:**
- [The Visual Uncertainty Experience](https://www.youtube.com/watch?v=pTVAn4oLvbc). Jessica Hullman. OpenVis Conf 2016.
- [Error Bars Considered Harmful: Exploring Alternate Encodings for Mean and Error](http://graphics.cs.wisc.edu/Papers/2014/CG14/Preprint.pdf). Correll & Gleicher. IEEE InfoVis 2014.

**Optional Reading:**
- [When(ish) is My Bus? User-centered Visualizations of Uncertainty](http://idl.cs.washington.edu/papers/when-ish-is-my-bus/). Kay et al. ACM CHI 2016.

**Lab:** 
- Implementing uncertainty visualizations in D3
- Confidence intervals and error representations
- Alternative uncertainty encodings
- User testing uncertainty representations

**Assignment:** Continue Mini-project 2 + Exercise 8 - Uncertainty visualization (due Nov 13)

### **Week 11** (Nov 14) - Network Data and Urban Systems
**Learning Objectives:** Understand network visualization techniques; apply to urban infrastructure and social systems

**Lecture:** 
- Network data structures and properties
- Node-link diagrams and layout algorithms
- Matrix representations of networks
- Hierarchical and multilevel networks
- Urban networks (transportation, social, infrastructure)

**Required Readings:**
- [Hierarchical Edge Bundles: Visualization of Adjacency Relations in Hierarchical Data](http://www.aviz.fr/wiki/uploads/Teaching2014/bundles_infovis.pdf). Danny Holten. InfoVis 2006.
- [Squarified Treemaps](https://courses.cs.washington.edu/courses/cse512/25sp/uwnetid/readings/trees/Bruls_SquarifiedTreemaps.pdf). Bruls, Huizing & van Wijk. 2000.

**Optional Reading:**
- [ManyNets: An Interface for Multiple Network Analysis and Visualization](http://dmrussell.net/CHI2010/docs/p213.pdf). Freire et al. ACM CHI 2010.

**Lab:** 
- D3 force simulation setup
- Creating node-link diagrams
- Network layout algorithms
- Interactive network exploration

**Assignment:** **Mini-project 3 begins** - Network visualization (due Dec 4)

### **Week 12** (Nov 21) - Scalability and Performance
**Learning Objectives:** Handle large datasets; optimize visualization performance; understand progressive loading

**Lecture:** 
- Challenges of large dataset visualization
- Data aggregation and sampling strategies
- Progressive loading and level-of-detail
- Performance optimization techniques
- Introduction to WebGL for visualization

**Required Readings:**
- [A Structured Review of Data Management Technology for Interactive Visualization](https://homes.cs.washington.edu/~leibatt/static/papers/battle2020structured.pdf). Battle & Scheidegger. IEEE TVCG. 2020.
- [Falcon: Balancing Interactive Latency and Resolution Sensitivity](http://idl.cs.washington.edu/papers/falcon/). Moritz, Howe & Heer. ACM CHI 2019.

**Optional Readings:**
- [imMens: Real-time Visual Querying of Big Data](http://idl.cs.washington.edu/papers/immens). Liu, Jiang & Heer. EuroVis 2013.
- [Trust, but Verify: Optimistic Visualizations of Approximate Queries](http://idl.cs.washington.edu/papers/trust-but-verify). Moritz et al. ACM CHI 2017.

**Lab:** 
- Data aggregation techniques
- Performance profiling and optimization
- Canvas vs SVG performance comparison
- Introduction to visualization with large datasets

**Assignment:** Continue Mini-project 3 + optimization exercises (due Nov 25)

### **Make-up Class** (Nov 26 - Wednesday) - Geographic and Urban Visualization II  
**Learning Objectives:** Advanced geographic techniques; intensive project development time

**Extended Workshop (2.5 hours with breaks):** 
- Advanced D3 geo techniques
- Multi-scale mapping strategies
- Spatial analysis and visualization
- Working with urban datasets
- Intensive hands-on work on Mini-project 1
- Individual guidance and troubleshooting

**Assignment:** Complete any outstanding work on Mini-project 1

### **Week 13** (Nov 28) - **NO CLASS** (Thanksgiving)
**Assignment:** Complete Mini-project 3 and prepare group project presentations

### **Week 14** (Dec 5) - Advanced Topics and Project Presentations I
**Learning Objectives:** Explore emerging trends; present and critique visualization projects

**Lecture (45 min):** 
- Emerging trends in visualization
- AI and machine learning visualization
- Virtual and augmented reality applications
- Future directions and career paths

**Presentations:** 
- Group project presentations (first half of teams)
- Peer feedback and discussion
- Q&A and critique sessions

**Assignment:** Prepare final presentations and project documentation

### **Week 15** (Dec 12) - Project Presentations II and Course Wrap-up
**Learning Objectives:** Complete project presentations; reflect on learning; plan continued development

**Presentations:** 
- Final group project presentations (second half)
- Peer feedback and evaluation
- Class discussion of projects and techniques

**Wrap-up:** 
- Course reflection and key takeaways
- Resources for continued learning
- Career advice and next steps
- Course evaluations