# alphaXiv submission — Turn-Level Trajectory Grammars for Voice Agents

Canal de publicación: **alphaXiv** (arXiv no disponible para el autor). Precedente en la fábrica:
`2608.latency-floor-cascade-voice-agents` (publicado 2026-08-28, 47 votos).

## Paquete
- `trajectory_grammars_voice_arxiv.zip` (17 ficheros: main.tex, main.bib, sections/, figures/ — los
  figures/ son TikZ, sin binarios).
- PDF de verificación local: `main.pdf` (28pp, 0 errores / 0 warnings / 0 overfull).
- **ACTUALIZACIÓN 2026-10-17 (user): el formulario de alphaXiv pide el PDF directamente, no un zip
  (y las figuras TikZ no renderizan en su preview). Pendiente de resolver: exportar un PDF final
  autocontenido para pegarlo en el formulario. Mientras tanto la subida está EN PAUSA por decisión
  del usuario.**

## Campos sugeridos para el formulario
- **Title**: Turn-Level Trajectory Grammars for Voice Agents: Early Outcome Prediction and
  Intervention on Partial Conversations
- **Author**: Daniel García Peña (info@iamdgarcia.com, ORCID 0000-0002-1456-4785)
- **Primary area**: cs.AI · **Secondary**: cs.CL (diálogo/voz)
- **Abstract**: copiar del `\begin{abstract}` de main.tex (texto abajo).

## Abstract (para pegar)
Production conversational-banking voice agents are judged by conversation-level outcomes —
containment, abandonment, human handoff, compliance — yet their engineering and evaluation
remain turn-level.
We propose a formal trajectory grammar for voice-agent conversations: a state space over
conversation phases (greeting, authentication, intent, tool loop, clarification, confirmation,
close) with typed transitions and terminal outcome classes, in which regressions are grammar
cycles and cycle depth is a first-class drift statistic that distinguishes longer from off-path.
On top of the grammar we define a partial-observation decision layer: a sequential stopping rule
(SPRT / confidence sequences) over the outcome-class posterior that achieves expected decision
time at most K(ε, c) turns at confidence 1−ε under standard sequential-analysis assumptions on
the emission model, with false-early-exit economics derived from a banking cost model; we show
that a recent learned early-failure detector is the fixed-sample instance of this rule.
We wire the outcome classes to production telephony KPIs, define a leave-one-campaign-out
evaluation protocol on real Spanish call logs with decision-latency accounting against the
published latency and cessation floors of cascade voice agents, and couple escalation,
clarification, and fraud-flag states to a production orchestration graph as actionable
interventions.
The trajectory layer thereby becomes the missing conversation-scale control layer for banking
voice agents.

## Post-publish (una vez tenga ID)
- [ ] Dar de alta el ID real en `main.bib` de los otros papers que citan esta línea
      (equivalente a `latencyfloor2025` → `alphaXiv:2608.latency-floor-cascade-voice-agents`).
- [ ] Fila en TLC hub / linking si procede.
