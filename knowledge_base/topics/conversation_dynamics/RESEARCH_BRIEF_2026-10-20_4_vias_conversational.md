# Research brief 2026-10-20 — Asistentes conversacionales: 4 vías (latencia, eficiencia, evaluación, seguridad)

*Mandato del user: dedicar el resto del día a investigar asistentes conversacionales por 4 vías.
Método: 4 rondas discover_papers (recency-prioritized, 2026+) + lectura completa de 3 papers
ancla (Jev empirical 2610.13092, Heartbeat Thinking 2610.26233, eval survey 2609.30798) y la
survey S2A de seguridad (2610.15390, estructura+tablas). Este brief = mapa + aplicación a repos.*

## Vía 1 — LATENCIA: la preparación especulativa durante la escucha es el nuevo frente

**Heartbeat Thinking (Ant International, 2610.26233, 10-19)** — Thinker invocado periódicamente
(Δ=500ms, K=2 concurrentes) DURANTE la escucha; estado compartido de razonamientos completados y
resultados de tools; Responder en el handoff VAD reutiliza lo completado y cancela lo pendiente.
Resultados FDBench v3: STC (speculative tool coverage) 34.7%→50.7%, latencia final 6.90→4.39s
(−36.4%; −45.7% vs Pipecat cascada). **Fallo documentado clave: 4.0% de las respuestas usan
resultados especulativos desactualizados** (carrito con precio antiguo tras revisión de búsqueda)
— ejecución especulativa correcta ≠ uso correcto del resultado.

**Vecinos:** SHANKS (ventana por chunk, trunca args de tools), SIA (interrumpe generación en
updates), Stream RAG (retrieval paralelo con check de reutilización), LTS-VoiceAgent (trigger
semántico + razonamiento incremental), Speculative Execution on-device (Qualcomm/KAIST 2610.07641),
Never Stop Thinking (cognición continuous-time), X2Streaming-ASR (wait-when-uncertain commit).

