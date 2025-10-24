# Week 9 Figure Extraction Checklist (UPDATED)

This document lists all figures needed for the **comprehensive** `week9-urban-flows-interactivity.qmd` (23 parts, ~80 slides). Extract and rename them according to the naming scheme below.

## Source Files

- **Primary PDF**: `/Users/csilva/Dropbox/2025-CS-GY-6313/TaxiVisInstructions.pdf`
- **Research Paper**: Look for TaxiVis paper PDFs (likely in same directory or subdirectory)
- **Note**: Some figures will need to be created or found from external sources

## Destination Directory

All figures should be saved to: `2025-InfoVis-CSE/slides/figs/week9/`

---

## Extraction Methods

### For PDF (using pdfimages):

```bash
cd ~/Dropbox/2025-CS-GY-6313/
pdfimages -all TaxiVisInstructions.pdf ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week9/temp-pdf
# Then manually identify and rename the extracted images
```

### Alternative: Screenshot/Extract Pages

Since TaxiVisInstructions.pdf likely contains UI screenshots, you may want to:
1. Open the PDF
2. Take high-quality screenshots of specific pages
3. Crop to focus on relevant UI components
4. Save with descriptive names

### For Research Paper Figures

If you have access to the TaxiVis research paper:
1. Extract figures from the paper PDF
2. Use pdfimages or screenshot method
3. Figure numbers are referenced in the checklist below (e.g., "Figure 2 from paper")

---

## Required Figures Checklist

### Title Slide & Introduction (Slides 1-2)

- [ ] **yellow-blob-taxi-heatmap.png** - Static heatmap of all 140M NYC taxi trips
  - Source: Create from data or find representative "overplotted" heatmap
  - Alternative: Screenshot from TaxiVis showing unfiltered view
  - Note: This is the "before" image showing the problem

### Part 1: The Urban Context (Slides 3-5)

- [ ] **hagerstrand-space-time-cube.png** - Hägerstrand's Space-Time Cube diagram
  - Source: Find classic diagram online (public domain versions available)
  - Should show: X-Y geographic plane with Time as vertical axis
  - Should depict: Individual trajectories as lines through the cube
  - Alternative: Create simple 3D diagram

### Part 2: Why Traditional Analysis Fails (Slides 6-8)

- [ ] **traditional-workflow.png** - Traditional analysis pipeline diagram
  - Source: Create simple flow diagram showing:
    1. Domain experts → 2. Data scientists → 3. Analyses → 4. Results → 5. Repeat
  - Style: Simple boxes and arrows
  - Alternative: Find similar workflow diagram

### Part 3: The Need for Interactivity (Slides 9-10)

- [ ] **mantra-overview.png** - Overview visualization example
  - Source: Can use yellow-blob or aggregate view
  - Alternative: Create simple diagram showing "all data"

- [ ] **mantra-filter.png** - Filtered subset visualization
  - Source: Create example showing filtered data (e.g., partial heatmap)
  - Alternative: Screenshot from TaxiVis showing filtered state

- [ ] **mantra-details.png** - Details-on-demand example
  - Source: Create example showing detailed information display (popup/tooltip)
  - Alternative: Screenshot from TaxiVis showing detail view

### Part 4: Enter TaxiVis (Slides 11-12)

- [ ] **taxi-patterns-anomalies.png** - Taxi activity patterns showing regularity and anomalies
  - Source: Research paper, Figure 2
  - Should show: Time series with marked events (Thanksgiving, hurricanes, etc.)
  - May need to create composite if not available

### Part 5: Design Requirements (Slide 13)

No new figures needed (text-only slide)

### Part 6: The Visual Query Model (Slides 14-15)

- [ ] **taxivis-visual-query-model.png** - TaxiVis interface showing visual query components
  - Source: TaxiVisInstructions.pdf or research paper, Figure 4
  - Should show: Polygons, arrows, time widgets, histograms with labels

### Part 7: TaxiVis Interface (Slides 16-17)

- [ ] **taxivis-full-interface.png** - Complete TaxiVis interface
  - Source: TaxiVisInstructions.pdf, Page 2
  - Should show: Full dashboard with map, control panel, temporal views

- [ ] **taxivis-labeled-components.png** - Interface with component labels
  - Source: TaxiVisInstructions.pdf, Page 4
  - Should show: Map view, Control panel, Temporal views labeled
  - Alternative: Create labeled version from taxivis-full-interface.png

### Part 8: Visual Queries in Action (Slides 18-19)

- [ ] **airport-comparison-query.png** - Airport comparison query setup
  - Source: Research paper, Figure 1 (or create composite)
  - Should show: Regions drawn around Manhattan, JFK, LGA with arrows

- [ ] **airport-comparison-results.png** - Side-by-side comparison of Sunday vs Monday
  - Source: Research paper, Figure 1
  - Should show: Split view with maps and scatter plots

### Part 9: Query Expressiveness (Slide 20)

No new figures needed (text-only slide)

### Part 10: Making It Interactive (Slide 21)

No new figures needed (text-only slide with performance metrics)

### Part 11: Visualization Techniques (Slides 22-24)

