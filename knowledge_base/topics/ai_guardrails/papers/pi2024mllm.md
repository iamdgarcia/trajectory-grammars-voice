---
title: "MLLM-Protector: Ensuring MLLM's Safety without Hurting Performance"
year: 2024
venue: "arXiv"
arxiv_id: "2401.02906"
cite_key: "pi2024mllm"
topic: "ai_guardrails"
subtopics: ["multimodal", "extrinsic-guardrails", "harm-detector", "detoxifier"]
key_claims:
  - "A lightweight harm detector + response detoxifier pipeline preserves helpfulness while blocking multimodal attacks"
  - "Decoupling detection from generation allows independent updates to the safety component"
limitations:
  - "Two-stage pipeline doubles inference latency"
  - "Detoxifier may alter factual content in benign responses"
open_questions:
  - "Can the detector and detoxifier be merged into a single streaming-compatible pass?"
gap_score: 4
conceptual: true
---

Modular multimodal guardrail architecture. The two-stage latency cost is a concrete instance of the real-time gap.
