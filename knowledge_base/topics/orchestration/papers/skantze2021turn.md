---
title: "Turn-Taking in Conversational Systems and Human-Robot Interaction: Challenges and Opportunities"
year: 2021
venue: "Computer Speech & Language (vol. 67, 101178)"
arxiv_id: ""
cite_key: "skantze2021turn"
topic: "orchestration"
subtopics:
  - "turn-taking"
  - "evaluation"
key_claims:
  - "There is no standard method for evaluating turn-taking behaviour of conversational systems; results are not comparable across systems."
  - "A continuous, flexible turn-taking model (vs discrete end-of-turn detection) better matches human conversation and is needed for natural engagement."
  - "Barge-in handling trades off against latency, and systems must commit to how much to predict vs react."
limitations:
  - "Survey: it catalogues the space rather than providing the missing benchmark or a formal latency model."
  - "Grounded in traditional SDS/VAD components, not modern streaming LLM agents."
open_questions:
  - "A standardized turn-taking evaluation for streaming generative agents (the RAES idea, eval discovery angle)."
  - "A formal cessation/barge-in floor for cascade agents (orchestration-floor paper, Thm 2)."
gap_score: 5
conceptual: true
---

Declares the "no standard evaluation for turn-taking" gap the evaluation
angle targets, and the barge-in-vs-latency trade the orchestration paper
formalizes. Also already cited in the published cascade_voice_latency paper.
