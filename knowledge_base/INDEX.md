# Knowledge Base — Master Index

## Topics

| Topic | Papers | Gaps Doc | Last Updated |
|-------|--------|----------|-------------|
| [ai_guardrails](topics/ai_guardrails/) | 92 | [gaps.md](topics/ai_guardrails/gaps.md) | 2026-06-15 |
| [alignment](topics/alignment/) | 0 | — | — |
| [multimodal](topics/multimodal/) | 0 | — | — |
| [orchestration](topics/orchestration/) | 29 | [gaps.md](topics/orchestration/gaps.md) | 2026-09-01 |
| [semantic_vad](topics/semantic_vad/) | 36 | [gaps.md](topics/semantic_vad/gaps.md) | 2026-10-08 |

## Orchestration Papers (29 total)

### Tool Calling / Agent Loops
- [yao2023react](topics/orchestration/papers/yao2023react.md) — ReAct reasoning+acting loop
- [wei2023chainofthought](topics/orchestration/papers/wei2023chainofthought.md) — CoT reasoning hops
- [langgraph2024](topics/orchestration/papers/langgraph2024.md) — LangGraph graph orchestration
- [openai2024realtimeapi](topics/orchestration/papers/openai2024realtimeapi.md) — Realtime API (full-duplex + tools)
- [google2024geminivoice](topics/orchestration/papers/google2024geminivoice.md) — Gemini long-context voice
- [defossez2024moshi](topics/orchestration/papers/defossez2024moshi.md) — Moshi full-duplex native voice

### Streaming Inference / Memory
- [xiao2023streamingllm](topics/orchestration/papers/xiao2023streamingllm.md) — StreamingLLM attention sinks
- [leviathan2023fast](topics/orchestration/papers/leviathan2023fast.md) — Speculative decoding
- [packer2023memgpt](topics/orchestration/papers/packer2023memgpt.md) — MemGPT hierarchical memory [VERIFIED]

### Incremental Dialogue / Turn-Taking
- [baumann2012prosodic](topics/orchestration/papers/baumann2012prosodic.md) — incremental synthesis prosody (InproTK) [VERIFIED]
- [schlangen2011general](topics/orchestration/papers/schlangen2011general.md) — Incremental dialogue processing
- [skantze2021turn](topics/orchestration/papers/skantze2021turn.md) — Turn-taking survey / no standard
- [levinson2015timing](topics/orchestration/papers/levinson2015timing.md) — ~200 ms turn-taking norm
- [stivers2009universals](topics/orchestration/papers/stivers2009universals.md) — cross-cultural turn-taking
- [heldner2010gaps](topics/orchestration/papers/heldner2010gaps.md) — sub-100 ms overlap timing [VERIFIED]
- [schegloff2000overlap](topics/orchestration/papers/schegloff2000overlap.md) — overlaps as ordered structure [VERIFIED]
- [ward2000backchannel](topics/orchestration/papers/ward2000backchannel.md) — backchannel prosodic timing [VERIFIED]

### Endpointing / Barge-In / Interruption
- [raux2008optimizing](topics/orchestration/papers/raux2008optimizing.md) — endpointing threshold tradeoffs
- [raux2012optimizing](topics/orchestration/papers/raux2012optimizing.md) — deployed barge-in/response-delay [VERIFY]
- [bohus2011interruptions](topics/orchestration/papers/bohus2011interruptions.md) — interruption as engagement policy [VERIFY]

### Tool Hiding / Orchestration Overlap
- [specrag2024](topics/orchestration/papers/specrag2024.md) — Speculative RAG retrieval overlap [VERIFIED]
- [tilt2025](topics/orchestration/papers/tilt2025.md) — DEPRECATED: arXiv id is a physics paper; do not cite
- [taubench2024](topics/orchestration/papers/taubench2024.md) — tau-bench latency+price eval [VERIFIED]
- [agentsnotenough2024](topics/orchestration/papers/agentsnotenough2024.md) — prefetch/skip-tool [VERIFIED]

