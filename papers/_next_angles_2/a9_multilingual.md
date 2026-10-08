# Spanish-First and Code-Switching Voice Agents: Multilingual Turn Policy

## Working title
*"No Language Left Listening: A Per-Class Turn-Policy Benchmark and the Code-Switch Turn-Boundary Problem for Spanish-First Voice Agents"*
(Alt: *"Endpointing the Switch: Language-Conditioned Turn Policies for Banking Voice Agents"*)

## Landscape
1. **Full-Duplex-Bench** (arXiv:2503.04721) — first full-duplex turn-taking/interaction benchmark; native-duplex models only, English-centric, no cascade, no Spanish slice.
2. **FDB v1.5** (arXiv:2507.23159) — adds overlap handling; same English full-duplex scope.
3. **FDB v2** (arXiv:2510.07838) — streaming speech-dialogue *simulator* feeding continuation audio; the mechanism our benchmark reuses, still no per-language or per-class labels.
4. **FDB v3** (arXiv:2604.04847) — tool use under disfluency; monolingual, native-duplex.
5. **FD-VAD** (arXiv:2609.35791) — strongest streaming semantic endpointer; explicitly English-only (smart-turn-v3.1 training), GPU-bound, binary stop/continue with no policy classes and no Spanish evaluation.
6. **Smart-Turn (Pipecat)** (open-source, production EOT, ~146 ms p50; verified in local KB) — deployed audio endpointer; per-language accuracy numbers unpublished [verify].
7. **Moshi** (arXiv:2410.00037 [verify]) — full-duplex speech foundation model; English+French-centric, no published turn-policy metrics per language.
8. **mmBERT** (arXiv:2509.06888; verified in local KB) — 1800+ language encoder under 300M params; the natural CPU-cheap backbone for a multilingual text-side veto.
9. **Commercial endpointers** — Deepgram Flux, OpenAI Realtime, ElevenLabs (local KB anchors): multilingual *claims*, zero per-language, per-class operating-point evidence.
10. **Cross-cultural turn-taking** — Stivers et al. 2009 (PNAS) includes Spanish in the 10-language ~200 ms gap study; Levinson & Torreira 2015 anchor τ_human. Code-switching as an interactional device: Auer 1984/1998 (books, no arXiv) — switches cue stance and boundary, never formalized for endpointing.
11. **Code-switch ASR context** — SEAME (LDC2009S17, Mandarin-English) is the classic CS benchmark; Spanish-English (Miami Bangor, BanCS) has no turn-policy labels; recent Whisper CS-failure studies exist but are ASR-WER only [verify].

## The gap
**RQ1 (our SV2, now sharpened):** Do open and commercial endpointers degrade on Spanish hard cuts and Spanish-English code-switched banking speech, per class (take-floor / backchannel / side-talk)? Nobody publishes per-language, per-class numbers in *any* language; our own ES text-only turn-end sits at 0.40-0.54 (near chance), and FD-VAD leaves ES untouched. **RQ2 (unformalized):** What *is* a turn boundary under code-switching? A mid-turn ES→EN switch ("…y el saldo de mi **checking account**…") is acoustically pause-adjacent and lexically discontinuous: monolingual endpointers plausibly misread switch points as turn ends, and interim ASR transcripts are least mature exactly there (Whisper repetition/hallucination at switches). No formal model defines when a language switch is turn-internal vs turn-final, nor the false-EOU floor it induces. Testable: (a) measure endpointer false-EOU rate at switch points vs within-language pauses; (b) show a language-conditioned policy (per-language operating points + switch detection) beats any single English-tuned operating point; (c) derive the switch-induced false-EOU bound as a function of switch-point pause statistics (extension of our latency-floor decomposition: language-conditioned δ_EOU term in Λ*).

## Candidate contribution
1. **CS-TurnBank**: first multilingual (ES, EN, ES-EN code-switch) turn-policy benchmark with three-class labels (take-floor/backchannel/side-talk), banking-vocabulary domain, simulator-driven continuation audio (FDB v2 mechanism), frozen-hash release — scaling our published frozen 100-phrase ES methodology.
2. **Code-switch turn-boundary formalization**: switch points as a boundary event class; ambiguity set over (pause, prosody, language-switch) evidence; a false-EOU lower bound for monolingual policies on code-switched speech, reusing our reducible/irreducible decomposition.
3. **Language-conditioned turn policy**: per-language operating points for one shared detector (mmBERT-class encoder + two-question veto framing), with the veto-only result from our ES benchmark as the Spanish prior.

## Reuse of our published results
- **Paper 3 (Asking Instead of Listening)**: the ES near-chance text-only turn-end measurement (0.40-0.54), barge-in veto F1 0.76, and cloud p99 178-268 ms become the Spanish baseline slice and the policy's text-side veto layer; its frozen-benchmark protocol becomes the labeling/release recipe.
- **Paper 1 (Latency Floor)**: Λ* machinery absorbs a language-conditioned endpointing delay term — code-switch speakers buy back latency only if per-language δ_EOU is measured; the k-step ReAct bound is unchanged.
- **Paper 2 (Cessation Floor)**: barge-in detect/decide/cease/resume applies to code-switched mid-utterance barge-ins, where the backchannel inventory differs ("sí sí sí", "claro", "dale") — the veto's precision requirement is per-language, and our asymmetric-cost framing carries over unchanged.

## Banking grounding
Spanish-first production system (iabto-ms-bc) makes this the program's most deployable angle: (i) real US-Hispanic/remittance calls code-switch mid-call, typically to English for account numbers, card products, and technical terms — exactly where endpointing errors trigger wrong tool dispatches (account lookup, card block) that waste real core-banking round-trips (SV5 link); (ii) compliance: recorded disclosure scripts and fraud-verification flows must not be cut mid-readout; a false turn-end during a CLABE/card number prompts re-prompting and re-verification; (iii) dialect spread ("vale" Spain vs "dale"/"órale" LatAm) changes backchannel distributions → per-language, per-dialect operating points are a production requirement, not a nicety; (iv) telemetry: per-language perceived V2V and barge-in reaction (OG5 protocol) are directly measurable in the existing GKE pipeline.

## Scores
- **Novelty: 4** — first multilingual per-class turn-policy benchmark + first code-switch turn-boundary formalization; turn-taking itself is crowded and multilingual full-duplex models are multiplying.
- **Fit: 5** — executes SV2 (gap_score 5, explicitly tagged as ours) plus the code-switch formalization named in the discovery brief.
- **Banking: 4** — Spanish-first production grounding, fraud/compliance cost story, but the benchmark is domain-neutral in core design.
- **Feasibility: 4** — benchmark recipe, veto design, and latency rig all exist from Paper 3; heavy part is labeled code-switch data (synthesized + scripted bilingual set, small real set).
- **Risk: 2** — main risks: reviewers demanding real bilingual recordings (mitigate with a small real seed set) and commercial endpointers silently handling ES well (unpublished = still a gap; measuring it is the contribution).

## Verdict
**Pursue now.** Highest-gap open item in the KB (SV2), directly reuses all three published papers' machinery, and the production Spanish-first system gives exclusive data access competitors lack. Do a 2024-2026 arXiv sweep for "code-switch turn-taking" and "multilingual end-of-turn" before writing the outline.
