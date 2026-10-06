# AI Learning Coach — 能力驱动学习方案 V2

修订日期：2026-10-06。状态：本仓库当前课程主线。

## 1. 这次方案解决什么

目标仍是 AI 应用架构师 / Agent 平台高级工程师，不是纯算法研究员。必须能独立解释机制、写出最小实现、定位故障、比较方案并应对面试追问，而不是仅认识 Transformer、RAG、Agent 等术语。

本方案由教练根据仓库旧计划、2026-09-28 Baseline、2026-10-06 对话证据及官方技术资料重新设计。它不是对旧计划的原文摘要，也不代表以下内容已经学完。

- 审计证据：[AUDIT_2026-10-06.md](AUDIT_2026-10-06.md)
- 当前状态与复习：[LEARNING_STATE.md](LEARNING_STATE.md)
- 教学执行规则：[COACH_PROTOCOL.md](COACH_PROTOCOL.md)
- 独立训练机制模块：[M02-training-mechanisms.md](modules/M02-training-mechanisms.md)
- 原有课程单元标准：[DAY_TEMPLATE.md](DAY_TEMPLATE.md)

## 2. 起点：哪些有证据，哪些不能默认

已有记录支持：多年后端和企业系统经验；Agent、Context、Sandbox、安全等工程直觉相对较强；已学习 RNN→Attention、Q/K/V、PE 和 Multi-Head 的若干部分。仓库 Baseline 是历史诊断，不是永久结论。

本轮对话直接支持：能复述 Scaled Dot-Product Attention 主流程；能推导 (1×3)(3×2)=(1×2)；在讲解后能区分 Concat 和 W_O。不能由此推断已稳定掌握一般矩阵运算、反向传播或完整 Multi-Head。

尚待验证：Python/PyTorch 熟练度，概率与导数基础，训练数据与泛化概念，独立实现能力，完整 Transformer/Agent 架构表达。只做针对性诊断，不重做已完成的全套 Baseline，也不把工程年限当成这些技能已掌握的证据。

## 3. 时间与范围

课程以能力模块 M00–M10 为稳定编号，学习会话以 S001、S002 等另行记录。旧 Day 1–5 保留原历史含义，不再临时给同一个 Day 改题。

以下是从当前状态出发的规划估算，不是完成保证：80–106 小时有效学习与实践，预算可取约 80–110 小时。暂按每周约 10 小时作为排程假设，通常需要约 8–11 个学习周，另留复习与中断缓冲；若可用时间不足则延长，不删掉训练或评估来凑 30 天。

30 / 60 / 90 天是检查点，不是自动升级：
- 约 30 天：争取完成基础桥梁、训练机制与微型 Transformer 的第一个训练闭环。
- 约 60 天：争取完成可评测 RAG 和带状态、工具约束的最小 Agent。
- 约 90 天：争取完成可靠性、安全、对照实验与综合答辩。

M00–M04 约 32–44 小时；M05–M08 约 32–40 小时；综合项目与表达约 16–22 小时。已经有证据通过的内容可抵扣；薄弱点复测不通过则增加预算。

## 4. 主线与依赖

推荐顺序：

M00 数学与张量桥梁 → M01 表示与 Attention → M02 神经网络如何学习 → M03 完整 Transformer 与语言建模 → M04 推理与模型适配 → M05 RAG/Context/Memory → M06 Agent runtime → M07 MCP/Harness/Sandbox → M08 评估与企业可靠性 → M09 综合项目。

M10 的表达与间隔复习贯穿全程，并在最后做综合验收。

这里区分“推荐顺序”和“硬性依赖”：写一个调用现成模型的 Agent 不要求先自己训练大模型；不接 Retrieval 的 Agent 也不依赖先完成 RAG。将基础放在前面，是为了当前学习者建立可解释的系统模型，不是在制造通用技术门槛。

三个持续实践成果：
1. P1：微型 decoder-only Transformer，覆盖前向计算、训练、生成和故障定位。
2. P2：可评测的 RAG / 阅读问答系统，作为 LightRAG 项目的对照基线。
3. P3：轻量企业 Agent runtime，接入 P2，并加入工具、状态、安全与评估。

Evaluation 与安全不是最后才出现：M00 开始保存证据，P1 建立训练/验证分离；P2 开始建立固定问题集和权限测试；P3 第一个有副作用的工具上线前就要有授权与幂等设计。M08 是系统深化，不是首次接触。

