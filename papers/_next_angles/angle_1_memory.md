# Research: Realtime Agentic Memory — Context & Memory Management Under Latency Deadlines

> Scope: how streaming/voice agents manage context and memory when every retokenization, retained token, and memory-write costs wall-clock time against a latency budget. Central hypothesis examined: *"what the agent forgets (and when)" is a latency lever nobody has formalized* — **confirmed, with a clean thesis and a clear publishable gap.**
>
> Method note: no `web_search` tool was available in this run, so the landscape and anchors below are synthesized from domain knowledge cross-checked against the repo (`cascade_voice_latency/main.bib`, its `sections/`, and `knowledge_base/`). All arXiv IDs must be spot-verified before final submission (flagged in risk list).

---

## 1) LANDSCAPE
1. **Streaming / infinite-context serving** — attention-sink + sliding-window decoding that keeps *everything* in context (no forgetting) at flat memory cost. ([Xiao 2309.17453](https://arxiv.org/abs/2309.17453), [Han 2401.02669](https://arxiv.org/abs/2401.02669))
2. **KV-cache compression & eviction** — token-importance-based eviction (heavy hitters / snapshot / persistence heuristics) trading perplexity against fixed KV *footprint*, evaluated offline, not against wall-clock deadlines or agent-task objectives. ([Zhang 2306.14048](https://arxiv.org/abs/2306.14048), [Liu 2405.08518](https://arxiv.org/abs/2405.08518), [Li 2404.14469](https://arxiv.org/abs/2404.14469), [Ge 2404.08454](https://arxiv.org/abs/2404.08454))
3. **KV/prefix caching in serving systems** — PagedAttention, RadixAttention, Prompt Cache make KV reuse and prefill-sharing first-class latency levers for interactive agents, but treat context as immutable. ([Kwon 2309.06180](https://arxiv.org/abs/2309.06180), [Zheng 2312.07104](https://arxiv.org/abs/2312.07104), [Gim 2311.04934](https://arxiv.org/abs/2311.04934))
4. **Prompt/context compression** — token-level and soft-prompt-level compression (incl. trainable memory tokens) explicitly sold on latency/throughput, but applied greedily per request, no deadline-aware policy. ([Jiang 2310.05736](https://arxiv.org/abs/2310.05736), [Jiang 2403.12968](https://arxiv.org/abs/2403.12968), [Chevalier 2305.14788](https://arxiv.org/abs/2305.14788))
5. **Hierarchical / external agent memory** — MemGPT paging, Generative Agents memory streams, MemoryBank long-term stores; motivated by context-*capacity* limits and capability, not by deadline-constrained wall-clock cost. ([Packer 2310.08560](https://arxiv.org/abs/2310.08560), [Park 2304.03442](https://arxiv.org/abs/2304.03442), [Zhong 2305.10250](https://arxiv.org/abs/2305.10250))
6. **Long-context position bias & evaluation** — Lost-in-the-Middle position sensitivity and LongBench-style long-context benchmarks show *where/how* memory is used drives real task performance, giving eviction ordering a measurable target. ([Liu 2307.03172](https://arxiv.org/abs/2307.03172), [Bai 2308.14508](https://arxiv.org/abs/2308.14508))
7. **Incremental/voice dialogue systems + native voice models** — the only formally-incremental framework for spoken context is pre-LLM (grounded conveniently in our own paper's chains); current voice agents treat context as a fixed prefill blob. ([Schlangen 2011](https://aclanthology.org/E11-1015), [Skantze 2021](https://www.sciencedirect.com/science/article/pii/S088523082030081X), [Défossez 2410.00037](https://arxiv.org/abs/2410.00037))
8. **Memory-safety: agent prompt-injection / knowledge-poisoning + our streaming-guardrail gap** — retained/evicted memory is an attack surface; no work yet ties *what an agent forgets* to safety under streaming deadlines. ([Liu 2306.05499](https://arxiv.org/abs/2306.05499), [Zou 2402.07867](https://arxiv.org/abs/2402.07867); our `knowledge_base/topics/ai_guardrails/gaps.md` **G1**)

## 2) THE GAP
**Confirmed single most promising unfilled gap — stated as a testable research question:**

> **RQ:** For a cascade voice agent with per-turn latency budget B, is there a closed-form, deadline-aware policy for per-step context decision |C_j| (retain / compress / evict) such that time-to-first-token stays **flat** across conversation length — and is there a *critical retained-context length* |C*|(B) below which expected task performance collapses discontinuously (a "forgetting cliff")?

**Why it is NOT already solved:**
- Cluster 1 stores *all* tokens (explicitly anti-forgetting, e.g. attention sinks keep history); Cluster 2 evicts by attention salience against a fixed KV *footprint*, optimizing perplexity offline — nobody optimizes against a *millisecond deadline* or an *agent task objective*.
- Cluster 5 (MemGPT et al.) optimizes *capability* (unlimited long-term memory) — memory there costs functionality, not wall-clock; paging policy is not deadline-aware.
- Cluster 7 (voice agents, incl. our own published floor) treats prefill context |C| as an exogenous constant. Our own paper only *flags* the coupling in passing (`05_react_extension.tex`: "later steps incur higher prefill cost as context grows with tool observations") — it is never formalized or optimized.
- **Nobody* has closed the loop that retained-token marginal value is a *deadline-dependent* quantity**, and no benchmark jointly measures memory-fidelity vs latency-budget for interactive agents. The verdict on the hypothesis: *"what the agent forgets (and when)" is a latency lever that is real and unformalized.*

## 3) CANDIDATE CONTRIBUTION
**A formal "forgetting-under-deadline" model layered onto our pipeline-DAG + a lever taxonomy + a benchmark protocol.**

Working title (parallels prior paper's branding):
> **"The Forgetting Floor: Context Eviction Under Latency Deadlines in Realtime Agents"**

Concrete deliverables:
1. **Model:** extend the cascade/ReAct DAG with memory-decision stages M_j (retain/compress/evict) and a *memory cost decomposition* into reducible (retokenization α·|C| when KV-splice is impossible; ASR-revision KV invalidation — already in `06_design_levers.tex`) vs irreducible (per-token decode + re-decode of retained tokens β·|C|). Context length |C_j| becomes a first-class decision variable.
2. **Theorems:** (i) *Forgetting Floor Theorem* — under budget B, the optimal retained context |C*_j| and the resulting floor Λ*_M = δ_N + Σ_j α_j|C*_j| + Σ_j β_j|C*_j| + λ_tts^irr; (ii) *Forgetting Cliff Theorem* — a discontinuity/threshold result: ∃ |C*| s.t. expected task performance degrades non-linearly below it, tying context size to the human turn-taking threshold τ_human≈200ms via the budget crossing condition (this is a direct analogue of the paper's silence-gap threshold logic).
3. **Taxonomy:** 6-8 *memory levers* (in-context length control; salience-based KV eviction; hierarchical paging; summarization/compression; retrieval-windowed context; compressed-state architectures like selective-state RNNs; commit-scheduling into user speech time) — each classified by whether it reduces the floor structurally or masks it.
4. **Benchmark (sketch):** a "Memory-Fidelity vs Latency (MELAT)" protocol — conversational task suite (tool-use continuation, entity recall, safety-relevant recency) measuring forgetting-inflicted error as a function of enforced budget; no existing benchmark does this jointly.

## 4) EXTENSION ANGLE
Reuses both prior paper results and the streaming-guardrail gap, visibly: 
1. **Direct floor reuse:** take Λ*_SC = δ_N + α·|C_residual| + λ_lm^decode,irr + λ_tts^irr (from `06_design_levers.tex`) and the k-step ReAct floor Λ*_k = λ_asr^irr + k·λ_lm^irr + (k-1)·λ_tool^irr + λ_tts^irr (from `05_react_extension.tex`); the new paper proves the **Compounded Memory Floor**: naive append-only context makes the prefill term grow super-linearly in k (each ReAct step re-prefills accumulated observations), whereas optimal forgetting keeps the per-step floor *flat* — turning our own footnote into a theorem.
2. **New 7th design lever:** *memory-commit scheduling* — compress/retokenize/evict during the user's own speech window T_speech (the same amortization trick that made streaming-ASR incremental prefill structural), so memory writes become "free" wall-clock time. Directly extends the 6-lever taxonomy.
3. **Guardrail bridge:** eviction policy must be *streaming-safety-cognizant* (never evict safety-relevant context; certify each eviction/retention decision chunk-wise, G1-style prefix safety) — seeds our open `ai_guardrails` gap so the memory paper visibly prefaces the guardrails paper.

## 5) ANCHORS (must-cite; verify IDs before submission)
1. **StreamingLLM** (Xiao 2309.17453) — the anti-forgetting baseline (keeps full history via attention sinks); the explicit contrast for "keep everything is not free". 
2. **H2O** (Zhang 2306.14048) — first principled token-importance KV eviction; our eviction-priority baseline, but no deadline/budget and perplexity-only eval.
3. **SnapKV** (Li 2404.14469) — compresses KV *during prefill*, i.e. attacks exactly our floor term α·|C_residual|; strongest serving-level hook for the streaming-cascade case.
4. **PagedAttention/vLLM** (Kwon 2309.06180) — establishes KV-as-accountable-memory resource accounting, the substrate any latency-aware memory policy must obey.
5. **MemGPT** (Packer 2310.08560) — hierarchical paging for agents; proves the "OS-like memory" analogy works but with no wall-clock policy (capability-not-latency motivation).
6. **LLMLingua-2** (Jiang 2403.12968; sibling 2310.05736) — prompt compression explicitly aimed at latency; shows the cost link exists but is done ad hoc, no deadline optimization.
7. **Lost in the Middle** (Liu 2307.03172) — position/ordering effects give eviction ordering an empirical target; supports the "where memory sits matters as much as what's kept" claim.
8. **Incremental dialogue model** (Schlangen & Skantze 2011, EACL; see `main.bib`) — the only formal incremental-processing machinery into which a deadline-aware context policy can slot; already in our bibliography, easy cite.
*Self-anchor:* our published cascade floor / ReAct extension sections (`papers/cascade_voice_latency/sections/05_react_extension.tex`, `06_design_levers.tex`).

---

## GAPS OF THIS BRIEF / IMPORTANT VERIFICATION NOTES
- arXiv IDs above are from recall; **verify each on arxiv.org** (esp. 2404.08454, 2404.14469, 2401.02669, 2405.08518, 2305.10250) before citing.
- Empirical numbers follow (no runs done this session): budget-to-threshold quantification (|C*| vs τ_human), the "flat TTFT" claim, and the cliff discontinuity need one measurement campaign — ideal as the benchmark section's evidence.
- LoCoMo (MemGPT long-context-conversation benchmark, ~2406.17446) not yet pulled to the KB — candidate new KB entry.

## Related local files (context anchors)
- `papers/cascade_voice_latency/sections/05_react_extension.tex` — k-step Λ_k formula + the "context grows with tool observations" remark this paper formalizes.
- `papers/cascade_voice_latency/sections/06_design_levers.tex` — streaming cascade floor Λ*_SC, KV-invalidation cost, 6-lever taxonomy.
- `knowledge_base/topics/ai_guardrails/gaps.md` — G1 streaming guardrails (bridge target).
- `knowledge_base/INDEX.md` — KB layout; ai_guardrails holds 92 entries (memory not yet a topic).
