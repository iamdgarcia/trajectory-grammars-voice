# The Forgetting Floor (REFRESH): Context Eviction Under Latency Deadlines, with Compliance-Constrained Memory

> Method note: no web-search tool available in this run; landscape synthesized from high-confidence knowledge + repo KB. All arXiv IDs must be spot-verified before citing; unverified ones marked [verify].

## Working title
"The Forgetting Floor: Deadline-Aware Context Eviction and Data-Minimized Memory in Realtime Conversational Agents" — third floor in the series: latency floor (onset), cessation floor (stop), forgetting floor (retention).

## Landscape
1. **StreamingLLM** — attention sinks + sliding window: keep everything cheap; the anti-forgetting baseline with no task- or deadline-aware eviction. arXiv:2309.17453 (ICLR 2024).
2. **H2O** — heavy-hitter token KV eviction; perplexity-only, offline, no wall-clock objective. arXiv:2306.14048 (NeurIPS 2023).
3. **SnapKV** — KV compression during prefill; attacks our prefill term directly but with fixed footprints, not deadlines. arXiv:2404.14469 (NeurIPS 2024).
4. **PagedAttention/vLLM** — KV as an accountable memory resource; context becomes budgetable state, policy still immutable-context. arXiv:2309.06180 (SOSP 2023).
5. **Quest** — query-aware page-level KV sparsity at decode; per-request salience, no cross-turn conversation policy. arXiv:2406.10735 (ICML 2024) [verify].
6. **MemGPT** — OS-style hierarchical paging for agents; capability-motivated (unlimited memory), never deadline-motivated. arXiv:2310.08560.
7. **LoCoMo** — very-long-term conversation memory benchmark; fidelity axis only, no latency axis. arXiv:2402.17753 (ACL 2024) [verify].
8. **Lost in the Middle** — position bias in long contexts: gives eviction *ordering* a measurable task target. arXiv:2307.03172 (TACL 2024).
9. **Moshi** — full-duplex native speech model with fixed-size state: the zero-memory extreme point of the design space. arXiv:2410.00037 (ICLR 2025) [verify].
10. **GDPR Art. 5(1)(c) data minimization + banking record-keeping duties** (not arXiv) — retention is *legally two-sided*: minimize what you hold, but preserve what you must evidence. [verify exact article mapping per jurisdiction]

## The gap
**Testable RQ:** For a cascade voice agent with per-turn budget B, regulatory minimization constraint m, and auditability constraint a: does a policy π: C_t → C_{t+1} exist with (i) per-step floor flat across conversation length, (ii) provable minimization invariant (bounded PII-bearing tokens in context), (iii) auditability invariant (evidentiary content durably preserved), and (iv) a critical retained-context threshold |C*|(B) below which task performance collapses — the **forgetting cliff**?

**Why unsolved:** (a) KV-eviction work optimizes perplexity against fixed footprints offline — never a millisecond deadline, never an agent task objective, never a legal constraint. (b) MemGPT-lineage memory optimizes capability; memory cost there is functionality, not wall-clock. (c) Compliance-by-design literature (GDPR minimization) is architectural principle, never a *schedulable per-turn decision* under τ_human ≈ 200 ms. Nobody connects "what the agent forgets" to latency, privacy, *and* auditability simultaneously; no benchmark measures fidelity × latency × minimization jointly.

**Sharpening vs. angle_1:** the previous brief's novelty leaned on deadline-aware eviction alone (crowded neighbourhood by 2025). The REFRESH differentiator is the **two-sided legal structure**: minimization *forces* forgetting (a regulatory feature, not an optimization), auditability *forbids deletion* — eviction must be **demotion-to-record**, never erasure. That turns the paper from "yet another eviction policy" into the first formalization of legally-constrained context management under realtime deadlines.

## Candidate contribution
1. **Forgetting Floor Theorem:** extend the ReAct floor Λ*_k with memory-decision stages; prove the naive append-only floor grows super-linearly in k (accumulated tool observations re-prefilled each step) while optimal eviction keeps it flat: Λ*_M(B) = δ_N + Σ_j (α_j|C*_j| + β_j|C*_j|) + λ_tts^irr.
2. **Forgetting Cliff Theorem:** threshold |C*|(B) at which task performance degrades discontinuously, via the budget-crossing condition with τ_human ≈ 200 ms (analogue of the silence-gap threshold logic in paper #1).
3. **Evict-to-Record framework:** eviction as a schedulable three-constraint decision (latency / minimization / auditability) with a compliance-preservation invariant — each eviction demotes content to an immutable record; forgetting becomes regulator-compatible *by construction*.
4. **Benchmark sketch (MELAT):** Spanish banking dialogues, tri-axis measurement (recall fidelity, enforced TTFT budget, in-context PII mass); extends LoCoMo with a latency axis.

## Reuse of our published results
- **Paper #1:** Λ*_SC and Λ*_k formulas reused verbatim as the substrate; the "context grows with tool observations" footnote in `06_design_levers.tex` becomes Theorem 1 — the program's own flag, finally formalized.
- **Paper #2 (cessation):** generation-interruptible vs execution-persistent separation maps directly: consolidation/eviction is an execution-persistent *background job* schedulable under the user's speech window T_speech — the amortization trick reused on memory.
- **Paper #3 (semantic VAD):** the verified turn-end signal is the natural **commit point** for memory writes; the measured cloud decision slot (p99 178–268 ms) is the measured budget for a summarize/evict decision. Veto-only role unchanged.

## Banking grounding
- **Context growth is structural:** every turn injects customer-profile data, balance/transaction tool observations, fraud flags — all PII. GDPR data minimization forbids hoarding them in-context; latency forbids re-prefilling them. Both constraints bind simultaneously in production.
- **Record retention:** banking conversations are evidentiary (disputes, fraud investigations; multi-year retention duties). The durable record ≠ model context; evict-to-record matches how banks already think about archives.
- **Fraud:** multi-session fraud investigations need cross-turn entity recall — the forgetting cliff measured on recall-critical tasks has direct fraud-desk consequences.
- **Spanish:** cliff measured on Spanish banking dialogues (our benchmark is Spanish-first; text-side decision weakness is known — cliff should be measured with ASR noise in the loop).
- **Tool backends/telemetry:** per-observation eviction interacts with the tool-hiding budget (OG3); GKE telemetry can measure real re-prefill growth across turns in the existing pipeline.

## Scores
- **Novelty: 4** — deadline-aware eviction alone is crowded; legally two-sided evict-to-record under realtime deadlines is unclaimed.
- **Fit: 5** — direct theorem-level extension of all three published floors; reuses formulas, amortization trick, and measured VAD slot.
- **Banking: 5** — data minimization + record retention + fraud recall is the exact compliance core of conversational banking.
- **Feasibility: 4** — theory + PoC on existing GKE pipeline is cheap; MELAT benchmark needs dialogue collection.
- **Risk: 2** — cliff may be gradual (not discontinuous) at realistic context sizes; mitigation: report threshold as crossing condition, not discontinuity.

## Verdict
**Pursue now.** Strongest reuse chain of any remaining angle (all three published results feed it), the compliance twist escapes the crowded KV-eviction neighbourhood, and no gaps.md conflict exists. Seed order: theorem 1 from existing LaTeX formulas first, cliff second, benchmark last.
