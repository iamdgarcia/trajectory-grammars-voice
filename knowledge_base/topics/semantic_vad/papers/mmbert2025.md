---
title: "mmBERT: A Modern Multilingual Encoder with Annealed Language Learning"
year: 2025
venue: "arXiv preprint arXiv:2509.06888 (verified via alphaXiv, 2026-10-05, jev-vad-poc)"
arxiv_id: "2509.06888"
cite_key: "mmbert2025"
topic: "semantic_vad"
subtopics:
  - "multilingual encoder"
  - "efficient inference"
key_claims:
  - "ModernBERT-class multilingual encoder (Marone, Weller, Fleshman, Yang, Lawrie, Van Durme, JHU) covering 1100+ languages with annealed language learning; decoder-only-free, single forward pass."
limitations:
  - "Base model, not turn-aware: turn decisions require a task head or question format on top."
open_questions:
  - "Fine-tuned, non-question-format multilingual turn detectors on its backbone."
gap_score: 4
conceptual: true
---

Backbone of the jev-vad System-1 model (Laya = mmBERT-base + typed-question
head, int4 ONNX ~206 MB). Its existence is what makes text-only, multilingual,
CPU-viable turn decisions possible in 2025 — the enabling technology argument
in jev-vad-poc §3 ("On model choice": the contribution is the question design,
any calibrated small model is swappable). Related: `warner2024modernbert`.
