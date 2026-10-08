# Research: Realtime Tool Use & Multi-Step Orchestration Latency for Voice Agents

_Discovery brief scoping the next paper after "The Latency Floor of Cascade Voice Agents" (slug: cascade_voice_latency)._
_NOTE ON METHOD: this session had no `web_search` tool provisioned (only read/write). Findings are synthesized from the published paper's formal machinery (read: sections/03–06, main.bib) plus field literature with confidence-tagged arXiv IDs. All IDs below marked [high]/[med] MUST be re-verified against arXiv before the KB entry or paper cites them._

## 1) LANDSCAPE

1. **Serial tool-calling agents** — Toolformer / Gorilla / OpenAI function-calling establish "reason -> call -> observe" loops; the wall-clock cost shape (k·λ_lm + k·λ_tool) is acknowledged in every empirical paper but never formalized. (arXiv:2210.03629 ReAct [high]; arXiv:2305.15334 Gorilla [high])
2. **Speculative / parallel tool & retrieval execution** — Speculative RAG and OpenAI parallel function-calling hide one tool RTT under drafting or generation; each is a single overlap *trick* with no composition rule for how many/which tools can be hidden. (arXiv:2407.08223 [high])
3. **Streaming / speculative LLM inference** — Speculative decoding, RadixAttention (SGLang): shrink the *reducible* decode term λ_lm^r; indifferent to tool-gated time-to-first-token (TTFT), which is exactly where tool RTT lands. (arXiv:2211.17192 [high], arXiv:2312.07104 [high])
4. **Realtime voice-agent frameworks** — OpenAI Realtime API + function calling, Gemini Live, LiveKit/Pipecat, Apple AURORA, Amazon "agentic server actions": production practice does prefetching, filler audio, and parallel dispatch *today*, but none of it is documented as a latency budget, let alone proven optimal. (AURORA arXiv:2509.21137 [med])
5. **Perceived latency & turn-taking** — Levinson & Torreira's ~200 ms modal inter-turn gap, incremental dialogue processing (Schlangen & Skantze), fillers and barge-in: the psychology of the gap, never extended to "how much tool RTT fits inside the perceived floor." (in paper's bib; no arXiv id)
6. **Orchestration graphs / multi-agent flows** — ReAct, AutoGen, LangGraph, "LLM as a compiler," Model Context Protocol: expressive scheduling of tool DAGs but latency is runtime *telemetry*, never a theorem; no provider states a schedulability condition. (arXiv:2308.08155 [high], arXiv:2406.16756 [med])
7. **Streaming RAG / tools-in-transcription pipelines** — TiLT (tools dispatched from a live transcription stream before EOU) and SpokenRAG: empirically overlap tool I/O with the speech stream; one trick each, no unifying model that nests token-hiding *and* IO-hiding under one budget. (arXiv:2502.19162 [med], arXiv:2411.03088 SpokenRAG [med])
8. **Efficiency-aware agent evaluation** — τ-bench (explicit latency+price axes), PerfEval, OmniFlutter (voice-native interaction): good metrics; none predicts a turn's latency from tool-DAG *structure*, so benchmarks can't separate architecture from implementation. (arXiv:2406.12045 τ-bench [high], arXiv:2505.05623 OmniFlutter [med])

## 2) THE GAP

**Testable research question:** For a cascade voice agent that must execute a set of `t` tool calls inside one turn, under a perceptual budget `τ ≈ 200–500 ms` with streaming TTS available, what is the exact composition rule that decides whether the tool-induced latency — formally `δ = Σ_t λ_tool − (hideable overlap window W)` — is schedulable inside the budget, and which per-tool properties (output-gates-first-audio vs. deferrable; parallelizable; speculatable) *provably* determine schedulability?

Why it is not already solved:
- The **ReAct/orchestration literature** (clusters 1, 6) treats tool RTT as an engineering annoyance: papers report "extra seconds per loop," frameworks add parallelism, and nobody states the irreducible wall-clock form. Our own §5 (Theorem thm:react) already exposes the shape — `Λ_k* = λ_asr^irr + k·λ_lm^irr + (k−1)·λ_tool^irr + λ_tts^irr` — and then **stops**: parallel dispatch is filed as "reduces reducible components only," leaving `λ_tool^irr` unformalized at the level of "it's positive for remote APIs."
- The **overlap literature** (clusters 2, 7) demonstrates that tool I/O *can* be hidden under generation (Speculative RAG), under drafting, or under the live transcription stream (TiLT) — empirical existence proofs of a hideability window `W`, with no theorem stating *when* hiding is possible, how large `W` is, or what happens when `Σ λ_tool^irr > W` (which is the regime real voice assistants actually live in).
- **Voice frameworks** (cluster 4) hide tool latency with filler audio and prefetching as undocumented heuristics; the perceptual floor (cluster 5) is never connected to a tool RTT budget.
- Net: three literatures each hold one piece (irreducible sum, hideable window, perceptual threshold). Nobody has composed them into a single schedulability/budget statement — precisely the gap our DAG/Latency-Floor machinery is built to close. It is a *formal* gap (a missing theorem), not just a missing empirical result, so it is defensible against "practitioners already ship this."

## 3) CANDIDATE CONTRIBUTION

**The Tool-Integrated Latency Budget (TILB) theorem + ToolGap-1 benchmark.** Concretely publishable pieces:

