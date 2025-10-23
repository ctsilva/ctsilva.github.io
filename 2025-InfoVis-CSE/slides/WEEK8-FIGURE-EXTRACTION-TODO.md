# Week 8 Figure Extraction Checklist

This document lists all figures needed for `week8-geovis-2d-maps.qmd`. Extract and rename them according to the naming scheme below.

## Source Files

- **PDF**: `/Users/csilva/Dropbox/2025-CS-GY-6313/heer-class/CSE512-Maps.pdf`
- **PPTX**: `/Users/csilva/Dropbox/2025-CS-GY-6313/bertini/InfoVis Material/Lecture slides/7-Visualizing Geographical Data.pptx`

## Destination Directory

All figures should be saved to: `2025-InfoVis-CSE/slides/figs/week8/`

---

## Extraction Methods

### For PDF (using pdfimages):

```bash
cd ~/Dropbox/2025-CS-GY-6313/heer-class/
pdfimages -all CSE512-Maps.pdf ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week8/temp-pdf
# Then manually identify and rename the extracted images
```

### For PPTX (using unzip):

```bash
cd ~/Dropbox/2025-CS-GY-6313/bertini/InfoVis\ Material/Lecture\ slides/
cp "7-Visualizing Geographical Data.pptx" temp-extract.zip
unzip temp-extract.zip
# Images will be in ppt/media/
cp ppt/media/* ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week8/temp-pptx/
# Then manually identify and rename the extracted images
rm -rf ppt/ [Content_Types].xml _rels/ docProps/ temp-extract.zip
```

---

## Required Figures Checklist

### Title Slide & Historical (Slides 1-3)

- [ ] **snow-cholera-map.png** - John Snow's Cholera Map (cover version)
  - Source: CSE512-Maps.pdf, Page 1

- [ ] **minard-napoleon.png** - Minard's Napoleon March (cover version)
  - Source: CSE512-Maps.pdf, Page 1

- [ ] **nyt-election-2020.png** - NYT 2020 Election Map (cover version)
  - Source: CSE512-Maps.pdf, Page 1

- [ ] **snow-cholera-detailed.png** - John Snow's Cholera Map (detailed version)
  - Source: CSE512-Maps.pdf, Page 1 or similar

- [ ] **ptolemy-map.png** - Ptolemy's Geographica
  - Source: CSE512-Maps.pdf, Page 3

- [ ] **minard-napoleon-detailed.png** - Minard's Map (detailed version)
  - Source: CSE512-Maps.pdf, Page 1

### When to Use a Map (Slides 4-5)

- [ ] **sales-map.png** - US states colored by sales value
  - Source: 7-Visualizing Geographical Data.pptx, Slides 10-11

- [ ] **sales-barchart.png** - Bar chart of sales by state
  - Source: 7-Visualizing Geographical Data.pptx, Slides 10-11

### Projections (Slides 6-9)

- [ ] **projection-concept.png** - 3D globe unpeeling onto 2D surface
  - Source: Find generic illustration or create placeholder

- [ ] **mercator-projection.png** - Basic Mercator projection
  - Source: CSE512-Maps.pdf, Page 28-29

- [ ] **albers-projection.png** - Albers Equal-Area projection
  - Source: CSE512-Maps.pdf, Page 30

- [ ] **azimuthal-projection.png** - Azimuthal Equidistant projection
  - Source: CSE512-Maps.pdf (find appropriate page)

- [ ] **tissot-mercator.png** - Tissot's Indicatrix on Mercator
  - Source: CSE512-Maps.pdf, Page 25-26

- [ ] **tissot-equal-area.png** - Tissot's Indicatrix on equal-area projection
  - Source: CSE512-Maps.pdf, Page 25-26

- [ ] **mercator-greenland-africa.png** - Mercator showing Greenland vs Africa comparison
  - Source: CSE512-Maps.pdf, Page 28-29

- [ ] **albers-us.png** - Albers projection of US
  - Source: CSE512-Maps.pdf, Page 30

### Taxonomy (Slides 10-13)

- [ ] **nyt-choropleth-winner.png** - NYT 2020 Election: By Winner
  - Source: CSE512-Maps.pdf, Page 37

- [ ] **nyt-proportional-lead.png** - NYT 2020 Election: Size of Lead
  - Source: CSE512-Maps.pdf, Page 38

