# minio

一个轻量级的企业 Agent Engineering 实验室。

这个仓库同时承担两个角色：
- 一个小型企业级 Agent runtime 的动手实现；
- 一个面向 AI 应用架构与 Agent Engineering 的持续学习工作区。

## 当前学习入口（2026-10-09 修订）

**教练/代理先读 [AGENTS.md](AGENTS.md)：每个用户回答后检查是否需要保存教学 checkpoint；有新证据或交接需要时当轮提交，无变化不做空提交。** 具体教学规则与持久化契约通过该文件进入。

从 [当前计划入口](docs/learning/PLAN.md) 开始。**继续学习或换会话时，读取 [最新教学 Checkpoint](docs/learning/checkpoints/LATEST.md) 及其指向的完整快照。** 其中包含实际实验输出、已答问题、不重复项与下一动作，不只保存课程进度。

- [能力驱动学习方案 V2](docs/learning/CURRICULUM_V2.md)：数学/表示、训练机制、完整 Transformer、推理、RAG、Agent、MCP/Sandbox、Evaluation 与企业架构。
- [当前学习状态](docs/learning/LEARNING_STATE.md)：保留已有证据，与Checkpoint一致，不把旧 Sources 初始化状态当成当前进度。
- [Checkpoint保存与恢复协议](docs/learning/checkpoints/README.md)：何时保存、必须记录什么、如何读后继续及防止重复提问。
- [课程完整性审计](docs/learning/AUDIT_2026-10-06.md)：核查发现和修订依据。
- [M02 神经网络如何学习](docs/learning/modules/M02-training-mechanisms.md)：T01–T08 的完整训练机制模块。

旧 30 天计划的不可变历史链接保留在 PLAN.md。旧 Day 编号不再临时改主题；后续使用 M00–M10 能力模块和独立会话记录。

## 原则

- 在用框架隐藏机制之前，先理解机制本身。
- 核心 Agent 逻辑自己实现；对于重复造轮子没有学习价值的基础设施则直接复用。
- 将生产级问题作为一等公民：state、retry、idempotency、isolation、security、observability、evaluation。
- 每个重要概念都必须经得住费曼解释、工程迁移和面试追问。
- 用独立推导、实现、测试与延迟验证记录掌握；提示后复述不等于独立通过。

## 三个渐进式学习成果

P1：能训练和生成的微型 Transformer，用于理解模型机制。

P2：可评测的 RAG / 阅读问答系统，作为 LightRAG 等方案的对照基线。

P3：接入工具、状态恢复、权限隔离和评估的轻量企业 Agent runtime。

这些是实施里程碑，不是声称代码已经完成。本次修订主要交付计划与状态文档。

## 项目方向

实现会采用渐进式演进，而不是一开始就构建大型框架：
1. 最小 Agent loop 与 tool contract
2. state 与 failure handling
3. retrieval / context
4. memory
5. MCP
6. sandbox runtime
7. observability 与 evaluation（从早期测试开始，之后深化）
8. multi-tenant / security（副作用与外部数据接入前定义边界）
9. 与主流 Agent framework 对比并重构

架构决策记录在 `docs/adr/` 下。既有架构方向见 [OVERVIEW.md](docs/architecture/OVERVIEW.md)。