1. **Formal extension of the decomposition** — extend `λ = λ^r + λ^irr` to tool nodes: define `λ_tool^irr` as the *network-round-trip floor* (physical RTT + server TFN, not reducible by local optimization) and give a per-tool hideability type: **A** = output required before any response audio token (gates first token; RTT lands in the silence gap), **B** = output deferrable past filler/lead-in tokens (hideable under streaming-TTS lead `W`), **C** = background (result needed only for a later turn / can be blended in).
2. **Generalized floor over branched-serial tool DAGs** — a theorem replacing the linear `(k−1)·λ_tool` sum with critical-path form over the *tool DAG* (which tool edges are on the critical path after parallel split) plus `Σ_{type A} λ_tool^irr` as unhideable surplus. States a **schedulability condition** (CCC-with-tools): the turn satisfies the Cascade Competitiveness Criterion `Λ ≤ τ` *iff* `Λ_floor^streaming + Σ_{type A} λ_tool^irr ≤ τ − overhead(W)`.
3. **Tool-Parity lemma** — a formal version of our §6 filler + barge-in levers as *budget transformations*: filler/speculative audio converts a type-A tool's unhideable RTT into prosody-capped but perceptually-bounded audio, trading a bounded prosody/quality cost for silence-gap compliance; gives the first formal basis for why "one moment" + parallel dispatch is the right engineering move and when it breaks (when `Σ type-A RTT` exceeds `τ` and audio-hold becomes perceptible).
4. **ToolGap-1 benchmark** — synthetic tool RTT distributions × orchestration policies (serial, parallel-split, speculative-auth-prefetch, filler-hold) measured on end-of-speech↔first-audio-token and *perceived* silence, validating the theorem numerically and giving reviewers something to run.

**Working title:** "Hiding the Tool Round-Trip: A Latency-Budget Model for Realtime Orchestrated Voice Agents."

## 4) EXTENSION ANGLE

This is a **direct generalization of two results already published** in papers/cascade_voice_latency, so the next paper visibly builds on the last one:

- **Generalizes Theorem thm:react (§5, the k-step silence gap).** The published linear chain `ASR → [LM₁→Tool₁→…→LMₖ] → LMₖ → TTS` becomes the special case of the new *branched, typed* tool DAG when every tool is type-A and nothing runs in parallel. The new critical-path floor with type-classification collapses to `Λ_k*` exactly when all tools are type-A serial — giving a "our 2025 result = special case" theorem statement reviewers will recognize.
- **Reuses the whole machinery:** reducible/irreducible decomposition, the Cascade Competitiveness Criterion `Λ ≤ τ_human`, the streaming-cascade floor of Theorem thm:streaming_floor (the hideable window `W` for tool overlap is the exact analog of `|C_pre|` prefill-hiding during speech), and §6's streaming-TTS / parallel-execution / filler levers reinterpreted as budget transformations rather than heuristics.
- **Feeds the safety KB gap (G1, streaming-safe guardrails).** In a tool-streaming turn, tool results arrive mid-stream and need prefix-safe validation at the same 200 ms scale. The TILB budget assigns the guardrail a *fixed per-tool-result latency allowance* inside `W` — turning KB gap G1 ("no streaming-safe guardrail framework") into a schedulable sub-problem of the same theorem, and cross-fertilizing the paper with the ai_guardrails KB (gaps G1/G3).

## 5) ANCHORS (must-cite, confidence-tagged — verify IDs)

1. **ReAct: Synergizing Reasoning and Acting in Language Models** — arXiv:2210.03629 [high]. The exact loop our §5 extends; the k-step tool trajectory is the object being budgeted.
2. **Fast Inference from Transformers via Speculative Decoding** (Leviathan et al.) — arXiv:2211.17192 [high]. Canonical reducible-decode speed-up; sets the ceiling on λ_lm^r and the draft-model pattern we borrow for speculative tool/auth prefetch.
3. **Gorilla: Large Language Model Connected with Massive APIs** — arXiv:2305.15334 [high]. Establishes function-call *generation as a first-class output*, i.e., the point where the DAG leaves the LM and hits network RTT.
4. **Agents Are Not Enough** (Instagram/Meta GenAI) — arXiv:2412.16241 [med]. Shows answering from prefetched intent can skip the tool entirely; empirical precedent for the type-B/C "hideable" classification and why hiding must be formal (privacy/accuracy tradeoff).
5. **Speculative RAG: An Optimized RAG with Speculative Decoding** — arXiv:2407.08223 [high]. Direct evidence that retrieval RTT can be overlapped with drafting = a concrete instance of our hideability window `W`.
6. **TiLT: Tools in Live Transcription** — arXiv:2502.19162 [med]. Pipelining tool execution off a live transcription stream *before EOU*; the closest empirical sibling to a type-A→B reclassification and the EOU-to-tool-dispatch latency analog of our δ_N.
7. **τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains** (Sierra) — arXiv:2406.12045 [high]. The dominant tool-agent benchmark with explicit latency+price axes; the natural evaluation baseline ToolGap-1 extends.
8. **Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations** — arXiv:2312.06674 [high]. The synchronous, full-response guardrail whose per-tool-result latency cost our budget must schedule — ties the paper to KB gap G1 (streaming-safe guardrails).

## (method note, not a section body)
Live web verification could not be run this session (no `web_search` tool). Confidence labels [high]/[med] reflect recall strength only; all eight IDs above, plus clusters 4–8 company/framework claims, should get a verification pass before the KB entry (knowledge_base/topics/<new topic or ai_guardrails>/papers/tool_latency_budget.md) and any \cite{} land in a paper.
