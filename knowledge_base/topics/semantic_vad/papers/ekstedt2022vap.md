---
title: "Voice Activity Projection: Self-Supervised Learning of Turn-Taking Events"
year: 2022
venue: "Proceedings of Interspeech (DOI 10.21437/Interspeech.2022-10716, verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: "2203.03955"
cite_key: "ekstedt2022vap"
topic: "semantic_vad"
subtopics:
  - "turn-shift prediction"
  - "self-supervised"
  - "audio-based"
key_claims:
  - "Voice Activity Projection predicts future voice activity of both speakers from audio, self-supervised, enabling continuous turn-taking without explicit end-of-turn classification."
limitations:
  - "Audio-only: conditions on when and how speech happens, not on the content of what was said."
  - "Event prediction, not per-decision operating points."
open_questions:
  - "Fusing projection-style continuous prediction with transcript-conditioned policy decisions."
gap_score: 3
conceptual: true
---

The audio-side sibling of TurnGPT (`ekstedt2020turngpt`). jev-vad-poc cites it
as the canonical example of acoustic/prosodic conditioning that cannot judge
turn-end semantics ("...un billete de ida" can sound prosodically complete).
Complementarity (audio sees truncation/prosody, text sees completeness) is the
architectural argument for serial acoustic→semantic veto.
