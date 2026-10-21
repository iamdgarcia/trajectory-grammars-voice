# Conversation Dynamics — topic state (2026-10-21)

*One-screen answer to "where is this lane and what's open". Written for cold-resume;
update after each lit-scan that changes the picture.*

## Where the lane converged (3 papers + our artifacts agree)

The industrial-academic consensus for realtime voice agents landed on the same three
mechanisms our factory built independently:

1. **Anticipation** — start deciding BEFORE the endpoint (Endpoint Anticipation 2606.13450;
   our Heartbeat baseline + event-driven orchestrator event-driven-voice-orchestrator).
2. **Speculation** — reason and call tools while the user still speaks, with a rollback
   story (Ant Intl Heartbeat Thinking 2610.26233, Berkeley Speculative Interaction Agents
   2605.13360, Qualcomm speculative tools jung2026speculativetool).
3. **Adaptive emit** — commit when uncertain→ready instead of fixed windows/timers
   (X2Streaming-ASR 2609.08672 "wait when uncertain, emit when ready"; our livekit#7994
   chunk-silence bound; DuplexJev 92 ms single-token decisions).

Fixed chunking and reactive-only endpointing are dead ends as of Q4 2026; the interesting
question moved to WHICH event triggers the speculation and WHAT rollback policy keeps it honest.

## What remains open (verified gaps, from gaps.md CD1-CD4 + scans)

- **CD2 (measurement):** no public benchmark evaluates the DECISION the agent takes at
  every pause; 2610.12802 (People Making Conversation) is the closest but builds synthetic
  conversations rather than deriving behavior from real-deployment observability traces.
  That derivation is exactly our trace2grammar atlas line (40.2% region coverage demo) —
  the atlas claim's neighborhood has no occupant yet.
- **Rollback accounting:** nobody publishes false-speculation cost per topology (our
  latency-gap-simulator + factsheet-4-topologies numbers are the only first-party ones we
  know of).
- **Calibration of tiny decision models:** the 2610.24649 negative placebo result (Jev
  controller +19% cost at equal pass rate when miscalibrated) has no follow-up paper; a
  calibration conformance kit would be a contribution.

## What does NOT need doing

- A third paper right now: the lane converges on what we already built; nothing new to
  claim. (Decision 2026-10-20: Nov paper in the drawer until the funnel moves.)
- Another turn-taking survey: the space is well-mapped in our 3 lit-scans of October.

## Feeds

- Papers line: `papers/trajectory_grammars_voice/` (complete), `papers/trace2trajectory/` (paused).
- Product line: event-driven-voice-orchestrator (library), jev-mini-bench (Space),
  trace2grammar (atlas implementation).
- Distribution line: factsheets here are the source material for LinkedIn pieces
  (fixed-chunking piece queued in the factory ideas lane).
