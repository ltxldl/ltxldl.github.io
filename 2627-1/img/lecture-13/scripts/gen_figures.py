#!/usr/bin/env python3
"""Sinh hình cho Bài 13: seaborn nâng cao + choropleth + bộ 'hình AI lỗi' để phê bình.
Chạy: python gen_figures.py <vis-listings.csv> <vis-reviews.csv>
(geojson tải trực tiếp từ Inside Airbnb)
"""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

OUT = Path(__file__).resolve().parent.parent
BLUE, ORANGE, GRAY = "#1E93AB", "#E8890C", "#8a8a8a"
plt.rcParams.update({"font.size": 12.5, "figure.facecolor": "white", "savefig.facecolor": "white"})

LISTINGS = sys.argv[1]
REVIEWS = sys.argv[2]
df = pd.read_csv(LISTINGS)
df = df[df["price"].notna() & (df["price"] > 0)]
rv = pd.read_csv(REVIEWS, parse_dates=["date"])

# ---------------------------------------------------------------- seaborn box (log)
sns.set_theme(style="whitegrid", rc={"grid.alpha": 0.3, "font.size": 12})
thu_tu = ["Shared room", "Private room", "Entire home/apt", "Hotel room"]
fig, ax = plt.subplots(figsize=(8.8, 3.9))
sns.boxplot(data=df, x="price", y="room_type", order=thu_tu, color=BLUE,
            showfliers=False, ax=ax, width=0.55)
ax.set_xscale("log")
ax.set_xlabel("giá (CLP/đêm, thang log)")
ax.set_ylabel("")
ax.set_title("Mỗi loại phòng một tầng giá — nhưng các hộp chồng lấn đáng kể",
             loc="left", fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "box-gia-loai.png", dpi=150)
plt.close(fig)
print("box-gia-loai.png")

# ---------------------------------------------------------------- heatmap
quan_lon = df["neighbourhood"].value_counts().head(8).index
pv = (df[df["neighbourhood"].isin(quan_lon)]
      .pivot_table(values="price", index="neighbourhood", columns="room_type", aggfunc="median")
      [["Entire home/apt", "Private room"]] / 1000)
fig, ax = plt.subplots(figsize=(7.6, 4.2))
sns.heatmap(pv.sort_values("Entire home/apt", ascending=False), annot=True, fmt=".0f",
            cmap="Blues", cbar_kws={"label": "giá trung vị (nghìn CLP)"}, ax=ax)
ax.set_title("Khoảng cách giá nguyên căn – phòng riêng nới rộng ở quận đắt",
             loc="left", fontweight="bold", fontsize=12.5)
ax.set_xlabel(""); ax.set_ylabel("")
fig.tight_layout()
fig.savefig(OUT / "heatmap-quan-loai.png", dpi=150)
plt.close(fig)
print("heatmap-quan-loai.png")

# ---------------------------------------------------------------- choropleth
import geopandas as gpd
geo = gpd.read_file("https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/"
                    "visualisations/neighbourhoods.geojson")
kpi = df.groupby("neighbourhood").agg(gia=("price", "median"), n=("price", "size")).reset_index()
geo2 = geo.merge(kpi, on="neighbourhood", how="left")
fig, ax = plt.subplots(figsize=(8.4, 5.6))
geo2.plot(column="gia", cmap="Blues", legend=True, ax=ax, edgecolor="#999", linewidth=0.5,
          legend_kwds={"label": "giá trung vị (CLP/đêm)", "shrink": 0.7},
          missing_kwds={"color": "#eeeeee", "label": "không đủ dữ liệu"})
ax.set_axis_off()
ax.set_title("Giá leo dần về phía đông bắc — đúng trục thu nhập của Santiago",
             loc="left", fontweight="bold", fontsize=13)
fig.tight_layout()
fig.savefig(OUT / "choropleth-gia.png", dpi=150)
plt.close(fig)
print("choropleth-gia.png")

# ================================================================ BỘ HÌNH "AI LỖI"
plt.rcdefaults()
plt.rcParams.update({"font.size": 12, "figure.facecolor": "white", "savefig.facecolor": "white"})

# (a) dual axis — tương quan giả
thang = rv[rv["date"] < "2026-07-01"].set_index("date").resample("ME").size().loc["2024":]
gia_thang = pd.Series(  # giá trung vị giả lập trượt nhẹ để minh hoạ trục kép đánh lừa
    np.linspace(55, 62, len(thang)) + np.random.default_rng(3).normal(0, 1.2, len(thang)),
    index=thang.index)
fig, ax1 = plt.subplots(figsize=(8.8, 3.8))
ax1.plot(thang.index, thang.values, color=BLUE, lw=2, label="số review")
ax1.set_ylabel("số review", color=BLUE)
ax2 = ax1.twinx()
ax2.plot(gia_thang.index, gia_thang.values, color="red", lw=2, ls="--", label="giá trung vị")
ax2.set_ylabel("giá trung vị (nghìn CLP)", color="red")
ax2.set_ylim(54, 63)
ax1.set_title("Demand and Price Analysis — Santiago Airbnb Market", fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "ai-loi-truc-kep.png", dpi=150)
plt.close(fig)
print("ai-loi-truc-kep.png")

# (b) pie 12 lát cầu vồng
quan12 = df["neighbourhood"].value_counts().head(12)
fig, ax = plt.subplots(figsize=(7.2, 4.6))
ax.pie(quan12.values, labels=quan12.index, autopct="%1.1f%%",
       colors=plt.cm.tab20.colors, startangle=90, textprops={"fontsize": 8.5})
ax.set_title("Distribution of Listings by Neighbourhood", fontweight="bold")
fig.tight_layout()
fig.savefig(OUT / "ai-loi-pie.png", dpi=150)
plt.close(fig)
print("ai-loi-pie.png")

# (c) hai thành phố, hai tiền tệ, MỘT trục
scl = np.linspace(52, 65, 24) + np.random.default_rng(1).normal(0, 1.5, 24)
rio = np.linspace(280, 340, 24) + np.random.default_rng(2).normal(0, 8, 24)
idx = pd.date_range("2024-07-31", periods=24, freq="ME")
fig, ax = plt.subplots(figsize=(8.8, 3.8))
ax.plot(idx, scl * 1000, lw=2, color=BLUE, label="Santiago (CLP)")
ax.plot(idx, rio, lw=2, color=ORANGE, label="Rio de Janeiro (BRL)")
ax.set_title("Price Comparison: Santiago vs Rio de Janeiro", fontweight="bold")
ax.set_ylabel("median price")
ax.legend()
fig.tight_layout()
fig.savefig(OUT / "ai-loi-hai-tien-te.png", dpi=150)
plt.close(fig)
print("ai-loi-hai-tien-te.png")

# (c-fixed) index hoá về 100
fig, ax = plt.subplots(figsize=(8.8, 3.8))
ax.plot(idx, scl / scl[0] * 100, lw=2.2, color=BLUE, label="Santiago")
ax.plot(idx, rio / rio[0] * 100, lw=2.2, color=ORANGE, label="Rio de Janeiro")
ax.axhline(100, color="#777", lw=1, ls="--")
ax.set_ylabel("chỉ số giá (tháng đầu = 100)")
ax.set_title("Cùng quy về mốc 100: Santiago tăng nhanh hơn Rio rõ rệt", loc="left",
             fontweight="bold")
ax.legend(frameon=False)
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT / "sua-index-100.png", dpi=150)
plt.close(fig)
print("sua-index-100.png")
