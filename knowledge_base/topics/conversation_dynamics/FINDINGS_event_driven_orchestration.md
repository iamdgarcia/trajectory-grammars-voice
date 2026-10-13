# Event-Driven Orchestration — Architecture Findings (iabto-ms-bc-orchestrator distillation)

_Distilled 2026-10-13 from the iabto-ms-bc-orchestrator POC: the event-driven runtime that replaces
LangGraph orchestration with a 500-line event loop (Pipecat demoted to transport). Sources: repo
README, `src/orchestrator/application/orchestrator.py`, `src/orchestrator/domain/*.py`,
`scripts/smoke_cessation.py` (executed: all invariants hold), and the harness spec
(`papers/_next_angles/harness_spec.md`). LaTeX-ready: math in `$…$`, theorem references match the
companion papers (`latencyfloor2025` = cascade_voice_latency; the orchestration-floor paper's
`thm:cessation_floor`, `thm:tool_hiding`, `def:interruptibility`, `def:phases`, `def:tool_typing`).
Purpose: candidate formalization for the trajectory-grammar paper (`papers/trajectory_grammars_voice/`)
and gap mapping for CD1–CD4._

## E1. The runtime as a trajectory grammar instance

Gap CD1 asks for a grammar $G=(Q,\Sigma,\delta)$ over voice-agent conversation states, with typed
transitions, terminal outcome classes, and a drift statistic (cycle depth). The orchestrator POC is
a mechanically instantiated $G$ — not yet the normative one (no outcome classes), but the first
artifact in the factory where $Q$, $\Sigma$, $\delta$ are executable code rather than definitions.

**State space $Q$.** One canonical `ConversationState` per conversation:

$$
q = (M,\; B,\; P,\; R,\; S) \in Q
$$

- $M$: canonical message history (provider-independent `ConversationMessage`: role, content,
  `tool_calls`, `tool_call_id`). Grows append-only; assistant tool-call messages are committed only
  together with their complete result batch (API-valid history, `def:apivalid`).
- $B$: pending tool batches, $b = (\text{decision}, \{results\})$ with
  `batch.is_complete() $\iff$ every call has a result`.
- $P$: per-call lifecycle, `status $\in$ {active, completed, failed}`.
- $R$: response records, one per model invocation with visible output. Each
  $r = (\text{generation\_status} \in \{\text{streaming}, \text{completed}, \text{cancelled}, \text{failed}\},$
  $\text{delivery\_status} \in \{\text{pending}, \text{playing}, \text{completed}, \text{interrupted}\},$
  content, interruption\_reason$)$. **Generation and delivery are independent clocks** — this is the
  property the whole design turns on (E3).
- $S$: loaded skills (mutable tool surface).

**Event alphabet $\Sigma$.** Five event types, all transport-neutral:

$$
\Sigma = \{\,\textsf{UserTextReceived}(x),\; \textsf{ToolCallFinished}(\rho),\;
\textsf{OutputDeliveryStarted}(r),\; \textsf{OutputDeliveryCompleted}(r),\;
\textsf{OutputDeliveryInterrupted}(r, \kappa)\,\}
$$

