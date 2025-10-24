# Week 8 Supplemental Material - Implementation Guide

## Overview

Supplemental slides have been added to `week8-geovis-2d-maps.qmd` covering practical implementation topics.

## Added Content

### Part 7: When to Use a Map?
- **Slides**: 2
- **Content**: Decision framework for choosing maps vs. alternative visualizations
- **Key Concepts**:
  - X/Y encoding trade-off
  - Spatial questions vs. aggregate comparisons
  - Area bias problem

### Part 8: Geographic Data Formats
- **Slides**: 3
- **Content**: GeoJSON and TopoJSON formats
- **Key Concepts**:
  - GeoJSON structure (FeatureCollection, Feature, geometry, properties)
  - Three geometry types: Point, LineString, Polygon
  - TopoJSON optimization and topology awareness
  - Tools: MapShaper, topojson-client

### Part 9: Data Classification Methods
- **Slides**: 2
- **Content**: Choropleth binning methods
- **Key Concepts**:
  - Equal Interval
  - Quantile (Equal Count)
  - Jenks Natural Breaks
  - Comparison table with pros/cons
- **Visual**: Uses `binning-comparison.png`

### Part 10: Practical Implementation with Leaflet.js
- **Slides**: 4
- **Content**: Step-by-step coding tutorial
- **Key Concepts**:
  - HTML setup with CDN
  - Map initialization
  - Tile layers (OpenStreetMap)
  - GeoJSON layer integration
  - Interactive popups
- **Demo**: Live demo prompt with working example

## Supporting Files

### examples/example.geojson
NYU campus GeoJSON dataset with 4 features:
- **Point**: NYU Bobst Library
- **Point**: NYU Tandon School of Engineering
- **LineString**: W 4th Street
- **Polygon**: Washington Square Park

### examples/leaflet_example.html
Fully functional Leaflet.js demo:
- Interactive map centered on NYU Manhattan campus
- Base map tiles from OpenStreetMap
- GeoJSON features rendered with custom styling
- Click popups for each feature
- Ready to open in any modern browser

## Usage Instructions

### For Students

1. **View the slides**:
   ```bash
   cd 2025-InfoVis-CSE/slides/
   open week8-geovis-2d-maps.html
   ```

2. **Try the live demo**:
   ```bash
   cd 2025-InfoVis-CSE/slides/examples/
   open leaflet_example.html
   ```

3. **Explore the data**:
   ```bash
   cat example.geojson | jq .
   ```

### For Instructors

**During Lecture:**
1. Navigate to "SUPPLEMENTAL MATERIAL" section (after Acknowledgments)
2. Walk through Parts 7-9 as conceptual material
3. For Part 10 (Leaflet):
   - Show code slides with line-by-line highlighting
   - Switch to browser and open `examples/leaflet_example.html`
   - Demonstrate: pan, zoom, click features, show popups
   - Emphasize minimal code required (~30 lines)

**Live Coding Option:**
- Use `example.geojson` as starting point
- Build `leaflet_example.html` from scratch
- Or modify existing demo to add new features

## Technical Details

### Dependencies
- Leaflet.js 1.9.4 (loaded via CDN)
- OpenStreetMap tiles (free, no API key required)

### Browser Compatibility
- Works in all modern browsers (Chrome, Firefox, Safari, Edge)
- No build step or transpilation needed
- Pure vanilla JavaScript

### Customization Points

Students can easily modify:
1. **Map center/zoom**: Change `setView([lat, lon], zoom)`
2. **Tile provider**: Swap OpenStreetMap for Mapbox, CartoDB, etc.
3. **GeoJSON data**: Add their own features
4. **Styling**: Customize colors, weights, opacity
5. **Popups**: Add more data fields or HTML

## Pedagogical Notes

### Why These Topics?

1. **When to Use a Map**: Addresses common mistake of defaulting to maps
2. **GeoJSON**: Industry standard, students will encounter everywhere
3. **Classification**: Often hidden in software, crucial for honesty
4. **Leaflet**: Lowest barrier to entry for hands-on practice

### Learning Outcomes

After this material, students should be able to:
- Justify when to use (or not use) a geographic map
- Read and write basic GeoJSON
- Explain the trade-offs between classification methods
- Create a simple interactive web map from scratch
- Add custom GeoJSON data to a Leaflet map

### Assignment Ideas

1. **Map vs. Chart**: Given a dataset, create both and justify which is better
2. **Classification Comparison**: Same data, three different binning methods, analyze differences
3. **Custom Leaflet Map**: Create map of student's hometown with 5+ features
4. **GeoJSON Editor**: Build a simple tool to create/edit GeoJSON features

## File Locations

```
2025-InfoVis-CSE/slides/
├── week8-geovis-2d-maps.qmd           # Main slides (includes supplemental)
├── week8-geovis-2d-maps.html          # Rendered slides
├── examples/
│   ├── example.geojson                # NYU campus data
│   └── leaflet_example.html           # Working demo
└── figs/week8/
    └── binning-comparison.png         # Used in classification section
```

## Next Steps

### Potential Enhancements

1. **Add more examples**:
   - D3.js alternative to Leaflet
   - Mapbox GL JS for vector tiles
   - Observable notebooks

2. **Classification deep dive**:
   - Show actual histograms of data
   - Interactive tool to try different methods

3. **GeoJSON exercises**:
   - Parse a shapefile to GeoJSON
   - Simplify geometries with Mapshaper
   - Convert to TopoJSON

4. **Advanced Leaflet**:
   - Choropleth coloring from data
   - Clustering markers
   - Heat maps

## Resources for Students

- **Leaflet Documentation**: https://leafletjs.com/
- **GeoJSON Specification**: https://geojson.org/
- **GeoJSON.io**: https://geojson.io/ (interactive editor)
- **Mapshaper**: https://mapshaper.org/ (online tool)
- **Natural Earth Data**: https://www.naturalearthdata.com/ (free geographic data)
