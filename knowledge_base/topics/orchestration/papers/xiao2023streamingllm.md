---
title: "Efficient Streaming Language Models with Attention Sinks"
year: 2023
venue: "arXiv (2309.17453)"
arxiv_id: "2309.17453"
cite_key: "xiao2023streamingllm"
topic: "orchestration"
subtopics:
  - "streaming inference"
  - "context management"
key_claims:
  - "Keeping only the recent sliding-window tokens plus an 'attention sink' (the earliest tokens) lets a model generate over arbitrarily long streams with flat memory and stable perplexity."
  - "Streaming correctness is thus decoupled from full-history retention — you can stream without paying for the whole context."
limitations:
  - "Anti-forgetting by design (keeps full history), so it gives no forgetting/viction policy for agent tasks or latency budgets."
  - "Optimized for generation persistence, not for interactive agent deadlines or tool interplay."
open_questions:
  - "Deadline-aware context/eviction policy layered on streaming models ('what the agent forgets and when' as a latency lever — forgetting-floor angle)."
gap_score: 4
conceptual: true
---

The streaming-inference substrate any latency-aware agent context policy must
respect; also a bridge entry to the ai_guardrails topic (already a stub
there) and to the forgetting-floor open problem in the orchestration paper.
Already cited in the published cascade_voice_latency paper.
