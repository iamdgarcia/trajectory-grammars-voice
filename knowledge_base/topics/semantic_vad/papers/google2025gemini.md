---
title: "Gemini Live API"
year: 2025
venue: "Google docs, ai.google.dev/gemini-api/docs/live (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: ""
cite_key: "google2025gemini"
topic: "semantic_vad"
subtopics:
  - "native voice stack"
  - "proprietary"
key_claims:
  - "Native speech-to-speech API with built-in voice activity and turn handling; also offers Chirp 3 STT with speech_end_timeout (500 ms floor) and endpointing_sensitivity in the speech-to-text product line."
limitations:
  - "Proprietary; endpointing floor fixed by the vendor (500 ms); semantics opaque."
open_questions:
  - "Whether STT-native endpointing floors can be hidden under client-side speculative dispatch (jev-vad-poc forward work)."
gap_score: 4
conceptual: true
---

Represents the STT-native endpointing family in jev-vad-poc's latency
analysis: the 500 ms `speech_end_timeout` floor is the binding constraint that
a fast text-side decision (p99 268 ms cloud) can hide under, enabling
dispatch-on-interim with a semantic veto.
