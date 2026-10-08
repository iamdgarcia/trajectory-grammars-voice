---
title: "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
year: 2024
venue: "arXiv 2406.12045 (2024-06-17); Sierra - verified via alphaXiv discovery, 2026-10-08"
arxiv_id: "2406.12045"
cite_key: "sierra2024taubench"
topic: "conversation_dynamics"
subtopics:
  - "agent benchmarks"
  - "customer service"
key_claims:
  - "Benchmarks language agents on tool use + user interaction + domain policy compliance (retail, airline)."
  - "pass^k metric over full trajectories; user simulated by LLM."
limitations:
  - "Full-episode success only; trajectory is data, not the object of analysis."
  - "No partial-observation decision theory; simulated users; no voice physics."
open_questions:
  - "Trajectory-level outcome taxonomy for deployed service agents."
gap_score: 3
conceptual: true
---

Existing KB cross-link: orchestration/taubench2024 (same work, latency axis). In the
conversation_dynamics topic it anchors the "full-episode success" evaluation paradigm that the
trajectory-grammars paper extends to partial observation. Note: tau2-bench dual-control
extension [verify arXiv 2506.07982]; tau2 trajectories appear in falsesuccess2026 (2606.09863).
