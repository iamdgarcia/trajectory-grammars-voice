# Night scan — alphaxiv knowledge expansion (2026-10-13/14, 6 discovery rounds)

*Orchestrator night session: systematic exploration beyond the immediate paper needs. Purpose:
fund the NEXT research decisions, not to generate artifacts. Organized by line; every entry = what
it changes for us. Each scan round was targeted at one of the factory's active lines.*

## Round A — Outcome prediction from partial conversations (CD1/CD2 neighbors)

- **TRACER proper** (2607.03974) — confirmed the method detail: early failure detection with
  process-level signals, evaluated post hoc. Our stopping-layer remains the differentiator (CD2).
- **Speech-Act Derailment Forecasting** (2608.25359, Melbourne) — speech acts for LOW-DATA
  derailment forecasting. *Useful:* our Spanish hard-cut finding (text near-chance) + speech-act
  conditioning = a low-data recipe compatible with our few-shot constraint. Bookmark for CD3 method.
- **Preference Tree Optimization** (2608.12062) — look-ahead simulations for goal-oriented dialogue.
  *Useful:* simulator-in-the-loop strategy search = our simulator line's second consumer (after
  coverage): the simulator doesn't just evaluate, it can TRAIN (connects SPADE below).
- **From Task Success to Productive Success** (2609.21117, Northeastern) — quality AND cost as
  co-equal axes for human-AI collaboration. *Useful:* citation ammunition for our cost-weighted
  detection-latency metrics (CD4) — validates the PARADISE-style cost axis in the LLM era.
- **Runtime Monitoring against Error Propagation** (2606.29026) — multi-agent trace exchange +
  revision. *Useful:* cites for the intervention-coupling section (§6 of grammar paper).

## Round B — The evaluation-coverage neighborhood (trace2trajectory's competitors/kin)

- **Mining Workflow Graphs for Black-Box Boundary Testing** (2607.06873, Limerick/CUHK-SZ) — ★ the
  closest competitor found tonight: mines workflow graphs from conversations to test state-dependent
  failures. Difference: (a) graph mining ≠ formal grammar with outcome classes; (b) black-box testing
  ≠ region coverage; (c) no observability-format ingestion. MUST cite + contrast in the paper.
- **SimVerity** (2608.25067) — when does simulated success survive physical deployment? ★ second
  closest: sim2real validity quantification for agents. Text/embodied, not conversation-trajectory.
  *Useful:* their validity quantification framing strengthens our coverage-as-evidence argument.
- **SSCBench** (2610.11514) — evidential validity of fault-injection tests for tool agents. Our
  world-faults (timeout/slow/error) get an evidential-quality standard to cite.
- **What Process Evaluation Actually Measures** (2608.22960, Amap/Nanjing) — action/task/step are
  THREE levels. ★ Useful: our grammar operates at "step" level (state transitions); this paper gives
  the vocabulary to say precisely which level we cover and prevents the "you only measure X" review.
- **Chunk Coverage for RAG Testing** (2607.18155) — coverage as a testing primitive exists in RAG
  land. *Useful:* precedent for "coverage of test-space" as a publishable metric in adjacent domain.
- **Load-Bearing Evidence** (2607.12469) — evaluation results as evidence with reconstructability
  metric. *Useful:* philosophy-of-measurement citation for the coverage paper's claims.

## Round C — Semantic EOT / endpointing (SV-line refresh; 5 nuggets)

- **TurnFSM** (2609.04240, Tsinghua/Huawei) — state-machine logic internalized for streaming semantic
  VAD + utterance rejection. ★★: a DISCRETE FSM inside the EOT model — the acoustic twin of our
  conversation grammar. Cite in grammar paper §2 and in any future "hierarchical state machines for
  voice agents" angle.
- **Next-Turn EPD** (2606.18094, Huawei) — endpointing as TIME-TO-NEXT-SPEECH-ONSET prediction.
  *Useful:* reframes endpointing from classification to forecasting — connects to our latency-floor
  framing (forecasting the gap IS predicting the Lambda* budget).
- **Label-Trade-off** (2609.04225) — causal supervision for turn-aware streaming ASR; the labels
  were the problem. *Useful:* methodology citation for our ES hard-cut benchmark construction.
- **Semantic Uncertainty for Transition Relevance** (2609.10934, Tufts) — uncertainty as the
  turn-taking signal. *Useful:* connects SPRT stopping (CD2) to the acoustic layer via uncertainty
  estimation — a unification hook we should not lose.
- **TamilEOT/BanglaTurn** (2609.05631/2609.29371) — EOT benchmarks spreading to low-resource
  telephone speech. *Useful:* evidence the EOT-benchmark space is filling — our Spanish position
  must cite these as the multilingual trend (SV2 gap is closing from outside).

## Round D — Speculative execution (the orchestrator-paper's acceleration field)

A WHOLE SUBFIELD formed in the last 90 days:
- **Hiding Tool Latency in On-Device Cascaded Voice Agent through Speculative Execution**
  (2610.07641, Qualcomm/KAIST, Oct 6) — ★★★ THE neighbor for the orchestrator work: cascaded voice
  agent + speculative tool execution. Must read in full; our event-driven runtime = the generic
  runtime version of what they do per-voice-component. Directly citeable; also validates the lane.
