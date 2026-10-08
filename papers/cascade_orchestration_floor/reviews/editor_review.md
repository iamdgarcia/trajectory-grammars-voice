# Chief Editor — Decision Dossier
## "Start Fast, Stop Fast: Interruptibility and the Cessation Floor of Realtime Cascade Voice Agents"

**Grounding note.** I read `main.tex`, `OUTLINE.md`, all eight `\input`-ed sections, `main.bib`, the five TikZ figures, and the companion paper's `04_latency_floor.tex` / `05_react_extension.tex` to verify the critical disputed facts before synthesising. Verified independently: (a) the companion §4 Remark states "for a branching pipeline … Λ* is the maximum irreducible latency along any critical path through the DAG, not the sum over all stages" — which contradicts this draft's Thm 3 "Σ_{i∈A} … possibly parallel tool DAGs" generalization; (b) `main.bib` carries 6 `TODO-VERIFY` gated entries (5 already cited in §2: `raux2012optimizing`, `bohus2011interruptions`, `heldner2010gaps`, `schegloff2000overlap`, `ward2000backchannel`), a `@misc`-with-`booktitle` `baumann2012incremental`, and the `latencyfloor2025` placeholder (`arXiv:XXXX.XXXXX`); (c) the KB entry `bohus2011interruptions.md` (ICMI, "Learning to Addressee-Respond…") conflicts with the bib entry (SIGdial, "Decide-to-Talk and Decide-to-Listen…") — same key, two titles/venues; (d) `fig_tool_hiding` draws its only floor-pointing arrow for serial type-A while "removed from floor" has no arrow away from the band, and `fig_four_architectures` re-plots Table 2. All four reviewers' evidence cross-checks against what I read; no false positives found in the blocking set.

---

## 1. DECISION: **MAJOR REVISION**

Not **Reject** — the spine is sound and independently verified: the two-floor framing, the phase-conditioned floor, and the tool-persistence/API-serializability combination are not a re-label of InproTK revocability or barge-in endpointing (m1/d2 confirmed the semantics against the real `orchestrator.py` and `smoke_cessation.py`). Not **Accept** — multiple formal statements are wrong as written (m1: "one literal false implication, one internal overclaim"; d2: P1 on Thm 1, the Lemma, the Filler Corollary). Not **Minor** — the definition of Minor ("acceptable after small fixes, no new content") doesn't hold: Thm 2 must be restated as an inequality, Thm 1 re-scoped/proven differently, Thm 3 re-scoped to serial chains, the Filler Corollary proof re-justified from batch-atomicity to content-integrity, and §2.5/§5 need new cited content. Those are real changes → Major.

**Risk assessment.** The theoretical fixes (M1–M4) are the load-bearing ones and also the cheapest (rewrite ≤ a paragraph each; no re-derivation loop needed — m1 gives the corrected forms). The citation gate (M6) and related-work body (M7) are mechanical but must close before any arXiv upload. No structural rethink required. This converges toward Minor material after one revision round.

## 2. SCORE TABLE

| Reviewer | Score | One-word rationale |
|---|---|---|
| m1 — methodology | 5 | Precision — theorem statements imprecise, one false literal implication |
| d2 — domain | 6 | Soundness — correct spine, but unguarded safety/idempotency and open gate |
| w3 — writing | 7 | Polish — close; presentation/bookkeeping fixes only |
| r4 — related work | 6 | Coverage — gate violated and MUST-COVER body missing |

## 3. CONSOLIDATED MANDATORY REVISIONS
Union of all blocking items, de-duplicated, rated, converted to concrete edits, ordered by severity. (No reviewer item dropped as false positive.)

- **M1 — Restate Thm 2 as an inequality with additive detection/decision and saturation** (`04_analysis.tex`, §4.2 "The cessation floor", eq with `thm:cessation_floor`). δ_detect is additive (ceasing cannot begin before detection), not an `O(...)` error term, and δ_decide (defined "may be zero") must appear in the bound: restore as `δ_cease^(phase-play) ≥ δ_detect + δ_decide + d·τ_f` (worst case, flush-on-cancel at full commit depth), state `δ_cease ∈ [τ_f, d·τ_f] + δ_detect + δ_decide`. Reconcile "grows with output length" (abstract, OUTLINE) with the fixed-depth bound: under a fixed in-flight policy the tail *saturates* at `d·τ_f`; output length matters only up to buffer fill. Add one clause that the equation specialises the general detect/decide/cease/resume decomposition to phase-play. Unifies m1#1, d2-P2(a), w3#2b.

