#!/usr/bin/env python3
"""Sinh hình cho Bài 12 (trực quan hoá cơ bản).
Chạy: python gen_figures.py <vis-listings.csv> <vis-reviews.csv>
"""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent.parent
plt.rcParams.update({
    "font.size": 13, "figure.facecolor": "white", "savefig.facecolor": "white",
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.alpha": 0.25, "grid.linewidth": 0.7,
})
BLUE, ORANGE, GRAY, GREEN = "#1E93AB", "#E8890C", "#8a8a8a", "#2E8B57"

LISTINGS = sys.argv[1] if len(sys.argv) > 1 else "listings.csv"
REVIEWS = sys.argv[2] if len(sys.argv) > 2 else "reviews.csv"
df = pd.read_csv(LISTINGS)
rv = pd.read_csv(REVIEWS, parse_dates=["date"])

# ---------------------------------------------------------------- anscombe
ans = {
    "I":   ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
            [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]),
    "II":  ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
            [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]),
    "III": ([10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
            [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]),
    "IV":  ([8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8],
            [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]),
}
fig, axes = plt.subplots(1, 4, figsize=(11, 2.9), sharey=True)
for ax, (ten, (x, y)) in zip(axes, ans.items()):
    ax.scatter(x, y, s=42, color=BLUE, alpha=0.85)
    b, a = np.polyfit(x, y, 1)
    xs = np.array([3, 20])
    ax.plot(xs, a + b * xs, color=ORANGE, lw=1.8)
    ax.set_title(f"Bộ {ten}", fontsize=12)
    ax.set_xlim(2, 20)
fig.suptitle("Bốn bộ dữ liệu — cùng mean, cùng phương sai, cùng đường hồi quy", fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "anscombe.png", dpi=150)
plt.close(fig)
print("anscombe.png")

# ---------------------------------------------------------------- anatomy
thang_du = rv[rv["date"] < "2026-07-01"].set_index("date").resample("ME").size().loc["2023":]
fig, ax = plt.subplots(figsize=(9.6, 4.9))
fig.subplots_adjust(top=0.80, bottom=0.20)
ax.plot(thang_du.index, thang_du.values, color=BLUE, lw=2.2)
ax.set_title("Review Airbnb ở Santiago tăng gấp ba trong ba năm", fontweight="bold", loc="left")
ax.set_xlabel("tháng")
ax.set_ylabel("số review / tháng")
peak = thang_du.idxmax()
ax.annotate(f"đỉnh {peak:%m/%Y}: {thang_du.max():,.0f}",
            xy=(peak, thang_du.max()), xytext=(-150, -6), textcoords="offset points",
            fontsize=12, color=ORANGE, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=ORANGE))
RED = "#c0392b"
# các chú thích "giải phẫu" đặt ngoài vùng vẽ
ax.text(0.0, 1.22, "① title — nói THÔNG ĐIỆP, không nói 'biểu đồ của…'",
        transform=ax.transAxes, fontsize=11.5, color=RED, style="italic")
ax.annotate("", xy=(0.02, 1.075), xytext=(0.035, 1.20), xycoords="axes fraction",
            arrowprops=dict(arrowstyle="->", color=RED))
ax.text(0.42, 0.55, "② annotation — chỉ vào điểm đáng nói", transform=ax.transAxes,
        fontsize=11.5, color=RED, style="italic", ha="left")
ax.text(0.045, 0.35, "③ nhãn trục\n+ đơn vị", transform=ax.transAxes, fontsize=11.5,
        color=RED, style="italic", ha="left")
ax.text(0.30, -0.24, "④ nguồn dữ liệu →", transform=ax.transAxes, fontsize=11.5,
        color=RED, style="italic", ha="right")
ax.text(1.0, -0.24, "Nguồn: Inside Airbnb, snapshot 29/06/2026", transform=ax.transAxes,
        fontsize=10, color="#777", ha="right")
fig.savefig(OUT / "anatomy.png", dpi=150)
plt.close(fig)
print("anatomy.png")

