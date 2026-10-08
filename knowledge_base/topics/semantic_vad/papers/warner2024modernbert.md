---
title: "Smarter, Better, Faster, Longer: A Modern Bidirectional Encoder for Fast, Memory Efficient, and Long Context Sequence Modeling"
year: 2024
venue: "arXiv (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: "2412.13663"
cite_key: "warner2024modernbert"
topic: "semantic_vad"
subtopics:
  - "efficient encoder"
key_claims:
  - "ModernBERT: hardware-aware bidirectional encoder with 8k context, fast and memory-efficient vs prior BERT-class models."
limitations:
  - "English-centric."
open_questions:
  - "Realtime decision workloads (ms budgets) beyond classification benchmarks."
gap_score: 3
conceptual: true
---

The architecture family (ModernBERT-class encoders) that mmBERT
(`mmbert2025`) extends multilingually. Cited in jev-vad-poc for why a single
non-autoregressive encoder pass can fit a per-decision ~100-200 ms CPU budget.
