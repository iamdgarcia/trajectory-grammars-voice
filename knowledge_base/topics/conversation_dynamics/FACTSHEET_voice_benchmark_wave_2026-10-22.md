# Voice-agent benchmark wave: factsheet + adoption verdicts (2026-10-22)

*Method note (updated 2026-10-22 night, task t04-noche5-verify-bench): all 6 papers now
READ IN FULL. Abstracts via export.arxiv.org/api/query (id_list batch); full text via
arxiv.org native HTML (ar5iv not needed); raw dumps + extracted text at
`runtime/papers_noche5/` (fetch script `runtime/verify_bench_papers_noche5.py` +
`fetch_fulltext_noche5.py`, all through the local relay with added arxiv/HF allowlist
entries). Code-availability claims cross-checked live against the GitHub API the same
session. All `unread:` and `memory-sourced:` labels below have been lifted; every number
carries its section/table reference. One residual: DSB-IFEval and APEX-Voice describe
release artifacts in their reproducibility appendices but publish no download URL in the
paper; hosting remains unverified (marked per-entry).*

## 1. tau-Voice (2603.13686)

- Title (verified): τ-Voice: Benchmarking Full-Duplex Voice Agents on Real-World Domains.
- What it is (verified): voice extension of τ²-bench; 278 tasks across 3 domains (§4.1):
  Retail 114, Airline 50, Telecom 114. Deterministic pass@1 by comparing final database
  state against gold (§4.5). Controllable voice user simulator with decoupled simulation
  time (§3.2), Clean vs Realistic conditions (noise, diverse accents, frame drops, coughs/
  sneezes, LLM-based interruptions and backchanneling; §4.3, Table 4).
- Headline numbers (verified): text GPT-5 (reasoning) 85% vs best voice provider 51% Clean
  and 38% Realistic (xAI, Table 6, §5.1.1); voice agents retain only 30-45% of text SOTA
  capability. Google: 31% Clean / 26% Realistic; OpenAI: 49% / 35%. Voice interaction
  quality (Realistic, Table 8, §5.1.3): OpenAI best latency 0.90s, responsiveness 100%,
  interrupt 14%, but worst selectivity 6% (answers nearly all backchannels/tics); xAI best
  selectivity 57% but interrupt 84% (cuts users off nearly once per turn); Google 1.14s /
  69% / 21% / 54%. Qualitative analysis (§5.2, Table 9): 79-90% of failures stem from
  agent behavior (abstract; two raters, 84% inter-rater agreement, resolved to 100%).
- Code availability (verified OPEN): "Code is available at
  https://github.com/sierra-research/tau2-bench" (§1, contribution 1); repo live on GitHub
  API this session: public, 2,280 stars, pushed 2026-10-21. Paper states it is open-source
  and extensible (bring your own TTS/STT/agents/VAD, §6.1 Limitations discussion of
  extensibility in "Open and extensible" paragraph).
- Adoptability: event-driven-voice-orchestrator bench (32 invariants): CITE + SCENARIO
  IMPORT (code open; its Retail/Airline/Telecom task suite with deterministic DB-state
  checking maps directly onto our bench tool mock family). jev-mini-bench: CITE.
  trace2grammar coverage: CITE (domain taxonomy as coverage checklist; also its
  turn-taking metric set R_R/R_Y/L_R/L_Y/I_A/S_BC/S_VT/S_ND, §4.5, is a ready-made
  trace-observable event list).
- Risk (unchanged): tau-Voice targets full-duplex agents; our cascade bench is not
  directly comparable on headline pass@1.

## 2. DuplexSpeechBench-IFEval (2609.03423)

- Title (verified): DuplexSpeechBench-IFEval: Evaluating Implicit Instruction Following
  in Full-Duplex Voice Agents.
- What it measures (verified, §3.1): implicit instruction following in full-duplex
  interaction. Five conditioning levels L0-L4: bare assistant default, explicit
  behavioral instruction, persona-only (behavior must be inferred from the role),
  persona + entailed instruction, conflicting instructions (benign L4a / safety L4b).
  1,038 test cases from 240 controlled conversations, 8 behaviorally contrastive roles
  (§3.2, Table 30 composition: L0 48, L4a 240, L4b 30 cases; total 240×4+48+30=1,038).
- Metrics (verified, §4): Instruction Adherence Score (IAS), deterministic per-probe
  verifiers over two-channel audio for 9 floor-management actions (Listen, Backchannel,
  No-Backchannel, Interrupt, Take-Turn, Readback, Yield, Continue, Accept-Overlap);
  Persona Adherence Score (PAS), LLM-judged content consistency; Entailment Gap (L1-L2).
