# Las 5 diferencias que nadie te explica entre los modelos de voz en cascada y los modelos nativos de voz

*Por Daniel Garcia Pena*

---

Si has experimentado con asistentes de voz basados en IA en los últimos dos años, habrás notado algo molesto: hay un silencio extraño entre cuando terminas de hablar y cuando el sistema empieza a responderte.

No es un bug. Es arquitectura.

Hemos publicado un paper que formaliza exactamente por qué ocurre esto — y demuestra matemáticamente que en algunos casos **no tiene solución**, sin cambiar la arquitectura completa. Hoy te lo cuento en humano.

---

## Un poco de contexto: dos formas de hacer IA de voz

Cuando hablas con un asistente de voz, puede estar construido de dos maneras radicalmente distintas:

**Arquitectura en cascada:** tres modelos independientes encadenados.
1. Un modelo de reconocimiento de voz (ASR) que convierte tu audio en texto.
2. Un modelo de lenguaje (LLM) que procesa ese texto y genera una respuesta.
3. Un modelo de síntesis de voz (TTS) que convierte el texto de vuelta en audio.

**Modelo nativo de voz:** un solo modelo que recibe audio y devuelve audio directamente. Sin intermediarios. Aquí es donde vive GPT-4o Realtime, Gemini Live o Moshi.

A primera vista parece que el modelo nativo es claramente superior. Pero la realidad es bastante más matizada. Estas son las cinco diferencias que importan.

---

## Diferencia 1: El silencio tiene un suelo que no puedes romper

Esta es la idea central de nuestro paper, y es más contraintuitiva de lo que parece.

En una arquitectura en cascada, el tiempo de silencio entre que terminas de hablar y que el sistema empieza a responderte es **la suma de las latencias de los tres modelos**. Llámalo el "silence gap".

Lo que demostramos formalmente es que ese silence gap tiene un **suelo irreducible** — una cantidad mínima de tiempo que ninguna mejora de hardware o de modelos puede eliminar, porque es consecuencia de la *topología* del pipeline, no de la *calidad* de los modelos.

La fórmula es sencilla:

> **Suelo de latencia = Σ latencias irreducibles de cada etapa**

¿Qué significa "latencia irreducible"? La parte de la latencia de cada modelo que viene impuesta por lo que tiene que hacer, no por lo bien o mal que lo hace. El modelo ASR no puede reconocer el audio antes de tener el audio. El LLM no puede generar el primer token antes de procesar el contexto completo. El TTS no puede producir audio antes de tener texto.

En los números reales de sistemas actuales, ese suelo ronda los **800–1.200 ms**. El umbral a partir del cual los humanos percibimos una respuesta como "rara" o "lenta" es de unos **200 ms**.

Es decir: la arquitectura en cascada estándar es, por construcción matemática, entre 4 y 6 veces más lenta que el umbral de percepción humana. Y ninguna GPU más rápida lo va a arreglar.

---

## Diferencia 2: Cada paso de razonamiento del agente multiplica el problema

Hasta ahora hablábamos de un intercambio simple: usuario habla → sistema responde.

Pero los sistemas modernos de voz son agentes: pueden usar herramientas, consultar bases de datos, hacer múltiples llamadas a APIs. Aquí la cascada tiene un problema adicional que formalizamos con lo que llamamos el **ReAct extension**.

En un agente que razona en múltiples pasos (el patrón ReAct: Reason → Act → Observe → Reason…), cada paso de razonamiento añade un ciclo completo de latencia al silence gap.

Si el agente necesita dos pasos de razonamiento, el suelo de latencia se duplica. Tres pasos, se triplica.

El modelo nativo de voz tiene la misma limitación de razonamiento, pero al eliminar las etapas ASR y TTS, el impacto de cada paso adicional es mucho menor.

Para agentes de voz complejos que requieren múltiples tool calls secuenciales, **la cascada se vuelve competitivamente inviable** desde el primer principio, no solo en la práctica.

---

## Diferencia 3: El modelo nativo no es tan rápido como parece

Aquí va el matiz que la mayoría de la gente no conoce: los modelos nativos de voz tampoco cumplen el umbral de 200 ms. No porque sean malos — sino porque hay dos clases arquitectónicas distintas.

**Clase buffer-and-commit (GPT-4o Realtime, Gemini Live):** el servidor acumula tu audio mientras hablas, espera a que termines, y *entonces* inicia la inferencia. El resultado: 320–500 ms de silencio. Mejor que la cascada, pero fuera del umbral humano ideal de 200 ms.

**Clase causal-streaming (Moshi):** el modelo procesa cada frame de audio en tiempo real mientras hablas. Cuando terminas, el modelo ya lleva el contexto casi completo prefilled. El silence gap baja a ~160 ms — dentro del umbral humano.

La diferencia entre los dos es si el modelo "esconde" el trabajo de prefill durante el tiempo en que hablas. La arquitectura en cascada estándar no puede hacer esto — pero existe una variante (el "streaming cascade") que sí puede, y que explicamos en el paper.

---

## Diferencia 4: La cascada tiene ventajas estructurales que el nativo no puede igualar

Este es el punto donde la cascada se defiende, y es importante entenderlo.