- [ ] **rendering-cluttered.png** - Completely cluttered map with all points
  - Source: Research paper, Figure 7(a)
  - Alternative: Create from yellow-blob image

- [ ] **rendering-lod.png** - Level of detail rendering in action
  - Source: Research paper, Figure 7(b)
  - Should show: Clear hierarchical sampling result

- [ ] **rendering-heatmap-continuous.png** - Pixel-based density heat map
  - Source: Research paper, Figure 7(c)
  - Should show: Continuous density visualization

- [ ] **rendering-heatmap-grid.png** - Grid-based aggregation map
  - Source: Research paper, Figure 7(d)
  - Should show: Choropleth-style neighborhood aggregation

- [ ] **multiple-views-comparison.png** - Sunday vs Monday airport comparison
  - Source: Can reuse airport-comparison-results.png
  - Alternative: Create from TaxiVis screenshots

### Part 12: Linked Views & Brushing (Slides 25-28)

- [ ] **taxivis-step1-default.png** - Default view showing all data
  - Source: TaxiVisInstructions.pdf, Page 2
  - Shows: Unfiltered view with yellow blob on map

- [ ] **taxivis-step2-brush-jfk.png** - User brushing/selecting JFK region
  - Source: TaxiVisInstructions.pdf, Page 17-18
  - Shows: JFK region highlighted/selected on map

- [ ] **taxivis-step3-jfk-temporal.png** - Linked views updated for JFK
  - Source: TaxiVisInstructions.pdf, Page 19
  - Shows: Time series and histograms filtered to JFK data

### Part 13: Temporal Queries (Slides 29-31)

- [ ] **taxivis-time-slice-selection.png** - Time series with time range highlighted
  - Source: TaxiVisInstructions.pdf, Page 6-7
  - Shows: User selecting 8am-10am rush hour on time series

- [ ] **taxivis-time-slice-map.png** - Map updated to show selected time slice
  - Source: TaxiVisInstructions.pdf, Page 6-7
  - Shows: Map showing only trips from selected time period

- [ ] **taxivis-recurrent-selection-ui.png** - Recurrent selection interface
  - Source: TaxiVisInstructions.pdf, Page 11-12
  - Shows: UI with day-of-week checkboxes and time range controls

- [ ] **taxivis-recurrent-weekday-morning.png** - Weekday morning pattern
  - Source: TaxiVisInstructions.pdf or create from data
  - Shows: Map with Mon-Fri 7-9am pattern

- [ ] **taxivis-recurrent-weekend-night.png** - Weekend night pattern
  - Source: TaxiVisInstructions.pdf or create from data
  - Shows: Map with Sat-Sun 10pm-2am pattern

### Part 14: Spatial Queries & Grouping (Slides 32-34)

- [ ] **taxivis-default-boundaries.png** - Default census tract boundaries
  - Source: TaxiVisInstructions.pdf, Page 36 (before merge)
  - Shows: Original fine-grained regions

- [ ] **taxivis-merged-midtown.png** - Custom merged region
  - Source: TaxiVisInstructions.pdf, Page 37 (after merge)
  - Shows: Multiple regions merged into one

- [ ] **taxivis-merge-step1-select.png** - Selecting multiple regions
  - Source: TaxiVisInstructions.pdf, Page 36
  - Shows: Multiple regions highlighted/selected

- [ ] **taxivis-merge-step2-button.png** - Merge button in control panel
  - Source: TaxiVisInstructions.pdf, Page 36-37
  - Shows: Close-up of merge button or control panel

- [ ] **taxivis-merge-step3-result.png** - Result of merge operation
  - Source: TaxiVisInstructions.pdf, Page 37
  - Shows: Merged region treated as single entity

### Part 15: Origin-Destination Queries (Slides 35-38)

- [ ] **taxivis-arrow-step1-select-tool.png** - Arrow tool selected
  - Source: TaxiVisInstructions.pdf, Page 32
  - Shows: Arrow tool button highlighted in toolbar

- [ ] **taxivis-arrow-step2-draw.png** - User drawing arrow JFK→LGA
  - Source: TaxiVisInstructions.pdf, Page 32
  - Shows: Arrow being drawn from JFK to LGA on map

- [ ] **taxivis-arrow-step3-result.png** - Dashboard filtered to JFK→LGA flow
  - Source: TaxiVisInstructions.pdf, Page 33
  - Shows: All views updated to show only trips matching that OD pair

### Part 16: Case Study 1 - Social Inequality (Slides 39-41)

- [ ] **case-study-inequality.png** - Taxi activity comparison across neighborhoods
  - Source: Research paper, Figure 8
  - Shows: Comparison of Midtown, UES, Greenwich Village, Harlem

- [ ] **case-study-inequality-comparison.png** - Harlem vs other neighborhoods
  - Source: Research paper, Figure 8
  - Shows: Bar charts or visualizations showing 10x difference

- [ ] **case-study-inequality-tips.png** - Tips and fare analysis for Harlem
  - Source: Research paper, Figure 9
  - Shows: Analysis of tips and fare/mile for different neighborhoods

### Part 17: Case Study 2 - Transportation Hubs (Slides 42-43)

