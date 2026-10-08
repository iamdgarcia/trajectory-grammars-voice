---
title: "NeMo Guardrails: A Toolkit for Controllable and Safe LLM Applications"
year: 2023
venue: "EMNLP"
arxiv_id: "2310.10501"
cite_key: "rebedea2023nemo"
topic: "ai_guardrails"
subtopics: ["extrinsic-guardrails", "framework", "colang", "input-output-filtering"]
key_claims:
  - "Colang, a domain-specific language, allows declarative specification of guardrail flows without model retraining"
  - "NeMo Guardrails integrates input, output, and dialogue-level rails in a single framework"
limitations:
  - "Colang requires developer expertise; not accessible to non-technical policy authors"
  - "Dialogue-level rails add latency proportional to conversation history length"
open_questions:
  - "Can Colang policies be automatically synthesised from natural-language safety requirements?"
  - "How do dialogue-level rails perform under adversarial multi-turn attacks?"
gap_score: 3
conceptual: true
---

Production guardrail framework reference. Colang DSL is a concrete instance of declarative safety policy — useful for taxonomy placement.
