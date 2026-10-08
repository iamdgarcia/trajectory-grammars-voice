---
title: "Trouble on the Horizon: Predicting Derailment in Online Conversations Prior to it Happening"
year: 2019
venue: "WWW 2019; Cornell (Chang & Danescu-Niculescu-Mizil) - verified indirectly via TRACER related work, 2026-10-08"
cite_key: "chang2019derailment"
topic: "conversation_dynamics"
subtopics:
  - "derailment forecasting"
  - "partial-context prediction"
key_claims:
  - "Sequential models over growing contexts forecast conversation derailment before breakdown."
limitations:
  - "Social/open-domain settings; relies on social cues, not belief-state evolution or tool state."
  - "Text-only; no voice, no task outcomes, no decision guarantees."
open_questions:
  - "Trajectory forecasting for task-oriented (not social) conversations."
gap_score: 4
conceptual: true
---

Establishes partial-context prediction as principled (TRACER credits it). The a5 paper transposes
the forecasting idea to voice-agent conversations with typed grammar states and stopping rules.
