# The Safety Deadline (REFRESH)

*Discovery brief, round 2. Refresh of `papers/_next_angles/angle_3_safety_deadline.md`. Caveat: no live web tool in this run — IDs marked [verify] must be checked before citing. Core-claim check: no paper known to me coins "safety deadline," defines prefix-safe certification with deadline semantics, or models guardrail placement as latency-floor arithmetic for voice agents; the two novelty threats are (i) vendor streaming-moderation products pre-empting the *practical* claim and (ii) an unrecognized prefix-safety line in controllable generation.*

## Working title

*The Safety Deadline: Dual-Bounded Guardrail Placement in Realtime Voice Agents (Perceptual τ_human, Regulatory τ_reg)*

## Landscape

1. **Llama Guard 3 / 4** — production guard classifiers; 4 adds multimodality but still scores complete content, no prefix semantics. [arXiv 2312.06674; 2504.12368 verify]
2. **ShieldGemma 2** — image-capable guard; confirms vendor guards are full-content, audio interface unproven. [arXiv 2503.08838 verify]
3. **GuardReasoner** — reasoning-style guards raise accuracy but *lengthen* prompts, worsening serving latency — sharpens the floor problem rather than solving it. [arXiv 2501.18492 verify]
4. **Erase-and-check certification** — only certified defence, O(n²) on complete inputs, no streaming form. [arXiv 2309.02705]
5. **FUDGE / GeDi / SafeDecoding** — per-prefix controlled-generation lineage; the nearest prior to "prefix-safe," but no deadline, no placement, no voice. [arXiv 2104.08718; 2009.06358; 2402.08983]
6. **NeMo Guardrails + Dong et al. survey** — placement taxonomy (pre/during/post) is descriptive; no budget arithmetic. Bedrock/OpenAI Realtime ship "streaming moderation" as product features with no published semantics [verify vendor docs]. [arXiv 2310.16901; 2402.01822]
7. **AgentDojo / AgentHarm** — agentic threat models with zero latency axis. [arXiv 2406.13352 verify; 2410.09024 verify]
8. **AudioJailbreak + Carlini & Wagner + DolphinAttack** — ASR/TTS-boundary attacks: the voice-specific surfaces a pre-speech guard must vet. [arXiv 2410.02465 verify; 1801.01944; CCS'17]
9. **Full-DuplexBench v1.5/v2 line** — evaluates native full-duplex models' interruption/safety *behaviors*; evaluates no guardrail, no cascade placement. [per KB entries fullduplexbenchv15/v2, IDs verify]
10. **Real-time audio deepfake / partial-spoof detection (ASVspoof 5 line)** — active detector line for the pre-ASR slot, but purely detection accuracy, no deadline model. [ASVspoof 5, arXiv verify]

## The gap

**Testable RQ:** Can a guardrail certify the response before the first token is spoken without inflating the latency floor Λ*, when the deadline is not one number but a *lattice*: τ_human ≈ 200 ms (perceptual, published) binding on every turn, and τ_reg (regulatory execution clock — e.g., SEPA Instant's 10 s execution window with Verification of Payee, EU Regulation 2024/886) binding on payment-class turns? A guard that fits τ_human can still miss τ_reg on an outbound-transfer turn, and the correct placement (serial vs shadow vs pre-tool) flips between the two.

**Why unsolved:** (i) every production guard is full-response with no monotone prefix-safety criterion; (ii) the only certified defence is O(n²) offline; (iii) the latency and safety literatures remain disjoint — nobody computes Λ*' = Λ* + λ_g^irr; (iv) no work models *bypass-with-abort*: in a cascade, unvetted tokens reach the speaker at time-to-first-audio, so a correct-but-late check is silently evaded (barge-in makes τ_safe undefined by construction — our cessation paper formalizes half of this but never the guardrail); (v) no paper treats regulator-imposed clocks as concurrent deadlines with perceptual ones.

## Candidate contribution

1. **Guardrail-in-DAG model** reusing our λ decomposition: each guard has λ_g = λ_g^r + λ_g^irr.
2. **Safety Deadline Theorem** (corollary of the Latency Floor Theorem): serial guard ⇒ Λ*' = Λ* + λ_g^irr; shadow guard ⇒ must decide by τ_safe = time-to-first-audio or is bypassed/aborts. **New in refresh:** the *deadline lattice* — schedulability iff λ_g^irr ≤ min(binding deadlines of the turn class); turn classification (informational vs payment) selects which deadline binds, and τ_reg-turns license serial guards that τ_human-turns forbid.
3. **Prefix-safe monotone certificate:** safe-prefix ⇒ safe-extension within a sliding window; O(n) amortized certification against erase-and-check's O(n²).
4. **Bypass-with-abort semantics** with abort-cost under τ_reg (cancel/hold the payment; log per DORA).
5. **Small benchmark:** guardrail latency vs bypass-miss-rate curves on a streaming ASR→LLM→TTS rig, reusing our Λ*_SC numbers and Spanish benchmark.

## Reuse of our published results

Latency Floor Theorem (corollary structure); k-step ReAct bound → per-step re-arming deadline τ_safe^(i) ≤ τ_human/k; cessation floor + generation-interruptible/execution-persistent split → kill-switch and tool-guard semantics; semantic VAD veto result (veto-only asymmetry: false-veto cost ≪ false-pass cost — the same cost structure guardrails need) and its measured p99 268 ms cloud decision latency as the shadow-guard headroom; streaming-cascade floor Λ*_SC as the free parallel slot.

## Banking grounding

- **Vishing arrives as speech, not text:** voice social engineering (Ferrari attempt, Jan 2024; Arup HK US$25M deepfake, Feb 2024 — publicly reported [verify citations]) hits the ASR boundary; guardrails must vet mid-stream ASR output before TTS.
- **APP fraud reimbursement (UK PSR, from Oct 2024)** makes post-hoc-only safety commercially untenable: payment turns need pre-execution checks.
- **SEPA Instant + VoP (EU 2024/886, VoP mandatory Oct 2025):** instantiates τ_reg concretely (10 s execution clock); payment-class turns are where the lattice bites.
- **DORA (applies 17 Jan 2025):** ICT-incident classification and reporting clock (initial notification hours-scale, final report ~1 month [verify exact hours]) — a guardrail bypass becomes a reportable incident; bypass-miss telemetry is a compliance artifact, not a nice-to-have.
- **EU AI Act:** GPAI duties Aug 2025; transparency obligations Aug 2026 — voice-channel disclosures and logging.
- **Spanish channel:** fraud lexicons and accent variation in es-ES/es-419; our frozen Spanish benchmark and CPU/cloud latency tables supply the headroom numbers.

## Scores

**Novelty 4** — claim unclaimed to high confidence; FUDGE/GeDi lineage is close on prefix-safety but the deadline+placement+certification+lattice combination is open.
**Fit 5** — every theorem is a corollary of our two published floors; visible program continuity.
**Banking 5** — τ_reg (VoP/SEPA Instant), APP fraud, DORA are native constraints, not garnish.
**Feasibility 4** — formal core reuses published machinery; benchmark needs one guard model + streaming rig we already operate.
**Risk 3** — two live threats: vendor streaming moderation may be practical prior art (mitigate: product features lack semantics — cite docs), and prefix-safety may exist under another name in controllable generation (mitigate: novelty then narrows to deadline lattice + placement, still unfilled).

## Verdict

**Pursue now.** The refresh adds what the prior brief lacked — the dual τ_human/τ_reg deadline lattice, which no found prior work claims and which is exactly where banking (unlike generic chatbots) has an external hard clock. Precondition: one targeted verification pass (ShieldGemma 2 audio interface; Llama Guard 4 ID; any "speculative safety decoding" paper; DORA notification hours; FDB v2 ID) before Stage 1 outline.
