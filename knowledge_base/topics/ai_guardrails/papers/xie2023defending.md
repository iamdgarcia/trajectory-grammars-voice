---
title: "Defending ChatGPT against Jailbreak Attack via Self-Reminder"
year: 2023
venue: "Nature Machine Intelligence"
arxiv_id: "2310.06387"
cite_key: "xie2023defending"
topic: "ai_guardrails"
subtopics: ["defence", "system-prompt", "self-reminder"]
key_claims:
  - "Prepending a responsibility reminder to the system prompt reduces jailbreak success by 61% on average"
  - "Self-reminder is model-agnostic and requires no additional training or computation"
limitations:
  - "Adversaries can craft prompts that override the self-reminder"
  - "Effectiveness untested on models without instruction-following training"
open_questions:
  - "Can self-reminder be dynamically updated based on detected attack patterns?"
gap_score: 3
conceptual: true
---

Zero-cost defence via system prompt engineering. Relevant to the low-latency guardrail design space.
