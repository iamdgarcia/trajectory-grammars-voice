# NOTES — trace2trajectory (open questions for the writing stage)

## Venue / format
- Template: `templates/arxiv_preprint/` (natbib, TikZ, one sentence per line) — same house style as the sibling papers.
- Primary: cs.AI. The paper is evaluation-methodology + visualization, not safety-critical → no cs.CR cross-list needed (decide finally at Stage 6).
- Length target: sibling paper is 27pp; this one is a *methods + protocol* paper — aim 18–22pp with 3 TikZ figures.

## Content decisions to make at Stage 3
1. **Real-log case study?** The worked example is fixture-scale (3 conversations: 2 real / 1 sim, 40.2% coverage).
   If the internal voice-bank project log access lands before writing finishes: add a real-call section (even 50–100 calls,
   GDPR-safe schema) — it upgrades the paper from "protocol + demo" to "protocol + field evidence".
   If not: keep fixtures, say so honestly in 08_discussion.
2. **Simulator integration demo?** Running the atlas against the a6 simulator (personas →
   conversations → coverage before/after calibration) would demo the *recommendation loop*
   (uncovered region → generated scenario → coverage delta). Cost: depends on a6 build order.
   Minimum viable version: a scripted "uncalibrated vs calibrated" sim set showing coverage
   move — the point is the metric's discriminative power, not simulator quality.
3. **MiniLM variant in or out?** Recommendation: OUT of the main line (keep the deterministic
   baseline as the headline; the embedding variant is the named future work + one sensitivity
   paragraph). Two engines in one methods paper doubles the attack surface at review.
4. **$\theta_{esc}$ treatment**: inherited as audit overlay from the sibling grammar. Keep the
   inherited framing verbatim; do not re-derive — cite `garcia2026grammar` and move on.
5. **Figure count**: 3 TikZ (`fig_pipeline`, `fig_coverage`, `fig_atlas`). If page budget tightens,
   `fig_pipeline` can compress to inline notation; never cut `fig_coverage` (it IS the paper).

## Risks / reviewer landmines (pre-mortem, from sibling-paper reviews)
- **"Just a heuristic"** on rule-based $\tau$: answer = config-exposure + emission-model abstraction
  (any calibrated estimator replaces `infer_states()`; the interface is the contribution).
- **"2-D projection is lossy"**: answer = coverage is defined on the projection, PCA basis fit on
  real-only is a stated design commitment, sensitivity protocol in 06.
- **"Grid resolution is arbitrary"**: answer = the $\rho/\beta/\varepsilon$ stability envelope IS
  part of the protocol; determinism makes the sweep exact.
- **"Fixture-scale"**: answer = honest scoping in 08; the artifact ships runnable code; field
  validation named as the follow-up (or added if logs land).
- **Overlap with 2605.07847**: response-level vs trajectory-level — make the delta table explicit
  in 02 (their axis: response distributions; ours: grammar walks + region coverage + outcome
  classes + per-class breakdown).
- **"Atlas = UMAP plot"**: answer = determinism + real-anchored basis + occupancy threshold +
  per-class semantics + exemplar recommendation loop; \citep{wildvis2024} contrast in 01.

## Cross-artifact wiring
- Code release: `github.com/iamdgarcia/trace2grammar` (MIT, clean-room verified, 46 checks (26 extract + 14 coverage + 6 smoke; 2026-10-19 re-verified)) — cite in the artifact section; freeze the CLI interface before Stage 4.
- The worked-example numbers (40.2%, per-class 45.3/35.2) must be re-generated at camera-ready if the fixtures change — add a `_regen.sh` note in 05.
- Index: INDEX.md links this paper dir under the trace→trajectory angle.

## Stage-1 gate recap (from OUTLINE)
- gap_score 5 (mapping + atlas unclaimed; four scan rounds), conceptual: true, honest risks
  recorded → **PASSED**. Proceed to Stage 3.
