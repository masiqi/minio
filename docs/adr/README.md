# Architecture Decision Records

对于值得长期记住、并且需要在面试或设计评审中能够解释和捍卫的决策，使用 ADR（Architecture Decision Record）记录。

每个 ADR 应包含：
- Context：背景
- Decision：决策
- Alternatives considered：考虑过的替代方案
- Trade-offs：权衡
- Failure / security implications：故障与安全影响
- 什么证据会促使我们重新审视该决策

早期预计记录的 ADR 包括：
- 在采用 orchestration framework 之前，先实现自定义的最小 Agent loop；
- sandbox interface 以及最终的 microVM / runtime 选型；
- state / checkpoint 持久化；
- tool contract 与 idempotency 语义；
- model / provider abstraction。
