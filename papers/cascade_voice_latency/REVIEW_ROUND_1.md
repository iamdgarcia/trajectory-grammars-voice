# Peer Review — Round 1
**Paper:** The Latency Floor of Cascade Voice Agents: Formal Bounds and Design Levers
**Author:** Daniel García Peña
**Date:** 2026-07-19

---

## Reviewer Scores

| Reviewer | Role | Score |
|----------|------|-------|
| Reviewer 1 | Methodology (formal correctness) | 5 / 10 |
| Reviewer 2 | Domain (voice agent latency, SDS) | 4 / 10 |
| Reviewer 3 | Writing and presentation | 7 / 10 |
| Reviewer 4 | Related work and prior art | 4 / 10 |

---

## Chief Editor Decision: **Major Revision**

The paper addresses a genuine and practically important problem. The conceptual contributions — latency decomposition, the floor theorem, the ReAct extension, and the design lever taxonomy — are valuable and original in framing. No reviewer found circular reasoning or fatal arithmetic errors. The k=2 worked example (1350ms) is arithmetically correct.

However, the paper has blocking deficiencies in four areas: (1) the formal apparatus has gaps that prevent the theorems from being rigorously valid as stated; (2) the "first formal analysis" novelty claim cannot be sustained against fifteen-plus years of incremental spoken dialogue system research that addresses the same structural latency problem; (3) two figures contain errors that contradict the body text; and (4) Table 1 numeric claims are asserted without citations. These deficiencies require major revision but do not warrant rejection — all are addressable without changing the paper's conceptual contribution.

---

## Consolidated Mandatory Revision List

The following 13 items block acceptance. Each must be addressed before resubmission.

### M1 — Fix Figure 2 TikZ band placement and caption (R3-M1, R2-1)

**File:** `figures/fig_perceptual_threshold.tex`

The native voice band is drawn from x=0 to x=320 (`\fill[green!20] (0,2.1) rectangle (320,2.6)`). This implies native voice can have zero latency, which contradicts the stated 320–500 ms range and the body text of §4. The caption also states native voice "currently falls partly within" the CCC zone (≤200 ms), which is false given 320–500 ms reported latencies.

**Required:** Shift the band to x=320–500. Correct the caption to accurately state that native voice currently falls outside the strict 200 ms CCC zone. This connects directly to M2.

### M2 — Resolve the native voice / τ_human contradiction (R2-1, R3-M1)

**Sections:** §2.3, §4.2, §4.3, §9

The paper defines CCC as Λ ≤ τ_human = 200 ms. It then reports that GPT-4o Realtime achieves "silence gaps in the 320–500 ms range." This means native voice itself fails CCC by the paper's own definition. The impossibility result (Corollary 1) and the framing of native voice as the perceptually competitive baseline both rely on native voice satisfying or approaching CCC — which the paper's own numbers contradict.

**Required:** Either (a) reframe τ_human as a soft perceptual distribution rather than a hard threshold, citing HCI literature on human-agent latency tolerance (distinct from human-human norms); or (b) separate the "perceptual improvement" criterion from the strict CCC definition. The current framing makes the impossibility result appear to apply when native voice also fails the criterion.

### M3 — Fix Figure 4 internal contradiction for Streaming TTS (R3-M2)

**File:** `figures/fig_design_levers.tex`

The Streaming TTS row states "Component addressed: Reducible λ_tts^r" but "Reduces Λ*?: Yes." A strategy that addresses only the reducible component cannot reduce Λ* (which is the sum of irreducible components). The body text of §6.1 correctly explains that streaming TTS reduces λ_tts^{irr} by changing the input dependency — this contradicts the table cell.

**Required:** Change the "Component addressed" cell for Streaming TTS to "Irreducible λ_tts^{irr} (topology change)" or equivalent. This must match §6.1's explanation.

### M4 — Formalize Definition 3 (irreducible latency) as an infimum (R1)

**Section:** §3 (Definition 3)

As written, "a lower bound on λ_i that holds for all implementations" is tautological — any non-negative value ≤ λ_i satisfies it, including 0. This makes Theorem 1 vacuous. The definition must specify that λ_i^{irr} is the *infimum* of λ_i over all valid implementations of stage s_i.

**Required:** Replace with: "λ_i^{irr} := inf_{ℐ ∈ valid(s_i)} λ_i^ℐ(x_i)" (or equivalent). Define what constitutes a "valid implementation" (the set ℐ over which the infimum is taken).

### M5 — Add missing theorem premises to Theorem 1 (R1)

**Section:** §4 (Theorem 1)

