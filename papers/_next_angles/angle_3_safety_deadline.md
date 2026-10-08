# Research: Safety & Guardrails Under Realtime Deadlines for Voice Agents

Discovery brief for the NEXT paper. Angle: streaming/prefix-safe safety classification, guardrail placement inside the cascade-pipeline DAG, latency-aware safety budgets, and realtime jailbreak/red-teaming — for the cascade-vs-full-duplex voice-agent setting of our published `cascade_voice_latency` paper. Grounded in local KB (`knowledge_base/topics/ai_guardrails/`) plus literature knowledge; see Gaps for a citation-verification caveat (no live web tool in this run).

---

## 1) LANDSCAPE

1. **Full-response content classifiers** — Llama Guard, ShieldGemma 2, WildGuard, AEGIS all classify a *complete* response; latency is a known blocker for streaming, and none has a prefix/suffix semantics. [Inan et al., arXiv 2312.06674; Zeng et al., arXiv 2503.08838; Han et al., arXiv 2406.18495; Ghosh et al., arXiv 2310.06786]
2. **Certified & robust off-line defences** — erase-and-check certification (O(n²) on complete inputs) and randomized smoothing (SmoothLLM, ~3x overhead) are sound but far too heavy for a realtime loop. [Kumar et al., arXiv 2309.02705; Robey et al., arXiv 2305.16493]
3. **Decoding-time / token-level safety** — FUDGE, GeDi, SafeDecoding, and realtime output monitors (Gradient Cuff) decide per-prefix *during* generation: the only lineage that is close to "streaming-safe", but none is coupled to a latency floor, a pipeline placement, or a hard deadline. [Yang et al., arXiv 2104.08718; Krause et al., arXiv 2009.06358; Xu et al., arXiv 2402.08983; Wang et al., arXiv 2403.00867]
4. **Streaming inference machinery** — attention sinks (StreamingLLM), speculative decoding, streaming RNN-T/CTC ASR show streaming correctness and overlap are *solved* at the LM/ASR layer, yet the safety layer has not adopted any streaming semantics (streaming-safe = the gap). [Xiao et al., arXiv 2309.17453; Leviathan et al., arXiv 2211.17192; Sainath et al., ICASSP 2020]
5. **Audio-domain & voice-channel attacks** — inaudible voice commands, audio adversarial examples against ASR, and audio-LLM jailbreaks land precisely on the ASR/TTS boundaries a cascade exposes; these are the attack surfaces a realtime guardrail must vet before decoding, not after. [Zhang et al., DolphinAttack CCS'17; Carlini & Wagner, arXiv 1801.01944; audio-LLM jailbreak line, arXiv 2410.02465 — verify]
6. **Agentic guardrail placement & threat models** — AgentDojo, AgentHarm, and NeMo Guardrails/Colang treat guardrail placement as dialogue policy, never as latency-constrained DAG scheduling; the Dong et al. survey's timing axis is descriptive (pre/during/post) with no budget arithmetic. [Debenedetti et al., arXiv 2406.13352 — verify; Arielly et al., arXiv 2410.09024 — verify; Rebedea et al., arXiv 2310.16901; Dong et al., arXiv 2402.01822]
7. **Realtime / low-query red-teaming** — PAIR and GCG-style adaptive attacks converge in tens of queries and online settings, matching a realtime budget; no benchmark measures attack success against a *guarded, deadline-constrained* voice cascade. [Chao et al., arXiv 2310.08419; Zou et al., arXiv 2307.15043]
8. **Audio-side toxicity detection** — MuTox offers an audio-level safety signal available *in the speech stream before ASR*, i.e., a guardrail slot that does not touch the latency-critical decode path. [Costa-jussà et al., arXiv 2301.11107]

---

## 2) THE GAP

**Testable research question:** *Can a guardrail certify the agent's response as safe before the first token is spoken, without increasing the irreducible latency floor Λ\* of the voice DAG — and what is the minimal certification latency achievable at a guaranteed (bounded) bypass-miss rate, under a hard safety deadline equal to time-to-first-audio?*

**Why this is not already solved (i.e., why "safety inside the latency floor" is genuinely unformalized — the suspicion checks out):**
- All production classifiers are full-response; streaming/prefix-safe classification has no accepted definition, no soundness criterion, and no monotonicity requirement (safe-prefix ⇒ safe-extension). [KB gap G1; inan2023llama, dong2024building]
- The only *certified* defence is O(n²) over complete inputs (erase-and-check); it has no streaming form and no deadline argument. [KB gap G3; kumar2023certifying]
- Latency-work (our own Latency Floor Theorem, CCC τ_human≈200ms, ReAct k-step bound; plus speculative-decode/streaming-ASR work) and safety-work (classifiers, certification, agent benchmarks) are two disconnected literatures — no paper computes `Λ*' = Λ* + λ_g^irr` for adding a guardrail stage, no paper defines a "safety deadline" τ_safe := time-of-first-spoken-token, and none models a guardrail missing its deadline as a *bypass with an abort fallback*.
- Barge-in/streaming gives a bypass vector unique to voice: audio can start before any complete-utterance check, so even a correct post-hoc check silently overruns — absent entirely from the text-only guardrail literature. [cascade_voice_latency 06_design_levers (barge-in as perceptual patch)]
- Consequence: practitioners either resign safety to post-hoc (audit-only) or add a serial classifier that blows the CCC — neither is principled, and no paper states this trade as a theorem.

---

## 3) CANDIDATE CONTRIBUTION

**Formal model + corollary theorem + taxonomy + scheme + small benchmark:**

1. **Guardrail-in-the-DAG model.** Extend the cascade/full-duplex DAG with a guardrail stage-set G = {pre-ASR audio check, post-ASR text check, parallel-decode shadow check, kill-switch}. Each guardrail has latency λ_g = λ_g^r + λ_g^irr under the paper's decomposition.
2. **Safety Deadline Theorem (corollary of the Latency Floor Theorem).** Every guardrail is either (a) *on-critical-path* ⇒ serial guardrail inflates the floor: Λ*' = Λ* + λ_g^irr (violates the CCC if λ_g^irr > τ_human − Λ*); or (b) *off-critical-path* (shadow/parallel) ⇒ it must decide by τ_safe = time-to-first-audio/`⌈first token⌉`, else it is silently bypassed (unvetted first tokens enter audio) or a kill-switch fires with its own λ_abort deadline. Barge-in is formally the case τ_safe is undefined/zero — the guardrail is evicted by construction.
3. **Prefix-safe certification.** Define a *monotone safety certificate*: a partial sequence classified acceptable must accept every extension within a sliding window (sound, prefix-closed criterion); give an O(n) amortized online certification via a sliding-window safety invariant, positioned explicitly against the O(n²) erase-and-check bound of kumar2023certifying. This is the direct answer to KB gap G1 (formal conditions on prefix-safe generation) and G3 (linear-cost certification).
4. **Latency-aware safety budget.** Allocate budget: a guardrail fits inside the frozen floor iff Λ* + λ_g^irr ≤ τ_human; when headroom is negative, hybrid routing (`cascade_voice_latency` design lever) must route the turn, or the turn class must be pre-approved/cache-verified offline. Formalizes "safety-vs-latency" as a constrained-scheduling trade with a closed feasibility condition.
5. **Benchmark (optional, small).** Empirical guardrail-latency vs bypass-miss-rate curves (P@k latency for prefix classification; deadline-miss ⇒ silence/abort cost) on a streaming ASR→LM→TTS rig, reusing our Λ*_SC streaming-cascade floor numbers.

**Working title:** *The Safety Deadline: Guardrail Placement Inside the Latency Floor of Realtime Voice Agents*

---

## 4) EXTENSION ANGLE

Every result is a direct corollary/extension of our published Latency Floor machinery, so the next paper visibly builds on the last:

1. **Guardrail-as-stage.** Add λ_g to the irreducible decomposition; the Safety Deadline Theorem is literally a derived corollary of Theorem 1 (Latency Floor) and the CCC — "safety-feasible iff Λ* + λ_g^irr ≤ τ_human" for serial guards.
2. **Shadow-window placement.** Under streaming ASR + incremental LM prefill, the Λ*_SC decode window (δ_N + λ_lm^{decode,irr} + λ_tts^{irr}, Theorem 3) provides a *free parallel slot*: the shadow guardrail runs on the stable text prefix concurrently with decode, so its cost is hidden — only this placement adds zero floor latency. Formalizes the lone escape from the serial-guardrail inflation result.
3. **ReAct k-step re-arming.** Our k-step silence-gap bound (≤ k·Λ*) becomes a per-step safety deadline τ_safe^(i) ≤ τ_human/k — multi-step agents must re-arm the guardrail every cycle, proving per-step re-certification is a *hard* requirement, not a design nicety.
4. **Deliver on KB gaps G1 and G3.** The paper supplies the missing theoretical framework (prefix-safe conditions; O(n) amortized certification) for the two top-scored open gaps already flagged in knowledge_base/topics/ai_guardrails/gaps.md — new KB entries + a "gap addressed" update follow from the same pipeline.

---

## 5) ANCHORS (must-cite)

1. **Llama Guard** (Inan et al., arXiv 2312.06674) — the baseline full-response production classifier whose latency our gap argument targets. [KB]
2. **ShieldGemma 2** (Zeng et al., arXiv 2503.08838 — verify) — nearest thing to an audio-capable production guard; the streaming-semantics counterexample/foil.
3. **Certifying LLM Safety against Adversarial Prompting** (Kumar et al., arXiv 2309.02705) — the O(n²) certified baseline our O(n) certificate must beat. [KB]
4. **SafeDecoding** (Xu et al., arXiv 2402.08983) — token-by-token safety-aware decoding; direct prior proof that prefix-level safety control is feasible.
5. **FUDGE** (Yang et al., arXiv 2104.08718) — formal future-discriminator control of partial sequences; the right starting point for defining prefix-safe acceptability (with GeDi, arXiv 2009.06358).
6. **Audio Adversarial Examples** (Carlini & Wagner, arXiv 1801.01944) + **DolphinAttack** (CCS'17) + audio-LLM jailbreak line (arXiv 2410.02465 — verify) — the ASR/TTS-boundary attack surfaces a realtime guardrail must pre-empt.
7. **Gradient Cuff** (Wang et al., arXiv 2403.00867 — verify) — real-time jailbreak detection at inference; the closest runtime monitor, but with no deadline/placement model.
8. **AgentDojo** (arXiv 2406.13352 — verify) / **AgentHarm** (arXiv 2410.09024 — verify) — agentic threat models for multi-step (ReAct-class) guardrail re-arming.
9. **Dong et al., Building Guardrails** (arXiv 2402.01822) + **NeMo Guardrails** (arXiv 2310.16901) — the placement/taxonomy prior to refute-and-extend (descriptive timing axis → budget arithmetic). [KB]

**Methodological companions:** **PAIR** (arXiv 2310.08419) for few-query red-teaming under realtime budgets; **MuTox** (arXiv 2301.11107) for the pre-ASR audio-safety slot; Levy/Skantze/Lee turn-taking (in KB) for τ_human anchoring; **StreamingLLM** (arXiv 2309.17453) and **speculative decoding** (arXiv 2211.17192, in KB as leviathan2023fast) for the streaming-machinery half of the shadow-window argument.

---

## Gaps

- **No live web tool in this run** (only read/write available): the brief is assembled from verified literature knowledge + local KB. Must-cite arXiv IDs with high certainty: 2312.06674, 2309.02705, 2104.08718, 2009.06358, 2305.16493, 2310.16901, 2402.01822, 2310.08419, 2310.06786, 2301.11107, 2309.17453, 2211.17192, 2307.15043, 2406.18495, 1801.01944. **Verify before citing:** 2503.08838 (ShieldGemma 2), 2410.02465 (audio-LLM jailbreak), 2403.00867 (Gradient Cuff), 2406.13352 (AgentDojo), 2410.09024 (AgentHarm).
- **Next step for the group:** run a targeted deep-research pass (with web tooling) on: (i) ShieldGemma 2's exact audio/speech-to-text interface, (ii) whether any 2025-2026 paper already coins a "safety deadline" or "latency-aware guardrail budget" for voice agents (none known to me, but this is the single highest-risk claim to falsify), (iii) the real arXiv ID for the audio-LLM jailbreak line.
- **Uncertainty:** whether "prefix-safe classification" already exists under another name in the controllable-generation literature (FUDGE/GeDi are the nearest; a dedicated survey would confirm) — if so, our novelty narrows to the *deadline + placement + certification* combination, which remains unfilled either way.
