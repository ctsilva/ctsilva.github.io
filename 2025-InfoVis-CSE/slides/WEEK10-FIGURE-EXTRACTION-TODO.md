# Week 10 Figure Extraction Checklist

This document lists all figures needed for `week10-urban-3d-simulation.qmd`. Extract and rename them according to the naming scheme below.

## Source Files

- **PPTX 1**: `/Users/csilva/Dropbox/2025-CS-GY-6313/urbane-vis2015 smaller.pptx`
- **PPTX 2**: `/Users/csilva/Dropbox/2025-CS-GY-6313/urbane-sigasia2015 smaller.pptx`

## Destination Directory

All figures should be saved to: `2025-InfoVis-CSE/slides/figs/week10/`

---

## Extraction Method

### For PPTX (using unzip):

```bash
cd ~/Dropbox/2025-CS-GY-6313/

# Extract from first PPTX
cp "urbane-vis2015 smaller.pptx" temp-extract-vis.zip
unzip temp-extract-vis.zip
# Images will be in ppt/media/
cp ppt/media/* ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week10/temp-vis/
rm -rf ppt/ [Content_Types].xml _rels/ docProps/ temp-extract-vis.zip

# Extract from second PPTX
cp "urbane-sigasia2015 smaller.pptx" temp-extract-sigasia.zip
unzip temp-extract-sigasia.zip
cp ppt/media/* ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week10/temp-sigasia/
rm -rf ppt/ [Content_Types].xml _rels/ docProps/ temp-extract-sigasia.zip

# Then manually identify and rename the extracted images
```

---

## Required Figures Checklist

### Opening & Recap (Slides 1-2)

- [ ] **urbane-title-3d-city.png** - Beautiful 3D rendering of city
  - Source: urbane-vis2015 smaller.pptx, Slide 1
  - Should be a hero image showing impressive 3D city visualization

- [ ] **recap-choropleth.png** - Example choropleth map from Week 8
  - Source: Can reuse from Week 8 figs (normalized choropleth example)
  - Alternative: Create simple representative example

- [ ] **recap-taxivis.png** - TaxiVis interface from Week 9
  - Source: Can reuse from Week 9 figs (taxivis-full-interface.png)
  - Alternative: Copy from week9 directory

### Part 1: Why 3D? (Slides 3-5)

- [ ] **lynch-five-elements.png** - Diagram of Lynch's 5 elements
  - Source: Create diagram or find online (classic urban planning diagram)
  - Should show: Paths, Edges, Districts, Nodes, Landmarks

- [ ] **lynch-elements-examples.png** - Examples in a real city
  - Source: Create or find annotated city map showing Lynch's elements
  - Alternative: Use Boston/NYC map with labeled examples

### Part 2: Urban Planning Challenge (Slides 6-8)

- [ ] **urbane-current-scenario.png** - Current scenario slide
  - Source: urbane-vis2015 smaller.pptx, Slides 8-11
  - Should show: "Intuition" and "Lack of tools" messaging

- [ ] **urbane-ideal-scenario.png** - Ideal/future scenario
  - Source: Create diagram or use from urbane-vis2015 smaller.pptx
  - Should show: Vision for data-driven tools

### Part 3: Urbane Interface (Slides 9-10)

- [ ] **urbane-full-interface.png** - Complete Urbane interface
  - Source: urbane-vis2015 smaller.pptx, Slide 46-47
  - Should show: 3D city view + scatterplot + parallel coordinates

- [ ] **urbane-labeled-interface.png** - Interface with component labels
  - Source: Create from urbane-full-interface.png with labels added
  - Alternative: Find annotated version in slides

### Part 4: 3D → 2D Linking (Slides 11-12)

- [ ] **urbane-3d-selection.png** - User selecting buildings in 3D
  - Source: urbane-vis2015 smaller.pptx (find interaction sequence)
  - Should show: Buildings highlighted in 3D view

- [ ] **urbane-scatterplot-highlight.png** - Selected buildings in scatterplot
  - Source: urbane-vis2015 smaller.pptx, Slide 48
  - Should show: Corresponding points highlighted in 2D scatterplot

