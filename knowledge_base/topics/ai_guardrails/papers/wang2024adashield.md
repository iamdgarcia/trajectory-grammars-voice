---
title: "AdaShield: Adapting System Prompts for Multi-modal Safety"
year: 2024
venue: "arXiv"
arxiv_id: "2403.09513"
cite_key: "wang2024adashield"
topic: "ai_guardrails"
subtopics: ["multimodal", "system-prompt", "adaptive-defence", "vision-language"]
key_claims:
  - "Adaptive system prompts that include the image description reduce multimodal jailbreak success by 40%"
  - "Static safety prompts are insufficient for image-based attacks that exploit visual context"
limitations:
  - "Image description adds latency proportional to image complexity"
  - "Adversaries can craft images whose descriptions appear benign"
open_questions:
  - "Can adaptive system prompt generation be made streaming-compatible for real-time VLM deployments?"
gap_score: 5
conceptual: true
---

Adaptive multimodal defence via dynamic system prompts. High gap score — streaming compatibility is an open problem with no current solution.
