# AI Learning Coach — 72 个学习日执行计划

版本：2026-10-06。状态：72 个学习日的教学任务书已预先建立；未发生的教学、代码实现和测试结果不标完成。

## 1. 这份计划怎样使用

目标是 AI 应用架构师 / Agent 平台高级工程师。Transformer 只是能力链中的一段；路线同时覆盖数学与训练基础、模型使用、RAG、Context/Memory、Agent runtime、MCP/Harness/Sandbox、评估、安全、企业架构和独立表达。

这份逐日计划承接 [CURRICULUM_V2](CURRICULUM_V2.md)，不是另起一套互相竞争的章节；模块仍用 M00–M10。历史 Day 1–5 保留原始记录，新的 L001–L072 是学习任务编号，不替换历史日期或学习结果。

**先迁移证据，再决定从哪一课进入。** 用户已学过的 Q/K/V、PE、MHA 不清零；能独立通过的部分跳过讲授，只保留必要迁移题。前置缺口在计划里已有落点，不靠学生临时发现。现状见 [LEARNING_STATE](LEARNING_STATE.md)，授课规则见 [COACH_PROTOCOL](COACH_PROTOCOL.md)。

## 2. 学习量与日历不是一回事

一个学习日默认是一张任务卡，可分成多个短会话。暂按普通卡 60–90 分钟、综合实验卡 90–120 分钟安排；这是排程假设，不是用户已确认可用时间，也不是完成保证。按本次逐日拆分，准备约 80–120 小时有效学习与实验预算；前置回补、环境问题与复习可能额外延长。

若每周学习约 6 天，72 张卡约对应 12 周的主体安排，另留缓冲；频次与时长不足则延长，不删除训练或评估来凑 30/60/90 天。30/60/90 天只做阶段检查，不自动宣布通过。先前已掌握内容可抵扣；卡中的复杂任务未完成时拆为子会话，不追求一天塞完。

每次默认先做到期主动回忆，再教学与算例，接着独立练习，最后用未见过的条件验证并记录。完整的讲解按问答动态展开，不能一次把整章内容倒给学习者。

## 3. 章节、学习日与产物

| 模块 | 学习日 | 章节主线 | 必须留下的证据 |
| --- | --- | --- | --- |
| M00 | L001–L004 | 数学、张量与实现桥梁 | 新 shape 推导、线性映射手算、基础测试 |
| M01 | L005–L010 | Token、Embedding、Attention、PE、MHA | 带 mask 的 attention/MHA 实现、全链解释 |
| M02 | L011–L020 | 数据、Loss、导数、反传、优化与泛化 | 手算/数值梯度、训练脚本、Head/W_O 梯度追踪 |
| M03 | L021–L028 | FFN、Residual、Norm、模型架构与语言建模 | P1：微型 Transformer 的训练、恢复、生成与排错 |
| M04 | L029–L034 | Prompt、推理、采样、缓存、性能与适配 | 可验证调用、cache 对照、Prompt/RAG/微调选型 |
| M05 | L035–L044 | RAG、索引、Context、Memory、GraphRAG | P2：带题集、权限、引用、更新删除的 RAG |
| M06 | L045–L053 | Agent loop、工具、状态、恢复与预算 | P3：可靠 runtime、幂等与故障注入证据 |
| M07 | L054–L058 | MCP、Harness、Sandbox 与信任边界 | 协议适配、身份路径、隔离与清理测试 |
| M08 | L059–L064 | Evaluation、Observability、安全与发布 | 校准过的评估、回归门槛、成本/可靠性方案 |
| M09 | L065–L070 | 综合工程项目与框架取舍 | 可复现入口、ADR、测试报告、runbook |
| M10 | L071–L072，且贯穿 | 独立答辩、延迟验证与下一阶段 | 无提示新题、四维证据、re-baseline |

### 依赖与并行边界

M00 是数学/实现桥梁；M01 支持 Attention 实现；M02 支持训练理解；M01+M02 支持 M03；M03 支持深入推理和适配。写一个调用现成模型的 Agent 并不要求先训练大模型；把基础放前是当前学习者的教学顺序，而非通用技术门槛。

M05 与 M06 可在相关前置通过后部分并行；Agent 只有接 Retrieval 工具时才依赖 P2。M07 依赖可解释的 runtime；M08 的早期评估/权限要求从 L035/L045 已开始；M09 复用前期项目。M10 每个模块都练，最后才做综合验收。

## 4. 全部学习日速查

### 第一册：[L001–L020：数学、Attention 与训练](daily/L001-L020.md)

