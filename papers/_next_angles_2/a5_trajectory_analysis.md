# Conversation Trajectory Analysis for Voice Agents

## Working title
*Turn-Level Trajectory Grammars for Voice Agents: Early Outcome Prediction and Intervention on Partial Conversations*

## Landscape
1. **τ-bench / τ²-bench** (arXiv:2406.12045, arXiv:2506.07982) — airline/retail/telecom customer-service LLM-agent benchmark; pass^k on full trajectories; no outcome-from-partial, no telephony voice, no drift.
2. **WebArena** (arXiv:2307.13854) and **SWE-bench** (arXiv:2310.06770) — trajectory-logging, success-only, static; the trajectory is data but not the object of analysis.
3. **Process mining on dialogues** (Klijn et al., "Dialogue Process Mining", arXiv:2410.00181; van der Aa, "Aligning event logs to declarative process models", Information Systems 2022) — conformance checking over dialogue acts; nothing bank-KPI-tuned, nothing voice-agent.
4. **Dialogue failure/success prediction** (Nanda et al., SIGDIAL 2021; Aackar et al., "Predicting task completion and user satisfaction", Information Processing & Management 2025 [verify]) — text-chat, post-hoc or late; no partial-transcript guarantee, no action rule.
5. **Voice-agent ecosystems** (arXiv:2504.06055 Voice Agent Benchmark; LiveBench/Speech [verify]; MultiVOI EN/ES turn-taking, arXiv:2505.22463) — component quality; conversations as data, never trajectories.
6. **Compliance/safety evals** (Crÿs et al., "Benchmarks for Differential Privacy", ACM CSUR 2025 [verify]; Garak, arXiv:2406.11036; HarmBench, arXiv:2402.05793) — prompt-level events; no conversation-level conformance accounting.
7. **Human-contact-center analytics** (Joshi et al., "An Empirical Study on Agent Assist using LLMs", arXiv:2409.11373) — supervised call-outcome classification, human-agent only, training-heavy.
8. **Abandonment/containment** — scattered industry reports and one Microsoft patent (US11954702B2, 2024); no formal model, no early-warning bound, nothing Spanish/voice.
9. **Anomaly detection over LLM agent traces** (arXiv:2412.04574 [verify]; proprietary "Guardrails Agent Trace Analyzer") — unsupervised outlier mining of traces; no semantics, no speech constraints, no banking KPI.
10. **Task-oriented dialogue evaluation** (SGD, arXiv:1909.05728; MultiWOZ; SIGDIAL community) — slot-filling turn corpora; latency and voice physics absent.

## The gap
No formal trajectory grammar or state-space model for voice-agent conversations that (a) defines outcome as a trajectory class (contained / abandoned / handoff / compliance-escape), (b) predicts that class from the **partial transcript** with a calibrated, provable decision time, and (c) is tuned to banking KPIs. Testable RQ: *can a partial-conversation trajectory state-space over banking voice-agent logs predict outcome (containment, abandonment, handoff, compliance escape) at turn k with probability ≥ 0.85, early enough (t_k + ε < escalation-only threshold) to act — intervention, escalation, fraud flag — and with detection/decision latency covered by the cascade's published floors?* Why unsolved: (i) LLM-agent trajectory work stops at full-episode success on static web/code tasks (τ-bench, WebArena) — no partial-observation decision theory; (ii) dialogue-process-mining does conformance checking on finished human-human logs, outcome-blind and voice-blind; (iii) contact-center outcome prediction is post-hoc supervised classification with no decision-time bound; (iv) abandonment/containment exist as patents and industry reports, not as formal models; (v) nothing Spanish-first; (vi) voice-physics constraints (endpointing, barge-in, tool RTT) that make banking trajectories non-stationary are absent everywhere.

