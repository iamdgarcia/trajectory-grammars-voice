# Data-true figures for the trace2trajectory paper (22-oct).
# Every point and cell comes from the shipped artifact: coverage_report.json
# (recomputed deterministically with the shipped trace2grammar.coverage and
# parity-checked against the report). No hand-placed decorative points: that
# was the flaw of the old TikZ figures (atlas showed dozens of fake points).
import json, sys

sys.path.insert(0, "C:/Users/U77225D/Desktop/proyectos/hf/builds/trace2grammar")
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyArrowPatch
from trace2grammar.coverage import coverage, top_k_uncovered

REP = json.load(open("C:/Users/U77225D/Desktop/proyectos/hf/builds/trace2grammar/coverage_report.json", encoding="utf-8"))
real2d = [tuple(p) for p in REP["real2d"]]
sim2d = [tuple(p) for p in REP["sim2d"]]
classes = [m["outcome"] for m in REP["real_meta"]]

# Recompute with the shipped code and assert parity with the stored report.
cov = coverage(real2d, sim2d, res=REP["grid"]["res"], eps=REP["grid"]["eps"],
               bw_frac=REP["grid"]["bw_frac"], classes=classes)
assert cov["coverage_pct"] == REP["coverage_pct"], (cov["coverage_pct"], REP["coverage_pct"])
assert cov["occupied_cells"] == REP["occupied_cells"]
assert cov["covered_cells"] == REP["covered_cells"]
assert len(cov["uncovered_cells"]) == len(REP["uncovered_cells"])
print("parity OK:", cov["coverage_pct"], "% |", cov["covered_cells"], "/", cov["occupied_cells"], "cells")

BLUE, ORANGE, RED, GRAY = "#1e5aa8", "#ef6c00", "#c62828", "#8a8a8a"
LBL = {"theta_cont": "contained", "theta_aban": "abandoned", "theta_hand": "handoff"}

def exemplar_label(i):
    m = REP["real_meta"][i]
    return ('"%s…" [%s, D=%d, %.1fs]' % (m["first_user_text"][:34], LBL.get(m["outcome"], m["outcome"]),
                                          m["cycle_depth"], m["duration_ms"]/1000))

# grid geometry (same transform as the shipped code, for cell rectangles)
from trace2grammar.coverage import _grid_transform, _box_blur, _bump_grid
x0, y0, cw, ch = _grid_transform(real2d, cov["grid"]["res"], 0.15)
res = cov["grid"]["res"]
sigma = cov["grid"]["bw_frac"] * res
real_g = _box_blur(_bump_grid(real2d, res, sigma, x0, y0, cw, ch), 2)
real_peak = max(max(r) for r in real_g)
flat = sorted((v for row in real_g for v in row), reverse=True)
p99 = flat[max(0, int(0.01 * len(flat)))]
core = max(p99, 0.5 * real_peak)
thresh = cov["grid"]["eps"] * core
uncovered_set = {(u["gx"], u["gy"]) for u in cov["uncovered_cells"]}
occupied = [(i, j) for i in range(res) for j in range(res) if real_g[i][j] > thresh]
assert len(occupied) == cov["occupied_cells"]

plt.rcParams.update({"font.size": 9, "axes.linewidth": 0.6})

# ---------------------------------------------------------------- fig_coverage
fig, axs = plt.subplots(1, 3, figsize=(11.4, 3.1))
# (a) behavior plane: the actual 3 walks
ax = axs[0]
allpts = real2d + sim2d
pad = 0.6
ax.set_xlim(min(p[0] for p in allpts)-pad, max(p[0] for p in allpts)+pad)
ax.set_ylim(min(p[1] for p in allpts)-pad, max(p[1] for p in allpts)+pad)
for (x, y), m in zip(real2d, REP["real_meta"]):
    ax.plot([x], [y], "o", color=BLUE, ms=7, mec="white", mew=0.8, zorder=3)
    ax.annotate(LBL[m["outcome"]], (x, y), textcoords="offset points", xytext=(8, 5),
                fontsize=8, color=BLUE)
(x, y), = sim2d
ax.plot([x], [y], "D", color=ORANGE, ms=7, mec="white", mew=0.8, zorder=3)
ax.annotate("sim", (x, y), textcoords="offset points", xytext=(8, -11), fontsize=8, color=ORANGE)
ax.set_xlabel("PC 1"); ax.set_ylabel("PC 2")
ax.set_title("(a) behavior plane (3 fixture walks)", fontsize=9)
# (b) density grid, occupancy threshold
ax = axs[1]
for i, j in occupied:
    ax.add_patch(Rectangle((x0+i*cw, y0+j*ch), cw, ch, fc=BLUE, alpha=0.22, ec="none"))