- **M2 — Thm 1 → Proposition; define primes and relations; drop the decode-drain claim** (`04_analysis.tex`, `thm:floor_dependency`). The primed symbols (`λ_detect'`, `λ_buf'`, `λ_decode'`) and `≡`/`∝` vs unmarked equality are undefined; define them in one sentence (prime = cessation-side contribution of the same shared subsystem). Remove the proof's "faster decode … lets the tail drain sooner": under playback-real-time commit the committed tail drains at the TTS/playback rate and faster decode *fills* the buffer sooner — decode does not shorten completion beyond fixed depth d; what it changes is how fast the committed buffer fills (capped at `d·τ_f`). Keep shared detection + buffer-depth coupling; cut decode from the shared list or soften to buffer-fill-only. Replace the prose "proof" with a 2–3 sentence argument tied to the definitions. Unifies m1#2, d2-P1#1, w3#1.

- **M3 — Thm 3 re-scoped to serial chains; DAG case = critical path; fix the type-B/C clause** (`04_analysis.tex`, §4.3 "Tool-hiding coupling"). `Σ_{i∈A}` is valid only for serial dispatch (a linear chain); for the "possibly parallel tool DAGs" sentence use the critical-path sum — this draft's own generalization outright conflicts with the companion §4 Remark (DAG floor = max along a critical path, not the sum). The type-B/C clause is tautological as written: under Def 5, B/C never gate *first* audio regardless of dispatch; say instead that background dispatch changes *subsequent-segment* onset and the total path. Remove/soften "This generalises the companion k-step silence-gap bound … to typed, possibly parallel tool DAGs." Expand the `irr` superscript (irreducible). Unifies m1#3, w3#2a (terminology/irr).

