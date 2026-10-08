# OUTLINE — Turn-Level Trajectory Grammars for Voice Agents

**Working title:** *Turn-Level Trajectory Grammars for Voice Agents: Early Outcome Prediction and Intervention on Partial Conversations*

**Slug:** `papers/trajectory_grammars_voice/`

**Status:** Stage 1–2 complete (gap detection + outline). Next: Stage 3 LaTeX writing.

---

## 1. Contribution statement

No formal model exists of voice-agent conversations as *trajectories* with early outcome
prediction. Adjacent work is structurally short: LLM-agent trajectory work stops at
full-episode success on static tasks (τ-bench, WebArena); dialogue process mining does
conformance checking on finished human–human logs, outcome-blind and voice-blind;
contact-center outcome prediction is post-hoc supervised classification with no
decision-time bound; TRACER (2607.03974, EMNLP 2026 — full text read and verified
2026-10-08) is the nearest neighbor: partial-dialogue failure forecasting with a
thresholded recovery trigger, but it is a learned classifier with no decision-time
guarantee, single-outcome (failure/success), English text-chat benchmarks (MultiWOZ/SGD/ABCD),
no voice physics (endpointing, barge-in, tool RTT), no voice-agent state space
(tool calls, endpointing errors, barge-ins, auth), and no banking KPI wiring
(containment, abandonment, compliance escape, fraud signature).

**The paper delivers:**

1. **Trajectory grammar** — a formal state space G = (Q, Σ, δ) over voice-agent conversation
   states (greeting, auth, intent, tool-loop, clarification, confirmation, close) with typed
   transitions Σ; outcome as terminal classes (contained / abandoned / handoff / compliance-escape);
   regressions (return-to-clarification, tool retry) as grammar cycles — cycle depth as a
   first-class drift statistic, formally distinguishing "longer" from "off-path".
2. **Partial-observation prediction theorem** — a stopping rule over P(class | x_{1:k}) via
   SPRT / confidence sequences achieving expected decision time ≤ k* turns at confidence ≥ 1−δ,
   with false-early-exit economics from a banking cost model. TRACER's threshold is an instance
   of this rule — the paper generalizes what TRACER instantiates.
3. **Banking KPI-tuned evaluation protocol** — outcome classes wired to production telephony
   telemetry (containment %, abandonment %, handoff rate, compliance-escape rate); evaluation on
   real Spanish call logs with leave-one-campaign-out validation; component latency (decision
   latency of the trajectory monitor measured against the published latency floor Λ* and
   cessation floor).
4. **Intervention coupling** — escalation/clarification/fraud-flag states plug into production
   LangGraph orchestration; prediction is actionable (live handoff triggers), and every
   intervention action must itself clear the published cessation floor (barge-in the agent
   mid-drift to take over).

**Reuse of published results (the honest-extension test):**
- **Latency floor** (Λ*, τ_human ≈ 200 ms, k-step ReAct bound): the k-step bound becomes the
  trajectory grammar's cycle-length constraint; floor arithmetic gives the real decision latency
  of an intervention trigger, so "early enough to act" is measured, not assumed.
- **Cessation floor** (detect/decide/cease/resume): the *detect* stage is the same
  partial-observation problem at utterance scale; trajectory prediction is its conversation-scale
  analogue; interventions must clear a cessation floor (barge-in mid-drift).
- **Asking Instead of Listening** (semantic VAD): the Spanish partial-transcript pipeline and its
  measured cloud decision latency (p99 178–268 ms) are the sensing substrate for turn-level state
  estimation; text-only turn-end near chance (0.40–0.54) warns the grammar must condition on
  intent/tool state, not text alone — a design constraint, not a confound.

## 2. Verified landscape (retrieval 2026-10-08, alphaXiv MCP)

All IDs verified live on alphaXiv unless marked [verify]. Two-round discovery: 11 queries across
agent-benchmark, process-mining, outcome-prediction, containment/queueing, SPRT, conversational
grammar, banking, and Spanish-voice facets.

