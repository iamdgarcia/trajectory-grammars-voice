# OUTLINE — What Are We Not Testing? Region Coverage of Conversation Trajectories from Agent Observability Traces

**Working title (primary):** *What Are We Not Testing? Region Coverage of Conversation Trajectories from Agent Observability Traces*

**Working title (alternates):** *Trace to Trajectory: Region-Coverage Evaluation for Conversational Agents* · *The Trajectory Atlas: From Agent Observability Traces to Region-Coverage Evaluation of Conversation Simulators*

**Slug:** `papers/trace2trajectory/`

**Status:** Stage 1–2 complete (gap detection + outline; SOTA scan + extraction probe already shipped). Next: Stage 3 LaTeX writing.

**Companion artifacts (shipped):** `github.com/iamdgarcia/trace2grammar` (extraction + coverage implementation, 40/40 checks), `github.com/iamdgarcia/event-driven-voice-orchestrator` (an agent runtime that emits the canonical events), KB `SOTA_scan_trace2trajectory.md` (4-round alphaxiv scan), KB `FINDINGS_event_driven_orchestration.md` (runtime-as-grammar formalization).

---

## 1. Contribution statement

Production conversational agents emit traces in standardized observability formats (OpenTelemetry
GenAI semantic conventions, OpenInference, LangSmith), and LLM-based user simulators are now the
standard tool for evaluating agents outside production. Yet these two artifacts have never been
joined: no published method maps observability traces to a discrete conversation state space with
terminal outcome classes, and no work quantifies *which regions of conversational behavior a
simulator (or a new agent version) fails to cover* — the evaluation question every team asks
("what are we NOT testing?") and none answers measurably. The 2026 trace-mining wave
(\citep{automataTraces2026, tracedance2026}) mines traces for failure prediction and benchmark
construction; the sim2real wave (\citep{distributionalGap2026, sim2realAgentic2026}) measures
response-level distributional agreement in text; both leave the trajectory level unclaimed.

**The paper delivers:**

1. **Formal extraction mapping $\tau$** — from standard agent-observability exports (OTel GenAI,
   OpenInference, LangSmith) to a grammar walk over the trajectory grammar
   $G = (Q, \Sigma, \delta)$ with terminal outcome classes
   $\{\theta_{cont}, \theta_{aban}, \theta_{hand}, \theta_{esc}\}$ and cycle depth $D$
   (\citep{garcia2026grammar} defines $G$; we define and ship $\tau$). The baseline
   $\tau$ is rule-based with a config-exposed classifier; the emission-model assumption is stated,
   and any calibrated state estimator can replace the baseline without changing the interface.
2. **Region-coverage evaluation** — conversation-level feature encodings (grammar features /
   transition bigrams) $\to$ deterministic 2-D projection (PCA fit on the real set only) $\to$
   density-occupied real regions (Gaussian-bump grid + smoothing with a shared relative threshold)
   $\to$ coverage \% overall and per outcome class $\to$ top-$K$ uncovered regions each with its
   nearest real exemplar: the tests you are not running, made concrete and actionable.
3. **The trajectory atlas** — the visualization + metric layer for sim-vs-real transfer at the
   trajectory level: two point clouds in one behavior plane (real = production, sim = simulator),
   color = outcome class, uncovered regions marked with exemplar tooltips. Positioned against
   \citep{distributionalGap2026} (response-level, text-only), reusing the distributional-comparison
   program of \citep{cds2026}, and feeding the calibrated-embedding agenda of \citep{cue2026}.

**Non-goals / honest scoping:** voice-physics channels (barge-in, endpointing, tool RTT) appear only
as an optional appendix extension — the central claim is region coverage of *conversation
structure*, not acoustic fidelity. The learned emission mapper is future work; this paper ships the
rule-based $\tau$ and its measurement.

---

## 2. Section plan (Stage 3 writes sections/01–09)

