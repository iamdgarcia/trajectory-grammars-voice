# Factsheet: decision models en el voice loop (2026-10-22) — investigado por orchestrator

*Method: discover_papers + 2 full paper reads (DuplexJev, Jev controllers). Resto de
papers del scan solo con título verificado. Números no leídos marcados. Sin guiones.*

## Verificados hoy (números con fuente)

### DuplexJev (2610.02638, Adventists.ai) — decision models DENTRO del voice loop

- Las decisiones closed del full-duplex hechas por generación de texto consumen el
  **30% de todos los input tokens** del LLM. Fuente: paper, intro.
- Leer 10 decisiones como single tokens: **92ms por evento** vs **1.57s** generarlas
  como JSON: reducción **17x**, sin contar los 411ms de ASR autoregressive.
- Batched por ventanas de 160-200ms: 8 eventos (80 decisiones) en **94-103ms** en un
  nodo 8xH200, sirviendo **161 eventos/s**.
- Calidad: spoken QA **90% vs 91%** leyendo el transcript oracle; el conector
  cross-attention añade oír al hablante: género y emoción **90%** (desde 55% y 28%).
- Su baseline de producción: **1.29s** de mediana desde end-of-speech a primer audio
  (mismo orden que Voice-Light 758ms y nuestro 1.141s).
- Conexión con nosotros: esto es EXACTAMENTE el hueco que jev-mini-bench enseña
  (12ms vs 1200ms) llevado a producción full-duplex.

### Jev controllers: resultado NEGATIVO placebo-controlled (2610.24649)

- En 21 tareas held-out (315 trials), un controlador Jev **subió el coste por intento
  un 19%** (ratio 1.19, CI 95%: 1.02-1.36) con pass rate IDÉNTICO (**73.0% vs 73.0%**).
- Mal calibrado: probabilidad media de "run completo" 0.50 cuando el 87% pasaba, es
  decir, pedía verificar trabajo ya correcto.
- Es la confirmación placebo-controlled del hallazgo que citamos en la pieza de
  outcome-accounting: el coste por intento no predice el coste por éxito entregado.
  Pieza LinkedIn D4 tiene ahora evidencia de doble fuente.

### Escaneados (solo título verificado, números unread)

- 2610.02267: System-1 decision models para LLM agent harnesses, evaluación paired
  self-audited. unread: verify before quoting.
- 2610.00346: benchmark de System One vs clasificadores entrenados y LLMs (16 votos,
  el más votado del wave). unread: verify before quoting.
- 2610.25553: Narrow Decision Models, arquitectura System-1 calibrada (Softplan).
  unread: verify before quoting.
- 2610.21150: VoxTurn (Melbourne): varias preguntas de turn-taking en una pasada,
  un modelo. unread: verify before quoting.
- 2609.38232: PACT-SLM (cuándo tiene un agente hablado suficiente evidencia para
  actuar). Ver factsheet benchmarks: RUN-CANDIDATE para jev-mini-bench.

## 5 ángulos LinkedIn (siguiente semana, español)

1. "17x más barato decidir que generar": DuplexJev mide 92ms vs 1.57s por el mismo
   bloque de decisiones de voz. (piezas: la decisión como token único)
2. El placebo Jev: +19% de coste, 0 puntos de pass rate. Cuando el controlador
   verifica trabajo ya correcto. (outcome-accounting parte 2)
3. "Tu agente de voz gasta el 30% de sus tokens en decidir, no en responder."
4. VoxTurn: una pasada, todas las preguntas de turn-taking. La convergencia de
   instrumentos (nuestro writeup de los 4 instrumentos, 4 meses después).
5. El nuevo benchmark System One (2610.00346): el wave ya tiene su leaderboard.
   Qué mide y qué no. (necesita verificación antes de publicar)

## Upgrade concreto para jev-mini-bench (propuesta)

Añadir una **categoría "batched voice decisions"**: mismo set de decisiones (turn
complete, backchannel, barge-in, safe/unsafe, summary) mostrando 3 columnas:
generación JSON (1.57s), token único (92ms), batched window (94-103ms/8 eventos).
Consumidor: la pieza LinkedIn 1 y el funnel del Space. Coste: ~100 líneas en
index.html con los datos ya verificados del paper (citar fuente en la UI).

RESEARCH-DECISIONS COMPLETE: 14 facts
