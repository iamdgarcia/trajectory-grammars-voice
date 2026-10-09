Turn budget wrap-up was requested after 18 assistant turns (soft limit 18, grace 2). Process-mode live steering is unavailable, so the child was warned at launch to wrap up by this budget. Output may be partial.

Verification complete. All four assigned items checked against source; I have no write-capable tool, so per instructions the full report is returned here (runtime to persist to `papers/trajectory_grammars_voice/reviews/round4/v4_intervention_domain.md`).

**v4_intervention_domain | score=8 | remaining=1 | fraud lane repaired on all four items; one residual: q_auth re-visit statistic is vacuous under Table 1 (no transition re-enters q_auth)**

# Round-4 Verification — v4_intervention_domain (r7/r8 lane)

## Item verification

| Item | Applied? | Evidence |
|---|---|---|
| #4 fraud signature on q_auth re-visits; user-answer never increments D | Textually yes, with residual defect (see New findings) | `sections/06_intervention.tex:80-82`: "the monitor counts re-visits of $q_{auth}$ … these, not \texttt{user-answer} (which is progress and never increments $D$), are the events the signature reads." Consistent with `sections/03_grammar.tex` def:cycledepth (D counts regression-typed transitions only) and Table 1 (user-answer rows marked progress). |
| #13 per-call clarify budget; D resets only on user-confirmed resolution | Yes | `06_intervention.tex:23-30`: reset "only on user-confirmed resolution … never on the intervention itself"; "per-call budget (three tokens in the deployment defaults) … after which the only available actions are escalate or close." Matches `03_grammar.tex` def:cycledepth reset sentence ("user-confirmed repair (a disclosure or a confirmed resolution)"). No contradiction between 6.1's budget/hysteresis and 3.2's reset: budget caps tokens, reset governs D. |
| #15 handoff requests unconditional, excluded from fraud channel | Yes | `05_evaluation.tex:~29-30` (§5.1): "honoured unconditionally … route to \texttt{handoff} regardless of the posterior and are excluded from the fraud-signature channel." `06_intervention.tex` contains no contradicting claim — its fraud channel reads only auth re-visits, tool-fail, and the silent detour. |
| #22 benign base rate + ATO/SIM-swap scope | Yes | `06_intervention.tex:89-92`: auth-cycling "dominated by benign causes … never by itself a fraud verdict … measures the benign cycling base rate"; `:93-95`: ATO with passed auth (SIM-swap, coached credentials) "complements --- and never replaces" transaction/device controls. |

**Coherence checks requested:** (a) Fraud section vs def:cycledepth/Table 1 — D-consistency holds (user-answer progress ✓, tool-fail regression ✓), but the signature's primary statistic is not generable (finding below). (b) Hysteresis/budget vs 3.2 reset — consistent; hysteresis is 6.1-only and unreferenced by 3.2, no conflict. (c) §6.3 overclaims — none left: "survives paraphrase" is scoped to paraphrase and immediately conceded by the spine-walking scope condition; the action-vs-detection conservatism sentence coheres with Prop:asymmetric (`04_stopping.tex`, prop:asymmetric) and Table tab:costmodel (false escape flag 0.5 vs missed escape ∞/floor 20).

## New findings

- **P1 — q_auth re-visit statistic is structurally zero under Table 1** (`sections/06_intervention.tex:77-82` vs `sections/03_grammar.tex` Table 1, `figures/fig_grammar.tex`). No typed transition targets $q_{auth}$: user-answer is $q_{auth/\ldots} \to$ next spine (forward only), endpoint-error is $q_{intent/confirm} \to q_{intent}$, agent-clarify is $q_{intent/confirm} \leftrightarrow q_{clarify}$, tool-fail is $q_{tool} \to q_{tool}$; fig_grammar draws only gr→au entering au. "Repeated auth re-visits" can therefore never be generated, recreating the vacuity r7 flagged. Also "tool-fail regressions between them" contradicts "no progress into intent" (tool-fail lives in $q_{tool}$, downstream of intent). Smallest fix: add one regression row \texttt{auth-fail} ($q_{auth} \to q_{auth}$, emitter: auth service) to Table 1 + one edge in fig_grammar, and drop or rescope the "tool-fail between them" clause.
- **P2** — `06_intervention.tex:96-97`: "\texttt{tool\_loop}" names no state or type; should be \texttt{tool-call} or $q_{tool}$.
- **P2** — Monitor-initiated clarify from states outside $\{q_{intent}, q_{confirm}\}$ (e.g., $q_{tool}$) has no Table-1 type; scope the clarify action or widen agent-clarify sources.
- **P2** — Benign-cycling base-rate measurement promised to §5 (`06_intervention.tex:91-92`) but §5 never names it; one clause in 05 §5.1 closes the dangling reference.

## Score

**8/10.** All four lane items are substantively applied with correct hedges; the fraud section now reads as a scoped, base-rate-aware routing signal with honest ATO limits. The single residual is that the headline statistic (q_auth re-visit count) is not an executable shape test under the paper's own transition table — the exact coherence class the item was meant to close. One table row fixes it.

## Remaining mandatory

1. (Partial re-open of #4, P1) Add an auth-fail regression type (or equivalent q_auth re-entry transition) to Table 1 + fig_grammar so the q_auth re-visit count is generable; fix the "tool-fail between them" clause.

**Supervisor must run:** `python _check_figs.py` from `papers/trajectory_grammars_voice/` (no shell tool in this lane). I statically verified its fraud/intervention assertions against sources: `never increments $D$` ✓, `re-visits of $q_{auth}$` ✓, `per-call budget` ✓, `dominated by benign causes` ✓, `SIM-swap` ✓ (06), `excluded from the fraud-signature channel` ✓ (05).