Los modelos nativos de voz son mejores en latencia de respuesta. Pero la cascada tiene ventajas que no son negociables para muchos casos de uso reales:

**Coste.** Las APIs de voz nativa (GPT-4o Realtime) cuestan entre 5× y 10× más que construir una cascada con Whisper + un LLM text + un TTS como ElevenLabs o Cartesia. Para un producto en producción con miles de llamadas diarias, esto importa.

**Auditabilidad.** La cascada produce texto intermedio: tienes el transcript del usuario, la respuesta del LLM en texto, antes de que llegue al TTS. Puedes aplicar guardrails de contenido en la capa de texto, loggear, auditar, depurar. El nativo es una caja negra de audio a audio.

**Tool use real.** Los frameworks de agentes (LangGraph, LlamaIndex, herramientas propias) están optimizados para texto. Encajar un modelo nativo de voz en un pipeline de agente con tool calling complejo es substancialmente más difícil que hacerlo con un LLM de texto en la posición central de la cascada.

**Intercambiabilidad.** En la cascada puedes cambiar el LLM por cualquier otro modelo sin tocar el ASR ni el TTS. Puedes actualizar el TTS independientemente. En el nativo, el modelo es monolítico.

---

## Diferencia 5: Existen tres palancas que de verdad reducen el suelo — y cuatro que solo lo disfrazan

Esta es quizá la parte más útil del paper para cualquiera construyendo un sistema de voz hoy.

Hemos clasificado **siete estrategias de mitigación** según si atacan el suelo irreducible o simplemente lo disfrazan:

### ✅ Palancas estructurales (reducen el suelo real)

**1. TTS en streaming:** en lugar de esperar toda la respuesta del LLM, el TTS empieza a sintetizar audio en cuanto tiene las primeras palabras. Reduce directamente el suelo irreducible. Es la primera optimización que deberías implementar en cualquier sistema en cascada, y tiene un coste de ingeniería relativamente bajo.

**2. ASR en streaming + prefill incremental del LLM:** usar un modelo ASR que emita tokens de texto en tiempo real mientras hablas (RNN-T, CTC streaming), y un LLM que vaya construyendo su KV cache mientras el usuario habla. Cuando terminas, el LLM ya lleva parte del trabajo hecho. Combinado con TTS streaming, el suelo baja a 220–440 ms — comparable a los mejores modelos nativos.

**3. Routing híbrido:** para turnos simples (preguntas factuales, respuestas cortas, sin tool calls) usa la cascada. Para turnos complejos, deriva al modelo nativo. Es la única estrategia que puede eliminar completamente el suelo de la cascada para los turnos donde más importa, aunque añade complejidad de integración.

### ⚠️ Palancas cosméticas (disfrazan el problema sin reducirlo)

**4. Filler generation:** reproducir "um", "déjame ver", "un momento" mientras el LLM procesa. Reduce el silencio *percibido* sin reducir la latencia real. Útil como complemento, engañoso como estrategia principal.

**5. Detección de barge-in:** permite al usuario interrumpir al agente. No reduce el silence gap, pero mejora la percepción de naturalidad de la conversación.

**6. Speculative decoding:** hace al LLM más rápido en generar tokens, pero tiene efecto mínimo en el tiempo-hasta-primer-token (que es la parte que determina el silence gap, no la velocidad de generación posterior).

**7. Ejecución paralela de tool calls:** cuando las herramientas no tienen dependencias entre sí, ejecutarlas en paralelo reduce la latencia total del agente. Es una mejora real, pero solo ataca la parte reducible, no el suelo irreducible.

---

## ¿Qué significa todo esto en la práctica?

Si estás construyendo un producto de voz hoy, aquí está la recomendación directa que se desprende del análisis:

1. **Empieza con cascada si tu caso de uso requiere tool calling complejo, auditoría, o control de costes.** El modelo nativo no te va a dar esas ventajas.

2. **Implementa TTS en streaming inmediatamente.** Es la optimización de mayor impacto y menor coste. Sin esto, estás dejando 300–500 ms de latencia innecesaria sobre la mesa.

3. **Si el silencio te sigue matando, el siguiente paso es ASR en streaming.** Es más complejo de implementar (invalidación de KV cache, estabilidad de tokens), pero es la única manera de reducir el suelo de forma estructural sin cambiar a un modelo nativo.

4. **Considera routing híbrido** si tienes una proporción alta de turnos simples donde la latencia importa y puedes permitirte mantener dos pipelines en paralelo.

5. **No confundas velocidad percibida con latencia real.** Los fillers y el barge-in mejoran la experiencia, pero no son sustitutos de una arquitectura bien diseñada.

---

La conclusión incómoda del paper es que ninguna mejora de hardware o de modelos puede resolver el problema fundamental de la cascada para su configuración estándar. El suelo es un resultado matemático, no una limitación temporal.

Pero los sistemas en cascada siguen siendo competitivos — si sabes exactamente qué palancas mover y por qué.

---

*El paper completo está disponible en arXiv bajo cs.AI. Si tienes preguntas técnicas o quieres discutir cómo aplicar esto a tu sistema, responde a este post o escríbeme directamente.*

*— Daniel*
