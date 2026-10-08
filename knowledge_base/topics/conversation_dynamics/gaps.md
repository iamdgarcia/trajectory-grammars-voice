# Conversation Dynamics — Research Gaps

_New topic opened 2026-10-08 alongside `papers/trajectory_grammars_voice/OUTLINE.md` (angle a5,
round-2 discovery). Scope: conversations as trajectory objects — outcome prediction from partial
transcripts, drift/detour structure, intervention decision rules — for voice agents, with banking
KPIs (containment, abandonment, handoff, compliance escape) as the application anchor._

## Gap CD1: No trajectory grammar with terminal outcome classes for voice-agent conversations — gap_score: 5

**Problem:** Adjacent flanks all stop short: agent benchmarks (tau-bench `sierra2024taubench`,
WebArena `webarena2023`) score full-episode success; workflow extraction (`salesforce2025workflows`)
recovers structure from completed conversations; TRACER (`nourbakhsh2026tracer`) forecasts a single
binary failure outcome from partial text-chat prefixes. Nobody defines a formal state space over
voice-agent conversation states (auth, intent, tool-loop, clarification, close) with typed
transitions and terminal classes (contained / abandoned / handoff / compliance-escape), nor a drift
statistic (cycle depth) that distinguishes "longer" from "off-path".

**Evidence:** `nourbakhsh2026tracer` (binary outcome, no grammar), `salesforce2025workflows`
(structure without outcomes), `falsesuccess2026` (final labels mislead), `tauvoice2026` (voice
benchmarks without trajectories).

**Candidate contribution:** Trajectory grammar G=(Q,Σ,δ) with outcome terminal classes and
cycle-depth drift; the latency-floor paper's k-step ReAct bound becomes the cycle-length
constraint. → **SELECTED 2026-10-08. This is the lead of `papers/trajectory_grammars_voice/`.**

---

## Gap CD2: No decision-time guarantee for early outcome prediction — gap_score: 5

**Problem:** TRACER's intervention trigger is a dev-set-tuned threshold on a learned score; no
work provides a sequential stopping rule with calibrated confidence and expected decision time
for conversation outcomes. SPRT exists inside single model calls (`consol2025` — reasoning paths)
but has not been transposed to multi-turn conversations with grammar-state posteriors.

**Evidence:** `nourbakhsh2026tracer` (threshold only), `consol2025` (wrong level), `earlyeval2026`
(offline eval pruning, no guarantees).

**Candidate contribution:** Trajectory Stopping Theorem: SPRT / confidence-sequence stopping over
P(class | x_{1:k}) achieves expected decision time ≤ k* turns at confidence ≥ 1−δ; TRACER's
threshold shown as a fixed-sample instance.

---

## Gap CD3: Voice physics and tool state are absent from outcome prediction — gap_score: 4

**Problem:** All partial-conversation prediction work is text-chat (MultiWOZ/SGD/ABCD lineage).
Voice-agent conversations have endpointing errors, barge-ins, tool round-trips, and auth events —
and our own published result shows text-only turn signals are near chance in Spanish (0.40–0.54).
No outcome predictor conditions on voice-physics/tool-state channels, and no one accounts for the
intervention decision latency (must clear the published latency/cessation floors).

**Evidence:** `nourbakhsh2026tracer` (text-only), jev-vad-poc ES sweep, published floors papers.

**Candidate contribution:** Grammar emissions over multi-channel observations (turn states from
`x2turn2026` + tool-call events + endpointing/barge-in flags); intervention latency accounted
against Λ* and the cessation floor.

---

## Gap CD4: Banking KPI wiring (containment/abandonment/handoff/compliance) is informal — gap_score: 4

**Problem:** Containment and abandonment exist as industry metrics and patents; abandonment is
modeled as queueing (`silentabandonment2024`), escalation as queue control
(`queuecontrol2026`), production evaluation as engineering reports (`nubank2026`). No formal
outcome taxonomy ties these KPIs to conversation-internal trajectory classes with early warning.

**Evidence:** the four anchors above; abandonment/fraud are rare classes (imbalance risk noted).

**Candidate contribution:** KPI-to-terminal-class mapping with cost-weighted detection-latency
metrics; leave-one-campaign-out protocol on real Spanish call logs.

---

## Already-Addressed / non-gaps (do not re-propose)

- Partial-context forecasting is principled in open-domain social conversation
  (`chang2019derailment`); the gap is task-oriented + voice + guarantees, not forecasting itself.
- Turn-level breakdown detection exists (`higashinaka2016breakdown`); do not re-derive it.
- Dialogue quality ≠ task success is classical (`walker1997paradise`); build on the cost axis.
- Workflow extraction from conversations exists (`salesforce2025workflows`); use as structure
  baseline, not as contribution.
- Early outcome prediction for offline eval cost reduction exists (`earlyeval2026`); different
  setting (not live intervention).
