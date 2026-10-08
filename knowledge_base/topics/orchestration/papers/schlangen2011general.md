---
title: "A General, Abstract Model of Incremental Dialogue Processing"
year: 2011
venue: "EACL"
arxiv_id: ""
cite_key: "schlangen2011general"
topic: "orchestration"
subtopics:
  - "incremental processing"
  - "incremental dialogue"
key_claims:
  - "Dialogue processing can be described abstractly in terms of processing modules that handle input incrementally through start/derive/update functionality, with incrementality as a first-class modelling primitive."
  - "The model decouples (a) an increment arriving, (b) how much a module commits to, and (c) how downstream modules consume it — the formal seed of the three-clock decoupling in the orchestration-floor paper."
limitations:
  - "Abstract and formalism-level; it was written for pre-LLM statistical components and never materialized as a modern agent-orchestration runtime."
  - "Assumes left-to-right increments; no treatment of tool round-trips, background jobs, or model reentry."
open_questions:
  - "Reinstating the module/clock separation for modern LLM loops: incremental ASR -> incremental LLM -> incremental TTS with events, not graph wiring (the PoC is a faithful instantiation)."
gap_score: 4
conceptual: true
---

Strongest theoretical anchor for the event-driven framing: it already argues
that dialogue systems should be built from incrementally-communicating
modules, and that the module boundary (not the framework) is where latency
gets hidden. The orchestration-floor paper bridges this 2011 abstraction to
LLM/ReAct orchestration in latency terms.
