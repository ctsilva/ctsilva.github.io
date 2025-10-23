# Week 9 Figure Extraction Checklist

This document lists all figures needed for `week9-urban-flows-interactivity.qmd`. Extract and rename them according to the naming scheme below.

## Source Files

- **PDF**: `/Users/csilva/Dropbox/2025-CS-GY-6313/TaxiVisInstructions.pdf`

## Destination Directory

All figures should be saved to: `2025-InfoVis-CSE/slides/figs/week9/`

---

## Extraction Method

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

---

## Required Figures Checklist

### Title Slide (Slide 1)

- [ ] **yellow-blob-taxi-heatmap.png** - Static heatmap of all 140M NYC taxi trips
  - Source: Create from data or find representative "overplotted" heatmap
  - Note: This is the "before" image showing the problem

### Part 1: Understanding Urban Data (Slides 2-3)

- [ ] **urban-data-scales.png** - Visualization showing different scales of urban data
  - Source: Create diagram showing human-level → metro-level scales
  - Alternative: Find illustration of multi-scale urban patterns

- [ ] **hagerstrand-space-time-cube.png** - Hägerstrand's Space-Time Cube diagram
  - Source: Find classic diagram or create clean illustration
  - Should show: X-Y geographic plane with Time as vertical axis
  - Should depict: Individual trajectories as lines through the cube

### Part 2: Interactivity (Slide 4)

- [ ] **mantra-overview.png** - Overview visualization example
  - Source: Can use yellow-blob or aggregate view

- [ ] **mantra-filter.png** - Filtered subset visualization
  - Source: Create example showing filtered data

- [ ] **mantra-details.png** - Details-on-demand example
  - Source: Create example showing detailed information display

### Part 3: TaxiVis Interface (Slides 5-6)

- [ ] **taxivis-full-interface.png** - Complete TaxiVis interface
  - Source: TaxiVisInstructions.pdf, Page 2

- [ ] **taxivis-labeled-components.png** - Interface with component labels
  - Source: TaxiVisInstructions.pdf, Page 4
  - Should show: Map view, Control panel, Temporal views labeled

### Part 4: Linked Views & Brushing (Slides 7-10)

- [ ] **taxivis-step1-default.png** - Default view showing all data
  - Source: TaxiVisInstructions.pdf, Page 2
  - Shows: Unfiltered view with yellow blob on map

- [ ] **taxivis-step2-brush-jfk.png** - User brushing/selecting JFK region
  - Source: TaxiVisInstructions.pdf, Page 17-18
  - Shows: JFK region highlighted/selected on map

- [ ] **taxivis-step3-jfk-temporal.png** - Linked views updated for JFK
  - Source: TaxiVisInstructions.pdf, Page 19
  - Shows: Time series and histograms filtered to JFK data

### Part 5: Temporal Queries (Slides 11-13)

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
  - Source: TaxiVisInstructions.pdf, Page 11-12 or create composite
  - Shows: Map with Mon-Fri 7-9am pattern

- [ ] **taxivis-recurrent-weekend-night.png** - Weekend night pattern
  - Source: TaxiVisInstructions.pdf, Page 11-12 or create composite
  - Shows: Map with Sat-Sun 10pm-2am pattern

### Part 6: Spatial Queries & Grouping (Slides 14-16)

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

### Part 7: Origin-Destination Queries (Slides 17-19)

- [ ] **taxivis-arrow-step1-select-tool.png** - Arrow tool selected
  - Source: TaxiVisInstructions.pdf, Page 32
  - Shows: Arrow tool button highlighted in toolbar

- [ ] **taxivis-arrow-step2-draw.png** - User drawing arrow JFK→LGA
  - Source: TaxiVisInstructions.pdf, Page 32
  - Shows: Arrow being drawn from JFK to LGA on map

- [ ] **taxivis-arrow-step3-result.png** - Dashboard filtered to JFK→LGA flow
  - Source: TaxiVisInstructions.pdf, Page 33
  - Shows: All views updated to show only trips matching that OD pair

### Part 8: Synthesis (Slides 20-21)

- [ ] **yellow-blob-taxi-heatmap-repeat.png** - Yellow blob (can reuse from Slide 1)
  - Source: Same as first yellow blob image

- [ ] **taxivis-full-interface-repeat.png** - Full interface (can reuse)
  - Source: Same as taxivis-full-interface.png from earlier

---

## Additional Notes

### Images That May Need Creation

Some images may not exist directly in the source PDF and may need to be created:

1. **urban-data-scales.png** - Create a diagram showing:
   - Individual pedestrian level
   - Street/block level
   - Neighborhood level
   - City-wide level

2. **hagerstrand-space-time-cube.png** - Find or create classic diagram:
   - Can search for "Hägerstrand space-time cube" online
   - Many public domain versions available
   - Key elements: 3D cube with X, Y (space) and Z (time), trajectories as lines

3. **mantra-*.png** files - Create simple diagrams illustrating Shneiderman's mantra:
   - Overview: Show aggregate/all data
   - Filter: Show subset of data
   - Details: Show specific information popup

### Screenshot Best Practices

When taking screenshots from TaxiVisInstructions.pdf:

1. **High resolution**: Use PDF viewer at high zoom level
2. **Crop carefully**: Remove excess whitespace but preserve context
3. **Consistent size**: Try to maintain similar dimensions for related images
4. **Clear UI elements**: Ensure buttons, labels, and interactions are visible
5. **Annotations**: If PDF has arrows/annotations, include them

### Image Processing

After extraction, you may want to:

```bash
# Resize images to consistent width (e.g., 1920px)
# Using ImageMagick:
mogrify -resize 1920x figs/week9/*.png

# Or using sips (macOS):
sips -Z 1920 figs/week9/*.png
```

---

## Post-Extraction Steps

After extracting and renaming all figures:

1. **Verify all images are in place:**
   ```bash
   cd ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week9/
   ls -la
   ```

2. **Check image quality:**
   - Open each image to ensure it's clear and readable
   - UI elements should be legible at presentation size
   - Resize if necessary (target: 1920x1080 or proportional)

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
   git commit -m "Add Week 9 Lecture 2: Urban Visualization I - Flows, Time & Interactivity"
   git push
   ```

---

## Summary of Required Figures

**Total figures needed: ~27**

- Title/Introduction: 1
- Urban data concepts: 2
- Mantra diagrams: 3
- TaxiVis interface: 2
- Linked views sequence: 3
- Temporal queries: 5
- Spatial queries/merging: 5
- OD queries: 3
- Synthesis: 2 (reused)
- Created/sourced externally: ~3

Most figures come from TaxiVisInstructions.pdf. A few conceptual diagrams need to be created or sourced from other references.
