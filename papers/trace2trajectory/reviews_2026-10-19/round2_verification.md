## Review — Round-2 verification (mandatory items vs current sources)

Verified against: `sections/02_background.tex`, `sections/04_coverage.tex`, `sections/05_atlas.tex`, `sections/06_evaluation.tex`, `main.tex`, `main.bib`. Tool budget exhausted before I could read `01_introduction`, `03_extraction`, `07–09`, `OUTLINE.md`/`NOTES.md` — flagged below as unverified.

### Checklist

**Rev1 (methodology)**
1. Degenerate basis at n=2 → **RESOLVED** — `06_evaluation.tex` §6.2 now states the centered real matrix is rank-deficient, second axis "implementation-defined… geometrically arbitrary," worked example demoted to "smoke test of runnability."
2. Anchoring never tested by protocol → **RESOLVED** — §6.2 adds a fourth rung: real-set resampling (subsample, refit basis, recompute coverage, report spread), explicitly tied to the anchoring commitment.
3. Abstract 40.2% without qualifier → **RESOLVED** — abstract now says "(2 real / 1 simulated fixture conversations, 3 dialects; an illustrative smoke test of runnability, not a population statistic)."
4. Out-of-grid fraction → **RESOLVED** — §6.2: coverage "always reported together with the out-of-grid fraction."
5. Z-norm provenance → **RESOLVED** — `04_coverage.tex` §4.1: "z-normalized per column with the statistics computed on the real set only."
6. Envelope-center overclaim / core constants → **RESOLVED** — §6.2: "sits within the envelope as shipped"; p99/0.5 constants "fixed by construction and not swept."
7. Kendall τ collision → **RESOLVED** — §6.1 uses `τ_K`/`ρ_S`.

**Rev2 (observability)**
1. Duplicated §2.4 paragraph → **RESOLVED** — single occurrence in `02_background.tex`.
2. Caption vs Eq. threshold → **RESOLVED** — `fig:coverage` caption now states `core = max(p99, 0.5·peak)` of the smoothed real field (OUTLINE copy unverified).
3. Table 1 gap hole → **RESOLVED** — `agenteval2026` cited in §2 prose, marked concurrent, and given its own Table 1 row; `salesforce2025workflows` cited in §2 prose.
4. LangSmith overstatement → **RESOLVED** — §2.4 bullet now scopes conversation identity to user metadata (`thread_id`). (`03_extraction` mirror bullet unverified.)
5. Real-set-size protocol dimension → **RESOLVED** — same fourth rung as Rev1-2.

**Rev3 (writing)** — 1, 2 → **RESOLVED** (same items as Rev2-1/2). Bonus confirmed: ε→`\varepsilon` unified in §6; bigram k=6 specified and marked not-swept.

**Rev4 (citations)**
1. Duplicate paragraph → **RESOLVED**.
2. Bib hygiene → **PARTIAL** — all `[verify]`/`[placeholder]` note strings stripped; `garcia2026grammar` now "Companion manuscript (under review)". BUT: `nourbakhsh2026tracer` still has malformed `journal = {arXiv preprint arXiv:2607.03974; EMNLP}`, and institutional author placeholders (`{Carnegie Mellon University}`, `{Salesforce Research}`, `{SAP Labs}`, `{KTH…}`, multi-institution strings) plus `{{anonymous}}` authors (`trajectoryGeometry2026`, `falsesuccess2026`, `resume2026`, `stopmeansstop2026`, `resolveRate2026`, `agenteval2026`) remain — these still typeset into the reference list under `plainnat`. The bib header claims author lists were "verified live on alphaXiv 2026-10-19," which I cannot re-check (no network); as written, the entries still read as placeholders.
3. OpenInference/LangSmith citations → **RESOLVED** — both `@misc` entries exist and are cited at the §2.4 bullets (§1 first-mention cite unverified).
4. Process-mining lineage → **RESOLVED** — `vanDerAalst2012process` added, cited in §2.4 with the delta sentence (business-process logs vs conversation semantics/coverage).
5. Companion self-containment → **RESOLVED** — §2.1 states the guarantees as companion-paper assertions with a pointer to §3, no longer load-bearing (§3.3–3.4 unverified).
6. AgentEval concurrent work → **RESOLVED** — cited + tabled + delta stated verbatim from the outline.

### New issues introduced by the revisions
None found in the revised text read — the edits are additive, internally consistent, and didn't break the numbers (103/256 = 40.2% still consistent across abstract/§5.2).

### Unverified (budget), listed as residual risk
`01_introduction`, `03_extraction`, `07–09` (incl. whether §9 carries the qualifier), OUTLINE/NOTES staleness, compile status — a supervisor should run `pdflatex`+`bibtex` and diff those files.

**Overall verdict: READY for round-2 scoring** — with one flagged carry-over (Rev4-2 residue: author fields + TRACER journal string) to finish before upload.

```
## Review
- Correct: 17 of 18 mandatory items verified resolved in current sources, with exact quoted evidence per item
- Finding: P1 — main.bib: nourbakhsh2026tracer malformed journal string + institutional/anonymous author placeholders remain (Rev4-2 PARTIAL); smallest fix: split journal/note, fill real author lists before upload
- Merge verdict: OK with notes (READY for round-2 scoring)
```