# ---------------------------------------------------------------- line (clean)
fig, ax = plt.subplots(figsize=(8.8, 3.6))
ax.plot(thang_du.index, thang_du.values, color=BLUE, lw=2.2)
ax.set_title("Thị trường Santiago phục hồi và tăng tốc sau 2023", fontweight="bold", loc="left")
ax.set_ylabel("số review / tháng")
fig.tight_layout()
fig.savefig(OUT / "line-reviews.png", dpi=150)
plt.close(fig)
print("line-reviews.png")

# ---------------------------------------------------------------- barh ranking
tk = df.groupby("neighbourhood")["price"].agg(median="median", n="size")
top = tk[tk["n"] >= 500].nlargest(8, "median").sort_values("median")
fig, ax = plt.subplots(figsize=(8.8, 4.2))
bars = ax.barh(top.index, top["median"], color=[ORANGE if i == len(top) - 1 else BLUE
                                                for i in range(len(top))], height=0.62)
ax.bar_label(bars, [f" {v/1000:,.0f}k" for v in top["median"]], fontsize=11)
ax.set_title("Lo Barnechea bỏ xa phần còn lại về giá trung vị", fontweight="bold", loc="left")
ax.set_xlabel("giá trung vị (CLP/đêm) — quận ≥ 500 listing")
ax.grid(axis="y", alpha=0)
fig.tight_layout()
fig.savefig(OUT / "barh-quan.png", dpi=150)
plt.close(fig)
print("barh-quan.png")

# ---------------------------------------------------------------- hist
gia = df.loc[df["price"] > 0, "price"]
fig, ax = plt.subplots(figsize=(8.8, 3.6))
ax.hist(np.log10(gia), bins=55, color=BLUE)
ax.set_title("Phân phối giá (log10): một đỉnh quanh ~60k CLP, đuôi phải dài", fontweight="bold",
             loc="left")
ax.set_xlabel("log10(giá CLP/đêm)")
ax.set_ylabel("số listing")
fig.tight_layout()
fig.savefig(OUT / "hist-gia.png", dpi=150)
plt.close(fig)
print("hist-gia.png")

# ---------------------------------------------------------------- scatter map
s = df.dropna(subset=["price"]).sample(6000, random_state=1)
mau = np.where(s["price"] > s["price"].median(), ORANGE, BLUE)
fig, ax = plt.subplots(figsize=(8.6, 4.6))
ax.scatter(s["longitude"], s["latitude"], s=6, c=mau, alpha=0.45, linewidths=0)
ax.set_title("Nửa đắt của thị trường (cam) dồn về đông bắc thành phố", fontweight="bold",
             loc="left", fontsize=12.5)
ax.set_xlabel("kinh độ")
ax.set_ylabel("vĩ độ")
ax.set_aspect("equal")
ax.grid(alpha=0.15)
from matplotlib.lines import Line2D
ax.legend(handles=[Line2D([], [], marker="o", ls="", color=BLUE, label="giá ≤ trung vị"),
                   Line2D([], [], marker="o", ls="", color=ORANGE, label="giá > trung vị")],
          frameon=False, loc="lower left", fontsize=11)
fig.tight_layout()
fig.savefig(OUT / "scatter-map.png", dpi=150)
plt.close(fig)
print("scatter-map.png")

# ---------------------------------------------------------------- y-axis truncation pair
mien = pd.Series({"Nguyên căn": 64.9, "Khách sạn": 117.1, "Phòng riêng": 34.2})
mien = mien[["Phòng riêng", "Nguyên căn", "Khách sạn"]]
fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.7))
for ax, (bat_dau, title, color) in zip(
        axes, [(30, "Trục y cắt từ 30: chênh lệch bị thổi phồng", "#c0392b"),
               (0, "Trục y từ 0: đúng tỷ lệ thật", GREEN)]):
    bars = ax.bar(mien.index, mien.values, color=BLUE, width=0.55)
    ax.set_ylim(bat_dau, 130)
    ax.set_title(title, fontsize=12.5, color=color, fontweight="bold")
    ax.bar_label(bars, [f"{v:.0f}k" for v in mien.values], fontsize=11)
    ax.set_ylabel("giá trung vị (nghìn CLP)")
    ax.grid(axis="x", alpha=0)
fig.tight_layout()
fig.savefig(OUT / "truc-y.png", dpi=150)
plt.close(fig)
print("truc-y.png")
