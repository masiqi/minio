# minio

一个轻量级的企业 Agent Engineering 实验室。

这个仓库同时承担两个角色：
- 一个小型企业级 Agent runtime 的动手实现；
- 一个面向 AI 应用架构与 Agent Engineering 的持续学习工作区。

## 原则

- 在用框架隐藏机制之前，先理解机制本身。
- 核心 Agent 逻辑自己实现；对于重复造轮子没有学习价值的基础设施则直接复用。
- 将生产级问题作为一等公民：state、retry、idempotency、isolation、security、observability、evaluation。
- 每个重要概念都必须经得住费曼解释、工程迁移和面试追问。

## 学习工作流

参见 [docs/learning/PLAN.md](docs/learning/PLAN.md)。

## 项目方向

实现会采用渐进式演进，而不是一开始就构建大型框架：
1. 最小 Agent loop 与 tool contract
2. state 与 failure handling
3. retrieval / context
4. memory
5. MCP
6. sandbox runtime
7. observability 与 evaluation
8. multi-tenant / security
9. 与主流 Agent framework 对比并重构

架构决策记录在 `docs/adr/` 下。
