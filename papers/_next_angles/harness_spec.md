# Cascade Architecture Comparison — Harness Spec & Metric Table

Context: long stateful sessions, chunked TTS (ASR streaming status TBD). Goal: choose the best
cascade architecture among our four candidates on evidence, not vibes — and produce an honest
empirical baseline that can later validate the Latency Floor theory.

## 0. The thesis (what this comparison is actually deciding)

For long stateful sessions the framework choice is NOT the main cost driver. Two things dominate:

1. **Where the per-turn latency lands** — in particular the *context/prefill* term, which grows with
   session length unless we carry state cheaply (KV reuse / summaries / memory layer). This is
   architecture + *state-strategy* jointly, and it's the thing that empirically separates great from
   mediocre long-session agents.
2. **What masking is available** — chunked TTS makes filler/lead-in nearly free, so manual filler is a
   cheap default; LLM filler can hide LM TTFT but risks "false starts" that leak uncommitted state.

So the comparison is really 4 architectures × a state-strategy — keep it controlled (same state
strategy across all 4 first; vary strategy in a second pass only if a winner is unclear).

## 1. The 4 harnesses (same components, orchestration only differs)

Shared, locked across all four: same ASR, same LLM, same chunked TTS, same tool stubs with
*injected* controlled RTT (25/100/300 ms jitter curve), same scripted dialog script, same session
length.

- **H1 — Serial LangGraph** (baseline): full stateful graph per turn; no concurrency; no filler.
- **H2 — LangGraph + manual filler**: canned lead-in (chunked TTS) queued while LM TTFT/tools run.
- **H3 — LangGraph + LLM filler**: node emits speculative partial answer that streams as the "fill";
  may be abandoned (false-start case) once the real completion wins.
- **H4 — Event-driven threads**: ASR→LLM→TTS run as concurrent pipeline; tools dispatched in worker
  threads mid-turn; manual filler for tool/TTFT gaps; LangGraph (or equivalent DAG) *inside* the
  reasoning/tool stage for state safety.

H4 is the structural prediction to test: it should hit the streaming-cascade floor (concurrent overlap
of reducible latency) while serial H1–H3 pay it serially — quantify *how much* instead of assuming.

## 2. Metric table

Instrument events: `asr_final | lm_prefill_start | lm_first_token | lm_end | tool_start | tool_end |
tts_first_chunk | eou | agent_stop`.

| Metric | Definition | Report | Target / anchor |
|---|---|---|---|
| Silence gap | eou → tts_first_chunk | P50 / P95 | ≤ 200 ms (τ_human); CCC-pct = %turns ≤ τ |
| Prefill cost | lm_prefill_start → lm_first_token | P50, and **drift vs turn #** | flat across session (no growth) |
| TTFT | eou → lm_first_token | P50 / P95 | as low as maskable |
| Tool hiding | tool_start → tool_end that overlaps speech/TTS | hidden-time / total-RTT | max hiding in H4/H2 |
| Barge-in react | user interrupt → agent_stop (audio off) | P50 | < ~300 ms target |
| Barge-in resume | agent_stop → new response first chunk | P50 | — |
| False starts | LLM-filler chunks abandoned | count / session | 0 for canned; low for LLM |
| Cost / turn | tokens in+out (+tool calls), normalized | per turn, vs turn # | record, not target |
| State fidelity | recall of earlier-turn facts in scripts; correctness after interrupt-mid-tool and after resume | accuracy | ≥ passes script |
| Context drift | per-turn TTFT/prefill growth + recall decay across session | curve 1→N | flat + no cliff |
| Eval time | harness build LOC + debug time (subjective) | 1 line each | record |

Run each harness on the SAME N-turn session (e.g., 20 scripted turns incl. tool calls + 3 injected
interrupts) × 3 seeds on the tool RTT jitter. Table is 4 rows × the columns above.

## 3. Decision rule

- If H4 ≈ H2 on silence gap but H4 ≫ H2 on barge-in react + state fidelity → adopt H4 (hybrid) with
  manual filler; LLM filler only where false-start cost is nil.
- If H4 shows no structural gap win over H2 serial → framework is NOT the lever; the lever is
  state-strategy (memory layer), and the paper becomes the state/forgetting angle instead.
- Flag for the paper: the measured P50/P95 floors per topology are exactly the empirical companion to
  the Latency Floor / streaming-cascade theorems (candidate: "Measured Latency Floors Across Cascade
  Orchestration Topologies").

## 4. Open questions before build

1. **Streaming/incremental ASR?** (determines EOU latency + barge-in quality + whether H4 can prefill
   during speech). Assumed in H4; mark N/A if unavailable.
2. **Where does session state live today** (LangGraph checkpointer / external store / rebuilt context
   each turn)? This sets the state-strategy baseline for all four.
3. **Real codebase location** — harnesses should live with the product repo, not this paper repo.
