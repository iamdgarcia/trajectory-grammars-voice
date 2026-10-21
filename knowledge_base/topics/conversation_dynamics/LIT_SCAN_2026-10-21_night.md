# Lit scan 2026-10-21 night (delta over the 10-19/20/21 scans)

*Method: HF papers search API (huggingface.co/api/papers/search, 7 queries: voice agent,
turn taking, full duplex speech, endpointing, voice activity detection, speech agent,
decision model) plus arXiv API (export.arxiv.org, cat:cs.CL+cs.SD, submittedDate last 48h,
131 entries, sorted by submittedDate desc). Curl via python subprocess timeout, pattern from
runtime/recon_2026-10-21_noche5.py; script and raw output in
hf/runtime/litscan_2026-10-21_noche5.py and _out.txt. Seen set: 30 IDs from the three
previous scans plus 10 IDs from the two factsheets written this session
(FACTSHEET_voice_benchmark_wave_2026-10-22.md, FACTSHEET_decision_models_voice_loop_2026-10-22.md).
Raw result: 547 new IDs from HF, 43 after recency (published after 2026-08-22) and
lane-keyword filter; arXiv 48h gave 1 lane paper (2 keyword matches were false positives).
Votes below = upvotes field of the HF search API, read 2026-10-21. Abstracts read via API;
anything beyond the abstract is marked unread: verify before quoting.*

## Already filed today (appear in HF results but covered by this session's factsheets)

2610.02638 DuplexJev, 2609.34973 APEX-Voice, 2609.03423 DuplexSpeechBench-IFEval,
2609.38232 PACT-SLM. No new action; see the two FACTSHEET_2026-10-22 files.

## New papers, verdicts

### Group A: industrial async-delegation wave (orchestrator lane)

- **2609.13814** Realtime-Venus (9-12, 190 votes, highest-vote paper this wave):
  full-duplex interaction system with ASYNCHRONOUS DELEGATION, continuous perception
  across audio and video. Per abstract, delegation of heavy work off the conversational
  loop. This is the event-driven-orchestrator thesis with industrial mass behind it.
  FILE: update FINDINGS_event_driven_orchestration.md next touch; numbers unread:
  verify before quoting.
- **2609.14005** StepAudio 3 Realtime (9-12, 130 votes): industrial technical report,
  continuous listen-converse-think-act loop. Confirms the loop framing at foundation-model
  scale. WATCHLIST (technical report, no adoptable instrument expected).
- **2609.08977** Omni Interaction Agent, Gander (9-08, 93 votes): end-to-end omni model,
  streaming multi-modal input, agentic actions. WATCHLIST.
- **2609.19334** Frontend-backend architecture for tool calls in full-duplex S2S (9-18):
  a duplex speech-to-text frontend emits a DELEGATION TOKEN to a backend. Mechanism-level
  version of our orchestrator contract. FILE with group A.
- **2609.25195** Qwen-Audio-Agent (9-21): foreground-background harness, Frontend Agent
  manages dialogue and picks direct tool use vs delegation, Backend Agent executes.
  Same bridge pattern, third independent instance this wave. FILE with group A.
- **2609.21967** NemotronLabs VoiceChat (9-18): open FD speech-to-speech with native tool
  calling, parallel output streams for agent text and function calls. WATCHLIST.
- **2609.33443** Context Spanning (9-27): communication framework between FD speech models
  and external LLM backends. WATCHLIST (same cascade bridge, eval side unclear).

### Group B: benchmark flood continues (eval lane)

Eight new benchmarks beyond the 6 already in FACTSHEET_voice_benchmark_wave:

- **2609.31948** Duplex-MPE (9-25, 90 votes): multi-party full-duplex benchmark where the
  assistant participates in a shared conversation, not just serves one user. FILE for the
  benchmark wave factsheet (multi-party axis is new).
- **2608.25218** TurnBench (8-25): multi-domain turn-taking benchmark, take/hold/yield
  floor decisions, linguistically grounded protocol. FILE for the benchmark wave.
- **2609.17360** ECHO (9-15): matched-contrast benchmark, interruption vs backchannel
  context sensitivity, rewards context-sensitive decisions over fixed action preferences.
  WATCHLIST (eval design worth copying: matched contrasts).
- **2609.39446** DuplexAct-Bench (9-30): bilingual, six complementary interaction behaviors
  including proactive initiation. Distinct from 2610.17738 DuplexAct (Melbourne, filed 10-20).
  WATCHLIST.
- **2609.38512** VAmoS Energy (9-29): 100-call benchmark with background speech and
  impatient callers (abstract). Simulator lane, feeds trace2trajectory framing. WATCHLIST.
- **2609.35820** tau-Multilingual (9-21): extends tau-Voice to 5 more languages, 4,500
  full-duplex calls (abstract). WATCHLIST as companion of tau-Voice 2603.13686.
- **2609.24812** MSI-Bench (9-21): multi-speaker voice interaction for collaborative agents
  (meetings, households). WATCHLIST.
- **2608.26432** SpeechGym (8-26): audio-native RL gym for training voice agents, argues
  text-trained agents fail at spoken tool calling. WATCHLIST.

### Group C: decision lane deepening (our jev/CD lane)

- **2609.32536** VGBench, Do Audio LLMs Listen Before They Act (9-26, 12 votes):
  action-level ADDRESSEDNESS gate: decide whether the acoustic context (side-talk,
  self-talk, speaker-switch) warrants acting at all, 1,018-item diagnostic (abstract).
  Directly a decision-model category we do not cover in jev-mini-bench. FILE: candidate
  category for jev-mini-bench upgrade (addressedness before action).
