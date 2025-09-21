# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is an academic personal website for Claudio Silva built using Jekyll and the Academic Pages template (forked from Minimal Mistakes theme). The site is hosted on GitHub Pages at ctsilva.github.io.

## Development Commands

### Local Development Setup (First Time)
```bash
# Install dependencies locally (without sudo)
bundle install --path vendor/bundle
```

### Running the Local Server
```bash
# Run Jekyll server locally with auto-rebuild
bundle exec jekyll liveserve

# Alternative serve command (without live reload)
bundle exec jekyll serve

# Server will be available at http://127.0.0.1:4000/
# Course pages at http://127.0.0.1:4000/2025-InfoVis-CSE/

# Note: Use 127.0.0.1 instead of localhost if localhost doesn't work
```

### Other Commands
```bash
# Clean build directory
bundle clean
```

### JavaScript Build Commands
```bash
# Build/minify JavaScript
npm run build:js
# or
npm run uglify

# Watch JavaScript files for changes
npm run watch:js
```

## Architecture & Structure

### Core Jekyll Collections
The site uses Jekyll collections for organizing content:
- **_publications**: Academic publications
- **_talks**: Presentations and talks  
- **_teaching**: Teaching materials
- **_portfolio**: Project portfolio items
- **_posts**: Blog posts
- **_pages**: Static pages (about, cv, news, etc.)

#### Publications Management
The publications are maintained in `_pages/publications.md` with the following structure:
- **Selected Recent Publications (2023-2025)**: Highlight reel of recent work with full links
- **Award-Winning Publications**: Chronologically organized by year (2024→1996) with comprehensive link coverage
- **Consistent formatting**: All journal extensions use "Invited journal extension of [Original Award]" terminology
- **Complete link coverage**: IEEE Xplore, ResearchGate, NYU Scholars, arXiv, PDFs, and other academic sources
- **Proper chronological ordering**: Publications flow from newest (2024) to oldest (1996) without duplicates

#### Media Coverage Management
The media coverage is maintained in `_pages/news.md` with the following structure:
- **Chronological organization**: Coverage from 2024 → 2015 with clear year sections
- **Resilient linking strategy**: Multiple access methods including original URLs, archive links, and search guidance
- **Featured highlights**: Key stories prominently displayed on main page (PaleoScan, Statcast 10-year, NYC shadows, SONYC)
- **Comprehensive coverage**: Major outlets including NYT, Smithsonian, The Economist, Forbes, etc.
- **Search fallbacks**: Each entry includes search terms to help users find articles even if URLs change
- **Future-proof approach**: Designed to handle link decay and media website changes over time

### Key Configuration
- **_config.yml**: Main Jekyll configuration with site metadata, author info, and collection settings
- **_config.dev.yml**: Development-specific configuration overrides

### Content Generation
The `markdown_generator/` directory contains Python scripts and Jupyter notebooks for generating markdown files from TSV/BibTeX data:
- `publications.py/ipynb`: Generate publication pages from TSV
- `pubsFromBib.py/PubsFromBib.ipynb`: Generate publication pages from BibTeX
- `talks.py/ipynb`: Generate talk pages from TSV

