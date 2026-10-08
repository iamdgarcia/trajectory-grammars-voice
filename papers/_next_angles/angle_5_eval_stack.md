# Research: Evaluation & Benchmarks for Realtime Agentic Systems

**Angle scoped:** the fragmented state of realtime-agent evaluation — latency-only reporting, no cost-per-turn under an SLA, no standardized "responsiveness" metric across cascade / full-duplex / streaming-tool pipelines, and no PRISMA-style minimum reporting standard.

---

## 1) LANDSCAPE

1. **Serving-layer LLM latency benchmarks** — TTFT/TPOT/end-to-end logging (DistServe, Splitwise, SGLang/Sarathi, MLPerf inference; vendor indexes like Artificial Analysis): precise text-level latency metrics, but no audio, no turn-taking, no agent loop, no quality-attached latency. [DistServe arXiv:2401.09670]
2. **Offline/batch agent task benchmarks (success-only)** — AgentBench, GAIA, SWE-bench, WebArena, τ-bench: measure task success / trajectory quality on fixed episodes; interactivity, per-turn latency, and cost under time pressure are deliberately stripped out. [AgentBench arXiv:2308.03688]
3. **Spoken-dialogue turn-taking & endpointing evaluation** — Raux (LISTEN/LEAP, SIGDIAL 2006; endpointing-threshold optimization 2008), Skantze 2021 survey, Schlangen's incremental-processing models: the only tradition that measures *turn timing quality* (floor conflicts, endpointing errors, incremental latency), but as per-system lab methodology with no cross-architecture standard. [Skantze 2021 CSL 101178]
4. **Human conversational timing & acceptance thresholds** — Levinson & Torreira 2015 (~200 ms human-human inter-turn), Stivers et al. 2009 (cross-cultural universals), Shiwa et al. 2008 HRI ("minimum acceptable response time" ~600 ms, 1 s+ judged slow): a *family* of context-dependent thresholds, not a single number — yet papers keep citing one.
5. **Speech/audio quality evaluation** — MOS via ITU-T P.800/P.808/P.85, P.863 (POLQA), neural MOS (NISQA/DNSMOS): mature, standardized, but purely quality-of-audio; no responsiveness or interaction dimension.
6. **Web responsiveness standards** — Google RAIL model, TTFB, Core Web Vitals with INP ("Interaction to Next Paint") replacing FID in 2024: the field's closest precedent for a *standardized, user-behavior-anchored responsiveness metric* that speech/agent evaluation lacks.
7. **Cost–latency–accuracy joint reporting** — HELM's efficiency metrics and cross-model standardization plus blog-scale cost/latency Pareto charts (Artificial Analysis, vendor price-per-minute): proves joint reporting is feasible and valued, but informal and not defined *per turn under a latency SLA*.
8. **Safety-evaluation standardization crisis** — HarmBench, StrongREJECT, Garak; meta-analyses showing 23/25 claims refuted as thresholds/prompts/templates shift: an adjacent "eval reproducibility" gap (our own KB Gap G4) that has already produced minimum-reporting-standard calls in the safety literature, with no realtime-agent analogue.
9. **Vendor realtime-voice product claims** — native voice / Realtime SDK latency and "full-duplex" marketing (Moshi latency analysis, Gemini Live, OpenAI Realtime): self-reported means with unreported percentiles and alignment conventions — exactly the measurement non-comparability this angle is about.

## 2) THE GAP

**Most promising unfilled gap — stated as a testable research question:**

> RQ: Can a small, standardized, architecture-agnostic responsiveness metric stack — (a) silence-gap distribution against an explicitly stated per-task SLA, (b) floor-conflict / endpointer-error rate, (c) cost-per-successful-turn at a stated latency percentile, and (d) guardrail-latency overhead — be applied to cascade, full-duplex, and streaming-tool pipelines on a canonical task set with inter-lab measurement agreement, and does it meaningfully separate the three architecture classes at the latencies our Latency Floor model predicts?

