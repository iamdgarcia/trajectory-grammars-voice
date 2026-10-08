---
title: "Llama 2: Open Foundation and Fine-Tuned Chat Models"
year: 2023
venue: "arXiv"
arxiv_id: "2307.09288"
cite_key: "touvron2023llama2"
topic: "ai_guardrails"
subtopics: ["alignment", "rlhf", "dual-reward-model"]
key_claims:
  - "Dual reward model architecture (helpfulness RM + safety RM) with separate optimisation targets reduces safety/helpfulness trade-off"
  - "Safety Context Distillation prepends a safety system prompt during fine-tuning to improve robustness"
  - "Ghost attention enables multi-turn instruction following without safety degradation"
limitations:
  - "Safety evaluation limited to English; multilingual robustness not characterised"
  - "Closed fine-tuning data; reproducibility limited"
open_questions:
  - "Does dual RM generalise to multimodal LLMs without architecture changes?"
  - "How does Ghost Attention interact with long-context deployments?"
gap_score: 3
conceptual: true
---

Key architectural reference for dual-RM safety patterns and Safety Context Distillation. Directly relevant to real-time guardrail design.
