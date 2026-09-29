# Architecture — Initial Direction

This is intentionally a learning-oriented, lightweight implementation.

## What we will build ourselves

The parts that directly teach Agent Engineering:
- Agent loop
- tool contracts and dispatch
- execution state
- failure/retry semantics
- context assembly
- memory orchestration
- policy boundaries
- evaluation hooks

## What we will reuse

Commodity infrastructure where reinventing it adds little learning value:
- database/storage
- model/provider SDKs
- MCP SDK/protocol implementation
- sandbox/microVM infrastructure
- tracing/metrics backends

## Initial logical boundaries

- `agent` — reasoning/execution loop
- `tools` — typed tool contracts and dispatch
- `state` — run/checkpoint state
- `context` — prompt/context assembly
- `memory` — durable memory interfaces
- `runtime` — execution orchestration
- `sandbox` — isolated execution abstraction
- `observability` — traces/metrics/events
- `evaluation` — offline/online evaluation hooks
- `security` — authorization/policy boundaries

We will delay committing to a concrete sandbox implementation until the sandbox learning/design stage. The interface and threat model come first.

## Framework strategy

Do not begin by hiding the Agent loop behind LangGraph/LangChain/AutoGen. Implement the minimal mechanism first. Later, rebuild or compare selected flows with frameworks and explain what each abstraction buys us and what it costs.
