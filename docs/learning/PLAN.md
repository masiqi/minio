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

## Day 2 学习结果 — 2026-10-04

**主题：** Self-Attention 与 Q/K/V

**已接受的核心理解：**
- Self-Attention 本身负责 token 之间的信息交互；Position Encoding / positional information 负责提供顺序与位置信息，两者职责不同。
- 同一个 token 的表示通过不同的可学习 projection 生成 Q、K、V：Q 表示当前需要寻找什么信息；K 用于与 Query 做相关性匹配；V 是匹配后实际被加权传递的信息。
- Q 与所有 K 的匹配是动态、context-dependent 的，不是每个 token 固定拥有一个重要性权重。
- Attention 的输出不是“选中某一个 Value”，而是根据 attention weights 对多个 Value 加权求和，形成新的 contextualized representation。
- 一个长度为 n 的序列会形成 n 个 Query，每个 Query 与 n 个 Key 建立相关性；这些计算可以组织为矩阵运算并行执行，而不像 RNN 依赖前一步 hidden state。
- Multi-Head Attention 的初步直觉已经建立：head 数量代表多个独立 attention 视角；每个 head 的维度代表单个视角的表示空间。不同 head 使用独立参数，并可能在训练中形成不同的关注模式。

**已提前覆盖的 Day 3 内容：**
- dot product attention score；
- scaled dot-product 中除以 √d_k 的直觉：控制高维点积的数值尺度，避免 Softmax 过度尖锐；
- Softmax 将 score 转换为非负且总和为 1 的相对 attention weights，而不是执行 Top-K 硬选择；
- 使用 attention weights 对 Value 做 weighted sum；
- Multi-Head 的基本动机与 head 数量 / head dimension 的 trade-off。

**发现并纠正的缺口：**
- 一度把 Self-Attention 的直接信息交互作用归因于 Position Encoding，已纠正。
- 一度把 Key 理解为“它能提供什么”，已进一步区分：Key 服务于匹配，Value 服务于实际信息传递。
- 一度把 Softmax 理解为排序 / 选择前几名，已纠正为连续权重分配。
- 对 √d_k scaling 最初只记得“让训练更稳定 / 防梯度问题”，现已补上高维点积 → score 尺度增大 → Softmax 过尖 → scaling 控制尺度的因果链。
- 需要继续巩固：更严谨地表达 Q 的作用，不把 Q 限定为“我是谁”，而是“当前 token 为更新自身表示需要从上下文寻找什么信息”。

**费曼证据：**
学习者能够以“苹果 / 它 / 好吃”为例，独立串联 Q → 与所有 K 点积 → scaling → Softmax → attention weights → 加权 Value → 新 contextual representation；能够解释 Self-Attention 相比 RNN 为什么更适合并行；能够用“多个专家视角”解释 Multi-Head 的基本动机，并识别 head 过多可能带来的冗余与单 head 表示空间变窄问题。

**Day 2 结论：** 已达到最低通过标准。

## 当前进度

- Baseline：已完成（2026-09-28）
- Day 1：已完成（2026-09-29）
- Day 2：已完成（2026-10-04）
- 阶段：30-Day Phase 1
- 下一步：Day 3
- 主题：Attention 计算、Softmax、weighted sum、Multi-Head
- Day 3 状态：已提前覆盖部分核心内容；下一次学习应先做短时主动回忆，再补齐矩阵形式、完整计算链、边界 / trade-off 与面试表达，避免机械重复今天已掌握内容。