### `01_introduction.tex`
- Motivation: agent evaluation is simulator-driven; simulator quality is unmeasured at the level that matters (conversation structure).
- The gap: traces exist everywhere (OTel GenAI adoption 2025–2026), trajectory semantics nowhere.
- Position vs the four neighbors: \citep{automataTraces2026} (automata for failure prediction, no conversation semantics, no atlas), \citep{graphoftrace2026} (scientific-workflow traces, design-time graph, no outcome classes), \citep{tracedance2026} (benchmarks from traces, no state space), \citep{wildvis2024} (corpus-level UMAP of chat logs, no agent spans, no grammar).
- Contributions (the three above), paper structure.

### `02_background.tex`
- **Trajectory grammar recap** — cite \citep{garcia2026grammar} for $G=(Q,\Sigma,\delta)$, the seven progress states, four terminal classes, cycle depth as drift statistic; one paragraph, no duplication.
- **Distributional evaluation lineage** — \citep{cds2026} (Conversational Distribution Score), \citep{mirrorbench2026} (human-likeness of user proxies), \citep{turnbench2026} (turn-taking dynamics outcomes).
- **Sim2real for agent evaluation** — \citep{sim2realAgentic2026} (sim2real gap in agentic tasks), \citep{distributionalGap2026} (measuring + mitigating the distributional gap, text-only response-level), \citep{realUserSim2026} (Formalism Ceiling), \citep{cue2026} (calibrated user embeddings).
- **Observability formats, verified facts** — OTel GenAI semconv (moved to `open-telemetry/semantic-conventions-genai`): `gen_ai.conversation.id` is Conditionally Required and a linking key only (no conversation object exists); span names `invoke_agent` / `execute_tool {tool}`; per-call spans under `gen_ai.input.messages` (Opt-In) at client-inference; OpenInference stable attribute spec (`openinference.span.kind` LLM/AGENT/TOOL/CHAIN); LangSmith run trees with `parent_run_id` grouping. Voice channels die at the transport boundary (pipecat emits them internally, exports nothing) — motivates the optional appendix extension.
- **Anchors from the sibling program** — \citep{nourbakhsh2026tracer} (partial-transcript prediction), \citep{sierra2024taubench} (full-episode outcome paradigm), \citep{salesforce2025workflows} (workflow extraction from logs).

### `03_extraction.tex` (the formal mapping $\tau$)
- Canonical event stream: format-agnostic `{t_ms, kind, name, attrs}` with kinds $\in$ {user_msg, assistant_msg, tool_call, tool_result, tool_error, hangup, handoff, session_end}; one `_normalize_<fmt>()` per dialect; dedupe rules.
- State inference as a config-exposed classifier: keyword/regex pattern tables (auth/handoff/clarify/confirm/close) + sequencing rules; the mapping table from canonical events to $\Sigma$ transition types; per-domain adaptation without code changes.
- Walk construction: runs $\sigma = q_0 \to q_1 \to \cdots \to \theta$; outcome-class assignment rules (contained / abandoned / handoff); compliance-escape as audit overlay (inherited from \citep{garcia2026grammar}); cycle depth $D$ = regression count.
- **Emission-model assumption discussion**: the guarantees of \citep{garcia2026grammar} attach to the stopping layer given calibrated emissions; $\tau$ supplies *deterministic* emissions, so this paper's coverage results inherit only the walk semantics — the honest dependency direction.
- TikZ figure: `fig_pipeline.tex` (three trace dialects → canonical events → walk → features → projection → coverage grid).

### `04_coverage.tex` (region coverage)
- Feature encodings: `grammar` features (walk length, duration, cycle depth, per-state visits, tool-call/error counts, terminal one-hot) and `bigram` features (first-$k$ transition histogram); z-normalization with zero-variance guard.
- Projection: PCA (power iteration + deflation) **fit on the real set only** — the behavior space is defined by production; sim points are projected into it (joint fitting would let the sim set move the axes). Determinism stated as a feature (no UMAP stochasticity; \citep{wildvis2024} contrast).
- Density: Gaussian-bump grid over the real cloud, box-blur smoothing; grid resolution $\rho$, bandwidth $\sigma = \beta\rho$; the shared relative threshold $\varepsilon \cdot \text{core}$ (99th-percentile-to-peak ratio) that defines occupancy for BOTH clouds — self-normalization would destroy relative magnitude, and the fix is stated.
- Coverage definitions: cell covered iff sim point inside OR sim kernel $\geq$ threshold; occupied = real cells above threshold; coverage \% overall + per outcome class; edge handling (skip-outside for sim: a sim point 10 extents away must not look like a corner point).
- **The recommendation loop**: top-$K$ uncovered cells by local real density, neighbor-deduped, each carrying its nearest real exemplar ("the tests you are not running"); turnaround: exemplar → simulator scenario seed.
- TikZ figure: `fig_coverage.tex` (real cloud → density grid → occupancy threshold → coverage count → uncovered cells with exemplar callouts).

