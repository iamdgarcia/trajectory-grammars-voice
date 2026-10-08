# Chief Editor Certification — Revision Round 2

Date: 2026-09-01. Single chief-editor certification pass over the revised draft
(sections 01-08, main.tex, figures, main.bib) against round-1 M1-M9.

## Verify table (all PASS)
- M1 Thm 2 inequality + additive detect/decide + saturation [tau_f, d*tau_f] — PASS
- M2 floor-constituency as Proposition, primes defined, decode-drain removed — PASS
- M3 Thm 3 serial chains, DAG critical path, 'irr' defined, generalisation sentence removed — PASS
- M4a Lemma as invariant (internal retention vs flushing; provider assumption) — PASS
- M4b Filler Corollary on content-integrity; §5 row updated — PASS
- M5 cancellable-vs-irrevocable tools open problem (idempotency/revocation) — PASS
- M6 bohus2011 reconciled bib=KB; baumann2012 @inproceedings + KB entry; 5 provisional entries — PASS
- M7 pre-dispatch/prefetch body cited (§2.5, §6.5); tau-bench in §5; §2.6 barge-in-open — PASS
- M8 hedges consistent; abstract CCC dangling callback removed; fig_four_architectures deleted — PASS
- M9 smoke-anchor honesty (zero-prefill, exact medians, 'consistent with', phase-tool no-op) — PASS

## Decision
**Accept** for the revised content. No genuine M-item miss; only external gates remain (below).
Two P2 notes (abstract "~0 ms" rounding; §8 "only idiomatically decoupled") addressed 2026-09-01.

## Residual gates (external, must close before arXiv)
- pdflatex+bibtex compile (target 0 errors, <=5 warnings) — no TeX toolchain local; run on TeX-capable host.
- All TODO-VERIFY citations incl. bohus2011 (ACM DL), InproTK, 5 tool-dispatch/memory records.
- 2025-26 arXiv sweep for competing interruption-metric definitions.
- latencyfloor2025 companion arXiv id (placeholder XXXX.XXXXX).
- Smoke-anchor reproduction (scripts/smoke_cessation.py in the PoC repo).