## 5. 分模块教学与验收

### M00 — 最小数学、张量与实现基础（4–6 小时）

**前置：** 后端编程经验；Python/PyTorch 水平先用小任务诊断，不预设。

**为什么现在学：** 防止把 Projection、shape、概率、梯度变成一串只能复述的名词。

**单元：**
- M00.1：标量、向量、矩阵、张量；batch / sequence / feature 三条轴；形状不等于语义。
- M00.2：点积、矩阵乘法、转置、广播；完整维度加权组合与切片的区别。
- M00.3：概率分布、条件概率、log/exp、均值/方差、Softmax 的归一化轴；微积分留到 M02 正式学习。
- M00.4：最小 Python/PyTorch 张量操作和断言；只补实际需要的语言/框架知识。

**练习与产物：** 手算一次 3→2 线性映射；编写 shape 断言与错误示例；解释 n×n 和 n×d 分别是什么。

**通过：** 对未见过的维度配置独立推导，而不是只会 512/8；能说明一次普通 512→64 线性变换不保证无损保留任意输入。尚未测试的维度仍标待验证。

### M01 — Token、表示与 Attention（4–6 小时，承接已学）

**前置：** M00.1–M00.3。

**为什么学：** 打通文本、数字表示、信息交互之间的关系，补回原计划中被临时 Day 5 覆盖的 Token/Embedding 内容。

**单元：**
- M01.1：tokenizer、子词直觉、vocabulary、token ID、embedding lookup；Embedding 与 contextual representation；模型内 token embedding 与检索用文本 embedding 的区别。
- M01.2：RNN/LSTM 到 Attention 的动机；已学内容采用新情境诊断，非整课重讲。
- M01.3：Q/K/V、score、scaling、Softmax、weighted sum；批量 shape；causal/padding mask 的动机。
- M01.4：位置表示、固定 sinusoidal 与 learned PE；多频率和 sin/cos 的适用边界；RoPE 先列入 M04 比较。
- M01.5：Multi-Head 独立投影、Concat、W_O；多视角的可能性而非必然语义分工；head width 是设计选择，不是数学定律。

**练习与产物：** 独立实现一个带 mask 的 attention 函数和一个小型 multi-head 层；写 shape、mask、Softmax 行和测试。允许使用基础张量/autograd，不直接调用完整 Transformer 层替代学习。

**通过：** 能从 X 到 Q/K/V、attention weights、head output、Concat、W_O 连续推导；解释维度切分与 token 切分的差别；通过一个更换 n/head 数的迁移题和一个遮挡未来信息的测试。

**当前衔接：** 今天不强制完成 Day 5 复述。下次先补 M00 必要桥梁与 Token 表示，再对 MHA 只做尚未验证的部分。

### M02 — 神经网络如何学习（10–14 小时，正式独立模块）

**前置：** M00；M01 的向量表示直觉。理解链式法则不要求先学完整 Transformer。

**学习链路：** 训练样本/目标 → 可学习参数与超参数 → prediction/Loss → 导数与梯度 → 链式法则 → 计算图与反向传播 → SGD/学习率 → Adam/AdamW 的工程直觉 → batch/epoch/step → 分类 Softmax/交叉熵 → 训练/验证与过拟合 → 映射回 W_Q/W_K/W_V/W_O。

**单元与练习：** 见独立模块的 T01–T08。不是把这些名词塞进一堂课；每个单元都有前置、手算或实验、无提示验收、未通过的回补动作。

**产物：** 单参数与双参数手算记录；数值梯度检查；最小 PyTorch 训练循环；一份 Transformer 参数梯度追踪记录。

**通过：** 独立解释 backprop 计算梯度与 optimizer 更新参数的区别；对简单网络算出一次更新；能用最终 Loss 说明 Head 与 W_O 为什么可以联合训练；区分“一次更新”和“训练完成”；定位至少一个训练错误。

### M03 — 完整 Transformer 与语言建模闭环（8–10 小时）

**前置：** M01、M02。

**为什么学：** Attention 层不是完整模型；理解架构要同时看数据、预测目标和训练路径。