Theorem 1 quantifies over "all implementations" without defining what an implementation is. It also requires sequential stage execution (no overlap) and input-independent latencies — both are implicit but never stated.

**Required:** Add to the theorem statement: (a) a definition of "implementation" specifying what can vary (model weights, hardware, inference engine) and what cannot (pipeline topology, stage boundary definitions, sequential execution order); (b) the premise that stages execute strictly sequentially — no stage begins before its predecessor completes full output; (c) the input-independence assumption (λ_i does not depend on the specific input x_i, only on stage parameters). These assumptions currently appear only in §8 (Limitations); they must appear as formal premises.

### M6 — Fix Theorem 2 irreducible floor formula (R1, R2)

**Section:** §5 (Theorem 2)

The total gap formula is Λ_k = λ_asr + k·λ_lm + (k−1)·λ_tool + λ_tts, but the irreducible floor is stated as Λ_k* = λ_asr^{irr} + k·λ_lm^{irr} + λ_tts^{irr}. The (k−1)·λ_tool^{irr} term is silently dropped. This is mathematically incorrect for the general case — for remote API tools, λ_tool^{irr} is non-negligible.

**Required:** Either (a) state the full general formula Λ_k* = λ_asr^{irr} + k·λ_lm^{irr} + (k−1)·λ_tool^{irr} + λ_tts^{irr} with a note on when λ_tool^{irr} ≈ 0 is justified (in-process local tools only); or (b) add as an explicit theorem premise: "assuming in-process tool calls with λ_tool^{irr} = 0."

### M7 — Fix Theorem 2 notation: λ_lm overloaded (R1)

**Section:** §5 (Theorem 2)

λ_lm means total LM latency in §3/Theorem 1 (prefill + full decode). In Theorem 2, intermediate LM steps care only about TTFT (time to first structured output token). The final step LM_k may require longer decode if TTS must wait for sufficient tokens. Using the same symbol for both is an inconsistency that makes the theorem formula ambiguous.

**Required:** Use λ_lm^{TTFT} for intermediate steps and either λ_lm for the final step or a note that the formulation assumes streaming TTS can begin on the first token. Also state explicitly: "assuming equal latency across all k LM inference steps" (in practice, later steps have longer context and higher prefill cost).

### M8 — Reframe ASR irreducibility as a model axiom (R1)

**Section:** §3 (§3.2 or equivalent)

The claim "no transcription can begin before the detector confirms the user has stopped speaking" is presented as a universal physical necessity. Incremental/streaming ASR systems begin partial decoding before EOU confirmation. This is a design constraint of the specific pipeline model, not an inherent constraint on ASR.

**Required:** Reframe as: "We restrict attention to ASR systems that begin decoding only after EOU confirmation (non-incremental pipeline model). Incremental ASR variants that overlap transcription with speech input are discussed as a design lever in §6."

### M9 — Hedge the "first formal analysis" novelty claim (R4)

**Sections:** §1, §9

The paper states in §1 that "no theoretical framework exists for determining when a cascade architecture can achieve perceptual equivalence with a native voice model" and in §9 that this is "the first formal analysis of the structural latency constraints of cascade voice agent architectures." Schlangen & Skantze's formal module pipeline model (EACL 2011) and related SDS incremental processing literature address the temporal dependency structure of cascade spoken dialogue pipelines.

**Required:** Replace the unqualified "first formal analysis" claim with a scoped claim. A defensible formulation: "We provide the first formal characterisation of the irreducible latency floor as a function of pipeline topology, and establish formal conditions under which cascade architectures can achieve perceptual equivalence with native voice models and with multi-step tool-using ReAct agents." Add a sentence distinguishing this from the SDS incremental processing literature (which motivates streaming as a solution but does not derive the floor bound or connect it to the CCC condition).

### M10 — Add SDS-related work subsection to §2 (R2, R4)

**Section:** §2

The spoken dialogue systems (SDS) and incremental processing community is entirely absent from the paper. This community has addressed the cascade latency problem since the early 2000s. The absence makes the paper appear to operate in a vacuum on a well-studied problem.

**Required:** Add a subsection §2.X "Spoken Dialogue Systems and Incremental Processing" covering: (a) Schlangen & Skantze (2011), which formalizes incremental module pipeline structure and motivates streaming to reduce sequential latency; (b) Skantze (2021) survey on turn-taking in SDS and human-robot interaction; (c) Raux & Eskenazi (2008) on optimizing EOU thresholds in deployed voice systems; (d) the distinction between the SDS literature's engineering solutions and this paper's formal floor result and CCC connection. Minimum additions: Schlangen & Skantze 2011, Skantze 2021, Raux & Eskenazi 2008.

