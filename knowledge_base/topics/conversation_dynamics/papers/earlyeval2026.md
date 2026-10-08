---
title: "EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction"
year: 2026
venue: "arXiv 2609.02783 (2026-09-02); SJTU / SMU / ECNU - verified via alphaXiv discovery, 2026-10-08"
arxiv_id: "2609.02783"
cite_key: "earlyeval2026"
topic: "conversation_dynamics"
subtopics:
  - "early outcome prediction"
  - "agent evaluation"
key_claims:
  - "Predicts agent-task outcomes early in the episode to cut offline evaluation cost."
  - "Ranking over full episodes for eval pruning; not live in-conversation decisioning."
limitations:
  - "Offline evaluation setting: no live partial-transcript prediction inside a running conversation."
  - "No decision-time guarantee; no voice; no banking KPIs."
open_questions:
  - "Whether early-prediction machinery transfers from eval pruning to live intervention."
gap_score: 4
conceptual: true
---

Companion early-prediction work: uses trajectory prefixes to prune expensive agent evaluation.
Establishes that partial trajectories carry outcome signal for LLM agents; differs from the a5
angle in setting (offline eval vs live intervention) and guarantees (none vs stopping rule).
