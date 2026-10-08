---
title: "Common Voice: A Massively-Multilingual Speech Corpus"
year: 2020
venue: "Proceedings of LREC 2020 (verified in jev-vad-poc bib, 2026-10-06)"
arxiv_id: "1912.06670"
cite_key: "ardila2020common"
topic: "semantic_vad"
subtopics:
  - "corpus"
  - "multilingual"
key_claims:
  - "Massively multilingual crowd-sourced speech corpus; the standard source of read Spanish speech for low-resource evaluation."
limitations:
  - "Read speech, single utterances, no dialogue labels: cannot supervise turn policies (barge-in/backchannel/turn-end) directly."
open_questions:
  - "Dialogue-labeled multilingual corpora for turn policy supervision (the jev-vad benchmark fills a 100-phrase slice for Spanish)."
gap_score: 3
conceptual: true
---

Cited in jev-vad-poc as the audio source for the benchmark's acoustic cuts
(phrase endings spliced to simulate ASR truncation). Also the canonical
example of why read-speech corpora don't transfer to turn-taking labels.
