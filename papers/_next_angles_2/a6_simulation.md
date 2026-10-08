# Calibrated Conversation Simulation — Synthetic Banking Customers

## Working title
**"The Sim-to-Real Gap of Voice-Agent Simulation: Calibrating Synthetic Banking Customers Against Real Spanish Call Logs"**

## Landscape
1. **τ-bench** (arXiv 2406.12045) — LLM user simulator for tool-agent eval; exposes the core problem: simulators drift (e.g., "confirmer" mode — agreeing too easily), and its authors flag simulator bias as an open issue [verify exact framing].
2. **τ²-bench** (arXiv 2506.07982 [verify]) — dual-control telecom domain; simulator must act on *its* side of the world, closer to voice-banking reality but still text, no timing behavior.
3. **Full-Duplex-Bench v2** (arXiv 2506.07985 [verify]) — simulator-driven evaluation of turn-taking/full-duplex behaviors (backchannels, interruptions) via an *audio* simulator; the closest neighbor, English-only, no banking, no calibration against real logs.
4. **Full-Duplex-Bench** (arXiv 2410.11915 [verify]) — v1: first standardized full-duplex interaction benchmark; single-scenario spliced cues.
5. **SODA** (arXiv 2110.10750) — 1M social dialogues; the standard backbone for persona-conditioned synthetic users; task-oriented *banking* fidelity is out of scope.
6. **Sotopia** (arXiv 2310.11667 [verify]) — social-agent environment with reward models over social goals; behaviors scored, not *calibrated* to production call distributions.
7. **Generative Agents** (arXiv 2304.03442) — persona memory/consistency lineage; fidelity is judged believability-by-humans, not metric-level agreement with real callers.
8. **UserBench** (arXiv 2507.22034 [verify]) — user-centric agent evaluation with lazy/incremental users; realistic user *traits*, but text chat, no acoustic/timing axis.
9. **VoiceBench** (arXiv 2410.17796 [verify]) — voice LLM evaluation; fixed prompts, no simulated interlocutor, no turn dynamics.
10. **Switchboard / CallHome Spanish (LDC corpora)** — real two-sided telephone Spanish; the only practical calibration source with grounded timing, disfluency, and code-switching, but not banking and not agent-in-the-loop.

## The gap
**Testable RQ:** Do LLM-simulated banking customers reproduce the *conversation-metric distribution* of real Spanish voice-banking calls — turn-gap timing vs. the human clock τ_human ~200 ms, barge-in rate/latency, disfluency rate, Spanish↔English code-switch points — well enough that agent policies ranked by simulator evaluation match ranks from real-call evaluation (rank correlation as the headline sim-to-real transfer number)?

**Why unsolved:** Every existing simulator (τ-bench lineage, FDB v2, Sotopia) is *used* as an evaluator but never *validated distributionally*: no paper reports agreement between simulator-induced and real-call distributions of conversation metrics, and none conditions the simulator on real logs at all. Text simulators have no acoustic/timing axis; audio simulators (FDB v2) have scripted cues, not log-calibrated behavior. Sim-to-real transfer of *conversation metrics* (as opposed to task success or speech quality) is measured by nobody — including in banking, where logs are private and unpublished. This also connects to the local gaps: SV2 (no labeled multilingual turn-policy benchmark — a calibrated simulator could *generate* labeled scenarios) and G4 (evaluation standardization — a calibration protocol is a reporting standard).

## Candidate contribution
A **calibration framework + benchmark**, not another simulator:
1. **Behavioral fidelity axes** formalized from our published metrics: onset timing (Λ*/τ_human), cessation/barge-in timing (detect→cease), disfluency, backchannel, code-switch — each a measurable distribution the simulator must hit.
2. **Sim-to-real transfer protocol**: fit simulator parameters (impatience, silence tolerance, filler usage) on a calibration split of real logs; hold out scenario classes (balance checks, transfers, fraud); report rank correlation of agent-policy scores and Wasserstein divergence of metric distributions between sim and real.
3. **Regression harness**: simulator-driven regression testing of turn policies (two-question VAD operating points) and tool DAGs (simulated backend faults: timeouts, slow RTTs), with an explicit sim/real divergence budget.
4. Honest null-result path: if transfer is low, the paper identifies *which* behavioral axis breaks — itself a benchmark contribution.

## Reuse of our published results
- **Latency floor paper**: supplies the metric set (Λ*, τ_human, k-step ReAct bound) the simulator must match distributionally — timing fidelity is defined against our own theorems.
- **Cessation floor paper**: defines the barge-in/cease/resume behaviors the simulator must reproduce (generation-interruptible vs execution-persistent stress cases become simulator scripts).
- **Asking Instead of Listening**: the two-question VAD + 100-phrase Spanish benchmark become the *thing under regression test* — the simulator stress-tests its veto operating point (P 0.68/R 0.85) against adversarial personas (impatient cutters, backchannelers, code-switchers).

## Banking grounding
- **Private Spanish call logs**: calibration data; privacy-safe release path via synthetic reconstruction (transcripts re-synthesized, no raw audio).
- **Fraud-scenario stress testing**: simulator plays vishing/social-engineering personas to test guardrail escalation and disclosure scripts — direct tie to ai_guardrails G1/G4 and to real core-banking tool backends under LangGraph orchestration.
- **Compliance/audit**: deterministic simulated regression suites are auditable artifacts regulators can accept, unlike live probes of production.
- **Production telemetry**: iabto-ms-bc logs (V2V latency, barge-in events) are the ground-truth distributions.

## Scores
- **Novelty: 4** — sim-to-real transfer of conversation metrics is unmeasured everywhere; simulators exist but are unvalidated.
- **Fit: 5** — consumes all three published papers as metric/behavior definitions; fills SV2/G4 adjacency.
- **Banking: 5** — fraud personas, Spanish calibration, tool-DAG regression, audit compliance are all banking-native.
- **Feasibility: 3** — blocked on real-log access and a sim/real split; buildable after the jev-vad-poc infra, but data negotiation is out of our control.
- **Risk: 3** — simulator fidelity may prove too low for transfer (null result is publishable but less impactful); commercial vendors may hold private equivalents [verify].

## Verdict
**Pursue later (high priority)** — the calibration claim is untestable until real-log access is secured; angle 5 (eval stack) or SV4 (dispatch-on-interim) lead now. The moment iabto-ms-bc log/telemetry access lands, this jumps the queue: it is the natural *third* program paper and reuses 100% of the existing metric apparatus.
