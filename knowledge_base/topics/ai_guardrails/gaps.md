# AI Guardrails — Research Gaps

_Aggregated from paper entries with gap_score >= 4 and conceptual: true._
_Last updated: 2026-06-15_

## Gap G1: Real-Time Streaming-Compatible Guardrails (gap_score: 5)

**Problem:** All production guardrail classifiers (Llama Guard, AEGIS, ShieldLM) require a complete response before classification. Token-streaming deployments need per-token or per-chunk safety decisions.

**Evidence:** `inan2023llama` (LLM classifier latency), `robey2023smoothllm` (3x overhead), `pi2024mllm` (two-stage pipeline), `dong2024building` (explicitly flags this gap).

**Candidate contribution:** Theoretical framework for prefix-safe generation — formal conditions under which a partial token sequence can be certified safe without inspecting future tokens.

---

## Gap G2: Multimodal Cross-Modal Safety Generalisation (gap_score: 4-5)

**Problem:** Text-only safety training does not generalise to image-embedded attacks. No unified guardrail architecture covers text + image + audio + video.

**Evidence:** `gong2023figstep`, `luo2024jailbreakv`, `liu2024mmsafetybench`, `wang2024adashield`.

**Candidate contribution:** Taxonomy of cross-modal attack surfaces and a theoretical model of how safety signals should be fused across modalities.

---

## Gap G3: Formal Safety Certification at Linear Cost (gap_score: 5)

**Problem:** The only certified defence (`kumar2023certifying`) has O(n^2) cost. No streaming-compatible certified guardrail exists.

**Evidence:** `kumar2023certifying`, `varshney2023art`.

**Candidate contribution:** Approximate certification framework with O(n) amortised cost using sliding-window safety invariants.

---

## Gap G4: Evaluation Standardisation (gap_score: 4)

**Problem:** Attack success rates are not comparable across papers due to inconsistent prompts, thresholds, and models.

**Evidence:** `mazeika2024harmbench`, `souly2024strongreject` (from SLR meta-finding: 23/25 empirical claims refuted).

**Candidate contribution:** Minimum reporting standard for guardrail evaluations — analogous to PRISMA for SLRs.

---

## Gap G5: Constitutional AI for Multimodal Models (gap_score: 4)

**Problem:** Constitutional AI (`bai2022constitutional`) has no multimodal analogue. VLM constitutions that govern image+text generation are undefined.

**Evidence:** `bai2022constitutional`, `oh2024safevlm`, `li2024vlguard`.

**Candidate contribution:** Formal definition of a multimodal constitution and a framework for RLAIF-based multimodal alignment.

---

## Already-Addressed Gaps (do not re-propose)

- Text-only jailbreak attacks: saturated (`zou2023universal`, `wei2023jailbroken`, many follow-ups)
- RLHF alignment fundamentals: saturated (`ouyang2022training`, `bai2022constitutional`, `touvron2023llama2`)
- Static multimodal benchmarks: well-covered (`liu2024mmsafetybench`, `luo2024jailbreakv`)
