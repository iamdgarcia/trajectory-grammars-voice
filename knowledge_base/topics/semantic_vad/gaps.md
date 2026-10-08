# Semantic VAD — Research Gaps

_Aggregated from the jev-vad-poc project (paper + benchmark + pipeline
investigation, 2026-10-06). Topic: text-side ("semantic") voice activity
detection — deciding barge-in and turn-end from the transcript instead of
from acoustic timing. Companion to the orchestration topic (which owns the
formal-floor program and system-level evaluation gaps)._

## Gap SV1: Turn-end semantics are near chance from text alone — gap_score: 4

**Problem:** The project's own ablations put text-only turn-end accuracy at
0.40-0.54 on Spanish hard cuts (near chance): completeness judgments from a
partial transcript alone are too thin to drive a turn decision. Every
published text-side detector (LiveKit, TurnGPT lineage) reports aggregate
accuracy without per-language or operating-point breakdowns, so nobody knows
how much of their claimed accuracy survives on Romance-language hard cases.

**Evidence:** `ekstedt2020turngpt`, `livekit2024turn`, `li2025easyturn`,
`mathur2026fdvad`; jev-vad-poc sweep (`sweep_results.json`): floor_v1/v2/v3 in ES framing
0.40-0.54 across dict/raw/turns serializations.
**Update 2026-10-08:** `mathur2026fdvad` reaches 0.97+ utterance accuracy
audio-side on smart-turn data, widening the text-vs-audio gap and sharpening
this gap: the fix is fusion or multimodality, not better text prompts.

**Candidate contribution:** Acoustic-semantic **fusion** as a learned, not
hand-AND-ed, decision — or honest re-positioning of semantic turn-end as
*only ever a veto* (never a trigger), formalized as a constraint on the
policy layer.

---

## Gap SV2: No labeled multilingual benchmark for barge-in/backchannel/side-talk — gap_score: 5

**Problem:** The three-class distinction (take-floor / backchannel /
side-talk) that barge-in policy needs has no public labeled dataset in any
language, let alone Spanish. Commercial semantic VADs
(`deepgram2024semanticvad`, `openai2024realtime`, `elevenlabs2025semantic`)
and open ones (`livekit2024turn`) publish no per-class, per-language numbers.
FDB line (`fullduplexbench2025`, `fullduplexbenchv15`, `fullduplexbenchv2`,
`fullduplexbenchv3`) covers native full-duplex only.

**Evidence:** `skantze2021turn` (no standard evaluation); jev-vad-poc had to
synthesize a 100-phrase labeled benchmark (frozen md5) from scratch.

**Candidate contribution:** A public, multilingual, per-class labeled
turn-policy benchmark; simulator-driven continuation audio
(a la `fullduplexbenchv2`) instead of single spliced cuts.

---

## Gap SV3: Barge-in false-interrupt cost is unquantified end-to-end — gap_score: 4

