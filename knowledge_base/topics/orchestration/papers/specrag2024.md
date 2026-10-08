---
title: "Speculative RAG: An Optimized RAG with Speculative Decoding"
year: 2024
venue: "arXiv (UNVERIFIED — 2407.08223)"
arxiv_id: "2407.08223"
cite_key: "specrag2024"
topic: "orchestration"
subtopics:
  - "tool hiding"
  - "retrieval overlap"
key_claims:
  - "A lightweight specialist 'retriever' draft model proposes candidate rationales/evidence before the target model gathers evidence and answers, overlapping retrieval round-trip time with drafting."
key_verification_note: "VERIFY — author/year/venue from discovery-agent recall; rename cite_key to author-based form once confirmed."
limitations:
  - "Retrieval-specific; relies on a compatible specialist draft model."
  - "Empirical existence proof of an overlap window; no composition rule for when hiding is possible."
open_questions:
  - "Generalizing retrieval-overlap to arbitrary tool round-trips (the hideability window W in the orchestration-floor Thm 3)."
gap_score: 3
conceptual: true
---

Concrete instance of the tool-hiding 'type B' class: tool/retrieval RTT
overlapped with generation. Cited in the orchestration-floor paper's
tool-hiding section.