## Candidate contribution
1. **Trajectory grammar** — a formal state space G = (Q, Σ, δ) over conversation states (greeting, auth, intent, tool-loop, clarification, confirmation, close) with typed transitions Σ; success/failure/handoff/compliance-escape as terminal classes; treat regressions (return-to-clarification, tool retry) as grammar cycles — cycle depth becomes a first-class *drift* statistic, formally distinguishing "longer" from "off-path".
2. **Partial-observation prediction theorem** — a decision-time guarantee: given turn k and partial transcript x_1..k, a stopping rule on P(class | x_1..k) achieves expected decision time ≤ k* turns at confidence ≥ 1−δ, via sequential analysis (SPRT / confidence-sequence stopping); false-early-exit economics derived from the paper's cost model.
3. **Banking KPI-tuned evaluation protocol** — outcome classes wired to production telephony telemetry (containment %, abandonment %, handoff rate, compliance-escape rate); benchmark on real Spanish call logs (production, GDPR-safe schema) with leave-one-campaign-out validation.
4. **Intervention coupling** — the state-space's escalation states plug into the production LangGraph orchestration (live handoff triggers, proactive clarification, fraud-flag routing), making prediction actionable, not just measurable.

## Reuse of our published results
- **Latency floor paper (Lambda\*, τ_human ≈ 200 ms, k-step ReAct bound)** — the k-step bound becomes the *cycle-length* bound inside the grammar; floor arithmetic (per-turn components) gives the real decision latency of an intervention trigger, so "early enough to act" is measured, not assumed.
- **Cessation-floor paper (detect/decide/cease/resume)** — the *detect* stage is the same partial-observation problem at utterance scale; trajectory prediction is the conversation-scale analogue. Escalation decisions must also clear a cessation floor (barge-in on the agent mid-drift), so the two papers compose: trajectory decides *when*, cessation decides *how fast to stop*.
- **"Asking Instead of Listening" (semantic VAD, Spanish turn-end near-chance 0.40–0.54, cloud p99 178–268 ms)** — the Spanish partial-transcript pipeline and its measured cloud decision latency (p99 178–268 ms) are the ready-made sensing substrate for turn-level state estimation; the paper's finding that text-only turn-end is weak warns the grammar must condition on intent/tool state, not text alone — a concrete design constraint, not a confound.

## Banking grounding
- Production GKE cascade (ASR→LangGraph→TTS) gives real Spanish call logs with turn timings, tool-call RTTs, barge-in events — the dataset the theorem's empirical section needs.
- Compliance escapes (unauthorized commitments, data leaks, disclosure omissions) become a terminal trajectory class — a conversation-level guardrail, complementing the per-turn guardrail gaps in `ai_guardrails` (G1/G3).
- Fraud flags as trajectory anomalies (e.g., repeated auth failures → social-engineering signature) — directly actionable routing in the production graph.
- Handoff decision = the escalate state; cost model ties false escalation to agent-minutes, false containment to AHT and repeat-call rate. Spanish-first: primary evidence, not an afterthought.

## Scores
- **Novelty = 4** — trajectory-as-grammar for voice agents with partial-observation decision guarantees is unclaimed; adjacent work (τ-bench, dialogue process mining, call-outcome classifiers) leaves the intersection empty.
- **Fit = 5** — directly extends the latency/cessation/semantic-VAD program from turn-scale to conversation-scale; same production system, same Spanish cascade, natural third paper.
- **Banking = 5** — containment, abandonment, fraud, handoff, compliance-escape are the actual production KPIs; every outcome class maps to a real ops lever.
- **Feasibility = 4** — data exists (production logs), theory reuses sequential-analysis and our own floor arithmetic; risk is class balance (abandonment/fraud may be rare) needing oversampling or longer collection.
- **Risk = 3** — moderate: an LLM trajectory-modeling paper could drop mid-project (fast-moving space); mitigation is that no competitor has voice + banking KPIs + decision-time guarantees simultaneously.

## Verdict
**Pursue now.** Highest-synergy next paper in the program: reuses all three published results as load-bearing machinery, runs on data the author already owns, and fills a gap (formal trajectory grammar + partial-observation prediction + banking KPI wiring) that adjacent 2024–2026 work structurally cannot reach — static-task agent benchmarks lack voice and partial decisions; dialogue process mining lacks voice and KPIs; call analytics lacks formality. The k-step ReAct bound from paper #1 becomes the grammar's cycle-length constraint, making the paper an honest extension rather than a new thread.
