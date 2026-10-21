# RESEARCH BRIEF: clúster speculative listening (adaptive chunking + endpoint anticipation)

*Fecha: 2026-10-21 noche. Bus: t06-noche5-brief-speculative. Método: 7 papers verificados por
título y abstract vía arXiv export API (fetch por subprocess, relay 8899, logs en
runtime/verify_papers_t06_2026-10-21*.py). Voice-Light y Heartbeat tienen lectura de texto
completa previa en la KB (2026-10-08 y 2026-10-21). Regla de evidencia aplicada: cada número
con paper y sección; lo no verificado no se cita.*

## 1. Tesis del clúster: de decidir-por-reloj a decidir-por-eventos

La pila de voz en tiempo real heredó sus decisiones del transporte: el audio viaja en chunks
fijos (20 ms de códec), y de ahí se colaron decisiones de producto que en realidad son
supuestos sobre el hablante sin medir. El clúster de papers de 2026 muestra la industria
revirtiendo eso capa a capa: cada decisión crítica (cuándo acaba el turno, cuándo se emite
el transcript, cuándo se lanza la respuesta, cuánto cómputo se hace mientras escuchan)
pasa de un umbral de reloj a una decisión condicionada por evidencia del propio stream.

Tres capas independientes aterrizaron el mismo principio el mismo trimestre:

- **ASR**: X2Streaming-ASR (2609.08672) elimina el chunk fijo y sustituye el commit del
  transcript por una política entrenada que decide cuándo emitir y qué emitir (abstract).
- **Framework**: nuestro PR livekit/agents#7994 documenta el daño del reloj mal puesto: un
  timeout pensado para medir silencio entre chunks se había convertido en deadline de la
  petición entera, matando streams sanos a mitad de frase (PR body, 05a0a1e).
- **Decisión**: DuplexJev (2610.02638, vía factsheet decision-models de la KB) mide que
  leer 10 decisiones como tokens sueltos cuesta 92 ms frente a 1.57 s generándolas como
  JSON (17x), y agrupa en ventanas de 160 a 200 ms que siguen el ritmo del hablante, no
  del reloj (factsheet 2026-10-22-factsheet-decision-models.md, paper leído).

El clúster speculative listening es la consecuencia natural: si las decisiones son por
eventos, el hueco entre eventos deja de ser tiempo muerto y se vuelve tiempo especulativo.
Endpoint Anticipation (2606.13450) lo dice explícito: anticipar el endpoint hasta 2.56 s
antes (abstract) para ejecutar LLM y TTS sobre contexto parcial. Heartbeat Thinking
(2610.26233) generaliza: no especular solo antes del endpoint, sino durante toda la escucha,
preservando el cómputo en curso cuando llega input nuevo (abstract).

## 2. Taxonomía de puntos de especulación

Cuatro puntos donde el sistema decide antes de tener certeza. Cada uno tiene papers con
mecanismo distinto y métrica propia (todavía no hay métrica unificada, ver gaps).

### 2.1 Predicción EOT (¿cuándo acaba el turno?)

- **Endpoint Anticipation** (2606.13450): de detección reactiva a forecast proactivo del
  end-of-turn en arquitecturas cascaded; su modelo de speech anticipa endpoints hasta 2.56 s
  antes (abstract) y propone métricas para el trade-off entre latencia ganada y riesgo.
- **JAL-Turn** (2603.26515, Recho Inc): predicción hold/shift por fusión acústica-lingüística
  con cross-attention sobre encoder ASR congelado y compartido; corre en paralelo con el ASR,
  sin latencia extra end-to-end (abstract). Validado en Easy-Turn, Smart-Turn y un dataset
  japonés propio; sin números en abstract, cualitativo.
- **SpeculativeETD** (2503.23439): detección de fin de turno en dos etapas (GRU ligero
  on-device para no-speech en tiempo real + Wav2vec en servidor para turno vs pausa), y el
  ETD Dataset, primer dataset público de end-turn detection (abstract). Sin números en
  abstract, cualitativo.

### 2.2 Commit adaptativo ASR (¿cuándo emito el transcript?)

