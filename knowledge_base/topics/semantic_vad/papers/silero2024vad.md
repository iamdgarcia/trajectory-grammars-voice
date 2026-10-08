---
title: "Silero VAD: Pre-trained Enterprise-grade Voice Activity Detector"
year: 2024
venue: "GitHub, snakers4/silero-vad (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: ""
cite_key: "silero2024vad"
topic: "semantic_vad"
subtopics:
  - "acoustic VAD"
  - "baseline"
key_claims:
  - "Enterprise-grade neural acoustic VAD, ~1 ms/classification, deployed as the default speech-activity gate in agent frameworks (Pipecat, LiveKit, others)."
limitations:
  - "Acoustic only: decides whether someone is speaking, never what to do about it — no barge-in policy, no turn-end semantics."
  - "Vendor-published metrics only."
open_questions:
  - "Silero added a semantic head in later versions (v5+) — public per-language numbers still missing."
gap_score: 4
conceptual: true
---

The baseline every semantic VAD composes with. In the serving pipeline
investigated (iabto-ms-bc) Silero runs always as the clock/gate and never
decides the turn — the clean division of labor: acoustic gate → acoustic
turn model (smart-turn) → semantic veto (jev-vad).
