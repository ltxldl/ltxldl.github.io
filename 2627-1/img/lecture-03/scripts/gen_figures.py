#!/usr/bin/env python3
"""Sinh hình minh hoạ cho Bài 3 (NumPy). Chạy: python gen_figures.py (từ thư mục scripts/).

Xuất SVG, chữ vẽ bằng outline của Source Sans Pro (bản vendored trong revealjs/) —
trùng font slide, nét ở mọi độ phóng. Không dùng svg.fonttype=none vì SVG nhúng qua
<img> là tài liệu cô lập, không thấy font của trang.
"""
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
from matplotlib import font_manager
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent.parent
FONT_DIR = OUT.parent.parent / "revealjs" / "dist" / "theme" / "fonts" / "source-sans-pro"
for f in FONT_DIR.glob("*.ttf"):
    font_manager.fontManager.addfont(str(f))

INK, MUTED = "#333333", "#666666"
plt.rcParams.update({
    "font.family": "Source Sans Pro",
    "font.size": 14,
    "svg.fonttype": "path",            # chữ → outline: <img> không load được font ngoài
    "figure.facecolor": "none",
    "savefig.facecolor": "none",
    "text.color": INK,
    "axes.edgecolor": MUTED,
    "axes.labelcolor": MUTED,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
})

BLUE, ORANGE, GREEN, GRAY = "#1E93AB", "#E8890C", "#2E8B57", "#9aa3a8"

# ---------------------------------------------------------- speed comparison
n = 5_000_000
xs_list = list(range(n))
xs_np = np.arange(n, dtype=np.int64)

t0 = time.perf_counter()
s1 = sum(x * 1.1 for x in xs_list)
t_list = time.perf_counter() - t0

t0 = time.perf_counter()
s2 = (xs_np * 1.1).sum()
t_np = time.perf_counter() - t0

fig, ax = plt.subplots(figsize=(7.6, 3.6))
bars = ax.barh(["NumPy\n(vector hoá)", "Python thuần\n(vòng for)"], [t_np, t_list],
               color=[BLUE, GRAY], height=0.55)
ax.bar_label(bars, [f" {t_np*1000:.0f} ms", f" {t_list*1000:.0f} ms"],
             fontsize=14, fontweight="bold", color=INK)
ax.set_xlabel("thời gian nhân 5 triệu số với 1.1 rồi cộng tổng (giây)")
ax.set_xlim(0, t_list * 1.28)
ax.spines[["top", "right"]].set_visible(False)
ax.set_title(f"Cùng một việc — NumPy nhanh hơn ~{t_list / t_np:.0f} lần",
             fontweight="bold", color=INK)
fig.tight_layout()
fig.savefig(OUT / "speed-comparison.svg")
plt.close(fig)
print(f"speed: list={t_list:.3f}s numpy={t_np:.4f}s ratio={t_list/t_np:.0f}x")

# ---------------------------------------------------------- broadcasting diagram
fig, ax = plt.subplots(figsize=(9.2, 4.2))
ax.set_xlim(0, 13.6)
ax.set_ylim(-0.4, 4.6)
ax.axis("off")

CELL = 0.92

def draw_grid(x0, y0, rows, cols, vals, color, edge, alpha=1.0, dashed=False):
    for r in range(rows):
        for c in range(cols):
            rect = plt.Rectangle((x0 + c * CELL, y0 + (rows - 1 - r) * CELL), CELL, CELL,
                                 facecolor=color, edgecolor=edge, alpha=alpha,
                                 linestyle="--" if dashed else "-", linewidth=1.2)
            ax.add_patch(rect)
            v = vals[r][c] if vals else ""
            ax.text(x0 + c * CELL + CELL / 2, y0 + (rows - 1 - r) * CELL + CELL / 2, str(v),
                    ha="center", va="center", fontsize=13, color=INK)

# (4,3) matrix
A = [[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]]
draw_grid(0.3, 0.5, 4, 3, A, "#dbeef3", "#0f6478")
ax.text(0.3 + 1.5 * CELL, 4.35, "giá (4 thành phố × 3 tháng)", ha="center", fontsize=13, color="#0f6478")

ax.text(3.75, 2.3, "+", ha="center", va="center", fontsize=26, fontweight="bold")

# (3,) row vector + ghosted copies
B = [[1, 2, 3]]
draw_grid(4.5, 0.5 + 3 * CELL, 1, 3, B, "#fdf0dd", "#b06f08")
for k in range(3):
    draw_grid(4.5, 0.5 + k * CELL, 1, 3, B, "#fdf0dd", "#b06f08", alpha=0.35, dashed=True)
ax.text(4.5 + 1.5 * CELL, 4.35, "phụ phí theo tháng (3,)", ha="center", fontsize=13, color="#b06f08")
ax.text(4.5 + 1.5 * CELL, 0.06, "tự “nhân bản” xuống 4 hàng", ha="center", va="top",
        fontsize=12, color="#b06f08", style="italic")

ax.text(8.9, 2.3, "=", ha="center", va="center", fontsize=26, fontweight="bold")

Cm = [[11, 14, 14], [21, 23, 27], [31, 35, 34], [41, 46, 45]]
draw_grid(9.8, 0.5, 4, 3, Cm, "#e3f2e9", "#20623f")
ax.text(9.8 + 1.5 * CELL, 4.35, "kết quả (4, 3)", ha="center", fontsize=13, color="#20623f")

fig.tight_layout()
fig.savefig(OUT / "broadcasting.svg")
plt.close(fig)
print("broadcasting.svg done")

# ---------------------------------------------------------- axis diagram
fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.4))
M = [[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]]
for ax, (title, color) in zip(axes, [("axis=0 — dọc theo hàng\n→ ra 1 số MỖI CỘT", BLUE),
                                     ("axis=1 — ngang theo cột\n→ ra 1 số MỖI HÀNG", ORANGE)]):
    ax.set_xlim(-0.7, 4.4)
    ax.set_ylim(-1.6, 4.4)
    ax.axis("off")
    for r in range(4):
        for c in range(3):
            ax.add_patch(plt.Rectangle((c, 3 - r), 0.92, 0.92, facecolor="#f2f2f2", edgecolor="#888"))
            ax.text(c + 0.46, 3 - r + 0.46, M[r][c], ha="center", va="center", fontsize=12, color=INK)
    if "axis=0" in title:
        for c in range(3):
            ax.annotate("", xy=(c + 0.46, -0.75), xytext=(c + 0.46, -0.12),
                        arrowprops=dict(arrowstyle="->", color=color, lw=2.6))
        for c, v in enumerate([25, 27.5, 27]):
            ax.text(c + 0.46, -1.25, f"{v:g}", ha="center", fontsize=12, color=color, fontweight="bold")
    else:
        for r in range(4):
            ax.annotate("", xy=(3.62, 3 - r + 0.46), xytext=(3.02, 3 - r + 0.46),
                        arrowprops=dict(arrowstyle="->", color=color, lw=2.6))
        for r, v in enumerate([11, 21.7, 31.3, 42]):
            ax.text(3.78, 3 - r + 0.34, f"{v:g}", fontsize=12, color=color, fontweight="bold")
    ax.set_title(title, fontsize=13, color=color)
fig.suptitle("mean(axis=?) trên ma trận (4 thành phố × 3 tháng)", fontsize=14,
             fontweight="bold", color=INK)
fig.tight_layout()
fig.savefig(OUT / "axis.svg")
plt.close(fig)
print("axis.svg done")