- [lin2025fullduplexbench](topics/orchestration/papers/lin2025fullduplexbench.md) — Full-Duplex-Bench turn-taking benchmark [VERIFIED]
- [lin2026fdbv3](topics/orchestration/papers/lin2026fdbv3.md) — Full-Duplex-Bench-v3 tool use [VERIFIED]
- [salimi2026ihbench](topics/orchestration/papers/salimi2026ihbench.md) — IHBench post-interruption recovery [VERIFIED]
- [li2025easyturn](topics/orchestration/papers/li2025easyturn.md) — Easy Turn turn-taking robustness [VERIFIED]
### Foundations / Cross-links
- [hewitt1973actor](topics/orchestration/papers/hewitt1973actor.md) — actor model / event-driven concurrency [VERIFY]
- [dong2024building](topics/orchestration/papers/dong2024building.md) — guardrail placement (cross-link to ai_guardrails)

## Semantic VAD Papers (33 total)
_See [topics/semantic_vad/](topics/semantic_vad/) — [gaps.md](topics/semantic_vad/gaps.md) (SV1-SV5), [FINDINGS.md](topics/semantic_vad/FINDINGS.md) for the engineering distillation._

### Decision Design / Question Framing (project results)
- jev-vad-poc (repo `github.com/iamdgarcia/jev-vad-poc`) — two-question semantic VAD, ES/EN framing ablations, th 0.30+filler-guard operating point (barge-in F1 0.76), turn-end near chance → veto-only role; 100-phrase frozen ES benchmark; dual-env latency (cloud p50 101-187 ms / p99 178-268 ms; laptop 326-609 ms). **Paper published 2026-10-08** ("Asking Instead of Listening", external venue; alphaXiv upload rejected by auto-review 2026-10-08, appeal sent to contact@alphaxiv.org)

### Speculative Dispatch / Latency Hiding (SV4 line)
- [braun2026voicelight](topics/semantic_vad/papers/braun2026voicelight.md) — Voice-Light: private speculative generation, acoustic trigger, honest negative on learned turn policy [VERIFIED]
- [jung2026speculativetool](topics/semantic_vad/papers/jung2026speculativetool.md) — Qualcomm speculative tool execution from partial ASR, on-device [VERIFIED]

### Turn-Shift / Turn-End Prediction (text and audio)
- [ekstedt2020turngpt](topics/semantic_vad/papers/ekstedt2020turngpt.md) — TurnGPT text-side turn-shift scoring
- [ekstedt2022vap](topics/semantic_vad/papers/ekstedt2022vap.md) — VAP audio-side continuous projection
- [mathur2026fdvad](topics/semantic_vad/papers/mathur2026fdvad.md) — FD-VAD streaming audio-side semantic endpointer (2609.35791), SOTA in its niche [VERIFIED]
- [umair2024turntaking](topics/semantic_vad/papers/umair2024turntaking.md) — LLM+acoustic fusion (ICASSP)
- [ruede2017probabilistic](topics/semantic_vad/papers/ruede2017probabilistic.md) — probabilistic backchannel prediction
- [li2025easyturn](topics/semantic_vad/papers/li2025easyturn.md) — Easy Turn acoustic+linguistic fusion
- [pipecat2024smartturn](topics/semantic_vad/papers/pipecat2024smartturn.md) — smart-turn v3.2 audio EOT (146 ms p50 verified, 8.7 MB)
- [livekit2024turn](topics/semantic_vad/papers/livekit2024turn.md) — LiveKit transcript turn detector (comparator)

### Commercial Semantic Endpointing (proprietary anchors)
- [deepgram2024semanticvad](topics/semantic_vad/papers/deepgram2024semanticvad.md) — Deepgram Flux / semantic VAD
- [openai2024realtime](topics/semantic_vad/papers/openai2024realtime.md) — OpenAI Realtime semantic turn detection
- [elevenlabs2025semantic](topics/semantic_vad/papers/elevenlabs2025semantic.md) — ElevenLabs semantic endpointing
- [google2025gemini](topics/semantic_vad/papers/google2025gemini.md) — Gemini Live / Chirp 3 endpointing floor (500 ms)

