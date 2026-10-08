---
title: "FD-VAD: Semantic Endpoint Detection for Streaming Full-Duplex Speech"
year: 2026
venue: "arXiv (2609.35791, 2026-09-16); University of Maryland — full text read and verified via alphaXiv MCP, 2026-10-08"
arxiv_id: "2609.35791"
cite_key: "mathur2026fdvad"
topic: "semantic_vad"
subtopics:
  - "streaming endpointing"
  - "audio-side semantic"
  - "full-duplex"
key_claims:
  - "ASR-free streaming semantic endpointing: frozen WavLM-base-plus + 2-layer adapter + LoRA Qwen2.5-0.5B maps a 2.56 s causal audio window (320 ms stride) directly to CONTINUE/STOP."
  - "Chunk F1 0.832, false-stop 0.6% on smart-turn-v3.1 test (1,000 clips); utterance-level 0.976 vs Smart Turn 0.965 (non-streaming)."
  - "Zero-shot on TurnBench dev: highest EOT recall among qualifying systems (0.853 at FP<=0.10), median commit latency 1019 ms."
  - "Confidence-gated commitment (P(STOP)>=tau for K consecutive decisions): tau=0.9, K=1 gives median endpoint delay 190 ms at 2.0% false-interruption rate."
  - "In continuous dialogue, semantic endpointing 'benefits substantially from acoustic gating' (Silero VAD gate before semantic commit)."
limitations:
  - "English-only: trained on the English subset of smart-turn-v3.1 (63,386 clips); no Spanish or Romance-language evaluation."
  - "GPU-bound in practice: 45.8 ms per 2.56 s window on an A100; no CPU deployment story."
  - "Stop-only binary (continue/stop): no barge-in three-way policy (take_floor/backchannel/side_talk), no transcript-level question framing."
open_questions:
  - "Does the text-side question framing of jev-vad compose with an audio-side FD-VAD-style streamer as independent veto layers?"
  - "TurnBench (Jiang et al. 2026, cited as FD-VAD's conversational eval) as a candidate shared eval for SV3/SV5 cost studies."
gap_score: 3
conceptual: true
---

The strongest published audio-side semantic endpointer at the time of writing
(2026-10). Directly relevant to the jev-vad program in four ways:

1. **External validation of the asymmetry framing.** FD-VAD's motivation states
   the same failure-cost asymmetry jev-vad formalized ("an early STOP can
   interrupt a user, whereas a conservative decision primarily adds delay") and
   builds a confidence gate as its operating-point controller — independent
   confirmation that operating points, not detectors, are the deployment unit.
2. **External validation of serial acoustic→semantic composition (F4).** Their
   TurnBench protocol gates semantic inference behind a Silero VAD gate and
   reports the composition beats ungated semantic prediction — the same
   conclusion as our FINDINGS F4, from a different lab.
3. **Sharpens gap SV1.** Audio-side models reach 0.97+ utterance accuracy on
   smart-turn-style data while text-only turn-end sits near chance (our sweep
   0.40-0.54 on Spanish hard cuts). The bottleneck is the *text-only signal*,
   not the decision layer — future work should fuse or go multimodal, not
   re-tune text prompts.
4. **Leaves the jev-vad niche open.** No Spanish evaluation, no CPU story
   (A100-only timing), no barge-in policy classes, no question-wording
   ablation — gaps SV2/SV4 untouched by this work.

Citation note: FD-VAD's related-work section is a useful anchor list for the
next paper (TEN turn detection, FastTurn 2604.01897, Next-Turn 2606.18094,
SpeculativeETD, SoulX-Duplug, X2-Turn 2608.10878, UltraVAD — all unverified
here except where cross-checked on alphaXiv; verify IDs before citing).
