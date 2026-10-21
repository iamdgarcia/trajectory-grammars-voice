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

### System-1 paired eval: "Fast Models, Slow Evidence" (2610.02267, Jiawei Li, 1-oct) VERIFICADO 21-oct noche

- Qué es: evaluación paired de un modelo System-1 open-weight (Laya) contra el hosted (Jev)
  en **11 puntos de decisión de agente** construidos de **18 fuentes públicas**: **7,283 casos
  base + 6,640 variantes de robustez**, inputs byte-idénticos, tests paired, reproducibilidad
  cross-hardware y cross-day. Fuente: paper, abstract + sección 4.
- Jev significativamente más preciso en **9 de 11** puntos (**+10.8 a +46.0 pp**); empate en
  RAG relevance gating; ninguno bate el azar en zero-shot model routing. Fuente: abstract + sección 5.
- Laya cambia el **30% de sus respuestas** al invertir el orden de opciones y cae a **31%** con
  50 herramientas vecinas (Jev mantiene 98% con tool única correcta). Fuente: abstract + sección 5.
- Self-audit (sección 7): 3 errores de análisis + 1 confound de diseño habían distorsionado las
  claims de despliegue: ahorro de pre-screen reportado **23.9%, real 4.3%** (coste del pre-screen
  omitido); gate accuracy presentada como calidad end-to-end (**58% vs 98%**); umbrales in-sample
  (objetivo 5%, hasta **17% de misses held-out**); "channel effect" en injection FPs que desaparece
  con contenido channel-native. Fuente: abstract + sección 7, tabla de claims corregidas.
- Qué aporta a nosotros: es la versión académica del outcome-accounting que defendemos. El ahorro
  del gate NO es el ahorro del sistema. Cita perfecta para la pieza LinkedIn D4 y para el diseño
  de jev-mini-bench (inputs byte-idénticos + tests paired como protocolo).
- Código y datos públicos: github.com/David-DL-Space/sys1-eval (repo verificado, public). Fuente:
  abs comments + API GitHub 21-oct.

### Benchmark System One vs clasificadores (2610.00346, Rafe y Das, 29-sep) VERIFICADO 21-oct noche

- Qué mide: un mismo harness envía las mismas peticiones semánticas a **8 checkpoints de
  decision models de 6 familias** (incluido Jev hosted) y **4 LLMs generativos abiertos de 3
  desarrolladores**, y puntúa también clasificadores entrenados y zero-shot sobre lo mismo:
  benchmarks de workflow (sintético), intents (**CLINC-150** con 150 intents + out-of-scope),
  **Banking77** (616 test queries x 77 intents), 4 tareas de social-science y emociones con
  raters que concuerdan. Fuente: abstract + secciones 4 y 5.1.
- Números clave: DeBERTa-v3-large fine-tuned es lo más preciso en todos los benchmarks
  etiquetados menos uno; sin labels, ningún decision model supera significativamente a Jev en
  workflows o intents (Gemma-4-31B lo iguala en workflows y le gana en CLINC-150 a más coste);
  riesgo garantizado del 5% deja a Jev **0.528** de las decisiones de intent; un threshold
  in-scope acepta aún **0.310** de peticiones out-of-scope; intercambiar yes/no voltea **50.5
  respuestas por 100** en Jev (generativos: al menos 16.8; fine-tuned: como mucho 6.5). Fuente:
  abstract + secciones 5.1 y 5.2.
- Corrección de nuestro scan: la cifra "16 votos, el más votado del wave" es FALSA hoy.
  Verificado en HF API 21-oct noche: la paper page tiene **0 upvotes**. No citar popularidad;
  citar solo contenido. Fuente: huggingface.co/api/papers/2610.00346.
- Adoptable como referencia externa de jev-mini-bench: SÍ, como CITE metodológico (no es voz,
  son decisiones de agente textual). Dos imports concretos: (1) el test de volteo yes/no con
  rubrics fijas como test de robustez de orden; (2) el D1 typed-decisions dataset está público
  en HF (LocalLLaMA/typed-decisions, 49,522 downloads verificados hoy) para calibrar nuestros
  umbrales de abstention. También existe el Decision Index (leaderboard comunitario, 70 modelos
  abiertos sobre 120,340 peticiones congeladas de 38 benchmarks) como referencia viva. Fuente:
  paper, secciones 3 y 5; HF API 21-oct.

