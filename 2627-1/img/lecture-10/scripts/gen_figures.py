#!/usr/bin/env python3
"""Sinh hình cho Bài 10 từ listings Santiago thật (price).
Chạy: python gen_figures.py <đường_dẫn listings.csv.gz>
"""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent.parent
plt.rcParams.update({"font.size": 13, "figure.facecolor": "white", "savefig.facecolor": "white"})
BLUE, ORANGE = "#1E93AB", "#E8890C"

PATH = sys.argv[1] if len(sys.argv) > 1 else "listings.csv.gz"
df = pd.read_csv(PATH, usecols=["price"])
gia = (df["price"].str.replace("$", "", regex=False)
       .str.replace(",", "", regex=False).astype(float).dropna())
gia = gia[gia > 0]

fig, axes = plt.subplots(1, 2, figsize=(10, 3.8))

axes[0].hist(gia, bins=60, color=BLUE)
axes[0].set_title("Thang thường: một cột + vài chấm vô hình", fontsize=12.5)
axes[0].set_xlabel("giá (CLP/đêm)")
axes[0].set_ylabel("số listing")

axes[1].hist(np.log10(gia), bins=60, color=ORANGE)
axes[1].set_title("Thang log10: phân phối hiện nguyên hình", fontsize=12.5)
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
fig.suptitle("Cùng một cột giá — chọn ngưỡng outlier phải NHÌN phân phối trước", fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "phan-phoi-gia.png", dpi=150)
print("phan-phoi-gia.png done")
