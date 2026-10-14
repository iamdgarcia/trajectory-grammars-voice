# AI Research Factory — trajectory grammars program

Research factory of **iamdgarcia** (Daniel García Peña) for the conversation-dynamics program:
turn-scale physics → conversation-scale trajectories.

## Papers (papers/)

| Paper | Status | Source |
|---|---|---|
| The Latency Floor of Cascade Voice Agents | **Published** — [alphaXiv:2608.latency-floor-cascade-voice-agents](https://www.alphaxiv.org/abs/2608.latency-floor-cascade-voice-agents) | `papers/cascade_voice_latency/` |
| Start Fast, Stop Fast: Interruptibility and the Cessation Floor | Stage-6 package ready (`cascade_orchestration_floor_arxiv.zip`) | `papers/cascade_orchestration_floor/` |
| Turn-Level Trajectory Grammars for Voice Agents | **In revision** — being generalized to public datasets (MultiWOZ 2.4 / ABCD / τ-bench); frozen pending re-evaluation results | `papers/trajectory_grammars_voice/` |
| What Are We Not Testing? (trace→trajectory region coverage) | Stage-2 outline; implementation at [trace2grammar](https://github.com/iamdgarcia/trace2grammar) | `papers/trace2trajectory/` |

## Artifacts

- `knowledge_base/` — 177+ paper notes across 6 topics (conversation_dynamics, semantic_vad, orchestration, ai_guardrails…)
- `templates/` — arXiv/venue paper templates
- `papers/*/reviews/` — multi-round verification panels (the review pipeline itself)

## Related repos

- [event-driven-voice-orchestrator](https://github.com/iamdgarcia/event-driven-voice-orchestrator) — the runtime the floors papers point to (zero deps, bench with invariants)
- [trace2grammar](https://github.com/iamdgarcia/trace2grammar) — observability traces → grammar walks + region coverage
- Live instruments: https://iamdgarcia.medium.com/watching-your-voice-agent-think-three-instruments-you-can-open-in-a-browser-tab-f7ed16ec2a2a

Contact: info@iamdgarcia.com
