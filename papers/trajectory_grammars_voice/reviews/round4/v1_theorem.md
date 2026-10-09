# Round-4 Verification — v1_theorem (Theorem lane, r10 + round-1-r1)

## Item verification

| Item | Applied? | Evidence |
|---|---|---|
| #1 (P0) aggregate θ₀ time bound | ✅ | `sections/04_stopping.tex:96–100` (eq:times): E[k_dec\|θ₀] ≤ min(E[k_term], Σ_{j∈A}(\|B_j\|+c)/\|μ₀^j\|); aggregation rationale at :100–104 ("gated by the slowest class-wise descent"); proof-sketch sum argument at :116–118. r10's counterexample is blocked: the bound is the sum, not per-class min. Math check: E[max_j T_j] ≤ Σ_j E[T_j] for nonneg T_j (valid), and per-class Wald+bounded-increment gives E[T_j] ≤ (\|B_j\|+c)/\|μ₀^j\| since E[ℓ_T] ≤ B_j−c and μ₀<0. **The sum argument is true.** |
| #5 three-exit decomposition, own-upper-crossing envelope | ✅ | eq:kdec (:44–52) has all three exits; eq:times θ_a-side (A_a+c)/μ₁^a via a's own crossing (:94, :110–115) — correct: k_dec ≤ T_a unconditionally, Wald with overshoot ≤ c gives the bound; Lorden cited (:115). Mean-one LR sentence corrected to "E[e^{Z_k}\|F_{k−1}]=1 exactly", conditional independence explicitly not needed (:109–110). |
| #6 budget scope + pairwise LR | ✅ | `rem:budget_scope` (:119–135): ε prices {action\|θ₀} and {θ₀\|θ_a}; cross-action unpriced; pairwise martingale e^{ℓ^b−ℓ^a} ⇒ Pr_{θ_a}[declare θ_b] ≤ α_b/α_a when A_b > A_a — correct (declared-θ_b requires θ_b's crossing to precede θ_a's, so ℓ^a < A_a at that turn). Properly scoped "operating curve, not a theorem". |
| #4-partial fraud asymmetry coherence | ✅ | Within my lane: prop:asymmetric (:186–199) and Table tab:costmodel (`05_evaluation.tex`) agree — escape miss cost ∞ (floor 20) ⇒ A_esc smallest, β_esc→0; def:rule contains no user-answer/D coupling, so no contradiction. Full #4 belongs to the 06-lane reviewer. |
| #16 guarantee qualified in abstract | ✅ | `main.tex` abstract: "expected decision time at most K(ε,c) turns at confidence 1−ε **under standard sequential-analysis assumptions on the emission model**" — one-clause scoping present. |

**K(ε,c) consistency:** thm definition (:101–103, max of the two conditional envelopes) ≡ eq:times envelopes; abstract uses it without redefinition (fine); `05_evaluation.tex:78` requires realized E[k_dec] ≤ K for the SPRT variant and explicitly exempts the confidence-sequence variant. Consistent across all three sites. No contradiction with def:rule (∀a lower-boundary reading matches :101–104) or prop:asymmetric.

## New findings

- **[P1] Corrupted `\ref` introduced by the rewrite**: `sections/04_stopping.tex:140–141` — line 140 ends "…the protocol of Section~" and line 141 begins "ef{sec:evaluation} measures them)". The `\r` of `\ref` was lost (CR→LF normalization). It compiles silently (braces balance) and typesets garbage "Section efsec:evaluation" in the second remark — which is why the 0-error/0-warning gate and the 52-check suite missed it. Smallest fix: restore `Section~\ref{sec:evaluation}` on one line.
- Residual risk: the "orphan `ef{`" sweep could not be run by me (ripgrep unavailable in this runtime); the parent should sweep all sections. No duplicate labels and no broken label/reference observed in 04_stopping.tex; the unnumbered-vs-numbered extra equation number on the K(ε,c) row of eq:unconditional is cosmetic only.
- P2 note (not a defect): as β_esc→0 under prop:asymmetric, \|B_esc\| inflates the θ₀-side sum — an inherent SPRT trade-off, honestly reflected by the bound; a one-line remark could pre-empt a future reviewer.

## Score

**8/10.** All five assigned items are verifiably applied and the core mathematics now holds: the aggregated θ₀ bound is genuinely true (sum-over-classes via E[max] ≤ Σ E[T_j], with Wald/Lorden constants correct), the θ_a envelope via own upper crossing is correct and tight, the pairwise-LS remark is sound under its stated A_b > A_a condition, and K(ε,c) is consistent abstract/theorem/§5.3. The only defect in this lane is the mechanical `\ref` corruption at :140–141, introduced by the edit machinery and already in the parent's fix queue — it does not touch the math.

## Remaining mandatory

None in this lane (0 of my 5 items outstanding; the :140–141 `\ref` fix is a revision-machinery defect tracked by the parent, not one of the 22).

`_check_figs.py`: not-run — no shell/exec tool in this runtime (supervisor confirmed report-only); parent must run the once-authorized `python papers/trajectory_grammars_voice/_check_figs.py`.

FINAL: v1_theorem | score=8 | remaining=0 | all 5 theorem items applied & math verified; one P1 corrupted \ref at 04_stopping.tex:140–141 (fix already in flight)
