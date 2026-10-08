---
title: "Probabilistic Backchannel Prediction based on Acoustic and Linguistic Input Data"
year: 2017
venue: "Proceedings of Interspeech (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: ""
cite_key: "ruede2017probabilistic"
topic: "semantic_vad"
subtopics:
  - "backchannels"
  - "multimodal fusion"
key_claims:
  - "Backchannel opportunity is predictable from fused acoustic+linguistic features with a probabilistic model."
limitations:
  - "Pre-LLM feature engineering; small data."
  - "Backchannel event only; no barge-in/turn-end policy split."
open_questions:
  - "Whether modern encoders make backchannel timing learnable per language (jev-vad-poc related work: still no public multilingual model)."
gap_score: 4
conceptual: true
---

Early fusion precedent for `umair2024turntaking`. In jev-vad-poc the
backchannel question is answered jointly with barge-in by one binary decision
(take-floor vs not) — this paper predicts backchannels as a separate event.