### Benchmarks (full-duplex family; cascade gap = SV2)
- [fullduplexbench2025](topics/semantic_vad/papers/fullduplexbench2025.md) — Full-Duplex-Bench (2503.04721)
- [fullduplexbenchv15](topics/semantic_vad/papers/fullduplexbenchv15.md) — overlap handling (2507.23159)
- [fullduplexbenchv2](topics/semantic_vad/papers/fullduplexbenchv2.md) — multi-turn + simulator (2510.07838)
- [fullduplexbenchv3](topics/semantic_vad/papers/fullduplexbenchv3.md) — tool use under disfluency (2604.04847)
- [salimi2026ihbench](topics/semantic_vad/papers/salimi2026ihbench.md) — IHBench interruption recovery (2606.19595)

### Enabling Technology / Backbones
- [mmbert2025](topics/semantic_vad/papers/mmbert2025.md) — mmBERT multilingual encoder (2509.06888), System-1 backbone
- [warner2024modernbert](topics/semantic_vad/papers/warner2024modernbert.md) — ModernBERT (2412.13663)
- [wang2020minilm](topics/semantic_vad/papers/wang2020minilm.md) — MiniLM distillation
- [onnx2024quantization](topics/semantic_vad/papers/onnx2024quantization.md) — int4 quantization (deployment vehicle)

### Acoustic VAD Baseline Lineage
- [webrtcvad](topics/semantic_vad/papers/webrtcvad.md) — classic GMM VAD
- [bredin2020pyannote](topics/semantic_vad/papers/bredin2020pyannote.md) — pyannote.audio
- [silero2024vad](topics/semantic_vad/papers/silero2024vad.md) — Silero VAD (production default)
- [ardila2020common](topics/semantic_vad/papers/ardila2020common.md) — Common Voice (audio source)

### Timing / Conversation-Analysis Foundations
- [stivers2009universals](topics/semantic_vad/papers/stivers2009universals.md) — ~200 ms universal gap
- [levinson2015timing](topics/semantic_vad/papers/levinson2015timing.md) — anticipatory projection
- [heldner2010gaps](topics/semantic_vad/papers/heldner2010gaps.md) — gap/overlap distribution
- [yngve1970getting](topics/semantic_vad/papers/yngve1970getting.md) — backchannel coinage
- [ward2000prosodic](topics/semantic_vad/papers/ward2000prosodic.md) — backchannel prosody
- [raux2008optimizing](topics/semantic_vad/papers/raux2008optimizing.md) — endpointing threshold trade
- [skantze2021turn](topics/semantic_vad/papers/skantze2021turn.md) — turn-taking review (no standard eval)
- [schlangen2011incremental](topics/semantic_vad/papers/schlangen2011incremental.md) — incremental processing model
- [defossez2024moshi](topics/semantic_vad/papers/defossez2024moshi.md) — Moshi full-duplex native

### Cross-links
- Orchestration topic: `raux2008optimizing`, `skantze2021turn`, `schlangen2011general` (same works, system-level angle); gaps OG2 (cessation) and OG5 (measurement) compose with SV3/SV4.


## AI Guardrails Papers (92 total)

### Methodology
- [kitchenham2007guidelines](topics/ai_guardrails/papers/kitchenham2007guidelines.md) — SLR protocol guidelines
- [page2021prisma](topics/ai_guardrails/papers/page2021prisma.md) — PRISMA 2020 reporting standard

### Foundations
- [bommasani2022opportunities](topics/ai_guardrails/papers/bommasani2022opportunities.md) — Foundation model risks
- [weidinger2021ethical](topics/ai_guardrails/papers/weidinger2021ethical.md) — LLM harm taxonomy
- [ouyang2022training](topics/ai_guardrails/papers/ouyang2022training.md) — InstructGPT / RLHF
- [bai2022constitutional](topics/ai_guardrails/papers/bai2022constitutional.md) — Constitutional AI
- [touvron2023llama2](topics/ai_guardrails/papers/touvron2023llama2.md) — Llama 2 dual-RM architecture
- [dong2024building](topics/ai_guardrails/papers/dong2024building.md) — Guardrails survey (prior work)