**Gap que NADIE cierra:** todos usan scheduling FIJO (Δ timer o chunk boundary). Ninguno emite la
preparación por EVENTOS (nueva entidad hablada, tool-result devuelto, cambio de saliencia).
→ **Es exactamente el modelo de emisión de nuestro event-driven-voice-orchestrator** (user-turns y
tool-completions como eventos genéricos). Limitación declarada de Heartbeat ("adaptive scheduling
based on changes in the partial transcript or the completion of tool calls — future work") = nuestra
 tabla de predicciones P1-P7 + bench de RTT×tools×depth. El paper de Nov gana su contraste:
Heartbeat es el baseline windowed-fijo; nosotros somos la variante event-driven.

**Aplicación:** (a) FINDINGS_event_driven_orchestration: nueva sección con Heartbeat como evidencia
P-externa; (b) bench/conformance: candidato a celda 5 — "speculative tool issued during pending
turn" (ya medimos pending-window; añadir tool dispatch DURANTE pending = STC-like). PENDIENTE
decisión user (no fabricar sin consumidor claro).

## Vía 2 — EFICIENCIA: el ahorro local no transfiere; medir por OUTCOME

**When Faster Decisions Do Not Make Better Agents: Jev in Agent Workflows (NJU/TUM, 2610.13092,
10-09)** — 4.500 ejecuciones, 5 familias de agentes (ReAct, Reflexion, T3A, AutoDroid, FastAgent),
ALFWorld + AndroidWorld. Hallazgos:
- Por-decisión: coste −66/−78%, tiempo −74/−81%. PERO tokens por decisión +53/+135% (observaciones
  + candidatos en el prompt).
- Task-level: éxito cae −1.5pp (ALFWorld) a −18pp (FastAgent mobile). Coste por tarea baja, pero
  **coste por ÉXITO ENTREGADO sube en T3A (+7.7%)**: las ejecuciones fallidas se comen el ahorro.
- Mecanismos: razonamiento auxiliar + interacciones extra absorben el ahorro; failed recovery
  (73/251 ejecuciones codificadas) y premature completion limitan la entrega. Reflexion-J: gana en
  first-trial (95.3% vs 93.5%) pero recupera peor (11/19 vs 25/26) → final peor.
- Prescripción: evaluar por "successful delivery, recovery behavior, and resources per delivered
  outcome"; checks de completion + progreso repetido como puntos de fallo terminales.

**Vecinos:** RouterWorld (routing latency-aware a escala), System X (decision model que responde
desde su propio KV cache — el siguiente paso natural del lane Jev), Whose turn is it? (Microsoft:
routing con estado conversacional — los routers naive rompen agentes stateful), DLite/H-Spec
(speculative decoding history-free/paralelo), Secure Speculative Decoding (2610.08678 — el draft
model como superficie de fuga).

**Aplicación:** (a) jev-mini-bench README: nuance honesta de 1 línea — "an empirical study shows
per-decision savings don't always transfer to task success; measure per delivered outcome"; (b)
**confirma la tesis outcome-classes de trace2grammar**: la unidad de cuenta correcta es el outcome,
no el turno ni el intento — refuerza §3/§4 del paper; (c) para el orquestador: "premature
completion" es un class de outcome que el walker YA detecta (terminal con goal incompleto).

## Vía 3 — EVALUACIÓN: de calidad-de-componente a OUTCOMES VERIFICADOS EN ESTADO

**Evaluating Real-Time Voice Agents (Northeastern/Walmart/Sinch, 2609.30798, 09-25)** — survey de
38 fuentes con corpus verificable (hashes SHA-256; pillaron un identificador arXiv falsificado de
FDB-v3 en circulación: el correcto es 2604.04847). 3 claims: (1) arquitectura = constraint de
despliegue, no veredicto — "duplex behaviour is separable from duplex architecture" (DuplexCascade:
micro-turns + control tokens en cascade con 50k diálogos texto + LoRA = SOTA turn-taking en FDB);
ningún E2E self-hostable cumple producción; cascada = 755ms TTFA con function calling. (2) La
evaluación ha girado a outcomes verificados contra ESTADO (VAmoS: 100 escenarios con PostgreSQL
sembrado, grader con aserciones binarias sobre la TRAZA completa incl. tool calls; containment =
share resuelto sin handoff). (3) El supuesto diádico se rompe (MP-Bench, MSI-Bench: autoridad —
quién puede saber qué — es first-class).

**Propuesta del paper: estándar TRG (Timing–Recovery–Grounded)** + 4º eje condicional M
(multiparty): timing con colas, recovery separado de performance sin-disrupción (IHBench: recovery
es eje de capacidad INDEPENDIENTE; closed-weight degrada 3.3× más lento), outcome verificado en
estado externo. TRG es deliberadamente débil: prescribe ejes, no métricas.

**Mapa de benchmarks nuevos:** TurnBench (ya citado), MP-Bench (participante multiparty),
MSI-Bench (razonamiento multi-speaker 1.152 casos), FLEXI (emergencias: cuándo INTERRUMPIR el
usuario), IHBench (post-interruption recovery), MTVA-Bench (el LLM interno del cascade bajo ruido),
SpeechGym (RL audio-native: los fallos agénticos en voz son PERCEPTUALES — valor mal-oído cascada a
call fallida; process reward por turno arregla el hambre de gradiente de outcome-only GRPO),
DuplexSpeechBench-DG (grounding documental/alucinación en voz), GAUGE (cuándo NO confiar en
LLM-judge con simuladores), TRACER (trajectory-aligned user simulation, Peking/Kuaishou 2609.28690
— OJO: otro TRACER distinto del de 2607.03974, no confundir en citas).

**Aplicación:** (a) **nuestros instrumentos = stack TRG completo**: playground/dash (T), nada de
recovery aún (hueco: IHBench-style post-barge-in resume KPI en voice-metrics-dashboard — candidato
LEDGER con consumidor=estándar emergente), conformance kit + VAmoS-style assertions (G);
(b) trace2trajectory: citar VAmoS + TRG en related work (containment ya es nuestro métrica central:
45.3% en fixtures); (c) paper Nov: DuplexCascade + este survey son los cites que blindan la tesis
cascade→duplex.

## Vía 4 — SEGURIDAD: la autoridad de instrucción hablada es el hueco abierto

**S2A survey (2610.15390, 10-11)** — modelo Acoustic Sensing-to-Action de 6 áreas: Acoustic
Sensing / Provenance & Authority / State & Reasoning / Tool & Action / Edge-Cloud Runtime /
Lifecycle Transformation. 4 características que cambian la seguridad vs model-centric: exposición
acústica compartida (el mic no sabe de quién es la voz), estado persistente (lo oído persiste y
contamina turnos futuros), ejecución externa (la palabra se convierte en acción), despliegue
edge distribuido.

**Huecos declarados (verbatim del paper):** (1) unión fuente+autoridad+acción "weakly evaluated"
en agentes de AUDIO — los ataques de memoria (AgentPoison, MINJA, MEXTRA) están evaluados solo en
agentes de TEXTO; (2) identidad spoof ≠ autoridad de instrucción: "identity attribution determines
who is speaking, whereas instruction authority determines what that identity may control" — la
distinción no está operacionalizada en voz; (3) acciones no-cancelables de estado (el caso carrito
de Heartbeat ES un problema de seguridad además de latencia); (4) SH-Bench (bystander speech
procesado/disclosure) y MSI-Bench (disclosure por autoridad) existen como benchmarks pero ningún
modelo los cierra.

**Vecinos:** audio prompt injection (Hijacking LALMs 2604.14604, Piggybacking 2607.28165 —
inyección concurrente stealth), taxonomy de audio jailbreaks (2605.30031), CaMeL/AgentSpec/VIGIL
(contención de acciones), Aegis (eval de seguridad en pipelines de voice agents con tools),
Persona Guardrail (Uber, producción), spoofing-aware ASV (2607.14753), codec-robust deepfake
detection (2609.39651, 2610.07216).

**Aplicación (la más directa al día-job):** el agente conversacional bancario (lane iabto/BC)
ENCAJA en el perfil "Personal Task / Service" del S2A: (a) la distinción identidad≠autoridad es
EL marco para auth en voz + acciones sensibles ( ¿"transfiere 500€" dicho por un familiar cerca
del mic?); (b) SH-Bench-style: bystander en llamada de teléfono; (c) las invariantes del
conformance kit (turn-ack, barge-in stop) son de CONFIANZA, no de seguridad — un kit TRG+seguridad
(¿quién autorizó esta tool-call? ¿la traza lleva speaker-attribution?) es la extensión natural
del conformance kit hacia el banco. → BRIEF SEPARADO: `SECURITY_brief_voice_agent_authority.md`
(siguiente sesión o cuando el user active el lane).

## Decisión de construcción (regla de consumo)

Nada de artefactos nuevos hoy. Aplicaciones SHIPPED esta sesión: FINDINGS actualizado (Heartbeat +
DuplexCascade como evidencia externa), jev-mini-bench README nuance, trace2trajectory cites
(VAmoS/TRG). Todo lo demás queda anotado como candidatos con consumidor declarado pendiente de
demanda (dashboard recovery-KPI, celda-5 conformance, security brief bancario).

## Semillas de cita para el paper Nov (cascade→duplex)

1. DuplexCascade (2603.09180): duplex behavior from control policy in cascade — la prueba externa.
2. Enterprise tutorial (2603.05413): cascada práctica 755ms TTFA; E2E self-hostable no viable.
3. Heartbeat (2610.26233): preparación especulativa durante escucha (baseline windowed-fijo).
4. LTS-VoiceAgent (2601.19952): trigger semántico + reasoning incremental.
5. Jev empirical (2610.13092): recursos por outcome entregado como métrica.
6. TRG survey (2609.30798): reporting conjunto timing+recovery+grounded.
