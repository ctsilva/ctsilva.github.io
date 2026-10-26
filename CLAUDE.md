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
- **Staff**: TA (labs) and Grader are both **Ryan Kim** (returning from 2025; site https://www.rkim.dev,
  Observable handle `@rk2546`). Listed on home, syllabus, and week1-syllabus slides.
- **Instructor office hours**: Fridays 1:30-2:30 PM, 370 Jay Street, Room 1153 (right after class).
- **Still stale in the lab decks**: they point at Ryan's 2025 resources — Observable notebooks under
  `observablehq.com/@rk2546/2025-infovis-cse_week-N-lab` and NYU Zoom rooms (`nyu.zoom.us/j/92815268504`,
  `/2817596431`, `/98539408719`), plus TA office hours listed as "Wednesdays 2-3PM, 8th floor common area
  @ 370 Jay". Confirm with Ryan whether the notebooks get 2026 copies, whether the Zoom rooms and office
  hours are unchanged, and whether the separate "Grader TA" Zoom is still needed now that one person holds
  both roles. Then update the lab decks.

#### 2026-VisML-CDS (DS-GA 3001)
- **Meeting pattern (corrected 2026-09-08 from the registrar listing)**: **everything is on Tuesday.**
  `.001` Lecture **Tuesdays 4:55-6:55 PM** (120 min), then `.002` Lab **Tuesdays 7:10-8:00 PM** (50 min)
  after a 15-min break, both in 60 Fifth Ave Room 150, cap 75 each. The lab is still its own
  registrar-scheduled section, so lab content does **not** consume lecture time — but it now lands at the
  end of a 3-hour evening rather than a day later, so a lab deck that overruns has no overnight reset.
  (An earlier version of this file recorded a Monday lecture as "confirmed"; that was wrong.)
- **Term**: 14 Tuesdays, **Sept 8 - Dec 8**, with **no cancellations** — Labor Day (Sept 7) and Fall Break
  (Oct 12) are Mondays, Thanksgiving (Nov 26-27) is Thu-Fri. No Wednesday make-up is needed.
- **No final exam** during exam week. Reading Day is Tue Dec 15 (no classes). Final report still due Dec 14
  (term end), a week after the last class.
- **Instructor office hours**: Fridays 1:30-2:30 PM, 370 Jay Street, Room 1153 (Brooklyn, not Washington Square).
- **Session leader (labs) & grader**: **Bhavya Matam** (bm3792@nyu.edu).
- **No default project (decided 2026-10-12)**: every group proposes its own project; the proposal is the approval
  step. `slides/default-project.qmd` (Tile2Net) and `projects/finalproject.md` (StreetAware) are unlinked leftovers.
- **Project proposal timing (resolved 2026-10-12)**: discussion deck moved to Week 6 (Oct 13), proposal due
  Week 7 (Oct 20); `project-discussion.qmd` no longer carries 2025 TA names or dates.
- **Registrar deadlines (Fall 2026)**: add/drop full-semester Sept 15; withdraw & pass/fail Nov 25;
  Thanksgiving recess Thu-Fri Nov 26-27 (does not affect Mon/Tue sessions).
- Sources copied from 2025-VisML-CSE; rendered `.html` was **not** copied — run `quarto render` per week before class.
- **Deck sizing against the real 120 min + 50 min split.** Lecture ≈60 slides max; a hands-on 50-min lab is
  more like ~25. Tandon's 150-min combined block is why several decks run long:

  | Week | Date | Lecture deck(s) | Slides | Lab deck | Slides |
  |------|------|-----------------|--------|----------|--------|
  | 1 | Sept 8 | course-intro + visualization-intro | 79 over | vega-lite | 17 ok |
  | 2 | Sept 15 | perception + color | 60 at limit | perception-color | 11 ok |
  | 3 | Sept 22 | model-assessment | 52 ok | *none — see below* | — |
  | 4 | Sept 29 | white-box-models | 64 slightly over | interpretable-ml | 7 ok |
  | 5 | Oct 6 | black-box-models + project-discussion | 82 over | black-box-explainability | 34 over |
  | 6 | Oct 13 | clustering + project-discussion | 65 slightly over (6 clustering slides skippable) | project-proposal (workshop; this is what ran) | 3 ok |
  | 7 | Oct 20 | dimensionality-reduction | 36 (was 21; 14 new slides, all skippable) | dimensionality-reduction (DR in practice; did not run Oct 13) | 48, about 25 core plus a backup block with jump links |
  | 8 | Oct 27 | deep-learning | 32 ok (24 + 8 split-out text slides, laid out 2026-10-26) | deep-learning (new; Playground + CNN Explainer, run by Claudio) + paper-writing (about 25 core min) | 12 + 39 |
  | 9 | Nov 3 | nlp | 35 ok | nlp-vis | 35 over |
  | 10 | Nov 10 | tda | 99 way over | tda (Mapper, persistent homology) | 31 over |
  | 11 | Nov 17 | Time Series — no deck yet | — | — | — |
  | 12 | Nov 24 | Interpretable ML & Fairness — no deck yet | — | — | — |

  Lecture problem is concentrated: **Week 10 TDA (99 slides)**, then Weeks 5 and 1. Labs run long more often
  (six of nine) because 50 min is tight — but lab overflow is far less disruptive than lecture overflow.