### M11 — Cite sources for all Table 1 numeric values (R2)

**Section:** §3 (Table 1)

The caption states values are "based on published and empirically observed figures" but provides no citations in the table rows. The LM TTFT claim of 100 ms for GPT-4o-class at 8k context is particularly in need of substantiation (community benchmarks show 200–800ms+ depending on load). All six numeric cells (ASR: 200ms irr, 150ms red; LM: 100ms irr, 250ms red; TTS: 80ms irr, 120ms red) require explicit citations or must be explicitly labelled as "representative estimates" with acknowledged uncertainty.

**Required:** Add citation pointers to each row, or add a footnote: "Values are representative estimates; see [cited sources] for empirical ranges." The LM 100ms figure requires either a citation to a specific serving benchmark or revision to a more defensible value with wider uncertainty.

### M12 — Correct factual claim about native voice and tool use (R2)

**Sections:** §2, §4

The paper states that native voice models "do not natively support tool use through standard agent frameworks." This is factually incorrect — the OpenAI Realtime API supports function calling in native audio mode without any application-managed ASR/TTS conversion.

**Required:** Correct to: native voice models support function calling, but tool-call turns still incur latency that partially reintroduces the sequential execution penalty. The argument about tool use worsening latency stands; only the categorical claim of non-support is wrong.

### M13 — Replace Silero VAD citation with peer-reviewed literature (R4)

**Bibliography:** `main.bib` entry `silero2021vad`

The current citation is a GitHub repository. VAD and EOU detection claims in §2 and §3 should cite peer-reviewed work.

**Required:** Replace or supplement with peer-reviewed VAD/EOU literature. Minimum: cite Bredin et al. (Pyannote series) or equivalent neural EOU detection work for the EOU detection claims in §3.

---

## Optional Suggestions (Non-Blocking)

These were flagged by reviewers as improvements but do not block acceptance.

**From R1 (Methodology):**
- O1. Elevate the DAG critical-path remark (after Theorem 1) to a formal proposition with a brief proof.
- O2. Add a proposition showing that streaming TTS lowers λ_tts^{irr} by changing the input-output contract.
- O3. Revise the parallel tool execution formula (§6.5) to cover partial parallelism via tool dependency graph topology.
- O4. Derive the inline Λ_k* = 380 + (k−1)·λ_lm^{irr} formula explicitly from Theorem 2.

**From R2 (Domain):**
- O5. Add streaming/incremental ASR as a design lever in §6 with analysis of whether it reduces Λ* or only Λ^r.
- O6. Add response caching as a lever in §6 (eliminates λ_lm for matched queries).
- O7. State more directly that speculative decoding provides negligible TTFT benefit for voice-latency-critical systems.
- O8. Correct the characterization of Stivers et al. (2009): they establish cross-linguistic universality of rapid turn-taking, not a specific 200ms boundary.
- O9. Add spoken language model foundation papers (AudioPaLM, GSLM) to §2's native voice background.
- O10. Distinguish Whisper (batch/offline) from streaming ASR in the Table 1 label and surrounding text.

**From R3 (Writing):**
- O11. Unify "streaming synthesis" (abstract) to "streaming TTS" (used everywhere else).
- O12. Remove or condense the roadmap paragraph in §1 (redundant with the itemized contribution list).
- O13. Replace "decoding" in §2.1 ASR context with "inference" or "transcription" to avoid confusion with LM decoding.
- O14. Note that the LM prefill O(n²) complexity claim applies to naive attention; FlashAttention reduces the constant but not the asymptotic prefill growth.
- O15. Consider swapping §7 (Open Problems) and §8 (Discussion) to standard ordering: Discussion before Future Work.

**From R4 (Related Work):**
- O16. Add a sentence explaining why "competitiveness" was chosen as the term in the CCC.
- O17. Cite HCI work on human-agent voice latency tolerance (e.g., Hone & Graham 2000; Yankelovich et al. 1995) in the Limitations subsection.
- O18. Expand bibliography to 30+ entries (currently 14).

---

## Summary for Author

The paper's core conceptual contributions are valid: the latency floor framework, the formal connection to human perceptual thresholds, and the design lever taxonomy are genuinely useful and clearly presented. The writing quality is high. The path to acceptance requires: fixing two figure errors (M1, M3), resolving the native-voice/threshold contradiction (M2), tightening the formal apparatus (M4–M8), engaging the incremental SDS literature (M9–M10), and providing citations for empirical claims (M11–M13). These are substantial but tractable revisions. The paper should not require a third review round if these items are addressed thoroughly.

**Estimated revision scope:** Major — approximately 2–3 days of focused work for an experienced author.
