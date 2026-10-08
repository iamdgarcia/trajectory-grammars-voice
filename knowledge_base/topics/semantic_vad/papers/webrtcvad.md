---
title: "WebRTC Voice Activity Detection (webrtcvad)"
year: 2024
venue: "WebRTC source, googlesource.com (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: ""
cite_key: "webrtcvad"
topic: "semantic_vad"
subtopics:
  - "acoustic VAD"
  - "baseline"
key_claims:
  - "Classic lightweight GMM-based acoustic VAD shipped in WebRTC; the 'dumb but free' baseline of the VAD lineage."
limitations:
  - "Frame-level energy/GMM decisions only; no semantics, no policy."
open_questions:
  - "—"
gap_score: 5
conceptual: true
---

Baseline anchor of the acoustic-VAD lineage in jev-vad-poc
(`webrtcvad` → `bredin2020pyannote` → `silero2024vad`). Saturation note: the
acoustic half of the problem is solved technology; everything open lives
text-side.
