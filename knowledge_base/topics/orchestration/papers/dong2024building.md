---
title: "Building Guardrails for Large Language Models"
year: 2024
venue: "arXiv (2402.01822)"
arxiv_id: "2402.01822"
cite_key: "dong2024building"
topic: "orchestration"
subtopics:
  - "guardrails"
  - "pipeline placement"
key_claims:
  - "Guardrail techniques form a landscape across attack surfaces and a syntax-semantics-safety layering, with timing classified descriptively as pre/during/post generation."
  - "Placement is treated as dialogue policy, with no latency-budget arithmetic for where a guardrail sits relative to a deadline."
limitations:
  - "The timing axis is descriptive, not a constrained-scheduling model."
  - "No treatment of streaming/prefix-safe classification under a hard first-token deadline."
open_questions:
  - "Guardrail placement as a schedulable stage inside the cascade latency floor (the safety-deadline angle; seeds ai_guardrails gaps G1/G3)."
gap_score: 3
conceptual: true
---

Cross-topic bridge: the product treats guardrail as pipeline stage, and the
orchestration-floor paper discusses re-armable guardrails on model reentry —
both motivate placing guardrails inside the DAG with a deadline rather than
post-hoc. Full entry also lives in ai_guardrails topic.
