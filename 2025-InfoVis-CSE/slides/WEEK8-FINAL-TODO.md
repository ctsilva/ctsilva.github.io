# Week 8 - Final TODO List

**Last Updated:** October 23, 2025

## ✅ COMPLETED

- Updated normalization example to use Tissot projection distortion (better pedagogical fit)
- Renamed `image63.png` → `tissot-equirectangular.png`
- Renamed `image76.png` → `tissot-circles-comparison.png`
- Created duplicate solution figures (election-choropleth-bad, nyt-proportional-lead-solution, nyt-cartogram-solution)
- All foundational figures in place (23/28 figures complete)

## ⚠️ STILL NEEDED (5 figures)

### 1. binning-comparison.png
**Location:** Slide 18 (Pitfall 2: Classification)
**Source:** PPTX Slides 213-219
**Action Required:** Create a composite image showing three maps side-by-side:
- Equal Interval binning
- Quantile binning
- Natural Breaks (Jenks) binning

**Suggestion:** Screenshot or extract individual maps and combine in image editor, OR take screenshot of a slide that shows all three together.

---

### 2. rainbow-colorscale-bad.png
**Location:** Slide 20 (Pitfall 3: Color - Bad Example)
**Source:** PPTX Slides 221-222
**Action Required:** Extract map showing rainbow color scale

---

### 3. good-sequential-scale.png
**Location:** Slide 21 (Pitfall 3: Color - Good Example 1)
**Source:** PPTX Slides 221-222 or create from ColorBrewer
**Action Required:** Extract or create map with proper sequential scale (e.g., Blues, YlOrRd, Viridis)

---

### 4. good-diverging-scale.png
**Location:** Slide 21 (Pitfall 3: Color - Good Example 2)
**Source:** PPTX Slides 221-222 or create from ColorBrewer
**Action Required:** Extract or create map with proper diverging scale (e.g., RdBu, BrBG)

---

### 5. election-2016-red.png
**Location:** Slide 22 (Pitfall 4: Geography/MAUP)
**Source:** PPTX Slides 66-67
**Action Required:** Extract the famous "sea of red" 2016 election map

---

## 📊 Progress: 82% Complete (23/28 figures)

## 🎯 Extraction Instructions

### Option 1: From PPTX (recommended)
```bash
cd ~/Dropbox/2025-CS-GY-6313/bertini/InfoVis\ Material/Lecture\ slides/
open "7-Visualizing Geographical Data.pptx"
# Navigate to slides 66-67, 213-219, 221-222
# Right-click images → "Save as Picture" → save to:
#   ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week8/
```

### Option 2: Screenshot Method
```bash
# Open PowerPoint, go to slide
# Take screenshot (Cmd+Shift+4 on Mac)
# Crop and save with appropriate filename
```

### Option 3: Alternative Sources
- **ColorBrewer examples:** https://colorbrewer2.org (for good color scales)
- **2016 Election map:** Search for "2016 election map county level" - many public sources

---

## ✅ After Extraction

1. **Verify all 5 images are in place:**
   ```bash
   cd ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/figs/week8/
   ls -lh binning-comparison.png rainbow-colorscale-bad.png \
         good-sequential-scale.png good-diverging-scale.png \
         election-2016-red.png
   ```

2. **Re-render slides:**
   ```bash
   cd ~/github/ctsilva.github.io/2025-InfoVis-CSE/slides/
   quarto render week8-geovis-2d-maps.qmd
   ```

3. **Preview:**
   ```bash
   quarto preview week8-geovis-2d-maps.qmd
   ```

4. **Commit:**
   ```bash
   git add week8-geovis-2d-maps.qmd week8-geovis-2d-maps.html \
           week8-geovis-2d-maps_files/ figs/week8/
   git commit -m "Week 8 Lecture 1: Complete geovisualization fundamentals slides"
   ```

---

## 📝 Notes

- **Slides currently render** but will show broken image placeholders for the 5 missing figures
- The normalization example was improved - it now uses Tissot circles to demonstrate projection distortion, which ties nicely into the broader projection discussion
- All other sections are complete and ready for presentation
