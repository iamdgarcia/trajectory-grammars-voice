---
title: "ONNX Runtime: Quantization Overview (int4 weight quantization)"
year: 2024
venue: "ONNX Runtime docs, onnxruntime.ai (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: ""
cite_key: "onnx2024quantization"
topic: "semantic_vad"
subtopics:
  - "quantization"
  - "CPU inference"
key_claims:
  - "Weight-only int4 blockwise quantization trades minimal accuracy loss for 4x weight-memory reduction and CPU speedups on transformer blocks."
limitations:
  - "Vendor documentation, not a peer-reviewed evaluation."
open_questions:
  - "Accuracy drift of int4 on calibrated probability outputs (operating points depend on calibration)."
gap_score: 3
conceptual: true
---

The deployment vehicle: jev-vad's model artifact is int4-blockwise ONNX
(~206 MB), same as the Laya distribution and smart-turn's 8.7 MB ONNX.
Operating points (th=0.30 etc.) are conditional on this quantization.