### Theme Structure
- **_sass/**: SCSS stylesheets
- **_layouts/**: Jekyll page layouts
- **_includes/**: Reusable HTML components
- **assets/**: JavaScript, CSS, and other static assets

### Course Websites
The repository includes complete course websites as subdirectories:
- **2024-VisML-CDS**: VisML (Visualization for Machine Learning) course website (Spring 2024, NYU CDS) - ARCHIVE
- **2025-InfoVis-CSE**: Information Visualization course website (Fall 2025, NYU Tandon) - CS-GY 6313 ✅ **Week 3 COMPLETE**
- **2025-VisML-CSE**: Visualization for Machine Learning course website (Fall 2025, NYU Tandon) - CS-GY 9223 🎉 **100% READY**

#### VisML Course Structure (2025-VisML-CSE)
- **Course Code**: CS-GY 9223 Section N - Selected Topics in CS: Visualization for Machine Learning
- **Schedule**: Mondays 5:00 PM - 7:30 PM, Fall 2025 (Sept 2 - Dec 11)
- **Location**: Jacobs Hall, 6 Metrotech Room 473, Brooklyn Campus
- **Make-up Class**: Tuesday, October 14 (for Fall Break)
- **Status**: ✅ **Week 4 COMPLETE** - Model Assessment lecture ready for Sept 22, 2025 class
- **Discord**: https://discord.gg/dyHSFN65

##### Week 2 Materials (Sept 8, 2025) - COMPLETE:
- **week2-intro.qmd/html**: Course introduction, syllabus, logistics (363 lines)
  - Course overview and policies
  - Assessment structure and timeline  
  - Academic integrity and AI policy
  - All syntax issues resolved, renders without warnings
- **week2-infovis.qmd/html**: Information visualization fundamentals (730+ lines)
  - Complete InfoVis theory with Power of Visualization examples
  - All 31 required figures copied and verified
  - Data types, encodings, tidy data principles
  - Graphical perception and effectiveness principles
- **week2-lab.qmd/html**: Vega-Lite hands-on lab activities
  - Observable notebooks and development environment setup
  - Basic visualization creation exercises
  - **Projector-optimized**: Light code backgrounds for classroom visibility
- **figs/**: Complete figure collection (34 total)
  - All Cleveland McGill research examples
  - Complete chart gallery (bar, line, scatter, matrix, symbol maps)  
  - Tidy data transformation examples
  - Visual encoding channels and marks
  - Historical examples (Snow cholera, Minard Napoleon, NYT dialect)

##### Content Sources and Figure Locations:
- **InfoVis fundamentals**: Migrated from 2025-InfoVis-CSE with complete figure set
- **Course logistics**: Adapted from previous VisML courses with Fall 2025 updates
- **Figure assets**: Collected from 2025-InfoVis-CSE and 2024-VisML-CDS repositories
- **Lab materials**: Adapted from InfoVis Vega-Lite exercises

##### Design Principles for Sustainable Course Materials:
- **Date-neutral language**: All content uses specific dates (e.g., "Sept 8") rather than relative terms ("Today", "Next Week")
  - **Rationale**: Avoids outdated language as semester progresses, maintains professional appearance
  - **Implementation**: Replaced "Today's Class" → "Week 2 (Sept 8)", "Today's Lab Activities" → "Lab Activities"
- **Evergreen content**: Materials remain accurate regardless of current date
- **Projector-friendly design**: Light backgrounds for code blocks ensure classroom visibility
- **Professional presentation**: Consistent, timeless language maintains quality over time
- **Future-proof structure**: Content can be reused in future semesters without modification

##### Week 4 Materials (Sept 22, 2025) - COMPLETE:
- **week4-model-assessment.qmd/html**: Model Assessment and Evaluation (848+ lines)
  - Complete migration from 2024-VisML-CDS with all missing content restored
  - Comprehensive speaker notes throughout for teaching preparation
  - Enhanced content depth with additional explanations and context
  - Projector-friendly code styling with light backgrounds for classroom visibility
  - Complete figure collection (39 images) from confusion matrices to calibration
- **figs/model_assessment_figs/**: Complete visual asset library (39 files)
  - Confusion matrix examples and extended matrices
  - ROC curves, AUC examples, and multiclass ROC demonstrations
  - Visual analytics systems screenshots (Squares, Alsallakh, Neo, EnsembleMatrix)
  - Complete calibration content: reliability diagrams, proper scoring rules, calibration techniques
  - Modern research examples: Calibrate (2023), Smooth ECE, neural network calibration
- **lab-light-theme.css**: Projector-optimized styling for code blocks

##### Content Sources and Improvements:
- **Base content**: Migrated from 2024-VisML-CDS with all missing advanced calibration content
- **Enhanced pedagogy**: Added comprehensive speaker notes and improved explanations
- **Technical improvements**: Projector-friendly code styling, larger video displays
- **Research coverage**: Complete coverage from basic confusion matrices to state-of-the-art calibration methods
- **Practical focus**: Working Python examples with sklearn for hands-on learning

##### Assignment Integration:
- **Observable Homework 1**: https://observablehq.com/d/aa2a22499278e4c1
  - NYC transportation data visualization with D3.js fundamentals
  - Student fork-and-complete model for hands-on learning
  - Integrates with week2-lab.qmd Observable setup tutorial

#### InfoVis Course Structure (2025-InfoVis-CSE)
- **Course Code**: CS-GY 6313 - Information Visualization
- **Schedule**: Fridays 11:00 AM - 1:30 PM, Fall 2025 (Sept 5 - Dec 13)
- **Location**: Jacobs Hall, Room 215, Brooklyn Campus  
- **Status**: ✅ **Week 3 COMPLETE** - Fundamental Graphs and Data Transformation ready for Sept 19, 2025
- **Discord**: https://discord.gg/sTEv3PnP

##### Course Materials:
- **home.md**: Main landing page with course announcements and upcoming classes
- **syllabus.md**: Full course syllabus with policies and grading
- **schedule.md**: Detailed weekly schedule with readings and assignments
- **resources.md**: Links to tools, datasets, and learning materials
- **refs/**: Required readings with direct PDF links (Shneiderman, Wickham, Card & Mackinlay)
- **slides/**: Quarto presentations for lectures (instructor content)
  - Uses reveal.js format with custom NYU branding
  - Includes VIDA lab logo (figs/vida.jpg) on all slides
  - Custom SCSS styling + projector-friendly code blocks
- **labs/**: Lab session materials and exercises (TA content)
  - Separate Quarto presentations for lab activities
  - Hands-on exercises and tutorials
  - Clear separation from lecture content

##### Week 2 Materials (Sept 12, 2025) - COMPLETE:
- **week2-data-transformation.qmd/html**: Analytical Questions and Data Transformation (40+ slides)
  - Domain-to-data question translation with flight data and Vision Zero examples
  - Complete SQL operations (Project, Filter, Aggregate) with proper table formatting
  - Roll-up and drill-down operations with visual cube representations  
  - Comprehensive tidy data section with Hadley Wickham examples
  - Data transformation pipeline and wrangling concepts
  - **Critical fixes**: Broken table formatting resolved, projector-friendly code styling
- **figs/**: Complete visual asset library (40+ images)
  - Domain question translation examples (flight data, Vision Zero)
  - SQL operation before/after table visualizations
  - Roll-up/drill-down cube diagrams and SQL examples
  - Complete tidy data transformation workflow images
  - Data abstraction and pipeline diagrams
- **lab-light-theme.css**: Projector-optimized code styling for classroom visibility

##### Week 3 Materials (Sept 19, 2025) - COMPLETE:
- **week3-fundamental-graphs.qmd/html**: Fundamental Graphs and Data Transformation (50+ slides)
  - Two-step visualization process (What to show → How to show)
  - Five fundamental chart types with use cases and examples
  - Expressiveness and effectiveness principles with Cleveland & McGill research
  - Visual encoding rankings and channel effectiveness theory
  - Scale types (linear vs logarithmic) with practical examples
  - Zero baseline rule and appropriate truncation guidelines
  - Data transformation pipeline and aggregation strategies
  - **Complete figure integration**: All missing images found and extracted from source presentations
  - **Optimized layout**: Professional two-column layouts with proper image sizing
  - **Interactive elements**: Quizzes and exercises with structured feedback
- **figs/**: Comprehensive image library with extracted figures
  - Truncated axis examples (misleading vs. proper baselines)
  - Scale comparison examples (linear vs. log scales)
  - Encoding effectiveness demonstrations (bar charts vs. pie charts)
  - Data transformation workflows and aggregation examples
  - All images extracted from PowerPoint and PDF source materials
  - Properly sized and formatted for classroom projection

##### Content Integration:
- **Homepage updates**: Week 2 lecture link added with required readings
- **PDF readings**: Direct links to Shneiderman (1996), Wickham (2014), Card & Mackinlay (1999)
- **Quality assurance**: Comprehensive review resolved formatting issues and content gaps

#### Important Notes
- **Reveal.js Dependencies**: The `.gitignore` has been configured to allow `*_files/` directories for course materials, ensuring reveal.js presentations work correctly on GitHub Pages
- **Week 1-3 Status**: All three weeks ready for Fall 2025 semester with complete materials
- **Projector-Ready**: Code blocks use light backgrounds for classroom visibility

#### Content Creation Guide for TAs

**Current TAs for Fall 2025:**
- **CS-GY 9223 (VisML):** Parikshit Solunke ([parisolunke.github.io](https://parisolunke.github.io)) - pss442@nyu.edu
- **CS-GY 6313 (InfoVis):** Ryan Kim ([rkim.dev](https://www.rkim.dev))

##### Creating New Lecture Slides
1. **Create a new .qmd file** in `2025-InfoVis-CSE/slides/`
2. **Use this template structure:**
```markdown
---
title: "Lecture Title"
subtitle: "CS-GY 6313 - Fall 2025"
author: "Instructor Name"
institute: "New York University"
date: "Month Day, 2025"
format:
  revealjs:
    theme: [default, custom.scss]
    slide-number: c/t
    show-slide-number: all
    hash-type: number
    logo: figs/vida.jpg
    width: 1920
    height: 1080
    preview-links: auto
    transition: fade
    transition-speed: fast
---

## Slide Title

Content here...

## Two Column Layout

:::: {.columns}
::: {.column width="50%"}
Left column content
:::
::: {.column width="50%"}
Right column content
:::
::::

## Code Example

```javascript
// JavaScript code
const data = [1, 2, 3];
```

## Callout Boxes

::: {.callout-tip}
This is a tip
:::

::: {.callout-warning}
This is a warning
:::

::: {.callout-important}
This is important
:::

## Speaker Notes

::: {.notes}
These notes are only visible in presenter mode
:::
```

##### Rendering Slides
```bash
# Navigate to slides directory
cd 2025-InfoVis-CSE/slides/

# Render a specific slide deck
quarto render week1-syllabus.qmd

# Render all .qmd files in directory
quarto render

# Preview with live reload (auto-updates on save)
quarto preview week1-syllabus.qmd
```

**Important:** After rendering, make sure to commit both the generated HTML files and `*_files/` directories containing reveal.js dependencies:
```bash
git add week1-syllabus.html week1-syllabus_files/
git commit -m "Add/update Week 1 slides"
```

The HTML files are **not ignored** by git so they're accessible to students at:
`https://ctsilva.github.io/2025-InfoVis-CSE/slides/[filename].html`

##### Adding Lab Materials
1. Lab materials go in `2025-InfoVis-CSE/labs/` directory
2. Create Quarto slides for lab sessions using same template as lectures
3. Path adjustments for labs:
   - Logo: `logo: ../slides/figs/vida.jpg`
   - Theme: `theme: [default, ../slides/custom.scss]`
4. Include Observable notebook links and exercises
5. Keep lab content separate from lecture slides for clear ownership

Example lab slide header:
```markdown
---
title: "Week X Lab: Topic"
subtitle: "CS-GY 6313 - Information Visualization"
author: "Teaching Assistant"
institute: "New York University"
date: "Month Day, 2025"
format:
  revealjs:
    theme: [default, ../slides/custom.scss]
    logo: ../slides/figs/vida.jpg
    # ... other settings
---
```

##### Updating Course Pages
1. **home.md**: Update with weekly announcements and assignment deadlines
2. **schedule.md**: Add lecture slides links, readings, and lab materials as they're created
3. Use Jekyll/Markdown format with YAML front matter:
```markdown
---
title: "Page Title"
permalink: /2025-InfoVis-CSE/pagename
author_profile: true
---

Content in markdown...
```

##### Adding Images and Assets
- Place images in appropriate directories:
  - Slide images: `2025-InfoVis-CSE/slides/figs/`
  - Course images: `2025-InfoVis-CSE/images/`
- Reference in markdown: `![Alt text](figs/image.png)`
- Reference in Quarto: `![[Alt text]](figs/image.png){width="50%"}`

##### Linking to Materials
- **Lecture slides:** `/2025-InfoVis-CSE/slides/week1-syllabus.html`
- **Lab slides:** `/2025-InfoVis-CSE/labs/week1-lab.html`
- **Course pages (MD):** `/2025-InfoVis-CSE/syllabus`
- **Example links:** 
  - `[Week 1 Lecture](/2025-InfoVis-CSE/slides/week1-syllabus.html)`
  - `[Week 1 Lab](/2025-InfoVis-CSE/labs/week1-lab.html)`
- **External links:** `[Observable](https://observablehq.com)`

Note: Link to `.html` for rendered slides, but omit extension for Jekyll pages

##### Testing Changes Locally
```bash
# From repository root
bundle exec jekyll serve

# View at http://127.0.0.1:4000/2025-InfoVis-CSE/
```

## Jekyll Plugins
Key plugins enabled (via github-pages gem):
- jekyll-paginate
- jekyll-sitemap  
- jekyll-gist
- jekyll-feed
- jekyll-redirect-from

## Deployment
The site automatically deploys to GitHub Pages when pushing to the main branch. GitHub Pages settings should have the repository renamed to `[username].github.io`.

## Future Enhancements

### Portfolio Expansion
- **Code repositories**: Highlight key GitHub projects (OpenSpace, OSCUR, PaleoScan, etc.)
- **Interactive demos**: Link to live visualizations or web-based tools
- **Project galleries**: Screenshots/videos of major systems in action
- **Technical documentation**: API docs, user guides for your tools

### Publications Organization
- **Research categories**: Visualization, Urban Computing, Sports Analytics, Machine Learning, etc.
- **Topic filters**: Allow visitors to browse by research area
- **Impact highlights**: Feature most-cited papers or award winners
- **Collaboration networks**: Show key co-authors and institutions
- **Timeline view**: Chronological research evolution
- **Audience-specific guides**: 
  - "New to visualization" → foundational papers
  - "Sports analytics researchers" → Statcast and related work
  - "Urban computing" → SONYC, shadow mapping, etc.

### Metrics Integration (Currently Commented Out)
- **Sidebar metrics**: h-index: 78, i10-index: 323, Citations: 29,427, Publications: 400+
- **Location**: `_includes/author-profile.html` (lines 118-125)
- **To enable**: Remove `{% comment %}` and `{% endcomment %}` tags

### Technical Notes
- **Academic Pages Template**: Base template provides solid foundation for future enhancements
- **Jekyll Collections**: Ready for additional content types and categorization
- **Responsive Design**: All additions should maintain mobile-friendly design
- **Search Optimization**: Consider adding site search functionality for larger content volumes
- to memorize
- to memorize