- Headline numbers (verified, §6): across 11 real-time speech systems (§5: GPT-Realtime,
  MiniCPM-o-4.5, Fun-Audio-Chat, PersonaPlex, F-Actor, Moshi, GPT-Live-1, Gemini-3.8-Live,
  StepAudio-3-Realtime, Nemotron-VoiceChat, Realtime-Venus-Audio). GPT-Live-1: 29.0 IAS at
  L0 → 43.2 with explicit instruction (L1) → only 36.1 when the same policy must be
  inferred from persona (L2). Gemini-3.8-Live: 29.0 → 32.5 (L1), 28.6 (L2): persona adapts
  dialogue language (PAS 32.8 → 66.8) without translating into floor behavior. F-Actor
  largest Entailment Gap +9.7pp. Safety conflict (L4b): NO system resolves in favor of
  safety persona in a majority of cases; best Fun-Audio-Chat 43.3%; L4b IAS falls to zero
  for most systems (§6.4).
- Code/data availability (verified: PROMISED, URL NOT FOUND IN PAPER): Appendix I
  ("Reproducibility and Release Checklist", Table 34) enumerates the full release
  (personas, scripts, WAVs, scorer, verifier thresholds, judge configs, adapters) and §A
  says annotations "will be released with the benchmark", but the paper contains no
  repository URL; GitHub/HF search found no official release this session. Do not claim
  downloadable until a URL exists.
- Adoptability: our artifacts: CITE only (we have no duplex speech model). Framing kept
  for trace2grammar: constraints as deterministic observable properties (their IAS
  verifiers are exactly per-probe trace assertions).

## 3. APEX-Voice (2609.34973)

- Title (verified): APEX-Voice: Can Voice Agents Complete Professional Workflows Through
  Full-Duplex Interaction.
- What it measures (verified, §3.1, §4): 120 interactive professional workflows, 10 work
  archetypes (form completion, negotiation, coordination, consulting, interviewing, ...),
  each characterized on 11 taxonomy dimensions (work archetype, industry, artifact,
  economic role, duplex phenomenon, delegation pattern, autonomy, knowledge burden, tool
  burden, user behavior, risk). Executed in a stateful "Voice Workbench" with typed tools,
  knowledge assets, authorization constraints, frozen Kokoro-synthesized user speech bank
  (§3.2). Metrics: Workflow Success (WS: terminal state + process validity + actions +
  valid artifact) and Artifact Field Accuracy (AFA) (§4).
- Headline numbers (verified, §6.1, Table 2, Table 3): across 5 frontier real-time agents
  (GPT-Live-1, Gemini-3.8-Live, Grok-Voice-Think-2.0, Step-Audio3, GPT-realtime-2.1): none
  exceeds 25% Pass@1 (best GPT-realtime-2.1 23.6%); best Reliable@3 only 10.8%; Grok
  Pass@3 41.7% but reliable-in-all-3 only 5.0%. Gate decomposition: Grok reaches Target
  State 99.4% of runs and GPT-Live-1 91.9% Process Validity, but Artifact Validity peaks
  at 35.3% (GPT-realtime-2.1): producing the valid final work artifact is the dominant
  end-to-end bottleneck. Text controls score ~54-62% Pass@1 vs 23.3% for the same agent
  in voice (Table 5).
- Code availability (verified: NOT PUBLIC): no repository URL anywhere in the paper (the
  abs page lists no code link); Appendix J describes the internal scripts
  (`scripts/run_step3_campaign.py`, `scripts/analyze_results_v1.py`) and a git-ignored
  secrets.txt, i.e. a real codebase, but GitHub search for "APEX-Voice"/"Voice Workbench"
  returns no official repo this session. HF papers entry has no githubRepo/projectPage.
- Adoption verdict: DOWNGRADED from RUN-CANDIDATE to CITE (decision 2026-10-22: its
  workflows do map conceptually to our bench tools, but without public code or workflow
  files there is nothing to run; re-check on camera-ready if a release URL appears). Its
  11-dimension taxonomy and gate decomposition (TS/PV/AC/AV) are a good coverage checklist
  for our orchestrator bench's failure-mode tagging. jev-mini-bench: CITE.

## 4. PACT-SLM (2609.38232)

- Title (verified): When Does a Spoken Agent Have Enough Evidence to Act? The PACT-SLM
  Contract Test.
