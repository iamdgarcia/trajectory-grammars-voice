I have enough evidence. Below is my related-work / citation-hygiene review, then the acceptance report.

---

## Review — Related-Work Coverage & Citation Hygiene

### Correct (evidence)
- **Self-cite is legitimate and well-integrated.** `papers/cascade_voice_latency/sections/05_react_extension.tex` contains `thm:react` (k-step silence gap, tool-using agents) and `07_open_problems.tex` contains the "Learned barge-in prediction" paragraph — so §2.6's "k-step silence-gap bound" and the theoretical bridge in §2 (reactive floor vs. predictive turn-end ceiling) trace to real content in the companion paper, not to a hand-wave. §1's "200 ms norm" (`levinson2015timing`,`stivers2009universals`) and the shared-substrate hedge in §2.6 are consistent with the companion.
- **§2 is well-structured and honestly differentiated** against its two stated formal ancestors: incremental revocability (schlangen2011, baumann/inproTK) and interruption policy/endpointing (raux2008/2012, bohus2011). The "no standard definition / no formal floor" framing (§1, §8) is correctly hedged — §6 explicitly acknowledges industry measures barge-in ad hoc, avoiding the "nobody measures this" over-claim.
- **Figures and anchors line up.** Fig two_floors/interruption_phases match §4's model; `smoke_cessation.py` measures exactly what the paper reports (109/609 ms at depths 1/6 ≈ FRAME_MS×depth, gen-stop < 100 ms, resume 0 vs ~1000 ms), with the three asserted invariants present in the script.

### Fixed
None — review-only, no edits made.

### Findings
- **P1 — Citation gate violated for 5 of the 9 gated entries, and the draft's own §7 caveat overstates safety.** `OUTLINE.md` says "Citation gating enforced: do NOT cite until verified — raux2012optimizing, bohus2011interruptions, heldner2010gaps, schegloff2000overlap, ward2000backchannel, …" but §2 (`sections/02_background.tex`) cites five of these in prose as authoritative. §7's "the structural results do not depend on the exact bibliographic detail" is too strong: §2.2 builds the *novelty positioning* on bohus2011 and raux2012 ("empirical and policy pillars our decomposition builds on"). Mis-cited pillars damage the positioning even if Thm 1–3 survive. Smallest fix: actually run the planned Stage-1 verification, or visibly mark each gated cite at the cite site until then.
- **P1 — Internal metadata conflict on a load-bearing ref: `bohus2011interruptions`.** `main.bib` says "Decide-to-Talk and Decide-to-Listen…", SIGdial 12th Annual; `knowledge_base/topics/orchestration/papers/bohus2011interruptions.md` says "Learning to Addressee-Respond to Concurrent Interruptions…", ICMI — same cite_key, two different titles **and** venues, both marked UNVERIFIED. This ref is used in §2.2 (§ should-stop policy) and again in §7. Must be reconciled and verified before submission.
- **P1 — `baumann2012incremental` is cited with no KB entry and a malformed bib entry.** It is the only concrete evidence for §2.1's InproTK revocability claim. There is no `….papers/baumann2012incremental.md` (OUTLINE itself says "To-add"), and the bib is `@misc` carrying a `booktitle` field (venue is silently dropped under plainnat). Verify the InproTK release metadata and add the KB entry before submission.
- **P1 — MUST-COVER: the tool pre-dispatch / prefetch body is absent from §2.5 and §6.5, and this is the space the paper's own lead claims to live in.** KB has `tilt2025` (pre-EOU tool dispatch, arXiv 2502.19162), `specrag2024` (retrieval overlap hiding RTT), `agentsnotenough2024` (prefetch), `taubench2024` (tool-agent liveness price axis) — all provisionally in KB, all absent from prose/bib. The OUTLINE's §2 plan explicitly listed specrag2024/tilt2025/taubench2024; the written §2 covers only ReAct/LangGraph/CoT/spec-decoding. Consequence: Thm 3's type-A→B hiding/reclassification and §5's "tool turns separate sharply" float free of the closest existing work, and §6.5 "Predictive tool dispatch … the live production trick behind many assistants" makes an operational claim with **zero citations**. Fix: verify then cite TiLT/specrag (or equivalent) in §2.5+§6.5, and tau-bench in §5.
- **P2 — Companion self-cite is unresolved.** `latencyfloor2025` is `arXiv preprint arXiv:XXXX.XXXXX` — must be filled before any submission; the claims it supports (k-step bound, predictive ceiling) verify against the companion repo, so keep the claims, fill the id.
- **P2 — Operational pause/resume precedents unacknowledged.** The lead contribution is the interruptibility model, yet §2.5 credits no existing pause/resume or checkpoint-reentry primitives (e.g., LangGraph human-in-the-loop `interrupt`), even though §5's own caption concedes graph orchestrators can emulate decoupling via "async nodes, background dispatch, and checkpoint reentry." One sentence in §2.5 acknowledging operational interrupt/reentry precedents would make "no formal treatment of interruptibility as a schedulable property" read as precise rather than dismissive.
- **P2 — §2.6 bridge is implied, not stated.** OUTLINE asked to say the companion "flags barge-in reaction as open" in §2; the draft only says the companion "stops at onset." One clause would strengthen the continuity narrative.
- **P2 — Minor.** Abstract says "~110 ms", §4 table says 109 ms (from `smoke_cessation.py`: 109.0). `ward2000backchannel` (§2.3) is tangential to the two-floor model — fine as support, but it's the most trimmable cite if space is tight.

