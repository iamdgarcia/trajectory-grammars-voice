---
title: "Fast Inference from Transformers via Speculative Decoding"
year: 2023
venue: "ICML"
arxiv_id: "2211.17192"
cite_key: "leviathan2023fast"
topic: "orchestration"
subtopics:
  - "decode acceleration"
  - "speculative execution"
key_claims:
  - "A small draft model proposes c tokens which the target model verifies in a single forward pass, yielding lossless 2-3x decode speedups by trading draft parallelism for serial decode."
limitations:
  - "Requires a draft model and its agreement rate with the target bounds gains."
  - "Accelerates the decode term only; does not touch tool round-trips, first-token latency, or orchestration."
open_questions:
  - "Applying the speculative pattern to tool-call prediction/prefetch instead of just token prediction (the hideability window of the orchestration-floor tool-hiding result)."
gap_score: 3
conceptual: true
---

The reducible-decode lever: it shrinks lambda_lm^r but never the floor. The
orchestration paper cites it when contrasting reducible (maskable/hideable)
vs irreducible latency. Already cited in the published paper and stubbed in
the ai_guardrails topic.
