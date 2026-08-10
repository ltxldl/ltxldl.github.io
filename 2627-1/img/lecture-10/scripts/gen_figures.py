#!/usr/bin/env python3
"""Sinh hình SVG cho Bài 10 từ dữ liệu giá chỗ ở tại Santiago.

Mặc định tải mốc chụp 2026-06-29 từ Inside Airbnb. Có thể truyền đường dẫn tới
``listings.csv.gz`` làm đối số thứ nhất để chạy hoàn toàn cục bộ.
"""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent.parent
FONT_DIR = OUT.parent.parent / "revealjs" / "dist" / "theme" / "fonts" / "source-sans-pro"
for font_file in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(font_file))

INK, MUTED = "#333333", "#666666"
plt.rcParams.update({
    "font.family": "Source Sans Pro",
    "font.size": 13,
    "svg.fonttype": "path",
    "figure.facecolor": "none",
    "savefig.facecolor": "none",
    "text.color": INK,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
})
BLUE, ORANGE = "#1E93AB", "#E8890C"

URL = ("https://data.insideairbnb.com/chile/rm/santiago/"
       "2026-06-29/data/listings.csv.gz")
PATH = sys.argv[1] if len(sys.argv) > 1 else URL
df = pd.read_csv(PATH, usecols=["price"])
gia = (df["price"].str.replace("$", "", regex=False)
       .str.replace(",", "", regex=False).astype(float).dropna())
gia = gia[gia > 0]

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))

axes[0].hist(gia, bins=60, color=BLUE)
axes[0].set_title("Thang gốc: dồn hết vào một cột", fontsize=12.5)
axes[0].set_xlabel("giá (CLP/đêm)")
axes[0].set_ylabel("số chỗ ở")

axes[1].hist(np.log10(gia), bins=60, color=ORANGE)
axes[1].set_title("Thang log10: phân phối hiện rõ", fontsize=12.5)
axes[1].set_xlabel("log10(giá)")
p1, p99 = np.percentile(gia, [1, 99])
axes[1].axvline(np.log10(p1), color="#c0392b", ls="--", lw=1.6)
axes[1].axvline(np.log10(p99), color="#c0392b", ls="--", lw=1.6)
axes[1].text(np.log10(p99) + 0.08, axes[1].get_ylim()[1] * 0.82, "P99", color="#c0392b",
             fontweight="bold")
axes[1].text(np.log10(p1) - 0.32, axes[1].get_ylim()[1] * 0.82, "P1", color="#c0392b",
             fontweight="bold")

for ax in axes:
    ax.spines[["top", "right"]].set_visible(False)
fig.suptitle("Phân phối giá chỗ ở tại Santiago", fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "phan-phoi-gia.svg")
print("phan-phoi-gia.svg done")
