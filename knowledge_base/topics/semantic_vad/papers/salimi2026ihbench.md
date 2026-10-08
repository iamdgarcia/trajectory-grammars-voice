---
title: "IHBench: Evaluating Post-Interruption Recovery in Voice Agents with Structured Workflows"
year: 2026
venue: "arXiv (verified via alphaXiv, 2026-10-05, jev-vad-poc)"
arxiv_id: "2606.19595"
cite_key: "salimi2026ihbench"
topic: "semantic_vad"
subtopics:
  - "full-duplex benchmark"
  - "interruption recovery"
key_claims:
  - "Post-interruption recovery in structured-workflow voice agents (customer service, healthcare scheduling, account management) evaluated empirically; closest prior to resume-after-interruption analyses."
limitations:
  - "Recovery outcomes, not reaction-latency floors; not Spanish."
open_questions:
  - "How barge-in policy precision (false interrupts on backchannels) degrades downstream recovery."
gap_score: 3
conceptual: true
---

IHBench is downstream of the decision jev-vad makes: a better barge-in policy
(fewer false interrupts on backchannels/side-talk) should improve recovery
metrics IHBench measures. Cross-link: orchestration gap OG2 (cessation floor),
`li2025easyturn`.