### `05_atlas.tex` (the visualization layer + worked example)
- The atlas: one behavior plane, real = blue dots, sim = orange, uncovered = red cells with tooltips; designed for cross-model comparison — real logs and simulated runs may come from different vendors/models, legitimized by cross-model representation convergence \citep{layersSimilarDepths2025} and the trajectory-geometry vocabulary \citep{trajectoryGeometry2026}.
- Sim-vs-real reading: where the sim cloud concentrates (over-cooperative collapse, cf. \citep{realUserSim2026}, \citep{mirrorbench2026}), where it scatters, which real regions it misses entirely.
- **Worked example on shipped fixtures** (github.com/iamdgarcia/trace2grammar): 5 conversations across 3 dialects; sim set covers **40.2\%** of occupied real regions; per-class contained 45.3\% / handoff 35.2\%; top-3 uncovered with exemplar texts reproduced as a table.
- Relationship to the simulator program (a6): the atlas is where calibrated simulation is *validated* — region coverage is the headline metric; Wasserstein divergence of grammar-walk statistics (CDS-style, \citep{cds2026}) and rank correlation are the secondary instruments.

### `06_evaluation.tex` (protocol for a paper-grade result)
- **Transfer headline**: rank correlation (Kendall $\tau$ / Spearman $\rho$) of agent-policy scores computed on simulator-sim vs real-call evaluation — the sim2real transfer number the a6 RQ asks for.
- **Coverage sensitivity**: coverage as a function of grid resolution $\rho \in \{16, 24, 32, 48\}$, bandwidth $\beta \in \{0.08, 0.12, 0.20\}$, threshold $\varepsilon \in \{0.02, 0.05, 0.10\}$; report the stability envelope (the deterministic pipeline makes this sweep exact, not sampled).
- **Class-conditional coverage** for imbalanced classes (abandonment/fraud are rare; per-class coverage prevents the majority class from hiding the failure).
- **Baseline comparisons**: coverage under (i) random sim sampling, (ii) persona-only sim (no calibration), (iii) log-conditional sim (\citep{cue2026}-style embeddings as the conditioning signal) — the ladder that makes the metric meaningful.
- **Honest baseline vs future**: the deterministic feature baseline may under-measure semantic similarity (paraphrase pairs far apart); the MiniLM-embedding variant replaces only the feature step — flagged as the sensitivity study's companion, not shipped as the headline.