| 编号 | 每天的主题 |
| --- | --- |
| L001 | batch/token/feature 轴与最小编程诊断 |
| L002 | 点积、矩阵乘法与线性投影，不是分组压缩 |
| L003 | 概率、log/exp、Softmax 与归一化轴 |
| L004 | 批量 shape、广播、reshape/transpose 与入场门槛 |
| L005 | Tokenizer、token ID、embedding lookup 与上下文表示 |
| L006 | RNN→Attention 与 Q/K/V 的新例验证 |
| L007 | Scaled Dot-Product Attention 手算与实现 |
| L008 | 位置编码、causal/padding mask 与顺序边界 |
| L009 | 多头独立投影与向量化实现 |
| L010 | Concat、W_O 与 MHA 全链验收 |
| L011 | 训练数据、目标、参数和 Loss |
| L012 | 导数、梯度、有限差分与更新方向 |
| L013 | 链式法则与两层参数联合更新 |
| L014 | 分叉计算图、多路径梯度与反向传播 |
| L015 | Y=XW 的矩阵梯度与数值检查 |
| L016 | Autograd、SGD 与最小训练循环 |
| L017 | Batch/step/epoch、学习率、优化器与恢复状态 |
| L018 | Logits、交叉熵、数据划分、过拟合与泛化 |
| L019 | 回到 Transformer：Head 与 W_O 如何一起学 |
| L020 | 训练机制完整答辩与故障定位 |

训练模块细化了原 [M02 的 T01–T08](modules/M02-training-mechanisms.md)，不再用几分钟支线代替。

### 第二册：[L021–L034：完整 Transformer 与推理](daily/L021-L034.md)

| 编号 | 每天的主题 |
| --- | --- |
| L021 | FFN、非线性与逐 token 变换 |
| L022 | Residual、Normalization、Dropout 与训练状态 |
| L023 | Encoder/Decoder/Cross-Attention 与信息可见性 |
| L024 | LM head、词表 logits、label shift 与预测目标 |
| L025 | 语言模型数据、清洗划分与可复现 loader |
| L026 | 微型 Decoder LM 的完整 forward |
| L027 | 训练、验证、checkpoint、恢复与生成 |
| L028 | P1：完整模型的实现、因果与排错验收 |
| L029 | 模型调用、Prompt、结构化输出与业务校验 |
| L030 | Greedy、temperature、Top-K/Top-P 与停止条件 |
| L031 | Prefill/decode、KV cache 与一致性对照 |
| L032 | RoPE、MHA/MQA/GQA、量化、FlashAttention 与资源账本 |
| L033 | Pretraining、SFT、LoRA/PEFT 与偏好优化边界 |
| L034 | Prompt/RAG/微调、部署与成本选型 |

L032–L033 是机制和选型课；本轮不要求一天实现所有现代 kernel 或完整 RLHF。

### 第三册：[L035–L053：RAG 与 Agent](daily/L035-L053.md)

| 编号 | 每天的主题 |
| --- | --- |
| L035 | RAG 目标、证据、评估题集与最小基线 |
| L036 | Parsing、chunking、表格/结构与来源追踪 |
| L037 | Retrieval embedding、余弦/点积与精确检索 |
| L038 | ANN、ACL、索引版本、更新删除与迁移 |
| L039 | Sparse/dense/hybrid 与候选召回 |
| L040 | Reranking、query rewrite 与分层诊断 |
| L041 | Context 预算、压缩、证据引用和拒答 |
| L042 | Memory、任务状态、冲突、时效与删除 |
| L043 | GraphRAG/LightRAG 与普通 RAG 的证据化比较 |
| L044 | P2：质量、权限、更新与引用验收 |
| L045 | LLM、Workflow、Agent 的任务与风险边界 |
| L046 | Model/tool/runtime 分离的最小 Agent loop |
| L047 | Tool schema、服务端校验、身份和授权 |
| L048 | Timeout、retry、幂等与未知结果 |
| L049 | Checkpoint、resume、持久化与外部副作用 |
| L050 | Planning/routing、Context Router、预算和取消 |
| L051 | Human approval、prompt injection 与执行边界 |
| L052 | Reflection、multi-agent 与复杂度对照 |
| L053 | P3：runtime 故障注入与执行结果验收 |

### 第四册：[L054–L072：平台、安全与综合验收](daily/L054-L072.md)

