# Research: Event-Driven Orchestration for Voice Agents — framework integration map (FINAL)

**Date:** 2026-10-14 · **Feeds:** paper "The orchestration runtime contract: event-driven structure for cascade voice agents, instantiated on existing frameworks" + conformance kit for github.com/iamdgarcia/event-driven-voice-orchestrator.

**Evidence classes used (nothing else):**
- **[V-local]** verified against local files: FINDINGS_event_driven_orchestration.md (G=(Q,Σ,δ), P1–P7, 32/32 bench invariants), event-driven-voice-orchestrator README + integrations/README.md (pipecat bridge, ALL CHECKS PASSED), cascade_orchestration_floor/OUTLINE.md, orchestration/gaps.md.
- **[V-orch]** verified live by the orchestrator via alphaxiv full-text today (2610.07641 claims + neighbors + EarlyEval datasets).
- **[U-doc]** unverified, needs a docs-with-version fetch — one targeted fetch per cell, listed in §6. No other claim in this brief lacks a tag.

---

## 1. Framework capability matrix vs the four contract properties

Contract properties (from the runtime's own definitions): **(a)** background/parallel tool execution during generation (execution-persistent dispatch); **(b)** non-stalling user turns (turn events applied while tools pending); **(c)** independent generation/delivery lifecycles (barge-in cancels generation only); **(d)** serializable/committable tool batches (API-Serializability Lemma: batch commits atomically with results).

| Framework | (a) bg tools | (b) non-stall turns | (c) gen/delivery split | (d) batch commit | Gap vs contract |
|---|---|---|---|---|---|
| **pipecat** [U-doc for current APIs] | partial — dispatch is user code in frame processors; no runtime-owned dispatcher | partial — frames flow regardless | **yes natively** (InterruptionFrame, BotStarted/StoppedSpeakingFrame) but no persistent state machine over them | no — context aggregator appends what you push | State machine missing. **Our bridge already fills it** [V-local]; the showcase cell |
| **LiveKit Agents** [U-doc] | yes-shaped — `function_tool` tools run as tasks while agent continues | partial — `UserStateChanged`/input events exist; whether a turn is processed while a tool blocks is undocumented | yes-shaped — playback/interruption events + `allow_interruptions` | no visible batch-commit primitive | (d) is the gap; (b) semantics undocumented. **Instantiate here** |
| **LangGraph** [U-doc] | no at graph level — nodes serialize; `async` nodes + `Send` API give *manual* parallelism | no — a user turn must be a new graph invocation; nothing arrives mid-graph | no delivery-clock concept (text-first) | checkpoint/reentry exists, but atomic tool-batch commit is not an API invariant | Weakest fit by design — the paper's **fair serial-graph baseline**, not an integration target |
| **AutoGen/AG2** [U-doc] | no — group chat / sequential turns | no | no | no | Not voice, no transport clock — one related-work paragraph |
| **CrewAI** [U-doc] | no — sequential task pipeline | no | no | no | Same as AutoGen; skip |
| **OpenAI Agents SDK** [U-doc] | yes-shaped — background/parallel function tools documented (checked in prior session research) | partial — SDK loop is reply-centric | no delivery clock (text/transport-agnostic) | tool-call/result pairs SDK-handled; commit-on-partial is user code | Closest text-side match for (a); (c)+(d) are the adapter's job. **Instantiate here** |
| **smolagents** [U-doc] | partial — async CodeAgent | no | no | no | Not voice; skip in paper, one sentence |
| **Vercel AI SDK** [U-doc] | partial — streamText tool streaming + client callbacks | no server-side concept | delivery is the UI's job | no | Client-rendering layer; cite as "delivery clock exists only client-side" |
| **Voice event-bus layers (TEN-framework, Retell/Vapi-style)** [U-doc — **highest priority**] | event-bus architectures claim event-driven | often yes for audio frames | partial — but tool state + conversation state usually merged in one session object | no | TEN-framework is the closest neighbor and the "industry already did this" objection — must be read and differentiated before the novelty claim is written |

**The pattern (paper's spine):** every framework has *fragments* — LiveKit has playback events, OpenAI SDK has background tools, LangGraph has checkpoint/reentry, pipecat has the delivery clock — but none exposes all four as first-class, tested runtime semantics. The runtime does (32/32 invariants, P1–P7 [V-local]). Claim: the four properties are one package — three without (d) loses API-validity under cancellation, (d) without (a) loses tool hiding (Thm 3), (a)–(d) without (c) loses barge-in correctness. No framework publishes these as testable invariants + a conformance kit.

## 2. Integration pattern: adapter-per-framework + 5-port SPI

- **Right pattern, already validated** [V-local]: `EventDrivenOrchestratorBridge` (pipecat `FrameProcessor`, transport-only — owns neither scheduling nor state) maps framework events → the 5-event alphabet Σ (`UserTextReceived`, `ToolCallFinished`, `OutputDelivery{Started,Completed,Interrupted}`). The five ports in `domain/ports.py` (`ModelPort`, `ToolRegistryPort`, `OutputPort`, `ConversationRepositoryPort`, dispatcher state) are the contract's SPI. Adapter cost ≈ 100–200 lines/framework; embedding the runtime *inside* a framework loop would mean forking its scheduler.
- **Conformance kit = the port-level harness:** scripted model + scripted tools + the 5 ports, run the existing invariant suite (`bench/bench_turn_latency.py` assertions + P1–P7) against (i) core runtime, (ii) each adapter. Pass = invariants hold *through* the adapter. Cheap (stdlib, exists in embryo) — this is the repo-side deliverable of the paper.
- **Prior art for runtime-contract/conformance kits in agent frameworks:** none found in local KB; nearest analogues are OpenTelemetry GenAI semantic conventions (conformance-by-spec for *telemetry*, verified in trace2trajectory brief) and MCP's spec+conformance model (protocol, not runtime scheduling). Framing: "what OTel did for trace semantics, this does for voice-agent turn semantics." Live sweep for competing claims still required (Stage-1 gate) [U-doc].

## 3. Literature positioning (2610.07641 now VERIFIED)

- **2610.07641 (Qualcomm/KAIST) [V-orch] — closest neighbor, delta is clean and honest:**
  - They: **speculative tool execution during streaming ASR** — a **scheduling strategy**, on a proprietary Android stack (Galaxy S26, QNN NPU, Llama3.2-3B); metric TTFA 5.79s→4.60s.
  - Explicitly absent from their work: **no barge-in handling, no user-turn-during-pending-tools, no framework instantiation, no state contract.**
  - Speculation is **restricted to read-only tools** with a "wasted calls" metric — i.e., they accept waste to hide latency; we dispatch only called tools and **persist execution under cancellation** (no speculation, no waste, but correctness under barge-in). Different semantics, complementary.
  - Our delta (paper §2 wording): strategy vs **runtime contract** (event algebra + state invariants + conformance kit); TTFA-only vs **both floors** (onset + cessation, companion paper); proprietary hardware demo vs **open-source framework instantiation** (pipecat shipped, LiveKit planned). They do NOT block us; they are the must-cite-first neighbor.
- **Cite-worthy precursors from their reference list [V-orch as names, U-doc for content]:** StreamRAG (streaming tool usage), LLM-Compiler (parallel function calling, ICML), Asynchronous LLM function calling (arXiv 2402). All operate at the LLM-decoding/scheduling level, not voice-runtime level — one paragraph each in §2.
- **EarlyEval 2609.02783 [V-orch]:** datasets are SWE-bench Verified / TerminalBench / Toolathlon — coding agents, **not dialogue**. Useful only to show parallel-tool evaluation lives elsewhere; no dialogue-level competitor.
- **Incremental-processing revocability (schlangen2011, InproTK):** already differentiated in the floors paper — they model revocable output increments, not tool semantics or runtime contracts. Reuse verbatim [V-local].
- **Moshi / OpenAI Realtime API:** native duplex = the ceiling; keep the honest scope statement "duplex *structure* at cascade cost, no token-level interleave" [V-local].
- **No competing paper claims "event-driven orchestration for voice agents" as a formal contribution in local KB** [V-local]; live arXiv 2026 sweep still mandatory before §2 (the floors outline already mandates this gate) [U-doc].

## 4. Instantiation recommendations (3 cells, with effort)

1. **LiveKit Agents — showcase cell.** Highest reward: voice-native, industry credibility; documented events map onto Σ (user-state → turn, playback callbacks → delivery lifecycle, `function_tool` → dispatcher). Effort: **medium, 2–4 days** — adapter shape already proven by the pipecat bridge; risk = undocumented (b)/(d) semantics, resolved by reading source. Deliverable: conformance kit green through a LiveKit adapter = "the contract holds in the leading voice framework."
2. **LangGraph — fair-baseline cell.** Required as baseline, not showcase: async nodes + `Send` + checkpoint reentry *emulate* the properties; the paper measures what it costs (code volume + measured latency gap + which invariants break). This makes the serial-graph strawman fair — exactly the hedge the floors paper already committed to ("sufficiency, not uniqueness"). Effort: **low-medium, 1–2 days**.
3. **OpenAI Agents SDK — transfer cell.** Text-side; background tools claimed to exist [U-doc], so the adapter adds only (c)+(d). Demonstrates the contract applies beyond voice transports → "contract, not library." Effort: **low, 1–2 days**.

Skip AutoGen/CrewAI/smolagents/Vercel (no voice, no delivery clock) — one related-work paragraph total.

## 5. Headline experiment spec (single, most defensible)

**One scripted conversation × three instantiations × one invariant suite.**
- Stimulus (fixed, published in the kit): 4 tools, RTT sweep {100, 500, 1000} ms, barge-in mid-tool, user turn mid-pending.
- Instantiations: core runtime (control) · LiveKit Agents adapter · fair LangGraph emulation (async + Send + checkpoint).
- Assertions per run: contract properties (a)–(d) hold; P1–P5 gates (linear A−B gap in (tools−1)×RTT, never-worse at tools=1, turn-ack < RTT, generation-stop < 1 frame, barge-in react < 300 ms).
- Metrics: turn total, turn-ack, cease, generation-stop, resume, invariant violations.
- Why defensible: identical stimulus + identical assertions + published conformance kit = reproducible; operationalizes the *contract* claim (invariants hold through adapters) instead of an unaffordable benchmark campaign; P1–P3 already verified on core [V-local], so new work is purely adapter-side.
- Expected failure mode to report honestly: LangGraph emulation likely breaks (b) (turn can't enter mid-graph) — that measured break IS the result.

## 6. Doc-verification pass (blocks)

Ordered, one fetch each:
1. LiveKit Agents docs: plugin API, `function_tool` lifecycle, interruption/session events, any batch-commit primitive → freezes SPI + fills 2 matrix rows.
2. OpenAI Agents SDK docs: background-tools page (confirm (a) as documented behavior).
3. TEN-framework architecture page → differentiation paragraph (novelty gate).
4. LangGraph docs: `Send` + async nodes + checkpoint semantics (baseline correctness).
5. Live arXiv sweep 2026: "event-driven orchestration voice agents" competing-claim check (Stage-1 gate already mandated by floors outline).
6. Optional: StreamRAG / LLM-Compiler / 2402-async-calling abstracts for the §2 precursor paragraph.

## Sources
- Kept: FINDINGS_event_driven_orchestration.md — G=(Q,Σ,δ), P1–P7, measured invariants [V-local]
- Kept: event-driven-voice-orchestrator README + integrations/README.md — pipecat bridge, 5-port SPI, bench table [V-local]
- Kept: cascade_orchestration_floor/OUTLINE.md — floors framing, hedged sufficiency claim, novelty rules [V-local]
- Kept: orchestration/gaps.md OG1–OG5 — gap map, OG1 folded-as-mechanism [V-local]
- Kept (orchestrator-verified): alphaxiv full-text of 2610.07641 + its references (StreamRAG, LLM-Compiler, 2402 async calling) + EarlyEval 2609.02783 datasets [V-orch]
- Dropped: all web claims from the draft round — replaced by [U-doc] tags + §6 fetch list

## Gaps
- Every [U-doc] cell (matrix §1, §6 list) — the framework survey's empirical content awaits the doc pass; nothing in the paper draft may assert them before it.
- Live arXiv competing-claim sweep (Stage-1 gate) — not runnable in this runtime.
- TEN-framework semantics — unknown; must be read before the novelty claim is written.
- Residual risk if 2610.07641's neighbors (LLM-Compiler etc.) contain a contract-level claim: checked only by name; the §6 pass should skim their abstracts.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Final brief at C:\\Users\\U77225D\\.pi\\agent\\sessions\\--C--Users-U77225D-Desktop-proyectos-hf--\\subagent-artifacts\\outputs\\2aa55de7-eb7a-4c98-89c6-cb0e59465758\\research.md: (1) capability matrix (a)-(d) for 9 frameworks with every framework-specific claim tagged [U-doc]; (2) integration pattern = adapter-per-framework + 5-port SPI, validated by shipped pipecat bridge [V-local]; (3) verified 2610.07641 delta (scheduling strategy vs runtime contract, no barge-in/no turn-during-pending/no framework instantiation, read-only speculation + wasted-calls vs execution-persistence); (4) 3-cell instantiation plan with effort (LiveKit 2-4d, LangGraph 1-2d, OpenAI SDK 1-2d); (5) headline experiment spec (one scripted conversation, RTT sweep, 3 instantiations, invariant suite, expected LangGraph (b) break as result); (6) ordered doc-verification fetch list"
    }
  ],
  "changedFiles": [
    "C:\\Users\\U77225D\\.pi\\agent\\sessions\\--C--Users-U77225D-Desktop-proyectos-hf--\\subagent-artifacts\\outputs\\2aa55de7-eb7a-4c98-89c6-cb0e59465758\\research.md"
  ],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "rewrite research.md from local evidence + orchestrator-verified 2610.07641 facts (no web tools invoked)",
      "result": "passed",
      "summary": "final brief written, 3-tier evidence tagging (V-local / V-orch / U-doc), no web dependency"
    }
  ],
  "validationOutput": [
    "brief ~2 pages, decision-ready; zero untagged claims; doc-fetch pass is executable item-by-item (6 ordered fetches)"
  ],
  "residualRisks": [
    "TEN-framework semantics unverified — blocks novelty wording, not the contract/conformance work",
    "neighbors (LLM-Compiler, StreamRAG, 2402) checked by name only — abstract skim needed in §6",
    "matrix empirical content pending the doc pass — paper §3/§4 must not cite those cells until then"
  ],
  "noStagedFiles": true,
  "diffSummary": "rewrote research.md: draft's unverified web claims replaced by 3-tier evidence tags; 2610.07641 section upgraded from [unverified] to orchestrator-verified delta; added headline experiment spec, effort estimates, ordered doc-verification list",
  "reviewFindings": [
    "no blockers"
  ],
  "manualNotes": "2610.07641 delta is now verified and clean: they are a scheduling strategy (read-only speculation during streaming ASR, proprietary Android, TTFA metric) with none of our four contract properties — they must be cited first, not defended against. The single decision the supervisor should ratify: the headline experiment (core + LiveKit adapter + fair LangGraph emulation, same stimulus + invariant suite) before the conformance-kit SPI is frozen."
}
```

---
## Doc-verification progress (orchestrator, 2026-10-14 afternoon)
- **LiveKit Agents [V-doc]:** tools docs (docs.livekit.io/agents/build/tools/) literally state
  "Tools can run synchronously or in the background, letting the agent keep talking while
  long-running work completes" → property (a) NATIVE. Remaining for the matrix: (b)(c)(d) —
  needs the delivery/interruption docs pages.
- **OpenAI Agents SDK [partial]:** docs tree confirmed (Voice + Realtime + Sessions sections
  exist; function tools page present). Async background semantics NOT yet extracted (nav-heavy
  page) → stays [U-doc].
- **TEN framework [U-doc]:** thenten.ai/docs/overview 404 — find the right docs URL.
- **LangGraph [U-doc]:** untagged; checkpoint/Send claims from prior session remain [U-doc].
