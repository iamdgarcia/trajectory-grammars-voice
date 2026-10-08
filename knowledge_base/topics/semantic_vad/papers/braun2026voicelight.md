---
title: "Voice-Light: A Full-Duplex Cascaded Voice Agent with Causal Turn-Taking and Speculative Generation"
year: 2026
venue: "arXiv (2609.20995, 2026-09-17); solo author Bertil Braun — full text read and verified via alphaXiv MCP, 2026-10-08"
arxiv_id: "2609.20995"
cite_key: "braun2026voicelight"
topic: "semantic_vad"
subtopics:
  - "speculative generation"
  - "full-duplex cascade"
  - "turn commitment"
key_claims:
  - "Cascaded ASR-LLM-TTS with PRIVATE speculative generation: candidate text+PCM generated during user speech, kept private until final-ASR + transcript-revision checks promote them (cosmetic revisions preserve work; lexical change invalidates)."
  - "Speculation trigger is acoustic: after 80 ms of low Silero speech probability the causal adapter gets 80 ms to open a candidate; Silero fallback at 160 ms. The turn signal is NOT used as a commit gate."
  - "HONEST NEGATIVE RESULT: learned completion checkpoint at locked eval (1,673 silence candidates) reached only 12.53% EOT recall at 2.70% false-cutoff vs 95.60% for Silero timing policy; no swept detector met the joint gate (<=5% false cutoff, >=70% recall, <=800 ms p95). Deployed hybrid controller, not learned policy."
  - "36-turn case study: 758 ms median final-VAD to first server audio; promoted-speculation turns 667 ms vs 1,513 ms without promotion (observational, confounded — not claimed causal)."
  - "Invariants: causal turn features, onset ducks but only stronger evidence commits cancellation, generation IDs + cancellation barriers reject stale text/PCM, history = only browser-acknowledged audio."
limitations:
  - "English-only; dedicated GPU (Qwen3-4B + Kyutai TTS); single-author instrumented case study (3 sessions, 36 turns), not a controlled eval."
  - "Learned turn-taking adapter failed the locked eval — the paper keeps timing baselines."
  - "Kyutai TTS fixed first-frame cost is the largest warm downstream cost."
open_questions:
  - "Would a text-side semantic gate (jev-vad on the interim) open speculation candidates EARLIER or more precisely than the 80 ms acoustic rule? SV4's unanswered question."
  - "Promotion-by-revision-type: what fraction of stt.final vs last-interim differences are cosmetic vs lexical in production Spanish? (SV4 reconcile cost, still unmeasured.)"
gap_score: 3
conceptual: true
---

Closest published relative of gap SV4 (speculative dispatch): proves private
speculation + promotion checks work in a deployed cascade and quantifies the
win (~850 ms when promotion succeeds), but its speculation trigger is a fixed
acoustic-pause rule (80/160 ms) and its learned turn signal FAILED the locked
evaluation. Does not use transcript semantics to gate speculation. English,
GPU, solo project. Composes with `jung2026speculativetool` (tool-call
speculation from partials, rule-based) — neither paper gates speculation with
a semantic end-of-turn signal on the interim transcript. That combination is
still open and is exactly what jev-vad's veto signal could provide.