**单元：**
- M03.1：FFN、非线性与逐 token 变换；为何不只堆线性层。
- M03.2：Residual、LayerNorm/RMSNorm 的直觉；Pre-LN/Post-LN 的区别；先掌握结构，不要求证明全部稳定性结论。
- M03.3：Encoder-only、decoder-only、encoder-decoder；self-attention 与 cross-attention；双向与 causal mask。
- M03.4：hidden states → LM head → vocabulary logits；Attention Softmax 与 vocabulary Softmax 的对象和轴不同。
- M03.5：next-token labels 的移位、teacher forcing、padding/ignore mask、交叉熵；训练可并行预测多个位置和生成逐步进行的区别。
- M03.6：从 tokenizer、batch 到 forward、Loss、backward、optimizer、验证、checkpoint、生成的完整闭环。

**产物 P1：** 1–2 层、可配置小维度的教学 decoder LM；先用合成或有授权的小语料做 CPU 级正确性实验，设备与算力预算待实际确认。不以流畅文本或训练大模型为验收目标。

**通过：** 能在小训练集上验证学习发生，同时保留独立验证集；打印并解释每层 shape；未来 token 改动不影响不应看见它的预测；能保存/恢复、生成，并解释过拟合不等于泛化。

### M04 — 推理、性能与模型适配（6–8 小时）

**前置：** M03。

**单元：**
- M04.1：推理通常不更新模型权重；prompt、context、memory 与参数学习的区别；结构化输出及其验证。
- M04.2：greedy、temperature、Top-K/Top-P、停止条件；生成随机性和可复现记录。
- M04.3：prefill/decode、KV cache、TTFT/每 token 延迟、batching、上下文长度/显存；MHA/MQA/GQA 与 RoPE 的工程比较。
- M04.4：量化、FlashAttention、服务并发的基本收益与边界；不要求手写 GPU kernel。
- M04.5：pretraining、SFT、LoRA/PEFT、偏好优化/RLHF/DPO 的目标与边界；Prompt vs RAG vs 微调的选型。不把微调当作可靠实时知识库，也不把所有对齐算法当作必修实现。

**产物：** P1 的带/不带 cache 正确性对照，或资源允许时一次小规模推理测量；一份 Prompt/RAG/微调决策记录。所有性能结论记录环境、长度、batch、版本，不凭感觉写加速倍数。

**通过：** 对“训练并行而生成为何逐 token”“cache 保存什么”“什么时候该微调”分别解释机制与边界。

### M05 — RAG、Context 与 Memory（10–12 小时）

**前置：** M00 的相似度/概率直觉、M01 的表示、M03 的输入输出；M04.1 的模型调用边界。

**单元：**
- M05.1：用户问题、证据需求、离线 ingestion 与在线 retrieval；解析、文档身份、版本、来源、删除/更新、chunk 信息边界。
- M05.2：检索 embedding 的训练目标/使用方式；距离与归一化；sparse/dense/hybrid、ANN 与过滤；embedding 版本迁移。
- M05.3：query 改写、reranking、recall/precision、Top-K、召回失败与生成失败分开定位。
- M05.4：context budget、结构与顺序、压缩损失、来源引用、无答案/矛盾证据；ACL 和 prompt injection 测试从这里开始。
- M05.5：conversation history、context window、working/episodic/semantic memory；写入策略、检索、冲突、TTL、隐私与删除。
- M05.6：GraphRAG/LightRAG 的实体、关系、全局/局部检索直觉；与普通 RAG 对照，核对实际项目版本后再讲实现，不预设图方案更好。

**产物 P2：** 选一个用户授权的数据域，建立最小 RAG、版本化小问题集和分层指标。起步可用 20–40 个覆盖明确的教学用例，不把这个数量当成统计充分性的保证。

**通过：** 固定数据和问题，对照检索策略与 chunk 方案；能把错误归于解析、召回、排序、组装或生成；验证无证据拒答、引用可回溯、权限隔离。能说明 LightRAG 在什么问题上值得增加复杂度，而不是凭概念选择它。

### M06 — Agent Loop 与可靠工具执行（8–10 小时）

**前置：** M04.1 与已有后端基础；接 Retrieval 工具时再依赖 M05。

**单元：**
- M06.1：单次 LLM、固定 workflow、Agent 的控制流区别；先做最简单足够方案。
- M06.2：messages、model response、tool request、执行结果、状态更新、终止条件；模型提出调用不等于执行器已经执行。
- M06.3：tool schema、参数验证、typed error、权限/人工批准；高风险写操作默认禁用或使用 mock。
- M06.4：planning/routing、task state、checkpoint/resume；可恢复执行与恰好一次副作用的区别。
- M06.5：timeout、retry、backoff、idempotency key、取消、并发、补偿、步数/token/费用预算。
- M06.6：反思、多 Agent 的收益/代价和适用条件；先以单 Agent 或固定 workflow 为基线，复杂化必须有评测证据。