**Problem:** Nobody measures the downstream cost of a false barge-in
(interrupting on a backchannel): cancelled tool calls, re-prompting, user
frustration, and post-interruption recovery time. IHBench
(`salimi2026ihbench`) measures recovery but not how it degrades with barge-in
policy precision. Barge-in reaction latency is also unmeasured in production
pipelines (documented as "nadie" in the investigated repo's telemetry docs).

**Evidence:** `salimi2026ihbench`, orchestration gap OG2/OG5; jev-vad-poc
operating points (`operating_point.json`) show the precision/recall dial
(P 0.68 / R 0.85 at th 0.30+filler guard) but the deployment cost mapping
is missing.

**Candidate contribution:** Cost model + measurement protocol linking
barge-in operating point to recovery time and tool-call waste; makes the
operating-point choice a business decision instead of a guess.

---

## Gap SV4: Semantic veto as latency enabler (dispatch-on-interim) — gap_score: 5 → 4 (partially claimed, core intersection open)

**Problem:** Cascade pipelines wait for `stt.final` before dispatching the
LLM because the transcript is immature (interims get rewritten). STT-native
endpointing floors (e.g. Chirp 3 `speech_end_timeout` 500 ms —
`google2025gemini`) put a hard wall after the acoustic pause. A calibrated
text-side decision over the interim (p99 268 ms cloud, hidden under the
finalization window) could license dispatching the LLM from the last interim
~200-400 ms earlier, with reconcile-on-final; nobody has published this
pattern or its failure modes (immature-text dispatch rate, reconcile cost).

**Evidence:** jev-vad-poc cloud latency table (1q p50 101-187 ms, p99 178-268
< 500 ms Chirp floor); pipeline investigation
(`jev-vad-poc/docs/investigacion-iabto-ms-bc-latencia.md`); 
`schlangen2011incremental` (revocation semantics exists in theory).

**Update 2026-10-08 — the neighbourhood moved, the intersection did not.**
Two days-old papers cover the adjacent flanks:
- `braun2026voicelight`: speculative GENERATION in a cascade (private text+PCM,
 promotion checks), but triggered by a fixed acoustic-pause rule (80/160 ms);
 its learned turn signal FAILED the locked eval (12.53% EOT recall). No
 semantic gating.
- `jung2026speculativetool`: speculative TOOL execution from partial ASR,
 rule-based predictor (word-count/pause triggers), on-device, honest ablation
 (prefetch-only wastes 47% of calls; direct injection is the win). No semantic
 gating either.

**Candidate contribution (updated):** the unclaimed intersection — a semantic
end-of-turn probability on the interim transcript as the SPECULATION GATE
(when to open the candidate + when to inject), with wasted-speculation
economics (SV5) as the tuning objective and promotion-by-revision-type as the
reconcile mechanism (Voice-Light's invariant reused). Both priors measured
their trigger quality; neither measured a semantic gate against it. This also
directly answers the user-facing latency problem: the veto signal that adds 0
ms on confirmations becomes the signal that EARNS -300..-800 ms when it fires
correctly.

---

## Gap SV5: Semantic VAD × tool-calling interaction — gap_score: 4

**Problem:** A false turn-end doesn't just produce a weird answer — it
triggers graph turns with tool round-trips (1 s RTT each, real backends).
The veto therefore protects tool budgets too, but no work connects turn
decision quality to tool-call waste in structured agents. FDB v3
(`fullduplexbenchv3`) measures tool use under disfluency for native models;
cascade component-level is untouched.

**Evidence:** `fullduplexbenchv3`, orchestration gap OG3
(tool-hiding budget), jev-vad-poc pipeline investigation (turn dispatch
triggers LangGraph).

**Candidate contribution:** Turn-policy-as-tool-guard analysis: P(veto)
against expected wasted tool round-trips, composable with the orchestration
tool-latency-budget program.

---

## Already-Addressed / non-gaps (do not re-propose)

- Acoustic VAD quality (`webrtcvad` → `bredin2020pyannote` → `silero2024vad`):
  solved technology.
- Text-side turn-shift event detection exists (`ekstedt2020turngpt`,
  `livekit2024turn`, `umair2024turntaking`, `li2025easyturn`); what is
  missing is not another detector but labels, operating points, and the
  policy integration (SV1-SV5).
- Proprietary semantic endpointing exists in production
  (`deepgram2024semanticvad` etc.): the gap is inspectability and
  per-language evidence, not existence.
- Two-question design + failure-cost asymmetry + Spanish benchmark +
  dual-environment CPU latency: **addressed** by jev-vad-poc
  (paper published 2026-10-08, external venue after alphaXiv auto-review
  rejection; repo `github.com/iamdgarcia/jev-vad-poc`).
- Streaming audio-side semantic endpointing with confidence-gated
  commitment: **now addressed** by `mathur2026fdvad` (2026-09) for English
  GPU serving — do not re-propose in that setting; the CPU/Spanish/policy
  combination remains open.
