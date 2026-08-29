# CLAUDE.md

Guidance for Claude Code when working with Claudio Silva's academic website (Jekyll/GitHub Pages at ctsilva.github.io).

## Quick Commands

```bash
# Setup
bundle install --path vendor/bundle

# Local server (http://127.0.0.1:4000/)
# --livereload auto-refreshes the browser on .md/_sass edits
bundle exec jekyll serve --livereload --incremental

# JavaScript build
npm run build:js
```

### Mermaid Diagrams (for Quarto slides)
```bash
# Setup
npm install -g @mermaid-js/mermaid-cli

# Generate PNGs from .mmd files (script also exists in 2025-VisML-CSE/slides)
cd 2026-VisML-CDS/slides
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
- **2025-InfoVis-CSE**: Information Visualization course website (Fall 2025, NYU Tandon) - CS-GY 6313 - ARCHIVE
- **2025-VisML-CSE**: Visualization for Machine Learning course website (Fall 2025, NYU Tandon) - CS-GY 9223 - ARCHIVE
- **2026-InfoVis-CSE**: Information Visualization (Fall 2026, NYU Tandon) - CS-GY 6313 B - **ACTIVE**
- **2026-VisML-CDS**: Visualization for Machine Learning (Fall 2026, NYU CDS) - DS-GA 3001 - **ACTIVE**

#### 2026-InfoVis-CSE (CS-GY 6313 B)
- **Schedule**: Fridays 11AM-1:30PM (Sept 4 - Dec 11), Jacobs Hall 6 MetroTech Room 315
- **No class**: Nov 27 (Thanksgiving Recess). Fall Break (Oct 12) is a Monday and does not affect this course.
- Sources copied from 2025; rendered `.html` was **not** copied — run `quarto render` per week before class.
- **Blocked on TA assignment**: the lab decks still point at the 2025 TA's personal resources —
  Observable notebooks under `observablehq.com/@rk2546/2025-infovis-cse_week-N-lab` and NYU Zoom rooms
  (`nyu.zoom.us/j/92815268504`, `/2817596431`, `/98539408719`). These need to be re-pointed once a TA is named.

#### 2026-VisML-CDS (DS-GA 3001)
- **Meeting pattern (confirmed)**: `.001` Lecture **Mondays 4:55-6:55 PM** (120 min); `.002` Lab
  **Tuesdays 7:10-8:00 PM** (50 min). Both in 60 Fifth Ave Room 150, cap 75 each. The lab is its own
  registrar-scheduled section that meets the day *after* each lecture — it is **not** time carved out of
  the lecture block, so lab content does not consume lecture time.
- **Term**: Sept 14 - Dec 14. First lab Sept 15, last lab Dec 8 (Week 14 on Dec 14 has no lab).
- **No class**: Sept 7 (Labor Day), Oct 12 (Fall Break). Make-up lecture Wed Oct 14 (University runs a Monday
  schedule). The Tuesday lab still meets Oct 13 — the one week where the lab precedes its lecture.
- **No final exam** during exam week. Reading Day is Tue Dec 15 (no classes).
- **Registrar deadlines (Fall 2026)**: add/drop full-semester Sept 15; withdraw & pass/fail Nov 25;
  Thanksgiving recess Thu-Fri Nov 26-27 (does not affect Mon/Tue sessions).
- Sources copied from 2025-VisML-CSE; rendered `.html` was **not** copied — run `quarto render` per week before class.
- **Deck sizing against the real 120 min + 50 min split.** Lecture ≈60 slides max; a hands-on 50-min lab is
  more like ~25. Tandon's 150-min combined block is why several decks run long:

  | Week | Date | Lecture deck(s) | Slides | Lab deck | Slides |
  |------|------|-----------------|--------|----------|--------|
  | 1 | Sept 14 | week2-intro + week2-infovis | 79 over | week2-lab | 17 ok |
  | 2 | Sept 21 | week3-perception + week3-color | 60 at limit | week3-slides | 11 ok |
  | 3 | Sept 28 | week4-model-assessment | 51 ok | *none — see below* | — |
  | 4 | Oct 5 | week5-white-box | 64 slightly over | week5-lab | 7 ok |
  | 5 | Oct 14 | week6-black-box + week6-project-discussion | 82 over | week6-lab | 34 over |
  | 6 | Oct 19 | week8-clustering + default-project | 57 ok | week7-lab | 39 over |
  | 7 | Oct 26 | week9-dimensionality | 21 ok | week8-lab | 3 ok |
  | 8 | Nov 2 | week7-deep-learning | 24 ok | week9-lab | 31 over |
  | 9 | Nov 9 | week11-nlp | 35 ok | week11-lab | 51 way over |
  | 10 | Nov 16 | week10-tda | 99 way over | week12-lab | 35 over |
  | 11 | Nov 23 | Time Series — no deck yet | — | — | — |
  | 12 | Nov 30 | Interpretable ML & Fairness — no deck yet | — | — | — |

  Lecture problem is concentrated: **Week 10 TDA (99 slides)**, then Weeks 5 and 1. Labs run long more often
  (six of nine) because 50 min is tight — but lab overflow is far less disruptive than lecture overflow.

- **Unresolved lab materials.** Nine lab decks exist as `.qmd` and are scheduled. Still open:
  - **Model Assessment lab** (2026 Week 3, Sept 28). In 2025 this deck lived only in external Google Slides
    (linked from `labs/week4-recap.md`), never in the repo — so it silently dropped out of the schedule.
    Currently listed on home/schedule as *"materials in preparation"*.
  - **`labs/week10-lab/`** holds only a recap; the 2025 session was a guest presentation (Parikshit,
    external Google Slides). Not placed in the 2026 schedule — decide whether to repeat it.
  - **Orphaned notebooks**, not linked from any page: `labs/Lab_white_box_vis1.ipynb`,
    `labs/Lab_white_box_vis2.ipynb` (white-box, Week 4), `labs/VisML_TDA_Lab.ipynb` (TDA, Week 10).

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
- **Status**: Week 13 COMPLETE ✅ (Final presentations Dec 5 & 12)
- **Discord**: https://discord.gg/sTEv3PnP
- **Materials**: week1-syllabus, week2-data-transformation, week3-fundamental-graphs, week4-perception, week5-color, week6-group-projects, week7-interaction, week8-geovis-2d-maps, week9-urban-flows-interactivity, week10-urban-3d-simulation, week11-temporal-data, week12-clustering-dimreduction, week13-network-data
- **Resources**: home.md, syllabus.md, schedule.md, slides/, labs/


### Quarto Slide Creation

```bash
# Render slides
cd 2026-InfoVis-CSE/slides/
quarto render week1-syllabus.qmd

# Preview with live reload
quarto preview week1-syllabus.qmd

# Commit both HTML and _files/ directories
git add week1-syllabus.html week1-syllabus_files/
git commit -m "Add Week 1 slides"
```

The 2026 sites were copied without rendered output, so each deck needs a
`quarto render` before its class. `*.html` / `*_files/` are globally ignored with
a per-year negation in `.gitignore` — add new course years there or renders stay
uncommitted.

**Template header**:
```yaml
---
title: "Title"
subtitle: "CS-GY 6313 - Fall 2026"
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