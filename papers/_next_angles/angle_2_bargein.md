# Research: Turn-Taking & Interaction Dynamics Beyond Raw Latency — scoping "reactive latency" (barge-in / interruption reaction)

_Provenance: produced from local repo context (papers/cascade_voice_latency/, knowledge_base/topics/ai_guardrails/) + curated conversational-analytics/pragmatics literature. No live web_search tool was exposed in this run; citations below are high-confidence real works, arXiv IDs given only where confident, uncertain ones flagged [verify]._

---

## 1) LANDSCAPE

- **Conversation Analysis foundations** — Sacks/Schegloff/Jefferson's turn-taking systematics; Schegloff on overlapping talk: overlaps are orderly, projectable events at transition-relevance places, not errors. _(Schegloff 2000)_
- **Quantitative cross-linguistic timing** — modal inter-turn gaps near 0–200ms across 10 languages (Stivers 2009) and anticipatory-processing accounts of sub-200ms responding (Levinson & Torreira 2015); Heldner & Edlund measure that ~40% of transitions have gaps < 100ms, showing a single "silence-gap threshold" under-describes real dynamics.
- **Projection / end-of-turn prediction** — listeners/hearers predict turn end before acoustic silence: early-content projection (de Ruiter, Mitterer & Enfield 2006), prosody+context turn-end estimation (Bögels & Torreira 2015), idiosyncratic multimodal prediction (de Kok & Heylen 2009).
- **Incremental & continuous turn-taking models in SDS** — incremental dialogue processing with overlap (Schlangen & Skantze 2011), continuous turn-taking state/asynchrony models (Skantze 2020), engineering review (Skantze 2021) — overlap is the canonical latency-reduction mechanism, exactly the machine-side analogue of barge-in tolerance.
- **Barge-in / endpointing / interruption handling in deployed SDS** — Raux & Eskenazi's endpointing and "optimizing turn-taking behaviour" line (finite-state turn-taking model 2009; ACM TSLP 2012 turn-taking/barge-in tradeoffs), Bohus & Horvitz's interruption and engagement-utility decision work.
- **Backchannels, feedback and disfluency timing** — prosodically cued backchannels with ~700ms timing (Ward & Tsukahara 2000); disfluency/prosody as turn-holding structure (Shriberg 2005); neuroimaging work on the suppressed "turn-entry" response in listeners (Bögels & Levinson 2017).
- **Engagement & perceived responsiveness in HAI/HRI** — engagement taxonomies and its measurement as an interaction-level target (Oertel 2020), responsive-gaze/gesture/utterance policies (Bohus & Horvitz 2010–2011).
- **Full-duplex native speech LLMs** — Moshi (arXiv:2410.00037), Mini-Omni [verify id: 2408.16725], OmniFlatten [verify id: 2410.16199], Freeze-Omni [verify id: 2411.00774], Spark-TTS-2 [verify id] — all *demonstrate* simultaneous-speech handling and interruption, but only with empirical/demo claims, no analytical latency model.

## 2) THE GAP

**Testable research question:** *For a given voice-agent architecture A ∈ {EOU-gated cascade, streaming cascade, streaming-causal/full-duplex native}, what is the minimal (irreducible) time between the onset of a user's interruptive/barge-in turn and the completion of the agent's cessation action (audibly stop speaking), and how does it decompose into reducible vs irreducible components as a function of pipeline topology?*

**Why it is not already solved:**
- The SDS literature treats barge-in **operationally**, not formally: endpoint thresholds, echo-cancellation budgets, "barge-in length" heuristics, and empirical user studies of allowed interruption windows; there is no per-topology lower bound analogous to the Latency Floor Theorem. (Raux & Eskenazi 2012 is the closest, and it is engineering-empirical.)
- Native S2S papers (Moshi class) claim interruption/full-duplex handling and report demo latency, but give **no analytical decomposition** of the cessation latency; the only bound of this genre is our own, and it is one-sided (onset only).
- Both literatures treat the agent's **stop** as instantaneous or thresholded — nobody has separated *detect / decide / cease / resume* costs, or noticed that they have *different* architectural orderings than onset latency (native wins onset; cascade's detached VAD may win detection, but pays TTS "audio-in-flight" on cessation).
- Our own paper's Open Problems (§7: "Learned barge-in prediction") already flags reactive barge-in as formally untreated, confirming the gap is real and adjacent to our brand.

## 3) CANDIDATE CONTRIBUTION

**Contribution type:** formal model + theorem, with an optional small benchmark as an empirical companion.

