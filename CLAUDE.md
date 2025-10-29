# CLAUDE.md

Guidance for Claude Code when working with Claudio Silva's academic website (Jekyll/GitHub Pages at ctsilva.github.io).

## Quick Commands

```bash
# Setup
bundle install --path vendor/bundle

# Local server (http://127.0.0.1:4000/)
bundle exec jekyll liveserve

# JavaScript build
npm run build:js
```

### Mermaid Diagrams (for Quarto slides)
```bash
# Setup
npm install -g @mermaid-js/mermaid-cli

# Generate PNGs from .mmd files
cd 2025-VisML-CSE/slides
python3 render_mermaid.py

# Manual generation
mmdc -i input.mmd -o output.png -w 800 -H 600 -t default -b transparent
```
**Note**: Always use PNG generation for RevealJS slides (inline mermaid doesn't render reliably).

## Site Structure

### Jekyll Collections
- `_publications`, `_talks`, `_teaching`, `_portfolio`, `_posts`, `_pages`
- Publications in `_pages/publications.md` (chronological 2024→1996)
- Media coverage in `_pages/news.md` (resilient linking with search fallbacks)

### Key Files
- `_config.yml`: Main configuration
- `markdown_generator/`: Scripts for generating content from TSV/BibTeX

### Course Websites
The repository includes complete course websites as subdirectories:
- **2024-VisML-CDS**: VisML (Visualization for Machine Learning) course website (Spring 2024, NYU CDS) - ARCHIVE
- **2025-InfoVis-CSE**: Information Visualization course website (Fall 2025, NYU Tandon) - CS-GY 6313 ✅ **Week 3 COMPLETE**
- **2025-VisML-CSE**: Visualization for Machine Learning course website (Fall 2025, NYU Tandon) - CS-GY 9223 🎉 **100% READY**

#### 2025-VisML-CSE (CS-GY 9223)
- **Schedule**: Mondays 5-7:30PM (Sept 2-Dec 11), Room 473
- **Status**: Week 11 (NLP and LLMs) COMPLETE ✅
- **Discord**: https://discord.gg/dyHSFN65
- **Materials**: week2-intro, week2-infovis, week2-lab, week4-model-assessment, week5-white-box, week6-black-box, week7-deep-learning, week11-nlp




### Course Material Enhancement Workflow

**Trigger**: "PLAN to do these updates for Week X"

1. **Rename generic figures**: paperX.png → descriptive-name.png
2. **Standardize citations**: Add footer citations with DOI links
3. **Add theoretical content**: Include foundational slides with speaker notes
4. **Optimize for projector**: Light code backgrounds, large centered videos
5. **Quality check**: Render, test links, commit with descriptive messages
6. **Update docs**: Mark week complete in CLAUDE.md

#### 2025-InfoVis-CSE (CS-GY 6313)
- **Schedule**: Fridays 11AM-1:30PM (Sept 5-Dec 13), Room 215
- **Status**: Week 3 COMPLETE
- **Discord**: https://discord.gg/sTEv3PnP
- **Materials**: week2-data-transformation, week3-fundamental-graphs
- **Resources**: home.md, syllabus.md, schedule.md, slides/, labs/


### Quarto Slide Creation

```bash
# Render slides
cd 2025-InfoVis-CSE/slides/
quarto render week1-syllabus.qmd

# Preview with live reload
quarto preview week1-syllabus.qmd

# Commit both HTML and _files/ directories
git add week1-syllabus.html week1-syllabus_files/
git commit -m "Add Week 1 slides"
```

**Template header**:
```yaml
---
title: "Title"
subtitle: "CS-GY 6313 - Fall 2025"
author: "Name"
format:
  revealjs:
    theme: [default, custom.scss]
    logo: figs/vida.jpg
    width: 1920
    height: 1080
---
```




## Reference Management

**PDF Naming**: `LastName_Year_Short_Title.pdf`

**Footer Citations**:
```markdown
:::footer
Author, A. (Year). [*Title*](../refs/Author_Year_Title.pdf). Venue.
:::
```

**Venue Abbreviations**: IEEE TVCG, CHI, ICML, AISTATS, ECML-PKDD