
## FREEZE (2026-10-14, user pivot)
Paper frozen by user decision ("no me gusta; profundizar en cascade orchestration"). State at freeze:
- Generic sweep DONE: banking→contact-centre/operational, Spanish mentions removed, fraud→abuse,
  teller→human-agent, Unicaja affiliation removed from main.tex affil.
- §5 rewritten to PUBLIC DATASETS only (MultiWOZ 2.4 + ABCD + tau-bench; binary instantiation;
  honest 4-class scope — see KB PUBLIC_DATASETS_brief_2026-10-14.md). Subsec label: subsec:datasets.
- fig_stopping fixed (2 real defects); fig_grammar STILL HAS 3 confirmed defects (audit edge
  crosses handoff terminal; escalation arc crosses service-complete label; D-curve crosses a
  user-answer label) + the q_auth→q_ident restructure NOT done. Fix list lives in the session
  log 2026-10-14 (geometric audit: 32 line-through-text hits p7, cross-checked by 2 detectors).
- Compile at freeze: 27pp, 0 err / 0 warn / 1 overfull (2.9pt, §5 eq intro — cosmetic).
- If re-activated: fix fig_grammar (3 defects) + q_auth→q_ident rename (sections/03, fig_grammar,
  06_intervention already uses ident in the abuse subsection), then run the public-dataset
  evaluation for real (EXPERIMENTS needed — no numbers exist yet).
