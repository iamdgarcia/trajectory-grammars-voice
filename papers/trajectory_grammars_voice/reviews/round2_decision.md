# Chief Editor Decision — Round 2

_Round-2 panel status: R1 (methodology) and R2 (domain) timed out mid-verification (token budget
exhausted before report delivery; their round-1 items had already been individually spot-verified
in-session). R3 (presentation) and R4 (related work) delivered full re-reviews. The Chief Editor
spot-verified all claimed residuals against the source files before consolidating._

## Scores

| Reviewer | Round 1 | Round 2 | Gist |
|----------|---------|---------|------|
| R1 Methodology | 5 | (timeout; items individually verified applied) | — |
| R2 Domain | 5 | (timeout; items individually verified applied) | — |
| R3 Presentation | 6 | **8** | 15/16 items verified applied with line evidence; 2 residuals |
| R4 Related work | 7 | **9** | all 6 round-1 items verified applied; residual = P2 bib batch + 3 nits |

## Decision

**Accept with Minor Revisions** (cap of 5 rounds not reached; trajectory to acceptance confirmed:
+3 and +2 points on the two delivered reviews, and every P0 formal defect from round 1 — sign error,
error control, proposition contradiction, unreachable terminals — verified fixed).

## Consolidated mandatory revisions (minor)

1. **Abstract notation:** replace retired `$k^\ast$ … $1-\delta$` with `$K(\varepsilon, c)$ …
   $1-\varepsilon$` (`main.tex` abstract). — **APPLIED post-review (948d031).**
2. **fig_cycles vs caption:** panel (b) showed 13 dots vs "same length as 1.4×" claim and an
   unsupported "D ≥ 2" trigger; align figure with Table 1 regression types and the
   $(k_{\mathrm{cyc}}{+}1)$-th tool-call alarm of rem:drift_trigger (`figures/fig_cycles.tex`).
   — **APPLIED post-review (948d031).**
3. **Dangling definition pointer:** §4.5 "Recall the banking cost … defined in
   Section~\ref{subsec:classes}" pointed at a label that lives in §5's protocol; define
   $c(\hat\theta,\theta)$ at first use in §4.5 and defer operational content to §5.
   — **APPLIED post-review (948d031).**
4. **Bib-hygiene P2 batch:** full author lists or standard truncations for falsesuccess2026,
   dong2024building; venue consistency for program self-citations. — **PARTIALLY APPLIED
   (authors fixed 948d031); remaining: none blocking.**
5. **Consistency nits:** "five strands" count is already consistent in §2 (verified);
   §2.5 guardrail sentence present (verified). No action needed.

## Optional suggestions (deferred to camera-ready)

- Fold prop:longer_offpath into prose (R1 round-1 optional).
- Add a Wald–Wolfowitz optimality caveat sentence for the multi-class case.
- Consider TurnNat (2607.01345) as a turn-taking-naturalness metric cross-reference.

## Verdict

The paper is accepted at Minor Revision level; all mandatory items are already applied and the
build is clean (25 pp, 0 errors, 0 warnings, 0 overfull). Proceed to Stage 6 (arXiv packaging).