- **2609.19596** Full-Duplex Speech Models Take the Floor When Asked, Not When Needed (9-17):
  proactive floor self-selection (correct a false claim, supply a missing word) is absent
  from current FD models. WATCHLIST (decision taxonomy expansion).
- **2609.05592** What Did I Just Say? Self-Listening for FD models (9-04, 23 votes):
  async text generation, synthesis and playback desynchronize, so the model's belief about
  its own utterance drifts from what was audible. Observability-flavored failure mode.
  WATCHLIST (CD instrument angle).
- **2610.04400** XTurnix (10-03): self-supervised turn control, two-state binary decisions
  (keep listening vs start responding; continue vs stop speaking) at scale. WATCHLIST
  (binary decision space is our minimal decision-model shape).
- **2609.11066** Less can be More (9-10): controlled ablation of acoustic, prosodic and
  semantic signals for end-of-turn detection. WATCHLIST (cites-worthy for semantic VAD).
- **2609.03321** Decoupling Turn-Taking from Semantics, NFSM (9-03): finite-state-machine
  serialized turn control on a causal tape. Nearest formal neighbor of our G=(Q,S,d)
  contract framing. WATCHLIST.

### Group D: voice security sub-lane (NEW, absent from all previous scans)

Three papers in one night form a cluster none of the 10-19/20/21 scans saw:

- **2609.09420** DuplexJail (9-08): safety alignment of FD models breaks under spoken
  interruption; fixed prompts injected through the user audio channel bypass it (abstract).
  FILE: feeds SECURITY_brief_voice_agent_authority.md next touch.
- **2609.35922** VoxParity (9-28, 3 votes): the decisions a voice SHOULD change: emergency,
  fraud and vulnerability rules where how something sounds changes the right action.
  This is the spoken-authority thesis of our security brief, independently argued. FILE.
- **2610.27210** You Are the Trigger: Speaker-Activated Backdoors (arXiv 10-19, in 48h
  window): attacker compromises a speech model at fine-tuning time, trigger is the speaker's
  voice itself, no inference-time access needed (abstract). FILE with the security brief.

### Group E: adjacent, descartar (one-line reasons, from abstracts)

2609.02812 VibeVoice-ASR-Streaming (streaming diarized ASR, NOT an adaptive-commit source,
16 votes, watch only if diarization product work starts); 2609.12623 SteerDuplex (steering
attributes, no decision content); 2609.09263 gender disentanglement in S2S; 2609.05631
TamilEOT (semantic EOT for Tamil, confirms the lane, nothing adoptable); 2610.20327
Anuvani diarization (22 languages); 2608.22071 Real-TurnTurk (Turkish corpus); 2608.27988
gaze-based multi-party turn prediction; 2609.07200 KABURI-TTS (conversational TTS data);
2609.08956 TASTE2 (text-aligned speech tokenization); 2610.11150 SmoothConv/DuplexConv
(Mandarin corpora); 2609.03992 Text-Audiobox (dubbing and dialogue synthesis); 2610.22499
JAVIS (audio-visual streaming); 2609.31511 Muslim Arabic platform (production vertical);
2610.02941 FASTDIAR (CPU streaming diarization, adjacent to browser-ML lane, revisit only
if a Space needs it). arXiv false positives: 2610.27641 BCT ("endpoint" meant endpoint
distribution of flow LMs); 2610.27200 Pareto steering ("endpoint-anchored" loss, multi-task
speech LLM steering, not lane).

## Verdict

A new cluster IS emerging, with three edges none of the previous scans had:

1. **Async delegation got industrial mass.** Realtime-Venus (190 votes), StepAudio 3
   Realtime (130), Gander (93), Qwen-Audio-Agent, NemotronLabs VoiceChat all ship
   foreground-background delegation. Our event-driven-orchestrator thesis is now the
   mainstream, which RETIRES its novelty value and raises the value of what only we have:
   the measurable runtime contract (G=(Q,S,d), conformance kit, ack latency under pending
   tools). Nobody in this wave ships a conformance kit.
2. **Benchmark flood keeps accelerating** (8 more tonight on top of the 6 in the
   benchmark-wave factsheet). The survey 2609.30798 (Evaluating Real-Time Voice Agents,
   9-25) explicitly states the literature is fragmented across three communities that
   rarely cite each other (abstract). FILE it: it is a citable premise for any future
   measurement paper, and it explains the flood: everyone is building their own eval.
3. **Voice security is a fresh sub-lane** (DuplexJail, VoxParity, Speaker-Activated
   Backdoors). Feeds the existing SECURITY_brief_voice_agent_authority.md; no new work
   spawns now (no declared consumer with demand), but annotate the brief on next touch.

**Nov paper (shelved):** stays shelved. The flood strengthens the conformance-kit premise
but also grows the related-work burden and the competition; the 2026-10-20 scope decision
(distribution over new papers) stands. The only change: if it revives, group A papers are
now the related-work spine, and 2609.30798 is the fragmentation citation.

**Fixed-chunking piece:** CLEARED to write with the existing three sources (DuplexJev
2610.02638 batched decisions, numbers verified in FACTSHEET_decision_models_voice_loop;
X2Streaming-ASR 2609.08672 from the 10-21 scan; our livekit#7994 chunk-silence bound).
No new adaptive-commit source appeared tonight (VibeVoice-ASR-Streaming is streaming
diarization, not adaptive commit latency), so no waiting is needed.