- **Week 7 (Oct 20) deck and lab, built 2026-10-15.** Lecture adds t-SNE equations, the crowding problem, live
  perplexity/seed/UMAP demos on sklearn digits, trustworthiness/continuity (a flat-with-perplexity result is shown on
  purpose), a PCA/t-SNE/UMAP table, a checklist, and a next-week slide; its Python cells need the uv venv and re-run on
  every render (about a minute). Speaker notes on the Distill/UMAP/TopoMap figure slides were rewritten against the
  figures (5 perplexities not 4, steps 10/20/60/120/1000, Fashion-MNIST not digits, TopoMap preserves components not
  holes). Lab `labs/dimensionality-reduction` loads sklearn's 8x8 digits (64 features), not MNIST; there is a heads-up slide for that.
  Jump links need ids: `[text](#lab-lle)` (Quarto adds the `/`; writing `#/lab-lle` produces `#//lab-lle`).
  Known environment limits: the 3D plotly slides need WebGL and plotly's CDN scripts (jquery, requirejs) and show
  "WebGL is not supported" in headless Chrome; the YouTube embed on the lab t-SNE slide errors (153) from `file://`.
- **File naming (renamed 2026-10-26): topic names, no week numbers.** Lectures are `slides/<topic>.qmd`
  (`deep-learning`, `nlp`, `tda`, ...). Labs are `labs/<topic>/lab.qmd` with a `recap.md` beside it
  (`labs/deep-learning/`, `labs/nlp-vis/`, `labs/paper-writing/`, ...). Only `schedule.md` and `home.md` map
  weeks to files, so a schedule change never makes a filename lie. Old URLs for the 16 pages that had
  already been published are tiny redirect stubs at their old paths (e.g. `slides/week2-intro.html`); leave them.
  Not renamed on purpose: `labs/week5/` (Colab links on the interpretable-ml lab point at that GitHub path),
  the loose `labs/*.ipynb` notebooks, and `slides/default-project*`. `labs/archive/` holds 2025 recaps whose
  topic could not be verified. The Discord channel `#week3-lab` is still named in the perception-color lab.
- **Unresolved lab materials.** Nine lab decks exist as `.qmd` and are scheduled. Still open:
  - **Model Assessment lab** (2026 Week 3, Sept 22). In 2025 this deck lived only in external Google Slides
    (linked from `labs/model-assessment/recap.md`), never in the repo — so it silently dropped out of the schedule.
    Currently listed on home/schedule as *"materials in preparation"*.
  - **`labs/guest-talk/`** holds only a recap; the 2025 session was a guest presentation (Parikshit,
    external Google Slides). Not placed in the 2026 schedule — decide whether to repeat it.
  - **Orphaned notebooks**, not linked from any page: `labs/Lab_white_box_vis1.ipynb`,
    `labs/Lab_white_box_vis2.ipynb` (white-box, Week 4), `labs/VisML_TDA_Lab.ipynb` (TDA, Week 10).

#### 2025-VisML-CSE (CS-GY 9223)
- **Schedule**: Mondays 5-7:30PM (Sept 2-Dec 11), Room 473
- **Status**: Week 11 (NLP and LLMs) COMPLETE ✅
- **Discord**: https://discord.gg/dyHSFN65
- **Materials**: week2-intro, week2-infovis, week2-lab, week4-model-assessment, week5-white-box, week6-black-box, week7-deep-learning, week11-nlp  (file names as they were in 2025; the 2026 site uses topic names)




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
`quarto render` before its class. Decks with executable `{python}` cells (VisML
`model-assessment.qmd`) need a Python with Jupyter, which the system Python lacks:
`uv venv /tmp/qpy && uv pip install --python /tmp/qpy/bin/python jupyter scikit-learn matplotlib seaborn pandas scipy plotly umap-learn`,
then `QUARTO_PYTHON=/tmp/qpy/bin/python quarto render <deck>.qmd`. `*.html` / `*_files/` are globally ignored with
a per-year negation in `.gitignore` — add new course years there or renders stay
uncommitted.

**Lab decks must be rendered `--to revealjs`.** The VisML lab `.qmd`s under `labs/<topic>/lab.qmd` (some, not all) declare
both `revealjs` and `html` formats; a plain `quarto render` writes both to the same
`<name>.html` and the html one wins, so the link on the site serves a scrolling page instead of
slides (and speaker notes become `div.notes`, which reveal ignores). Their Python cells also need
`lime`, `shap` and `umap-learn` on top of the venv above.

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




**Slide layouts**: six canonical layouts (full-bleed, statement + figure, 40/60 text|figure,
centred `.nostretch`, comparison, text-only) with the sizing rules that actually hold under this
theme are in `slide-templates/LAYOUTS.md`; `slide-templates/layout-templates.qmd` renders one
slide per layout. Pick the layout from the figure's aspect ratio, not the amount of text. Two
traps: `width=` alone does not disable auto-stretch (add `.nostretch`), and images inside
`.columns` need `height="760"` (square/tall) or `width="100%"` (landscape).

## Reference Management

**PDF Naming**: `LastName_Year_Short_Title.pdf`

**Footer Citations**:
```markdown
:::footer
Author, A. (Year). [*Title*](../refs/Author_Year_Title.pdf). Venue.
:::
```

**Venue Abbreviations**: IEEE TVCG, CHI, ICML, AISTATS, ECML-PKDD