---
title: "Training language models to follow instructions with human feedback"
year: 2022
venue: "NeurIPS"
arxiv_id: "2203.02155"
cite_key: "ouyang2022training"
topic: "ai_guardrails"
subtopics: ["alignment", "rlhf", "intrinsic-guardrails"]
key_claims:
  - "RLHF with human preference labels produces InstructGPT, which humans prefer over GPT-3 despite being 100x smaller"
  - "Alignment tax is small: RLHF slightly degrades public NLP benchmarks but is offset by instruction-following gains"
limitations:
  - "Reward model trained on a narrow set of human labellers — cultural bias not characterised"
  - "No formal safety guarantee; jailbreaks still possible"
open_questions:
  - "Can RLHF scale to multimodal alignment without proportional labelling cost?"
  - "What is the minimum human feedback signal needed for safe alignment?"
gap_score: 2
conceptual: true
---

Foundational RLHF paper. Establishes the intrinsic-guardrail baseline against which inference-time approaches are compared.
