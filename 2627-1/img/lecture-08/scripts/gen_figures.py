#!/usr/bin/env python3
"""Sinh hình cho Bài 8 từ dữ liệu reviews Santiago thật.
Cần file visualisations/reviews.csv của snapshot 2026-06-29 (tải về cùng thư mục hoặc chỉnh PATH).
"""
from pathlib import Path
import sys

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

OUT = Path(__file__).resolve().parent.parent
plt.rcParams.update({"font.size": 13, "figure.facecolor": "white", "savefig.facecolor": "white"})
BLUE, ORANGE, GRAY = "#1E93AB", "#E8890C", "#999999"

PATH = sys.argv[1] if len(sys.argv) > 1 else "reviews.csv"
rv = pd.read_csv(PATH, parse_dates=["date"])
rv = rv[rv["date"] < "2026-07-01"]          # bỏ "tháng cụt" cuối cùng (snapshot giữa tháng)
theo_thang = rv.set_index("date").resample("ME").size()
theo_thang = theo_thang.loc["2016":]

# ------------------------------------------------ monthly + rolling
fig, ax = plt.subplots(figsize=(9.6, 4.2))
ax.plot(theo_thang.index, theo_thang.values, color=GRAY, lw=1.1, label="Số review mỗi tháng")
ax.plot(theo_thang.index, theo_thang.rolling(6, center=True).mean(),
        color=BLUE, lw=2.6, label="Trung bình trượt 6 tháng")
ax.axvspan(pd.Timestamp("2020-03-01"), pd.Timestamp("2021-10-31"), color="#fbeaea", zorder=0)
ax.text(pd.Timestamp("2020-12-01"), theo_thang.max() * 0.92, "COVID-19", color="#c0392b",
        ha="center", fontweight="bold")
ax.set_title("Review Santiago theo tháng: mùa vụ + vết sẹo COVID", fontweight="bold")
ax.set_ylabel("số review")
ax.legend(frameon=False, loc="upper left")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT / "reviews-theo-thang.png", dpi=150)
plt.close(fig)
print("reviews-theo-thang.png done")

# ------------------------------------------------ seasonality profile
# CHỈ dùng các năm trọn vẹn (2022–2025): nếu gộp cả nửa đầu 2026 — nửa năm lớn nhất,
# chỉ góp mặt cho T1–T6 — các tháng đầu năm bị thổi phồng thành "đỉnh T1–T4" ảo
# (lỗi của bản nháp đầu, đính chính 06/07/2026 — xem DECISIONS.md).
tron_nam = rv.loc[(rv["date"] >= "2022-01-01") & (rv["date"] <= "2025-12-31")]
thang_tb = tron_nam.groupby(tron_nam["date"].dt.month).size()
thang_tb = thang_tb / thang_tb.mean() * 100

fig, ax = plt.subplots(figsize=(8.6, 3.8))
colors = [ORANGE if m in (7, 8, 10, 11) else BLUE for m in thang_tb.index]
ax.bar(thang_tb.index, thang_tb.values, color=colors)
ax.axhline(100, color="#555", lw=1, ls="--")
ax.set_xticks(range(1, 13), [f"T{m}" for m in range(1, 13)])
ax.set_ylabel("chỉ số mùa vụ (100 = TB năm)")
ax.set_ylim(0, 140)
ax.set_title("Đỉnh review rơi vào T7–T8 và T10–T11, đáy vào T2", fontweight="bold")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(OUT / "mua-vu.png", dpi=150)
plt.close(fig)
print("mua-vu.png done")