### Part 5: 2D → 3D Linking (Slides 13-14)

- [ ] **urbane-parallel-coords-brush.png** - Brushing on parallel coordinates
  - Source: urbane-vis2015 smaller.pptx, Slide 50
  - Should show: User selecting ranges on parallel coordinates plot

- [ ] **urbane-scatterplot-brush.png** - Brushing on scatterplot
  - Source: urbane-vis2015 smaller.pptx, Slide 48
  - Should show: User selecting region in scatterplot

- [ ] **urbane-3d-filtered-result.png** - 3D view with filtered buildings highlighted
  - Source: urbane-vis2015 smaller.pptx (after brushing action)
  - Should show: Only selected buildings highlighted in 3D

### Part 6: Impact Analysis (Slides 15-19)

- [ ] **urbane-new-building-insert.png** - New building being added
  - Source: urbane-vis2015 smaller.pptx, Slide 29
  - Should show: New tall building in context

- [ ] **urbane-computing-impact.png** - System computing impact
  - Source: May need to create, or show progress/loading state
  - Alternative: Skip if not available

- [ ] **urbane-sky-exposure-before-after.png** - Sky exposure impact visualization
  - Source: urbane-vis2015 smaller.pptx, Slides 30-37
  - Should show: Heatmap of sky exposure changes (before/after composite)
  - May need to create side-by-side comparison

### Part 7: Performance-Driven Design (Slides 20-22)

- [ ] **urbane-sigasia-title.png** - SIGGRAPH Asia title slide
  - Source: urbane-sigasia2015 smaller.pptx, Slide 1
  - Should be: Title slide from the SIGGRAPH Asia paper

- [ ] **urbane-design-space-towers.png** - Various tower shapes/designs
  - Source: urbane-sigasia2015 smaller.pptx, Slides 23-26
  - Should show: Multiple building design variations (twisting, tapering, etc.)

- [ ] **urbane-view-score-diagram.png** - Diagram illustrating view score
  - Source: urbane-sigasia2015 smaller.pptx, Slide 30
  - Should show: How view quality is calculated

### Part 8: Precomputation & Exploration (Slides 23-26)

- [ ] **urbane-4d-texture.png** - 4D texture precomputation diagram
  - Source: urbane-sigasia2015 smaller.pptx, Slide 41-42
  - Should show: Concept of 4D view texture (x, y, z, direction)

- [ ] **urbane-exploration-interface.png** - Exploration interface overview
  - Source: urbane-sigasia2015 smaller.pptx, Slides 52-54
  - Should show: Scatterplot + 3D models

- [ ] **urbane-4d-texture-detail.png** - Detailed view of 4D texture
  - Source: urbane-sigasia2015 smaller.pptx, Slide 41-42
  - Alternative: Create diagram if needed

- [ ] **urbane-tradeoff-scatterplot.png** - Scatterplot of view score vs cost
  - Source: urbane-sigasia2015 smaller.pptx, Slides 52-54
  - Should show: X=cost, Y=view score, points=designs

- [ ] **urbane-scatterplot-brushed.png** - Brushed region on scatterplot
  - Source: urbane-sigasia2015 smaller.pptx (interaction sequence)
  - Should show: User selecting "sweet spot" region

- [ ] **urbane-selected-designs-3d.png** - 3D models of selected designs
  - Source: urbane-sigasia2015 smaller.pptx
  - Should show: Multiple building models corresponding to selection

### Part 9: Critical Reflection (Slide 27)

- [ ] **urbane-discussion-slide.png** - Discussion slide about 3D
  - Source: urbane-vis2015 smaller.pptx, Slide 55
  - Should show: Pros/cons discussion from original presentation

### Part 10: Grand Synthesis (Slides 28-30)

- [ ] **recap-week8-choropleth.png** - Week 8 recap image
  - Source: Reuse from earlier or Week 8 figs
  - Good normalized choropleth example

