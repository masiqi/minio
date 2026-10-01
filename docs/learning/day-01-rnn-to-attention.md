# Day 1 — RNN 结构性局限 → 为什么需要 Attention

日期：2026-09-29  
阶段：30-Day Phase 1 / Week 1 — LLM 心智模型

## 1. 今日定位：为什么第一天先学这个

Day 1 不直接从 Attention 公式或 Q/K/V 开始，而是先回答一个更重要的问题：

> **为什么序列模型需要从 RNN / LSTM 进一步走向 Attention？**

如果不知道旧方案的问题，Q/K/V、Self-Attention、Multi-Head Attention 很容易变成需要背诵的术语。

今天的目标是建立一条因果链：

**序列建模需求 → RNN 的 recurrent information path → 长距离依赖困难 → LSTM/GRU 的改进及边界 → Attention 改变信息交互方式 → Transformer 的后续设计动机。**

这条因果链是 Day 2 学习 Self-Attention 与 Q/K/V 的前置心智模型。

---

## 2. 前置知识

### 开始前需要知道

只需要具备以下直觉：

- 文本可以被拆成 token；
- 模型需要结合上下文理解当前 token；
- 一个 token 的含义可能依赖很远之前的信息。

### 今天暂时不要求掌握

- LSTM gate 的具体公式；
- Q/K/V 数学计算；
- scaled dot-product Attention；
- softmax 细节；
- Multi-Head Attention；
- Transformer block 的完整结构。

这些内容会在后续 Day 中逐步学习。

---

## 3. 今日学习目标

完成 Day 1 后，应当能够在**不看笔记**的情况下：

1. 解释 RNN 如何利用当前输入和 previous hidden state 处理序列；
2. 解释为什么远距离信息在 RNN 中需要经过较长的 sequential path；
3. 说明 LSTM / GRU 改善了什么，以及它们没有改变什么；
4. 解释 Attention 如何改变 token 之间的信息交互路径；
5. 说明 Attention 为什么有利于训练并行化；
6. 指出“Attention 没有路径 / 序列长度没有成本 / token 有固定 Attention weight”等说法的问题；
7. 用 2–3 分钟形成一段结构化的面试回答。

---

## 4. 问题从哪里来：序列中的远距离依赖

自然语言不是只依赖相邻词。

例如：

> The animal didn't cross the street because **it** was too tired.

要理解 `it` 指什么，模型需要利用前面出现的信息。

更长的文档中，当前 token 可能依赖几十、几百甚至更多位置之前的信息。

因此一个核心问题是：

> **当前位置如何高效地获取之前真正相关的信息？**

---

## 5. RNN 的核心心智模型

### 5.1 RNN 并不是每一步重新阅读全部历史

一个常见错误理解是：

> RNN 处理当前 token 时，会重新读取前面所有 token。

更准确的模型是：

```text
x1 → h1
      ↓
x2 → h2
      ↓
x3 → h3
      ↓
x4 → h4
```

在时间步 `t`，可以用一个抽象表达理解：

```text
h_t = f(x_t, h_{t-1})
```

其中：

- `x_t`：当前输入；
- `h_{t-1}`：之前步骤形成的 hidden state；
- `h_t`：融合当前输入和历史信息后的新 hidden state。

这里不需要记公式，关键是理解：

> **历史信息主要通过 hidden state 沿着 recurrent chain 向后传递。**

### 5.2 Hidden state 到底是什么

Hidden state 是模型学习得到的向量 representation。

它不是：

- 前面所有文字的原样复制；
- 一个数据库；
- 一个 ZIP 压缩包；
- 可以无损恢复全部历史的存储。

更合适的直觉是：

> 它是模型在当前步骤认为有用的历史信息 representation，并继续参与下一步计算。

---

## 6. 为什么长距离依赖困难

假设第 100 个位置需要利用第 2 个位置的信息。

在 recurrent 模型中，这份信息需要经过类似：

```text
h2 → h3 → h4 → ... → h99 → h100
```

这意味着两个问题。

### 6.1 信息路径很长

早期信息需要经过很多次 state transition 才能影响后面的位置。

因此距离越远，模型越难稳定地保留和利用相关信息。

### 6.2 训练存在 sequential dependency

计算 `h_t` 依赖 `h_{t-1}`。

所以：

```text
h1 完成
  ↓
才能计算 h2
  ↓
才能计算 h3
  ↓
...
```

这种 recurrence 限制了训练阶段跨 sequence position 的并行化。

### 今天真正需要记住的不是一句“RNN 会遗忘”

更准确的因果关系是：

> **RNN 的历史信息沿 recurrent path 顺序传递。距离越远，信息需要经历的连续状态转换越多；同时这种前后依赖限制了训练并行性。**

---

## 7. LSTM / GRU 改善了什么

