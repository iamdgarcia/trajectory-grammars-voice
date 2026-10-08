---
title: "A General, Abstract Model of Incremental Dialogue Processing"
year: 2011
venue: "Proceedings of EACL 2011, pp. 51-60 (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: ""
cite_key: "schlangen2011incremental"
topic: "semantic_vad"
subtopics:
  - "incremental processing"
  - "architecture"
key_claims:
  - "A general abstract model (modules + incremental units) in which downstream components add, revise, and revoke hypotheses as input arrives: the architectural license for treating endpointing as a continuously revised decision instead of a one-shot timer."
limitations:
  - "Pre-neural, pre-LLM; never materialized into modern agent runtimes."
open_questions:
  - "Incremental revocation semantics in modern frame-based pipelines (e.g. dispatch-on-interim + reconcile-on-final)."
gap_score: 3
conceptual: true
---

The architecture citation jev-vad-poc uses to justify: (a) the semantic veto
revising the acoustic decision, and (b) forward work on dispatching the LLM
from the last interim transcript and reconciling when the final arrives.
Shared with orchestration topic (`schlangen2011general`).