- [ ] **recap-week9-taxivis.png** - Week 9 recap image
  - Source: Reuse from Week 9 figs (taxivis-full-interface.png)

- [ ] **recap-week10-urbane.png** - Week 10 recap image
  - Source: Reuse urbane-full-interface.png from above

---

## Additional Notes

### Images That May Need Creation

1. **lynch-five-elements.png** - Classic urban planning diagram
   - Search for "Kevin Lynch five elements" online
   - Many public domain versions available
   - Can create simple diagram with icons

2. **urbane-ideal-scenario.png** - May need to create
   - Show vision of integrated tools
   - Can be a conceptual diagram

3. **urbane-sky-exposure-before-after.png** - Composite image
   - May need to combine slides 30-37 from urbane-vis2015 smaller.pptx
   - Create side-by-side or before/after comparison

### Screenshot Best Practices

When taking screenshots from PowerPoint presentations:

1. **Open in presentation mode**: For clean, full-screen captures
2. **High resolution**: Export slides as images at maximum quality
3. **Crop consistently**: Remove black bars, keep aspect ratio
4. **Preserve animations**: If slides show step-by-step, capture each step separately

### PowerPoint Export Method (Alternative to Unzip)

```bash
# In PowerPoint:
# File → Export → File Format: PNG
# This will export each slide as a high-res image

# Or use command line (macOS):
# First, install imagemagick if not already installed
# brew install imagemagick

# Convert PPTX to images (requires libreoffice)
# brew install libreoffice
# Then:
soffice --headless --convert-to pdf "urbane-vis2015 smaller.pptx"
magick convert -density 300 "urbane-vis2015 smaller.pdf" figs/week10/slide-%03d.png
```

### Image Processing

After extraction:

```bash
# Resize to consistent width
mogrify -resize 1920x figs/week10/*.png

# Or using sips (macOS)
sips -Z 1920 figs/week10/*.png
```

---

## Post-Extraction Steps

1. **Verify all images are in place:**
   ```bash
   cd ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week10/
   ls -la
   ```

2. **Check image quality:**
   - Open each image
   - Ensure UI elements and text are legible
   - Resize if needed

3. **Clean up temporary directories:**
   ```bash
   rm -rf temp-vis/ temp-sigasia/
   ```

4. **Render the slides:**
   ```bash
   cd ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/
   quarto render week10-urban-3d-simulation.qmd
   ```

5. **Preview the slides:**
   ```bash
   quarto preview week10-urban-3d-simulation.qmd
   ```

6. **Commit to git:**
   ```bash
   cd ~/github/ctsilva.github.io/
   git add 2025-InfoVis-CSE/slides/week10-urban-3d-simulation.qmd
   git add 2025-InfoVis-CSE/slides/week10-urban-3d-simulation.html
   git add 2025-InfoVis-CSE/slides/week10-urban-3d-simulation_files/
   git add 2025-InfoVis-CSE/slides/figs/week10/
   git commit -m "Add Week 10 Lecture 3: Urban Visualization II - 3D, Form & Simulation"
   git push
   ```

---

## Summary of Required Figures

**Total figures needed: ~30**

- Opening/Recap: 3
- Lynch framework: 2
- Urban planning: 2
- Urbane interface: 2
- 3D→2D linking: 2
- 2D→3D linking: 3
- Impact analysis: 3
- Performance-driven design: 3
- Precomputation: 6
- Critical reflection: 1
- Grand synthesis: 3

**Sources:**
- urbane-vis2015 smaller.pptx: ~15 figures
- urbane-sigasia2015 smaller.pptx: ~10 figures
- Created/external: ~5 figures
- Reused from Weeks 8-9: ~3 figures

## Tips for Success

1. **Export all slides first**: Export both PowerPoint files as PNG images, then identify and rename
2. **Use descriptive names**: Follow the naming scheme exactly for easy debugging
3. **Create composites carefully**: Some figures need multiple slides combined (e.g., before/after)
4. **Test incrementally**: Render slides after adding each batch of figures to catch issues early
5. **Document sources**: Keep notes on which original slide each figure came from
