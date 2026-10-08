---
title: "pyannote.audio: Neural Building Blocks for Speaker Diarization"
year: 2020
venue: "Proceedings of ICASSP (DOI 10.1109/ICASSP40776.2020.9052969, verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: "1911.01255"
cite_key: "bredin2020pyannote"
topic: "semantic_vad"
subtopics:
  - "acoustic VAD"
  - "diarization"
key_claims:
  - "Neural building blocks (segmentation, diarization) as composable open components for speech pipelines."
limitations:
  - "Diarization-first; VAD a byproduct, not a policy layer."
open_questions:
  - "Speaker-aware turn policies (who is speaking matters for barge-in: user vs bot echo)."
gap_score: 3
conceptual: true
---

Cited in jev-vad-poc's acoustic-VAD lineage (alongside `webrtcvad`,
`silero2024vad`). In the investigated pipeline, bot-echo filtering during
barge-in uses speaker embeddings (IABTO-510) — the diarization connection.
