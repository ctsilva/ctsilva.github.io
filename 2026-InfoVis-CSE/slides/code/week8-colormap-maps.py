"""Generate figs/week8/colormap-real-data.png for the Week 8 color-scale pitfall.

Same county unemployment data drawn with three continuous color scales
(rainbow/jet, viridis, diverging RdBu centered on the 2009 U.S. rate of 9.3%).
The bottom row shows each map's lightness only (CIE L*), which is roughly what
a grayscale printout preserves and what carries order for the eye.

Data: vega-datasets 2.8.0 `unemployment.tsv` (BLS LAUS county rates,
"generally consistent with levels reported in 2009") and `us-10m.json`
(county TopoJSON in lon/lat). Lower 48 only, US Albers equal-area (EPSG:5070).

Run from 2026-InfoVis-CSE/slides:
    python code/week8-colormap-maps.py
Needs: geopandas, matplotlib, pandas (pyogrio for TopoJSON).
"""
import os
import urllib.request

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import colors as mcolors

CDN = "https://cdn.jsdelivr.net/npm/vega-datasets@2.8.0/data/"
CACHE = os.path.join(os.path.dirname(__file__), ".cache")
OUT = os.path.join(os.path.dirname(__file__), "..", "figs", "week8", "colormap-real-data.png")
US_RATE_2009 = 9.3  # BLS CPS annual average, 2009
VMIN, VMAX = 0, 20


def fetch(name):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        urllib.request.urlretrieve(CDN + name, path)
    return path


def lightness_cmap(cmap, n=256):
    """Grayscale colormap carrying only the CIE L* of `cmap`."""
    rgb = cmap(np.linspace(0, 1, n))[:, :3]
    lin = np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)
    Y = lin @ np.array([0.2126, 0.7152, 0.0722])
    L = np.where(Y > 216 / 24389, 116 * np.cbrt(Y) - 16, Y * 24389 / 27)  # L* in 0..100
    g = L / 100
    return mcolors.ListedColormap(np.stack([g, g, g], axis=1)), L


rates = pd.read_csv(fetch("unemployment.tsv"), sep="\t", dtype={"id": str})
rates["id"] = rates["id"].str.zfill(5)
rates["pct"] = rates["rate"] * 100
LOWER48 = lambda f: (f.str[:2].astype(int) <= 56) & ~f.str[:2].isin(["02", "15"])
counties = gpd.read_file(fetch("us-10m.json"), layer="counties")
counties["id"] = counties["id"].astype(str).str.zfill(5)
counties = counties[LOWER48(counties["id"])].set_crs(4326, allow_override=True).to_crs(5070)
states = gpd.read_file(fetch("us-10m.json"), layer="states")
states = states[LOWER48(states["id"].astype(str).str.zfill(2))].set_crs(4326, allow_override=True).to_crs(5070)
gdf = counties.merge(rates, on="id", how="left")

panels = [
    ("Rainbow (jet)", plt.get_cmap("jet"), mcolors.Normalize(VMIN, VMAX),
     "lightness: dark – white – dark (not ordered)"),
    ("Sequential (viridis)", plt.get_cmap("viridis"), mcolors.Normalize(VMIN, VMAX),
     "lightness: dark → light (ordered)"),
    (f"Diverging, center = U.S. {US_RATE_2009}%", plt.get_cmap("RdBu_r"),
     mcolors.TwoSlopeNorm(vcenter=US_RATE_2009, vmin=VMIN, vmax=VMAX),
     "lightness: light center, dark ends (by design)"),
]

fig, axs = plt.subplots(2, 3, figsize=(19.2, 9.6), dpi=100,
                        gridspec_kw=dict(hspace=0.32, wspace=0.03))
for col, (name, cmap, norm, caption) in enumerate(panels):
    gray, L = lightness_cmap(cmap)
    for row, cm in enumerate([cmap, gray]):
        ax = axs[row, col]
        gdf.plot(ax=ax, column="pct", cmap=cm, norm=norm, linewidth=0,
                 missing_kwds=dict(color="#ffffff"))
        states.boundary.plot(ax=ax, color="#ffffff", linewidth=0.4)
        ax.set_aspect("equal"); ax.axis("off")
        sm = plt.cm.ScalarMappable(norm=norm, cmap=cm)
        cb = fig.colorbar(sm, ax=ax, orientation="horizontal", fraction=0.05, pad=0.01,
                          extend="max", ticks=[0, 5, US_RATE_2009, 15, 20] if col == 2 else [0, 5, 10, 15, 20])
        cb.ax.set_xticklabels(["0", "5", f"{US_RATE_2009}", "15", "20%"] if col == 2 else ["0", "5", "10", "15", "20%"])
        cb.ax.tick_params(labelsize=13)
        if row == 0:
            ax.set_title(name, fontsize=19, fontweight="bold", pad=4)
    axs[1, col].set_title(caption, fontsize=16, pad=4)

fig.savefig(OUT, bbox_inches="tight", facecolor="white")
y = rates["pct"]
print("counties", len(y), "median", y.median(), "above 20%:", int((y > VMAX).sum()))
for name, cmap, norm, _ in panels:
    _, L = lightness_cmap(cmap)
    i = int(np.argmax(L))
    print(name, "L* at 0%", round(L[0]), "max L*", round(L.max()), "at value",
          round(float(norm.inverse(i / 255)), 1), "L* at 20%", round(L[-1]))
