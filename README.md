# minio

A lightweight enterprise-agent engineering lab.

This repository is both:
- a hands-on implementation of a small enterprise-grade agent runtime;
- a persistent learning workspace for AI application architecture and Agent Engineering.

## Principles

- Learn the mechanism before hiding it behind a framework.
- Build core agent logic ourselves; reuse infrastructure where it is not educational to reinvent it.
- Production concerns are first-class: state, retries, idempotency, isolation, security, observability, evaluation.
- Every important concept must survive Feynman explanation, engineering transfer, and interview follow-up.

## Learning workflow

See [docs/learning/PLAN.md](docs/learning/PLAN.md).

## Project direction

The implementation will evolve incrementally rather than starting as a large framework:
1. minimal agent loop and tool contract
2. state and failure handling
3. retrieval/context
4. memory
5. MCP
6. sandbox runtime
7. observability and evaluation
8. multi-tenant/security concerns
9. compare/refactor with mainstream agent frameworks

Architecture decisions will be recorded under `docs/adr/`.
