---
title: "Building Guardrails for Large Language Models"
year: 2024
venue: "arXiv"
arxiv_id: "2402.01822"
cite_key: "dong2024building"
topic: "ai_guardrails"
subtopics: ["survey", "taxonomy", "extrinsic-guardrails"]
key_claims:
  - "Guardrails can be taxonomised along three axes: timing (pre/post/during), modality, and enforcement mechanism"
  - "Existing surveys do not address streaming/real-time deployment constraints"
limitations:
  - "Taxonomy is descriptive, not prescriptive — no design guidance for practitioners"
  - "Multimodal coverage limited to image-text; audio and video omitted"
open_questions:
  - "How do guardrail design choices interact with token-streaming latency budgets?"
  - "What is the minimum viable guardrail for real-time voice LLM applications?"
gap_score: 4
conceptual: true
---

Closest prior survey to the current SLR. Explicitly omits real-time and full-multimodal coverage — directly motivates the guardrails paper contribution.
