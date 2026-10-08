# Knowledge Base Schema

Every paper entry lives at `knowledge_base/topics/<topic>/papers/<cite_key>.md`.

## Frontmatter Fields

```yaml
---
title: "Full paper title"
year: 2024
venue: "NeurIPS / arXiv / ICML / ACM CSUR / IEEE TNNLS / ..."
arxiv_id: "2402.XXXXX"          # omit if no arXiv version
cite_key: "author2024keyword"   # matches BibTeX key and filename
topic: "ai_guardrails"          # matches topics/ folder name
subtopics:
  - "real-time"
  - "multimodal"
key_claims:
  - "Verbatim or close paraphrase of the paper's central empirical/theoretical claim"
limitations:
  - "Acknowledged limitation from the paper itself"
open_questions:
  - "Unresolved question or stated future work direction"
gap_score: 3      # 1=saturated (many follow-ups exist), 5=wide open (no direct follow-up)
conceptual: true  # true = contribution can be extended without new experiments
---
```

## Body

Free-form Markdown notes on:
- Why this paper is relevant to the topic
- Connections to other papers (use cite_key references)
- Potential use as a citation in a future paper

## Gap Score Guide

| Score | Meaning |
|-------|---------|
| 1 | Saturated — multiple papers already extend this work |
| 2 | Mostly covered — one or two direct follow-ups exist |
| 3 | Partial gap — follow-ups exist but leave open angles |
| 4 | Significant gap — identified as future work, no paper yet |
| 5 | Wide open — no follow-up work found in the literature |
