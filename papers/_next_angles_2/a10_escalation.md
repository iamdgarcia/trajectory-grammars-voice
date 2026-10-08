# The Escalation Floor: Human Handoff as Cost-Aware Deferral in Voice Banking

## Working title
**"Asking for a Human: The Escalation Floor and Cost-Aware Deferral in Conversational Banking"**

## Landscape (8-10 anchors, one line each)
1. **Bohus & Horvitz 2011** (ICMI, KB-verified) — interruption/engagement handling as a utility-driven decision policy (yield/continue/re-engage); pre-generative era, no latency-floor or cost analysis — our direct policy-layer ancestor.
2. **Madras et al. 2018**, *Predict Responsibly: Learning to Defer* (arXiv 1711.06864 [verify]) — deferral as learning problem with human accuracy coupled in; static classification only.
3. **Mozannar & Sontag 2020**, *Consistent Surrogates for Learning to Defer* (NeurIPS, arXiv 2006.13565 [verify]) — consistent surrogate losses for the defer decision; the formal core we would lift to dialogue state.
4. **Okati et al. 2021**, *Differentiable Learning Under Triage* (arXiv 2103.08902 [verify]) — triage cost asymmetry; still no conversation dynamics or time pressure.
5. **Gans, Koole & Mandelbaum 2003**, *Telephone Call Centers: Tutorial, Review, and Research Prospects* (M&SOM [verify]) — the queueing/staffing-cost canon for teller-side economics; zero agent-side coupling.
6. **Schegloff, Jefferson & Sacks 1977**, *The Preference for Self-Correction in Repair* (Language [verify]) — handoff as conversational repair with a preference structure; grounds the "one chance to hand off gracefully" claim.
7. **de Visser et al. 2018**, longitudinal *trust repair in human-machine interaction* (HFES [verify]) — post-failure trust repair exists but never tied to the latency of the repair handoff.
8. **taubench2024** (KB-verified) — latency+cost evaluation of agent tool loops; escalation is absent from the action space.
9. **lin2026fdbv3** (KB-verified, Full-Duplex-Bench-v3) — tool use under disfluency; no human-in-the-loop transitions at all.
10. **Our three papers** (KB-verified; Zenodo 10.5281/zenodo.23233331 for the third) — onset floor Λ*, cessation floor (detect/decide/cease/resume), two-question semantic VAD veto with Spanish barge-in F1 0.76 and cloud p99 178-268 ms.

## The gap (testable RQ + why unsolved)
**RQ:** *What is the fastest possible warm handoff from a live voice agent to a human teller, and what cost-aware policy should trigger it mid-conversation?*

Two sub-questions, both open:
- **The escalation floor:** from the instant the policy decides "defer," time-to-first-human-audio decomposes into detect + decide + bridge + queue-connect + read-in. Nobody bounds this. The published floors (onset Λ*, cessation) stop at the agent; the human leg is unmodeled. Read-in is the interesting term: it is reducible only by context the *agent* can push ahead of the connect (transcript + summary + intent + tool state), i.e., a partial handoff where the agent demotes to scribe.
- **Deferral under conversation dynamics:** learning-to-defer theory assumes an i.i.d. example arrives, one defer decision, static human cost. In dialogue, deferral cost *accrues over turns* (frustration, abandonment, repeat-contact risk), the human's cost is a queueing/staffing function, and the decision competes with the latency budget the agent is already fighting. No formal policy couples conversation state, latency floors, and a banking cost vector. Closest work (bohus2011interruptions) predates generative agents and has no cost or bound.

Testable prediction to anchor it: handoff latency above a threshold measurably degrades trust repair (customer must re-explain), and the escalation floor is achievable with an agent-authored read-in package.

## Candidate contribution
1. **Theorem (escalation floor):** Ω_esc = τ_detect + τ_decide + τ_bridge + τ_connect + τ_readin, with τ_readin bounded below by the human's information absorption given a maximal agent-pushed context package; τ_bridge shown to mask τ_connect under the existing filler-hygiene rule (delivery clock only). Mirrors thm:latency_floor / cessation structure.
2. **Framework:** escalation as learning-to-defer over dialogue state with cost vector (agent marginal cost, teller staffing cost, frustration-accrual cost), frustration proxied by measured signals we already have (barge-in rate, repair requests, negative feedback). One-chance property: a botched handoff forfeits the repair preference structure (Schegloff), so deferral must be *calibrated veto-style*, like our turn-end veto.
3. **Benchmark:** Spanish escalation episodes (fraud, dispute, vulnerability) with gold handoff points; simulator + small rig; measures Ω_esc decomposition and re-explanation rate.

## Reuse of our published results
- Cessation floor's detect/decide/cease/resume topology maps 1:1 onto handoff's detect/decide/bridge/connect — reuse the formal machinery, not a from-scratch build.
- Two-question semantic VAD: the calibrated veto becomes the escalation *probe* ("asking instead of listening" applied to "should I fetch a human?"); the Spanish frozen benchmark and p99 latency table transfer directly.
- Tool-hiding budget (OG3): context summarization for read-in is a type-C tool hidden under bridge speech.
- Λ* decomposition method is the template for the Ω_esc proof.

## Banking grounding
Teller staffing is a real, measurable cost (queueing canon); banking compliance requires guaranteed human recourse channels, so handoff is a regulatory artifact, not a UX nicety. Fraud/dispute calls are exactly where agent failure costs most and where a sub-second, fully-contextualized warm handoff has auditable value. Spanish-first population makes read-in quality (who re-explains, in which language) the trust-repair variable.

## Scores (1-5)
- **Novelty: 4** — deferral theory is mature but has never met latency floors, conversation state, or voice; the escalation floor itself is unclaimed.
- **Fit: 5** — the natural third floor of the series; reuses the formal template and policy layer wholesale.
- **Banking: 5** — staffing cost, compliance-mandated human availability, fraud-episode urgency, Spanish.
- **Feasibility: 4** — theory + small rig are in-pattern; main lift is constructing the Spanish escalation benchmark (synthetic, as with the VAD benchmark).
- **Risk: 3** — deferral lit is crowded; the paper must sell floor+cost coupling, not a new deferrer, or reviewers will say "Mozannar with extra steps."

## Verdict
**Pursue now.** It is the third paper of the floors series (onset → cessation → escalation), the intersection (defer theory × latency floors × voice banking) is empty in the anchors above, and every prior result reused is already published and citable. Do it before the eval-stack capstone; the escalation benchmark it produces also feeds the eval-stack angle later.
