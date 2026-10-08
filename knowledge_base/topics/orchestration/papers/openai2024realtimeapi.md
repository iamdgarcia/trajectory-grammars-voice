---
title: "Introducing the Realtime API"
year: 2024
venue: "OpenAI product documentation (openai.com)"
arxiv_id: ""
cite_key: "openai2024realtimeapi"
topic: "orchestration"
subtopics:
  - "full-duplex native voice"
  - "realtime tool calling"
key_claims:
  - "A single speech-in/speech-out API exposes native voice + built-in function calling (tools) in a session, so realtime agentic voice applications no longer need an external ASR/LLM/TTS composition."
  - "The vendor performs endpointing and transmits the user's turn; tool calls and their results are exchanged within the same session."
limitations:
  - "Vendor black box: latency characteristics and tool-scheduling internals are undocumented and non-reproducible."
  - "Cost per session is high relative to cascades; no formal guarantees."
open_questions:
  - "How the vendor schedules tool round-trips relative to turn-taking, and whether the type-A/B/C tool-hiding model predicts its perceived latency."
gap_score: 4
conceptual: true
---

Industrial full-duplex point of reference for tool-calling voice agents;
motivates why orchestrating tools *off* the critical path matters in
cascades (the PoC's core move). Already cited in the published
cascade_voice_latency paper.