ax.plot([p[0] for p in real2d], [p[1] for p in real2d], "o", color=BLUE, ms=6, mec="white", mew=0.7, zorder=3)
ax.set_xlim(x0, x0+res*cw); ax.set_ylim(y0, y0+res*ch)
ax.set_xlabel("PC 1"); ax.set_ylabel("PC 2")
ax.set_title("(b) occupied: $d > \\varepsilon\\cdot$core\n(core $=\\max($p99$,\\ 0.5\\cdot$peak$)$, $\\rho{=}24$)", fontsize=9)
# (c) covered vs uncovered
ax = axs[2]
for i, j in occupied:
    unc = (i, j) in uncovered_set
    ax.add_patch(Rectangle((x0+i*cw, y0+j*ch), cw, ch,
                           fc=RED if unc else BLUE, alpha=0.30 if unc else 0.22, ec="none"))
ax.plot([p[0] for p in real2d], [p[1] for p in real2d], "o", color=BLUE, ms=6, mec="white", mew=0.7, zorder=3)
ax.plot(sim2d[0][0], sim2d[0][1], "D", color=ORANGE, ms=6, mec="white", mew=0.7, zorder=3)
ax.set_xlim(x0, x0+res*cw); ax.set_ylim(y0, y0+res*ch)
ax.set_xlabel("PC 1"); ax.set_ylabel("PC 2")
ax.set_title("(c) %s%% covered (%d/%d cells)" % (cov["coverage_pct"], cov["covered_cells"], cov["occupied_cells"]), fontsize=9)
for ax in axs:
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_color("#cccccc")
fig.tight_layout()
fig.savefig("fig_coverage.pdf", bbox_inches="tight", dpi=300)
print("fig_coverage.pdf written")

# ---------------------------------------------------------------- fig_atlas
fig, ax = plt.subplots(figsize=(7.0, 4.4))
top = top_k_uncovered(cov, 3)
# uncovered cells (all 153, data-true) + top-3 highlighted
for u in cov["uncovered_cells"]:
    ax.add_patch(Rectangle((x0+u["gx"]*cw, y0+u["gy"]*ch), cw, ch, fc=RED, alpha=0.18, ec="none"))
for u in top:
    ax.add_patch(Rectangle((x0+u["gx"]*cw, y0+u["gy"]*ch), cw, ch, fc=RED, alpha=0.45, ec=RED, lw=0.8))
for (x, y), m in zip(real2d, REP["real_meta"]):
    ax.plot([x], [y], "o", color=BLUE, ms=8, mec="white", mew=1.0, zorder=4)
    ax.annotate('real: %s' % exemplar_label(REP["real_meta"].index(m)), (x, y),
                textcoords="offset points", xytext=(10, 8), fontsize=8, color="#1a3f7a",
                bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#cccccc", lw=0.5, alpha=0.9))
(x, y), = sim2d
ax.plot([x], [y], "D", color=ORANGE, ms=8, mec="white", mew=1.0, zorder=4)
ax.annotate("sim: %s" % exemplar_label(-1).replace(REP["real_meta"][0]["first_user_text"][:34], "sim walk"), (x, y),
            textcoords="offset points", xytext=(10, -16), fontsize=8, color=ORANGE,
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec="#e0b080", lw=0.5, alpha=0.9))
# callouts from the top-1 uncovered cell to its nearest real exemplar label
u = top[0]
ax.annotate("top uncovered region\nnearest real: %s" % exemplar_label(u["exemplar_idx"]),
            (x0+(u["gx"]+0.5)*cw, y0+(u["gy"]+0.5)*ch), (x0+(u["gx"]+0.5)*cw+1.2, y0+(u["gy"]+0.5)*ch-1.6),
            fontsize=8, color=RED, ha="left",
            arrowprops=dict(arrowstyle="->", color=RED, lw=0.8),
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=RED, lw=0.5, alpha=0.9))
ax.set_xlim(x0, x0+res*cw); ax.set_ylim(y0, y0+res*ch)
ax.set_xlabel("PC 1"); ax.set_ylabel("PC 2")
ax.set_xticks([]); ax.set_yticks([])
for s in ax.spines.values(): s.set_color("#cccccc")
ax.set_title("trajectory atlas — fixture scale: %d real / %d simulated walks (rank-deficient basis at n=2;\nsmoke test of runnability, see §6.2)" % (len(real2d), len(sim2d)), fontsize=9)
from matplotlib.lines import Line2D
leg = [Line2D([],[], marker="o", ls="none", color=BLUE, label="real (production)"),
       Line2D([],[], marker="D", ls="none", color=ORANGE, label="simulated"),
       Rectangle((0,0),1,1, fc=RED, alpha=0.30, label="occupied, uncovered (%d cells)" % len(cov["uncovered_cells"]))]
ax.legend(handles=leg, loc="upper left", fontsize=8, frameon=True, framealpha=0.9)
fig.tight_layout()
fig.savefig("fig_atlas.pdf", bbox_inches="tight", dpi=300)
print("fig_atlas.pdf written")