- What it measures (verified, §3): a contract test for the decision to act under partial
  evidence: paired transcript-matched action contrasts (two utterances sharing transcript
  prefix, diverging in the action they justify), assigns the FIRST valid action time and
  scores action identity AND onset timing separately. Test split: 80 paired contrast
  groups from 4 held-out semantic families (book uncertainty, calendar noise, message
  barge-in, timer urgency; §3.3), 1,600 prefix predictions, clean + 15 dB noise. Corpus
  totals: 4,200 records from 680 source trajectories (208 train / 52 dev / 80 test
  groups).
- Headline numbers (verified, §5, Appendix G): WavLM Base+ probe reaches 26.03% pooled
  post-onset semantic-label accuracy (95% bootstrap CI [22.14, 29.68]), exposes an action
  on 18.99% of pre-onset prefixes, 5.94% complete-trajectory exactness. Elapsed-time
  features are more onset-exact (36.25% vs 23.13%) but worse on action identity (9.92%
  vs 26.03%). Pooled label score at the 96th percentile of within-prefix label
  permutations, just below the 97.5th significance reference (26.73%). Core finding (§5.1):
  action identity and onset timing are different capabilities and must be measured
  separately.
- Code/data availability (verified PARTIAL, probe set CLOSED): repo exists and is public:
  github.com/MENGZHEGENG/pact-speech-action-calibration (verified via GitHub API this
  session; created 2026-09-14, MIT license for prediction_replay/). BUT the README states
  explicitly it is a prediction-REPLAY package: it recomputes metrics from saved held-out
  predictions; it "does not regenerate speech, extract embeddings, fit the WavLM probe".
  The generated-speech probe set and embeddings are NOT released. So the probe family is
  not runnable as-is.
- Adoption verdict: DOWNGRADED from RUN-CANDIDATE to CITE + CONTRACT-IMPORT for
  jev-mini-bench (decision 2026-10-22): their probe DATA is closed, so no RUN; but the
  contract itself (paired contrast groups, first-valid-action-time assignment, separate
  identity-vs-onset metrics, group bootstrap) is fully specified (§3, Appendix G metric
  definitions) and small in shape; jev-mini-bench can implement the same contract over our
  own evidence-to-act task families. CITE in the decision-index writeup.

## 5. Speculative End-Turn Detector (2503.23439)

- Title (verified): Speculative End-Turn Detector for Efficient Speech Chatbot Assistant.
- What it measures (verified): end-turn detection (ETD): distinguishing turn completion
  from hesitation. Contributions: OpenETD dataset (first public ETD dataset: 120k+
  samples, 300+ hours; synthetic TTS on MultiWOZ split + real YouTube/Buckeye data; §3,
  §3.3) and SpeculativeETD, a two-stage cascade: on-device 1M-param GRU detects
  non-speaking units in real time; a server Wav2vec 2.0 classifies turn-end vs pause only
  when needed (§4).
- Portable metrics (verified, §5 "Evaluation"): yes, fully defined. Binary task:
  Precision / Recall / F1 / accuracy. Real-time segmentation: F1 evaluated at 100ms
  intervals + mean Intersection-over-Union over 3 classes (Speaking Unit, Gap, Pause),
  labeled by the 200ms rule (same-speaker silence = Pause, speaker change = Gap;
  Heldner & Edlund 2010 criteria). Both are directly importable into
  bench_turn_latency.py: our orchestrator's EOT decisions can be scored as binary ETD
  (F1/acc) and as segmentation F1@100ms/IoU against these class definitions.
- Headline numbers (verified, §6.1 Table, §6.3): wav2vec 2.0: 99.2 F1 synthetic / 75.2 F1
  real (81.2 acc); VAP 92.1 / 59.1; GRU 78.1 / 49.8. On-device GRU latency < 1ms per
  100ms interval on iPhone 12 mini via LiteRT (§6.3). Ablation (repo README):
  synthetic+real training beats real-only (F1 45.9 vs 38.7, IoU 32.3 vs 30.3).