### Narrow Decision Models (2610.25553, Softplan, 18-oct) VERIFICADO 21-oct noche

- Autores: 10 autores, todos @softplan.com.br. Empresa brasileña de software judicial. Fuente:
  abs HTML, bloque de autores.
- Arquitectura (NDM-Block): serializa la petición como **prefix tree** (estado, luego cada
  pregunta, luego cada opción) y corre un encoder bidireccional (mmBERT-base) bajo **block
  attention mask con posiciones lógicas**: la respuesta queda por construcción invariante al
  orden de opciones e independiente de qué otras preguntas se hacen. Tipos: Choice, Score,
  Noul (yes/no), con opción explícita "none of these" calibrada aparte (abstention). Fuente:
  abstract + secciones 4.2 a 4.5.
- Tamaño: **6.4M parámetros nuevos** (markers, proyecciones, set head, readings) sobre cuerpo
  entrenado de **110M** y embedding table congelada de **197M**. Fuente: sección 4.2 + apéndice B.
- Entrenamiento: proper scoring rules vía curriculum por etapas, temperatura post-hoc, abstention
  prior, decisiones selectivas. Fuente: sección 5.
- Validación mínima (sección 10): las invariancias se cumplen hasta redondeo (mayor diferencia
  1.5e-5 en float32); en 165 comunicaciones no vistas, greedy descent acierta la unidad final en
  **0.376** [0.297, 0.448] vs 0.152 de BM25 léxico y 0.067 del baseline primera opción; el bloque
  alcanza menor pérdida que un cross-encoder pairwise a igual cómputo; primera instancia
  entrenada con documentos legales reales concuerda con el clasificador LLM en producción en
  **91%** de documentos held-out. La evaluación real completa va en un paper companion. Fuente:
  abstract + secciones 10.1 a 10.6.
- Qué aporta a nosotros: es el contrapunto narrow al Jev generalista (misma interfaz, pesos
  propios, arquitectura abierta verificable). Para jev-mini-bench es un tercer tipo de
  competidor (clasificador calibrado con garantías de invariancia) y su protocolo de aceptación
  de mecanismo antes de abrir held-out (sección 9) es importable tal cual a nuestro bench.

### Cifra del Jev study (2610.13092) CONFIRMADA 21-oct noche: cita pública desbloqueada

- La cifra exacta es **4,500 task executions**. Aparece tres veces: abstract ("Across 4,500
  task executions"), bullets de contribuciones, y sección 4.2 Experimental Setup ("Each
  configuration runs three times on the same tasks, yielding 4,500 task executions").
- La aritmética cierra: 134 tareas ALFWorld x 3 runs x 6 configuraciones = 2,412; 116 tareas
  AndroidWorld x 3 runs x 6 configuraciones = 2,088; total 4,500. Fuente: apéndice B.1 ("402
  executions per ALFWorld configuration and 348 per AndroidWorld configuration", o sea 134 y
  116 tareas x 3 runs) + tabla 1 (6 configuraciones por benchmark).
- La línea "~4.500 ejecuciones" del factsheet-4-topologies (hf/writing/, NO editable en esta
  tarea) puede citarse ya en público sin la tilde: es exacta. Pendiente para el próximo
  agente con permiso de escritura en hf/writing/: quitar el "~" y la nota de no-citar.

### Escaneados (solo título verificado, números unread)

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
5. El benchmark System One vs clasificadores (2610.00346): decisiones tipadas con
   garantías: DeBERTa fine-tuned gana con labels, y el volteo yes/no de 50.5/100 del
   hosted model. VERIFICADO, publicable (sin la cifra de votos, que era falsa).

## Upgrade concreto para jev-mini-bench (propuesta)

Añadir una **categoría "batched voice decisions"**: mismo set de decisiones (turn
complete, backchannel, barge-in, safe/unsafe, summary) mostrando 3 columnas:
generación JSON (1.57s), token único (92ms), batched window (94-103ms/8 eventos).
Consumidor: la pieza LinkedIn 1 y el funnel del Space. Coste: ~100 líneas en
index.html con los datos ya verificados del paper (citar fuente en la UI).

RESEARCH-DECISIONS COMPLETE: 14 facts + 3 papers verificados 21-oct noche (02267, 00346, 25553)
+ cifra Jev study 4,500 confirmada (cita pública desbloqueada) + corrección: 00346 tiene 0
upvotes en HF hoy, la cifra de 16 votos del scan era falsa y no se cita.
