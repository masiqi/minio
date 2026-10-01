# Architecture — 初始方向

这是一个有意保持轻量、以学习为导向的实现。

## 我们自己实现什么

直接用于学习 Agent Engineering 的部分：
- Agent loop
- tool contract 与 dispatch
- execution state
- failure / retry 语义
- context assembly
- memory orchestration
- policy boundary
- evaluation hook

## 我们复用什么

对于重复实现不会带来太多学习价值的通用基础设施，直接复用：
- database / storage
- model / provider SDK
- MCP SDK / protocol implementation
- sandbox / microVM infrastructure
- tracing / metrics backend

## 初始逻辑边界

- `agent` — reasoning / execution loop
- `tools` — typed tool contract 与 dispatch
- `state` — run / checkpoint state
- `context` — prompt / context assembly
- `memory` — durable memory interface
- `runtime` — execution orchestration
- `sandbox` — isolated execution abstraction
- `observability` — traces / metrics / events
- `evaluation` — offline / online evaluation hooks
- `security` — authorization / policy boundaries

在进入 sandbox 学习和设计阶段之前，我们暂不确定具体的 sandbox 实现。先定义 interface 和 threat model，再做技术选型。

## Framework 策略

不要一开始就用 LangGraph / LangChain / AutoGen 把 Agent loop 隐藏起来。先实现最小机制。之后再使用 framework 重建或对比选定流程，并能够解释每一层 abstraction 带来了什么收益，又付出了什么成本。