**Why it is not already solved:**
- Three disjoint communities measure three disjoint things — serving-latency (TTFT), SDS turn-taking (floor conflicts), agent quality (task success) — with no shared metric vocabulary, so no single result answers "is this realtime agent good?".
- **No SLA convention:** papers/vendors report mean silence gaps or TTFT without a stated acceptable-latency budget, so "good" is undefined; our own paper's 200 ms τ_human is a human–human *norm* (Levinson) and machine tolerance is empirically higher and task-dependent (Shiwa HRI ~600 ms) — nobody has standardized an acceptance threshold per task.
- **No PRISMA-style minimum reporting standard** for empirical realtime-agent papers: no consensus on gap-vs-GPT-alignment origin points, mean-vs-p95, VAD/EOU parameters, or which cost denominator (per turn, per completed turn, per 1k audio-seconds). PRISMA exists for systematic reviews; HELM exists for text models; nothing exists for realtime voice/agent empirics — confirmed in the guardrail KB too (G4 is the same disease in the safety literature).
- Self-reported vendor latency is not reproducible; reproducing the safety-eval meta-finding (1 arXiv survey found ~23/25 empirical claims refuted on re-measure) would be cheap for latency claims, which is exactly why a reporting standard is a defensible, high-citation contribution.

## 3) CANDIDATE CONTRIBUTION

**"The Realtime Agentic Evaluation Stack (RAES)"** — a 3-part, publishable deliverable:

