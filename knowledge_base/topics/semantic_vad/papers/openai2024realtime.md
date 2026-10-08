---
title: "OpenAI Realtime API Guide: Voice Activity Detection"
year: 2024
venue: "OpenAI docs, platform.openai.com/docs/guides/realtime (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: ""
cite_key: "openai2024realtime"
topic: "semantic_vad"
subtopics:
  - "semantic VAD"
  - "proprietary"
key_claims:
  - "Realtime API exposes a semantic turn-detection mode alongside server-side acoustic VAD inside the same proprietary API."
limitations:
  - "Proprietary; semantics opaque; no per-language operating points."
open_questions:
  - "Comparison of proprietary semantic modes against inspectable detectors on public data."
gap_score: 4
conceptual: true
---

Second proprietary anchor (`deepgram2024semanticvad`,
`elevenlabs2025semantic` are the others). Collectively they prove demand for
semantic endpointing; none is inspectable or multilingually evaluated — the
market gap jev-vad-poc states in its abstract.
