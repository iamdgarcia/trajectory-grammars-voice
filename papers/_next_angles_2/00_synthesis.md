# Next-Paper Angles 2 — Discovery Synthesis (Round 2)

Source: 10 parallel researcher agents, launched 2026-10-08 after publishing "Asking Instead of
Listening" (Zenodo 10.5281/zenodo.23233331). Scope widened beyond the voice-agent loop at the
author's request: trajectory analysis, simulation, fraud, compliance, multilingual, escalation —
plus refreshes of the four strongest round-1 angles. Full briefs: `a1..a10_*.md` in this folder.

Caveat: no live web search was available in any child run; every citation carries a `[verify]`
mark and must be checked on arXiv before any KB entry or `\cite{}`.

## Scorecard

| # | Angle | Working title | N | F | B | Fe | R | Verdict |
|---|-------|--------------|---|---|---|----|----|---------|
| a1 | Safety Deadline (refresh) | The Safety Deadline: Dual-Bounded Guardrail Placement (τ_human, τ_reg) | 4 | 5 | 5 | 4 | 3 | **pursue now** |
| a2 | Tool Latency (refresh) | Hidden Reads, Irreversible Transfers: Reversibility-Aware Latency Budget | 3 | 5 | 4 | 4 | 3 | pursue now |
| a3 | Eval Stack (refresh) | Deadlines, Not Means: Deadline-Conformance Evaluation Standard for Cascade Voice | 4 | 4 | 4 | 3 | 2 | pursue now (capstone) |
| a4 | Memory Floor (refresh) | The Forgetting Floor: Deadline-Aware Context Eviction & Data-Minimized Memory | 4 | 5 | 5 | 4 | 2 | **pursue now** |
| a5 | Trajectory Analysis (NEW) | Turn-Level Trajectory Grammars: Early Outcome Prediction on Partial Conversations | 4 | 5 | 5 | 4 | 3 | **pursue now** |
| a6 | Simulation (NEW) | Calibrated Simulators: The Sim-to-Real Gap of LLM-Simulated Banking Customers | 4 | 5 | 5 | 3 | 3 | **pursue later** (gated on log access) |
| a7 | Voice Fraud (NEW) | The Security Floor: Two-Sided, Latency-Bounded Defense of the Voice Channel | 4 | 4 | 5 | 4 | 3 | pursue now (second wave) |
| a8 | Compliance (NEW) | Deadlines, Not Audits: Regulatory Obligations as Schedulable Constraints | 4 | 5 | 5 | 4 | 3 | pursue now |
| a9 | Multilingual (NEW) | No Language Left Listening: Per-Class Turn-Policy Benchmark + Code-Switch Problem | 4 | 5 | 4 | 4 | 2 | pursue now (SV2) |
| a10 | Escalation (NEW) | Asking for a Human: The Escalation Floor and Cost-Aware Deferral | 4 | 5 | 5 | 4 | 4 | **pursue now** (needs corpus spike) |

(N=Novelty, F=Fit, B=Banking, Fe=Feasibility, R=Risk; lower R is better.)

## Assessment

- **Trajectory analysis (a5) is the direct answer to the author's question.** It is the natural
  scale-up of the program — from turn-scale (floors, VAD) to conversation-scale (outcome
  prediction, drift, abandonment) — and it runs on data the author already owns (production
  Spanish banking logs). No competitor combines voice + partial-observation decision guarantees +
  banking KPIs. The published k-step ReAct bound becomes the trajectory grammar's cycle-length
  constraint, making it an honest extension of all three published papers.
- **The floors program still has three cheap sequels** (a1 Safety Deadline, a4 Forgetting Floor,
  a8 Compliance Deadlines): all "pursue now", all zero-data-dependency, all formal, all
  reusing the published theorem machinery. a8 in particular mirrors the floors as *regulatory*
  deadlines (disclosure timing, handoff windows) — the most distinctive banking framing found.
- **Two angles are gated on assets:** a6 (simulation) needs real call-log access for calibration;
  a10 (escalation) needs a one-week synthetic-corpus spike. Both jumped in value — the escalation
  floor completes the onset→cessation→escalation floor trilogy.
- **a7 (voice fraud/security)** and **a9 (multilingual benchmark)** are strong second-wave papers:
  a7 converts security sprawl into a compact deadline/veto/irreversibility frame; a9 executes the
  KB's highest-gap open item (SV2) with the author's exclusive Spanish data advantage.

## Suggested sequence

1. **a5 Trajectory Grammars** (conversation-scale, uses owned data, answers the "beyond voice
   agents" question) — or **a1 Safety Deadline** if the safety thread is preferred.
2. **a8 Compliance Deadlines** (zero data dependency, strongest distinctive banking framing).
3. **a4 Forgetting Floor** (cheap formal sequel).
4. **a9 Multilingual benchmark** (executes SV2, durable community asset).
5. **a10 Escalation Floor** (after corpus spike) → **a7 Security Floor** → **a3 Eval Stack**
   (capstone) → **a6 Simulation** (once log access lands).

## Method note

Children had no web tool this round; all literature scans were knowledge-based with `[verify]`
marks. Round-1 files in `papers/_next_angles/` remain valid; angle_2 (barge-in) is DONE
(published paper #2) and angle_3's refresh (a1) supersedes it in this folder.