- Code/data availability (verified: CLAIMED OPEN, LINK NOT WORKING): paper says the
  dataset is released ("we construct and release the OpenETD dataset, an open-to-public
  dataset", §1/§3) with code + download URLs for YouTube sources (§3.3). Reality this
  session: github.com/HJ-Ok/SpeculativeETD exists (verified via API, 1 star) but contains
  ONLY a README (dataset stats, hyperparameters, ablations) and figures: no code, no data
  links. Treat dataset as "announced open, hosting unverified".
- Adoptability: our bench: METRICIMPORT CONFIRMED (the metric definitions are portable
  and now pinned: binary F1 + segmentation F1@100ms + 3-class IoU). trace2grammar: CITE
  (the ETD decision is a trace-observable event; the 200ms Pause/Gap labeling rule is a
  grammar-ready predicate). Dataset RUN: blocked on hosting link.

## 6. FDBench v3 via Heartbeat (2610.26233)

- Title (verified): Heartbeat Thinking: Speculative Reasoning and Tool Execution While
  Listening in Realtime Voice Agents.
- VERIFIED FROM FRESH FETCH (2026-10-22, full text): the memory-sourced numbers are
  correct. On FDBench v3, speculative tool coverage (STC) increases from 34.67% to 50.67%
  (+16.00pp) over the SHANKS-style Window Thinking baseline (Table 1, §4.2; gains 10.56 /
  16.00 / 42.37pp on SpeechFCEval / FDBench / AudioCRAG). Mean final-response latency
  falls from 6.90s to 4.39s, a 36.4% cut, and is 45.7% below Pipecat, the fastest
  cascaded baseline (Table 5, §4.2 "Latency"). Task quality also improves on FDBench:
  Quality 72.0% → 77.0%, Pass@1 57.0% → 65.0% (Table 1 / Table 7). STC definition (§4.1):
  fraction of reference calls covered by completed matching speculative calls whose
  results enter the Responder context without repeated calls. Correct tool-call latency
  −4.37s (Heartbeat) vs −2.74s (Window) relative to speech end (Table 5).
- FDBench v3 provenance (verified, §B.2): FDBench v3 = Full-Duplex-Bench-v3 (Lin, Chen,
  Chen, Lee 2026, arXiv 2604.04847): 100 recordings, 79 scenarios, 12 speakers; tests
  turn taking, tool selection, argument accuracy, response quality, task success under
  disfluency; responses transcribed with Parakeet TDT 0.6B v2. Heartbeat setup: Qwen3.6-
  35B-A3B Thinker, DeepSeek-V4-Flash Responder, Δ=500ms, K=2.
- Label: memory-sourced label REMOVED; numbers now session-verified against the paper
  full text. (Note: 34.7/50.7 in the factsheet were rounded forms of 34.67/50.67.)
- Adoptability: unchanged and now evidence-backed: our conformance kit + Heartbeat
  baseline were annotated together (shelved Nov paper assets). We can COMPARE: restate our
  bench turn numbers in their protocol shape (STC + final-response latency relative to
  speech end). "The ONE benchmark worth adopting if the Nov paper revives" verdict holds.

## The ONE benchmark worth adopting if the Nov paper revives

**FDBench v3 (via Heartbeat 2610.26233), now fully verified.** Reasons: it is the
baseline we already annotated; it measures the speculative-listening regime our
event-driven topology feeds into; its numbers (STC 34.67→50.67, −36.4% latency) are
session-verified, so a comparison is quotable today; our bench numbers become a floor
comparison instead of an isolated claim. Runner-up changed: PACT-SLM is no longer a RUN
candidate (probe set closed), but its CONTRACT (paired action contrasts, separate
identity/onset scoring) is the cheapest thing jev-mini-bench can import.

## Adoption decision table (re-evaluated 2026-10-22 after full reads)

Adoption verdicts:
- tau-Voice: our bench CITE + SCENARIO IMPORT (code OPEN: sierra-research/tau2-bench,
  verified live); jev-mini-bench CITE; trace2grammar CITE (taxonomy + turn-taking metric
  set §4.5).
- DuplexSpeechBenchIFEval: CITE across all three (constraints as observables); release
  promised (Appendix I) but no URL: re-check before ever running.
- APEX-Voice: our bench RUN-CANDIDATE → CITE (downgraded 2026-10-22: no public code found
  in paper, abs page, GitHub, or HF metadata); its taxonomy + gate decomposition (TS/PV/
  AC/AV) adopted as failure-tagging checklist; re-check on camera-ready.
- PACT-SLM: jev-mini-bench RUN-CANDIDATE → CITE + CONTRACT-IMPORT (downgraded 2026-10-22:
  public repo is prediction-replay only, probe set closed); rest CITE.
- Speculative EOT Detector: our bench METRICIMPORT CONFIRMED (binary F1/acc + segmentation
  F1@100ms + 3-class IoU, §5); trace2grammar CITE (event type + 200ms Pause/Gap rule);
  dataset RUN blocked (hosting link unverified).
- FDBench v3: our bench COMPARE (verified numbers; adopt if Nov paper revives); rest CITE.

RESEARCH-BENCH COMPLETE: 6 (all verified full-read 2026-10-22)
