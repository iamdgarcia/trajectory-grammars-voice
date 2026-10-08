---
title: "Full-Duplex-Bench-v3: Benchmarking Tool Use for Full-Duplex Voice Agents Under Real-World Disfluency"
year: 2026
venue: "arXiv (verified via alphaXiv, 2026-10-05, jev-vad-poc)"
arxiv_id: "2604.04847"
cite_key: "fullduplexbenchv3"
topic: "semantic_vad"
subtopics:
  - "full-duplex benchmark"
  - "tool use"
  - "disfluency"
key_claims:
  - "Third FDB iteration: tool use under real-world disfluency for full-duplex voice agents."
limitations:
  - "Full-duplex S2S + tools; no cascade, no Spanish, no component-level floors."
open_questions:
  - "Interaction of turn decisions with tool-calling policies in cascades (cf. knowledge_base orchestration OG3/OG4)."
gap_score: 3
conceptual: true
---

FDB v3 adds tools + disfluency — exactly the two things a semantic VAD layer
sits between: turn decisions guard tool dispatch (veto false turn-ends before
a graph turn triggers tool round-trips). Cross-link:
`orchestration/papers/taubench2024`, orchestration gap OG3.
