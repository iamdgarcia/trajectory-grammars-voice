# Standardized Evaluation Stack for Realtime Agentic Voice — Deadline-Conformance Refresh

## Working title
*"Deadlines, Not Means: A Deadline-Conformance Evaluation Standard for Cascade Voice Agents"* (alt: *"Measuring Responsiveness Under Floors: A Compliance Metric for Realtime Agentic Voice"*)

## Landscape (10 anchors)

1. **Full-Duplex-Bench** (arXiv:2503.04721) — turn-taking/overlap eval for native full-duplex S2S models; cascade pipelines explicitly out of scope. [VERIFIED in KB]
2. **FDB v1.5** (arXiv:2507.23159) — overlap-handling refinements; still native-model-only, outcome metrics. [VERIFIED in KB]
3. **FDB v2** (arXiv:2510.07838) — streaming speech dialogue simulator for multi-turn duplex eval; simulator idea reusable for cascades, floors absent. [VERIFIED in KB]
4. **FDB v3** (arXiv:2604.04847) — tool use under real disfluency for full-duplex agents; no cascade, no Spanish, no component-level decomposition. [VERIFIED in KB]
5. **IHBench** (arXiv:2606.19595) — post-interruption recovery in structured workflows; measures outcomes, not cessation reaction latency or floors. [VERIFIED in KB]
6. **FD-VAD** (arXiv:2609.35791) — best endpointer eval line (smart-turn, TurnBench); component-level but single-stage, English, GPU-only; TurnBench itself unverified. [VERIFIED in KB; TurnBench ID: verify]
7. **τ-bench** (arXiv:2406.12045) — text-domain liveness + price axes under latency budget; no voice, no turn-taking, no audio alignment conventions.
8. **HELM** (arXiv:2211.09110) — standardized multi-axis eval incl. efficiency; the precedent that cross-model standardization is publishable, text-only.
9. **Skantze 2021** (Computer Speech & Language 67:101178) — authoritative declaration that turn-taking/latency evaluation has no standard across systems. [verify venue string]
10. **Levinson & Torreira 2015** (Frontiers in Psychology 6:731) — τ_human ≈ 200 ms anchor; Shiwa et al. 2008 (HRI, ~600 ms machine tolerance) shows per-task thresholds, not one number. [verify Shiwa]

**Refresh verdict on the question asked:** the 2025-2026 wave (FDB ×4, IHBench, FD-VAD/TurnBench) is real and fast-moving, but it uniformly targets **native full-duplex S2S models and outcome metrics**. There is still no component-level, cascade-aware, deadline-based standard: nobody evaluates cascade components against formal floors, nobody standardizes gap-alignment conventions and percentile reporting, and perceived-V2V / barge-in reaction latency remain unmeasured anywhere (KB OG5).

## The gap

**RQ:** Can *deadline conformance* — pass/fail of measured latency percentiles against explicitly declared floors (onset Λ*, cessation floor, tool-budget bound) — be standardized as an evaluation primitive for cascade voice agents, with a measurement-validity taxonomy that separates irreducible, reducible, and **measurement-artifact** latency (start-of-speech alignment, VAD window, TTS prefix flush), and validated by replication on a published reference harness?

**Why unsolved:** three communities measure three disjoint things (TTFT serving-latency; floor-conflict lab dialogue; task-success agent benchmarks); no shared metric vocabulary or minimum-reporting checklist exists for realtime voice empirics (the G4 disease, now in eval rather than safety). Benchmarks that appeared in 2025-2026 crowded the *outcome* space for native models while leaving cascade *floors* untouched — including our own production telemetry gap: server V2V is logged, audible latency and stop-reaction are "nadie" (OG5).

## Candidate contribution

1. **Measurement-validity taxonomy** — extend the published λ^reducible/λ^irreducible decomposition to the *measurement process itself*; every reported gap becomes floor + improvement + artifact, with alignment conventions defined once.
2. **MERREAL minimum reporting standard** — 8-12 item checklist + fill-in table (SLA source, gap alignment, VAD/EOU parameters, percentile stack p50/p95/p99, cost denominator, hardware/API, Spanish/language breakdown), PRISMA-style (Page et al., BMJ 372:n71 [verify]).
3. **Deadline-conformance reference benchmark** — 3 architecture classes (EOU-gated cascade, streaming cascade, native full-duplex) × deadline classes (τ_human factoid; tool-budget turn; compliance-utterance class with zero-misclassification), reporting CCC pass-rate, cessation latency, cost-per-successful-turn-under-SLA. Seed leaderboard from our PoC telemetry (cloud p50 101-187 ms, p99 178-268 ms).

## Reuse of our published results

- Latency floor theorem (Λ*) and k-step ReAct bound = the deadlines the benchmark tests; streaming-CCC corollary (δ_N vs WER) = built-in quality gate.
- Cessation floor (detect/decide/cease/resume; generation-interruptible ∩ execution-persistent) = the second headline metric family; IHBench becomes the outcome-side comparator.
- "Asking Instead of Listening" (DOI 10.5281/zenodo.23233331) latency tables = seed cascade measurements; veto-only operating point = an evaluated policy component; Spanish negative result (turn-end 0.40-0.54) motivates mandatory per-language reporting.

## Banking grounding

- **Containment rate & abandonment** as the business axes a latency deadline miss moves (miss → silence/over-talk → abandonment → human-transfer cost); the eval stack must carry them, not just ms.
- **Compliance-critical utterances** (amounts: "cinco"/"quince"; disclosures; fraud warnings) as a deadline-privileged, zero-error class — a mis-timed turn on a confirmation is a compliance event, not a UX blemish.
- **Spanish-first:** SV1's near-chance text-only turn-end in ES makes per-language percentile reporting non-optional; Spanish is the lead language of the harness.
- **Real tool backends:** cost-per-successful-turn priced at ~1 s core-banking RTT (OG3) instead of toy mocks; production telemetry vocabulary (perceived-V2V, barge-in reaction) straight from OG5's `docs/bench/medicion-latencia-v2v.md`.

## Scores

- **Novelty: 4** — eval space is crowding fast, but the cascade/deadline/artifact axis is still empty; window is 12-18 months.
- **Fit: 4** — capstone of the floor program (OG5 + G4); visibly extends both published papers rather than repeating them.
- **Banking: 4** — containment/abandonment/compliance classes are the real KPIs; author has production telemetry to seed it.
- **Feasibility: 3** — rig exists, but credible standardization needs inter-lab replication or at least a scrape of vendor latency claims as non-comparability evidence.
- **Risk: 2** (low) — even a negative result ("floors don't separate classes in practice") is publishable; main threat is being scooped on generic leaderboards, not on deadline-conformance.

## Verdict

**Pursue now**, repositioned: lead with *deadline conformance + measurement validity for cascade voice*, not a generic eval stack — the generic leaderboard space is filling (FDB line, IHBench, TurnBench), the floors-and-artifacts space is not. Pair with a targeted scrape of OpenAI/Gemini/Moshi latency claims as the reporting-non-comparability smoking gun.

## Gaps

- No live web verification this run: VoiceBench (2410.17196), TurnBench (Jiang et al. 2026), Skantze CSL string, Shiwa HRI 2008, PRISMA 2020, τ-bench authorship — mark [verify] and confirm before bibliography. Severity: medium.
- Whether any 2026 Q4 preprint already extends FDB to cascade pipelines could not be confirmed; one arXiv sweep ("cascade latency benchmark", "voice agent deadline evaluation", 2026) before writing is the recommended next step.
