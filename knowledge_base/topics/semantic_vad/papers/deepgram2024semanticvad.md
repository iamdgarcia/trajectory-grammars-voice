---
title: "Deepgram Voice Agent API: Endpointing and Turn Detection (Flux, Semantic VAD modes)"
year: 2024
venue: "Deepgram docs, developers.deepgram.com/docs/voice-agent (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: ""
cite_key: "deepgram2024semanticvad"
topic: "semantic_vad"
subtopics:
  - "semantic VAD"
  - "proprietary"
  - "endpointing"
key_claims:
  - "Commercial STT-native endpointing: semantic VAD mode decides end of speech from meaning rather than silence; Flux model adds server-side turn management (eot_timeout_ms, eot_threshold, eager end-of-turn with speculative response)."
limitations:
  - "Proprietary and cloud-hosted: weights, operating points, and per-language numbers uninspectable; transcript audio leaves the premises."
  - "Semantics opaque — cannot be re-tuned or audited per deployment/domain."
open_questions:
  - "Per-language accuracy of server-side semantic endpointing (Spanish unreported)."
gap_score: 4
conceptual: true
---

One of the three proprietary semantic-VAD anchors (with
`openai2024realtime`, `elevenlabs2025semantic`). In the investigated pipeline
the deployed Flux eot_timeout_ms went 600→800→3000 because pauses mid-turn
split phrases — evidence that opaque acoustic thresholds get tuned by trial
and error, which is the auditability argument for an inspectable semantic VAD.