- **X2Streaming-ASR** (2609.08672, X Square Robot): "wait when uncertain, emit when ready".
  Descompone el streaming en cuándo hacer commit y qué hacer commit; política refinada con
  recompensas group-relative a nivel de carácter (abstract). En 10 test sets chino/inglés,
  latencia de commit media más baja respecto a endpoints forzados: 32 a 109 ms en caracteres
  chinos y 12 a 85 ms en palabras inglesas, con accuracy comparable (abstract). Código público
  en github.com/X-Square-Robot/X2Streaming-ASR (abstract).
- **Nuestro PR #7994** (livekit/agents, abierto, head 05a0a1e): la misma intuición en la capa
  de framework. El plugin de Google convertía conn_options.timeout en dos deadlines de petición
  entera (genai deriva X-Server-Timeout; aiohttp usa ClientTimeout(total)); el fix acota el
  silencio entre chunks en vez del request completo, para que un stream sano y largo no muera
  a mitad de frase sin failover (PR body verificado vía API, 2026-10-21).

### 2.3 Generación especulativa de respuesta (¿preparo la salida antes de la certeza?)

- **Voice-Light** (2609.20995, texto completo leído 2026-10-08): cascada full-duplex con
  generación especulativa PRIVADA: texto y PCM candidatos durante el habla del usuario,
  promovidos solo si las revisiones del ASR final son cosméticas; cambio léxico invalida.
  Trigger acústico: 80 ms de baja probabilidad Silero abren candidato, fallback a 160 ms.
  Coste honesto medido: su checkpoint aprendido quedó en 12.53% EOT recall a 2.70%
  false-cutoff frente a 95.60% de la política temporal Silero; el gate conjunto
  (false cutoff <= 5%, recall >= 70%, p95 <= 800 ms) no lo superó ningún detector barrido
  (secciones de resultados, key_claims en papers/braun2026voicelight.md). Desplegaron el
  controlador híbrido, no la política aprendida.
- **Speculative Interaction Agents** (2605.13360, Berkeley/ICSI/LBNL): async I/O que separa el
  hilo reason-and-act de la espera de usuario o entorno, más speculative tool calling cuando
  el agente no sabe si tiene la información completa (abstract). Speedups 1.3 a 1.7x con
  modelos cloud sin reentrenar; 1.6 a 2.2x con Qwen2.5-3B-Instruct y Llama-3.2-3B-Instruct
  con una metodología de entrenamiento clock-based (abstract).

### 2.4 Speculative listening (¿cómputo útil durante toda la escucha?)

- **Heartbeat Thinking** (2610.26233, Ant International, texto leído 2026-10-21): invocaciones
  periódicas del Thinker que leen el transcript parcial y un registro compartido de razonamiento
  y tools completados; las invocaciones en curso y las tools despachadas SOBREVIVEN a input
  nuevo (eso es lo que las ventanas fijas tipo SHANKS no permiten, abstract). Números: en
  FDBench v3 sube la cobertura especulativa de tools 16 puntos porcentuales y baja la latencia
  media de respuesta final un 36.4% (abstract); STC 34.7 a 50.7 contra baseline sin especulación
  (sección de resultados, verificado en lectura del paper 2026-10-21, factsheet-4-topologies).
  Efecto sobre calidad final de tarea dependiente del benchmark (abstract, honesto).

Orden de lectura de la taxonomía: 2.1 y 2.2 deciden CUÁNDO; 2.3 y 2.4 deciden QUÉ hacer con
el tiempo que 2.1 y 2.2 liberan. Un agente de voz completo necesita los cuatro; ningún paper
del clúster los integra (gap 1).

## 3. Números verificados por paper

