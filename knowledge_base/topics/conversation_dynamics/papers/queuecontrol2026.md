---
title: "Learning When to Automate: Queue Control in Human-AI Service Systems"
year: 2026
venue: "arXiv 2607.06017 (2026-07-07) - verified via alphaXiv discovery, 2026-10-08"
arxiv_id: "2607.06017"
cite_key: "queuecontrol2026"
topic: "conversation_dynamics"
subtopics:
  - "escalation"
  - "queueing"
key_claims:
  - "Two-stage human-AI service system (chatbot then human); optimal routing/escalation from queue state."
limitations:
  - "Escalation decided OUTSIDE the conversation from queue-level state; no conversation-internal signal, no trajectories, no voice."
open_questions:
  - "Conversation-internal escalation signals (a5 escalate state; a10 escalation floor)."
gap_score: 4
conceptual: true
---

Complementary escalation anchor: queue control decides which tasks to automate; a5/a10 decide
inside the conversation when to escalate, from partial trajectory state. The cost model
(agent-minutes vs teller-minutes vs customer frustration) is shared vocabulary.
