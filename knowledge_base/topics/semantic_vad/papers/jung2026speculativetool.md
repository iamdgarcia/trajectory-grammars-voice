---
title: "Hiding Tool Latency in On-Device Cascaded Voice Agent through Speculative Execution"
year: 2026
venue: "arXiv (2610.07641, 2026-10-06); Qualcomm AI Research + KAIST — full text read and verified via alphaXiv MCP, 2026-10-08"
arxiv_id: "2610.07641"
cite_key: "jung2026speculativetool"
topic: "semantic_vad"
subtopics:
  - "speculative execution"
  - "tool calling"
  - "on-device"
key_claims:
  - "Rule-based Predictor watches streaming ASR partials and fires LONG-LATENCY tool calls (web search) speculatively while the user is still speaking; results cached and either injected directly into the LLM prompt (direct injection) or reused when the LLM independently requests the same tool (verified fallback)."
  - "Trigger cadence: after N_min=6 words, every ΔN=5 words, or at pauses > τ_pause=300 ms. Clause-splitting allows parallel dispatch of multiple intents in one utterance."
  - "Safety design: worst case is upper-bounded by the serial baseline — LLM can always issue tool calls normally; rule-based validation rejects invalid caches (self-corrections); cache verification prevents redundant re-fetch."
  - "Android on-device (Snapdragon, Llama-3.2-3B W4A16 on NPU): TTFA median 5.79→4.60 s, p99 19.76→15.10 s, F1 44.8→60.6%. Ablation: prefetch-only ≈ baseline (wasted 47%); direct injection is where the win comes from (Ready 46.6%, wasted 6%)."
  - "146-sample eval (100 written + 22 hard negatives + 24 adversarial with corrections/retractions/late intents), TTS-synthesized speech, English."
limitations:
  - "English-only; single tool class that matters (web search vs fixed 12-topic set); rule-based predictor (no learned gate); on-device Android stack, not server cascade."
  - "TTFA measured from END of speech — the end-of-turn decision itself is not part of the contribution; no semantic gating of speculation."
  - "Wasted speculative calls in adversarial set: 21/24 — self-corrections still burn speculations."
open_questions:
  - "Replace the rule-based predictor/trigger with a semantic end-of-turn probability (jev-vad-style) as the speculation gate: fire only when P(turn_complete) is high enough to justify the wasted-call cost. Untested."
  - "Multilingual reproduction (Spanish interim transcripts) — nothing published."
gap_score: 3
conceptual: true
---

Second half of the SV4 picture (2026-10-06, days old): speculative TOOL
execution from partial ASR hypotheses, on-device, with the honest ablation
(prefetch alone wastes half the calls; the win is direct injection + verified
fallback). Together with `braun2026voicelight` (speculative GENERATION gated
by an acoustic-pause rule), the building blocks of speculative cascade
dispatch exist — but BOTH trigger speculation without a semantic end-of-turn
signal on the interim transcript. The unclaimed intersection, and the
cheapest next paper/measurement of the jev-vad program: use the turn-end
probability as the *speculation gate* (when to start + when to inject), with
the wasted-call economics of SV5 as the tuning objective.
