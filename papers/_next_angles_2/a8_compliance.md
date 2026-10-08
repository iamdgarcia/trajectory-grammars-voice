# Compliance-by-Construction for Conversational Banking Agents

## Working title
"Deadlines, Not Audits: Regulatory Obligations as Schedulable Constraints in Conversational Banking Agents" (alt: "Floors Meet Deadlines: Compliance-by-Construction for Cascade Voice Agents in Banking").

## Landscape
1. **EU AI Act, Reg. (EU) 2024/1689** — Art. 50(1) obliges operators to disclose that users interact with an AI system; Art. 99 penalties up to €35M/7% turnover; general application 2 Aug 2026. A disclosure duty with an implicit "immediately" — never modeled as a deadline.
2. **GDPR, Reg. (EU) 2016/679** — Art. 5(1)(c) minimization, Art. 9 (voice-biometric templates as special-category data), Art. 22(3) right to human intervention: precedence gates and handoff obligations attachable to specific dialogue events.
3. **DORA, Reg. (EU) 2022/2554** (applies 17 Jan 2025) — ICT-resilience duties for the cloud voice pipeline plus major-incident reporting deadlines (initial notification ≤4h after classification / ≤24h from awareness [verify exact RTS figures]) — the regulator itself imposes deadlines at a second clock scale.
4. **PSD2 + Del. Reg. (EU) 2018/389** — SCA and dynamic linking; voice-channel SCA forces a mandatory pre-execution gate before any irreversible payment.
5. **MiFID II Art. 16(7) + RTS 6** — call recording with 5-year retention; PCI DSS "pause-and-resume" during card-number capture: recording as a toggleable obligation on the conversation DAG.
6. **CFPB, "Chatbots in Consumer Finance"** (June 2023); **FINRA Reg. Notice 24-09** (2024); **ESMA public statement on AI in investment services** (May 2024) [verify document numbers] — supervisors already treat chatbot failures as conduct issues, still audit-based.
7. **τ-bench, arXiv:2406.12045** — evaluates policy adherence of tool-using service agents (retail/airline), but static, text-only, timeless.
8. **GuardAgent, arXiv:2406.09187** [verify ID] and 2025 runtime-constraint work (AgentSpec [verify]) — enforce agent policies at runtime, but task/text agents: no statutory mapping, no deadlines, no audio-out semantics.
9. **Commitment machines (Yolum & Singh, 2002)** and **event-calculus normative systems (Artikis & Sergot [verify venue])** — obligations-with-deadlines in protocols; mature logic never applied to voice-agent compliance.
10. **Runtime verification (Leucker & Schallhart, 2009)** + **Declare LTL patterns (Pesic & van der Aalst, BPM 2006)** — checkable obligation templates over event logs; the business-process-compliance community never lifted them into conversation DAGs.

## The gap
**RQ:** Can statutory duties for a banking voice agent be compiled, obligation by obligation, into schedulable constraints (deadlines, precedence gates, toggle conditions) on the conversation DAG — so compliance becomes a runtime-satisfiability property checked on the event stream instead of a post-hoc audit — and what does the resulting schedulability condition say about cascade latency floors? Unsolved because (i) legal/compliance literature treats chatbots at policy level with no formal dialogue model; (ii) runtime-constraint work (GuardAgent et al.) has no notion of statutory deadlines or audibility; (iii) our floor program bounds what the pipeline *can* do, nothing bounds what it *must* do. The unclaimed object: **mandatory utterances as deadlines** — "speak the AI disclosure within δ of session start" is a real-time scheduling constraint competing with the 200 ms CCC.

## Candidate contribution
**Framework (CbC):** (a) obligation taxonomy — disclosure-on-contact, recording-consent gate, minimization constraints on tool arguments, handoff-offer, pre-execution gates on irreversible actions, retention/erasure, incident reporting; (b) formal semantics — deadline obligations + precedence + toggles over the conversation event log, LTL-templated and monitor-checkable; (c) **Compliance Schedulability Theorem**: obligations are satisfiable iff every mandatory utterance's window δ_i dominates worst-case completion (p99 Λ\* + cessation floor + hangup race), with corollaries: mandated content belongs in the delivery clock (generalizing OG4 filler-hygiene); interrupted-disclosure semantics under barge-in (audibility required — extends generation-interruptible vs execution-persistent); DORA-degraded mode must keep compliance satisfiable under component failover. Deliverables: formal model + worked Spanish banking obligation set with verbatim reg citations + reference-monitor design + compliance-trace telemetry spec.

## Reuse of our published results
Paper 1's Λ\* and ReAct k-step bound give the completion-time side of every slack computation; Paper 2's detect/decide/cease/resume gives interruption semantics for mandated utterances and the hangup-race distribution; Paper 3's two-question veto extends to a third question ("is a mandatory utterance due now?"), with its published p99 178–268 ms decision latency showing headroom under 500 ms-class windows; KB OG3's typed tool DAG hosts the pre-execution gates; KB OG4's filler-placement theorem becomes mandated-content placement.

## Banking grounding
Intrinsic: Spanish AEPD/LOPDGDD consent doctrine for call recording; GDPR 22(3) handoff before automated credit decisions (CCD2 2023/2225 adds human-review rights [verify article no.]); PSD2 SCA on spoken OTPs; PCI DSS pause-resume on PAN capture; ASR/TTS/GKE components as DORA third-party ICT services with failover and exit duties; production telemetry already logs the trigger/satisfy/violate timestamps the monitor consumes; vishing and voice-deepfake pressure push authentication disclosures into the same deadline formalism.

## Scores
- **Novelty 4** — unclaimed voice×legal-deadline intersection; each flank has precedents, the synthesis does not.
- **Fit 5** — deadlines are the exact mirror of the published floors; reuses all three papers plus two KB results.
- **Banking 5** — obligations are real, dated, penalty-backed; the Spanish production channel exists.
- **Feasibility 4** — conceptual + formal; the empirical part is a monitor over existing telemetry, no new dataset.
- **Risk 3** — legal-precision burden and unsettled AI Act interpretation (obviousness exception to Art. 50) invite law-side pushback; mitigated by engineering framing and verbatim reg citation.

## Verdict
**Pursue now.** Intrinsic banking fit, direct theoretical reuse, zero data dependency, and a genuinely unclaimed formal object. Before drafting: one live 2024–2026 arXiv sweep for "runtime regulatory constraints LLM agents" and "AI Act compliance dialogue systems" to confirm the gap holds, and verify all [verify] marks.
