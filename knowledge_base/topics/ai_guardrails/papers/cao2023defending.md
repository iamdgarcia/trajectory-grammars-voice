---
title: "Defending Against Alignment-Breaking Attacks via Robustly Aligned LLM"
year: 2023
venue: "arXiv"
arxiv_id: "2309.14348"
cite_key: "cao2023defending"
topic: "ai_guardrails"
subtopics: ["defence", "robust-alignment", "fine-tuning"]
key_claims:
  - "Augmenting alignment fine-tuning with adversarial examples improves robustness to jailbreaks"
  - "Robust alignment does not significantly degrade helpfulness on standard benchmarks"
limitations:
  - "Requires access to model weights — not applicable to API-only deployments"
open_questions:
  - "Can adversarial alignment be combined with inference-time guardrails for defence in depth?"
gap_score: 3
conceptual: true
---

Robust fine-tuning defence. Contrasts with extrinsic inference-time approaches — relevant to the intrinsic/extrinsic taxonomy axis.