### Nearest neighbors (read in full text)
- **TRACER** — arXiv **2607.03974** (EMNLP 2026, UT San Antonio). Partial-dialogue failure
  forecasting: dual-stream (belief-state trajectory features + serialized belief text, RoBERTa +
  small Transformer), MultiWOZ 2.4 (+SGD/ABCD zero-shot transfer), AUC 0.741 oracle / 0.617
  generated, EDS/det-turn metrics, threshold τ=0.7788 frozen under FPR ≤ 0.15, template recovery
  beats T5 recovery. **Positioning: TRACER is a learned classifier; no stopping rule, no
  decision-time guarantee, single binary outcome, no voice physics, no banking KPIs.** Code:
  github.com/erfan-nourbakhsh/TRACER.
- **EarlyEval** — arXiv **2609.02783** (2026-09-02, SJTU/SMU/ECNU). Early outcome prediction to
  cut agent-evaluation cost; ranking over full episodes, not live partial-transcript prediction in
  a running conversation; no decision-time guarantee; not voice, not banking.
- **Queue control in human–AI service systems** — arXiv **2607.06017** (2026-07-07). Chatbot +
  human two-stage queue control (which tasks to escalate); complements our escalation state but
  has no conversation-internal signal, no trajectories, no voice.
- **Nubank eval-driven support agents** — arXiv **2606.08867** (2026-06-07, Nubank). Production
  100M-user-scale support-agent evaluation framework; containment-adjacent industrial practice,
  no formal trajectory model.
- **ConSol** — arXiv **2503.17587** (2025-03-22). SPRT to stop LLM reasoning paths — SPRT applied
  at the *reasoning-path* level, not conversation-turn level; the stopping-rule citation.
  (Related: [verify] early-exit / early-stopping LLM decoding literature.)
  [verify] X2-Turn — arXiv 2608.10878 — frame-synchronous joint streaming ASR + turn-state prediction (turn states at utterance scale; our grammar is conversation scale).
- [verify] HiThink Turn — arXiv 2609.34096 — intent-aware turn-taking control module (interruption selectivity at utterance scale).
- [verify] EarlyEval companion claims; Silent Abandonment in Contact Centers — arXiv 2304.11754 (2024, Technion) — customer-patience estimation from uncertain data (queueing, not conversation-internal).
- [verify] τ-Voice / τ-Multilingual — arXiv 2609.35820 (Sierra/Mercor/Princeton) — Spanish voice-agent benchmarking across languages (component+task quality; no trajectory outcome classes, no decision-time guarantees).
- [verify] ESCUCHA — arXiv 2607.17812 — Spanish speech benchmark, heterogeneous acoustic conditions (acoustic robustness, not trajectory outcomes).
- [verify] Dialogue process mining — Klijn et al., arXiv 2410.00181 — conformance over finished human–human logs, outcome-blind, voice-blind.
- [verify] Flow discovery from TOD — arXiv 2405.01403 — unsupervised dialogue-flow discovery (no outcomes, no voice).
- [verify] Conversational state and behavioral reliability — arXiv 2609.33883 (Georgia Tech) — conversational-state maintenance in LLMs (no outcome prediction).
- [verify] Lost-with-a-map / τ²-bench (2506.07982), WebArena (2307.13854), SWE-bench (2310.06770) — full-episode success, static tasks.
- [verify] Abandonment/containment as patents/industry reports only; no formal model.

## 3. Section plan (Stage 3 writes sections/01–09)

- `01_introduction.tex` — motivation, gap statement, contributions, structure.
- `02_background.tex` — taxonomy: agent-trajectory benchmarks → dialogue process mining → outcome
  prediction → contact-center analytics → our floors program. Cite KB entries.
- `03_grammar.tex` — the trajectory grammar G=(Q,Σ,δ): states, typed transitions, terminal
  outcome classes, cycles as drift; TikZ state diagram; k-step cycle-length lemma.
  - ×m×*: cycle-depth drift statistic; bounded-workload lemma (k-step bound reused).
- `04_stopping.tex` — SPRT / confidence-sequence stopping over the grammar state posterior;
  **Trajectory Stopping Theorem** (expected decision time ≤ k* turns at confidence ≥ 1−δ);
  false-early-exit economics; TRACER threshold shown as a fixed-sample instance of the rule.