- **Speculative Programmatic Tool Calling** (190 votes) — pre-launch tool calls from partial REPL
  code. *Useful:* the harness-level analogue of our background dispatcher.
- **TomasuLLM** (2609.38201) — out-of-order speculative execution for long-running tools.
- **AOSpec** (2608.00881, Imperial) — action+observation co-speculation for agent serving.
- **Speculate While You Reason** (2607.25816, UCSB/LinkedIn) — RL-trained speculator predicts next
  tool call. *Useful:* the LEARNED version of our rule-based dispatcher policy.
- **Simulate to Generalize** (2607.16900, Apple) — LLM world models generate stateful supervision.
  *Useful:* bridge between simulator line and training-data line (our simulator's third consumer).
- **AgentSpec / AsymSpec / DynBranch / SpecBox / SchemaFill / Macro Commit / LEAP** — the serving-side
  wave (batch speculation, context-asymmetric decoding, branch reuse, sandbox scheduling).
  *Verdict:* our orchestrator paper must cite the speculative-execution wave as RELATED SYSTEMS WORK
  and position the event loop as the RUNTIME CONTRACT that these optimizations plug into (they
  speculate WHAT to launch; we define WHEN launching is legal). That's a strong, honest position.

## Round E — Self-play / synthetic data (simulator line's supply side)

- **SPADE** (2608.19197, UW/Stanford/MIT/CMU, 199 votes) — self-play in ADAPTIVE synthetic
  executable environments; ever-expanding goal pools. ★★ the training-side twin of our coverage
  idea: adaptive environments expand WHERE you train; coverage measures WHERE you haven't. Natural
  composition: our uncovered regions = SPADE's goal-generation prompt.
- **Autodata** (2606.25996, Meta, 481 votes, 7.7k views) — agents as data scientists building
  training/eval data. *Useful:* the "who builds the scenarios" answer for the simulator at scale.
- **EDGEGEN** (2609.24115, SAP) — synthetic edge-case generation BEYOND happy paths for tool agents.
  ★ direct precedent for our uncovered-region -> edge-case pipeline; must cite.
- **SynAE** (2605.22564, CMU/MSR) — quality measurement for synthetic tool-calling eval data.
  *Useful:* their quality axes = checklist for our simulator's output validity.
- **VISTA** (2606.11079, Columbia) — interactive user-simulation toolkit. Competitor for the
  simulator-repo positioning; text-only, no coverage/atlas.

## Round F — Latent-space navigation / atlas method (the visualization layer)

- **EviMap** (2609.06664, Hannover/Darmstadt) — evidence-grounded hierarchical topic maps for
  UNLABELED corpora. ★ method neighbor for the atlas (hierarchical structure + evidence grounding).
- **Semantic Steering of Embedding Projections** (2605.01957) — analyst-intent-aware projection.
  *Useful:* our (cycle_depth, duration) plane is one deterministic projection; this paper shows how
  to make projections answer specific analyst questions — future work hook.
- **Topic Drift at comment level** (2608.19133) — embedding-based drift detection in massive corpus.
  *Useful:* drift-detection machinery for the atlas (drift over TIME, not just over regions).
- **Shared Global and Local Geometry** (2503.21073, Harvard/DeepMind, 72 votes) + **Representation
  Manifolds** (2505.18235, 42 votes) + **Linear structure of VL embeddings** (2504.11695, 84 votes)
  — the geometry foundation layer: cross-model geometric similarity is REAL and measurable.
  *Useful:* legitimizes comparing real-log embeddings vs simulator embeddings from a different model.
- **Characterizing Human Semantic Navigation as Trajectories** (2602.05971) — humans traverse
  embedding space as trajectories. *Useful:* the conversation-as-trajectory-in-embedding-space
  framing has a cognitive-science anchor; cite in the atlas method section.

## Synthesis: what the night changed

1. **The orchestrator/paper positioning is STRONGER than believed**: speculative-execution is a hot
   subfield (7 papers/90 days) but all are SERVING-LAYER optimizations; the runtime-contract
   position (when is launching tools legal/safe) is ours to claim. Read 2610.07641 in full next.
2. **trace2trajectory has ONE close competitor to contrast**: 2607.06873 (workflow-graph mining for
   boundary testing). The contrast paragraph is already writable: formal grammar + outcome classes +
   coverage metric + standard-format ingestion vs heuristic graphs + boundary cases + ad-hoc parsing.
3. **The simulator line gained a second consumer** (training: look-ahead + SPADE + EDGEGEN) and a
   quality checklist (SynAE). Coverage -> generate tests -> adaptive environments is now a closed loop
   with published precedents at each step.
4. **The atlas method section has real anchors** now (EviMap, semantic steering, drift machinery,
   shared-geometry results). The "conversation as trajectory in embedding space" framing gets a
   cognitive-science citation (2602.05971).
5. **New unread pile (priority order)**: 2610.07641 (full read), 2608.23670 (automata method detail),
   2605.07847 (their metric machinery), 2607.06873 (competitor contrast), 2610.02460 (CUE).

*No artifacts generated beyond this file — per the consumption directive, this scan FUNDS decisions
(it sharpens two papers' positioning and found the competitor to contrast), it does not spawn builds.*
