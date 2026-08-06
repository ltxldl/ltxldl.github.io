#!/usr/bin/env python3
"""Sinh hai hình SVG cho Bài 8 từ dữ liệu đánh giá Santiago.

Mặc định đọc dữ liệu tại mốc chụp 2026-06-29 từ Inside Airbnb. Có thể truyền đường dẫn tới
``reviews.csv`` làm đối số thứ nhất để chạy hoàn toàn cục bộ.
"""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager
import matplotlib.pyplot as plt
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
BLUE, ORANGE, GRAY = "#1E93AB", "#E8890C", "#9aa3a8"

URL = ("https://data.insideairbnb.com/chile/rm/santiago/"
       "2026-06-29/visualisations/reviews.csv")
PATH = sys.argv[1] if len(sys.argv) > 1 else URL
SNAPSHOT = pd.Timestamp("2026-06-29")
rv = pd.read_csv(PATH, parse_dates=["date"])
rv = rv.loc[rv["date"] <= SNAPSHOT].copy()  # bỏ 204 ngày sau mốc chụp
theo_thang = rv.set_index("date").resample("ME").size()
theo_thang = theo_thang.loc["2016":"2026-05-31"]  # tháng đầy đủ cuối cùng

# ------------------------------------------------ theo tháng + cửa sổ trượt
fig, ax = plt.subplots(figsize=(9.6, 4.2))
ax.plot(theo_thang.index, theo_thang.values, color=GRAY, lw=1.1, label="Số đánh giá mỗi tháng")
ax.plot(theo_thang.index, theo_thang.rolling(6, center=True).mean(),
        color=BLUE, lw=2.6, label="Trung bình trượt 6 tháng")
ax.axvspan(pd.Timestamp("2020-03-01"), pd.Timestamp("2021-10-31"), color="#fbeaea", zorder=0)
ax.text(pd.Timestamp("2020-12-01"), theo_thang.max() * 0.92, "COVID-19", color="#c0392b",
        ha="center", fontweight="bold")
ax.set_title("Số đánh giá theo tháng tại Santiago", fontweight="bold")
ax.set_ylabel("số đánh giá")
ax.legend(frameon=False, loc="upper left")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT / "reviews-theo-thang.svg")
plt.close(fig)
print("reviews-theo-thang.svg done")

# ------------------------------------------------ seasonality profile
# Chỉ dùng các năm đầy đủ 2022–2025 để mỗi tháng góp mặt cùng số lần.
tron_nam = rv.loc[(rv["date"] >= "2022-01-01") & (rv["date"] <= "2025-12-31")]
thang_tb = tron_nam.groupby(tron_nam["date"].dt.month).size()
thang_tb = thang_tb / thang_tb.mean() * 100

fig, ax = plt.subplots(figsize=(8.6, 3.8))
colors = [ORANGE if m in (7, 8, 10, 11) else BLUE for m in thang_tb.index]
ax.bar(thang_tb.index, thang_tb.values, color=colors)
ax.axhline(100, color="#555", lw=1, ls="--")
ax.set_xticks(range(1, 13), [f"T{m}" for m in range(1, 13)])
ax.set_ylabel("chỉ số mùa vụ (100 = trung bình)")
ax.set_ylim(0, 140)
ax.set_title("Chỉ số mùa vụ theo tháng (2022–2025)", fontweight="bold")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT / "mua-vu.svg")
plt.close(fig)
print("mua-vu.svg done")
