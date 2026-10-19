## Review — Reviewer 3 (writing & presentation)

**SCORE: 7.5/10.** Structure, claim-delivery, and number consistency are strong; two must-fix defects (a verbatim duplicated paragraph, a caption that misdefines the paper's central quantity), plus a cluster of notation collisions.

### Correct (verified)
- **Title question explicitly answered.** §9 (`09_conclusion.tex`, para 3): "turns the question in the title from a worry into a report: *what are we not testing* becomes a ranked list of regions" — and concretely delivered in §5.2 + Table `tab:topk` (named exemplars, outcome classes).
- **Worked-example numbers consistent everywhere** and arithmetically sound: abstract (40.2 / 45.3 / 35.2), §5.2 (256 occupied, 103 covered → 103/256 = 40.2%), §8 limitations ("3 conversations across 3 dialects"). Abstract's "3 conversations, 3 dialects" matches §5.2's 2 real + 1 sim.
- **`06_evaluation.tex` is protocol-only as declared** (opening line says so; no fabricated results present). ✓
- **Figure color coding consistent** (real=blue, sim=orange diamonds, uncovered=red) across `fig_coverage.tex`, `fig_atlas.tex`, and both captions/§5 text.
- **One-sentence-per-line**: eyeball check across 01–09 shows each sentence starting a fresh line; no violations spotted in full reads of 01, 02, 03, 04, 05, 06, 07, 08, 09.

### MANDATORY (fix before upload)
1. **P1 — Verbatim duplicated paragraph.** `sections/02_background.tex`, subsection "Trace mining and observability formats": the sentence block "Trace mining recovers structure from execution logs: automata for failure and next-step prediction \citep{automataTraces2026}, behavior benchmarks … \citep{wildvis2024}." appears **twice, back-to-back**. Smallest fix: delete one copy (keep the second, which flows into the "Early outcome prediction" sentence).
2. **P1 — Caption contradicts the central equation.** `sections/04_coverage.tex`, `fig:coverage` caption, panel (b): "core is the field's 99th-percentile-to-peak ratio." Eq. `\eqref{eq:threshold}` defines `core = max(p99, 0.5·peak)` — a density value, not a ratio. Fix: "where core = max(p99, 0.5·peak)" (mirror Eq. 2 verbatim).

### OPTIONAL
3. **P2 — Symbol collisions in §6.1.** Kendall **τ** collides with the extraction mapping τ (the paper's headline operator, §3); Spearman **ρ** collides with grid resolution ρ (§4.3, §6.2 sweep) **and** with the density field ρ in `fig_coverage.tex` panel (b) label "occupancy ρ > ε·core". Fix: `τ_K`/`ρ_S` subscripts, and relabel panel (b)'s density as e.g. `d`.
4. **P2 — ε vs ϵ.** §4/§5 use `\varepsilon`; §6 uses `\epsilon` throughout ("threshold $\epsilon$", sweep list, worked-example config). Pick one (`\varepsilon`).
5. **P2 — `def:tau` (`03_extraction.tex`).** Domain symbol **D** collides with cycle depth D(σ) used in the same definition; codomain Σ* type-slips (walks are over states q∈Q, Σ is transition types). Suggest domain `\mathcal{D}` and "walk with typed transitions" phrasing.
6. **P2 — Axis naming inconsistent between figures.** `fig_coverage.tex` uses c₁/c₂; `fig_atlas.tex` uses PC 1/PC 2; body text names neither. Pick one (PC 1/PC 2 matches the PCA fit of §4.2).
7. **P2 — `fig_atlas.tex` caption garble.** "a scattered **real** cloud with uncovered lobes is the typical deficient configuration" — per §5.1, scatter is a *sim*-cloud pathology. Likely should read "scattered sim cloud"; as written it's ambiguous.
8. **P2 — Stale planning docs.** `NOTES.md` ("5 conversations, 40.2%", "40/40 checks") and `OUTLINE.md` §5.2 ("5 conversations across 3 dialects") contradict the shipped paper (3 conversations; 46 checks, stated consistently in §5.2 and §8). Update before the arXiv zip so packaged docs don't contradict the PDF.
9. **P2 — Author block (`main.tex`).** Missing `\\` after "AI Engineering, Unicaja Bank, Spain." → the email will typeset run-on with the affiliation. Also note "Unicaja Bank" is a corporate string: confirm affiliation convention matches sibling papers and the clean-room policy before pushing paper sources anywhere public.
10. **P2 — Dangling comma.** `03_extraction.tex`, sentence introducing Eq. `eq:kinds` ends at the equation with ",\end{aligned}" and is never completed ("…with event kinds [eq],"). Change the trailing comma inside the equation to a period.
11. **P2 — Natbib note reads oddly.** `01_introduction.tex`: `\citep[still marked Development as of October 2026]{otelgenai2026}` renders as "[still marked Development as of October 2026, N]" — move the status note into prose.
12. **P2 — Bigram k never specified.** §4.1 "first $k$ state-to-state transitions" — k has no value and isn't in the §6 sweep. One clause fixes it.

**Merge verdict: OK with notes** — no P0s; items 1–2 are mandatory pre-upload fixes, the rest polish.

### What I understood (summary)
The paper claims a first: a formal extraction τ turning OTel-GenAI/OpenInference/LangSmith exports into trajectory-grammar walks (G=(Q,Σ,δ), four terminal classes, cycle depth), a deterministic real-anchored 2-D projection with density-grid occupancy under a shared relative threshold ε·core, and a region-coverage metric (overall + per-class + top-K uncovered regions with nearest real exemplars) visualized as the trajectory atlas. §6 deliberately ships a protocol (sensitivity sweep, rank-correlation transfer headline, baseline ladder), not results; the only executed evidence is the 3-conversation fixture example (40.2%). The text is honest about the rule-based classifier, lossy 2-D projection, and fixture scale. Residual risks: the systematic duplicate/multi-sentence-per-line scan could not be run (ripgrep unavailable in this environment), compile output was not re-verified (out of scope), and main.bib's 26 entries were not individually cross-checked against citations.