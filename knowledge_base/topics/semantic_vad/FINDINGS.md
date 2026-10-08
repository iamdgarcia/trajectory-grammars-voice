# Semantic VAD — Engineering Findings (jev-vad-poc distillation)

_Distilled 2026-10-06 from the jev-vad-poc project: benchmark design, sweep
ablations, operating points, dual-environment latency (laptop + Cloud Run
8 vCPU), and the pipeline investigation of the production voice stack
(iabto-ms-bc). Numbers are project-measured unless flagged otherwise; frozen
artifacts live in `jev-vad-poc/benchmark/`. Update 2026-10-08: paper
published (external venue); FD-VAD (`mathur2026fdvad`) added as the audio-side
SOTA reference — see note under F4._

## F1. Question design beats model scale (at this granularity)

The controllable lever was **how you ask**, not which encoder:
- Barge-in works in **English framing over Spanish state** (0.62 acc) and
  collapses in Spanish framing (0.22) — instruction-language ≠ data-language.
- Turn-end needs **Spanish framing**; the English mirror flattens to ~0.5.
- Serializations (dict vs raw vs turns) move accuracy ±0.04-0.20 within a
  framing; framing choice moves it up to 0.40.

Design rule: treat question language and serialization as **hyperparameters
with a sweep budget**, chosen per decision, not per model.

## F2. The two decisions are not one decision

Barge-in and turn-end have different signals, different framings, different
failure costs, and therefore different operating points:
- **Barge-in**: bias to recall (R 0.85, th 0.30 + pure-filler guard,
  P 0.68, F1 0.76, CI95 [0.64, 0.948], n=100). Missing a real interruption
  (user repeats themselves) is cheaper than a false interrupt (cancelled
  tools, restart).
- **Turn-end**: text-only signal is near chance (0.40-0.54). Use only as a
  **soft veto AND-ed with the acoustic decision**, bias to precision. Never
  as a trigger.

A single combined decision destroys one of the two operating points.

## F3. Latency is small, conditional on hardware, and hides under STT

- Cloud Run 8 vCPU (Xeon 2.80 GHz), n=100: 1-question p50 101/108/187 ms at
  4/8/32 words; p99 178/168/268. 2-question combined 276 ms p50 / 333 p90.
  batch8 136 ms/state. Cold load 19.6 s (model must be preloaded at deploy).
- Laptop i7-10850H: 326/386/609 p50 — **not** inline-viable for barge-in on
  laptop-class CPU; cloud band is.
- The decision runs on the **partial transcript**, which exists before
  `stt.final`: p99 268 ms < 500 ms Chirp `speech_end_timeout` floor → the
  semantic decision completes inside the window the STT is already making
  the user wait. Zero marginal latency when it confirms; it only "costs"
  when it vetoes — and a veto saves a whole false turn (~2 s+ V2V).

## F4. Complementarity is architectural, measured on both sides

- smart-turn v3.2 (audio, 8.7 MB ONNX in the pipecat wheel): **verified
  locally p50 146 ms, p90 205 ms**; blind to content ("...un billete de ida"
  sounds complete).
- Semantic (text): blind to prosody/truncation — turn_complete 0.75-0.96 on
  hard ASR cuts.
- Therefore: **serial acoustic → semantic veto** is the correct composition.
  Two independent deciders would double-fire turn-ends.
- **Confirmed externally (2026-10-08):** FD-VAD (`mathur2026fdvad`) gates its
  semantic endpointer behind Silero VAD in continuous dialogue and reports the
  composition is what makes it qualify on TurnBench (FP<=0.10) — independent
  lab, same conclusion.

## F5. The 600 ms that wasn't a VAD problem

In the production pipeline, interim transcripts arrive fast; the dispatch
waits for `stt.final` (Chirp finalize ~400-500 ms after the 0.2 s VAD
hangover). The wait is **STT finalization, not endpointing tuning**: the
hangover (0.2-0.5 s) is already near-minimal. The lever is dispatching the
LLM from the last interim (SV4), not shaving the VAD further.

## F6. Benchmarks must be frozen and class-balanced, with honest scoring

- 100 phrases, 3 classes (take_floor/backchannel/side_talk), md5-frozen
  (`293f9a66d26af383013e85d0ce076256`); acoustic cuts spliced from Common
  Voice (`ardila2020common`) to simulate ASR truncation.
- **Scorer label mismatch invalidated the first sweep** (option name vs truth
  label `mid_turn`/`still_speaking`): one mapping bug made a near-chance
  signal look usable. Freeze the scorer alongside the data; add a
  confusion-matrix guard.
- Report per-class Wilson CIs: side_talk 3/10 [0.108, 0.603] means the class
  is barely measured at n=100 — resample before trusting deltas.

## F7. Selection is in-sample — say so

All thresholds and framings were selected on the same 100 phrases used to
report. The honest claim is calibrated *methodology* (how to sweep, freeze,
and audit), not generalization; the numbers are floor-setting. Any future
headline accuracy needs a held-out corpus (see gap SV2).

## F8. Integration surface (Pipecat-class pipelines)

Viable insertion points, in preference order:
1. **Stop strategy** (turn-end veto): subclass of the smart-turn stop
   strategy; must pass through the silence ceiling and watchdogs — only the
   model's verdict is vetoable, or real silences never close the turn.
2. **Start strategy** (barge-in policy): must live *inside* the
   transcription-start strategy — after the InterruptionFrame broadcasts,
   it is too late.
3. **NOT** as a `BaseTurnAnalyzer` (audio-only interface).
4. With STT-managed turns (Flux): turn-end veto is meaningless (fin arrives
   server-side); barge-in policy still applies.
5. Keep a `*_enabled` flag mirroring the incumbent smart-turn flag; report
   per-decision latency as a pipeline stage KPI (today smart-turn's cost is
   instrumented but unpublished).