with $\kappa$ the interruption reason (e.g. `generation_cancelled`, or the transport's barge-in).

**Transition function $\delta: Q \times \Sigma \to Q \times \{\textsf{invoke}, \textsf{skip}\}$.**
Event application is deliberately semantics-free (the runtime never classifies user wording):

| Event | State change | invoke? |
|---|---|---|
| `UserTextReceived(x)` | $M \mathrel{+}= \textsf{user}(x)$ | yes |
| `ToolCallFinished(ρ)` | attach result; if batch complete: commit $\textsf{assistant}(\text{tool\_calls}) + \textsf{tool}(\rho)$ pair into $M$ | only when batch completes |
| `OutputDeliveryStarted(r)` | $r.\text{delivery} = \textsf{playing}$ (if pending) | no |
| `OutputDeliveryCompleted(r)` | $r.\text{delivery} = \textsf{completed}$ (if not already interrupted) | no |
| `OutputDeliveryInterrupted(r, κ)` | $r.\text{delivery} = \textsf{interrupted}$, record $\kappa$; cancel open generation | interrupts model |

plus the **model-reentry rule**: any event with $\textsf{invoke}$ triggers `_run_interruptible_model()`.
During an active generation, a `UserTextReceived` / `ToolCallFinished` / `OutputDeliveryInterrupted`
event **cancels the stream mid-decode** (real `asyncio` cancellation of the async generator), applies
the event, and re-invokes — this is `def:interruptibility` (generation-interruptible) composed with
execution-persistence (background tools are never cancelled by barge-in).

**Mapping onto CD1.** The runtime *is* an emission model for the grammar:

- Grammar transitions $\delta_G$ := runtime event applications; every CD1 transition type has a
  deterministic trigger here (user turn, tool batch commit, delivery lifecycle).
- **Cycle depth is directly observable**: model invocations per user utterance, counted from
  `turn_id`/`response_id` pairs (each `_run_model_once` allocates a fresh `response_id`). A user
  utterance that needs $k$ tool round-trips yields a cycle depth of exactly $k+1$ invocations —
  the drift statistic CD1 wants (distinguishing "longer" from "off-path") is a counter on this
  runtime, not a learned quantity.
- **Terminal outcome classes are the open part.** The runtime has no
  {contained, abandoned, handoff, compliance-escape} marking. But each class has a candidate
  mechanical correlate: `handoff` = committed history contains a handoff-typed tool call
  (`salesforce2025workflows`-style structure); `abandoned` = conversation ends with
  `delivery_status = interrupted` and no subsequent user turn; `contained` = terminal exchange with
  all batches completed and delivery completed; `compliance-escape` requires an external compliance
  detector (out of runtime scope, correctly so per the semantic-policy abstention).
- Emissions for a predictor: message contents, per-event timestamps, delivery lifecycle, tool
  arguments — i.e. the runtime already logs the grammar's emission sequence.

**Honest framing:** this is $G$ as *operational semantics* (what the machine does), not yet $G$ as
*normative semantics* (what the conversation should be labeled). The bridge — outcome-class
annotation on terminal states — is exactly the CD4 KPI-mapping contribution
(`walker1997paradise` cost axis).

## E2. The concurrency argument: duplex structure without a duplex model

The runtime reproduces the **turn-taking structure** of S2S-duplex systems in a cascade, minus
token-level interleaving. State honestly what is and is not gained.

**Gained.**

1. **Pipeline overlap (tool hiding).** Tools execute during TTS playback of the segment that
   requested them. Under `thm:tool_hiding` (orchestration floor), background dispatch with reentry
   removes type-B/C tool round-trips from the first-audio gate; only type-A tools (result required
   before any audio) sit on the onset floor. The POC's dispatcher is exactly that background clock
   (`def:floors`), with per-call records persisted (`ToolDispatcherSnapshot`).
2. **Non-stalling user turns.** A user turn arriving during phase-tool (model waiting on tools) is
   appended immediately and triggers a fresh model invocation that *sees the pending calls as
   internal context* (system prompt block). The model, not the runtime, decides whether the new
   utterance supersedes, amends, or ignores the in-flight calls. In LangGraph-style serial graphs
   this turn would queue behind the graph; here it is a first-class event. This is the
   floor-greeting behavior full-duplex models get natively (`defossez2024moshi`-style), achieved
   with batch APIs.
3. **Execution persistence under barge-in.** Cancelling generation never cancels dispatched tools;
   their completion still re-enters the model. A user interrupt mid-lookup therefore costs one
   wasted generation, not one lost tool result — the resume-after-interrupt case the harness spec
   tracks as state fidelity.

**Not gained (be explicit).**

- **No token-level interleaving.** The model never attends to user speech *during* decode. User
  speech during phase-gen cancels the stream instead of updating it; reentry is batch-level
  (turn/tool-completion granularity), not incremental. A duplex model would absorb "wait, actually—"
  mid-sentence; this runtime produces a cancelled partial and a fresh generation. The
  duplicate-suppression hack (E4) exists precisely to paper over the resulting restart artifact.
- **No overlapping audio.** Only one response is audible at a time; the runtime cancels the
  previous audible tail on interrupt (flush-on-cancel, matching `thm:cessation_floor`'s
  $\delta_{\mathrm{cease}} \in [\tau_f, d\cdot\tau_f] + \delta_{\mathrm{detect}} +
  \delta_{\mathrm{decide}}$). True duplex permits backchannel-over-speech; this does not.

**Connection to the $k$-step bound.** With `thm:react` (`latencyfloor2025`),
$\Lambda_k = \lambda_{asr} + k\lambda_{lm} + (k-1)\lambda_{tool} + \lambda_{tts}$. The runtime's
background dispatch attacks the $(k-1)\lambda_{tool}$ term (type-B/C tools drop off the critical
path); the $k\lambda_{lm}$ term **remains and is the runtime's invariant cost** — every tool
completion is a full re-invocation. This yields the cycle-length constraint for the grammar: given
a silence budget $\Lambda_{\max}$, the admissible cycle depth is

$$
k \leq k_{\max} \approx \frac{\Lambda_{\max} - \lambda_{asr} - \lambda_{tts} - \lambda_{tool}^{A}}{\lambda_{lm}}
$$

and the CD1 drift statistic (cycle-depth growth across a session) is precisely the quantity that
predicts budget breach. A trajectory whose cycle depth trends toward $k_{\max}$ is the
"off-path" case CD1 wants distinguished from "merely long".

## E3. Generation/delivery independence as the CD3 observation channel

Gap CD3 requires outcome predictors to condition on **voice physics and tool state** — turn states,
tool-call events, endpointing/barge-in flags — because text-only turn signals are near chance in
Spanish (0.40–0.54; jev-vad-poc sweep, see `FINDINGS.md` in `semantic_vad/`). The runtime exposes
exactly this multi-channel observation stream as first-class state:

1. **Delivery lifecycle = what the user physically heard.** `OutputDeliveryStarted/Completed/
   Interrupted` distinguish "generated but never played" from "played completely" from "cut off at
   reason $\kappa$". A text-only transcript collapses these; a predictor conditioning on
   delivery status knows the user never heard the cancelled 200 ms of a barge-in response.
2. **Barge-in with reason = endpointing/barge-in flag.** `interruption_reason` records the cause
   (`generation_cancelled` vs transport barge-in), the phase (gen vs play, `def:phases`) is
   recoverable from generation vs delivery status at event time.
3. **Tool state = batch/call lifecycle.** `PendingToolCall.status`, dispatch records with
   queued/running/completed timestamps, arguments — the tool-event channel, persisted.
4. **Heard/not-heard injection = conditioning by construction.** `_system_prompt()` adds an internal
   block when the latest response was interrupted ("the user may not have heard it; use their next
   intervention to decide whether to retake, summarize, or move on"). The *next decision* is thus
   already conditioned on the delivery channel. An external outcome predictor
   (`nourbakhsh2026tracer`-style, but multi-channel per CD3) can consume the same events without
   new instrumentation: $(x_{1:k})$ = interleaved stream of message events, delivery lifecycle
   events, and tool events with monotonic timestamps.

The correspondence is exact: CD3's "grammar emissions over multi-channel observations (turn states
from `x2turn2026` + tool-call events + endpointing/barge-in flags)" is a superset of what this
runtime already emits. What CD3 additionally demands — intervention decision latency accounted
against $\Lambda^*$ and the cessation floor — is measurable here because the runtime's clocks
(generation, delivery, tool) are separated, so the cost of waiting for a predictor before acting is
computable, not assumed. Early-outcome decisions can be evaluated against the same budget the
runtime itself must meet (cf. `howard2021time` anytime-valid confidence sequences for the
decision-side; CD2's SPRT transpose is the open formal piece, `consol2025` is the wrong level —
inside one call — while this runtime offers the right level: across turns).

## E4. Weaknesses (measured or read off the code; none fatal, all bounded)

1. **Duplicate-suppression prefix-match fragility.** `_run_model_once` withholds deltas while the
   accumulating response is a prefix of the last visible response. Two legitimate consecutive
   turns that start identically ("Sí, claro, …") silently swallow text until the streams diverge;
   a reentry response *equal* to the previous one is never emitted at all. The heuristic targets
   the real artifact (restart-style duplication after cancellation) but is a string-prefix
   proxy for intent. Ceiling: swap for response-id-scoped suppression (the runtime already has
   `response_id`; the check is only needed across cancellation restarts of the *same* turn).
2. **Non-cancelable dispatched tools.** Execution-persistence is a design commitment
   (`def:interruptibility`), not an accident — but it means an already-dispatched
   `send_transfer` completes after a user's "wait, no". The README is explicit: invalidation
   belongs to an explicit application policy port. Until that port exists, safety-relevant
   tools must be made internal (confirmation-gated) at the registry level.
3. **No backpressure on turn bursts.** Every user turn invokes the model; $N$ rapid turns cost
   $N$ invocations (superseded streams are cancelled promptly — measured generation-stop 0 ms —
   but prefill is paid per invocation). Ceiling: coalescing/debounce policy port; latency-sensitive
   voice needs the opposite (immediate), cost-sensitive text can queue.
4. **No token-level duplex.** As E2: batch-level reentry, cancel-and-restart instead of
   update-in-place. This is the structural ceiling of the approach; the honest claim is
   "duplex *structure* at cascade cost", not "duplex behavior".
5. **Single-writer event loop.** One `asyncio.Queue` + one processor task per conversation; no
   multi-tenant story beyond per-conversation instances (README documents per-session dispatcher
   state files). Fine at POC scale, a real constraint at fleet scale.

## E5. Testable predictions for the benchmark

The named benchmark file (`bench_orchestration.py`) **does not exist yet** — the measurement
artifacts today are `scripts/smoke_cessation.py` (5-run medians, executed 2026-10-13, all
invariants hold on this machine) and the harness spec (`papers/_next_angles/harness_spec.md`,
H1–H4 cells, not yet built). The predictions below are stated as **acceptance gates**: they bind
whichever harness implements the spec's cells, and each is already anchored by the smoke cells
where noted.

| # | Prediction | Cell / source | Status |
|---|---|---|---|
| P1 | Cessation tail is linear in in-flight depth: cease$(d{=}6) >$ cease$(d{=}1) + \tau_f/2$, with cease $\approx d\cdot\tau_f$ ($\tau_f = 100$ ms frame) | smoke `measure_cease` | **holds**: 609 vs 109 ms (5-run medians) — matches `thm:cessation_floor` phase-play bound |
| P2 | Generation cancellation is prompt and depth-independent: generation-stop $< 1$ frame at every depth | smoke `measure_cease` | **holds**: 0.0 ms at depths 1 and 6 (phase-gen task-cancel path) |
| P3 | Resume after interrupt-during-tool is dominated by the tool round-trip: resume$(\lambda_{tool}{=}1\text{s}) >$ resume$(\lambda_{tool}{=}10\text{ms}) + 400$ ms | smoke `measure_resume` | **holds**: 1000 vs 0 ms |
| P4 | Multi-tool turns: event-driven (H4) beats serial LangGraph (H1) on silence gap by $\geq (k{-}1)\lambda_{tool}$ for type-B/C tools, at equal state fidelity | harness spec H1 vs H4 (silence-gap + tool-hiding cells) | open — defines the harness build |
| P5 | Barge-in react (user interrupt → agent_stop) $< 300$ ms in the event-driven cell, independent of tool count (persistence means no tool-cancel storm) | harness spec barge-in react cell | open |
| P6 | Per-turn model-invocation count = cycle depth $k{+}1$ (E1 counter); prefill (TTFT vs turn #) is flat for in-memory state but grows monotonically without compaction — the forgetting-floor open problem | harness spec prefill-cost + context-drift cells | open |
| P7 | User-turn-during-tool: the reentrant invocation observes pending calls (internal context) and completes without waiting for them, i.e. perceived silence gap of the overlapping turn $< \lambda_{tool}$ | runtime behavior, `ejemplo_run.txt` trace; needs a harness cell | open — the non-stalling claim, currently trace-verified only |

P1–P3 are the smoke anchors (the paper's `thm:cessation_floor` / `thm:tool_hiding` statements
reproduced on one machine, synthetic latencies). P4–P7 require the full harness; they are written
so `bench_orchestration.py` (or successor) can assert them directly.

## References (KB cite keys)

`yao2023react` ($k$-step loop, latency limitation), `latencyfloor2025` (cascade_voice_latency:
`thm:react`, `thm:streaming_floor`), orchestration-floor paper (`thm:cessation_floor`,
`thm:tool_hiding`, `def:interruptibility`, `def:phases`, `def:tool_typing`, `def:apivalid`),
`sierra2024taubench` (full-episode outcome paradigm), `nourbakhsh2026tracer` (partial-transcript
failure forecasting — the predictor CD3 upgrades), `x2turn2026` (frame-synchronous turn states),
`skantze2021turn` (turn-taking as no-standard), `bohus2011interruptions` (interruption decisions),
`walker1997paradise` (quality = success + cost), `consol2025` + `howard2021time` (SPRT /
anytime-valid sequences, CD2 direction), `salesforce2025workflows` (workflow extraction — handoff
correlate), `wald1947sprt` (sequential decision foundation).
