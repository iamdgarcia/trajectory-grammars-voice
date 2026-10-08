---
title: "Moshi: A Speech-Text Foundation Model for Real-Time Dialogue"
year: 2024
venue: "arXiv (2410.00037)"
arxiv_id: "2410.00037"
cite_key: "defossez2024moshi"
topic: "orchestration"
subtopics:
  - "full-duplex native voice"
  - "interruption handling"
key_claims:
  - "An end-to-end full-duplex speech model can stream audio in and out with ~200 ms latency using a text-stream supervision branch, supporting natural concurrent dialogue including interruption handling."
  - "Full-duplex audio modelling is the native contrast to cascade pipelines: no ASR/LM/TTS stage boundaries, hence no per-stage latency floor."
limitations:
  - "Demonstrated empirically; gives no formal latency lower bounds or reactive/barge-in guarantees."
  - "Higher operational cost and less flexible tool use than cascades in practice."
open_questions:
  - "Formal interruption-reaction (cessation) bounds for native full-duplex vs cascade — the orchestration-floor Thm 2 contrast."
  - "Whether native models can be extended with the same background-tool/persistent-execution semantics."
gap_score: 4
conceptual: true
---

The full-duplex architecture class of the published paper's comparison;
reused as the baseline the orchestration-floor results are contrasted
against (its ~codec-frame cessation vs cascade audio-in-flight cessation).
Already cited in the published cascade_voice_latency paper.