### Merge verdict
**Major Revision** — but concentrated and mechanical: the content (floor theorems, API-serializability lemma, honest hedge, self-cite integration) is close to publishable. The blockers are all citation-hygiene/coverage: clear the verification gate for the 5 already-cited gated refs, resolve the bohus2011 title/venue conflict, add the missing tool pre-dispatch/prefetch body (and tau-bench), fix the InproTK entry, and fill the companion arXiv id. Once those land, this is Minor Revision material.

---

SCORE: 6
MANDATORY REVISIONS:
1. Run the Stage-1 verification gate for all nine gated KB entries (raux2012optimizing, bohus2011interruptions, heldner2010gaps, schegloff2000overlap, ward2000backchannel, tilt2025, specrag2024, agentsnotenough2024, packer2023memgpt) — five are already cited in §2; until verified, mark each cite visibly provisional or hold it.
2. Reconcile the `bohus2011interruptions` metadata across `main.bib` (SIGdial, "Decide-to-Talk and Decide-to-Listen…") and `knowledge_base/topics/orchestration/papers/bohus2011interruptions.md` (ICMI, different title) and verify against the publisher; §2.2 and §7 position the paper on it.
3. Add the missing KB entry for `baumann2012incremental` and verify the InproTK release metadata; fix the bib entry (currently `@misc` with a `booktitle`, so the venue is dropped under plainnat).
4. Add the MUST-COVER tool pre-dispatch/prefetch body to §2.5 (and cite it in §6.5 "Predictive tool dispatch"): TiLT (pre-EOU dispatch) and/or specrag2024 (retrieval overlap) and/or agentsnotenough2024 (prefetch) — all present in KB, verify then cite.
5. Cite tau-bench (in KB) in §5 to ground the "framework noise for single-hop vs decisive for tool turns" empirical claim, which the OUTLINE promised but §5 currently asserts uncited.
6. Fill in the `latencyfloor2025` arXiv id (placeholder `XXXX.XXXXX`) and, in §2.6, make the "companion explicitly flagged barge-in reaction as open" continuity explicit (verify claims against companion §5 thm:react and §7 learned-barge-in-prediction — both check out).

OPTIONAL SUGGESTIONS:
1. Soften §7's "structural results do not depend on exact bibliographic detail" — the §2.2 positioning *does* depend on bohus/raux being the papers claimed.
2. Acknowledge operational pause/resume + checkpoint-reentry precedents (e.g., LangGraph human-in-the-loop interrupt) in §2.5 so "no formal treatment" is precise.
3. Cite the external-memory body (`packer2023memgpt`, in KB) in §6's forgetting open problem alongside `xiao2023streamingllm`.
4. Align abstract "~110 ms" with the 109 ms table value.
5. If space is tight, `ward2000backchannel` is the most expendable §2.3 cite.

VERDICT: Major Revision

---