| 编号 | 每天的主题 |
| --- | --- |
| L054 | MCP host/client/server 与协议能力边界 |
| L055 | MCP transport、身份、授权与取消 |
| L056 | Harness、runtime、SDK 与组件职责 |
| L057 | Sandbox、容器/microVM、资源和生命周期 |
| L058 | MCP × runtime × sandbox 集成测试 |
| L059 | Evaluation 对象、指标、重复试验与不确定性 |
| L060 | Code/model/human grader、校准与评估泄漏 |
| L061 | Trace、指标、SLO 与分层故障定位 |
| L062 | 多租户、IAM、索引/cache/memory/log 全链隔离 |
| L063 | Gateway、限流、成本、fallback、灰度与回滚 |
| L064 | CI/回归、安全约束与发布质量门槛 |
| L065 | 综合项目需求、边界和验收合同 |
| L066 | 从用户请求到实际结果的一条垂直流程 |
| L067 | 基准、容量与单变量优化 |
| L068 | 一个编排框架与最小 runtime 的对照 |
| L069 | 中断、删除、恢复和 runbook 演练 |
| L070 | 综合作品交付与可复现工程门槛 |
| L071 | Transformer/RAG/Agent 无提示机制答辩 |
| L072 | 新任务系统设计、re-baseline 与下一阶段 |

## 5. 每天不是只有标题

四册中每张卡都提前写明：前置知识；要解决的问题和可验证目标；教学顺序与核心机制；练习与产物；独立解释/追问；错误模型；回补与下一步。每天的实际结果、掌握状态、代码证据与复习日期在学习发生后另记，不提前编造。

正式讲义仍须符合 [DAY_TEMPLATE](DAY_TEMPLATE.md) 的 16 项结构。当前交付是完整的章节及每日教学计划，不是 72 篇已讲完的教材，也不是 72 份已经运行成功的实验代码。计划和教学展开不是同一回事。

## 6. 通过与回补的门槛

不能因答出 512/8=64、接受一句解释、紧接提示复述，就宣布整个 MHA 或数学基础通过。至少需要核心因果解释、对应推导/实现产物、一个未见过的条件变化。独立通过与延迟通过分开；评分只有证据足够时才给。

P1 门槛：可解释完整前向与联合训练，mask/label 正确，能训练、恢复、生成和排错。

P2 门槛：固定问题和来源，检索/排序/生成分层评测，引用支持、无证据处理、权限与更新删除有测试。

P3 门槛：工具契约、授权、状态、恢复、幂等、取消与预算可验证；不能靠模型声称完成代替实际环境证据。

综合门槛：干净环境可复现；至少三份 ADR；有失败案例与 runbook；接受新约束和故障后仍能说明设计。模拟执行的结果不替代真实模型质量或真实隔离验证。

## 7. 本轮深度与非必修范围

必须能独立推导/实现：基础线性映射、attention、最小训练循环、微型 Transformer、RAG 评估、工具/状态/恢复与权限测试。

必须能解释和选型：现代位置/attention 变体、KV cache、量化、SFT/LoRA/偏好优化、GraphRAG、MCP、Sandbox、框架取舍。

本轮不要求：训练生产规模基础模型、手写 GPU kernel、多机训练、完整强化学习收敛理论、自建虚拟化平台，或追所有新 framework。多模态/语音实时 Agent、深度后训练、GPU 系统等按岗位需要另立完整模块；不假装 72 天覆盖整个 AI 学科。

## 8. 下一次学习入口

当前任务是检查并修复课程计划，不要求立刻继续 Day 5。恢复教学时先迁移现有证据，检查 L001–L004 中未验证的轴/投影基础；再检查 L005 的表示区别与 L009–L010 的 MHA 缺项，满足门槛后进入 L011。数学链路不稳就先补，不因为赶进度提前跳到 backprop API。

## 9. 来源与审计

仓库原 30 天计划、BASELINE、DAY_TEMPLATE、V2 总纲、M02 模块和 LEARNING_STATE 是本计划的直接项目依据；对话是当前理解和教学问题的证据。新 L 编号、日划分、练习、门槛与预算属于本轮课程设计，不伪装成旧计划原有内容。

外部覆盖核对使用 Stanford CS336 2025 存档、PyTorch Autograd/Optimization、Hugging Face causal LM 课程、Anthropic Agent/Context/Evals 官方工程资料和 MCP 官方规范。来源入口见各册与 CURRICULUM_V2。访问日期 2026-10-06；实施时锁定实际版本。不会把旧课程的工具名单当永久推荐。

Project Sources 的旧快照不会因本次 GitHub 写入自动更新。当前课程与状态从本仓库读取，偏好和规则仍参考用户 Sources。