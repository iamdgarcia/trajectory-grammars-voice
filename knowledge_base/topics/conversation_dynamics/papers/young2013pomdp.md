---
title: "POMDP-based statistical spoken dialogue systems: a review"
year: 2013
venue: "Proceedings of the IEEE 101(5):1160-1179 (S. Young, M. Gasic, B. Thomson, J.D. Williams) - bibliographic facts verified 2026-10-08"
cite_key: "young2013pomdp"
topic: "conversation_dynamics"
subtopics:
  - "POMDP dialogue management"
  - "belief state"
key_claims:
  - "Spoken dialogue systems as POMDPs: belief over dialogue state updated from noisy observations, policy acts on the belief."
limitations:
  - "Belief over DIALOGUE STATE (slots/goals), not over terminal business outcome classes; no decision-time guarantees for outcomes; pre-LLM pipeline scale."
open_questions:
  - "POMDP-style treatment of outcome-class posteriors over grammar runs."
gap_score: 2
conceptual: true
---

The classical partial-observation lineage the trajectory-grammars paper must scope itself against
(02_background.tex strand): same mathematical skeleton (belief from partial observations), different
object (state tracking vs terminal business outcome) and different guarantee (none vs stopping bound).
