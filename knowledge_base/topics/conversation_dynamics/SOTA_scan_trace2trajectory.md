# Research brief — From traces to trajectories: SOTA scan (alphaxiv, 2026-10-13)

*Method: 4 `discover_papers` rounds (agent-trace viz/analysis, user-sim fidelity, dialogue-flow viz,
process mining on event logs) + representation-geometry control scan. Verdicts by orchestrator.*

## The five neighbors that define the gap

| Paper | What it does | What it does NOT do (our opening) |
|---|---|---|
| **Automata from Agent Traces** (2608.23670, Holistic AI/PUC-Rio/UCL, 31 votes) | Mines automata from unstructured agent traces for failure/next-step prediction | No conversation semantics (no dialogue states), no voice channels, no visualization-atlas claim |
| **Graph of Trace** (2606.15116, Tsinghua/RUC/Georgia Tech) | Visualizes scientific-agent execution traces as graphs | Domain = scientific workflows; design-time graph, not distributional atlas; no outcome classes |
| **TraceDance** (2609.33295, ByteDance/UIC, 35 votes) | Builds behavior benchmarks from real deployment traces | Benchmarks behavior, does not recover a state space nor visualize collections |
| **TRACER-Traj** (2609.28690, PKU/Kuaishou) | Trajectory-aligned learning FOR user simulation | Sim side only; trajectory = training signal, not an extraction/analysis target |
| **WildVis** (2409.03753) | Million-scale chat-log visualization (UMAP over chats) | Static corpora, chat only: no agent/tool spans, no outcome classes, no grammar |

**Critical confirmation:** the 2026 wave mines traces for *prediction* (automata, attribution,
fault graphs — 2608.06909 Huawei, 2608.24361 AWS, 2609.32514 Tsinghua) and *benchmarks* (TraceDance,
Agentic CLEAR, AutoSaddler), but **nobody publishes a mapping from standard observability exports
(OTel GenAI / OpenInference / LangSmith) to a discrete conversation state space with outcome
classes**, and **nobody projects trace collections into a shared atlas where sim and real clouds
are compared by region**. Viz prior art remains design-time (LangGraph Studio) or corpus-level
(WildVis). Gap (a),(b),(c) from the earlier brief survives this scan intact.

## The user-simulation wave changes the paper's second half

2026 produced a calibrated-simulation lineage we must build on, not duplicate:

- **Mind the Sim2Real Gap** (2603.11245, CMU, 35 votes, 956 views) — sim2real gap for agentic tasks; user-proxy quality question.
- **Measuring and Mitigating the Distributional Gap** (2605.07847, UIUC/MSR/Berkeley, 28 votes) — **distributional** alignment of real vs simulated user behavior. Closest to a6's RQ; text-only, no conversation-grammar atlas, no voice axis.
- **Synthetic Users, Real Differences** (2605.02624, JHU/Berkeley) — evaluation framework for user simulators in multi-turn settings.
- **RealUserSim** (2605.20204, Salesforce) — Formalism Ceiling: unconstrained LLM users fail as proxies.
- **CUEing User Simulators** (2610.02460, Oct 2026) — **calibrated user embeddings** for benchmarking → direct precedent for embedding-conditioned simulation (our latent atlas feeds this).
- **MirrorBench** (2601.08118) / **Disclosure-Gated** (2609.00982) / **Back in Style** (2610.10988) — human-likeness, over-cooperativeness, persona fidelity: the failure axes a calibrated simulator must not exhibit.

**Implication:** the simulator paper (a6) is no longer "nobody measures sim2real of conversation
metrics" — 2605.07847 does, text-only. Our differentiated claim becomes: **sim2real transfer of
trajectory-level structure (grammar walks, cycle depth, outcome classes, voice-physics channels),
not just response distributions** — and the atlas is the vehicle nobody has.

## Voice-agent dynamics: crowded outcome space, empty trajectory space

TurnBench (2608.25218), MP-Bench (2609.13076), Dyadic (2610.08125), CDS distributional metrics
(2609.31719, KTH — same group as 2605.07847 family), People-Make-Conversation (2610.12802), Voice-Light
(2609.20995): all evaluate turn-taking *behavior* aggregate or outcome-level. None extract a state
space walk per conversation. **CDS (2609.31719) is the metric-side neighbor for our atlas validation**
(distribution comparison machinery exists — we apply it to grammar walks, not response text).

## Representation-geometry adjacent (for the atlas method section)

- **Layers at Similar Depths** (2504.08775, 81 votes): cross-model nearest-neighbor convergence — legitimizes cross-model/cross-vendor latent comparisons (real logs vs sim from different models).
- **Trajectory Geometry of Transformer Representations** (2606.09287): diff-geometry over representation paths — methodological vocabulary for "conversation as trajectory object".
- **Truth as a Trajectory** (2603.01326): internal-reasoning trajectories; conversation-scale analogue unclaimed.

## Consolidated gap statement (paper-ready)

> Production agents emit traces in standard formats (OTel GenAI, OpenInference, LangSmith), yet no
> published method maps those traces to a machine-level conversation state space with typed
> transitions and terminal outcome classes — nor visualizes conversation collections as a
> distributional atlas where synthetic and real populations can be compared by region. We
> contribute the formal extraction mapping and the trajectory atlas. The headline evaluation is
> **region coverage**: given real-conversation embeddings, which regions of conversational
> behavior does a simulator (or a new agent version) cover, and which are uncovered — the
> measurable answer to "what are we NOT testing". Sim2real transfer is quantified as coverage +
> Wasserstein divergence of grammar-walk statistics (CDS-style), with rank correlation of policy
> scores as the transfer headline. Voice-physics channels are an OPTIONAL extension (appendix),
> not the central claim.

## Citation pack (new, verified arXiv ids)

Core: 2608.23670 (automata-from-traces) · 2606.15116 (Graph of Trace) · 2609.33295 (TraceDance) ·
2609.28690 (TRACER-Traj) · 2409.03753 (WildVis) · 2605.07847 (distributional gap) · 2603.11245
(sim2real agentic) · 2610.02460 (CUE embeddings) · 2605.20204 (RealUserSim) · 2609.31719 (CDS) ·
2608.25218 (TurnBench) · 2504.08775 (layer convergence) · 2606.09287 (trajectory geometry).
Existing KB anchors: sierra2024taubench, nourbakhsh2026tracer, salesforce2025workflows, x2turn2026.
