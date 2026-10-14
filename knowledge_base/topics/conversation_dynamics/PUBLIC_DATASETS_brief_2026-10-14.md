# Public datasets brief — trajectory-level / early-outcome evaluation (2026-10-14)

*Researcher brief (factory session 2026-10-14) + orchestrator live verification. Purpose: redesign
the evaluation section of papers/trajectory_grammars_voice around PUBLIC datasets only (user
mandate: generic paper, no banking environment, no Spanish, no private-corpus claims).*

## Verdict
A TRACER-comparable public evaluation is achievable on **MultiWOZ 2.4 + ABCD + τ-bench
(retail+airline)**. **No public dataset supports all four terminal classes**
(contained/abandoned/handoff/compliance-escape): the honest public instantiation is a
**binary terminal outcome** (success/failure), with MultiWOZ's aborted flag as a weak
abandoned-like subclass [verify lineage] and τ-bench's write-check as a policy-compliance
ANALOGUE. Handoff + compliance-escape stay as the formal/operational classes, grounded by the
write-check analogue; state this explicitly or reviewers will flag the 4-class headline.

## Primary dataset recommendation
1. **MultiWOZ 2.4** — direct TRACER comparability (AUC 0.741 oracle / 0.617 generated, EDS 0.727,
   τ=0.7788 frozen on dev, FPR≤0.15 — all [V] from KB full-text); per-turn belief states ground
   trajectory features; maximal legitimacy. Caveat: document label derivation; check aborted-flag
   provenance; read TRACER's public code (github.com/erfan-nourbakhsh/TRACER [V]) for the exact
   split + failure-label derivation before committing our protocol.
2. **ABCD** — only major public TOD set with explicit customer-service action taxonomy per turn
   (closest public stand-in for grammar states); TRACER's best zero-shot transfer (0.771 [V]);
   real human-human dialogues.
3. **τ-bench retail+airline** — only candidate with native env-verified outcome labels (pass/fail
   incl. write-check) and native per-turn tool calls (tool-loop channel measurable); 2024-26
   legitimacy (Sierra; τ² 9,876-trajectory corpus [V]; Stanford τ² environment paper 2609.04611).
   Caveat: agent-generated trajectories w/ simulated users — state distributional caveat.
- Dropped: SGD as primary (TRACER's own zero-shot collapse 0.494 [V]); AgentBench/TheAgentCompany/
  SWE-bench (not dialogues); τ-Multilingual → optional voice-adjacent appendix (no outcome classes).

## Voice verdict
No public voice set carries terminal outcome labels (FDB family, IHBench, X2-Turn, τ-Multilingual
are component/quality benchmarks [V]). Honest framing: "text-chat TOD benchmarks; voice extension
with terminal outcomes is future work."

## Prior art (orchestrator-verified live 2026-10-14)
- **EarlyEval 2609.02783 [V full text]**: early outcome prediction via LightGBM dual-threshold
  halting on prefixes — datasets are **SWE-bench Verified / TerminalBench / Toolathlon, NOT
  dialogue** → no collision in TOD; gap INTACT for conversations. Cite as the eval-efficiency
  neighbor; contrast: behavioral features + calibrated thresholds vs our SPRT cost-asymmetric
  stopping over an outcome-class posterior. Code: github.com/inphotoo/earlyeval.
- **2609.25647**: reliability audit of trajectory-based early outcome prediction (calibration
  transfer within benchmark) — cite as concurrent. **2608.03222** Fail-Fast/Restart-Smart (SWE
  agents) — deployment-side early stopping, cite.
- **No 2025-26 paper found doing early/partial-trajectory outcome prediction on τ-bench or ABCD**
  (2 live rounds incl. this one). TRACER zero-shot ABCD remains the only dialogue prior [V].

## Open verification debts (before submission)
- [ ] MultiWOZ 2.4 sizes/split + aborted-flag lineage [unverified]
- [ ] ABCD action taxonomy details + license [unverified]
- [ ] τ-bench sizes/licenses [unverified]
- [ ] TRACER code read: exact split + failure-label derivation [V code URL only]