1. **Formal metric vocabulary + measurement protocol.** Precision definitions and measurement rules for: *responsiveness* (time-to-first-audio TTFA, silence-gap distribution: mean/p50/p95/p99 vs declared SLA τ_SLA, floor-conflict / barge-in rate, endpointer-error decomposition into false-EOU and missed-EOU — reusing Raux's endpointing-errors framing); *quality* (task success + a MOS-lite audio-quality score); *economy* (cost-per-turn and cost-per-successful-turn at a stated latency percentile — "cost under SLA" as the unifying quantity); *safety* (guardrail-latency overhead, prefix-safe generation rate — plugs directly into KB Gap G1).
2. **A PRISMA-style minimum reporting standard** — a compact 8–12 item checklist (e.g., "MERREAL: Minimum Evaluation & Reporting for REaltime Agent Latency") with a fill-in reporting-table template: SLA and threshold source, gap alignment definition, EOU/VAD parameters, percentile stack, dataset/task set, cost per 1k turns, hardware/API, inter-lab instruction. This is the standardization artifact the field demonstrably lacks.
3. **A reference benchmark + leaderboard seed** — 3 architecture classes (legacy EOU-gated cascade, streaming cascade, full-duplex native) × 3–5 canonical tasks (factoid, multi-step tool use, interruption/barge-in stress) with the RAES metric stack pre-measured, published as a reproducible baseline + public table.

**Working title:** *"Measuring Responsiveness: Toward a Standardized Evaluation Stack for Realtime Agentic Systems"*
(Alt: *"The Realtime Agentic Evaluation Stack: Latency, Quality, Cost, and Safety Under an SLA."*)

## 4) EXTENSION ANGLE

Reuse the published Latency Floor machinery as the **theory the benchmark is built to empirically validate** — this makes the next paper visibly extend, not repeat, the last one:

- For each architecture class we already derived closed-form floors: EGC sum Λ* = Σλ_irr; streaming cascade Λ*_SC = δ_N + α·|C_residual| + λ_lm,decode,irr + λ_tts,irr; native buffer-and-commit; native streaming-causal ≈ 160 ms. The RAES benchmark's headline sanity check becomes: **do observed silence-gap percentiles track the predicted Λ* per architecture, and what fraction of turns satisfy the CCC (Λ ≤ τ_human = 200 ms)?** Our theory predicts the ordering; the paper gives the first standardized measurement that confirms (or refutes) it across the three classes — turning the CCC into an empirical *compliance metric* with a δ_N→WER acknowledgment from Corollary (streaming-CCC) as a built-in quality check.
- Extend the reducible/irreducible decomposition to *measurement validity*: decompose each reported gap into irreducible + reducible + "measurement artifact" (start-of-speech alignment, VAD window, TTS prefix flush), so RAES includes a validation appendix that is itself an instance of our own λ^r/λ^irr taxonomy applied to the measurement process, not just the pipeline.
- **Two-way bridge to the guardrail gap:** insert a guardrail stage into the DAG (λ_guard between LM and TTS) — our model then predicts how much a streaming-safe guardrail (KB Gap G1) costs in silence-gap headroom; RAES makes that guardrail-latency-overhead and cost-per-turn-under-SLA measurable for the first time, co-closing KB Gaps G1 (streaming-safe guardrails) and G4 (eval standardization).

## 5) ANCHORS

1. **Levinson & Torreira 2015, *Timing in Turn-Taking*, Frontiers in Psychology 6:731** — the 200 ms inter-turn norm underwriting our τ_human and CCC; must-cite as the perceptual anchor RAES turns into a per-task SLA. (journal, no arXiv)
2. **Stivers et al. 2009, *Universals and Cultural Variation in Turn-Taking*, PNAS 106(26):10587** — cross-cultural ~200 ms universality; defends using τ_human as a general rather than Weiß-only threshold.
3. **Skantze 2021, *Turn-Taking in Conversational Systems and HRI*, Computer Speech & Language 67:101178** — the authoritative survey of turn-taking evaluation (floor conflicts, response timing, endpointing) in systems; the natural citation declaring the "no standard" gap we fill.
4. **Raux & Eskenazi 2008, *Optimizing Endpointing Thresholds using Dialogue Features*, SIGDIAL** — defines endpointing error regimes (false-EOU / missed-EOU) and their latency cost; our endpointer-error decomposition reuses this as a first-class RAES metric. (conference paper)
5. **Shiwa et al. 2008, *In a Right Mood? Minimum Acceptable Response Time in Human-Robot Interaction* — HRI 2008** — empirically shows machine-facing acceptance thresholds (~600 ms acceptable; >1 s slow) differ from the 200 ms human-human norm; the load-bearing citation for our claim that a *single* τ_human is insufficient and standardized per-task thresholds are needed.
6. **Liang et al., *Holistic Evaluation of Language Models (HELM)*, arXiv:2211.09110** — precedent that cross-model standardized evaluation is possible and citable, including an efficiency (inference cost) axis — the template for RAES's cost-under-SLA reporting.
7. **Page et al., PRISMA 2020, BMJ 372:n71** — the canonical reporting-standard artifact; the explicit analogy for our minimum-reporting checklist (the "PRISMA for realtime-agent empirics" argument).
8. **Zhong et al., *DistServe: Disaggregating Prefill and Decoding*, arXiv:2401.09670** — represents the serving-latency community's TTFT/TPOT metric standardization, which stops at the text/HTTP layer and never reaches audio or the agent loop — the boundary RAES must cross.

---

**Sources consulted (repo):** `papers/cascade_voice_latency/OUTLINE.md`, `sections/01_introduction.tex`, `sections/04_latency_floor.tex`, `sections/06_design_levers.tex`, `sections/07_open_problems.tex`, `main.bib`; `knowledge_base/topics/ai_guardrails/gaps.md` (G1 streaming guardrails, G4 eval standardization).
**Web round (this sandbox has no live web_search tool):** anchors above are from domain knowledge; verify the 3 non-arXiv IDs (Skantze CSL 101178, Raux SIGDIAL, Shiwa HRI) and both arXiv IDs (2211.09110, 2401.09670) against the venues before submission.

## Gaps

- **No live web verification** in this run: citation existence/venue details for anchors 3, 4, 5, 7 and both arXiv IDs should be re-checked with a real search before the bibliography is finalized (severity: medium — a wrong ID is a hard reject under peer review).
- Not confirmed live: whether a competitive/comparable "realtime agent eval" benchmark has been released in the last few months (the space moves fast; a sweep of arXiv CS.CL/CS.LG for "realtime agent benchmark" 2024–2026 is the recommended follow-up).
- Not sourced: quantitative evidence of how vendor "latency" numbers are computed (informal blogs only) — worth one focused scrape of OpenAI/Gemini/Moshi latency write-ups to cite as the "non-comparable reporting" smoking gun.
- GODEL/MultiWOZ-style dialogue-quality metrics were assessed as in-scope but secondary; excluded to keep RAES contribution sharp.

**Suggested next step for the parent:** a follow-up worker with live web access to (1) verify the 8 anchors, (2) run a 2024–2026 arXiv sweep for competing realtime-agent evaluation benchmarks, (3) pull 3–5 vendor realtime-SDK latency claims to quote as non-standardized reporting examples.
