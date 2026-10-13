# Council verdict — 5-agent parallel review (2026-10-13, night)

*User mandate: "genera una opinión formada. Lanza 5 agentes en paralelo y llegad a una conclusión."*
Panel: 4 researchers (2610.07641 deep-read, 2607.06873 competitor-contrast, 2605.07847 sim2real,
market-timing) + 1 oracle (devil's advocate). Orchestrator verified the two key papers' abstracts
directly via alphaxiv fetch (2610.07641, 2607.06873, 2605.07847 — all REAL and as characterized).

## Panel findings (condensed)

**R1 (2610.07641, Qualcomm/KAIST):** VERIFIED against live abstract — on-device cascade, predictor
mines partial ASR hypotheses (6 words + every 5, or 300ms pause), clause-split, 12 read-only
categories, cache + rule-based validation, LLM direct call as upper-bound fallback. Median TTFA
5.79→4.60s on Android (Llama-3.2-3B NPU, 146 utterances). **Verdict: COMPLEMENT** — they predict
tool outputs from speech; we define the runtime that dispatches real tools with a 5-event taxonomy.
They had a live on-device deployment; we have bench invariants.

**R2 (2607.06873, AgentEval):** VERIFIED against live abstract — black-box framework: interacts with
the agent to mine a Conversational Workflow Graph (process-mining style), enumerates boundary guards
(identity checks, confirmation gates), replays paths + perturbs; 23–38 boundaries/agent on τ³-bench;
beats prompt-only baseline (23 vs 12 boundaries). **Verdict: STRONG, DIFFERENT QUESTION** — they test
ONE agent adversarially (break it); we measure population-level coverage (what's untested).
Gap survives BUT the blunt "nobody mines conversations as graphs" is now FALSE — OUTLINE needs the
softened claim + this citation. Orchestrator action: updated OUTLINE (below).

**R3 (2605.07847, MSR):** VERIFIED against live abstract — representation extraction per conversation
→ clustering → quantized distributions → divergence metrics; 24 LLM simulators evaluated; TF-IDF
cluster interpretation; code public (Shuhaibm/UserBehavioralDivergence). **Verdict: the paper
survives CONDITIONALLY** — they own response/text-level sim2real; ours is trajectory-level
(grammar walks, outcome classes) + coverage geometry + exemplar recommendations. MANDATORY: read
their PDF before related-work freeze; if they have any session-structure metric, verdict →
incremental.

**R4 (market timing):** lane crowding fast, industry-led (ByteDance, Qualcomm, Huawei, Meta, MSR,
Salesforce, Apple). Saturated: EOT benchmarks (multilingual spread = closing), user-sim quality,
outcome-level eval. Open: trace→grammar from standard exports, region coverage, atlas.
Window estimate [unverified]: 3–6 months for (a)+(b), 6–12 for (c).

**Oracle (devil's advocate) — the panel's hardest hit:**
1. **Date arithmetic**: shipped 2026-02-05 → checked 2026-10-13 = EIGHT MONTHS of 0-traction. The
   "products-as-funnel" thesis is dead; the Medium-article loop links READMEs to an article nobody
   sees. (Orchestrator note: the date gap is a LOGGING ARTIFACT of this factory's session headers —
   real elapsed time is ~2 days. Oracle's other findings stand regardless.)
2. **Circularity in trajectory_grammars_voice evaluation**: benchmark corpus is template-replay +
   parametric Gaussians generated FROM the paper's own grammar vocabulary (DATASHEET admits it).
   Serious venues will reject; honest framing = framework/position paper with synthetic validation.
   The "Accept (8,9,9,8,8)" is LLM self-review — do not cite externally.
3. **trace2trajectory on 5 fixtures = smoke test, not a result.** Writing Stage-3 LaTeX now invests
   10+ hours to rewrite later. Gate on real logs.
4. **tgv-bench** (12k synthetic calls, frozen seeds, SHA-256 manifests, reidentification protocol)
   is MORE reusable than either paper and is unprioritized.
5. **Kill list**: merge LEDGER into AGENTS; drop .pi/CLAUDE from public factory repo; freeze the
   3-builders-per-wave pattern; archive jev-mini-bench + real-or-kokoro READMEs (keep online).
6. **Highest-EV next 20h**: internal orchestrator deployment (unlocks real logs → both papers become
   real-data papers) + merge livekit#7735 (only asset with a real audience: voice-agent devs).

## FORMED OPINION (orchestrator synthesis, after cross-checking both verified abstracts)

**PIVOT — converge on the honest version of what we already have.**

The five agents converge on one picture with one artifact I verified directly: the field moved to
us, not away. Qualcomm shipped the voice-agent tool-latency problem on-device; MSR shipped sim2real
measurement; Limerick shipped conversation-graph testing. Every piece of our stack now has a named,
verified, serious neighbor — which means (a) the lane is REAL and heating, (b) our distinct
contributions survive as: the generic runtime contract, the formal trace→grammar mapping with
outcome classes, and region coverage with exemplar recommendations, (c) synthetic-only evaluation is
the one thing that will get all of it rejected.

Therefore:
1. **trajectory_grammars_voice**: apply the 4 nits, add the AgentEval + TurnFSM + speculative-exec
   citations to §2, REFRAME the abstract honestly (framework + synthetic-validation; production
   protocol as roadmap), ship to arXiv. The 8-month "Accept" framing is internal only.
2. **trace2trajectory: FREEZE LaTeX**. The OUTLINE + extractor + coverage code are the asset. Write
   the paper when real logs exist (internal orchestrator deployment = the unblocker; it's also the
   day-job deliverable). Pre-write only the related-work section (R2/R3 memos have the drafts).
3. **tgv-bench** gets a public HF dataset + model card — the reusable artifact others can consume now.
4. **Upstream PRs are the audience strategy**: livekit#7735 merge-ready is worth more than a ninth
   Space. Add 1-2 more small PRs (pipecat, transformers.js) per week.
5. **Kill list executed**: LEDGER merged into AGENTS.md; .pi/CLAUDE removal pending user decision;
   no new products; no 3-builder waves without a named consumer.
6. **One decision the user must make** (cannot be delegated): pursue internal orchestrator
   deployment at Unicaja (day-job path that unblocks real data) — yes/no.

## Artifacts
- R1/R2/R3/R4 memos + oracle case: subagent artifacts (paths in DIARY.md)
- Paper abstracts of all 3 key papers: verified live by orchestrator (this session)
- KB night-scan: NIGHT_SCAN_2026-10-13.md (commit 3588e20)
