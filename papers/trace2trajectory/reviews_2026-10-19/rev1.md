## Review — Reviewer 1 (methodology)

**SCORE: 7.5/10.** The coverage method is cleanly defined, genuinely deterministic, and mostly honest about its fixture-scale status. Two P1 gaps: the worked example's real-anchored basis is degenerate at n=2, and the paper's own sensitivity protocol never tests the anchoring commitment it declares central.

### MANDATORY

1. **P1 — Degenerate basis at fixture scale.** §5.2 (`sections/05_atlas.tex`, "Worked example" paragraph) states the real set is **two** conversations (OTel + OpenInference), the simulated set is one. §4.2 fits the PCA basis "on the real set only." With 2 real samples, the centered feature matrix has rank 1: the second principal component has zero variance and its direction is implementation-defined — deterministic, yes, but geometrically arbitrary. The 256 occupied cells and the 40.2% therefore depend on an arbitrary axis. §6.2's determinism argument ("no seed variance") does not rescue this: determinism ≠ validity. Fix: one sentence in §5.2 acknowledging that at real-set sizes comparable to the fixture the 2-D basis is degenerate and the number is a smoke test of runnability only (the paper already half-says this; the degeneracy mechanism is the missing part).

2. **P1 — Protocol never tests the anchoring commitment.** §6.2 sweeps ρ, β, ε (36 configs) — all downstream of the projection, which is held fixed. The paper's central design commitment ("production defines the behavior space," §4.2) is exactly the thing the sweep cannot detect: if the basis is unstable, every one of the 36 configurations inherits the same arbitrary plane and the "stability envelope" reports false stability. Fix: add a real-set resampling rung to the protocol (subsample the real collection, refit the basis, report coverage spread). It is cheap, deterministic-friendly, and it is the only sweep that tests the anchoring claim.

3. **P2 — Abstract and conclusion quote 40.2% without the illustrative qualifier.** `main.tex` abstract: "a 1-conversation simulated set covers 40.2% of the occupied real regions" with class breakdowns; §9 repeats it. §5.2 and §8 carry the honest framing ("fixture-scale by design," "not field evidence"), but the abstract hides the 2-real/1-sim split behind "(3 conversations, 3 dialects)". Fix: one parenthetical in the abstract — "(2 real / 1 simulated fixture conversations)" — so the number cannot be read as a population statistic.

4. **P2 — Silent dropping of out-of-grid sim points.** §4.4: "dropped, not clamped." Correct choice, but §5.1 sells "Scatter" as a diagnostic configuration the atlas reveals, while the metric never quantifies it: a sim set that is 90% off-plane and one that is 0% off-plane can post identical coverage. Fix: report the out-of-grid fraction alongside coverage (one number, already computed).

5. **P2 — Z-normalization provenance unstated.** §4.1 says features are "z-normalized per column" but never says whether column mean/std come from the real set or are fit jointly. The real-anchoring argument of §4.2 depends on this. Fix: one clause — "normalization statistics computed on the real set."

6. **P2 — Envelope-center claim is half-true, and core construction escapes the sweep.** §6.2: the worked config "sits at the envelope's center." β=0.12 and ε=0.05 are the centers of 3-element sets; ρ=24 is second-lowest of {16,24,32,48}. Also, `core = max(p99, 0.5·peak)` (Eq. 5, §4.3) embeds two constants (99th percentile, the 0.5 factor) that the sweep never varies. Fix: soften to "within the envelope" and note the core constants as fixed-by-construction.

7. **P2 — Symbol collision.** §6.1 uses "Kendall $\tau$" while $\tau$ is the extraction mapping (Def. 3.1, §3) used throughout. Fix: τ_K/ρ_S or spell out "Kendall rank correlation."

### OPTIONAL

- `main.bib`: several entries carry `author list [verify]` notes and `garcia2026grammar` is a placeholder ("companion paper"). Resolve before upload — a reviewer reading the .bbl will see the scaffolding.
- §5.2 Table 2: ranks 1 and 3 share the same exemplar utterance after Chebyshev-2 dedup — fine as shown, but one clause noting dedup is distance-local would preempt a "why is this duplicated?" question.

### What I understood (summary)

The paper defines a two-stage pipeline: τ-normalization converts observability exports (OTel GenAI, OpenInference, LangSmith, plus τ-bench) into deterministic grammar walks over Q with four terminal outcome classes and a cycle-depth statistic; region coverage then encodes walks as shallow structural features, projects real and simulated collections into a 2-D plane fit on the real set only, estimates real density on a grid with a shared relative occupancy threshold (ε·core), and reports overall + per-class coverage plus top-K uncovered regions with nearest real exemplars. The single executed evidence is a fixture-scale worked example (40.2%); §6 is explicitly protocol-only, specifying a rank-correlation transfer headline, a 36-config hyperparameter sweep, class-conditional coverage, and a three-rung simulator baseline ladder. The protocol-only discipline is real and well-executed; the residual risk is that both the worked example and the sweep stop one layer short of testing the paper's own anchoring premise.

## Review
- Correct: determinism argument (§4.2), shared-threshold commensurability (§4.3), per-class design (§4.4), protocol-only framing (§6, first paragraph), honest limitations (§8).
- Finding: P1 items 1–2, P2 items 3–7 above; no P0 — nothing blocks merge; the P1s are one-paragraph fixes.
- Merge verdict: **OK with notes** — fix M1/M2 (text-only) and the abstract parenthetical before upload.