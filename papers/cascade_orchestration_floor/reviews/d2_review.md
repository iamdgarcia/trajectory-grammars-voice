I've read all the specified files: main.tex, OUTLINE.md, all eight sections, all five TikZ figures, main.bib, the smoke harness (`smoke_cessation.py`), the actual orchestrator source it drives, and the companion latency-floor paper's §5/§7 for continuity. Here is my domain-expert review.

## Review

**What is genuinely good (with evidence)**
- The two-floor framing matches operational reality. Real IVR/car-HMI/assistant systems do treat "when the agent can fully stop" as a first-class felt quantity; the banking motivation in §1 is accurate — interrupting to correct an account number is exactly where cease tail and re-listen time dominate UX.
- The self-critique in §2 is honest and correct. InproTK / Schlangen–Skantze incremental revocability *is* the closest formal ancestor, and the differentiation ("cancellable output increments … no lower-bound arithmetic for interruption reaction," `02_background.tex`) is defensible. The paper correctly retreats from "nobody measures this" to "no standardised definition and no formal floor" — that is the right and defensible novelty claim.
- The §5 architecture table rows 2 and 3 are operationally correct: delivery-layer manual filler being instantly droppable (classic barge-in device), and LLM-uttered filler bleeding/corrupting history, both match production behavior.
- The PoC semantics are real, not decorative: I verified the orchestrator (`application/orchestrator.py`) — `interrupt()` cancels only the model task and never the dispatcher; `_commit_completed_batch()` commits the assistant message *only when* `batch.is_complete()`; reentry fires on completion. `smoke_cessation.py` drives the real runtime, and the reported numbers (109/609 ms ≈ 1/6 frames × 100 ms synthetic frame) are internally consistent with the harness.

**Findings (severity, location, evidence, smallest fix)**

- **P1 — Thm 1 overclaims decode-speed coupling to cessation.** `04_analysis.tex` (`thm:floor_dependency`, proof: "Faster decode … simultaneously lets the tail drain sooner"). A committed playback tail drains at the TTS/playback rate, not the decode rate; decode speed does not shorten it beyond the fixed depth d. The shared-membership claim for decode is unproven and likely false as stated. Fix: restate that under the fixed policy decode affects cessation only via how fast the committed buffer fills (capped at d · τ_f), or drop decode from the shared list — detection and buffer depth already carry the argument.
- **P1 — Corollary (filler) overextends the Lemma to free text.** `04_analysis.tex` (`cor:filler`): the Lemma governs tool-call *batch* atomicity; an interrupted model-uttered filler fragment is a *partial free-text message*, and the real reason it must not be committed is content corruption + append-only provider history (it cannot be retracted/edited), not batch atomicity. Rewrite the proof accordingly, or the formal device reads as borrowed force.
- **P1 — Lemma conflates persistence with commit.** `04_analysis.tex` (`lem:serializability` + Def `def:apivalid`): "persists a partially completed batch … necessarily yields a provider-invalid sequence" is only true if "persists" means *flushed to the provider history*. The PoC's whole trick is that pending batches live in internal state and are committed only on completion — internal persistence is safe by construction. Reword to pin the invalid operation as *flushing* a partial batch; state the assumption that providers reject partial tool-call messages.
- **P1 — "Tool persistence under cancellation is safe" is only protocol-safe, not business-safe.** The paper never separates cancellable from *irrevocable/side-effecting* persisted tools (payment, authorization, transfer). For a banking agent this is the exact case that matters: execution-persistent reentry risks double-execution on resumed context. Add at least a remark/§6 open problem on idempotency keys and revocation; the tool typing A/B/C is a *when-needed* taxonomy, not a persistence-safety taxonomy.
- **P1 — Submission gate is open and blocks any arXiv upload.** `main.bib` still carries 9 `TODO-VERIFY` provisional entries (incl. `bohus2011interruptions`, `raux2012optimizing`, `heldner2010gaps`, `schegloff2000overlap`, `baumann2012incremental`) and the companion's placeholder arXiv id (`latencyfloor2025`, arXiv:XXXX.XXXXX). §2's differentiation from InproTK rests on the provisional `baumann2012incremental` whose KB entry does not yet exist. OUTLINE confirms the Stage-1 sweep/verification is still open. Must be closed before submission.
- **P2 — Minor formalism slips:** (a) Thm 2's Eq (1) folds `O(δ_detect)` into δ_cease right after decomposing reaction = detect+decide+cease+resume — pick one scope for δ_cease; (b) the paper never bounds δ_resume against re-prefill (long-context re-prefill can dominate the tool RTT for long sessions, which §6's forgetting floor hints at but the resume claim in §4/§8 doesn't condition on); (c) calling definition-derived statements "Theorem 1" invites credibility pushback on cs.AI/cs.CL (the pair with the companion paper keeps style consistent, but hedge the top-level claims).

**Verdict on novelty, per your lens:** the cessation-floor arithmetic, the phase conditioning, and the generated-interruptible ∩ execution-persistent + API-serializability combination are not a re-label of InproTK revocability or of barge-in endpointing — those lines model *what can be revoked / when to yield*, not reproducible latency-floor mathematics of a cascade's stop path, and I cannot name a published formal floor equivalent under another name. The claim "no standardised definition and no formal floor" is defensible *today*, but the mandated 2025–26 arXiv sweep is a real risk that full-duplex/interruption evaluation papers may already define an interruption-response metric — which is precisely why that gate is blocking.

