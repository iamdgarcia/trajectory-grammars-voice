---
title: "Certifying LLM Safety against Adversarial Prompting"
year: 2023
venue: "arXiv"
arxiv_id: "2309.02705"
cite_key: "kumar2023certifying"
topic: "ai_guardrails"
subtopics: ["formal-verification", "certified-defence", "safety-guarantee"]
key_claims:
  - "Erase-and-check framework provides certified safety: if any sub-sequence triggers harmful output, the input is flagged"
  - "Certification comes at O(n^2) inference cost — impractical for long inputs"
limitations:
  - "O(n^2) cost makes real-time deployment infeasible for inputs longer than ~100 tokens"
  - "Only certifies against insertion-type attacks, not semantic rephrasing"
open_questions:
  - "Can approximate certification achieve near-identical guarantees with O(n) cost?"
gap_score: 5
conceptual: true
---

Formal safety certification paper. The O(n^2) cost is a direct example of the theory-practice gap in real-time guardrails.
