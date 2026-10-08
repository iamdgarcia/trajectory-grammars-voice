---
title: "Pipecat Smart-Turn Detection (Latency-Mitigating turn detection, v3.2 ONNX)"
year: 2024
venue: "GitHub, pipecat-ai/smart-turn (verified in jev-vad-poc bib, 2026-10-06; latency verified locally 2026-10-06)"
arxiv_id: ""
cite_key: "pipecat2024smartturn"
topic: "semantic_vad"
subtopics:
  - "turn-end detection"
  - "audio-based"
  - "CPU inference"
key_claims:
  - "Open-weights audio-conditioned turn-end model (Daily/Pipecat): whisper-features over the buffered mic audio decide if the user will keep speaking; ships as 8.7 MB ONNX in the wheel, CPU-viable."
  - "VERIFIED (local i7-10850H, 1 core, 50 runs): p50 146 ms, p90 205 ms, max 272 ms per inference."
limitations:
  - "Audio-only: blind to transcript content — an incomplete utterance with falling prosody reads complete."
  - "English-trained; no Spanish evaluation published; no barge-in/backchannel distinction."
  - "Per-inference cost instrumented but not reported in product docs."
gap_score: 4
conceptual: true
---

The EOT incumbent in the investigated pipeline (SmartTurnStopStrategy,
silence ceiling 3 s). Complementary, not redundant, with text-side semantic
VAD: serial acoustic→semantic veto is the correct design; two independent
decisions would duplicate turn-ends. Verified numbers live in
`jev-vad-poc/docs/investigacion-smartturn-vs-semantico.md`.
