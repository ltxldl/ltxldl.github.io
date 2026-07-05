#!/usr/bin/env python3
"""Sinh hình cho Bài 5: split-apply-combine và các kiểu merge."""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OUT = Path(__file__).resolve().parent.parent
plt.rcParams.update({"font.size": 13, "figure.facecolor": "white", "savefig.facecolor": "white"})

BLUE, ORANGE, GREEN = "#1E93AB", "#E8890C", "#2E8B57"
COLS = {"A": "#dbeef3", "B": "#fdf0dd", "C": "#e3f2e9"}
EDGE = "#444"


def cell(ax, x, y, w, h, text, fc="#f5f5f5", fontsize=12, bold=False):
    ax.add_patch(plt.Rectangle((x, y), w, h, facecolor=fc, edgecolor=EDGE, linewidth=1.1))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize,
            fontweight="bold" if bold else "normal")


# ============================================================ split-apply-combine
fig, ax = plt.subplots(figsize=(10.2, 4.6))
ax.set_xlim(0, 20.4)
ax.set_ylim(-0.6, 9.2)
ax.axis("off")

rows = [("A", 10), ("B", 40), ("A", 20), ("C", 30), ("B", 50), ("A", 30)]
# bảng gốc
cell(ax, 0.2, 8.0, 1.6, 0.85, "khoá", "#e8e8e8", bold=True)
cell(ax, 1.8, 8.0, 1.6, 0.85, "giá", "#e8e8e8", bold=True)
for i, (k, v) in enumerate(rows):
    y = 7.15 - i * 0.85
    cell(ax, 0.2, y, 1.6, 0.85, k, COLS[k])
    cell(ax, 1.8, y, 1.6, 0.85, v, COLS[k])
ax.text(1.7, 8.15 + 0.95, "bảng gốc", ha="center", fontsize=13, fontweight="bold")

ax.annotate("", xy=(5.1, 4.6), xytext=(3.7, 4.6), arrowprops=dict(arrowstyle="->", lw=2.2, color=BLUE))
ax.text(4.4, 5.45, "SPLIT", ha="center", color=BLUE, fontweight="bold")
ax.text(4.4, 4.95, "chia theo khoá", ha="center", fontsize=11, color=BLUE)

# các nhóm
groups = {"A": [10, 20, 30], "B": [40, 50], "C": [30]}
ys = {"A": 7.6, "B": 4.7, "C": 2.4}
for k, vals in groups.items():
    y0 = ys[k]
    for j, v in enumerate(vals):
        cell(ax, 5.4 + j * 1.5, y0 - 0.85, 1.5, 0.85, v, COLS[k])
    ax.text(5.4 - 0.25, y0 - 0.43, k, ha="right", va="center", fontweight="bold")

ax.annotate("", xy=(11.6, 4.6), xytext=(10.3, 4.6), arrowprops=dict(arrowstyle="->", lw=2.2, color=ORANGE))
ax.text(10.95, 5.45, "APPLY", ha="center", color=ORANGE, fontweight="bold")
ax.text(10.95, 4.95, "mean từng nhóm", ha="center", fontsize=11, color=ORANGE)

# kết quả từng nhóm
means = {"A": 20, "B": 45, "C": 30}
for k in groups:
    cell(ax, 11.9, ys[k] - 0.85, 1.7, 0.85, means[k], COLS[k], bold=True)

ax.annotate("", xy=(15.4, 4.6), xytext=(14.1, 4.6), arrowprops=dict(arrowstyle="->", lw=2.2, color=GREEN))
ax.text(14.75, 5.45, "COMBINE", ha="center", color=GREEN, fontweight="bold")
ax.text(14.75, 4.95, "ghép lại", ha="center", fontsize=11, color=GREEN)

# bảng kết quả
cell(ax, 15.7, 5.5, 1.5, 0.85, "khoá", "#e8e8e8", bold=True)
cell(ax, 17.2, 5.5, 1.7, 0.85, "mean", "#e8e8e8", bold=True)
for i, k in enumerate(["A", "B", "C"]):
    y = 4.65 - i * 0.85
    cell(ax, 15.7, y, 1.5, 0.85, k, COLS[k])
    cell(ax, 17.2, y, 1.7, 0.85, means[k], COLS[k], bold=True)
ax.text(17.3, 6.6, 'df.groupby("khoá")["giá"].mean()', ha="center", fontsize=12,
        family="monospace", fontweight="bold")

fig.tight_layout()
fig.savefig(OUT / "split-apply-combine.png", dpi=150)
plt.close(fig)
print("split-apply-combine.png done")

# ============================================================ merge how
fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.4))

left_rows = [("P01", "Santiago"), ("P02", "Ñuñoa"), ("P03", "Vitacura")]
right_rows = [("Santiago", "Trung tâm"), ("Ñuñoa", "Đông"), ("Providencia", "Đông")]

for ax, how in zip(axes, ["inner", "left"]):
    ax.set_xlim(0, 10.2)
    ax.set_ylim(-0.4, 8.6)
    ax.axis("off")
    ax.text(1.9, 8.15, "listings", fontweight="bold", ha="center")
    cell(ax, 0.3, 6.6, 1.6, 0.8, "id", "#e8e8e8", 11, True)
    cell(ax, 1.9, 6.6, 2.2, 0.8, "quận", "#e8e8e8", 11, True)
    for i, (a, b) in enumerate(left_rows):
        cell(ax, 0.3, 5.8 - i * 0.8, 1.6, 0.8, a, "#dbeef3", 11)
        cell(ax, 1.9, 5.8 - i * 0.8, 2.2, 0.8, b, "#dbeef3", 11)
    ax.text(7.3, 8.15, "vùng", fontweight="bold", ha="center")
    cell(ax, 5.6, 6.6, 2.2, 0.8, "quận", "#e8e8e8", 11, True)
    cell(ax, 7.8, 6.6, 2.1, 0.8, "vùng", "#e8e8e8", 11, True)
    for i, (a, b) in enumerate(right_rows):
        cell(ax, 5.6, 5.8 - i * 0.8, 2.2, 0.8, a, "#fdf0dd", 11)
        cell(ax, 7.8, 5.8 - i * 0.8, 2.1, 0.8, b, "#fdf0dd", 11)

    y0 = 2.6
    ax.text(5.1, y0 + 0.5, f'merge(..., how="{how}", on="quận")', ha="center",
            fontsize=12, family="monospace", fontweight="bold")
    out_rows = [("P01", "Santiago", "Trung tâm"), ("P02", "Ñuñoa", "Đông")]
    if how == "left":
        out_rows.append(("P03", "Vitacura", "NaN"))
    for i, (a, b, c) in enumerate(out_rows):
        y = y0 - 0.8 - i * 0.8
        missing = c == "NaN"
        cell(ax, 1.6, y, 1.6, 0.8, a, "#eee" if missing else "#e3f2e9", 11)
        cell(ax, 3.2, y, 2.2, 0.8, b, "#eee" if missing else "#e3f2e9", 11)
        cell(ax, 5.4, y, 2.1, 0.8, c, "#fbeaea" if missing else "#e3f2e9", 11, missing)
    title = ("inner: chỉ giữ khoá có ở CẢ HAI bảng\n(P03 Vitacura bị rơi)"
             if how == "inner" else
             "left: giữ đủ bảng trái\n(Vitacura không khớp → vùng = NaN)")
    ax.set_title(title, fontsize=12.5)

fig.tight_layout()
fig.savefig(OUT / "merge-how.png", dpi=150)
plt.close(fig)
print("merge-how.png done")
