# Realtime Orchestration — Research Gaps

_Aggregated from paper entries + discovery agents on the orchestration layer of cascade voice agents._
_Created 2026-09-01 alongside papers/cascade_orchestration_floor/OUTLINE.md._

## Gap OG1: Orchestration-Layer Latency Floor (three clocks) — gap_score: 5

**Problem:** The published Latency Floor work (`papers/cascade_voice_latency/`,
`thm:latency_floor`, `thm:react`) bounds latency *between* ASR/LM/TTS but treats the LM stage as a
black box with k serial hops. No formal model exists of how the *orchestration* inside that stage
schedules reasoning hops, tool calls, fillers, and interruptions, nor of when orchestration turns
reducible latency into hidden latency.

**Evidence:** `langgraph2024` (graph orchestration, static wiring), `yao2023react` (serial loop),
`schlangen2011general` (incremental modules never materialized into an agent runtime),
`skantze2021turn` (no standard, no formal model).

**Candidate contribution:** Orchestrator-as-event-system with three decoupled clocks (generation /
delivery / tool) + topology-latency equivalence theorem. → **Demoted 2026-09-01:** folded into
`responsiveness_floors` as the event-system *mechanism*; kept here as future-work potential, not the
paper's lead (lead moved to OG2).

---

## Gap OG2: Cessation / Barge-In Floor — gap_score: 5

**Problem:** Response *onset* is bounded (published CCC, τ_human); response *cessation* —
reaction time from user barge-in to the agent's audio actually stopping — is modeled by nobody.
The longer a cascade agent talks, the more audio is in flight in the TTS queue before it can stop.

**Evidence:** `skantze2021turn` (barge-in/latency trade, no bound), `raux2008optimizing` +
`raux2012optimizing` (operational endpointing, no lower bound), `schegloff2000overlap`,
`heldner2010gaps` (overlap timing), `defossez2024moshi` (full-duplex interruption, no analysis).

**Candidate contribution:** Cessation floor detect/decide/cease/resume with the
generation-interruptible ∩ execution-persistent separation (PoC-verified).

→ **SELECTED (2026-09-01). This is the lead of `papers/cascade_orchestration_floor/OUTLINE.md`
(`responsiveness_floors`): cessation as the missing second floor alongside the published onset floor.**

---

## Gap OG3: Tool-Hiding Budget (typed tool DAG) — gap_score: 4-5

**Problem:** Tool round-trips (network RTT ~1 s against real backends) dominate the middle stage,
yet no composition rule states which tools can be hidden under generation/speech (type A/B/C) and
what happens when unhideable type-A RTT exceeds the budget.

**Evidence:** `specrag2024` (retrieval overlap, one trick), `tilt2025` (pre-EOU dispatch, one trick),
`agentsnotenough2024` (prefetch, unsystematic), `openai2024realtimeapi` (vendor tool scheduling,
opaque), `taubench2024` (latency axis, not structural).

**Candidate contribution:** Type A/B/C classification + CCC-with-tools schedulability condition +
API-valid serializability lemma (PoC-verified).

---

## Gap OG4: Filler Placement (delivery vs generation clock) — gap_score: 4

**Problem:** Whether filler should be emitted by the reasoning model (LLM filler) or by the delivery
layer (canned/procedural) is undecided in practice. Product evidence shows LLM filler bleeds into
real answers (documented rejection in the production voice monolith); no formal reason is given.

**Evidence:** `ward2000backchannel` (timing rule, delivery-side), `levinson2015timing` / `stivers2009universals`
(perceptual basis), PoC delivery-status clock.

**Candidate contribution:** Filler-hygiene claim — filler belongs in the delivery clock; only the
delivery clock may mask without corrupting the generation stream.

---

## Gap OG5: Perceived V2V and Barge-In Measurement — gap_score: 5 (protocol)

**Problem:** Product telemetry measures server-side V2V (`T0 → tts.first_audio`); the *perceived*
latency (audible on speaker) and barge-in reaction are `nadie` (measured by nobody) in
`docs/bench/medicion-latencia-v2v.md` of the production voice monolith.

**Evidence:** `skantze2021turn` (no standard eval), product telemetry vocabulary.

**Candidate contribution:** Measurement protocol for perceived V2V + barge-in latency across
orchestration topologies (small rig, not a production campaign).

---

## Already-Addressed / Bridge Gaps (do not re-propose here)

- Inter-component latency floor of cascades: **addressed** by `cascade_voice_latency`
  (`thm:latency_floor`, `thm:streaming_floor`, `thm:react`).
- Basic graph orchestration frameworks: saturated (`langgraph2024`, `yao2023react` + many
  follow-ups).
- Streaming-safe guardrails (G1) and linear-cost certification (G3): tracked in
  `knowledge_base/topics/ai_guardrails/gaps.md`; the orchestration paper *seeds* guardrail
  re-arming per model reentry but does not claim to address them.
- Standardized realtime-agent evaluation (G4): tracked in `ai_guardrails/gaps.md`; candidate
  future capstone paper (see `papers/_next_angles/angle_5_eval_stack.md`).
