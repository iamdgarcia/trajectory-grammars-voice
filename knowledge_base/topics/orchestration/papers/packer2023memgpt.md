---
title: "MemGPT: Towards LLMs as Operating Systems"
year: 2023
venue: "arXiv (UNVERIFIED — 2310.08560)"
arxiv_id: "2310.08560"
cite_key: "packer2023memgpt"
topic: "orchestration"
subtopics:
  - "hierarchical memory"
  - "context management"
key_claims:
  - "OS-style hierarchical memory with paging (context < main memory < external storage) lets agents exceed context limits; motivated by capability, not wall-clock latency."
key_verification_note: "VERIFY — author list/year from discovery-agent recall; rename cite_key once confirmed."
limitations:
  - "Paging policy is not deadline-aware; memory operations cost capability, not scheduling time."
open_questions:
  - "Deadline-aware context/eviction for long stateful sessions (the forgetting-floor open problem)."
gap_score: 4
conceptual: true
---

Seeds the long-session context-management open problem; relevant because the
orchestration target is long stateful sessions where prefill cost grows.
Verify before citing.
