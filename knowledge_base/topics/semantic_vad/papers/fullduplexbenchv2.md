---
title: "Full-Duplex-Bench-v2: A Multi-Turn Evaluation Framework for Duplex Dialogue Systems with a Streaming Speech Dialogue Simulator"
year: 2025
venue: "arXiv (verified via alphaXiv, 2026-10-05, jev-vad-poc)"
arxiv_id: "2510.07838"
cite_key: "fullduplexbenchv2"
topic: "semantic_vad"
subtopics:
  - "full-duplex benchmark"
  - "multi-turn evaluation"
key_claims:
  - "Multi-turn duplex evaluation with a streaming speech dialogue simulator replacing scripted user audio."
limitations:
  - "Duplex dialogue systems; no cascade component benchmarks."
open_questions:
  - "Simulator-driven multi-turn evaluation of cascade turn policies."
gap_score: 3
conceptual: true
---

FDB v2 (`fullduplexbench2025`): simulator-based multi-turn. The simulator idea
(keep feeding a frozen detector realistic continuation audio instead of single
cuts) is transferable to benchmarking semantic VADs beyond single-utterance
labels — noted as a jev-vad benchmark limitation.
