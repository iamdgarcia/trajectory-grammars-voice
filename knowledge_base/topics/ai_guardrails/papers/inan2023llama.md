---
title: "Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations"
year: 2023
venue: "arXiv"
arxiv_id: "2312.06674"
cite_key: "inan2023llama"
topic: "ai_guardrails"
subtopics: ["extrinsic-guardrails", "classifier", "input-output-filtering"]
key_claims:
  - "A fine-tuned LLM classifier outperforms rule-based and smaller ML classifiers on content safety benchmarks"
  - "A taxonomy of six harm categories (violence, hate, sexual, criminal, weapons, self-harm) covers most production safety requirements"
limitations:
  - "Inference latency of a full LLM classifier may be prohibitive for real-time streaming"
  - "Taxonomy is English-centric and US-regulatory-aligned"
open_questions:
  - "Can Llama Guard be distilled into a smaller model for low-latency deployment?"
  - "How does the six-category taxonomy extend to multimodal harms?"
gap_score: 4
conceptual: true
---

Primary extrinsic guardrail reference. The latency gap (full-LLM classifier vs. streaming requirement) is a key open problem in the guardrails SLR.
