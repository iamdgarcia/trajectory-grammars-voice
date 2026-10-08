---
title: "Moshi: A Speech-Text Foundation Model for Real-Time Dialogue"
year: 2024
venue: "arXiv (verified via alphaXiv, 2026-10-05, jev-vad-poc)"
arxiv_id: "2410.00037"
cite_key: "defossez2024moshi"
topic: "semantic_vad"
subtopics:
  - "full-duplex native"
  - "speech-text foundation model"
key_claims:
  - "Native full-duplex spoken dialogue: parallel streams for user and agent audio remove the explicit endpointing step (Défossez, Mazaré, Orsini, Royer, Pérez, Jégou, Grave, Zeghidour — Kyutai)."
limitations:
  - "No analytical latency model; interruption handling empirical/demo."
  - "Parallel-stream architecture diverges from cascade; multilingual coverage centered on English/French."
open_questions:
  - "Formal cessation/onset floors per architecture (orchestration gap OG2)."
  - "Whether native full-duplex obviates or still needs semantic policy layers for banking-grade domains."
gap_score: 3
conceptual: true
---

The 'endpointing disappears' alternative that jev-vad-poc must argue against:
native full-duplex removes the timer but not the policy (what to do with
backchannels/side-talk still needs deciding), and cascade remains dominant in
regulated deployments. Related: `openai2024realtime`, `google2025gemini`.
