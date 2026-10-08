---
title: "TRACER: Early Failure Detection for Task-Oriented Dialogue"
year: 2026
venue: "arXiv 2607.03974 (2026-07-04); EMNLP 2026, UT San Antonio - full text read and verified via alphaXiv MCP, 2026-10-08"
arxiv_id: "2607.03974"
cite_key: "nourbakhsh2026tracer"
topic: "conversation_dynamics"
subtopics:
  - "early failure detection"
  - "partial-dialogue forecasting"
  - "trajectory features"
key_claims:
  - "Formulates TOD failure prediction as partial-dialogue forecasting: one supervised example per visible prefix, terminal label shared across prefixes."
  - "Dual-stream model: 5-dim belief-state trajectory features (oscillation, coverage rate, conflict count, fill velocity, domain shifts) + serialized belief-state text (RoBERTa), fused by MLP."
  - "MultiWOZ 2.4: AUC 0.741 oracle / 0.617 generated belief states; F1 0.463/0.370; EDS 0.727; det turn 1.36 under FPR<=0.15 (tau=0.7788 frozen)."
  - "Thresholded recovery trigger: template-based recovery beats fine-tuned T5 generation on targetedness."
  - "Useful failure signals visible from 25% of the dialogue (fixed-context analysis)."
limitations:
  - "Learned classifier only: no stopping rule, no decision-time guarantee, threshold tuned on dev set."
  - "Single binary outcome (eventual failure/success); no outcome taxonomy (abandonment, handoff, compliance escape)."
  - "Text-chat benchmarks (MultiWOZ/SGD/ABCD), English-only; no voice physics (endpointing, barge-in, tool RTT)."
  - "Weak zero-shot transfer to SGD (AUC 0.494)."
open_questions:
  - "Interactive settings with live recovery left as future work by the authors."
  - "Does trajectory-signal forecasting transfer to voice-agent state spaces (tool calls, endpointing, barge-ins)?"
gap_score: 4
conceptual: true
---

Nearest neighbor to the trajectory-grammars angle (a5). Verified live: full text read.
TRACER instantiates a fixed-threshold intervention policy over a learned failure score; the a5
paper generalizes this into a sequential stopping rule with decision-time guarantees (SPRT /
confidence sequences), multi-class banking outcomes, voice-physics state spaces, and floor-based
intervention-latency accounting. Its EDS and detection-turn metrics are reused with credit in
the a5 evaluation protocol. Failure taxonomy (information incompleteness, contradiction,
state instability, task drift) maps naturally onto grammar-level drift statistics.
Citation note: its related-work section supplied verified anchors: walker1997paradise,
higashinaka2016breakdown, chang2019derailment, plus MultiWOZ/SGD/ABCD lineage.
