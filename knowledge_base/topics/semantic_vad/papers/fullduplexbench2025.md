---
title: "Full-Duplex-Bench: A Benchmark to Evaluate Full-Duplex Spoken Dialogue Models on Turn-Taking Capabilities"
year: 2025
venue: "arXiv (verified via alphaXiv, 2026-10-05, jev-vad-poc)"
arxiv_id: "2503.04721"
cite_key: "fullduplexbench2025"
topic: "semantic_vad"
subtopics:
  - "full-duplex benchmark"
  - "turn-taking"
key_claims:
  - "First benchmark measuring turn-taking and overlap handling of full-duplex spoken dialogue models (Lin et al.)."
limitations:
  - "Benchmarks native full-duplex S2S models; cascade pipelines with separate components out of scope."
  - "Outcomes, not formal floors."
open_questions:
  - "Cascade-specific turn-taking evaluation (semantic VAD layer included)."
gap_score: 3
conceptual: true
---

Original of the FDB line (`fullduplexbenchv15`, `fullduplexbenchv2`,
`fullduplexbenchv3` follow). In jev-vad-poc it anchors the claim that
evaluation pressure exists but targets native S2S, leaving cascade
component-level detectors (Silero, smart-turn, semantic VADs) without a
labeled multilingual benchmark — the benchmark contribution's motivation.