### Extrinsic Guardrails / Frameworks
- [inan2023llama](topics/ai_guardrails/papers/inan2023llama.md) — Llama Guard classifier
- [rebedea2023nemo](topics/ai_guardrails/papers/rebedea2023nemo.md) — NeMo Guardrails / Colang

### Attacks
- [zou2023universal](topics/ai_guardrails/papers/zou2023universal.md) — GCG universal adversarial suffix
- [wei2023jailbroken](topics/ai_guardrails/papers/wei2023jailbroken.md) — Jailbreak failure mode analysis
- [perez2022red](topics/ai_guardrails/papers/perez2022red.md) — LLM red-teaming with LLMs

### Defences
- [robey2023smoothllm](topics/ai_guardrails/papers/robey2023smoothllm.md) — SmoothLLM randomised smoothing
- [jain2023baseline](topics/ai_guardrails/papers/jain2023baseline.md) — Baseline defence evaluation
- [xie2023defending](topics/ai_guardrails/papers/xie2023defending.md) — Self-reminder system prompt
- [cao2023defending](topics/ai_guardrails/papers/cao2023defending.md) — Robust alignment fine-tuning
- [kumar2023certifying](topics/ai_guardrails/papers/kumar2023certifying.md) — Certified safety (O(n^2))
- [varshney2023art](topics/ai_guardrails/papers/varshney2023art.md) — Defence strategy meta-analysis

### Evaluation
- [mazeika2024harmbench](topics/ai_guardrails/papers/mazeika2024harmbench.md) — HarmBench standardised eval

### Multimodal (Full Entries)
- [gong2023figstep](topics/ai_guardrails/papers/gong2023figstep.md) — FigStep typographic attacks
- [liu2024mmsafetybench](topics/ai_guardrails/papers/liu2024mmsafetybench.md) — MM-SafetyBench
- [luo2024jailbreakv](topics/ai_guardrails/papers/luo2024jailbreakv.md) — JailBreakV-28K
- [pi2024mllm](topics/ai_guardrails/papers/pi2024mllm.md) — MLLM-Protector
- [oh2024safevlm](topics/ai_guardrails/papers/oh2024safevlm.md) — SafeVLM
- [li2024vlguard](topics/ai_guardrails/papers/li2024vlguard.md) — VLGuard
- [wang2024adashield](topics/ai_guardrails/papers/wang2024adashield.md) — AdaShield adaptive prompts

### Stubs (65 entries — populate via deep-research)
zhang2024shieldlm, han2024wildguard, su2024aegis, yang2023shadow, qi2023finetuning, chen2024agentpoison, souly2024strongreject, huang2023survey, chiang2024chatbot, li2024salad, zhao2024evaluating, liu2023queryrelevant, niu2024jailbreaking, dong2024safeguarding, chen2024dresssafety, russinovich2024greatescalation, yang2024chain, li2024llm, meta2024llamaguard2, azure2024contentsafety, wei2023jailbreak, mehrotra2023tree, liu2023autodan, zhu2023autodan, perez2022ignore, yi2023benchmarking, wan2023poisoning, zou2024improving, pisano2023bergeron, wang2024defending, helbling2023llm, mo2024fight, goldowsky2023localizing, ganguli2022red, sun2023safety, zhang2023safetybench, shen2023anything, yuan2023gpt4, deng2023multilingual, zong2024safety, shi2023large, carlini2024aligned, cheng2024leveraging, anthropic2024claude3, google2024gemini, xhonneux2024efficient, kim2024break, zeng2024johnny, ding2023wolf, wei2024assessment, bhatt2023purple, zhou2024easyjailbreak, chen2024red, bailey2023image, shayegani2023jailbreak, qi2024visual, ghosh2024aegis2, yao2023survey, chang2024survey, pineau2021improving, yang2021fudge, qin2022cold, lu2021neurologic, leviathan2023fast, zhu2024gram
