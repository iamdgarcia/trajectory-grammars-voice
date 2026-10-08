---
title: "tau-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains"
year: 2024
venue: "arXiv (UNVERIFIED — 2406.12045)"
arxiv_id: "2406.12045"
cite_key: "taubench2024"
topic: "orchestration"
subtopics:
  - "agent evaluation"
  - "latency-price axes"
key_claims:
  - "A realistic tool-agent-user benchmark whose primary metrics are accuracy and liveness/wait time, with an explicit price axis — the closest existing standard for tool-agent latency evaluation."
key_verification_note: "VERIFY — author/year/venue from discovery-agent recall; rename cite_key once confirmed."
limitations:
  - "Text-domain (retail, airline); latency is an outcome metric, not predicted from tool-DAG structure."
  - "Does not cover voice/streaming turn-taking, barge-in, or EOU latency."
open_questions:
  - "Extending tau-bench-style liveness metrics to realtime voice agents (the RAES stack / eval angle)."
gap_score: 3
conceptual: true
---

Evaluation baseline the orchestration-floor paper's empirical discussion can
borrow 'liveness under a latency budget' from; verify before citing.
