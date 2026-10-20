All files read. Here is my complete review.

---
SCORE: 7

---

## Writing & Presentation Review — "Start Fast, Stop Fast"

### Abstract & title
- **Works.** ~250 words, covers problem (cessation unmeasured/unbounded), gap (no standardised definition, no formal floor), contribution (two-floor model, phase-conditioned floor, tool-persistence lemma), method (semantics-tested PoC + smoke anchor), and result (109/609 ms, ~0 gen-stop, ~0/1000 ms resume). Concise, specific, honest (synthetic-latency caveat is in the body but the "small tested orchestrator"/"smoke measurement" is accurately labelled).
- **Title** is memorable and thematically matched to the companion ("The Latency Floor…"). The colloquial "Start Fast, Stop Fast" slightly undersells the formal content but is a fair editorial choice for arXiv. Keep.
- **One real problem:** the final sentence — *"The Cascade Competitiveness Criterion now applies inside the orchestration stage."* — is a dangling callback to an **unpublished, placeholder-ArXiv-id companion** (`latencyfloor2025` is `arXiv:XXXX.XXXXX`). A fresh reader cannot resolve it. Either self-contain one clause explaining CCC or delete the sentence. (MANDATORY #3.)

### Structure, flow, redundancy
- Flow is clean: Intro → Background (properly differentiated ancestors) → Framework (all definitions) → Analysis (theorems) → Practical (table) → Open → Discussion → Conclusion. Good skeleton, tight length; appropriate for a preprint, not padded.
- **§5** is substance (the four-architecture table carries real content; the "single-hop noise vs tool-turn decisive" consequence is the payoff). Keep.
- **§6** is mostly substance; paragraph 4 ("Learned turn-end prediction", 3 sentences) is a pointer, not a paragraph — merge into §2's bridge or cut. Paragraph 5 (predictive cross-type dispatch) is the freshest and should be kept.
- **§7** is substantive (evidence scope + policy/physics + companion relation). The "Citation status" paragraph is process, not prose — acceptable, but it belongs in a footnote, not the Discussion.
- **Repetition to trim:**
  1. *"sufficiency, not uniqueness / not a uniqueness claim"* appears **five times**: `01_introduction`, `03_framework §event system`, `05_practical_question` (table caption), `07_discussion` ("No uniqueness claim"), `08_conclusion`. Keep it in §3 and §7; cut the others.
  2. *"cessation is neither standardly defined nor formally bounded"* appears ~5× (intro, §2, §6, §7, conclusion). Vary it or keep only intro + conclusion.
  3. §8 Conclusion re-states the abstract near-verbatim for three consecutive sentences ("cessation grows with in-flight audio… prompt depth-independent cancellation… tool-dominated resumption"). Compress the conclusion to the practical punchline (its last two paragraphs are the good part).

### Figures (TikZ)
- `fig_two_floors` — legible, conceptual, marks shared subsystems. Best figure. Keep. (Placement nit: it floats inside §4 but belongs thematically in §3 with the definitions.)
- `fig_interruption_phases` — clear phase→outcome map. Keep.
- `fig_event_loop` — conveys the one semantic no other figure shows (red interrupt arrow cancels generation *only*; tool persists via dashed self-loop; reentry on completion). Small but worth keeping. Slightly cramped; widen or use `large`.
- `fig_tool_hiding` — **needs a redraw.** The green "onset floor" band sits on the right and *every* arrow, including *"removed from floor"*, points into/at it. A node explicitly outside the floor should arrow away from the band. As drawn the figure contradicts its own caption. Also the Type-A "background dispatch → removed from floor" claim is parenthesised in prose but drawn as an absolute — tighten.
- `fig_four_architectures` — **the weakest figure and a true redundancy:** it re-plots exactly what Table 2 already states (four rows, clock coupling, filler colouring). It adds no temporal information the table lacks. **Cut it, or redraw it as an actual clock/timeline diagram** (coupled vs decoupled scheduling across a turn) so it teaches something the table cannot.

### Theorem clarity & math-notation hygiene (the core issue for a non-expert)
1. **Thm 1 is the weakest formal object and the notation is undefined.** The statement introduces **primed** symbols `λ_detect'`, `λ_buf'`, `λ_decode'` with no definition of what the prime means (cessation-side contribution of the same subsystem? a different quantity?). `≡` vs `∝` vs unmarked equality are never explained. The *proof* is prose ("The three equalities follow directly") for a claim that is close to definitional — `λ_detect' ≡ λ_detect` is nearly tautological (same VAD feeds both timelines). *Recommendation:* re-scope this as a **Proposition**, define the primed symbols in one sentence, state what `≡`/`∝` mean, and shorten the proof to two sentences — or the weakest theorem will attract the most reviewer fire. (MANDATORY #1.)
2. **"irr" superscript in Thm 3** (`λ_tool,i^{irr}`) is never expanded. Add "(irreducible)" or define in §4 intro.
3. **Terminology wobble:** the paper promises a *detect/decide/cease/resume* decomposition (abstract & theorem framing) but §4.2 writes "detection, decision, cession, and resumption" and uses `δ_decide`/`δ_resume`/`δ_cease`. Pick one verb ("cease") and one symbol set, and align the decomposition names with Thm 2's equation. Also `δ_resume`, `δ_decide`, and `t_0` are introduced in Thm 2 but never appear in its equation — say explicitly that the equation specialises the general decomposition to phase-play.
4. **The "cessation floor" as an object.** Abstract says "prove a … cessation floor" and §4.1 defines `Λ_c`, but no theorem ever states `Λ_c = <closed form>`. The reader gets a phase-conditioned bound on `δ_cease` instead. Add one explicit sentence composing `Λ_c` from the `δ_*` terms so "the floor" has a single definable object (this also makes the intro/abstract-to-theorem bookkeeping line up). (Folded into MANDATORY #2.)
5. **No notation conventions paragraph.** With `Λ_on/Λ_c`, `λ_*` (constituents), `δ_*` (reaction), `τ_f`, `d`, `τ_human` (inherited) all in play, one "Notation" sentence near the top of §4 would lift clarity substantially for a non-expert. P2; cheap to add.

### Bibliography / bib hygiene (blocks submission)
6. **9+ TODO-VERIFY provisional entries + a placeholder companion ArXiv ID.** This is the outline's own Stage-1 gate, but from a presentation standpoint it must still be listed as mandatory: an arXiv upload with unverified titles/venues for `raux2012optimizing`, `bohus2011interruptions`, `heldner2010gaps`, `schegloff2000overlap`, `ward2000backchannel`, `baumann2012incremental`, and a placeholder self-citation would fail review. (MANDATORY #4 — it's the same item they've already gated.)
7. **`baumann2012incremental` is a `@misc` with a `booktitle` field** — bibtex will warn and `plainnat` will not render a venue properly. Convert to `@inproceedings`. P2.
8. **Cross-paper metadata drift:** the companion (`cascade_voice_latency/main.tex`) lists the affiliation as *"Department of Energy and Process Control"*, this draft says *"Department of Computer Science"*. Same author, two different department names. Reconcile. P2.
9. **`\fancyhdr` without `\setlength{\headheight}{...}`** (companion sets 14pt) — likely an overfull header warning under warnings budget. P2.

### Length/scope
Appropriately scoped for a tight arXiv preprint. With one figure cut, one redrawn, and §6.4 folded, it lands very tight. Do not grow it.

### Smoke anchor (cross-check of the cited evidence)
- Read `scripts/smoke_cessation.py`: prose vs script are **consistent** — `N_RUNS=5`, `FRAME_MS=100`, cease = `last_audible_end − t0` with a real `await orchestrator.interrupt()` on a real async-generator model stream (gen-stop is a genuine task-cancel), resume measured from interrupt during `active_calls()` to first resumed frame. Table values (109/609/~0/~0/~1000) match the script's median output and the self-check asserts exactly the three claimed invariants. Labelled "anchor, not benchmark" in caption and §7 — correct and honest. No issues from the writing side; the numbers support the prose claims as feasibility instances.

### Directness summary (what would actually hurt this draft)
The biggest presentation risks are **(a)** Thm 1's undefined-primes + prose-"proof" inviting a formal-hostile review, **(b)** the unresolved labelled accompaniment (`arXiv:XXXX`) leaking into the abstract via the CCC sentence, **(c)** `fig_four_architectures` duplicating Table 2, **(d)** 5× repetition of the two signature hedges. The prose itself is clear, well-differentiated, and honest; the draft is close.

MANDATORY REVISIONS: (blocking for submission)
1. Re-scope and re-type **Thm 1** as a Proposition; define the primed symbols (`λ_detect'` etc.) and the semantics of `≡`/`∝`; replace the prose-"proof" with a 2–3 sentence argument tied to the definitions (`04_analysis.tex`, `thm:floor_dependency`). As written the strongest hedge is dressed as a theorem.
2. Fix theorem-math bookkeeping for a non-expert in §4: define "irr" in Thm 3; make "cease/cession" terminology uniform; add one sentence composing `Λ_c` from `δ_detect/δ_decide/δ_cease/δ_resume` so "the cessation floor" has a single definable object; state that Thm 2's equation specialises the general decomposition to phase-play.
3. Self-contain the abstract: explain or drop the final *"Cascade Competitiveness Criterion now applies inside the orchestration stage"* callback, which depends on an unpublished companion with a placeholder ArXiv ID.
4. Complete the Stage-1 citation gate before any upload: verify all TODO-VERIFY entries in `main.bib`, fill the `latencyfloor2025` ArXiv ID, and fix `baumann2012incremental` from `@misc{booktitle}` to `@inproceedings`.

OPTIONAL SUGGESTIONS:
1. Cut `fig_four_architectures` (duplicate of Table 2) or redraw as a real clock/timeline diagram; fix `fig_tool_hiding` arrows so "removed from floor" points away from the floor band.
2. Add one "Notation" convention sentence at the top of §4 (Λ vs λ vs δ, τ_f, d, what `≈`/`∝`/`≡` mean).
3. Trim repeated signature claims: "sufficiency-not-uniqueness" (5×) and "neither standardly defined nor bounded" (5×); keep intro + conclusion.
4. Merge §6 paragraph 4 ("learned turn-end prediction") into the §2 bridge; keep §6 paragraph 5 (predictive cross-type dispatch), which is the freshest open direction.
5. Move the §7 "Citation status" paragraph to a footnote; compress §8's first three sentences (they restate the abstract).
6. Reconcile the author's department string with the companion paper (Energy and Process Control vs Computer Science); add `\setlength{\headheight}{14pt}`.

VERDICT: Minor Revision

---

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Concrete findings with file paths and severity returned: Thm 1 undefined primed symbols/prose proof (papers/cascade_orchestration_floor/sections/04_analysis.tex, thm:floor_dependency); CCC callback to placeholder-Id companion in abstract (papers/cascade_orchestration_floor/main.tex); TODO-VERIFY bib gate + @misc/booktitle defect in papers/cascade_orchestration_floor/main.bib; 5x redundant 'sufficiency-not-uniqueness' hedge; fig_four_architectures duplicates Table 2 and fig_tool_hiding arrow contradiction (figures/*.tex); smoke-anchor prose-vs-script cross-check verified consistent (code/the production voice monolith-orchestrator/scripts/smoke_cessation.py). All block/severe items scored and prioritized."
    }
  ],
  "changedFiles": [],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "read all 8 sections, main.tex, OUTLINE.md, main.bib, 5 TikZ figures, smoke_cessation.py, companion main.tex + open-problems",
      "result": "passed",
      "summary": "Full read of draft, figures, bib and PoC script; cross-checked smoke numbers against script constants (N_RUNS=5, FRAME_MS=100) and self-check asserts - consistent, no fabrication"
    }
  ],
  "validationOutput": [
    "Review-only task: no compile/test commands run (no TeX toolchain on this machine, per OUTLINE.md); compile + bibtex must happen on a TeX-capable host before submission"
  ],
  "residualRisks": [
    "Thm 1 formal soundness not independently provable from the draft alone - notation and claim need tightening regardless (flagged MANDATORY #1)",
    "All 9 TODO-VERIFY bibliographic entries inherit the outline's Stage-1 gate; verified factually here only to the extent feasible offline (ward2000backchannel venue low-confidence)",
    "fig_four_architectures / fig_tool_hiding legibility judged from source TikZ, not a compiled PDF",
    "Cross-paper companion arXiv id is a placeholder (arXiv:XXXX.XXXXX), so the abstract self-containment fix is a hard precondition"
  ],
  "noStagedFiles": true,
  "diffSummary": "Review-only pass; no files changed",
  "reviewFindings": [
    "no blocker on prose quality",
    "P1: 04_analysis.tex thm:floor_dependency - undefined primed symbols, prose proof, near-tautological equality; rescope to Proposition",
    "P1: abstract CCC callback depends on placeholder companion id; self-contain or drop",
    "P1: main.bib TODO-VERIFY gate + baumann2012incremental @misc/booktitle defect",
    "P2: 5x redundant 'sufficiency not uniqueness' hedge across intro/framework/§5/§7/§8",
    "P2: fig_four_architectures duplicates Table 2",
    "P2: fig_tool_hiding 'removed from floor' arrow points into the floor band",
    "P2: terminology wobble cease/cession; 'irr' superscript undefined; Λ_c never written closed-form",
    "P2: author department string differs from companion paper; missing setlength headheight"
  ],
  "manualNotes": "Verdict Minor Revision, SCORE 7 (writing/presentation lens). Smoke-anchor evidence in scripts/smoke_cessation.py is fully consistent with the numeric claims in Table 2 and is properly labelled an anchor, not a benchmark. No edit requested/needed; no compile run performed."
}
```