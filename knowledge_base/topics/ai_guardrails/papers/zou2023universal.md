---
title: "Universal and Transferable Adversarial Attacks on Aligned Language Models"
year: 2023
venue: "arXiv"
arxiv_id: "2307.15043"
cite_key: "zou2023universal"
topic: "ai_guardrails"
subtopics: ["adversarial-attacks", "jailbreak", "transferability"]
key_claims:
  - "Greedy coordinate gradient (GCG) search finds adversarial suffixes that transfer across models"
  - "Aligned models (ChatGPT, Claude, Gemini) are vulnerable to white-box-derived transferable attacks"
limitations:
  - "GCG suffix is detectable by perplexity filters"
  - "Attack effectiveness degrades with output length"
open_questions:
  - "Can guardrails detect GCG suffixes in real-time without full perplexity computation?"
gap_score: 3
conceptual: true
---

Landmark adversarial attack paper. Motivates the need for inference-time guardrails that go beyond alignment training.
