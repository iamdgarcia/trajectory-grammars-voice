---
title: "FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts"
year: 2023
venue: "arXiv"
arxiv_id: "2311.05608"
cite_key: "gong2023figstep"
topic: "ai_guardrails"
subtopics: ["multimodal", "jailbreak", "vision-language", "typographic-attack"]
key_claims:
  - "Embedding harmful instructions as text within images bypasses text-only safety filters"
  - "Typographic attacks succeed on GPT-4V, LLaVA, and MiniGPT-4 with >70% success rate"
limitations:
  - "Attack requires the model to perform OCR on the embedded text — fails if OCR is blocked"
open_questions:
  - "Can a multimodal guardrail detect typographic attacks without full OCR of all input images?"
gap_score: 4
conceptual: true
---

Key multimodal jailbreak paper. Typographic attacks are a concrete instance of the cross-modal safety gap.
