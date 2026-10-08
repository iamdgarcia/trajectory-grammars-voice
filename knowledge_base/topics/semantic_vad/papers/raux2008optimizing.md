---
title: "Optimizing Endpointing Thresholds using Dialogue Features in a Spoken Dialogue System"
year: 2008
venue: "SIGdial Workshop on Discourse and Dialogue (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: ""
cite_key: "raux2008optimizing"
topic: "semantic_vad"
subtopics:
  - "endpointing"
  - "threshold tuning"
key_claims:
  - "Endpointing thresholds tuned on dialogue features reduce both end-of-turn latency and barge-in errors vs fixed thresholds; endpointing is a latency/reliability trade."
limitations:
  - "Voice-search domain, turn-based ASR, threshold endpointers."
  - "Empirical; no lower-bound analysis; conditions on when/how speech happens, not content."
open_questions:
  - "Content-conditioned endpointing (the semantic-VAD move) in streaming agents."
gap_score: 4
conceptual: true
---

The pre-LLM ancestor of the whole semantic-endpointing program: Raux & Eskenazi
already framed endpointing as a decision with error costs; what changed with
jev-vad-class systems is that the condition can read the transcript, not just
dialogue metadata. Cross-link: orchestration papers `raux2008optimizing`
(entry shared with orchestration topic).
