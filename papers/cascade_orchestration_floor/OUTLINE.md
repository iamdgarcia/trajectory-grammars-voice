# Start Fast, Stop Fast: Interruptibility and the Cessation Floor of Realtime Cascade Agents — Outline

**Slug:** responsiveness_floors
**Template:** arxiv_preprint
**Target:** arXiv cs.AI (primary), cs.CL (cross-list)
**Status:** Stage 5 revision round complete; peer panel Major Revision, all nine mandatory revisions M1--M9 applied and certified **Accept** (reviews in `reviews/`).
**Compile gate CLOSED (2026-09-01):** local MiKTeX builds cleanly — **0 errors, 0 warnings, 29/29 citations resolved, 14 pages** → `main.pdf`.
**Citation gate CLOSED (2026-09-01):** all related-work metadata verified against the **arXiv API + Crossref**; a **2025--26 sweep** was run and its findings (Full-Duplex-Bench, FDB-v3 tool-use, IHBench post-interruption recovery, Easy Turn) are now integrated and differentiated in §2.7. Corrections applied: raux2012 title, bohus2011 (→ ``Decisions about Turns in Multiparty Conversation``, ICMI), baumann2012 (→ Interspeech prosodic-synthesis paper), ward2000 (→ Journal of Pragmatics backchannel paper), Agents-are-not-enough authors (→ Shah & White), TiLT dropped (its ``2502.19162`` id is a physics paper).
**Companion id CLOSED (2026-10-07):** `latencyfloor2025` now cites the live companion as `alphaXiv:2608.latency-floor-cascade-voice-agents` (year corrected 2025→2026, full title). No placeholders remain. Pipeline stage 6 (arXiv package) is ready.

## Thesis (hedged per review)

Perceived responsiveness in a cascade voice agent has two floors — response *onset* and response
*cessation* (how fast the agent fully stops when the user interrupts). Their constituents are set
by mostly different pipeline segments **under a fixed in-flight policy**, but the floors **share
the detection, buffer, and decode subsystems** — no honest claim of disjointness. The genuinely
new, defensible contribution lives at the *agent-orchestration* level: an interruptible agent that
cancels generation but persists background tool execution, with API-serializable commit of pending
tool batches, is the mechanism that lets a topology own both floors without losing work. Decoupled-
clocks (event-driven) scheduling is a **sufficient, idiomatic** realisation; serial graph
topologies can emulate it via async nodes / background dispatch / checkpoint reentry at
expressiveness cost — **a sufficiency claim, not an in-principle uniqueness claim**.

## Novelty positioning (honest, per review — ~40-50% as strong as first drafted)

- **Genuinely new spine:** tool-persistence under cancellation (generation-interruptible ∩
  execution-persistent) + the API-serializability lemma. Fresh at the *agent-orchestration* level;
  the SDS/UX literature never formalised this combination.
- **Closest formal ancestors — must be cited and differentiated FIRST (else re-brand risk):**
  incremental-processing **revocability** (schlangen2011 revocable increments; Baumann & Schlangen
  InproTK incremental TTS), Raux & Eskenazi endpointing/barge-in tradeoff, Bohus & Horvitz
  interruption-as-policy. They modelled *revocable output increments and stop/yield decisions*, not
  latency-floor arithmetic or agent tool semantics — that is our increment over them.
- **Framing: "nobody measures this" is false.** Industry (IVR / car-HMI / assistant UX) measures
  barge-in timing routinely. Correct claim: **no standardised definition and no formal floor exist**
  for agent response-cessation; measurement is ad hoc.
- **Stage-1 requirement:** fresh arXiv sweep (2025–2026) for voice-agent cessation/interruptibility
  work before writing §02 (space moves fast; no live web tool in this run — mandatory verification
  step).

## Relation to prior work (verified continuity)

From `papers/cascade_voice_latency/`: `thm:latency_floor`, `def:ccc` (Λ ≤ τ_human, 200 ms),
`thm:streaming_floor`, `thm:react`. Prior paper bounded **onset** and its §7 flags barge-in
reaction as open. **Explicit bridge:** our §06's *reactive* detect→cease floor and the prior
paper's *learned predictive stop* ceiling together define the intervention window — say it in §02.

