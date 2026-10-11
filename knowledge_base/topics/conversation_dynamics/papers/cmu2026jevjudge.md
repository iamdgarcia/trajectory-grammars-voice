---
title: "JEV-as-a-Judge: Accept When Confident, Escalate When Unsure"
year: 2026
venue: "arXiv (Carnegie Mellon University)"
arxiv_id: "2609.26550"
cite_key: "cmu2026jevjudge"
topic: "conversation_dynamics"
subtopics:
  - "decision-models"
  - "llm-routing"
  - "evaluation"
key_claims:
  - "JEV, a decision-only judge returning label probabilities instead of text, can replace reasoning LLM-as-a-judge pipelines for accept/escalate decisions: accept when confident, escalate to a reasoning judge when unsure"
  - "Decision-only judging achieves large cost reductions at comparable or better agreement than textual judging on evaluation tasks"
limitations:
  - "Binary/confined label spaces; free-form qualitative assessment remains out of reach for decision-only judges"
open_questions:
  - "How decision-only judges compose with sequential stopping rules (connects to CD2 SPRT gap)"
  - "Calibration of the escalate-when-unsure threshold in production voice-agent KPI contexts"
gap_score: 3
conceptual: true
---

# JEV-as-a-Judge (CMU, 2026-09-22)

Highest-attention academic validation of the tiny decision-model ("Jev") wave: 331 votes, 7.4k views
on alphaXiv within two weeks. Positions decision-only models as a *judge* tier: confident decisions
are accepted at tiny-model cost, uncertain ones escalate to a reasoning LLM.

## Relevance to the factory

- Validates the mechanism assumed by the **Jev Mini Bench** product (iamdgarcia/jev-mini-bench): tiny
  decision models as first-class routing components, not toys. The escalate-when-unsure pattern is
  exactly a cascade with a calibrated confidence gate.
- Direct connection to **CD2 (SPRT stopping rule for conversation outcomes)**: the escalate-when-unsure
  threshold is a fixed-sample decision; CD2's contribution would be the sequential version over
  multi-turn posteriors. This paper strengthens the motivation section of trajectory_grammars_voice.
- Connects to jev_vad: a VAD endpointing decision is itself a decision-only judge over
  "is the turn complete" — the acoustic twin of this paper's textual judge.

## Connections

- `sierra2024taubench` (outcome classes), `consol2025` (SPRT inside single calls), `earlyeval2026`
  (offline eval pruning) — JEV-as-a-Judge supplies the missing "cheap confident accept" primitive.
- Product hook: Voice KPI API / Voice Metrics Dashboard containment estimation could cite this as
  evidence that decision-only models are production-viable components.

## Use as citation

Future paper candidate: "Sequential decision-only judging for voice-agent trajectory outcomes" —
this paper is the base cite for decision-only judging; CD2 is the open angle.
