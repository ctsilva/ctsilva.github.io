# Generating Color Scale Figures

## Option 1: Use the HTML Generator
Open `single-hue-scale-generator.html` in a browser and take screenshots of:
1. Figure 1: The blue gradient scale
2. Figure 2: The luminance progression plot
3. Combined view showing both together

## Option 2: Observable Notebook Code
Create these figures in Observable (observablehq.com):

```javascript
// Figure 1: Single-Hue Gradient
{
  const width = 600;
  const height = 60;
  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]);

  const scale = d3.scaleSequential(d3.interpolateBlues).domain([0, 100]);

  // Create gradient
  const gradient = svg.append("defs")
    .append("linearGradient")
    .attr("id", "blue-gradient")
    .attr("x1", "0%").attr("x2", "100%");

  d3.range(100).forEach(i => {
    gradient.append("stop")
      .attr("offset", `${i}%`)
      .attr("stop-color", scale(i));
  });

  svg.append("rect")
    .attr("width", width)
    .attr("height", height)
    .attr("fill", "url(#blue-gradient)")
    .attr("stroke", "#ccc");

  return svg.node();
}
```

```javascript
// Figure 2: Luminance Plot
{
  const width = 600;
  const height = 250;
  const margin = {top: 20, right: 30, bottom: 40, left: 60};

  const svg = d3.create("svg").attr("viewBox", [0, 0, width, height]);

  // Generate luminance data
  const scale = d3.scaleSequential(d3.interpolateBlues).domain([0, 100]);
  const data = d3.range(0, 101, 2).map(i => {
    const color = d3.lab(scale(i));
    return {value: i, luminance: color.l};
  });

  // Scales
  const x = d3.scaleLinear()
    .domain([0, 100])
    .range([margin.left, width - margin.right]);

  const y = d3.scaleLinear()
    .domain([0, 100])
    .range([height - margin.bottom, margin.top]);

  // Line
  const line = d3.line()
    .x(d => x(d.value))
    .y(d => y(d.luminance))
    .curve(d3.curveMonotoneX);

  // Draw axes
  svg.append("g")
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).tickValues([0, 25, 50, 75, 100]));

  svg.append("g")
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y));

  // Labels
  svg.append("text")
    .attr("x", width/2)
    .attr("y", height - 5)
    .attr("text-anchor", "middle")
    .text("Data Value");

  svg.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 15)
    .attr("x", -height/2)
    .attr("text-anchor", "middle")
    .text("Luminance (L*)");

  // Draw line
  svg.append("path")
    .datum(data)
    .attr("fill", "none")
    .attr("stroke", "#2166ac")
    .attr("stroke-width", 2)
    .attr("d", line);

  return svg.node();
}
```

## Option 3: Python with Matplotlib
```python
import matplotlib.pyplot as plt
import numpy as np
from colorspacious import cspace_convert

# Create figure with subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 6))

# Generate blue scale
n_steps = 100
blues = plt.cm.Blues(np.linspace(0.1, 1, n_steps))

# Show gradient
gradient = np.vstack((blues[:, :3], blues[:, :3]))
ax1.imshow(gradient, aspect='auto', extent=[0, 100, 0, 1])
ax1.set_yticks([])
ax1.set_xlabel('Data Value')
ax1.set_title('Single-Hue Sequential Scale (Blue)')

# Calculate and plot luminance
luminance = []
for color in blues:
    lab = cspace_convert(color[:3], "sRGB1", "CIELab")
    luminance.append(lab[0])

ax2.plot(range(n_steps), luminance, 'b-', linewidth=2)
ax2.set_xlabel('Data Value')
ax2.set_ylabel('Luminance (L*)')
ax2.set_title('Monotonic Luminance Increase')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('single_hue_scale.png', dpi=150, bbox_inches='tight')
```

## Recommended Approach
1. Open the HTML file in Chrome/Firefox
2. Use browser developer tools (F12) to adjust size if needed
3. Take screenshots using:
   - Mac: Cmd+Shift+4 (select area)
   - Windows: Windows+Shift+S (snipping tool)
4. Save as `single-hue-gradient.png` and `luminance-progression.png`