| Paper | Número | Fuente (paper + sección) |
|---|---|---|
| 2606.13450 Endpoint Anticipation | hasta 2.56 s de anticipación | abstract (arXiv API, 2026-10-21) |
| 2609.08672 X2Streaming-ASR | commit 32 a 109 ms (zh), 12 a 85 ms (en) | abstract (arXiv API, 2026-10-21) |
| 2610.26233 Heartbeat Thinking | latencia final media -36.4%; cobertura tools +16 pp; STC 34.7 a 50.7 | abstract + sección de resultados (lectura 2026-10-21, factsheet-4-topologies) |
| 2605.13360 Speculative Interaction Agents | 1.3 a 1.7x (cloud); 1.6 a 2.2x (3B edge) | abstract (arXiv API, 2026-10-21) |
| 2609.20995 Voice-Light | 758 ms mediana final-VAD a primer audio; turnos promovidos 667 ms vs 1513 ms; learned 12.53% recall a 2.70% false-cutoff vs 95.60% Silero; trigger 80/160 ms | texto completo leído 2026-10-08, resultados (papers/braun2026voicelight.md) |
| 2610.02638 DuplexJev (contexto cross-capa) | 92 ms tokens sueltos vs 1.57 s JSON (17x); ventanas 160 a 200 ms | factsheet 2026-10-22-factsheet-decision-models.md (paper leído) |
| 2503.23439 SpeculativeETD | sin números en abstract | cualitativo solo |
| 2603.26515 JAL-Turn | sin números en abstract | cualitativo solo |
| Nuestro bench (event-driven-voice-orchestrator) | serial 4343 ms vs event-driven 1141 ms (RTT 1s, 4 tools); ack < 260 ms; 32/32 invariantes en sweep RTT 10 a 2000 ms x tools 1 a 4 | builds/event-driven-voice-orchestrator/README.md + bench/ |
| livekit/agents#7994 (nuestro) | fix de deadline de request entera a bound de silencio entre chunks | PR body, head 05a0a1e (API, 2026-10-21) |

No verificado y por tanto NO citado en este brief: cifras internas de JAL-Turn y SpeculativeETD
(sus abstracts no traen números; unread: verify before quoting si alguien los necesita).

## 4. Conexiones con nuestros artefactos

- **PR livekit/agents#7994 = instanciación framework del clúster.** El mismo cambio de fondo
  que X2Streaming aplica al commit del ASR, nosotros lo aplicamos a la semántica de timeouts:
  decidir por eventos (silencio entre chunks) y no por reloj (deadline de request). Es el
  tercer ejemplo independiente de la pieza LinkedIn y el único a nivel framework.
- **Pitch ghost-reply** (bus/ideas/IDEATOR_out_event-driven-orchestrator.md): la lane fantasma
  con contador de especulaciones adoptadas/descartadas es la visualización del punto 2.3 + 2.4.
  Heartbeat (-36.4% en FDBench v3) es la prueba académica de que la experiencia tiene sustancia;
  Voice-Light aporta el momento honesto (667 ms vs 1513 ms cuando la promoción funciona, y la
  evaporación visible cuando el hablante cambia de idea). Ningún paper mide el coste visible
  del descarte (gap 5): el Space lo mediría por diseño.
