---
title: "LangGraph: Building Stateful Multi-Actor Applications with LLMs"
year: 2024
venue: "Software library / documentation (github.com/langchain-ai/langgraph)"
arxiv_id: ""
cite_key: "langgraph2024"
topic: "orchestration"
subtopics:
  - "graph orchestration"
  - "stateful agents"
key_claims:
  - "Graph-structured orchestration (nodes + conditional/static edges over a shared, checkpointed state) enables stateful LLM applications with resumability, human-in-the-loop, and deterministic control flow."
  - "Checkpointing gives every graph run a replayable state, which is the production reason serial LangGraph is chosen for long stateful sessions."
limitations:
  - "Graph wiring is static per run; concurrency, true streaming overlap, and realtime turn semantics are not first-class."
  - "Latency of checkpointing and state serialization is unaccounted in early design."
open_questions:
  - "Where graph nodes should yield to an event loop when a tool call or user barge-in arrives mid-node."
  - "Formal comparison of graph-serial vs event-concurrent scheduling for the same latency floor (orchestration-floor paper, Thm 1)."
gap_score: 3
conceptual: true
---

Orchestration-framework anchor — the production baseline (comprender /
razonar / resolver graph) in the product repo. Contrast with the
event-driven PoC: this is the serial-topology extreme where all three clocks
(generation, delivery, tool) are coupled in one node stack.
