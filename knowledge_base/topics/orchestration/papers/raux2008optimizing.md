---
title: "Optimizing Endpointing Thresholds using Dialogue Features for a Voice Search System"
year: 2008
venue: "SIGdial Workshop on Discourse and Dialogue"
arxiv_id: ""
cite_key: "raux2008optimizing"
topic: "orchestration"
subtopics:
  - "endpointing"
  - "barge-in"
key_claims:
  - "Endpointing thresholds tuned on dialogue features reduce both end-of-turn detection latency and barge-in errors compared with fixed thresholds."
  - "Endpointing is a latency/reliability trade: firing early risks cutting the user off (barge-in), firing late adds silence to the floor."
limitations:
  - "Voice-search domain with turn-based ASR; threshold-based endpointers, not generative streaming agents."
  - "Empirical and domain-specific; no lower-bound analysis."
open_questions:
  - "Endpointing (T0->T1 detect) contribution to the V2V floor in streaming LLM agents."
  - "Barge-in reaction latency as a formal, architecture-dependent bound (orchestration-floor paper, Thm 2: detect/decide/cease/resume)."
gap_score: 4
conceptual: true
---

The endpointing half of the barge-in story; paired with its 2012 follow-up
(`raux2012bargein`, provisional) which extracts deployed response/barge-in
tradeoff lessons. Already cited in the published cascade_voice_latency paper.
