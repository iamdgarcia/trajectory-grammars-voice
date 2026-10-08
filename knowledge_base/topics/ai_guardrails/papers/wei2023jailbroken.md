---
title: "Jailbroken: How Does LLM Safety Training Fail?"
year: 2023
venue: "NeurIPS"
arxiv_id: "2307.02483"
cite_key: "wei2023jailbroken"
topic: "ai_guardrails"
subtopics: ["jailbreak", "safety-training", "failure-modes"]
key_claims:
  - "Two failure modes explain most jailbreaks: competing objectives (helpfulness vs. safety) and mismatched generalisation"
  - "Safety training generalises poorly to out-of-distribution inputs including foreign languages and base64 encoding"
limitations:
  - "Analysis is qualitative; no formal characterisation of the failure mode boundary"
open_questions:
  - "Can guardrails be designed to specifically address competing-objectives and mismatched-generalisation failure modes?"
gap_score: 4
conceptual: true
---

Theoretical analysis of why safety training fails. Directly motivates extrinsic guardrails as a necessary complement to RLHF.
