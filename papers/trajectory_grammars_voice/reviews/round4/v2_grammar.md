# Round-4 Verification — v2_grammar (Grammar verifier; r3 lane)

## Item verification

| Item | Verdict | Evidence |
|---|---|---|
| #2 (P0) θ_esc satisfiable via unguarded path | **APPLIED** | `sections/03_grammar.tex:37-40` — def:grammar states q_close reachable by two paths (guarded `disclosure`, unguarded `user-answer`) and "only the latter can be re-labelled as an escape"; `03_grammar.tex:64-66` — θ_esc class definition = audit re-label of `service-complete` reached via the unguarded close path; `03_grammar.tex:90` — Table 1 adds unguarded row `user-answer \| progress \| q_confirm → q_close`; `figures/fig_grammar.tex:37` — unguarded edge `cf → cl` labelled "user-answer (unguarded path)"; `fig_grammar.tex:54-55` — dashed overlay edge `cont → comp` labelled "audit: close was unguarded". Guard-as-monitor-side-predicate realized as audit-time overlay; semantically equivalent, and overlay sentence (`03_grammar.tex:34-35`) matches the figure's dashed label. |
| #8 def:run uniqueness reworded | **APPLIED** | `03_grammar.tex:129-134` — "true outcome … terminal class of the well-formed run that **actually extends it**"; "several terminal classes generally remain reachable … that non-uniqueness of *abstract* extensions is exactly why prediction is needed." Verbatim response to r3. |
| #9 agent-clarify decidable rule | **APPLIED** | `03_grammar.tex:150-153` — increments D **iff** target state was previously visited and subsequently exited via a progress transition; both clauses decidable by scanning the prefix. Consistent with the "either" direction label (`03_grammar.tex:112-114`) and the regression blanket (`03_grammar.tex:27-29`). |
| #7-partial λ rename | **N/A here** | No `ε_decide`/`ε_cease` anywhere in `03_grammar.tex`; the cycle-bound lemma already uses `λ_asr/λ_lm/λ_tool/λ_tts` and `Λ_k`. Clean in this file. |

Targeted checks from the brief:
- **Two user-answer rows coherent?** Yes. Rows `03_grammar.tex:89` and `:90` share the type but have disjoint source→target pairs (spine vs `q_confirm→q_close`), so δ stays a well-defined partial function; the figure disambiguates by label (`fig_grammar.tex:37`).
- **Audit sentence vs figure label:** match (`03_grammar.tex:34-35,39-40` ↔ `fig_grammar.tex:54-55`).
- **Caption "ten event classes" (`03_grammar.tex:50`): still correct** — Table 1 has 11 rows (`:89-99`) but 10 distinct types; `user-answer` duplicated. No count defect.
- **"Every drawn edge is a Table-1 row" (`fig_grammar.tex:2`):** all 15 drawn edges map to rows 89-99; dashed overlay is exempt by design (`fig_grammar.tex:54`, `03_grammar.tex:34`).

## New findings
- **P2** — `sections/03_grammar.tex:90`: the revision-added row ends `\\\` (three backslashes; all other rows end `\\`). Compiles (trailing `\`+newline = escaped space) but is a typo introduced by the revision; fix: drop one backslash.
- **P2** — `sections/03_grammar.tex:89` vs `figures/fig_grammar.tex:27`: the figure draws `gr → au` as `user-answer`, but row 89's source column reads `$q_{auth/\ldots}$`, which does not literally cover `q_greet`. Pre-existing elision, made more visible by the duplicate row; fix: read `$q_{greet/auth/\ldots}$`. Neither finding blocks merge.

## Score
**9/10.** The round-3 P0 in this lane is soundly fixed: the unguarded path makes the audit overlay non-vacuous, the two close paths are stated consistently in definition, class definition, Table 1, and figure, and the overlay is correctly scoped to unguarded completions only. Items #8 and #9 are addressed essentially verbatim. Only two P2 nits remain, both one-token fixes.

## Remaining mandatory
None in scope.

---
`v2_grammar | score=9 | remaining=0 | #2/#8/#9 applied (03_grammar.tex:37-40,64-66,90,129-134,150-153; fig_grammar.tex:37,54-55); 2×P2 (L90 `\\\` typo, row-89 elision vs gr→au edge)`