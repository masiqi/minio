# 30 天 AI Engineering 学习计划

## 目标

从较强的后端 / 企业工程能力和实际 Agent 经验出发，成长为能够独立解释、实现并应对面试的 AI Application Architect / Agent Engineer。

完成这一阶段意味着能够：
- 解释一个机制为什么存在；
- 解释它的因果关系和内部机制；
- 讨论边界条件与 trade-off；
- 将它应用到真实系统；
- 在没有提示的情况下回答面试追问；
- 将这一思想迁移到新的问题。

## 每日学习闭环

每个重要主题都遵循：

1. Diagnostic — 先在没有提示的情况下回答。
2. Why — 找出问题，以及为什么之前的方法不够。
3. Mechanism — 理解因果机制。
4. Feynman Recall — 用自己的话独立解释。
5. Challenge — 针对因果、边界、反例或工程实践进行 1–3 个追问。
6. Correction — 明确指出正确点、错误、混淆和遗漏。
7. Engineering Transfer — 映射到真实 Agent / RAG / MCP / Sandbox 系统。
8. Interview Expression — 在没有提示的情况下完成 2–5 分钟回答。
9. Acceptance — 分别评估 Concept / Mechanism / Engineering / Interview。
10. Review — 根据真实掌握程度安排间隔复习。

能够复述定义 **不等于** 掌握。

## Baseline 摘要 — 2026-09-28

- Transformer：有基本认识；从 RNN 局限到 Transformer 的因果模型还不完整。
- Attention：优先薄弱点；对 Attention 与 positional information 存在部分混淆。
- Token / Embedding：理解基本 pipeline；需要进一步厘清 embedding 与 contextual representation。
- RAG / Retrieval：工程直觉相对较强。
- Agent / Tool Calling：生产工程直觉相对较强；定义和核心 loop 需要系统化。
- MCP：有实际经验；需要加强 protocol abstraction 与 standardization value 的理解。
- Context / Memory：相对较强。
- Evaluation：observability / tracing 直觉强于系统化 evaluation 方法。
- Enterprise AI Architecture：security / isolation 意识较强；架构拆解需要更加结构化。

## 30 天路线

### Week 1 — LLM 心智模型
- Day 1：RNN 结构性局限 → 为什么需要 Attention
- Day 2：Self-Attention 与 Q/K/V
- Day 3：Attention 计算、softmax、weighted sum、multi-head
- Day 4：Positional information
- Day 5：Token、token id、embedding、contextual representation
- Day 6：Transformer block：Attention、FFN、residual、normalization
- Day 7：费曼复习 + Transformer 面试

### Week 2 — RAG / Retrieval / Context
- Day 8：parsing、chunking、information boundary
- Day 9：embedding retrieval 与 vector similarity
- Day 10：sparse / dense / hybrid retrieval
- Day 11：reranking、recall vs precision、Top-K
- Day 12：context construction、context window、compression
- Day 13：RAG failure mode 与 evaluation
- Day 14：设计一个 100 万文档的企业级 RAG 系统

### Week 3 — Agent Engineering
- Day 15：LLM + Tool Calling 与 Agent 的区别
- Day 16：Agent loop、planning、state
- Day 17：tool contract、error、idempotency、recovery
- Day 18：memory engineering model
- Day 19：MCP boundary 与 protocol abstraction
- Day 20：harness、sandbox、execution runtime
- Day 21：企业 Agent workflow 系统设计

### Week 4 — Evaluation + Enterprise Architecture
- Day 22：Observability vs Evaluation
- Day 23：offline eval、dataset、golden set、metric、grader
- Day 24：online eval、A/B、human feedback、production monitoring
- Day 25：分层诊断：model / retrieval / tool / workflow
- Day 26：multi-tenancy、IAM、secret、data isolation
- Day 27：sandbox、network policy、risky action、security boundary
- Day 28：model gateway、cost、reliability、fallback、rate limit
- Day 29：完整 Enterprise Agent Platform 系统设计
- Day 30：综合面试 + re-baseline + 下一阶段计划

## 并行学习轨道

在概念路线之外，同时进行：

- **Framework track：** 根据当前岗位市场相关性选择 LangGraph、LangChain、AutoGen 等 framework。重点理解 abstraction 与 trade-off，而不是记 API。
- **Production track：** timeout、retry、fallback、idempotency、checkpoint / resume、concurrency、rate limiting、tool / model / RAG failure、observability。
- **Hands-on track：** 在本仓库中逐步构建轻量级企业 Agent runtime。

## Day 1 学习结果 — 2026-09-29

**主题：** RNN 结构性局限 → 为什么需要 Attention

**已接受的核心理解：**
- RNN 按序列位置递归处理；历史信息通过 hidden state 传递，而不是每一步都重新读取之前所有 token。
- 长距离信息必须经过多次连续的 state transition，因此远距离依赖更难保存和学习。
- LSTM / GRU 改善了 recurrent path 上的信息保存能力，但没有消除 sequential path 本身。
- Attention 改变了信息交互模式：一个位置可以直接使用相关位置的信息，而不需要让信息经过整个 recurrent chain。
- 去除 recurrent sequential dependency 也使训练能够实现更高程度的并行化。

**发现并纠正的缺口：**
- 最初对 hidden state 不够清晰；复习时需要再次建立 RNN hidden-state 直觉。
- 最初把 Attention weight 理解成每个 token 固定拥有的重要性。正确模型是：相关性 / attention weight 会针对当前 context 在不同位置之间动态计算。
- 需要继续区分 token embedding 与 contextual representation：相同 token embedding 会因为 position 和 context 不同而形成不同的 contextual representation。
- 不要说 Attention “没有 path”，也不要说 sequence length 没有成本。

**费曼证据：**
学习者已经能够独立解释：长序列处理会削弱早期信息的有效利用，而 Attention 缩短了信息交互路径，使相关信息能够被更直接地使用。纠正后达到 Day 1 的最低机制理解目标。

**复习目标：** 在 Day 2 前或 Day 2 开始时重新测试 RNN / LSTM 与 Attention 的因果区别，重点检查 hidden state 和 information path。

## 当前进度

- Baseline：已完成（2026-09-28）
- Day 1：已完成（2026-09-29）
- 阶段：30-Day Phase 1
- 下一步：Day 2
- 主题：Self-Attention 与 Q/K/V
- Day 2 入场要求：用一分钟解释 Attention 相比 RNN / LSTM 如何改变 information path。
- Day 2 最低通过标准：能够解释为什么 Q、K、V 是三个不同的 projection，它们如何支持动态 token-to-token relevance，并能够把这一机制连接回 contextual representation，而不是依赖背诵定义。
