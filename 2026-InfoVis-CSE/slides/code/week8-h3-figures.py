"""Generate the two H3 figures for the Week 8 geography (MAUP) pitfall.

1. figs/week8/h3-uber-explainer.png
   Six figures from Brodsky, "H3: Uber's Hexagonal Hierarchical Spatial Index"
   (Uber Engineering blog, 2018), composed into one slide image:
   points -> H3 cells -> shaded counts, and triangle/square/hexagon neighbors.

2. figs/week8/h3-nyc-crashes-resolutions.png
   NYC motor-vehicle crashes for September 2025 (NYC Open Data, dataset
   h9gi-nx95, rows with coordinates) counted in H3 cells at resolutions 7, 8, 9.

Run from 2026-InfoVis-CSE/slides:
    python code/week8-h3-figures.py
Needs: h3 (v4), geopandas, matplotlib, pandas, pillow, shapely.
"""
import io
import os
import urllib.parse
import urllib.request

import geopandas as gpd
import h3
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PIL import Image
from shapely.geometry import Polygon

HERE = os.path.dirname(__file__)
CACHE = os.path.join(HERE, ".cache")
FIGS = os.path.join(HERE, "..", "figs", "week8")
UA = {"User-Agent": "Mozilla/5.0"}

# Original image assets behind the Uber blog post (in article order 2,3,4,10,11,12)
UBER = "https://tb-static.uber.com/prod/udam-assets/"
UBER_IMAGES = {
    "points": "971dc5a0-ebda-515d-8941-6d4364587e7a.png",
    "cells": "ddf580d4-64a1-5186-b255-83b720f55b89.png",
    "counts": "0dd0a719-2440-5078-a11d-e717aaff7681.png",
    "triangles": "72b82fa8-71a4-53e7-a5bb-ce17b61bfabe.png",
    "squares": "b81c40ee-4b27-5f8e-bf1e-3dfe057909eb.png",
    "hexagons": "c9170bc3-2de6-5cea-9d71-38f6d59603bd.png",
}


def fetch(url, name):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, name)
    if not os.path.exists(path):
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req) as r, open(path, "wb") as f:
            f.write(r.read())
    return path


# ---------------------------------------------------------------- figure 1
def uber_explainer(asset_ids):
    imgs = {k: Image.open(fetch(UBER + v, f"uber-{k}.png")).convert("RGB") for k, v in asset_ids.items()}
    # map tiles have a black band at the bottom; neighbor diagrams have a dark frame
    for k in ("points", "cells", "counts"):
        w, h = imgs[k].size
        imgs[k] = imgs[k].crop((0, 0, w, int(h * 0.865)))
    for k in ("triangles", "squares", "hexagons"):
        w, h = imgs[k].size
        imgs[k] = imgs[k].crop((int(w * 0.12), int(h * 0.15), int(w * 0.88), int(h * 0.85)))

    fig, axs = plt.subplots(2, 3, figsize=(19.2, 9.4), dpi=100,
                            gridspec_kw=dict(height_ratios=[1.25, 1], hspace=0.16, wspace=0.05))
    top = [("points", "1. Events (cars) as points"),
           ("cells", "2. Bucket into H3 hexagons"),
           ("counts", "3. Shade cells by count")]
    bottom = [("triangles", "Triangles: 3 neighbor distances"),
              ("squares", "Squares: 2 neighbor distances"),
              ("hexagons", "Hexagons: 1 neighbor distance")]
    for ax, (k, title) in zip(axs[0], top):
        ax.imshow(imgs[k]); ax.set_title(title, fontsize=19, fontweight="bold"); ax.axis("off")
    for ax, (k, title) in zip(axs[1], bottom):
        ax.imshow(imgs[k]); ax.set_title(title, fontsize=19, fontweight="bold"); ax.axis("off")
    out = os.path.join(FIGS, "h3-uber-explainer.png")
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- figure 2
def nyc_crashes():
    q = urllib.parse.urlencode({
        "$select": "latitude,longitude",
        "$where": "crash_date between '2025-09-01T00:00:00' and '2025-09-30T23:59:59' "
                  "and latitude > 40.4 and latitude < 41 and longitude > -74.3 and longitude < -73.6",
        "$limit": 50000,
    })
    pts = pd.read_csv(fetch("https://data.cityofnewyork.us/resource/h9gi-nx95.csv?" + q,
                            "nyc-crashes-2025-09.csv"))
    boros = gpd.read_file(fetch("https://data.cityofnewyork.us/resource/gthc-hcne.geojson",
                                "nyc-boroughs.geojson")).to_crs(2263)

    fig, axs = plt.subplots(1, 3, figsize=(19.2, 8.0), dpi=100, gridspec_kw=dict(wspace=0.02))
    stats = []
    for ax, res in zip(axs, (7, 8, 9)):
        cells = pts.apply(lambda r: h3.latlng_to_cell(r.latitude, r.longitude, res), axis=1)
        counts = cells.value_counts()
        polys = [Polygon([(lng, lat) for lat, lng in h3.cell_to_boundary(c)]) for c in counts.index]
        g = gpd.GeoDataFrame({"n": counts.values}, geometry=polys, crs=4326).to_crs(2263)
        boros.plot(ax=ax, color="#eeeeee", edgecolor="#bbbbbb", linewidth=0.6)
        g.plot(ax=ax, column="n", cmap="magma_r", linewidth=0.15, edgecolor="white",
               legend=True, legend_kwds=dict(orientation="horizontal", shrink=0.7, pad=0.01,
                                             label="crashes per cell"))
        tops = g[g.n == g.n.max()]
        for c in tops.geometry.centroid:  # circle every cell tied for the most crashes
            ax.add_patch(plt.Circle((c.x, c.y), 9000, fill=False, ec="#00a0ff", lw=2.5))
        km2 = h3.average_hexagon_area(res, "km^2")
        tie = f" ({len(tops)}-way tie)" if len(tops) > 1 else ""
        ax.set_title(f"Resolution {res}: cells ≈ {km2:.2g} km²\n{len(counts):,} cells, busiest = {int(g.n.max())} crashes{tie}",
                     fontsize=17)
        ax.set_aspect("equal"); ax.axis("off")
        top_ll = h3.cell_to_latlng(counts.index[0])
        stats.append((res, len(counts), int(counts.iloc[0]), round(counts.median(), 1),
                      int((counts == 1).sum()), top_ll))
    out = os.path.join(FIGS, "h3-nyc-crashes-resolutions.png")
    fig.savefig(out, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("crashes", len(pts))
    for s in stats:
        print("res %d: %d cells, max %d, median %.1f, cells with 1 crash %d, busiest cell center %s" % s)


if __name__ == "__main__":
    uber_explainer(UBER_IMAGES)
    nyc_crashes()
