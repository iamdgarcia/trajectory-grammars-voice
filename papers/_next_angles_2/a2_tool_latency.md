# Tool Round-Trip Latency Budget (REFRESH)

## Working title
"Hidden Reads, Irreversible Transfers: A Reversibility-Aware Latency Budget for Tool-Calling Voice Agents"

## Landscape
1. **ReAct** (arXiv:2210.03629) — serial reason→call→observe loop; the (k−1)·λ_tool term our published thm:react already exposes, left unformalized.
2. **Speculative decoding** (arXiv:2211.17192) — canonical hide-work-under-verification pattern; the structural template for speculative tool calls.
3. **Speculative RAG** (arXiv:2407.08223) — retrieval RTT hidden under drafting; one-trick existence proof of a hideability window W.
4. **τ-bench** (arXiv:2406.12045) — tool-agent benchmark with explicit latency/price axes; measures, never predicts from DAG structure.
5. **Agents Are Not Enough** (arXiv:2412.16241) — intent prefetch can skip tools entirely; hiding is unsystematic.
6. **Full-Duplex-Bench v3** (arXiv:2604.04847) — tool use under disfluency for native full-duplex models only; cascade untouched.
7. **Speculative tool execution, Qualcomm/KAIST** (arXiv:2610.07641, `jung2026speculativetool`) — rule-triggered speculative tool calls from partial ASR; prefetch-only wastes 47% of calls, direct injection is the win. **The new adjacent prior.**
8. **Voice-Light** (arXiv:2609.20995, `braun2026voicelight`) — speculative generation with promotion-by-revision-type reconcile; fixed acoustic trigger; learned turn gate failed its locked eval.
9. **OpenAI Realtime API / MCP** (vendor docs + spec) — parallel function calling and filler audio ship in production; scheduling opaque, no budget theorem, no schedulability condition.

## The gap
**Testable RQ:** given a tool DAG whose nodes carry a (hideability type A/B/C, reversibility class idempotent/compensable/irreversible) pair, what schedulability condition makes CCC-with-tools hold — `Λ_floor + Σ_{type A} λ_tool^irr ≤ τ` — and what speculation policy maximizes expected budget saving minus wasted-call and rollback cost?

**Why unsolved after the 2025-10 refresh:** (i) `jung2026speculativetool` proves speculative tool execution works but uses word-count/pause triggers, one tool class (web search), English, on-device — no DAG composition rule, no reversibility axis, no schedulability theorem, TTFA measured from end of speech; (ii) the typed-DAG machinery (A/B/C hiddability + CCC-with-tools + API-valid serializability, PoC-verified per OG3) is published nowhere; (iii) the old TiLT anchor is **dead** (arXiv 2502.19162 is a condensed-matter paper; deprecated in the KB), so pre-EOU tool dispatch is now anchored only by jung; (iv) nobody separates speculation-safety by reversibility: speculating an idempotent balance read is free; speculating an irreversible transfer is not an optimization but a safety violation.

## Candidate contribution
1. **Hiddability×Reversibility matrix** — type A/B/C × (idempotent / compensable / irreversible); theorem: only (A, irreversible) is both unhideable and unspeculatable — the irreducible core of any money-moving turn.
2. **CCC-with-tools schedulability theorem** — critical-path floor over the tool DAG; the published linear `Λ_k*` (thm:react) is the all-type-A-serial special case.
3. **Speculation-risk lemma** — `E[Δ] = P(hit)·δ_tool − P(miss)·(cost_wasted + cost_rollback)`, with `cost_rollback = ∞` for irreversible tools; formalizes why filler + speculative reads are safe and writes never are.
4. **ToolGap-1 benchmark** — synthetic RTT distributions × policies (serial / parallel-split / speculative / filler-hold), endpoints: end-of-speech↔first-audio and perceived silence; banking tool mix as headline scenario.

## Reuse of our published results
- Paper #1: thm:react + CCC = the collapsed special case; streaming floor's prefill-hiding window W = the tool-hiding window.
- Paper #2: generation-interruptible vs execution-persistent is exactly the reversibility axis; barge-in-cancelled tool calls (SV3) become rollback events in the risk lemma.
- jev-vad: P(turn-end) as speculation gate (SV4's open question in the KB) — optional cross-hook, not the lead; honest constraint: ES turn-end is near chance from text (0.40-0.54), so semantic speculation gating is fragile in Spanish.

## Banking grounding
- Core-banking RTTs ~0.5-2 s against τ_human ≈ 200 ms: a single type-A transfer RTT alone breaks CCC → budget predicts filler-hold or split-turn; the production voice monolith production telemetry can validate.
- Idempotency keys (standard in banking APIs) are precisely what makes speculative balance reads safe to retry and duplicate speculative transfers detectable — the API primitive the risk lemma formalizes.
- Irreversible transfers: speculation must be vetoed regardless of latency; audit-trail logging of speculative calls is a real compliance requirement.
- Tool backends span the full matrix in one system: balance reads (speculatable, idempotent), card blocks (compensable), transfers (irreversible).
- Spanish-first: no multilingual speculative-dispatch evidence exists; ES interim transcripts are the unmeasured regime.

## Scores (1-5)
- **Novelty 3** — typed-DAG schedulability + reversibility axis unclaimed, but bare speculative tool execution published weeks ago (jung).
- **Fit 5** — direct generalization of two published theorems; OG3 lists the exact candidate contribution.
- **Banking 4** — idempotency, irreversibility, and real RTT telemetry are ours; no external banking-latency literature anchor to lean on.
- **Feasibility 4** — serializability lemma already PoC-verified; benchmark is synthetic-RTT-cheap; theorem is incremental over existing machinery.
- **Risk 3** — jung/braun show the neighborhood is moving fast (two papers in three weeks); TiLT anchor lost; theorem could be scooped.

## Verdict
**Pursue now.** The schedulability theorem + reversibility axis remain unclaimed and our published machinery yields a defensible "our 2025 result is the special case" story. Conditions: position explicitly against jung2026speculativetool (reversibility × DAG composition × server cascade vs its rule-trigger × single-tool × on-device), and purge every TiLT citation.
