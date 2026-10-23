"""Generate figs/week8/classed-maps-comparison.png for the Week 8 binning slides.

Same county unemployment data, same five colors, three classing methods
(equal interval, quantile, Jenks/Fisher natural breaks). Under each map, the
histogram of all county rates shows where that method puts its class breaks.

Data: vega-datasets 2.8.0 `unemployment.tsv` (BLS LAUS county rates,
"generally consistent with levels reported in 2009") and `us-10m.json`
(county TopoJSON in lon/lat). Maps show the lower 48 states, projected to US Albers
equal-area (EPSG:5070) (AK, HI, PR and other territories omitted from the maps); the classing uses every county in the rate file.

Run from 2026-InfoVis-CSE/slides:
    python code/week8-classed-maps.py
Needs: geopandas, mapclassify, matplotlib, pandas (pyogrio for TopoJSON).
"""
import os
import urllib.request

import geopandas as gpd
import mapclassify
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

CDN = "https://cdn.jsdelivr.net/npm/vega-datasets@2.8.0/data/"
CACHE = os.path.join(os.path.dirname(__file__), ".cache")
OUT = os.path.join(os.path.dirname(__file__), "..", "figs", "week8", "classed-maps-comparison.png")
K = 5
COLORS = ["#ffffcc", "#a1dab4", "#41b6c4", "#2c7fb8", "#253494"]  # ColorBrewer YlGnBu-5


def fetch(name):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        urllib.request.urlretrieve(CDN + name, path)
    return path


rates = pd.read_csv(fetch("unemployment.tsv"), sep="\t", dtype={"id": str})
rates["id"] = rates["id"].str.zfill(5)
rates["pct"] = rates["rate"] * 100
counties = gpd.read_file(fetch("us-10m.json"), layer="counties")
counties["id"] = counties["id"].astype(str).str.zfill(5)
states = gpd.read_file(fetch("us-10m.json"), layer="states")
LOWER48 = lambda f: (f.str[:2].astype(int) <= 56) & ~f.str[:2].isin(["02", "15"])  # drop AK, HI, territories
counties = counties[LOWER48(counties["id"])].set_crs(4326, allow_override=True).to_crs(5070)
states = states[LOWER48(states["id"].astype(str).str.zfill(2))].set_crs(4326, allow_override=True).to_crs(5070)
gdf = counties.merge(rates, on="id", how="left")

y = rates["pct"].to_numpy()
methods = {
    "Equal interval": mapclassify.EqualInterval(y, k=K),
    "Quantile": mapclassify.Quantiles(y, k=K),
    "Natural breaks (Jenks)": mapclassify.FisherJenks(y, k=K),
}

fig = plt.figure(figsize=(19.2, 7.6), dpi=100)
gs = fig.add_gridspec(3, 3, height_ratios=[2.0, 0.36, 1.0], hspace=0.14, wspace=0.05)
bins_hist = np.arange(0, 31, 0.5)

for col, (name, mc) in enumerate(methods.items()):
    edges = [y.min()] + list(mc.bins)
    cls = np.searchsorted(mc.bins, gdf["pct"].to_numpy(), side="left")
    face = np.where(gdf["pct"].isna(), "#dddddd",
                    np.array(COLORS)[np.clip(cls, 0, K - 1)])

    ax = fig.add_subplot(gs[0, col])
    gdf.plot(ax=ax, color=face, linewidth=0)
    states.boundary.plot(ax=ax, color="white", linewidth=0.5)
    ax.set_aspect("equal"); ax.set_anchor("S")
    ax.axis("off")
    ax.set_title(name, fontsize=22, fontweight="bold", pad=2)

    # legend row: one equal-width swatch per class, with its range and county count
    lx = fig.add_subplot(gs[1, col])
    for i in range(K):
        lx.add_patch(plt.Rectangle((i, 0), 1, 1, fc=COLORS[i], ec="#888888", lw=0.6))
        lx.text(i + 0.5, 0.5, f"{edges[i]:.1f}–{mc.bins[i]:.1f}\nn={mc.counts[i]}",
                ha="center", va="center", fontsize=12.5,
                color="white" if i >= 3 else "black")
    lx.set_xlim(0, K); lx.set_ylim(0, 1); lx.axis("off")

    hx = fig.add_subplot(gs[2, col])
    n, b, patches = hx.hist(y, bins=bins_hist, edgecolor="none")
    centers = (b[:-1] + b[1:]) / 2
    for p, c in zip(patches, np.searchsorted(mc.bins, centers, side="left")):
        p.set_facecolor(COLORS[min(c, K - 1)])
        p.set_edgecolor("#999999"); p.set_linewidth(0.3)
    for edge in mc.bins[:-1]:
        hx.axvline(edge, color="#c23b22", lw=1.6)
    hx.set_xlim(0, 31)
    hx.set_yticks([])
    for s in ("top", "right", "left"):
        hx.spines[s].set_visible(False)
    hx.tick_params(labelsize=12)
    hx.set_xlabel("county unemployment rate (%); red lines = class breaks", fontsize=12)

fig.savefig(OUT, bbox_inches="tight", facecolor="white")
for name, mc in methods.items():
    print(name, "breaks", np.round(mc.bins, 1).tolist(), "counts", mc.counts.tolist())
print("n", len(y), "min", y.min(), "median", np.median(y), "max", y.max(),
      "missing geometry rates", int(gdf["pct"].isna().sum()))