### `07_open_problems.tex`
- Learned emission mapper (replacing `infer_states()`; interface-stable); calibrated embeddings as features (\citep{cue2026}); coverage in higher dimensions (kernel two-sample tests instead of grid); closed-loop sim improvement (uncovered regions → generated scenarios); voice-physics channels (appendix spec of \citep{garcia2026grammar}'s `voice.*` extension).

### `08_discussion.tex`
- Limitations, honestly: rule-based state inference (misclassification propagates to walks — bounded by config exposure and the audit-overlay); 2-D projection discards variance (mitigation: coverage is computed on the projection, not claimed to be the full behavior space; PCA-basis-on-real is the design commitment); grid resolution is a hyperparameter (sensitivity protocol given); fixture-scale worked example (production-scale validation is the follow-up requiring log access); no human-subject data in this paper.
- Scope: any agent that emits the three formats (voice agents, chat agents, multi-agent) — the mapping is voice-agnostic by construction.

### `09_conclusion.tex`

---

## 3. Figures (TikZ only)

1. `fig_pipeline.tex` — extraction pipeline: 3 dialects → canonical events → walk → features → PCA → density grid → coverage.
2. `fig_coverage.tex` — the coverage geometry: real cloud, density grid, occupancy threshold, covered/uncovered cells, exemplar callouts.
3. `fig_atlas.tex` — the atlas concept: two clouds (real/sim), outcome-colored, uncovered regions marked; small multiples for per-class views.

---

## 4. Gap analysis box (why now)

> **Traces standardized, semantics absent.** OpenTelemetry's GenAI semantic conventions moved to their
> own repository and stabilized per-call span semantics through 2025–2026 (`invoke_agent`,
> `execute_tool`, Opt-In message events); OpenInference ships the most complete stable attribute
> spec; LangSmith/Langfuse exports are the de-facto evaluation-side artifacts. Yet the conventions
> deliberately stop at the operation level: `gen_ai.conversation.id` is a linking key, not a
> conversation object — the conversation-scale semantics (states, outcomes, drift) are left
> undefined by everyone.
> **Simulators became the evaluator, unvalidated.** The 2026 calibrated-simulation wave
> (\citep{sim2realAgentic2026}, \citep{distributionalGap2026}, \citep{cue2026}) measures response
> distribution agreement in text — response-level, response-level, and style-level respectively.
> The trajectory level — which conversation structures a simulator exercises and which it never
> does — is unmeasured everywhere.
> **The trace-mining wave mines for prediction, not semantics.** \citep{automataTraces2026},
> \citep{tracedance2026} and the attribution line (2608.06909, 2608.24361, 2609.32514) recover
> automata/graphs/benchmarks from traces but assign no conversation states, no outcome classes, no
> shared space where real and synthetic populations can be compared.
> **Nobody claimed the mapping.** Four alphaxiv scan rounds (agent-trace viz, user-sim fidelity,
> dialogue-flow viz, process mining) found no published trace→state-space mapping with outcome
> classes and no collection-level atlas comparing sim and real clouds by region. The grammar that
> gives the mapping its target vocabulary exists (\citep{garcia2026grammar}); the extraction layer
> is the missing bridge — and the region-coverage metric is the evaluation primitive the
> simulator-building community is currently missing.

---

## 5. Stage-1 gate self-assessment

**Gate: gap_score ≥ 4 and conceptual: true.**

- **Gap score: 5.** Four independent scan rounds confirm no published mapping from standard
  observability formats to a discrete conversation state space with outcome classes; no
  collection-level sim-vs-real atlas; the region-coverage evaluation primitive is unclaimed. The
  nearest neighbors each miss the claim on a different axis (prediction vs semantics; design-time
  vs distributional; response-level vs trajectory-level; corpus-level vs grammar-level).
- **Conceptual: true.** The contribution is a formal mapping + an evaluation protocol + a
  visualization/metric layer — extendable without new experiments (the shipped probe already
  demonstrates the pipeline end-to-end on fixtures; the worked example's 40.2% is real executed
  output, not a projection).
- **Honest risks recorded:** (i) the rule-based $\tau$ baseline invites the "just a heuristic"
  critique — answered by the config-exposure argument and the emission-model abstraction; (ii) the
  2-D projection is a design commitment with a sensitivity protocol, not a silently-lossy step;
  (iii) fixture-scale demonstration only — production-scale validation is explicitly the follow-up
  (log access is the blocker, as flagged in a6).

**Verdict: passes Stage-1 gates. Proceed to Stage 3.**

---

## 6. Stage-3+ execution plan

1. Copy `templates/arxiv_preprint/` → `papers/trace2trajectory/`; write `sections/01–09.tex` (one sentence per line; natbib `\citep/\citet`; TikZ figures `fig_pipeline/fig_coverage/fig_atlas`).
2. Compile gate: `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex` — 0 errors, ≤5 warnings.
3. Stage 4 review panel (chief editor + 4 reviewers); Stage 5 loop ≤5 rounds.
4. Stage 6: arXiv zip (`main.tex main.bib sections/ figures/`); cs.AI primary.
5. Companion artifact: the `trace2grammar` repo doubles as the paper's code release (MIT, clean-room verified).
