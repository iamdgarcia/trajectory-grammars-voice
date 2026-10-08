---
title: "Evaluating Prosodic Processing for Incremental Speech Synthesis"
year: 2012
venue: "Interspeech (verified via Crossref, 2026-09-01)"
arxiv_id: ""
cite_key: "baumann2012prosodic"
topic: "orchestration"
subtopics:
  - "incremental processing"
  - "revocable output"
key_claims:
  - "InproTK is a toolkit for incremental incremental dialogue processing enabling incremental speech recognition, incremental language generation, and incremental (revocable) speech synthesis."
key_verification_note: "VERIFIED 2026-09-01 via Crossref — Baumann & Schlangen, Evaluating Prosodic Processing for Incremental Speech Synthesis, Interspeech 2012, pp. 438-441. Demonstrates InproTK incremental-synthesis revocability."
limitations:
  - "Pre-LLM statistical component toolkit; no agent-orchestration or tool-execution semantics; no latency-floor arithmetic."
open_questions:
  - "Reinstating the incremental-module / revocable-unit model for modern LLM agent loops (bridged in the two-floor paper, §2)."
gap_score: 4
conceptual: true
---

InproTK (Baumann, Schlangen, et al.) is the closest *formal ancestor* for the draft paper's
cessation floor: it demonstrates that output increments are revocable/cancellable behaviours.
The draft cites it to differentiate: revocability is a capability, not a lower-bound
latency-floor account of an agent's stop path.
