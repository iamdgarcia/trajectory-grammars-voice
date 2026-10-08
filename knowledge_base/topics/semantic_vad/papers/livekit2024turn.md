---
title: "LiveKit Agents: Turn Detection plugin"
year: 2024
venue: "LiveKit docs, docs.livekit.io/agents/turns/turn-detector (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: ""
cite_key: "livekit2024turn"
topic: "semantic_vad"
subtopics:
  - "turn-end detection"
  - "text-based"
  - "product"
key_claims:
  - "Open turn-detection plugin classifying whether the user's partial transcript completes a turn; English model first, multilingual variant later; tuning surface = model choice + confidence threshold."
limitations:
  - "No per-language evaluations on public data; no tuned operating points; no barge-in/backchannel/side-talk distinction."
  - "Reported accuracy figures are vendor-published."
open_questions:
  - "Spanish per-language precision/recall (jev-vad-poc fills this for ES)."
gap_score: 4
conceptual: true
---

The text-side commercial-incumbent comparator. jev-vad-poc's related-work
section positions directly against it: same signal (transcript), missing
per-language evaluation and the policy split. Vendor figures (~89% vs
smart-turn ~94%) exist only in Daily's comparison blog — treat as
part-interested [unverified].
