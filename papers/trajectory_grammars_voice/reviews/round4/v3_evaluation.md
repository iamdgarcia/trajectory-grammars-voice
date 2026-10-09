All evidence gathered from the decision file and `sections/05_evaluation.tex` (read in full). No write tool is available in this runtime, and no shell tool exists to execute the check script, so per the brief's fallback clause the full verification report is returned here instead of being written to `reviews/round4/v3_evaluation.md`.

# Round-4 Verification — v3_evaluation (Evaluation-protocol verifier; r1/r2/r5 lane)

## Item verification

| Item | Applied? | Evidence (file:line) |
|---|---|---|
| #10 metric | YES | `05_evaluation.tex:40-58` — Eq. `eq:cost_weighted_latency` sums over `T \ {θ_esc}` (L41); `w(k)=(H−k)/H` with fixed per-scenario horizon H = campaign 90th-percentile call length, "not the realised length" (L48); "π_θ is the per-fold empirical class distribution" (L49); renamed "cost-weighted error" $\mathcal{L}_{cwe}$ with "correct decisions contribute zero" (L50); escape "excluded from the scalar… reported separately as detection rate at audit-precision, never averaged in" (L52). |
| #11 audit selection | YES | `05_evaluation.tex:21-24` — random audit stratum (10% of contained; all handoffs, all fraud-flagged), "calls outside the audited strata are treated as unlabelled rather than negative", per-class θ_esc precision "with a sensitivity analysis under negative-by-default labelling"; audit fraction stated. |
| #12 split axes | YES | `05_evaluation.tex:30-34` — two axes (campaigns, collection cycles); LOCO headline, temporal blocking "train past, test future" alongside; "per-campaign prevalence tables are published with the splits". |
| #21-partial artifacts | YES | `05_evaluation.tex:99-115` — CC-BY-4.0 + datasheet; SHA-256 split manifests; generator method (template replay, fitted timing/RTT) with two-sample distributional validation and reported synthetic-to-private gap; membership-inference + singularity re-identification check before release. Cost table `tab:costmodel` (L62-80) has full Provenance column. TRACER retraining base: "retrained for multi-class outcomes on our schema from the authors' public implementation" (L90). |
| #16/§5.3 variant attachment | YES | `05_evaluation.tex:55-59` — SPRT calibration checked against K(ε,c); "For the confidence-sequence variant… decision-time distributions are reported as empirical observations rather than checked against K. Every reported metric states which variant (SPRT or confidence sequence) produced it." |

## Internal consistency checks

- §5.5 dominance: "must dominate all five under the cost-weighted error metric $\mathcal{L}_{cwe}$ at per-class matched false-alarm budgets, not merely under ranking metrics" (`05_evaluation.tex:94`) — references L_cwe and per-class budgets. Consistent with L50.
- tab:costmodel escape row "$\infty$ (floor 20)" (L73) vs text: §5.3 says escape cost "is unbounded" and excluded from the scalar (L52); caption states "the escape row is a floor, not a finite price" and the table serves the stopping boundaries too, where a finite surrogate is required. Coherent; no contradiction.
- Every metric carries a variant: the blanket sentence at L59 covers EDS/latency quantiles/calibration; SPRT and CS are separately conditioned at L55-58. No orphan metric found.
- Bonus consistency: explicit-human-request exclusion from fraud signature present at L24-25 (item #15's §5.1 half), and GDPR hedging at L29-30 (item #14's §5.2 half) — adjacent items verified applied, no regression.

## New findings

No defects introduced by the revision were found. One cosmetic, non-blocking note: the equation label `eq:cost_weighted_latency` retains the pre-rename "latency" name while the metric is now "cost-weighted error" — internal label only, no reader-visible effect.

## Score

**9/10.** All five assigned items are applied with concrete, checkable language: the metric definition is now runnable (exclusion, normalisation, prior, rename all explicit), the audit protocol specifies rule + fraction + sensitivity, splits are two-axis with prevalence published, the artifact spec covers license/checksums/generator/re-identification, and variant attachment is enforced by a blanket sentence plus per-variant treatment of the K(ε,c) check. Internal cross-references (dominance claim, escape floor, fraud exclusion) are coherent. Residual gap is inherent, not a defect: results remain assertions about a private deployment — the protocol cannot be executed from the paper alone, and the release machinery (correctly) acknowledges this.

## Remaining mandatory

None in this lane.

## Note for supervisor

The brief's two execution steps could not be performed with available tools (read-only toolset, no shell): (1) writing this report to `reviews/round4/v3_evaluation.md` — full report returned above, please persist; (2) running `python papers/trajectory_grammars_voice/_check_figs.py` from `papers/trajectory_grammars_voice/` — must be run by the parent to confirm 52/52 still pass after the round-4 edits.