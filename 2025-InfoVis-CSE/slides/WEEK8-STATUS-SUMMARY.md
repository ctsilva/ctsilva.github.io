# Week 8 Figure Extraction - STATUS SUMMARY

**Last Updated:** October 23, 2025

## ✅ COMPLETED (24/31 figures)

All foundational figures are in place:
- Title slide & historical (6/6) ✅
- When to use a map (2/2) ✅
- Projections (8/8) ✅
- Taxonomy (4/4) ✅
- Urban viz bridge (1/1) ✅
- Duplicate solution figures (3/3) ✅

## ⚠️ STILL NEEDED (7 figures)

### Pitfall 1: Normalization (2 figures)
- [ ] **twitter-raw-counts.png** - Number of Twitter Users (bad example)
  - Source: PPTX Slides 56-59
  - Possibly `image63.png` or `image76.png` (check these)

- [ ] **twitter-percentage.png** - Percentage of Twitter Users (good example)
  - Source: PPTX Slides 56-59
  - Possibly `image63.png` or `image76.png` (check these)

### Pitfall 2: Classification (1 figure)
- [ ] **binning-comparison.png** - Composite showing Equal Interval, Quantile, Natural Breaks
  - Source: PPTX Slides 213-219
  - **NOTE**: This needs to be manually created as a side-by-side composite

### Pitfall 3: Color (3 figures)
- [ ] **rainbow-colorscale-bad.png** - Map with rainbow scale
  - Source: PPTX Slides 221-222

- [ ] **good-sequential-scale.png** - Map with sequential scale
  - Source: PPTX Slides 221-222

- [ ] **good-diverging-scale.png** - Map with diverging scale
  - Source: PPTX Slides 221-222

### Pitfall 4: Geography (1 figure)
- [ ] **election-2016-red.png** - 2016 Election looking "all red"
  - Source: PPTX Slides 66-67

## 📋 YOUR TODO LIST

1. **Check mystery images:**
   ```bash
   cd ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week8/
   open image63.png  # Check if this is one of the Twitter maps
   open image76.png  # Check if this is one of the Twitter maps
   ```

2. **Extract remaining PPTX images** (if mystery images aren't the right ones):
   - Open `7-Visualizing Geographical Data.pptx`
   - Manually screenshot or extract from slides:
     - 56-59 (Twitter normalization)
     - 66-67 (2016 Election)
     - 213-219 (Binning methods - need to composite)
     - 221-222 (Color scales)

3. **Create composite for binning-comparison.png:**
   - Use image editing tool to combine 3 maps side-by-side
   - Or use screenshot of slide showing all three

4. **Rename and place files** in `figs/week8/`

5. **Re-render slides:**
   ```bash
   cd ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/
   quarto render week8-geovis-2d-maps.qmd
   ```

## 📊 PROGRESS: 77% Complete (24/31)

**Slides will render** but 7 images will show as broken until completed.
