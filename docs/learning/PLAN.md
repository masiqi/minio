# 30-Day AI Engineering Learning Plan

## Goal

Move from strong backend/enterprise engineering and practical Agent experience to an independently explainable, implementable, and interview-ready AI Application Architect / Agent Engineer skill set.

Completion means being able to:
- explain why a mechanism exists;
- explain its causal/internal mechanism;
- discuss boundaries and trade-offs;
- apply it to a real system;
- answer follow-up interview questions without hints;
- transfer the idea to a new problem.

## Daily learning loop

Every important topic follows:

1. Diagnostic — answer first without hints.
2. Why — identify the problem and why previous approaches are insufficient.
3. Mechanism — understand the causal mechanism.
4. Feynman Recall — explain it independently in your own words.
5. Challenge — 1–3 follow-ups on causality, boundaries, counterexamples, or engineering.
6. Correction — explicitly identify correct points, errors, confusion, and omissions.
7. Engineering Transfer — map it to real Agent/RAG/MCP/Sandbox systems.
8. Interview Expression — give a 2–5 minute answer without prompts.
9. Acceptance — assess Concept / Mechanism / Engineering / Interview.
10. Review — schedule spaced review from actual mastery.

Being able to repeat a definition is **not** mastery.

## Baseline summary — 2026-09-28

- Transformer: basic recognition; causal model from RNN limitations to Transformer is incomplete.
- Attention: priority weakness; Attention and positional information are partially conflated.
- Token / Embedding: basic pipeline understood; embedding vs contextual representation needs clarification.
- RAG / Retrieval: comparatively strong engineering intuition.
- Agent / Tool Calling: comparatively strong production-oriented intuition; definitions and core loop need systematization.
- MCP: hands-on experience; protocol abstraction and standardization value need strengthening.
- Context / Memory: comparatively strong.
- Evaluation: observability/tracing intuition is stronger than systematic evaluation methodology.
- Enterprise AI Architecture: strong security/isolation instincts; architecture needs more structured decomposition.

## 30-day route

### Week 1 — LLM mental model
- Day 1: RNN structural limitations → why Attention
- Day 2: Self-Attention and Q/K/V
- Day 3: Attention computation, softmax, weighted sum, multi-head
- Day 4: Positional information
- Day 5: Token, token id, embedding, contextual representation
- Day 6: Transformer block: Attention, FFN, residual, normalization
- Day 7: Feynman review + Transformer interview

### Week 2 — RAG / Retrieval / Context
- Day 8: parsing, chunking, information boundaries
- Day 9: embedding retrieval and vector similarity
- Day 10: sparse / dense / hybrid retrieval
- Day 11: reranking, recall vs precision, Top-K
- Day 12: context construction, context window, compression
- Day 13: RAG failure modes and evaluation
- Day 14: design a 1M-document enterprise RAG system

### Week 3 — Agent Engineering
- Day 15: LLM + Tool Calling vs Agent
- Day 16: Agent loop, planning, state
- Day 17: tool contracts, errors, idempotency, recovery
- Day 18: memory engineering models
- Day 19: MCP boundaries and protocol abstractions
- Day 20: harness, sandbox, execution runtime
- Day 21: enterprise Agent workflow system design

### Week 4 — Evaluation + Enterprise Architecture
- Day 22: Observability vs Evaluation
- Day 23: offline eval, datasets, golden sets, metrics, graders
- Day 24: online eval, A/B, human feedback, production monitoring
- Day 25: layered diagnosis: model / retrieval / tool / workflow
- Day 26: multi-tenancy, IAM, secrets, data isolation
- Day 27: sandbox, network policy, risky actions, security boundaries
- Day 28: model gateway, cost, reliability, fallback, rate limits
- Day 29: full Enterprise Agent Platform system design
- Day 30: comprehensive interview + re-baseline + next-phase plan

## Parallel tracks

Alongside the conceptual route:

- **Framework track:** LangGraph, LangChain, AutoGen and other frameworks selected from current job-market relevance. Focus on abstractions and trade-offs, not API memorization.
- **Production track:** timeout, retry, fallback, idempotency, checkpoint/resume, concurrency, rate limiting, tool/model/RAG failure, observability.
- **Hands-on track:** incrementally build this repository's lightweight enterprise Agent runtime.

## Day 1 result — 2026-09-29

**Topic:** RNN structural limitations → why Attention

**Accepted core understanding:**
- RNN processes sequence positions recurrently; historical information is carried through a hidden state rather than re-reading all previous tokens at every step.
- Long-distance information must pass through many sequential state transitions, making distant dependencies harder to preserve and learn.
- LSTM/GRU improve information preservation on the recurrent path but do not remove the sequential path itself.
- Attention changes the information-interaction pattern: a position can directly use information from relevant positions instead of requiring it to traverse the whole recurrent chain.
- Removing recurrent sequential dependency also enables much greater parallelism during training.

**Corrections / gaps discovered:**
- Hidden state was initially unclear; revisit RNN hidden-state intuition during review.
- Attention weights were initially understood as fixed importance attached to each token. Correct model: relevance/attention weights are dynamically computed between positions for the current context.
- Token embedding and contextual representation need continued separation: identical token embeddings can develop different contextual representations because position and context differ.
- Do not say Attention has "no path" or that sequence length has no cost.

**Feynman evidence:**
The learner independently explained that long sequential processing can weaken early information and that Attention shortens the interaction path so relevant information can be used more directly. The final explanation met Day 1's minimum mechanism goal after correction.

**Review target:** Re-test the RNN/LSTM vs Attention causal distinction before or during Day 2, with emphasis on hidden state and information path.

## Current pointer

- Baseline: completed (2026-09-28)
- Day 1: completed (2026-09-29)
- Phase: 30-Day Phase 1
- Next: Day 2
- Topic: Self-Attention and Q/K/V
- Day 2 entry requirement: explain in one minute why Attention changes the information path relative to RNN/LSTM.
- Day 2 minimum acceptance: explain why Q, K, and V are three different projections, how they support dynamic token-to-token relevance, and connect the mechanism back to contextual representation without relying on memorized definitions.
