# Voice-Channel Fraud & Security in Conversational Banking (two-sided, latency-bounded)

## Working title
**"The Security Floor: Two-Sided, Latency-Bounded Defense of the Conversational Banking Voice Channel"**
(Alt: *"Fraud on the Clock: Vetoes, Deepfakes, and Irreversibility Gates for Spanish Voice Banking Agents."*)

## Landscape
1. **Audio deepfake / spoof detection (ASVspoof 5, 2024)** — crowdsourced data + adversarial attacks + real variability; the benchmark line for attacker-side voice cloning, but all offline scoring, zero dialogue context. [arXiv:2408.08739 [verify]]
2. **AASIST (ICASSP 2022)** and the wav2vec2-ADD lineage (Tak et al., Odyssey 2022, arXiv:2202.12233 [verify]) — SOTA anti-spoofing architectures; per-utterance classifiers, no streaming/latency guarantees, no conversation.
3. **Audio adversarial examples (Carlini & Wagner, 2018)** — imperceptible perturbations flip ASR/speech-model outputs; the acoustic ancestor of prompt injection arriving via audio. [arXiv:1805.11478]
4. **DolphinAttack (CCS 2017)** and Hidden Voice Commands (USENIX Security 2016) — inaudible/ultrasonic command injection: the voice channel carries commands the human interlocutor never hears.
5. **InjecAgent (2024)** — indirect prompt injection against tool-integrated agents; the text-only analog of what lands in a banking agent's tool DAG via audio. [arXiv:2403.02691]
6. **AirGapAgent (CCS 2024)** — context isolation/data minimization for privacy-conscious conversational agents; the closest existing "voice-agent security systems" work, but privacy-scoped, no fraud, no latency model. [arXiv:2402.10235 [verify]]
7. **LLM-scaled social engineering (Hazell, 2023)** — LLMs industrialize spear phishing and pretexting; attacker capability anchor. [arXiv:2305.06972]
8. **Voice cloning at 3 s of speech (VALL-E, 2023)** — deepfake caller identity is now cheap; authentication-in-dialogue cannot rest on caller voice alone. [arXiv:2301.02111]
9. **Dialog guardrails (NeMo Guardrails arXiv:2310.10501; Llama Guard [arXiv:2312.06674 [verify]])** — our KB Gap G1 already establishes none are streaming-compatible; no one prices them against a 200 ms deadline.
10. **Real-world grounding (non-academic)** — Arup's ~$25M deepfake video-call heist (news, 2024); STIR/SHAKEN (RFC 8224) authenticates the telephony hop but nothing above it; SEPA instant payments settle in seconds [verify], so fraud decisions have hard external deadlines.

## The gap
**RQ (testable):** Can a cascade conversational-banking voice agent defend a two-sided threat model — attacker-borne inputs (audio prompt injection, deepfake caller, homophone instruction smuggling) and victim protection (scam-coercion signals: urgency, secrecy, payment compliance) — such that all security decisions (a) run **asynchronously as vetoes** inside the pipeline's reducible-latency headroom (preserving the CCC), (b) **gate only at irreversible tool calls** (payments), and (c) measurably cut attack success and scam-completion by ≥10× at ≈0 added perceived latency?

**Why unsolved:** three disjoint literatures own three disjoint slices and none talks to the others. Deepfake/anti-spoof detection is per-utterance, offline, dialogue-blind. Prompt-injection work is text-only, tool-blind to real core-banking backends. Fraud/scam analytics run batch over call logs, never mid-conversation, never under a deadline. Nobody treats the channel as a *two-sided* problem in one decision layer, and nobody has connected security latency to a response-floor model — our KB Gap G1 (no streaming-safe guardrails) is exactly this disease on the text side; the voice side adds audio-borne injection and a victim under coercion.

## Candidate contribution
A conceptual/framework paper in the floors program's style:
1. **Threat taxonomy for the banking voice channel** — attacker-side (deepfake identity, audio-borne injection incl. Spanish homophones and background speech, social engineering *through* the victim) × victim-side (scam coercion), mapped onto pipeline stages (ASR text → orchestration → tool call → TTS).
2. **Security-floor lemma set** — inherit Λ* decomposition: any *blocking* security check adds to the onset floor and violates the CCC ⇒ in-conversation security must be **veto-only and asynchronous**; reuse the cessation paper's **execution-persistent** class to define the **irreversibility gate**: the only mandatory blocking point is pre-dispatch of irreversible tools (transfer, card unblock, credential change). Fraud policy composes with OG3's typed tool DAG (gate placement = which tools are type-A-irreversible).
3. **Benchmark design** — Spanish synthetic vishing corpus with labeled scam signals + injection audio (homophone/code-switch/background-speech variants) + deepfake segments; metrics: detection F1 *at latency percentiles*, injection-driven-action success rate, task success under defense. (jev-vad's frozen 100-phrase methodology scales to this.)

## Reuse of our published results
- **Paper 1 (latency floor, τ_human, Λ*)**: the deadline frame — security must be hidden in reducible latency; new lemma family mirrors the onset-floor proof.
- **Paper 2 (cessation floor, generation-interruptible vs execution-persistent)**: the irreversibility gate is a direct re-application — payments are the execution-persistent class; "stop the payment" barge-in must also respect cessation bounds.
- **Paper 3 (two-question semantic VAD, veto-only, p99 178–268 ms)**: the veto pattern generalizes from turn-policy to fraud-policy over the same interim transcripts; cloud-latency evidence transfers directly.

## Banking grounding
Intrinsic: payments are irreversible tool calls against real core-banking backends; PSD2 SCA forces authentication-in-dialogue without killing latency [verify regulatory framing]; Spanish-first means homophone/code-switch injection and Spanish vishing scripts are first-class; production telemetry from the deployed pipeline gives real latency operating points for the budget claims.

## Scores
- **Novelty: 4** — deepfake detection itself is crowded, but the two-sided, latency-bounded, banking-channel frame with an irreversibility gate is unclaimed.
- **Fit: 5** — pure extension of the floors program (deadline + veto + execution-persistence + tool DAG); reuses all three papers' machinery.
- **Banking: 5** — fraud, payments, SCA, Spanish; the production system is the testbed.
- **Feasibility: 4** — conceptual + formal core is safe; the benchmark needs synthetic corpus construction (proven pattern, real effort).
- **Risk: 3** — threat-model papers can drift hand-wavy (mitigate with lemmas + measurable RQ); ADD literature could subsume the deepfake slice if we claim detection rather than integration.

## Verdict
**Pursue now** — highest banking fit of any open angle; the deadline/veto/irreversibility frame converts a sprawling security topic into a compact floors-program paper, and the benchmark it seeds (Spanish vishing + injection) is a durable asset for every later safety paper.