## Acceptance report

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "Concrete, evidence-backed findings with file paths and severities: P1 citation-gate violation (5 of 9 gated refs cited in sections/02_background.tex per OUTLINE.md gate list); P1 bib/KB metadata conflict on bohus2011interruptions (main.bib vs knowledge_base/topics/orchestration/papers/bohus2011interruptions.md); P1 baumann2012incremental cited with no KB entry and malformed @misc+booktitle bib; P1 MUST-COVER tool pre-dispatch body (tilt2025/specrag2024/agentsnotenough2024/taubench2024 in KB, absent from prose/bib) with uncited operational claim in 06_open_problems.tex; P2 latencyfloor2025 arXiv id placeholder; P2 unresolved self-cite continuity in 02_background.tex. All 21 bib keys traced to cite sites (all cited, matching OUTLINE's static-check claim); companion self-cite verified against papers/cascade_voice_latency sections; smoke anchor cross-checked against scripts/smoke_cessation.py (109/609ms, gen-stop<100ms, resume 0/~1000ms)."
    }
  ],
  "changedFiles": [],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "read papers/cascade_orchestration_floor/main.tex, OUTLINE.md, sections/*.tex, main.bib, figures/fig_{two_floors,interruption_phases,four_architectures}.tex",
      "result": "passed",
      "summary": "Traced all 21 bib keys to cite sites; cross-checked theorem claims, table values, and figure references"
    },
    {
      "command": "read knowledge_base/topics/orchestration/gaps.md + papers/*.md",
      "result": "passed",
      "summary": "Confirmed gap-origin claims (OG2/OG3/OG4), confirmed 4 planned-but-uncited KB entries (tilt2025, specrag2024, agentsnotenough2024, taubench2024), confirmed missing baumann2012incremental entry"
    },
    {
      "command": "read papers/cascade_voice_latency/sections/{05_react_extension,07_open_problems}.tex",
      "result": "passed",
      "summary": "Verified companion self-cite legitimacy: thm:react k-step gap and learned barge-in prediction present"
    },
    {
      "command": "read scripts/smoke_cessation.py (via C:/Users/U77225D/Desktop/code/iabto-ms-bc-orchestrator)",
      "result": "passed",
      "summary": "Verified measured numbers 109/609ms, gen-stop<FRAME_MS, resume 0/~1000ms and the three self-check invariants"
    },
    {
      "command": "pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex",
      "result": "not-run",
      "summary": "No TeX toolchain on this host per OUTLINE; compile must be run on a TeX-capable host before submission"
    }
  ],
  "validationOutput": [
    "21/21 bib keys cited (matches OUTLINE static-check claim).",
    "bohus2011interruptions metadata conflict confirmed: main.bib (SIGdial, 'Decide-to-Talk and Decide-to-Listen... Dialogues') vs KB entry (ICMI, 'Learning to Addressee-Respond to Concurrent Interruptions').",
    "5 of 9 gate-listed unverified entries are already cited in §2: raux2012optimizing, bohus2011interruptions, heldner2010gaps, schegloff2000overlap, ward2000backchannel.",
    "baumann2012incremental: no KB entry; @misc entry with booktitle field (venue dropped under plainnat).",
    "tool pre-dispatch/prefetch body (tilt2025, specrag2024, agentsnotenough2024, taubench2024) present in KB, absent from §2/§5/§6 prose and bib.",
    "Abstract ~110ms vs table 109ms (smoke_cessation.py reports 109.0)."
  ],
  "residualRisks": [
    "Stage-1 2025-26 arXiv sweep not run (no web tool in session) — fresh voice-agent cessation/interruptibility work after 2024 could change §2 §2.5 coverage.",
    "All TODO-VERIFY metadata (raux2012, bohus2011, heldner2010, schegloff2000, ward2000, baumann2012, latencyfloor2025 id) remains unresolved.",
    "No TeX compile executed; §7's 'structural results do not depend on bibliographic detail' is stronger than the §2.2 positioning warrants.",
    "Only ~few KB entries skimmed; deepest verification was on the cited-gate and planned-§2 items relevant to the related-work lens."
  ],
  "noStagedFiles": true,
  "diffSummary": "Review-only: no edits. Reviewed related-work coverage and citation hygiene of cascade_orchestration_floor (main.tex, 8 sections, bib, 3 figures, KB gaps/papers, companion-voice-latency sections, smoke anchor script).",
  "reviewFindings": [
    "blocker: papers/cascade_orchestration_floor/sections/02_background.tex + main.bib - 5 of 9 gate-listed UNVERIFIED refs cited as authoritative; §7 caveat overstates safety",
    "blocker: main.bib vs knowledge_base/topics/orchestration/papers/bohus2011interruptions.md - same cite_key, conflicting title AND venue, load-bearing for §2.2/§7",
    "blocker: baumann2012incremental - cited with no KB entry and malformed @misc+booktitle bib entry",
    "blocker: tool pre-dispatch/prefetch body (tilt2025, specrag2024, agentsnotenough2024, taubench2024) missing from §2.5/§5/§6.5 despite being in KB and planned in OUTLINE; §6.5 makes an uncited operational claim",
    "blocker: latencyfloor2025 companion arXiv id is placeholder arXiv:XXXX.XXXXX - must resolve before submission"
  ],
  "manualNotes": "Review-only; no files written (grep/find tools were unavailable - rg/fd binaries missing - worked around with ls/read). Verdict: Major Revision, SCORE 6. The findings above are repeated in the RELWORK/CITATION-verdict block form as required by the review task. Two commands require upstream action: the pdflatex compile sequence and running scripts/smoke_cessation.py (the latter in C:/Users/U77225D/Desktop/code/iabto-ms-bc-orchestrator)."
}
```