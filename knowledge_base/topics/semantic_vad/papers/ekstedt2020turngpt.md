---
title: "TurnGPT: A Transformer-Based Language Model for Predicting Turn-Taking in Spoken Dialog"
year: 2020
venue: "arXiv (arXiv:2010.10854, verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: "2010.10854"
cite_key: "ekstedt2020turngpt"
topic: "semantic_vad"
subtopics:
  - "turn-shift prediction"
  - "text-based"
key_claims:
  - "A transformer LM over tokenized transcripts scores the probability of a turn shift at each token: text alone carries turn-shift information before acoustic silence."
limitations:
  - "English-centric."
  - "Targets the turn-shift event itself, not pipeline policy decisions (barge-in vs turn-end) with separate operating points."
open_questions:
  - "Multilingual transfer of text-only turn-shift prediction (Spanish underserved)."
  - "Use as a soft signal AND-ed with acoustic endpointing rather than a standalone decision."
gap_score: 3
conceptual: true
---

Founding text-side entry point. Related work in jev-vad-poc positions against
it: TurnGPT scores the shift event; the semantic-VAD question design instead
asks two separate policy questions (barge-in, turn-end) with independent
operating points. Precursor of `ekstedt2022vap` (audio-side sibling) and
`umair2024turntaking` (LLM fusion).