LSTM / GRU 的重要价值是：

> 改善 recurrent path 上的信息保存和梯度传播，让模型更容易保留长期有用信息。

但是今天需要特别区分：

### 它们改善了

- 哪些信息应该保留；
- 哪些信息应该更新或遗忘；
- 长期依赖的学习能力。

### 它们没有消除

```text
h1 → h2 → h3 → ... → hn
```

也就是说：

> **LSTM / GRU 改善了 recurrent path 上的信息传递，但没有移除 recurrent sequential path 本身。**

这正是理解 Attention 动机的重要桥梁。

---

## 8. Attention 改变了什么

Attention 的关键变化不是简单地说“它记忆力更强”。

它改变的是**信息交互模式**。

RNN 的直觉：

```text
token 1 → token 2 → token 3 → ... → token n
```

如果 token n 需要 token 1 的信息，这份信息需要沿 chain 逐步传递。

Attention 的直觉：

```text
当前位置
 ├── 关注 position 1
 ├── 关注 position 4
 ├── 关注 position 8
 └── ...
```

当前位置可以根据相关性直接聚合其他位置的信息。

因此：

> Attention 为不同位置之间提供了更直接的信息交互方式，不再要求相关信息必须沿完整 recurrent chain 逐步传递。

这就是 Day 1 最核心的机制变化。

---

## 9. 为什么这也改善训练并行化

RNN 的 recurrence 要求前一步 state 先产生。

Self-Attention 在训练时可以对一个 sequence 中多个位置的表示进行矩阵化计算，因此能够获得更高程度的并行化。

但必须保留一个边界：

> **并行化更好 ≠ 计算免费。**

标准 Self-Attention 的计算和 memory cost 会随 sequence length 显著增长。后续学习 Attention computation 时再具体讨论复杂度。

---

## 10. 今天必须区分的三个概念

### 10.1 Hidden state vs 完整历史

错误：

> Hidden state 保存了之前全部文本。

正确：

> Hidden state 是学习得到的 representation，历史信息通过它沿 recurrent steps 传播，但它不是历史文本的无损副本。

### 10.2 固定 token 重要性 vs 动态 relevance

错误：

> 每个 token 自己有一个固定 Attention weight。

正确：

> Attention relevance 取决于当前查询位置和 context，是位置之间动态计算的关系。

同一个 token 在不同 context、面对不同 querying position 时，可以产生不同的 relevance。

Day 2 会用 Q/K/V 解释“动态 relevance 到底如何计算”。

### 10.3 Token embedding vs contextual representation

Token embedding 可以理解为 token 进入模型时的初始 representation。

但真正经过 Transformer 后的 representation 会受到：

- position；
- surrounding context；
- Attention interaction

等因素影响。

因此：

> 两个相同 token 可以从相同或相近的 token embedding 出发，却因为上下文不同形成不同的 contextual representation。

---

## 11. 常见错误模型

### 错误 1：RNN 每一步都会重新读取所有历史 token

问题：忽略了 recurrent hidden state 的作用。

正确模型：当前输入与 previous hidden state 共同形成新的 hidden state。

### 错误 2：LSTM 已经解决了 RNN 的所有问题

问题：LSTM 改善长期信息保存，但 recurrence 仍存在。

### 错误 3：Attention 完全“没有路径”

问题：Attention 仍然存在计算图和信息交互结构。

更准确的表达：

> Attention 缩短了不同 sequence position 之间的信息交互路径。

### 错误 4：Attention 让 sequence length 不再有成本

错误。标准 Self-Attention 对长 sequence 有明显计算和 memory 成本。

### 错误 5：Attention weight 是 token 固定属性

错误。它是根据当前 context 和 position-to-position relevance 动态计算的。

---

## 12. 工程映射

今天的概念可以连接到你熟悉的 Context / Retrieval，但只能作为工程直觉，不能把它们当成同一种机制。

例如在 RAG 中：

```text
query
  ↓
retrieval
  ↓
选择相关 chunk
  ↓
组装 context
```

它和 Attention 有一个抽象层面的共同问题：

> 当前任务真正需要哪些信息？

但两者机制不同：

- Retrieval 通常是在模型外选择候选信息；
- Self-Attention 是模型内部 representation 之间的动态交互机制。

这个区别后续学习 RAG / Context Engineering 时会再次使用。

---

## 13. 主动练习

### Exercise 1 — 不看笔记解释 RNN

用 60 秒回答：

> RNN 在处理第 t 个 token 时，之前的信息从哪里来？

答案必须提到：

- current input；
- previous hidden state；
- recurrent state transition。

### Exercise 2 — 信息路径

画出：

```text
token 1 → token 2 → token 3 → token 4 → token 5
```

然后回答：

> 如果 token 5 需要 token 1 的信息，在 RNN 中这份信息经历了什么？

