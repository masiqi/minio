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

## Current pointer

- Baseline: completed (2026-09-28)
- Phase: 30-Day Phase 1
- Next: Day 1
- Topic: RNN structural limitations → why Attention
- Minimum acceptance: explain Attention's design motivation without hints and correctly distinguish Attention's role from positional information.
