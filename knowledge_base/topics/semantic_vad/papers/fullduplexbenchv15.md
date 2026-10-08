---
title: "Full-Duplex-Bench v1.5: Evaluating Overlap Handling for Full-Duplex Speech Models"
year: 2025
venue: "arXiv (verified via alphaXiv, 2026-10-05, jev-vad-poc)"
arxiv_id: "2507.23159"
cite_key: "fullduplexbenchv15"
topic: "semantic_vad"
subtopics:
  - "full-duplex benchmark"
  - "overlap handling"
key_claims:
  - "Extends Full-Duplex-Bench to overlap handling: whether a duplex model can speak while the user is also speaking without collapsing."
limitations:
  - "Native full-duplex S2S only; cascade out of scope."
open_questions:
  - "Overlap-handling metrics for cascade pipelines (component-level VAD + policy)."
gap_score: 3
conceptual: true
---

FDB v1 → v1.5 (`fullduplexbench2025`) adds the overlap axis. Relevant to the
barge-in question: overlap tolerance is what a semantic VAD's backchannel/
side-talk discrimination operationalizes on the cascade side.