**产物 P3 第一版：** 不用完整编排框架隐藏核心循环，完成至少一条带工具、状态、终止与错误路径的流程。真实 provider 可替换为 deterministic fake，故障测试优先使用 fake/mock。

**通过：** 正确处理非法参数、超时、重复回调、进程重启、预算耗尽；证明测试中的写操作不会因简单重试而重复；能解释模型错误与 runtime 错误分别由谁处理。

### M07 — MCP、Harness 与 Sandbox（6–8 小时）

**前置：** M06；已有安全经验只作可用背景，不免除边界验证。

**单元：**
- M07.1：MCP host/client/server、tools/resources/prompts、能力协商和连接/请求边界；协议规范与 SDK 版本配套核验。
- M07.2：transport、身份/授权、用户同意、凭证边界；协议标准化不自动等于业务授权或安全隔离。
- M07.3：Harness 在本项目中明确定义为围绕模型的工具、context、执行、恢复、预算与评估支撑层；区分 model、SDK、协议、runtime、sandbox。
- M07.4：Sandbox threat model、文件/进程/网络权限、资源限制、生命周期、artifact 管理；容器与 microVM 的选择由威胁与运维要求决定，不要求自建虚拟化基础设施。

**产物：** 用维护中的 MCP SDK 给一个已有工具增加协议适配；画出信任边界；在受控测试中验证拒绝越权访问、取消与资源清理。

**版本规则：** 2026-10-06 核验时官方 latest 指向 2026-07-28。正式实施时重新核对并在实验中固定规范/SDK/transport 版本，不能把旧版流程默认为所有版本都一样。

**通过：** 能解释 MCP 没有替代哪些 runtime/security 职责；能追踪一次调用跨越的身份、策略和执行边界。

### M08 — Evaluation、可靠性与企业架构（8–10 小时）

**前置：** P2/P3 的最小实现和早期测试。

**单元：**
- M08.1：observability、testing、evaluation 的区别；dataset、task、trial、grader、trace、最终环境状态。
- M08.2：code/model/human grader，人工校准、judge 偏差；重复试验、不确定性、数据泄漏与测试集污染。
- M08.3：离线回归、能力评估、在线监测、A/B 适用条件；RAG 分层评估和 Agent outcome/trajectory 双维度评估。
- M08.4：tenant identity、IAM、secret、data/cache/index/checkpoint/log 隔离；不信任检索文档中的指令。
- M08.5：model gateway、路由/fallback、限流、超时、成本预算、SLO、审计、版本变更与回滚。

**产物：** 可重复的评估命令、固定配置和报告；最小 threat model 与故障注入矩阵。模型质量测试和权限/副作用确定性测试分开。

**通过：** 对更换模型、prompt、retriever 或 framework 的影响给出数据和失败案例；区分“这组安全测试全部通过”和“已经证明系统绝对安全”。

### M09 — 综合项目与架构答辩（12–16 小时）

**前置：** M05–M08 的阶段通过；可复用前面产物，不另起一个重复项目。

**场景：** 企业文档/书籍问答与受控任务执行 Agent。项目资料未提供前，不声称已检查真实平台或 LightRAG 源码。

**交付：**
- 可运行入口、配置和版本锁定、测试、评估数据与报告、成本/延迟测量、失败案例。
- 架构图的文字或图形表示、信任边界、至少三份 ADR：检索策略、状态/副作用、runtime/framework 选择。
- 在相同任务和测试上，选一个当前仍受维护的编排框架做小范围对照；选型时核验官方文档，不并行学习三个框架 API。
- runbook：失败如何诊断、恢复、停止、回滚和审计。

**通过：** 接受一次需求变化、一次越权诱导和一次执行中断，解释并实现合理处理；以证据说明为何不是更复杂或更简单的架构。没有真实测试证据的能力不得写为已完成。

### M10 — 独立表达与延迟验证（4–6 小时，贯穿）

每模块安排独立机制解释、一个未见过的迁移问题、一个边界追问；面试模式一次一个问题，不先给答案。

阶段末做 Transformer、RAG、Agent 三类完整答辩，记录技术正确性、机制、工程、trade-off、表达。最后基线与最初 Baseline 对比，不能凭“说得流畅”升级掌握状态。