### Exercise 3 — LSTM 边界

回答：

> LSTM 改善了长期依赖，为什么还会出现 Attention？

如果只能回答“Attention 更先进”，说明还没有掌握。

### Exercise 4 — Attention 的变化

禁止使用“Attention 就是注意重要的词”这句话。

用 information path 的角度解释 Attention。

---

## 14. 费曼验证

不看文档，用自己的话完成以下解释：

> “为什么从 RNN / LSTM 的结构会自然引出 Attention？”

推荐结构：

1. RNN 如何处理 sequence；
2. 长距离 dependency 为什么困难；
3. LSTM / GRU 改善什么；
4. 哪个结构性问题仍存在；
5. Attention 改变什么；
6. 带来什么收益和新的成本。

目标时间：2–3 分钟。

---

## 15. 追问验证

只有能够应对下面的追问，才说明理解不是停留在口号：

### 追问 1

> 如果 LSTM 能够保留长期信息，为什么还需要 Attention？

### 追问 2

> Attention 是否意味着任意两个 token 之间的信息传递完全没有成本？

### 追问 3

> 为什么说 Attention weight 不是一个 token 固定拥有的属性？

---

## 16. Day 1 达标标准（Acceptance Criteria）

### Concept

能够准确说明：

- RNN；
- hidden state；
- long-range dependency；
- Attention

之间的关系。

### Mechanism

能够独立解释：

```text
recurrent sequential path
        ↓
long-distance information path
        ↓
LSTM/GRU improve preservation
        ↓
recurrence still exists
        ↓
Attention changes interaction pattern
```

不能只背“Attention 解决长距离依赖”。

### Engineering

能够说明：

- recurrence 为什么限制训练并行化；
- Attention 为什么提高 parallelism；
- Attention 并不意味着 sequence length 没有计算成本。

### Interview Expression

不看笔记，用 2–3 分钟回答：

> 为什么 Transformer / Attention 相比传统 RNN 更适合处理长距离依赖？

并能够接受至少一个追问。

### 最低通过条件

以下三项同时满足才算通过：

- 独立费曼解释基本正确；
- 1–3 个追问没有暴露核心因果链错误；
- 能指出至少一个 Attention 的边界或 trade-off。

---

## 17. 当天实际学习结果

### 已经建立的理解

当天最终解释已经覆盖：

- 长时间 sequential processing 会降低早期信息被有效利用的能力；
- Attention 缩短不同位置的信息交互路径；
- 相关的早期信息可以被更直接地使用。

因此 Day 1 的最低机制目标：**PASSED**。

### 当天暴露并纠正的问题

1. **Hidden state 不够清晰**
   - 需要再次主动回忆，直到可以流畅解释。

2. **曾把 Attention weight 理解为 token 固定重要性**
   - 已纠正为 position-to-position 的动态 relevance。

3. **Token embedding 与 contextual representation 仍需继续区分**
   - 这是后续 Transformer 心智模型的重要基础。

4. **Attention 的边界表达需要保持准确**
   - 不说“没有 path”；
   - 不说 sequence length 没有成本。

### 尚未学习

- Q/K/V 的真实机制；
- Attention score 的计算；
- scaling；
- softmax；
- weighted sum；
- Multi-Head Attention。

这些不属于 Day 1 的通过要求。

---

## 18. 复习计划

Day 2 开始前进行一次短复习。

不看笔记回答：

1. Hidden state 是什么？
2. 为什么 RNN 的 long-range dependency 存在结构性困难？
3. LSTM 改善什么、没有改变什么？
4. Attention 对 information path 做了什么？

如果第 2 或第 3 题无法清晰回答，应先修复 Day 1 心智模型，再进入 Q/K/V。

---

## 19. 与 Day 2 的衔接

Day 1 回答的是：

> **为什么需要一种新的信息交互方式？**

Day 2 要回答的是：

> **Self-Attention 如何动态判断“当前位置应该从哪些位置获取什么信息”？**

这会自然引出三个角色：

- Query；
- Key；
- Value。

下一步不是背 Q/K/V 定义，而是理解：

> 为什么“寻找什么”“如何匹配”“真正传递什么内容”需要不同的 learned projection。

---

# Day 2 预习 — Self-Attention 与 Q/K/V

目标时间：20–30 分钟。

1. 不看笔记，用一分钟重建 Day 1 的因果链。
2. 回顾：Text → tokenizer → token IDs → token embeddings → positional information → Transformer → contextual representations。
3. 思考为什么“匹配 relevance”和“传递 content”可能需要不同 representation。
4. 可以看一次 scaled dot-product Attention 公式，但不要背。

Day 2 入场问题：

> 为什么不直接使用同一个 vector 完成所有事情，而需要 Q、K、V？
