# Day 1 — RNN 结构性局限 → 为什么需要 Attention

日期：2026-09-29

## 学习目标

在学习 Q/K/V 实现细节之前，建立“为什么需要 Attention”的因果心智模型。

## 核心结论

1. RNN 并不会在每一步重新读取之前的所有 token。它把当前输入与前一个 hidden state 结合起来。
2. 历史信息必须经过连续的 hidden-state transition 传递，因此长距离依赖具有更长的信息路径。
3. LSTM / GRU 提升了保存有用信息的能力，但 recurrence 与 sequential dependency 仍然存在。
4. Attention 改变了交互模式：一个 token 可以直接从相关位置获取信息，而不需要这些信息经过完整的 recurrent chain。
5. 去除 recurrent dependency 也提高了训练并行度。
6. Attention 并不意味着 sequence length 没有成本；标准 Self-Attention 仍然存在与长度相关的重要计算和内存开销。

## 今天发现的重要区别

### Hidden state

Hidden state 是一个学习得到的向量表示，用于携带之前 recurrent step 的信息。它不是前面文本的逐字副本，也不是一个 ZIP 压缩包。

### 固定 token 重要性 vs 动态相关性

最初的错误模型：每个 token 自己拥有一个固定的 attention weight。

正确方向：Attention relevance 是在当前 context 中、不同 position 之间动态计算出来的。同一个 token 得到的 Attention 可以随着“哪个位置正在查询”以及周围 context 的不同而变化。

### Token embedding vs contextual representation

同一个 token 的两次出现可能从相同的 token embedding 开始。不同 position 和不同 contextual interaction 会使它们后续在 Transformer 中形成不同的 representation。

## 费曼结果

学习者最终的解释已经覆盖所需的因果链：

- 长时间的顺序处理会削弱早期信息的有效利用；
- Attention 缩短了信息交互路径；
- 更早出现的相关信息可以被更直接地使用。

Day 1 最低通过标准：**PASSED**。

## 后续需要复习的缺口

- Hidden state 还需要再次主动回忆 / 复习，达到流畅解释。
- LSTM / GRU 的具体机制尚未学习；当前阶段只需要理解它们相对于 recurrence 的作用。
- 不要把 Attention 描述为“没有 path”。
- 不要把 attention weight 描述为 token 自己固定拥有的值。
- Q/K/V 机制有意留到 Day 2 学习。

---

# Day 2 预习 — Self-Attention 与 Q/K/V

目标时间：20–30 分钟。

## 目标

不要背 Attention 公式。进入 Day 2 时，应能够推理 Q/K/V 所要解决的问题。

## 按以下顺序阅读 / 思考

### 1. 从记忆重建 Day 1 — 3 分钟

不要看笔记，口头回答：

- 为什么长距离信息交互在 RNN 中存在结构性困难？
- LSTM 改善了什么？还有什么结构性限制没有消失？
- Attention 对 information path 做了什么改变？

### 2. 建立输入心智模型 — 5 分钟

只复习这一条 pipeline：

Text → tokenizer → token IDs → token embeddings → positional information → Transformer processing → contextual representations

带着以下问题进入课堂：

- 如果两个相同 token 从相同 embedding 开始，什么信息可以区分它们的角色？
- 为什么只有 token embedding 不足以表达 context 中的含义？

### 3. 建立 Q/K/V 直觉 — 10 分钟

可以使用 information retrieval 类比，但不要把类比当成真实实现：

- Query：我现在正在寻找什么信息？
- Key：这个位置可能匹配 / 提供哪一类信息？
- Value：如果这个位置相关，实际应该向后传递什么信息？

思考为什么“匹配相关性”和“实际传递的内容”可能需要不同的 representation。

示例：

“我有一张银行卡。我又给孩子办了一张卡。昨天孩子发现它不能用了。”

对于“它”对应的位置：

- 它正在尝试解析什么？
- 前面哪些位置应该成为候选？
- 为什么机制应该先判断 relevance，再聚合有用信息？

现在还不需要计算具体数字。

### 4. 可选公式预览 — 最多 5 分钟

可以看一次 scaled dot-product Attention 公式，只需要认识它的结构，不要背公式。

注意观察：

- 哪一部分看起来是在计算 relevance？
- 哪一部分看起来是在携带 content？
- 为什么可能需要 softmax？

Day 3 会详细学习计算过程、scaling、softmax、weighted sum 和 multi-head Attention。

## Day 2 诊断问题

准备在不看笔记的情况下回答：

1. 为什么不直接使用同一个 vector 完成所有事情，而要创建 Q、K、V？
2. Q–K interaction 在概念上完成什么工作？
3. relevance 已经计算完成后，为什么还需要 V？
4. 为什么 Q/K/V 是 learned projection，而不是三份互不相关的文本副本？

这些是诊断题，不是要求完美答案的作业。

## 建议的主要参考资料

选择性阅读 Transformer 论文中的 model / Attention 部分，而不是从头到尾阅读整篇论文。重点关注动机和 scaled dot-product Attention 的定义。可视化解释只作为辅助资料。

## Day 2 通过目标

Day 2 结束时，能够独立解释：

- Self-Attention 试图计算什么；
- Q、K、V 各自的概念角色；
- 为什么 Q/K 决定动态 relevance，而 V 携带需要被聚合的信息；
- 这一机制如何产生依赖 context 的 representation；
- 哪些部分只是类比，哪些部分才是真实的数学机制。
