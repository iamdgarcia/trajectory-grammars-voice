---
title: "VLGuard: Efficient Safety Fine-tuning for Vision-Language Models"
year: 2024
venue: "arXiv"
arxiv_id: "2405.13581"
cite_key: "li2024vlguard"
topic: "ai_guardrails"
subtopics: ["multimodal", "safety-fine-tuning", "vision-language", "efficiency"]
key_claims:
  - "Mixed safety/utility data fine-tuning avoids the safety-utility trade-off seen in separate fine-tuning stages"
  - "2K safety samples are sufficient for strong multimodal safety with minimal utility degradation"
limitations:
  - "Requires model retraining — not deployable as an extrinsic guardrail"
open_questions:
  - "What is the minimum multimodal safety dataset size for production-grade VLM guardrails?"
gap_score: 3
conceptual: true
---

Data-efficient VLM safety fine-tuning. Relevant to the training-vs-inference guardrail design choice.
