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
- **_pages**: Static pages (about, cv, etc.)

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
- **2024-VisML-CDS**: VisML (Visualization for Machine Learning) course website (taught in 2024)
- **2025-InfoVis-CSE**: Information Visualization course website (Fall 2025)

#### InfoVis Course Structure
- **home.md**: Main landing page with course announcements and upcoming classes
- **syllabus.md**: Full course syllabus with policies and grading
- **schedule.md**: Detailed weekly schedule with readings and assignments
- **resources.md**: Links to tools, datasets, and learning materials
- **slides/**: Quarto presentations for lectures (instructor content)
  - Uses reveal.js format with custom NYU branding
  - Includes VIDA lab logo (figs/vida.jpg) on all slides
  - Custom SCSS styling in custom.scss
- **labs/**: Lab session materials and exercises (TA content)
  - Separate Quarto presentations for lab activities
  - Hands-on exercises and tutorials
  - Clear separation from lecture content
- **Discord**: https://discord.gg/sTEv3PnP

#### Important Notes
- **Reveal.js Dependencies**: The `.gitignore` has been configured to allow `*_files/` directories for course materials, ensuring reveal.js presentations work correctly on GitHub Pages
- **Week 1 Status**: Ready for Sept 5, 2025 class with Ryan Kim as TA and Discord channel active

#### Content Creation Guide for TAs

**Current TA for Fall 2025:** Ryan Kim ([rkim.dev](https://www.rkim.dev))

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
- to memorize