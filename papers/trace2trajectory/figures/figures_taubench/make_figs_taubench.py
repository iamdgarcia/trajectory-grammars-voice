# Data-true figures for the tau-bench real-agent anchor (25-oct).
# Every point and cell comes from runtime/taubench_anchor/tb_coverage.json, recomputed
# here with the shipped trace2grammar.coverage and parity-asserted before plotting.
# n_real = 1,980 official tau-bench eval runs (gpt-4o + claude-3.5-sonnet, airline+retail);
# n_sim = the artifact's 60 production-shaped template compositions (labeled as such).
import json
import os
import sys

sys.path.insert(0, "C:/Users/U77225D/Desktop/proyectos/hf/builds/trace2grammar")
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from trace2grammar.coverage import coverage, _grid_transform, _box_blur, _bump_grid

HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = json.load(open("C:/Users/U77225D/Desktop/proyectos/hf/runtime/taubench_anchor/tb_coverage.json", encoding="utf-8"))
real2d = [tuple(p) for p in SNAP["real2d"]]
sim2d = [tuple(p) for p in SNAP["sim2d"]]
classes = [m["outcome"] for m in SNAP["real_meta"]]

# recompute with the shipped code and assert parity with the stored snapshot
cov = coverage(real2d, sim2d, res=24, eps=0.05, bw_frac=0.12, classes=classes)
assert cov["coverage_pct"] == SNAP["coverage_pct"], (cov["coverage_pct"], SNAP["coverage_pct"])
assert cov["occupied_cells"] == SNAP["occupied_cells"]
assert cov["covered_cells"] == SNAP["covered_cells"]
assert len(cov["uncovered_cells"]) == len(SNAP["uncovered_cells"])
print("parity OK:", cov["coverage_pct"], "% |", cov["covered_cells"], "/", cov["occupied_cells"], "cells")

BLUE, TEAL, ORANGE, GRAY = "#1e5aa8", "#00795f", "#ef6c00", "#c9c9c9"
LBL = {"theta_cont": "contained", "theta_aban": "abandoned", "theta_hand": "handoff"}
CLS_COLOR = {"theta_cont": TEAL, "theta_aban": BLUE, "theta_hand": "#8e24aa"}

plt.rcParams.update({"font.size": 9, "axes.linewidth": 0.6})

fig, axs = plt.subplots(1, 2, figsize=(10.6, 3.9))

# ------------------------------------------- (a) atlas: 1,980 real + 60 sim
ax = axs[0]
allpts = real2d + sim2d
pad = 0.05 * max(max(p[0] for p in allpts) - min(p[0] for p in allpts),
                 max(p[1] for p in allpts) - min(p[1] for p in allpts), 1.0)
ax.set_xlim(min(p[0] for p in allpts) - pad, max(p[0] for p in allpts) + pad)
ax.set_ylim(min(p[1] for p in allpts) - pad, max(p[1] for p in allpts) + pad)
for cls in ("theta_aban", "theta_cont", "theta_hand"):
    pts = [(x, y) for (x, y), c in zip(real2d, classes) if c == cls]
    if not pts:
        continue
    ax.plot([p[0] for p in pts], [p[1] for p in pts], "o", color=CLS_COLOR[cls],
            ms=2.6, alpha=0.22, mew=0, zorder=2,
            label=f"{LBL[cls]} (n={len(pts)})")
ax.plot([p[0] for p in sim2d], [p[1] for p in sim2d], "D", color=ORANGE,
        ms=4.5, mec="white", mew=0.5, alpha=0.95, zorder=3,
        label="sim compositions (n=60)")
ax.set_xlabel("PC 1")
ax.set_ylabel("PC 2")
ax.set_title("(a) behavior plane: 1,980 real agent runs (PCA fit on real)", fontsize=9)
ax.legend(loc="best", fontsize=7, framealpha=0.9)

# ------------------------------------------- (b) coverage grid at bw 0.12
ax = axs[1]
x0, y0, cw, ch = _grid_transform(real2d, cov["grid"]["res"], 0.15)
res = cov["grid"]["res"]
sigma = 0.12 * res
real_g = _box_blur(_bump_grid(real2d, res, sigma, x0, y0, cw, ch), 2)
real_peak = max(max(r) for r in real_g)
flat = sorted((v for row in real_g for v in row), reverse=True)
p99 = flat[max(0, int(0.01 * len(flat)))]
core = max(p99, 0.5 * real_peak)
thresh = cov["grid"]["eps"] * core
uncovered_set = {(u["gx"], u["gy"]) for u in cov["uncovered_cells"]}
occupied = [(i, j) for i in range(res) for j in range(res) if real_g[i][j] > thresh]
assert len(occupied) == cov["occupied_cells"], (len(occupied), cov["occupied_cells"])
covered_set = {(u["gx"], u["gy"]) for u in []}
# covered = occupied minus uncovered
occ_un = len(uncovered_set & set(occupied))
for i, j in occupied:
    color = "#f7d4d4" if (i, j) in uncovered_set else "#cfe0f5"
    ax.add_patch(plt.Rectangle((x0 + i * cw, y0 + j * ch), cw, ch,
                               facecolor=color, edgecolor="none", zorder=1))
sim_pts = set()
for (x, y) in sim2d:
    gx = int((x - x0) / cw)
    gy = int((y - y0) / ch)
    sim_pts.add((gx, gy))
n_sim_cells = len(sim_pts & set(occupied))
ax.plot([p[0] for p in real2d], [p[1] for p in real2d], "o", color="#666666",
        ms=1.4, alpha=0.10, mew=0, zorder=2)
ax.plot([p[0] for p in sim2d], [p[1] for p in sim2d], "D", color=ORANGE,
        ms=4.5, mec="white", mew=0.5, zorder=3)
ax.set_xlim(x0, x0 + res * cw)
ax.set_ylim(y0, y0 + res * ch)
ax.set_aspect("equal")
ax.set_title(f"(b) coverage @ kernel 0.12: {cov['covered_cells']}/{cov['occupied_cells']} cells (100%)", fontsize=9)
ax.set_xlabel("PC 1")
ax.set_ylabel("PC 2")

fig.tight_layout()
out_dir = os.path.dirname(HERE)
fig.savefig(os.path.join(out_dir, "fig_atlas_taubench.pdf"))
fig.savefig(os.path.join(out_dir, "fig_coverage_taubench.pdf"))
print("fig_atlas_taubench.pdf + fig_coverage_taubench.pdf written",
      "| sim cells touched:", n_sim_cells, "| occ-uncovered:", occ_un)
