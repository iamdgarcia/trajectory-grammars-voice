---
title: "SafeVLM: A Simple and Effective Framework for Safe Vision-Language Models"
year: 2024
venue: "arXiv"
arxiv_id: "2402.08583"
cite_key: "oh2024safevlm"
topic: "ai_guardrails"
subtopics: ["multimodal", "extrinsic-guardrails", "vision-language"]
key_claims:
  - "Safety token alignment during fine-tuning improves VLM refusal rates without dedicated safety modules"
  - "A single safety embedding prepended to visual tokens is sufficient for most harm categories"
limitations:
  - "Safety token approach requires model weight access — not applicable to API deployments"
open_questions:
  - "Can safety tokens be injected at inference time via soft prompting without retraining?"
gap_score: 4
conceptual: true
---

Lightweight VLM safety approach. The soft-prompting open question is a candidate contribution for a future paper.