## Contributions (lead = tool-safety spine; floors as framing)

1. **Interruptibility model (LEAD).** Generation-interruptible ∩ execution-persistent
   separation; interruption event algebra (detected / generation-cancelled / delivery-tail-flushed
   / tool-persisted / reentry); internal context about possibly-unheard responses.
2. **API-Serializability Lemma.** A pending tool-call batch must commit atomically with its result
   set; violation yields a provider-invalid sequence. This invariant is what makes
   *tool persistence under cancellation* safe — cancel-generation cannot strand pending calls.
3. **Cessation Floor (Thm 2, phase-conditioned).** detect / decide / cease / resume, split per
   interruption phase: (a) mid-generation = task-cancel, onset-adjacent; (b) mid-playback =
   delivery flush, bounded by audio in flight ≈ queue depth × frame (cascade tail grows with own
   output length; shorter filler = shorter tail); (c) mid-tool = nothing audible to stop, real
   metric is **resume** (re-prefill + reentry → re-enters the onset floor). Separates **can stop**
   (physics: in-flight granularity) from **should stop** (policy: engagement, per bohus2011).
4. **Two-floor dependency structure (Thm 1, hedged).** Under a fixed in-flight policy, onset and
   cessation constituents are set by mostly distinct segments; the floors **share** detection
   (EOU/VAD), buffer policy, and decode speed — optimisation on any shared component moves both.
5. **Tool-hiding coupling (Thm 3).** Onset floor includes Σ type-A λ_tool^irr under serial
   dispatch; background dispatch + reentry removes it (typed generalisation of thm:react).
   Tongue-in-cheek but real: phase (c) of Thm 2 and Thm 3 are the two windows where tools live.
6. **Filler hygiene (Corollary).** Filler masks onset from the delivery clock AND short manual
   filler shortens the interruption tail (classic barge-in-friendly device — a cessation win at an
   onset-quality price); generation-clock LLM filler must not be committed to the stream
   (prod-documented bleed).

## The practical question, answered formally (table repaired per review)

| Architecture | Onset | Cessation |
|---|---|---|
| Serial LangGraph | pays reducible serially | can cancel generation; checkpoint preserves state; **synchronous coupled loops drag tool-wait + delivery into the stop path** |
| + manual filler (delivery overlay) | masked at delivery | **shortens interruption tail (cessation win)** — the classic barge-in device |
| + LLM filler (generation clock) | masked but bleeds/duplicates (prod-documented) | no gain; corrupts stream |
| Event-driven (decoupled clocks) | hides reducible during speech | suffices to own both floors (cancel gen / persist tools / reenter); idiomatic, not unique |

Verdict: framework noise for single-hop turns; decisive for tool / long-duration / barge-in turns
(repo telemetry: tools ≈ ms in-memory, ~1 s real backend).

## PoC evidence — semantics verified + smoke anchor MEASURED (per review)

Artifact `C:\Users\U77225D\Desktop\code\iabto-ms-bc-orchestrator`. Existing tests verify the
*semantics* (interruption cancels model stream, never background tools; reentry per completed
batch; atomic pending-batch commit; interrupted delivery → internal context).

**Smoke anchor (added; done 2026-09-01):** `scripts/smoke_cessation.py` drives the *real*
organizer runtime with a scripted model, a delayed tool, and a simulated audible delivery clock
(configurable queue depth). Monotonic-clock medians over 5 runs (`python scripts/smoke_cessation.py`):

| Metric | Result | Claim anchored |
|---|---|---|
| cease, queue depth 1 | 109 ms | Thm 2: cease ≈ in-flight frame |
| cease, queue depth 6 | 609 ms | Thm 2: tail ≈ queue-depth × frame (linear in in-flight audio) |
| generation-stop, depth 1/6 | ~0 ms / ~0 ms | interrupt cancels generation promptly, independent of delivery tail |
| resume, tool ~0.01 s | ~0 ms | Thm 3/phase-c: in-memory tool → reentry only |
| resume, tool 1.0 s | ~1000 ms | Thm 3/phase-c: resume dominated by tool RTT + reentry |

Self-check asserts the three invariants (cease grows with depth; generation-stop < frame;
resume dominated by tool RTT) — all pass. Labelled an **anchor / feasibility instance, not a
benchmark** (no real ASR/TTS/LLM; synthetic latencies).