- [ ] **nyt-cartogram-electoral.png** - NYT Electoral College Cartogram
  - Source: CSE512-Maps.pdf, Page 42

- [ ] **minard-coal-exports.png** - Minard's British Coal Exports (1864)
  - Source: CSE512-Maps.pdf, Page 45

### Pitfall 1: Normalization (Slides 16-17)

- [ ] **twitter-raw-counts.png** - Number of Twitter Users (bad example)
  - Source: 7-Visualizing Geographical Data.pptx, Slides 56-59

- [ ] **twitter-percentage.png** - Percentage of Twitter Users (good example)
  - Source: 7-Visualizing Geographical Data.pptx, Slides 56-59

### Pitfall 2: Classification (Slide 18)

- [ ] **binning-comparison.png** - Three maps showing Equal Interval, Quantile, Natural Breaks
  - Source: 7-Visualizing Geographical Data.pptx, Slides 213-219
  - Note: This may need to be a composite image showing all three methods

### Pitfall 3: Color (Slides 20-21)

- [ ] **rainbow-colorscale-bad.png** - Map with rainbow color scale (bad example)
  - Source: 7-Visualizing Geographical Data.pptx, Slides 221-222

- [ ] **good-sequential-scale.png** - Map with proper sequential color scale
  - Source: 7-Visualizing Geographical Data.pptx, Slides 221-222 or create example

- [ ] **good-diverging-scale.png** - Map with proper diverging color scale
  - Source: 7-Visualizing Geographical Data.pptx, Slides 221-222 or create example

### Pitfall 4: Geography/MAUP (Slides 22-23)

- [ ] **election-2016-red.png** - 2016 Election map looking "all red"
  - Source: 7-Visualizing Geographical Data.pptx, Slides 66-67

- [ ] **election-choropleth-bad.png** - Standard choropleth (misleading)
  - Source: Can reuse election-2016-red.png or similar

- [ ] **nyt-proportional-lead-solution.png** - NYT Size of Lead (solution)
  - Source: CSE512-Maps.pdf, Page 38 (may be duplicate of earlier image)

- [ ] **nyt-cartogram-solution.png** - NYT Electoral College cartogram (solution)
  - Source: CSE512-Maps.pdf, Page 42 (may be duplicate of earlier image)

### Urban Viz Bridge (Slide 24)

- [ ] **beck-tube-map.png** - Beck's London Tube Diagram
  - Source: CSE512-Maps.pdf, Page 49

---

## Post-Extraction Steps

After extracting and renaming all figures:

1. **Verify all images are in place:**
   ```bash
   cd ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week8/
   ls -la
   ```

2. **Check image quality:**
   - Open each image to ensure it's clear and readable
   - Resize if necessary (target: 1920x1080 or proportional)

3. **Clean up temporary directories:**
   ```bash
   rm -rf temp-pdf/ temp-pptx/
   ```

4. **Render the slides:**
   ```bash
   cd ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/
   quarto render week8-geovis-2d-maps.qmd
   ```

5. **Preview the slides:**
   ```bash
   quarto preview week8-geovis-2d-maps.qmd
   ```

6. **Commit to git:**
   ```bash
   cd ~/github/ctsilva.github.io/
   git add 2025-InfoVis-CSE/slides/week8-geovis-2d-maps.qmd
   git add 2025-InfoVis-CSE/slides/week8-geovis-2d-maps.html
   git add 2025-InfoVis-CSE/slides/week8-geovis-2d-maps_files/
   git add 2025-InfoVis-CSE/slides/figs/week8/
   git commit -m "Add Week 8 Lecture 1: Foundations of Geovisualization (2D Maps)"
   git push
   ```

---

## Notes

- **Duplicate images**: Some images are referenced multiple times (e.g., the NYT election maps). You can create symbolic links or copy the same file with different names if you prefer to keep them separate for organizational clarity.

- **Missing images**: If you can't find an exact match in the source materials, you may need to:
  - Create a simple placeholder image
  - Find a suitable Creative Commons or public domain alternative
  - Skip the image temporarily and add it later

- **Image format**: PNG is preferred for compatibility and quality. If extracted as JPEG, consider converting to PNG for slides with text overlays.

- **Resolution**: Aim for high-resolution images that will look crisp on a 1920x1080 presentation display.
