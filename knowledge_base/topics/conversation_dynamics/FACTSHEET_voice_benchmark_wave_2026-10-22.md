# Voice-agent benchmark wave: factsheet + adoption verdicts (2026-10-22)

*Method note: the worker fetching full paper content died repeatedly on cold-start this
session. Titles below were verified via the HF papers search API (api/papers/search) in
this session. Numeric content was NOT read for 5 of 6 papers: those entries are marked
`unread: verify before quoting` and must not reach any public artifact until verified.
FDBench entries are memory-sourced from our LIT_SCAN_2026-10-20.md and the Heartbeat
reading of 2026-10-21 (factsheet-4-topologies), and are labelled as such. Evidence rule
applies: an unverified number is not a number.*

## 1. tau-Voice (2603.13686)

- Title (verified): Benchmarking Full-Duplex Voice Agents on Real-World Domains.
- Measures: full-duplex agents on real-world task domains rather than synthetic chat.
- Headline numbers: unread: verify before quoting.
- Code availability: unread: verify before quoting.
- Adoptability: event-driven-voice-orchestrator bench (32 invariants): CITE, and if its
  domains are open, candidate scenario source for our harness. jev-mini-bench: CITE.
  trace2grammar coverage: CITE (its domain taxonomy is a coverage checklist).
- Risk: tau-Voice targets full-duplex agents; our cascade bench is not directly comparable.

## 2. DuplexSpeechBench-IFEval (2609.03423)

- Title (verified): Evaluating Implicit Instruction Following in Full-Duplex Speech.
- Measures: implicit instruction following while conversing duplex (constraints obeyed
  without explicit commands).
- Headline numbers: unread: verify before quoting.
- Adoptability: our artifacts: CITE only (we have no duplex speech model). Interesting
  framing for trace2grammar: constraints as observable conversation properties.

## 3. APEX-Voice (2609.34973)

- Title (verified): Can Voice Agents Complete Professional Workflows Through Full-Duplex.
- Measures: end-to-end professional workflow completion over full-duplex voice.
- Headline numbers: unread: verify before quoting.
- Adoptability: closest to our orchestrator's thesis (tools inside voice turns). If open,
  RUN-candidate for event-driven-voice-orchestrator adapters (its workflows map to our
  bench tools). jev-mini-bench: CITE. Verdict now: RUN-CANDIDATE pending code check.

## 4. PACT-SLM (2609.38232)

- Title (verified): When Does a Spoken Agent Have Enough Evidence to Act? The PACT-SLM.
- Measures: the decision to act under partial evidence during spoken interaction. This is
  the Jev decision point exactly: when to stop listening and start deciding.
- Headline numbers: unread: verify before quoting.
- Adoptability: strongest conceptual neighbor of jev-mini-bench this wave. If its probe
  set is open, jev-mini-bench gains a real task family. Verdict: RUN-CANDIDATE pending
  code check; at minimum CITE in the decision-index writeup.

## 5. Speculative End-Turn Detector (2503.23439)

- Title (verified): Speculative End-Turn Detector for Efficient Speech Chatbot Assistant.
- Measures: predicting end-of-turn early so generation can start speculatively.
- Headline numbers: unread: verify before quoting.
- Adoptability: our event-driven orchestrator bench can absorb its metric (early EOT
  prediction accuracy vs our ack latency invariant). CITE + potential metric import into
  bench_turn_latency.py if the paper defines a portable metric. trace2grammar: the
  detector decision is exactly a trace-observable event.

## 6. FDBench (memory-sourced: LIT_SCAN_2026-10-20 + Heartbeat 2610.26233 reading)

- Measures: full-duplex conversation quality; Heartbeat evaluates speculative listening
  on FDBench v3 with the STC metric.
- Headline numbers (memory-sourced, verified on 2026-10-21 paper read): STC 34.7 to 50.7;
  36.4% final-latency cut from speculative reasoning while listening.
- Adoptability: our conformance kit + Heartbeat baseline were already annotated together
  (shelved Nov paper assets). We can COMPARE: restate our bench turn numbers in their
  protocol shape. Label stays memory-sourced until a fresh fetch confirms.

## The ONE benchmark worth adopting if the Nov paper revives

**FDBench (v3, via Heartbeat 2610.26233).** Reasons: it is the baseline we already
annotated; it measures the speculative-listening regime our event-driven topology feeds
into; our bench numbers become a floor comparison instead of an isolated claim. Runner-up:
PACT-SLM, if its evidence-to-act probe set turns out open and small.

## Adoption decision table

Adoption verdicts:
- tau-Voice: our bench CITE (+scenarios if open); jev-mini-bench CITE; trace2grammar CITE (taxonomy).
- DuplexSpeechBenchIFEval: CITE across all three (constraints as observables).
- APEX-Voice: our bench RUN-CANDIDATE (workflows map to bench tools); rest CITE.
- PACT-SLM: jev-mini-bench RUN-CANDIDATE (evidence-to-act probe family); rest CITE.
- Speculative EOT Detector: our bench METRICIMPORT candidate; trace2grammar CITE (event type).
- FDBench: our bench COMPARE (adopt if Nov paper revives); rest CITE.

RESEARCH-BENCH COMPLETE: 6