## Section structure

- **01 Introduction** — motivation (interruptibility is what users feel on tool-heavy turns); gap
  (no standardised definition + no formal floor for cessation — not "nobody measures"); thesis;
  contributions.
- **02 Background** — FIRST differentiate incremental revocability (schlangen2011; Baumann &
  Schlangen InproTK) and stop/yield policy (bohus2011; raux2008/2012); then endpointing, overlap
  structure & timing (schegloff2000, heldner2010), backchannel timing (ward2000), native
  full-duplex (defossez2024moshi, openai2024realtimeapi), turn-taking survey (skantze2021), tool
  loops & orchestration (yao2023react, langgraph2024, specrag2024, tilt2025, taubench2024). Bridge
  sentence: reactive floor (this) vs predictive ceiling (prior §7).
- **03 Framework** — two floors; three clocks (generation / delivery / tool); event algebra;
  interruption phases (gen / playback / tool-wait); type A/B/C tools; topology vocabulary.
- **04 Analysis** — Thm 1 (dependency structure), Thm 2 (phase-conditioned cessation + can/should),
  Thm 3 (tool-hiding), Lemma (serializability), Corollary (filler) + smoke-test anchor results.
- **05 The Practical Question** — repaired four-architecture table; when orchestration matters.
- **06 Open Problems** — standardised cessation/perceived-V2V measurement protocol (OG5);
  guardrail re-arm per reentry (bridges ai_guardrails G1/G3); forgetting floor / context compaction
  (long sessions); learned turn-end prediction (intervention window with the reactive floor).
- **07 Discussion** — limitations (conceptual + PoC semantics + small smoke anchor; no benchmark
  campaign; unverified citations gated), relation to v2v_server telemetry vocabulary.
- **08 Conclusion** — responsiveness is two floors; interruptibility is the agent-level mechanism;
  CCC applies inside the stage.

## Theorems (working statements, hedged)

- **Thm 1 (Floor-constituent dependency).** Under a fixed in-flight policy (queue depth, decode
  speed), onset vs cessation constituents are set by mostly distinct segments; shared components
  (detection, buffer policy, decode speed) move both.
- **Thm 2 (Phase-conditioned cessation).** Reaction ≥ detect^irr + decide + cease + resume^(phase);
  phase-(b) cease is bounded by audio in flight ≈ queue depth × frame and grows with agent output
  length; phase-(c) reduces cessation to resume, which re-enters the onset floor; can-stop
  (physics) vs should-stop (policy) are separated.
- **Thm 3 (Tool-hiding coupling).** Serial dispatch adds Σ type-A λ_tool^irr to onset; background
  dispatch + reentry removes it (typed generalisation of thm:react).
- **Lemma (API serializability).** A pending tool-call batch commits atomically with its results;
  violation yields a provider-invalid sequence; prerequisite for safe tool persistence.
- **Corollary (Filler).** Filler is an onset mask from the delivery clock; short manual filler also
  shortens the interruption tail; generation-clock filler must not be committed.

## TikZ figures

- `fig_two_floors` — onset vs cessation floors vs turn timeline (with shared components marked).
- `fig_interruption_phases` — gen / playback / tool-wait phases and the react/resume paths.
- `fig_event_loop` — event algebra + reentry transitions.
- `fig_tool_hiding` — type A/B/C vs the onset floor.
- `fig_four_architectures` — repaired topology table.

## KB status (updated)

- `knowledge_base/topics/orchestration/` populated (24 entries). **Citation gating enforced:** do
  NOT cite until verified — raux2012optimizing, bohus2011interruptions, heldner2010gaps,
  schegloff2000overlap, ward2000backchannel, tilt2025, specrag2024, agentsnotenough2024,
  packer2023memgpt. To-add: Baumann & Schlangen InproTK / incremental-TTS revocability entry.
- `gaps.md`: OG1 demoted (Open Problems); **OG2 selected as paper lead**; OG3/OG4 folded in;
  OG5 recorded as companion.
- **Stage-1 gate before §02:** fresh arXiv 2025–2026 sweep for voice-agent cessation /
  interruptibility; verify the 9 [VERIFY] entries; add Baumann & Schlangen entry.
