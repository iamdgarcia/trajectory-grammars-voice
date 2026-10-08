---
title: "Gemini 1.5 Pro and Flash: Multimodal and Long-Context Capabilities"
year: 2024
venue: "Google DeepMind (deepmind.google)"
arxiv_id: ""
cite_key: "google2024geminivoice"
topic: "orchestration"
subtopics:
  - "long-context"
  - "realtime voice assistants"
key_claims:
  - "Long-context multimodal models enable spans of conversation/context to be held in a single prompt, which is the substrate vendor voice assistants (Gemini Live) build on."
  - "Cited in the published paper as the voice-assistant deployment of the Gemini family on the personal-assistant side of the cascade-vs-native trade."
limitations:
  - "Vendor documentation; long-context capability itself does not make a realtime loop."
  - "No latency or turn-taking guarantees published."
open_questions:
  - "Cost of re-prefilling a long session state vs carrying it (KV / summarised context) — bridges the forgetting-floor open problem."
gap_score: 3
conceptual: true
---

Vendor long-context anchor showing why cascade+long-context is the current
practical answer for stateful assistants, and why the orchestration-layer
question (what does the context/prefill cost do to the floor over a long
session) is the live engineering gap. Already cited in the published paper.