- **Pieza fixed-chunking-is-dead** (writing/linkedin/2026-10-21-linkedin-fixed-chunking-is-dead.md):
  el brief extiende su tesis de tres capas a cuatro puntos de especulación; el tercer paper
  que pedía la pieza como confirmación ya está (X2Streaming + DuplexJev + #7994) y este
  brief añade la capa de anticipación (2606.13450) que la pieza no cubría.
- **Orchestrator bench (32 invariantes)**: el conformance kit es el árbitro natural para
  importar métricas del clúster: la invariante de turn-ack (< 260 ms) es el análogo
  event-driven de la predicción EOT del punto 2.1, y el abstract de SpeculativeETD (2503.23439)
  define el par accuracy/coste que el factsheet de benchmarks ya marcó como METRICIMPORT
  candidate. El port JS de la política de emisión (ghost-reply) se valida contra estas
  invariantes, igual que el port de la política de #7994.

## 5. Gaps abiertos y qué paper los cerraría

1. **Métrica unificada entre los cuatro puntos.** Cada paper mide lo suyo: commit latency
   (X2), recall/false-cutoff (Voice-Light, SpeculativeETD), STC y cobertura (Heartbeat),
   speedup (Speculative Interaction). FDBench v3 es el más cercano pero solo cubre 2.3/2.4.
   Lo cierra un benchmark que puntué los cuatro puntos en un protocolo (un hipotético
   FDBench v4 con capa de commit adaptativo, o un paper de posicionamiento tipo survey con
   re-evaluación cruzada).
2. **Gate semántico sobre el trigger de especulación.** Voice-Light lo declara open question:
   su trigger es acústico (80/160 ms) y su política aprendida falló el eval; jung2026speculativetool
   (KB semantic_vad) también es rule-based. Nadie gatea el dispatch especulativo con semántica
   del transcript parcial. Lo cierra un paper que use una señal tipo jev-vad (dos preguntas
   sobre el interim) como veto de especulación; es literalmente el gap SV4 de nuestra KB.
3. **Formalismo común del commit.** ASR (cuándo emito transcript), EOT (cuándo cierro turno) y
   framework (cuándo expira un wait) son el mismo tipo de decisión: emitir bajo incertidumbre
   con coste asimétrico. No existe tratamiento formal unificado. Lo cierra un paper de
   formalización (candidato natural: nosotros, conectando #7994 + X2 + 2606.13450 bajo un
   marco de decisión tipo SPRT; ya tenemos wald1947sprt en la KB).
4. **Anticipación vs riesgo en una sola curva cross-arquitectura.** 2606.13450 reporta 2.56 s
   de anticipación; JAL-Turn optimiza accuracy en paralelo al ASR; nadie compara
   anticipación-temprana contra cutoff-risk en cascada y full-duplex con el mismo protocolo.
   Lo cierra un benchmark cross-arquitectura de decisiones de turno (Easy-Turn/Smart-Turn
   ampliado con métrica de coste del error).
5. **Contabilidad de adopción/descarte.** Voice-Light cuenta promociones, Heartbeat cuenta
   cobertura; nadie mide el coste de usuario del descarte visible (respuesta que muere).
   Lo cierra un eval con métrica de "waste rate" percibido; nuestro ghost-reply sería el
   instrumento y el conformance kit el protocolo si el Nov paper revive.

## 6. Veredicto: topic propio o sección del CD?

**Sección del CD (este brief como ancla), no topic nuevo todavía.** Razones:

- La convergencia ya estaba anotada en TOPIC_STATE.md (2026-10-21): "the lane converged on
  anticipation / speculation / adaptive emit". Este brief documenta esa convergencia con
  números; no descubre un clúster nuevo que requiera gaps doc propio.
- Densidad insuficiente para topic: 7 papers, de los cuales 2 tienen lectura completa en la
  KB (Voice-Light ya fichado en semantic_vad, Heartbeat ya anotado contra el conformance kit)
  y 2 solo cualitativos. Los papers 2.1 viven mejor en semantic_vad/orchestration, donde ya
  están sus vecinos (VAP, TurnGPT, FD-VAD, smart-turn).
- Condición de promoción a topic propio: que aterrice el gap 1 (benchmark unificado) o el
  gap 2 (gate semántico de especulación). Si eso ocurre, este brief es el esqueleto del
  nuevo topic y los 4 puntos de la taxonomía pasan a ser sus subtopics.
- Acción práctica ahora: enlazar este brief desde INDEX.md y TOPIC_STATE.md; usar la
  taxonomía de 4 puntos como estructura del related-work SI el Nov paper del cajón se
  reactiva (el marco de commit unificado del gap 3 es la aportación propia más barata).

## Fuentes

- arXiv export API, fetch 2026-10-21 (runtime/verify_papers_t06_2026-10-21_b.py y _c.py):
  títulos y abstracts de 2606.13450, 2603.26515, 2605.13360, 2609.08672, 2610.26233,
  2503.23439, 2609.20995 (7/7 títulos verificados).
- GitHub API: livekit/agents#7994 (abierto, head 05a0a1e, actualizado 2026-10-21T06:53Z) y
  iamdgarcia/event-driven-voice-orchestrator (README con invariantes).
- KB interna: papers/braun2026voicelight.md (lectura completa 2026-10-08);
  FACTSHEET_voice_benchmark_wave_2026-10-22.md (Heartbeat STC verificado en lectura 2026-10-21);
  writing/factsheets/2026-10-21-factsheet-4-topologies.md y 2026-10-22-factsheet-decision-models.md
  (DuplexJev); bus/ideas/IDEATOR_out_event-driven-orchestrator.md;
  writing/linkedin/2026-10-21-linkedin-fixed-chunking-is-dead.md;
  builds/event-driven-voice-orchestrator/README.md.