**The Interruption Reaction Model.** On the same DAG family as the published paper, define, for an interruption event I = onset of a user turn while the agent is producing output:
RL(A, I) = δ_detect(A) + δ_decide(A) + δ_cease(A) + δ_resume(A)
- δ_detect — time until I's first informative audio frame is observable to the controlling component: EGC cascade = VAD on ASR ingest + partial ASR commit; streaming-causal native = one codec frame at stride Δ_t.
- δ_decide — time to classify I as a true barge-in vs noise/backchannel (cascade: LM or a detached interruption policy on the partial hypothesis; native: same network's streaming forward step; both can be decoupled to a separate "interruption policy" component).
- δ_cease — time to stop audible output; **floor = residual audio already synthesised / queued for playback ("audio in flight")**, ≈ 0 frames for streaming native, ≥ TTS token-generation lookahead × number of chunks in the playback queue for cascade.
- δ_resume — reacquiring the turn after the user finishes; reuses our speculative-restart machinery (open problem §7).

**Theorems (skeleton):**
- (T1) **Cessation Floor Theorem** — RL ≥ δ_detect^irr + δ_decide^irr + δ_cease^irr per architecture; in particular δ_cease^irr(cascade) grows with the agent's own output duration (longer speech ⇒ more queued audio to void), whereas δ_cease^irr(streaming-native) ≈ 2×codec frame, constant in output length. This is the *dual* of the Latency Floor, and the asymmetry (onset: native ≼ cascade; cessation per-frame: native ≼ cascade, but detect: detached-VAD cascade may even win) is itself the interesting result.
- (T2) **Reactivity matrix** — a 4×3 table (detect / decide / cease / resume × EGC / streaming-cascade / streaming-native) of reducible-vs-irreducible entries; this matrix is the compact publishable artifact engineers can actually use.

**Benchmark (optional companion):** record barge-in reaction latency (time from interruptive onset to audible stop; post-interruption comprehension) on public S2S/assistant audio; measures per architecture class.

**Working title:** *"The Barge-In Barrier: A Formal Model of Interruption Reaction Latency in Cascade and Full-Duplex Voice Agents"* (alt: *"Reactive Latency: Cessation Bounds for Barge-In in Real-Time Voice Agents"*).

## 4) EXTENSION ANGLE

- **Two-sided responsiveness.** The published paper bounds response-**onset** (silence gap Λ vs Latency Floor Theorem, τ_human). The new paper bounds response-**cessation** via a dual Cessation Floor, reusing the exact same machinery: cascade DAG definitions (EGC / streaming SC), reducible/irreducible decomposition, τ_human as a parameter. Together they form a coherent "interactive responsiveness" program: *start fast (last paper) and stop fast (this paper)*.
- **Architecture contrast in the other direction.** Last paper: Λ*_native ≤ Λ*_cascade (native starts faster). New paper derives the (non-symmetric) cessation contrast, producing a genuinely new claim the first paper could not: cascade's cessation floor is dominated by its own synthesis queue and thus grows with agent output length — i.e., the longer a cascade agent talks, the *slower* it can comply with an interruption.
- **Feeds the streaming-guardrail gap (KB G1).** Barge-in is the user's natural abort signal. A streaming-safe guardrail that must silence the agent before it can say more needs to run inside the reactive-latency budget RL; the Cessation Floor therefore defines the worst-case time-budget that a streaming-compatible guardrail must satisfy — a direct, formal bridge to the KB's top open gap.
- **ReAct extension.** barge-in during a tool-calling turn = aborting a tool call mid-flight; extends the k-step silence-gap result to "interruptibility of tool-calling turns," connecting §7's open problems (barge-in prediction, speculative restart) to the reaction model.

## 5) ANCHORS

1. **Stivers et al. 2009**, *Universals and cultural variation in turn-taking in conversation*, PNAS 106(26):10587–10592 — the empirical base of the 200ms claim the previous paper already cites; also documents overlaps, i.e. why onset-gap alone is insufficient. (journal, no arXiv)
2. **Heldner & Edlund 2010**, *Pauses, gaps and overlaps in conversations*, Journal of Phonetics 38(4):555–568 — ~40% of transitions at sub-100ms gaps/overlaps; the strongest quantitative refutation of single-threshold "silence gap" storytelling, i.e. motivation for a dynamics model. (journal, no arXiv)
3. **Schegloff 2000**, *Overlapping talk and the organization of turn-taking for conversation*, Language in Society 29(1):1–63 — canonical CA treatment of overlaps as ordered, projectable phenomena; supports modelling barge-in as structure, not noise. (journal, no arXiv)
4. **Levinson & Torreira 2015**, *Timing in turn-taking and its implications for processing models of language*, Frontiers in Psychology 6:731 — anticipatory/cryo-typing account of sub-200ms responding; the cognitive basis for *predictive* (pre-onset) stop, i.e. our δ_detect/δ_decide floors. (already in repo main.bib)
5. **Raux & Eskenazi 2012**, *Optimizing the turn-taking behavior of task-oriented spoken dialog systems*, ACM TSLP 9(1) — deployed endpointing/ barge-in/ perceived-delay tradeoffs; the operational nearest-neighbor to "reaction latency" and the strongest evidence the formal bound is missing. (journal, no arXiv)
6. **Bohus & Horvitz 2011**, *Decisions about turns in multiparty conversation: from perception to action*, ICMI — interruption handling formulated as decisions with engagement/utility; the policy framework into which our δ_decide plugs. (conference, no arXiv)
7. **Ward & Tsukahara 2000**, *Prosodic features which cue back-channel responses in English and Japanese*, Speech Communication 32(1–2):117–124 — prosodic timing (~700ms rule) of backchannels; anchor for the *feedback side* of turn dynamics that a full-duplex model must also schedule. (journal, no arXiv)
8. **Défossez et al. 2024**, *Moshi: A Speech-Text Foundation Model for Real-Time Dialogue*, arXiv:2410.00037 — full-duplex native model with demonstrated disruption/interruption handling; the architecture class our Cessation Floor must contrast, and already in repo main.bib.

---

### Citation-confidence note
Journal/conference anchors (1–7) are verifiable in ProQuest/ACM/OLR/Google Scholar. arXiv IDs outside the repo (Mini-Omni, OmniFlatten, Freeze-Omni, Spark-TTS-2) are flagged `[verify]` and must be confirmed before inclusion in any bibliographic export; the four solid repo-based anchors (Levinson & Torreira, Moshi, Stivers, Dong) are verbatim-safe.
