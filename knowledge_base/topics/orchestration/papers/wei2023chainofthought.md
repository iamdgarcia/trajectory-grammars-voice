---
title: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
year: 2022
venue: "NeurIPS (vol. 35)"
arxiv_id: "2201.11903"
cite_key: "wei2023chainofthought"
topic: "orchestration"
subtopics:
  - "reasoning hops"
key_claims:
  - "Generating intermediate reasoning steps before the final answer substantially improves LLM performance on arithmetic, commonsense, and symbolic reasoning tasks."
  - "Reasoning is an internal multi-step process expressed as tokens, which is what makes each hop a latency component in interactive use."
limitations:
  - "Optimized for accuracy, not timing: nothing bounds the number of steps or their wall-clock cost."
  - "Close guidance needed for some tasks; CoT does not by itself ground in external state."
open_questions:
  - "The latency cost of CoT hops in interactive loops — formalized as k·lambda_lm^irr in the published thm:react and opened further in the orchestration-floor paper."
gap_score: 3
conceptual: true
---

Reasoning-hops anchor: every reasoning step is a prefill+decode of wall-clock
time in a cascade, which is exactly the term the orchestration-floor model
schedules around. Already cited in the published cascade_voice_latency paper.