SCORE: 6
MANDATORY REVISIONS:
1. Rework Theorem 1's proof/statement to remove the unproven decode-speed coupling to cessation (decode speed does not drain a committed playback tail); keep shared detection+buffer-depth coupling.
2. Rewrite the Filler Corollary proof to justify model-uttered filler rejection from append-only/content corruption, not from Lemma 1's tool-batch atomicity.
3. Re-state the API-serializability Lemma so it clearly distinguishes *internal* persistence (safe by construction) from *flushing* a partial batch to the provider (invalid), and state the partial-tool-call-message assumption.
4. Add a persistence-safety remark/§6 item distinguishing cancellable vs irrevocable side-effecting tools, requiring idempotency (no double-execution/double-charge on reentry) — without this, the "safe" headline is only protocol-safe.
5. Close the Stage-1 gate before any submission: verify all 9 TODO-VERIFY bib entries (add the Baumann & Schlangen InproTK KB entry the §2 differentiation depends on), fill the companion arXiv id, and run the 2025–26 arXiv sweep for competing interruption-metric definitions (FullDuplex/voice benchmarks).

OPTIONAL SUGGESTIONS:
1. Quantify the pre-detection component explicitly (real barge-in includes VAD/channel detection, ~150–400 ms) so the 109–609 ms smoke numbers are not read as user-perceived stop latency.
2. Strengthen the smoke anchor: report per-run spread/variance with N>5 and add one run exercising a VAD-style detect instead of a direct `interrupt()` call.
3. Demote or hedge definition-derived "Theorems"; keep pair-consistency with the companion paper but avoid over-claiming.
4. Add one production datapoint (§5) grounding the per-architecture table — e.g., real TTS prefetch depth / IVR post-speech cancel latency — to translate d·τ_f into realistic units.
5. In §7 (policy vs physics), note that on PSTN/narrowband two-wire channels the 'should stop' policy is partly channel physics (barge-in detectability), not free choice.
6. Bound δ_resume against re-prefill (long-context) and tie it to the §6 forgetting-floor item.
7. Doc consistency: OUTLINE still lists specrag2024/tilt2025/taubench2024/agentsnotenough2024 for §02 that appear in neither the draft nor the .bib; either drop them or add after verification.

VERDICT: Major Revision

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Returned concrete findings with file paths and severities: P1 Thm 1 decode-coupling overclaim (04_analysis.tex, thm:floor_dependency proof), P1 Corollary filler overextension of Lemma 1 (04_analysis.tex, cor:filler), P1 Lemma persist-vs-commit conflation (04_analysis.tex, lem:serializability), P1 missing revocation/idempotency semantics for persisted tools, P1 open submission gate (main.bib TODO-VERIFY x9 + placeholder companion arXiv id, confirmed open in OUTLINE.md), plus P2 formalism slips; each with evidence from the read files."
    }
  ],
  "changedFiles": [],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex",
      "result": "not-run",
      "summary": "Read-only review role; no command execution available. OUTLINE.md states no TeX toolchain on this machine and compile is unverified — engine must run this before submission."
    },
    {
      "command": "python scripts/smoke_cessation.py",
      "result": "not-run",
      "summary": "Not executed by reviewer (read-only role). Script read in full; its self-check asserts and the 109/609/~0/~1000 medians are internally consistent with a 100 ms synthetic frame and depths 1/6. Re-run on the March-2024-era external repo before submission."
    }
  ],
  "validationOutput": [
    "Cross-checked all 21 bib keys appear cited in the sections incl. heldner2010gaps, ward2000backchannel, schegloff2000overlap, bohus2011interruptions, raux2012optimizing, baumann2012incremental — consistent with OUTLINE's '21 keys all cited' claim.",
    "Verified orchestrator semantics against source: interrupt() cancels only model task; _commit_completed_batch fires only when batch.is_complete(); reentry on ToolCallFinished. Paper's PoC-semantics claims are substantiated.",
    "Companion continuity verified: thm:react, def:ccc, and §7 barge-in-prediction open problem exist in papers/cascade_voice_latency as the draft claims."
  ],
  "residualRisks": [
    "No compile check possible (no TeX toolchain); latex errors/label resolution unverified by me.",
    "Smoke numbers not re-run by reviewer; depend on synthetic frame timing (100 ms) and no real ASR/VAD/TTS.",
    "Novelty of the 'no formal floor' claim is vulnerable to 2025-26 interruption-metric definitions; the paper itself gates this behind the incomplete Stage-1 sweep.",
    "grep/find helper tools were unavailable in this session; verification done via read/ls only."
  ],
  "noStagedFiles": true,
  "diffSummary": "No code/diff reviewed — this was a peer-review of a conceptual paper draft (title/abstract/OUTLINE, 8 .tex sections, 5 TikZ figures, main.bib, smoke anchor script, orchestrator source, companion paper continuity).",
  "reviewFindings": [
    "P1: 04_analysis.tex thm:floor_dependency - decode-speed coupling to cessation unproven; decode does not drain a committed playback tail.",
    "P1: 04_analysis.tex cor:filler - overextends Lemma 1 (tool-batch atomicity) to free-text filler; real cause is append-only history + content corruption.",
    "P1: 04_analysis.tex lem:serializability - conflates internal persistence (safe) with provider flush (invalid); needs restating.",
    "P1: paper-wide - tool-persistence safety is protocol-only; missing revocation/idempotency semantics for side-effecting banking tools.",
    "P1: main.bib - 9 TODO-VERIFY provisional citations + placeholder companion arXiv id; Stage-1 gate open per OUTLINE; blocks submission.",
    "P2: Thm 2 Eq (1) scope of delta_cease vs delta_detect inconsistent; delta_resume unbounded against re-prefill; OUTLINE lists §02 refs (specrag2024 etc.) absent from draft and bib."
  ],
  "manualNotes": "Verdict: Major Revision, SCORE 6. Structure per task format is in the final message (SCORE / MANDATORY REVISIONS / OPTIONAL SUGGESTIONS / VERDICT). No edits performed (review-only)."
}
```