- **M4 — Lemma reframed as an invariant; Filler Corollary re-justified on content-integrity** (`04_analysis.tex` §4.4 Lemma, §4.5 Corollary; `05_practical_question.tex` table row). (a) Lemma: distinguish *internal* persistence of a pending batch (safe by construction — this is the PoC's whole mechanism) from *flushing* a partial batch to the provider (invalid); state the assumption (providers reject partial tool-call messages / append-only immutable histories) and scope "necessarily yields a provider-invalid sequence" to those providers. As written the "iff" is definitional and "necessarily" overclaims across providers. (b) Corollary: the API-validity claim is literally false as stated — Def 6 constrains only tool-call batches; a truncated plain-text filler fragment cannot "corrupt API-valid history" or "violate atomicity." Rewrite the proof around content-integrity: bleed/duplication and unretractable append-only text. (c) Fix the §5 row "risks corrupting history per Corollary" to match. Unifies m1#4+#5, d2-P1#2+#3.

- **M5 — Add the cancellable-vs-irrevocable safety distinction** (`06_open_problems.tex` — new paragraph, or a remark in `05_practical_question.tex`). "Tool persistence under cancellation is safe" is only *protocol*-safe; for side-effecting/irrevocable tools (payment, transfer, authorization) execution-persistent reentry risks double-execution/double-charge on resumed context. Add idempotency keys / revocation as a §6 open problem and mark the type A/B/C taxonomy as a *when-needed* typing, not a persistence-safety typing. (Demanded by d2 alone; not a false positive — it strengthens the paper's own safety headline for its stated banking domain.)

- **M6 — Close the Stage-1 citation gate** (`main.bib`, `knowledge_base/topics/orchestration/`, `02_background.tex`). Verify the 5 gated refs already cited in §2 (`raux2012optimizing`, `bohus2011interruptions`, `heldner2010gaps`, `schegloff2000overlap`, `ward2000backchannel`); reconcile the `bohus2011interruptions` conflict (bib: SIGdial "Decide-to-Talk…" vs KB: ICMI "Learning to Addressee-Respond…" — confirm on ACM DL and pick one); add the `baumann2012incremental` KB entry and fix the bib entry from `@misc{booktitle}` to a venue-renderable `@inproceedings`; fill the `latencyfloor2025` arXiv id; run the mandated 2025–26 arXiv sweep for competing interruption-response/full-duplex metrics; keep any still-unverified cite visibly provisional at its cite site (or hold the §2 sentence that builds novelty positioning on it — §7's "structural results do not depend on exact bibliographic detail" is too strong).

- **M7 — Add the tool pre-dispatch/prefetch related-work body** (`02_background.tex` §2.5, `06_open_problems.tex` §6.5 predictive dispatch, `05_practical_question.tex` §5). Verify then cite TiLT (pre-EOU dispatch) and/or `specrag2024` (retrieval overlap) and/or `agentsnotenough2024` (prefetch) — present in KB, absent from prose/bib — in §2.5; cite tau-bench in §5 to ground "framework noise for single-hop turns; decisive for tool turns" which is currently asserted uncited; use them to anchor §6.5's "live production trick behind many assistants" (zero citations today). Add the one-clause §2.6 continuity statement that the companion explicitly flags barge-in reaction as open.

- **M8 — Hedge consistency + self-contain the abstract** (`08_conclusion.tex`, `figures/fig_four_architectures.tex` caption, `main.tex` abstract). Soften "only a decoupled runtime avoids paying each round trip…" and "Only full decoupling … realises…" to the sufficiency-not-uniqueness framing the paper itself asserts in §5/§7/§3 (a serial topology with async nodes/background dispatch/checkpoint reentry can emulate at expressiveness cost). The @abstract's closing "The Cascade Competitiveness Criterion now applies inside the orchestration stage" dangles off an unpublished, placeholder-`arXiv:XXXX.XXXXX` companion — self-contain it with one clause or drop it (fixing the id in M6 alone doesn't make the callback resolvable to a fresh reader).

- **M9 — Smoke-anchor honesty fixes** (`04_analysis.tex` §4.6, table caption, abstract). (a) State explicitly that the scripted model has zero prefill, and report exact medians — "resume ≈ 0 ms in-memory" is impossible by construction (`resume ≥ remaining tool delay ~10 ms + reentry`); (b) note that in phase-tool `interrupt()` is a no-op (`_model_task` already None), so that row measures plain reentry, not "resume after interruption"; (c) replace "confirming Theorem 2/3" with "instantiates / consistent with" — the emulated flush-on-cancel delivery clock *embeds* the theorem's own assumption, so 109/609 ms is a self-consistent reproduction, not independent evidence.

## 4. OPTIONAL (top 3, most valuable)
1. **Cut `fig_four_architectures` or redraw it as a real clock/timeline diagram** — it currently re-plots exactly what Table 2 states; and fix `fig_tool_hiding` so "removed from floor" is drawn with an arrow pointing *away* from the onset-floor band (w3, r4).
2. **Add a §4 "Notation" convention sentence and a formal definition of "floor"** (e.g., infimum over admissible scheduler decisions under the fixed in-flight policy) so "the floor" is one definable object and `Λ_c` is composed explicitly from the `δ_*` terms; this also fixes intro/abstract-to-theorem bookkeeping (w3, m1).
3. **Quantify the pre-detection component** (VAD/channel detect, ~150–400 ms) and report per-run spread (N>5) so the 109/609 ms figures are not read as user-perceived stop latency (d2, r4).

**Report-only notes (P2, non-blocking):** orphan placeholder files `sections/03_methodology.tex`, `05_open_problems.tex`, `06_discussion.tex`, `07_conclusion.tex` sit in the tree but are not `\input` (inert, but a stray-inclusion hazard); abstract "~110 ms" vs table 109 ms rounding; OUTLINE §02 still names specrag/tilt/taubench/agentsnotenough that must match the section once M7 lands; `\fancyhdr` without `\setlength{\headheight}` (overfull-header warning risk); reviewer-flagged department-string drift vs companion ("Computer Science" vs "Energy and Process Control").

**Compile/test commands a supervisor must run (not run here — no shell):** `pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex` (target 0 errors, ≤5 warnings); `python scripts/smoke_cessation.py` to reproduce the 109/609/~0/~0/~1000 medians, especially the "~0" rows grounding M9.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Read main.tex, OUTLINE.md, all 8 sections, main.bib, all 5 figures, and companion 04_latency_floor.tex/05_react_extension.tex. Independent verification of disputed claims: companion §4 Remark (DAG floor = max along critical path) contradicts draft Thm 3 sum-over-DAG generalisation (M3); main.bib holds 5 gated refs cited in §2, a @misc{booktitle} baumann2012incremental, and latencyfloor2025 arXiv:XXXX.XXXXX placeholder (M6); bohus2011interruptions key conflicts bib(SIGdial) vs KB(ICMI) (M6); fig_four_architectures re-plots Table 2 and fig_tool_hiding lacks an away-from-band arrow (optional #1). Findings below carry file paths + severity."
    }
  ],
  "changedFiles": [],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex",
      "result": "not-run",
      "summary": "No TeX toolchain in this environment; draft is un-compiled. Supervisor must run to confirm 0 errors / <=5 warnings."
    },
    {
      "command": "python scripts/smoke_cessation.py",
      "result": "not-run",
      "summary": "No shell here; reviewers who read the script confirm values match prose. Supervisor must run to reproduce 109/609/~0/~0/~1000 medians, especially the '~0' rows grounding M9."
    }
  ],
  "validationOutput": [
    "DECISION: Major Revision. Scores m1=5, d2=6, w3=7, r4=6. Spine (two-floor model, phase-conditioned floor, tool-persistence/API-serializability) verified sound and original by m1/d2 against real orchestrator code and smoke script; blocking items are formal-precision (M1-M4), safety scope (M5), and the open citation/coverage gate (M6-M7), plus hedge/honesty edits (M8-M9)."
  ],
  "residualRisks": [
    "Draft un-compiled; pdflatex/bibtex warnings budget (<=5) is unverified, and fancyhdr headheight may add an overfull-header warning.",
    "6 gated bib refs + bohus2011 title/venue conflict + baumann2012 KB entry + latencyfloor2025 arXiv id all still unverified; 2025-26 arXiv sweep not run.",
    "Smoke '~0' resume rows not independently reproduced; M9 requires exact medians and zero-prefill disclosure.",
    "MUST-COVER body (TiLT/specrag/agentsnotenough/tau-bench) absent from prose/bib; synthesis unverified.",
    "Orphan placeholder section files (03_methodology, 05_open_problems, 06_discussion, 07_conclusion) risk accidental inclusion.",
    "Dissenting-rev factor: author-discipline department string differs from companion ('Computer Science' vs 'Energy and Process Control')."
  ],
  "noStagedFiles": true,
  "diffSummary": "Review-only; no files changed.",
  "reviewFindings": [
    "P0/M1: 04_analysis.tex thm:cessation_floor - equation uses approx + O(delta_detect), drops delta_decide; must be inequality with additive detect/decide and fixed-depth saturation.",
    "P0/M2: 04_analysis.tex thm:floor_dependency - undefined primes and 'equiv'/'propto'; decode-drain claim wrong under playback-real-time commit; rescope to Proposition.",
    "P0/M3: 04_analysis.tex thm:tool_hiding - sum valid only for serial chain; DAG generalisation contradicts companion 04_latency_floor.tex Remark; B/C clause tautological.",
    "P0/M4: 04_analysis.tex lem:serializability + cor:filler - Lemma confuses internal persistence with flushing; Filler Corollary's API-validity/atomicity claim false for plain-text filler (Def 6 covers tool batches only).",
    "P1/M5: no idempotency/revocation treatment for irrevocable side-effecting tools; 'safe' headline only protocol-safe.",
    "P1/M6: main.bib 5 gated refs cited in §2; bohus2011interruptions key has two titles/venues (bib SIGdial vs KB ICMI); baumann2012 @misc{booktitle}; latencyfloor2025 arXiv:XXXX.XXXXX.",
    "P1/M7: §2.5/§6.5/§5 lack tool pre-dispatch/prefetch coverage (tilt2025, specrag2024, agentsnotenough2024, taubench2024 in KB, uncited); §5 'decisive for tool turns' asserted uncited.",
    "P1/M8: 08_conclusion.tex 'only a decoupled runtime' + fig_four_architectures caption 'Only full decoupling' contradict sufficiency hedge; abstract CCC closing sentence dangles off placeholder companion.",
    "P2/M9: 04_analysis.tex smoke-anchor '~0' resume impossible by construction; phase-tool interrupt() no-op; 'confirming Thm 2' should be 'instantiates/consistent with'.",
    "P2 (report-only): orphan placeholder sections 03_methodology/05_open_problems/06_discussion/07_conclusion not \\input; abstract ~110 vs table 109 ms; OUTLINE §02 vs section content drift; fancyhdr headheight; department-string mismatch with companion."
  ],
  "manualNotes": "Chief Editor synthesis, review-only (no files written). Verdict: Major Revision - concentrated and mechanical; after M1-M9 this is Minor material. I could not run TeX, the smoke script, or grep/ripgrep (no shell/toolchain here); compile + smoke must be reproduced by a supervisor. Evidence for M9 and the smoke figures relies on the four reviewers' code-level verification of scripts/smoke_cessation.py, which I could not re-run."
}
```