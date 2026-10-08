---
title: "Turn-Taking and Backchannel Prediction with Acoustic and Large Language Model Fusion"
year: 2024
venue: "Proceedings of ICASSP (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: ""
cite_key: "umair2024turntaking"
topic: "semantic_vad"
subtopics:
  - "multimodal fusion"
  - "turn-shift prediction"
  - "backchannels"
key_claims:
  - "Fusing acoustic features with LLM representations predicts both turn-taking and backchannels, outperforming unimodal baselines."
limitations:
  - "English-centric; event-level evaluation."
  - "No deployment operating points, no CPU latency analysis."
open_questions:
  - "Per-decision operating points (precision vs recall bias) for the two pipeline decisions."
  - "Spanish/romance-language coverage."
gap_score: 3
conceptual: true
---

Modern LLM-fusion continuation of `ruede2017probabilistic` (features) and
`ekstedt2020turngpt` (text). jev-vad-poc's distinction: instead of one fused
predictor of the shift event, two typed questions with independent thresholds —
motivated by the failure-cost asymmetry between cutting a user off and waiting.
