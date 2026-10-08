# Chief Editor Decision — Round 1

## Scores

| Reviewer | Score | Gist |
|----------|-------|------|
| R1 Methodology | 5/10 | Centerpiece theorem has a sign-flipped bound; error control unproven for the actual multi-class rule; prop:asymmetric contradicts its own proof |
| R2 Domain | 5/10 | Grammar cannot produce 3 of 4 terminal classes as specified; drift statistic counts the tool episode it exempts; fraud signature has no transition type |
| R3 Presentation | 6/10 | Cross-references untrustworthy: k*/δ/Λ symbol collisions, posterior conditioning contradiction, figures contradict text |
| R4 Related work | 7/10 | Verified landscape honest and accurate; missing Wald/POMDP/IHBench/ReAct/LangGraph citations; one mis-citation |

## Decision

**Major Revision.**
The framing, landscape verification, honesty (private vs releasable), and nearest-neighbor
positioning are above the bar — reviewers uniformly credit them. But the paper's claim to
novelty is its *guarantee*, and that guarantee is currently defective as stated: a sign-flipped
null-case bound (verified at 04_stopping.tex:69-74), a proposition asserting the opposite of its
proof (04_stopping.tex:126-138), error control asserted for a rule the cited machinery does not
cover, and a grammar whose transition table cannot reach three of its four terminal classes
(verified). All are fixable with targeted edits; none requires new research.

**Complaint dropped as a misread:** R4's question about TRACER's "training-time early-prediction
reward" — TRACER's full text does define the `L_early` reward term; §5's claim stands.

## Consolidated mandatory revisions

1. **[P0] Fix the sign-flipped null-case time bound** (`04_stopping.tex`, thm:stopping, eq:times):
   E[k_dec | θ_0] bound must be [(1−α_a)B_a + α_a A_a]/μ_0^a with μ_0^a < 0 (negate as displayed);
   re-verify the θ_a case (positive, correct).
2. **[P0] Establish error control for the rule actually defined** (`04_stopping.tex` §4.2–4.3):
   add supermartingale/Ville route (correctly specified emissions ⇒ e^{Λ^a} is a θ_0-supermartingale;
   P_0(∃k: Λ_k^a ≥ A_a) ≤ e^{−A_a} = α_a/(1−β_a) ≤ α_a) or redefine per-class stopping;
   add hypotheses: correct emission specification, a.s. termination or E[k_term] < ∞
   (tool-call self-loop makes unbounded runs representable), integrable increments;
   fix the garbled optional-stopping sentence.
3. **[P0] Rewrite prop:asymmetric to match its proof** (`04_stopping.tex` §4.5): compliance-escape
   fires at first credible signal (A_esc small, β_esc → 0, α_esc elevated); reconcile §6.3's
   "calibrates conservatively" sentence.
4. **[P0] Make all four terminal classes reachable** (`03_grammar.tex` Table 1 + Definition):
   add `service-complete` (q_close → θ_cont), `hangup` (→ θ_aban), and an explicit θ_esc semantics
   (unguarded-close type or audit-overlay definition, as §6.5 does); reconcile fig_grammar.
5. **[P1] Resolve symbol collisions:** k* → k_cyc (latency cycle bound) and K(ε, c) (decision-time
   bound, with explicit prior over terminal classes and error-budget allocation ε = Σ_a(α_a+β_a));
   transition function δ → keep, error budget δ → ε; LLR Λ_k^a → ℓ_k^a (keep Λ_k for the silence
   gap); terminal set T vs 𝒯 → one symbol; EDS length T_i → L_i.
6. **[P1] Unify posterior conditioning on the multi-channel observation o_{1:k}** everywhere in
   §4–§7 and fig_eval_stack; include the turn-state channel in the emission list.
7. **[P1] Fix cycle-depth definition:** D = count of regression-typed transitions (self-loop
   tool-call does not increment; tool-fail does); drop the monotonicity claim or say the monitor's
   counter is policy-resettable (reconcile §6.1); align fig_cycles threshold with
   rem:drift_trigger.
8. **[P1] Redraw figures:** fig_grammar with all seven progress states (q_clarify present) and
   every drawn edge a Table 1 type (add disclosure, endpoint-error, user-bargein; escalation from
   any q_p); fig_stopping as LLR trajectories vs A_a/B_a boundaries with a shaded joint θ_0
   region (not posteriors crossing "accept H_1").
9. **[P1] Demote lem:cyclebound(ii) to a remark** (or derive an explicit hazard bound); fix the
   "k* tool-loop cycles" wall-clock/turn-count slide in §1, §4.4, §6.3.
10. **[P1] Fix cor:tracer:** one-sided boundary (not "symmetric"); remove anytime-validity
    attribution OR state the confidence-sequence rule formally (it is the rule deployed in §5).
11. **[P1] Cite sequential-analysis foundations** (`04_stopping.tex`): Wald (1947), Wald–Wolfowitz
    (1948) optimality, one anytime-valid confidence-sequence reference (Howard et al. 2021 or
    Waudby-Smith & Ramdas 2023) — seed KB entries `wald1947sprt`, `waldwolfowitz1948optimality`,
    `howard2021time` (verify IDs) before citing.
12. **[P1] Add the POMDP dialogue strand** (`02_background.tex`; seed `young2013pomdp` — Young et
    al. 2013, Proc. IEEE): belief over dialogue state ≠ posterior over terminal business outcomes;
    no decision-time guarantee; pre-LLM. Qualify the "first formal trajectory layer" claim in §9.
13. **[P1] Fix the guardrail mis-citation** (`06_intervention.tex` §6.5): replace
    garcia2026cessationfloor with rebedea2023nemo + dong2024building (dialogue-level rails);
    add one guardrail sentence to §2.5.
14. **[P1] Cite yao2023react at the first ReAct mention (§1) and langgraph2024 in §6.1.**
15. **[P1] Cite salimi2026ihbench in §6.2** (post-interruption recovery anchor).
16. **[P2] Hygiene:** fix bib entries (garcia2026latencyfloor note, garcia2026cessationfloor venue,
    falsesuccess2026 authors); align §9 HF-release wording with §5.7 (synthetic, not real logs);
    define λ_mon^irr at first use; define c(θ̂,θ) before §4.5 "recall"; fix overfull boxes.

## Optional suggestions worth doing

1. Unify observation notation sentence (fixed under mandatory 6).
2. Strengthen or fold prop:longer_offpath into prose.
3. §5.4 EDS credit sentence: keep (verified fair).
4. Add TurnNat/multi-party VAP lineage only if a sentence naturally invites it (not mandatory).