## 6. 训练机制为什么必须是完整模块

它不是关于 W_O 的临时补丁。FFN、embedding、LM head、微调与模型训练都依赖“目标函数如何通过可微计算图指导参数更新”的共同基础。

学习路径先用小网络暴露基本问题，再引入必要微积分和 autograd，最后映射回实际 Transformer。先掌握计算过程，再学习 API。具体见 M02，不在 MHA 课末用几句“端到端训练”替代整个模块。

## 7. 统一验收与回补

每个学习单元的状态只能是：未开始 / 已接触 / 提示后能解释 / 独立通过 / 延迟通过 / 需回补。

“可以接受”或紧接讲解复述，只能证明当下理解的线索，不等于独立通过。一个 shape 题正确不能代表整个矩阵基础通过。

评估分别记录 Concept、Mechanism、Engineering、Interview。尚未测试写待验证；不为显得精确而补造分数。

独立通过至少需要：无提示解释核心因果链；完成该单元指定的推导/代码/工程任务；处理一个边界或新配置。延迟通过另需隔开后再测。失败时只回补失败依赖，不把整章从头重讲。

间隔沿用项目规则：评分确有证据时，9–10 约 30 天、7–8 约 7 天、5–6 约 3 天、0–4 下一次优先回补；没有有效评分就记录明确的下次检查条件，不虚构数字。

## 8. 哪些必须深入，哪些留作扩展

**必须独立推导/实现：** 基本 shape 与线性映射、Attention、一个完整微型模型训练循环、检索评测、工具/状态/恢复逻辑、权限和预算测试。

**必须能解释和选型：** RoPE、GQA/KV cache、量化、LoRA/PEFT、SFT/偏好优化、GraphRAG、MCP、Sandbox、framework trade-off。

**本轮非必修：** 手写 FlashAttention GPU kernel、多机训练、完整 PPO/DPO 推导、MoE 训练系统、自建 microVM、追逐所有新框架。后续岗位或项目需要时再增设独立模块。

## 9. 接下来从哪里重新开始

不要求现在补交 Day 5 复述。恢复学习时按照 LEARNING_STATE 中的入口：
1. 用未见过的输入做短诊断，确认矩阵乘法、线性投影与 token/feature 轴。
2. 回补缺项，确认 Token/Embedding 与 contextual representation；已稳定内容跳过重复教学。
3. 对 MHA 做一次整条链路的独立验证；提示依赖的部分保持待复测。
4. 正式进入 M02；达到训练基础门槛后，再学习完整 block 和 tiny LM。

## 10. 资料依据与使用边界

以下用于核对课程覆盖和技术机制，不是要求完整照搬外部课程；模块顺序、工作量和验收为本项目的新设计。访问核验日期：2026-10-06。

- [R1] Stanford CS336（2025 存档）：https://cs336.stanford.edu/spring2025/index.html 。用其 tokenizer、模型、optimizer、训练、数据、评估的覆盖作检查，并注意其已有数学/ML/PyTorch 前置要求，不能原封不动用于当前起点。
- [R2] PyTorch Autograd：https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html 。用于反向传播和计算图的机制核对。
- [R3] Hugging Face causal LM 训练课程：https://huggingface.co/learn/llm-course/chapter7/6 。用于语言建模训练闭环的覆盖检查。
- [R4] Anthropic Building effective agents：https://www.anthropic.com/engineering/building-effective-agents 。用于 workflow/agent、简单模式、工具接口与复杂度权衡；页面含后续更新，不将文中工具清单视为永久推荐。
- [R5] Anthropic Demystifying evals for AI agents：https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents 。用于任务、试验、grader、结果状态与早期评估设计。
- [R6] MCP Specification：https://modelcontextprotocol.io/specification/2026-07-28 。用于协议与信任边界；实施前复核版本。

## 11. 文档与代码完成边界

本次完成的是课程审计、总方案、独立训练模块、学习状态与执行规则。各未来单元的完整讲义、实验代码和测试结果在本次修订时尚未产生，不能声称已有可运行项目。

每个正式单元开课前必须依据 DAY_TEMPLATE 准备可独立学习的讲义、练习、错误模型和验收；先检查前置缺口，不能等学习者在课堂上发现后才补计划。已有 day-01 文件和 Baseline 保留，不冒充今日重新验证的成果。
