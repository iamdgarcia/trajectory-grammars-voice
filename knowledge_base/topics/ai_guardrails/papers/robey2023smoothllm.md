---
title: "SmoothLLM: Defending Large Language Models Against Jailbreaking Attacks"
year: 2023
venue: "arXiv"
arxiv_id: "2310.03684"
cite_key: "robey2023smoothllm"
topic: "ai_guardrails"
subtopics: ["defence", "randomised-smoothing", "extrinsic-guardrails"]
key_claims:
  - "Randomly perturbing input copies and majority-voting reduces GCG attack success rate from ~90% to <1%"
  - "SmoothLLM adds ~3x latency overhead due to multiple forward passes"
limitations:
  - "3x latency overhead is incompatible with real-time streaming requirements"
  - "Ineffective against semantic jailbreaks that are perturbation-invariant"
open_questions:
  - "Can randomised smoothing be approximated in a single pass for streaming-compatible defence?"
gap_score: 4
conceptual: true
---

Randomised smoothing defence. The latency overhead is a direct example of the real-time guardrail gap identified in the SLR.
