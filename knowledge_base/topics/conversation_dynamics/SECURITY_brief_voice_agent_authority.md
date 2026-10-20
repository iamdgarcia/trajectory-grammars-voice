# Security brief 2026-10-20 — Voice-agent authority (lane bancario)

*Derivado del research brief de 4 vías (mis día). Fuente principal: survey S2A
"From Acoustic Sensing to Physical Actions" (arXiv:2610.15390, 10-11) + SH-Bench/MSI-Bench
(via eval survey 2609.30798) + Aegis. Consumidor: el agente conversacional bancario (BC) y la
extensión del conformance kit. NO es paper — es el mapa de aplicar seguridad al producto.*

## El hueco central: identidad ≠ autoridad

Verbatim del gap del survey: *"identity attribution determines who is speaking, whereas
instruction authority determines what that identity may control"* — la distinción NO está
operacionalizada en agentes de voz. Todo el stack de ataques a memoria/estado (AgentPoison,
MINJA, MEXTRA, BackdoorAgent) está evaluado SOLO en agentes de texto; la unión
fuente+autoridad+acción es "weakly evaluated" en audio.

Para el banco esto es EL marco:
- **Identidad**: ¿quién habla? (ASV / speaker verification — spoofable, ver 2607.14753)
- **Autoridad**: ¿qué puede controlar ESA identidad en ESTA interacción? (session binding,
  permisos por producto, límites)
- La pregunta de riesgo real no es "¿es la voz de Daniel?" sino "¿esta instrucción hablada
  procede de alguien autorizado para esta cuenta/acción?" — spoofing de voz es solo UN vector;
  los otros dos son bystander (otra persona cerca del mic) y confusión de destinatario
  (speech dirigido a otra conversación/TV/radio).

## Superficies concretas del agente BC (perfil "Personal Task / Service" del S2A)

1. **Bystander speech en llamadas**: SH-Bench documenta que LALMs procesan habla de terceros.
   En una llamada telefónica (call-center de voz), audio de TV/fondo/familia puede entrar como
   instrucción. Mitigación operable: attribution de cada user-turn a fuente (caller vs canal) y
   require-confirm para acciones sensibles cuando la fuente sea ambigua.
2. **Acciones no-cancelables de estado**: el fallo documentado de Heartbeat (2610.26233) — carrito
   con precio antiguo tras revisión — ES un problema de seguridad además de latencia. En banca:
   preparación especulativa sobre instrucciones habladas incompletas puede disparar transferencias.
   Regla: acciones de débito/alta = NUNCA especulativas; solo lectura/búsqueda.
3. **Estado persistente en multi-user**: si el agente guarda contexto por usuario, la memoria es
   superficie de envenenamiento y de fuga (MEXTRA). Provenance en cada memoria escrita: quién la
   dijo, en qué sesión, con qué autoridad en ese momento.
4. **Traza como evidencia**: las aserciones de VAmoS sobre trazas (incl. tool calls + argumentos
   + filas retornadas) son el patrón para AUDITAR decisiones del agente bancario. La traza
   event-driven ya registra user-turns y tool-completions — falta el campo de authority en el
   evento (quién/qué rol autorizó).

## Extensión del conformance kit (célula de seguridad, propuesta)

Las 4 células actuales son invariantes de CONFIANZA (latencia/timing). Una 5ª célula de
AUTORIDAD sería:
- scripted caller + scripted bystander audio solapado → invariante: ninguna tool-call de
  escritura se dispara con provenance ambigua;
- invariante: toda tool-call en la traza lleva speaker-attribution + authority-check registrados;
- invariante: instrucciones de revisión/anulación aplican a generación (barge-in) pero NUNCA
  retro-activamente a acciones ya ejecutadas (non-cancelable = ack explícito antes).
Coste: bajo (el harness ya scripting; añade 1 actor + 3 checks). Decisión pendiente de user.

## Referencias mínimas

- S2A survey: 2610.15390 (6 áreas; gaps verbatim §V)
- SH-Bench (bystander/selective hearing): citado en 2609.30798 corpus
- MSI-Bench (multi-speaker authority/disclosure, 1.152 casos): 2609.24812
- Aegis (seguridad end-to-end en pipelines de voice agents con tools): citado en 2610.15390
- Spoofing-aware ASV: 2607.14753 · Audio jailbreak taxonomy: 2605.30031
- CaMeL/AgentSpec (contención de acciones): citados en 2610.15390 defenses
- Inyección por audio: 2604.14604 (hijacking LALMs), 2607.28165 (concurrente stealth)
