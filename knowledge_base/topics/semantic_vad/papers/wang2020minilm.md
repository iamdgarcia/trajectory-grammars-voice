---
title: "MiniLM: Deep Self-Attention Distillation for Task-Agnostic Compression of Pre-Trained Transformers"
year: 2020
venue: "Advances in NeurIPS 33 (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: "1902.09662"
cite_key: "wang2020minilm"
topic: "semantic_vad"
subtopics:
  - "distillation"
  - "efficient inference"
key_claims:
  - "Deep self-attention distillation compresses transformer encoders task-agnostically, preserving quality at a fraction of the size."
limitations:
  - "Pre-ModernBERT era; English-centric benchmarks."
open_questions:
  - "Distilling question-format decision models below int4 ONNX sizes for realtime gates."
gap_score: 3
conceptual: true
---

Cited in jev-vad-poc as the distillation precedent behind the CPU-viable
model-size argument (small encoder + int4 = per-decision 100-200 ms).