- `05_evaluation_protocol.tex` — banking KPI classes; leave-one-campaign-out; Spanish logs;
  decision-latency accounting against Λ* and the cessation floor; TRACER as baseline;
  TRACER-style EDS + det-turn metrics reused (with credit) and extended with cost-weighted
  detection-latency and class-conditional economics.
- `06_intervention.tex` — intervention coupling into LangGraph orchestration; escalation state
  must clear the cessation floor; fraud-flag routing; the a10 escalation-floor interface (future).
- `07_open_problems.tex` — multilingual trajectory classes (a9 interface), escalation floor
  composition (a10), simulation calibration (a6 interface), compliance escapes as trajectory
  classes (a8 interface).
- `08_discussion.tex` — limitations: class imbalance (rare abandonment/fraud), Spanish-only
  evidence, belief-state noise, GDPR-safe schema, legal-precision care, scope (no human-subjects).
- `09_conclusion.tex`.

## 4. Figures (TikZ only)

1. `fig_grammar.tex` — the state machine with terminal classes (paper #1's pipeline DAG style).
2. `fig_stopping.tex` — stopping rule timeline: partial transcript → state posterior → SPRT
   crossing → intervention window vs. escalation-only threshold (cessation-floor composition).
3. `fig_cycles.tex` — cycle-depth drift: contained vs. drifted trajectories as grammar walks.
4. `fig_eval_stack.tex` — banking KPI wiring diagram (containment/abandonment/handoff/compliance).

## 4.5 Related-work deltas from the verification pass (fold into 02)

- TRACER (2607.03974) → cite as the nearest neighbor; our theorem generalizes its threshold as a
  fixed-sample SPRT instance; differs on: no stopping rule, single outcome, text-only,
  MultiWOZ/SGD/ABCD vs. Spanish voice logs, no intervention-latency accounting.
- EarlyEval (2609.02783) → early prediction exists for *offline eval cost reduction*; we do live,
  in-conversation decisioning with guarantees. Different problem.
- Queue control (2607.06017) → escalate-or-not decided *outside* the conversation from queue
  state; we decide *inside* from the partial transcript. Complementary; cite.
- ConSol (2503.17587) → SPRT for LLM reasoning-path early stopping; we transpose SPRT to
  conversation trajectories. Cite as the stopping-rule anchor.
- τ-Multilingual (2609.35820) → Spanish voice-agent quality exists as benchmarks; no outcome
  prediction from partial conversations. Cite.
- Process mining (2410.00181) → conformance on finished human–human logs; outcome-blind,
  voice-blind. Cite.
- Flow discovery (2405.01403) → unsupervised flows, no outcomes. Cite.
- Silent abandonment (2304.11754) → customer patience from queueing data, not conversation
  state. Cite.
- Nubank (2606.08867) → production eval framework, industrial grounding. Cite.

## 5. Stage 3+ execution plan

1. **Verification sweep** — resolve all `[verify]` marks above (done for TRACER full text;
   quick `discover_papers` / `answer_pdf_queries` checks for X2-Turn, HiThink, τ-Multilingual,
   ESCUCHA, process mining, flow discovery, ConSol, EarlyEval, queue control, Nubank).
2. **KB seeding** — create `knowledge_base/topics/conversation_dynamics/` with entries for the
   ~14 anchors above (schema-conformant, verified IDs only; [verify] items resolved or dropped).
3. `templates/arxiv_preprint/` → `papers/trajectory_grammars_voice/`; write `sections/01–09.tex`
   (one sentence per line; natbib \citep/\citet; TikZ figures from `figures/*.tex`).
4. Compile: `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex`
   (0 errors, ≤5 warnings).
5. Stage 4: five-agent review panel (chief editor + 4 reviewers).
6. Stage 5: revision loop (≤5 rounds).
7. Stage 6: arXiv zip; GitHub repo with paper + KB (needs push token from author);
   Hugging Face dataset for the Spanish benchmark artifacts; experiments (if any) via the
   gcloud lab environment (gcloud config: dgarcpea@unicaja.es, europe-west1).