- [ ] **case-study-hubs.png** - Transportation hubs comparison
  - Source: Research paper, Figure 10
  - Shows: JFK, LGA, Penn Station, Grand Central comparison

### Part 18: Case Study 3 - Temporal Exploration (Slides 44-45)

- [ ] **case-study-memorial-day.png** - Grid of maps showing each Monday in May
  - Source: Research paper, Figure 11
  - Shows: Multiple small maps arranged in grid

- [ ] **case-study-memorial-day-comparison.png** - Memorial Day vs regular Mondays
  - Source: Research paper, Figure 11 or create from data
  - Shows: Comparison highlighting the difference

### Part 19: Case Study 4 - Hurricane Sandy (Slides 46-48)

- [ ] **case-study-hurricane-sandy.png** - Daily heat maps showing Hurricane Sandy impact
  - Source: Research paper, Figure 12
  - Shows: Week of heat maps (Sunday before through Saturday after)

- [ ] **case-study-hurricane-irene.png** - Hurricane Irene impact on taxi trips
  - Source: Research paper, Figure 13
  - Shows: Similar weekly view for Hurricane Irene

### Part 20-22: Design Insights & Impact (Slides 49-51)

No new figures needed (text-only slides)

### Part 23: From TaxiVis to Urban Analytics (Slides 52-53)

- [ ] **visual-analytics-framework.png** - Visual analytics pipeline diagram
  - Source: Create diagram showing:
    1. Visualization (multiple representations)
    2. Data Analysis (topology, ML, patterns)
    3. Data Management (indices, GPU)
  - Style: Simple flow diagram with three connected components

### Summary & Conclusion (Slides 54-56)

No new figures needed (text-only slides, may reuse earlier figures)

---

## Summary of Required Figures

**Total figures needed: ~40+**

### Breakdown by Source:
- **TaxiVisInstructions.pdf**: ~20-25 figures (interface screenshots)
- **Research Paper**: ~10-15 figures (Figure 1, 2, 7-13)
- **Create/External**: ~5-10 figures (diagrams, conceptual illustrations)

### Priority Levels:

**HIGH PRIORITY** (Essential for core content):
- yellow-blob-taxi-heatmap.png
- taxivis-full-interface.png
- taxivis-step1/2/3 (linked views sequence)
- taxivis-arrow-step1/2/3 (OD queries)
- All case study figures (inequality, hubs, memorial day, hurricane)

**MEDIUM PRIORITY** (Enhances understanding):
- All rendering technique figures (LOD, heat maps)
- Temporal query figures (time slicing, recurrent selection)
- Merge regions sequence

**LOW PRIORITY** (Can be placeholders initially):
- Conceptual diagrams (traditional-workflow, visual-analytics-framework)
- Mantra illustrations (overview, filter, details)
- hagerstrand-space-time-cube (widely available online)

---

## Post-Extraction Steps

1. **Verify all images are in place:**
   ```bash
   cd ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week9/
   ls -la | wc -l  # Should show ~40+ files
   ```

2. **Check image quality:**
   - Open each image
   - Ensure UI elements and text are legible
   - Resize if needed (target: 1920px width or proportional)

3. **Clean up temporary directories:**
   ```bash
   rm -rf temp-pdf/
   ```

4. **Render the slides:**
   ```bash
   cd ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/
   quarto render week9-urban-flows-interactivity.qmd
   ```

5. **Preview the slides:**
   ```bash
   quarto preview week9-urban-flows-interactivity.qmd
   ```

6. **Commit to git:**
   ```bash
   cd ~/github/ctsilva.github.io/
   git add 2025-InfoVis-CSE/slides/week9-urban-flows-interactivity.qmd
   git add 2025-InfoVis-CSE/slides/week9-urban-flows-interactivity.html
   git add 2025-InfoVis-CSE/slides/week9-urban-flows-interactivity_files/
   git add 2025-InfoVis-CSE/slides/figs/week9/
   git commit -m "Add comprehensive Week 9 slides: Urban Visualization I with case studies"
   git push
   ```

---

## Tips for Efficient Extraction

1. **Start with TaxiVisInstructions.pdf**: This will give you most of the interface screenshots

2. **Find the research paper**: Look for files named like:
   - `taxivis_paper.pdf`
   - `ferreira_taxivis_*.pdf`
   - Or search for "TaxiVis" papers online

3. **Create simple diagrams first**: For conceptual figures like workflows and frameworks, create simple diagrams in PowerPoint/Keynote and export as PNG

4. **Batch processing**: Extract all PDF images at once, then identify and rename

5. **Placeholder strategy**: For figures you can't find, create simple placeholder images with the figure name as text. This allows you to render and preview the slides while you work on getting the actual images.

---

## Alternative: Find Research Paper Online

If you don't have the TaxiVis paper locally, you can find it online:

1. Search for: "TaxiVis: An Interactive Visualization System for Taxi Trajectories"
2. Authors: Ferreira, Poco, Vo, Freire, Silva
3. Conference: IEEE VAST 2013
4. Should be available as PDF from NYU or IEEE Xplore

The paper will have all the case study figures (Figures 8-13) that are referenced in the slides.
