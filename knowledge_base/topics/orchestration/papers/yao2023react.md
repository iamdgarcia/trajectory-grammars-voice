---
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
year: 2023
venue: "ICLR"
arxiv_id: "2210.03629"
cite_key: "yao2023react"
topic: "orchestration"
subtopics:
  - "reasoning-acting loops"
  - "tool calling"
key_claims:
  - "Interleaving textual reasoning traces with acting steps (tool/API calls and environment interaction) improves groundedness, factuality, and traceability over prompting-only or acting-only baselines on knowledge and decision tasks."
  - "ReAct reduces hallucination and error-propagation by forcing the model to reason about observations before acting."
limitations:
  - "Multi-step reason-act loops multiply wall-clock latency: each hop adds one model prefill/decode and usually one tool round-trip."
  - "Task control is heuristic (max hops), not deadline-aware."
open_questions:
  - "Formal latency of the k-step reason-act loop for interactive/realtime deployment — addressed by the published cascade_voice_latency thm:react and extended to typed tool DAGs in the orchestration-floor paper."
  - "When can tool round-trips be overlapped with generation or user speech (hideability window)?"
gap_score: 3
conceptual: true
---

Anchor for the orchestration topic's tool-calling thread. Its loop shape
`reason -> call -> observe -> reason` is the object the event-driven
orchestrator schedules; the product PoC keeps this loop but runs tool
execution in a background dispatcher instead of in the serial call path.
See also `langgraph2024` (graph form) and `skantze2021turn` (turn semantics).
