All reads complete; no write tool available in this session, so the report follows. I also could not execute `python _check_figs.py` (no exec tool); the pipeline should run it once from `papers/trajectory_grammars_voice/` to confirm — noted in commands below.

## Review

### Round-4 Verification — v5_scoping_bib (r9/r4 lane)

**Item verification**

| Item | Applied? | Evidence (file:line) |
|---|---|---|
| #17 absence claims scoped | ✅ | `sections/01_introduction.tex:23-26` — "To our knowledge, no formal model connects the partial, multi-channel observation stream … and no prior formalism composes that connection with a decision-time guarantee and KPI-aligned outcome classes; classical finite-state and ATN dialogue managers formalized dialogue phases, but with neither terminal business classes nor decision-time bounds." (T-o-k + FSA/ATN scoping; the item's "or scope the claim" branch is satisfied — no cite added, none needed.) `sections/02_background.tex:85-88` (§2.7 Positioning) — "Across the five strands, and to our knowledge, no work defines a formal state space … finite-state dialogue managers formalized phases without business outcomes, and optimal stopping exists in POMDP theory without a dialogue-management instantiation…" (composition-level restatement). |
| #18 POMDP optimal-stopping fairness | ✅ | `sections/02_background.tex:43-47` (§2.4) — "optimal stopping is classical POMDP material, but the dialogue instantiation does not import it … our stopping theorem is exactly that import, transposed to grammar runs." The concession is explicit; absence correctly relocated to the dialogue-management instantiation. |
| #19 raux2008optimizing + skantze2021turn | ✅ | Cited: `sections/02_background.tex:48` — "endpointing-threshold tradeoffs \citep{raux2008optimizing} and the turn-taking survey … \citep{skantze2021turn}". Present in `main.bib` (raux2008optimizing: Raux & Eskenazi, 2008, correct paper; skantze2021turn: CSL vol. 67, art. 101178, 2021, correct). Fields sane. |
| #20 bib hygiene batch | ✅ (one P2 residual) | `main.bib`: nourbakhsh2026tracer journal now "arXiv preprint arXiv:2607.03974; EMNLP" (venue split); higashinaka2016breakdown venue in journal field "Dialogue Breakdown Detection Challenge 3 (IWSDS/D-BDCh)"; tauvoice2026 author wrapped `{Sierra, Mercor, and Princeton University}` (corporate braces); salimi2026ihbench has explicit "Salimi, Parisa and others". T-as-length → L: `sections/02_background.tex:52` "a dialogue of length $L$ contributes $L$ instances". Spelling "organised" consistent. **Residual:** `main.bib:6-11` garcia2026cessationfloor has no DOI/URL/identifier (latencyfloor has the alphaXiv note, asking has the Zenodo DOI) — the "self-citation DOIs/URLs" instruction is only 2/3 discharged; defensible only if no identifier exists for that preprint. P2. |
| #5-partial T-as-length in §2.5 | ✅ | See above, `sections/02_background.tex:52`. |
| #16 guarantee qualifier (abstract + §9) | ✅ | `main.tex:74-76` (abstract) — "…at most $K(\varepsilon, c)$ turns at confidence $1-\varepsilon$ **under standard sequential-analysis assumptions on the emission model**". `sections/09_conclusion.tex:3` — "…bounded by $K(\varepsilon, c)$ turns at confidence $1-\varepsilon$ --- **conditional on a calibrated emission model over the outcome posterior** ---". §1:50-53 scopes via "at a calibrated confidence". |

**No new overclaims found.** All absence claims carry "to our knowledge"; the abstract guarantee is assumption-conditioned; TRACER comparisons remain factual (§2.5). One artifact note: my file reads rendered `Section~ef{sec:grammar}` (02_background.tex:48) and `Section~ef{sec:evaluation}` (09_conclusion.tex:15-16) — this is a carriage-return transport artifact of `\ref` (`\r` swallowed), not source corruption; the reported 0-warning compile would flag any genuinely broken ref. Verify once via the check script/compile to be certain.

**New findings**
- P2: `main.bib:6-11` — garcia2026cessationfloor lacks any identifier (DOI/URL/alphaXiv note); smallest fix: add the preprint's identifier or a Zenodo DOI note.
- P2: `main.bib` raux2008optimizing typed `@article` with `journal={SIGdial}` — SIGdial is a conference; `@inproceedings`/booktitle would be cleaner. Cosmetic.
- P2: `sections/02_background.tex:43-47` — mild editing residue: the "offers no bound on when acting on the belief is justified" and "adds what the lineage lacks: an explicit bound on when acting on the belief is justified" clauses near-duplicate; "the lineage" in the second could be read as POMDP theory generally. Suggest "…what the dialogue-management instantiation lacks". Non-blocking; the preceding concession (#18) is unambiguous.

**Score: 8/10** — All six assigned items are verifiably applied in the named seams with correct scoping and honest hedging; the two new sensing citations exist in main.bib with accurate real-world metadata (Raux & Eskenazi SIGdial 2008; Skantze CSL 2021). Deductions are the single unresolvable self-citation identifier (cessationfloor) and cosmetic bib/wording residue — nothing that changes a claim, a scope, or a reviewer-facing statement.

**Remaining mandatory:** none.

```acceptance-report
{
  "criteriaSatisfied": [
    {
      "id": "criterion-1",
      "status": "satisfied",
      "evidence": "All 6 assigned items verified with file:line evidence in sections/01_introduction.tex, sections/02_background.tex, sections/09_conclusion.tex, main.tex, main.bib; 3 P2 findings reported (cessationfloor bib identifier missing, raux2008optimizing @article/SIGdial venue type, duplicated scoping clause in 02_background §2.4)."
    }
  ],
  "changedFiles": [],
  "testsAddedOrUpdated": [],
  "commandsRun": [
    {
      "command": "python papers/trajectory_grammars_voice/_check_figs.py",
      "result": "not-run",
      "summary": "No exec tool available in this reviewer session; pipeline must run once from papers/trajectory_grammars_voice/ (52 checks, reportedly passing)"
    }
  ],
  "validationOutput": [
    "Manual verification of items #17, #18, #19, #20, #5-partial, #16 against panel10_decision.md: all applied",
    "main.bib inspected in full: raux2008optimizing and skantze2021turn present with sane fields; no dangling keys among lane-relevant citations"
  ],
  "residualRisks": [
    "garcia2026cessationfloor bib entry lacks DOI/URL identifier (P2, item #20 only 2/3 discharged on self-citations)",
    "Read-transport artifact made \\ref appear as 'ef' in two reads; almost certainly display-only, but confirm via the one check-script run / compile"
  ],
  "noStagedFiles": true,
  "diffSummary": "Review-only task; no files modified",
  "reviewFindings": [
    "P2: main.bib:6-11 - garcia2026cessationfloor has no self-citation identifier; add DOI/URL note",
    "P2: main.bib (raux2008optimizing) - @article with journal={SIGdial}; should be @inproceedings/booktitle",
    "P2: sections/02_background.tex:43-47 - duplicated scoping clause; tighten 'what the lineage lacks' to 'what the dialogue-management instantiation lacks'"
  ],
  "manualNotes": "Reviewer key v5_scoping_bib; could not write reviews/round4/v5_scoping_bib.md (no write tool) — full report returned in final message for persistence."
}
```

v5_scoping_bib | score=8 | remaining=0 | All 6 items verified applied with evidence; 3 P2 nits (cessationfloor bib identifier, SIGdial venue type, duplicated §2.4 clause), no blockers.