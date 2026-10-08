# Next-Paper Angles — Discovery Synthesis

Source: 5 parallel researcher agents, launched after publishing `cascade_voice_latency` (Latency Floor of
Cascade Voice Agents). Each brief has: LANDSCAPE / THE GAP / CANDIDATE CONTRIBUTION / EXTENSION ANGLE / ANCHORS.
Full briefs: `angle_1..5_*.md` in this folder.

| # | Angle | Working title (agent) | Direct reuse of published work | KB gap closed |
|---|-------|----------------------|-------------------------------|---------------|
| 1 | Realtime memory / forgetting under deadlines | *The Forgetting Floor: Context Eviction Under Latency Deadlines* | Reuses streaming-cascade floor Λ*_SC + k-step ReAct floor; compiles "context grows with tool observations" footnote into a Compound Memory Floor theorem | G1 (bridges) |
| 2 | Interaction dynamics beyond latency (barge-in / interruption) | *The Barge-In Barrier: Interruption Reaction Latency* | Dual of the Latency Floor: bounds response *cessation* using the same DAG + reducible/irreducible decomposition; "start fast and stop fast" program | — (touches G1) |
| 3 | Safety & guardrails placed inside the DAG deadline | *The Safety Deadline: Guardrail Placement Inside the Latency Floor of Realtime Voice Agents* | Guardrail-as-stage; Safety Deadline Theorem is a derived corollary of the Latency Floor Theorem + CCC; shadow window as free slot; per-step re-arming via k-step bound | **G1 (5) + G3 (5)** |
| 4 | Tool round-trips / multi-step orchestration | *Hiding the Tool Round-Trip: A Latency-Budget Model for Realtime Orchestrated Voice Agents* | Generalizes ReAct theorem to branched typed tool DAGs (type A/B/C tools); our 2025 result becomes a special case; Tool-Parity lemma formalizes filler levers | G1 (schedules guardrail cost per tool result) |
| 5 | Evaluation standard / benchmark for realtime agents | *Measuring Responsiveness: A Standardized Evaluation Stack for Realtime Agentic Systems* | Makes the CCC an empirical compliance metric; derives per-class floors then measures gap percentiles against them; extends reducible/irreducible split to measurement validity | **G4 (4)** + G1 |

## Assessment

- **Strongest continuity + highest KB value: #3 Safety Deadline.** Alone among the five it bridges BOTH project
  threads (latency paper + ai_guardrails KB) and answers the two top-scored open gaps (G1, G3). The thesis
  ("no paper models safety as a schedulable stage inside the latency floor, or a missed deadline as a bypass
  with abort fallback") reads as the natural sequel and is defensible as a *formal* gap, not just an
  engineering one. Risk: prefix-safe classification may exist under another name (FUDGE/GeDi lineage) — novelty
  then narrows to deadline + placement + certification, which is still open.
- **Highest general impact / clean theorem: #4 Tool Latency Budget.** Every production voice agent ships
  tool-calling; the TILB schedulability condition (CCC-with-tools) and type-A/B/C tool taxonomy extend the
  published React theorem exactly ("our 2025 result = special case"). Best if the group wants breadth of
  audience over safety focus.
- #2 Barge-In is elegant (the missing "stop fast" half of the floor) but the most tied to HCI/pragmatics;
  #1 Memory is strong but overlaps #4 (re-tokenization cost) and needs an empirical "forgetting cliff"
  campaign; #5 is a benchmark/meta paper — good capstone or companion, weaker as a standalone theory paper.

## Method note (all five agents)

No live `web_search` tool was available in the child runs; citations were assembled from high-confidence
knowledge + local KB. Every arXiv / venue ID marked `[verify]` / `[med]` in the briefs MUST be verified on
arXiv before any KB entry or `\cite{}` — suggested as the first step of the selected angle's Stage 1.

## Candidate next step

Run Stage 1 (gap detection) for the chosen angle: populate `knowledge_base/topics/<topic>/papers/` with
verified entries, cross-check `gaps.md`, write `OUTLINE.md`, then proceed through the pipeline.
