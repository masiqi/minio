# 90 个单元的预习与复习知识框架

版本：2026-10-06 · 仓库：masiqi/minio · 对齐：M00–M10 / D001–D090

[当前计划](../PLAN.md) · [90 单元教学计划](../DAILY_PLAN_90.md) · [实际学习状态](../LEARNING_STATE.md) · [本次核查与边界](AUDIT.md) · [技术资料 S01–S23](SOURCES.md)

## 这套材料怎么用

**课前：** 从当前学习入口找到对应 D 卡，先读“预习”“核心框架与例子”，知道要解决什么、哪些概念彼此相连；记下一个说不清的问题即可。不要求先读完所有参考论文，也不要求把90张一次性看完。

**课后：** 合上正文，独立回答卡内两道自测，再展开“核对要点”。答错时回看具体机制或数字例子，不只背标准句子；公式类再手算一遍，工程类再走一条失败时间线。

**隔开后：** 用新数字、新数据或新故障再解释一次。已看过的自测答案不作为正式无提示验收证据；教练需要换题验证，而不是反复问你能否接受。

预习是建立地图，不是要求自己完成整章教学。卡内不理解的符号与前置可带到课堂，由教练补讲；不要因为预习没全懂就停在原地。每日阅读量由当前学习单元决定，不是自然日必须推进一个编号。

## 一张框架里有什么

每张都有：课程定位与前置 → 要解决的问题/概念链 → 具体公式、小数值例子或工程场景 → 易错边界 → 两道复习自测 → 折叠核对要点 → 动手证据、回补与下一入口。

这里补充的是可独立阅读的**知识框架**，不是把教学计划标题再复制一遍。原卡继续规定正式任务与验收，正式完整讲义继续遵循 [DAY_TEMPLATE](../DAY_TEMPLATE.md)。本套新增例子和自测是教学展开，不冒充原计划逐字内容、真实实验结果或你的已掌握记录。

读过≠会复述；会复述≠会手算/实现；即时答对≠延迟保持。Concept、Mechanism、Engineering、Interview 的实际证据仍写入学习状态，不写入这些公共知识卡。

## 针对当前薄弱点的快速入口

先用 [D002 轴与 shape](D002.md)、[D003 线性投影](D003.md)、[D010 权重与表示](D010.md)、[D013 多头与 W_O](D013.md) 定位疑惑；[D025 联合训练](D025.md) 与 [D031 表示到 logits](D031.md) 回答之前提出的两条完整链路。

这只是查阅快捷方式，不跳过训练章节的导数、链式法则和计算图前置，也不要求从 D001 清零重学。实际下一课以 LEARNING_STATE 和独立诊断为准。

## M00｜数学、张量与实现桥梁（D001–D006）

| 单元 | 知识框架 |
| --- | --- |
| D001 | [起点校准与可复现实验环境](D001.md) |
| D002 | [向量、矩阵与 batch/sequence/feature 轴](D002.md) |
| D003 | [点积、矩阵乘法与 Linear Projection](D003.md) |
| D004 | [概率、log/exp、统计量与 Softmax](D004.md) |
| D005 | [PyTorch 张量操作与参数对象](D005.md) |
| D006 | [基础门槛与回补缓冲](D006.md) |

## M01｜Token、表示与 Attention（D007–D014）

| 单元 | 知识框架 |
| --- | --- |
| D007 | [文本、Tokenizer、词表与 Token ID](D007.md) |
| D008 | [Embedding 查表与 Contextual Representation](D008.md) |
| D009 | [RNN 到 Attention：信息路径复核](D009.md) |
| D010 | [单头 Scaled Dot-Product Attention](D010.md) |
| D011 | [Batch Attention、Causal Mask 与 Padding Mask](D011.md) |
| D012 | [位置表示及其适用边界](D012.md) |
| D013 | [Multi-Head、Concat 与 W_O](D013.md) |
| D014 | [Attention 实现、迁移验收与缓冲](D014.md) |

## M02｜神经网络如何学习（D015–D026）

| 单元 | 知识框架 |
| --- | --- |
| D015 | [T01：样本、目标、参数、超参数与 Loss](D015.md) |
| D016 | [T02A：从局部变化到导数](D016.md) |
| D017 | [T02B：梯度下降与学习率](D017.md) |
| D018 | [T03A：链式法则与多参数共同学习](D018.md) |
| D019 | [T03B：计算图、Backprop 与 Autograd](D019.md) |
| D020 | [T04：矩阵投影的梯度](D020.md) |
| D021 | [T05A：完整 Training Step 与训练循环](D021.md) |
| D022 | [T05B：SGD、Momentum、Adam/AdamW 与训练状态](D022.md) |
| D023 | [T06A：分类、Logits、交叉熵](D023.md) |
| D024 | [T06B：泛化、数据划分与训练故障](D024.md) |
| D025 | [T07：从最终 Loss 回到所有 Head 与 W_O](D025.md) |
| D026 | [T08：训练机制独立验收与缓冲](D026.md) |

## M03｜完整 Transformer 与语言建模（D027–D036）

| 单元 | 知识框架 |
| --- | --- |
| D027 | [FFN 与非线性](D027.md) |
| D028 | [Residual Connection 与信息路径](D028.md) |
| D029 | [LayerNorm、RMSNorm 与 Block 顺序](D029.md) |
| D030 | [Encoder、Decoder 与 Cross-Attention](D030.md) |
| D031 | [Hidden States、LM Head 与 Vocabulary Logits](D031.md) |
| D032 | [语言模型数据：Label Shift、Packing 与 Mask](D032.md) |
| D033 | [P1：拼装一个微型 Decoder-only Transformer](D033.md) |
| D034 | [P1：训练、验证与第一份误差分析](D034.md) |
| D035 | [P1：Checkpoint、恢复与自回归生成](D035.md) |
| D036 | [P1 门槛：完整 Transformer 解释、实现与排错](D036.md) |

## M04｜模型调用、推理性能与适配（D037–D044）

| 单元 | 知识框架 |
| --- | --- |
| D037 | [模型接口、Prompt 与 Structured Output](D037.md) |
| D038 | [生成策略与随机性](D038.md) |
| D039 | [Prefill、Decode 与 KV Cache](D039.md) |
| D040 | [RoPE、MHA/MQA/GQA 与长上下文边界](D040.md) |
| D041 | [推理性能：测量、量化与 Attention 优化](D041.md) |
| D042 | [Pretraining、SFT 与 LoRA/PEFT](D042.md) |
| D043 | [偏好优化、对齐与适配风险](D043.md) |
| D044 | [模型应用选型门槛与缓冲](D044.md) |

## M05｜RAG、Context 与 Memory（D045–D057）

| 单元 | 知识框架 |
| --- | --- |
| D045 | [P2 需求、数据边界与评测集先行](D045.md) |
| D046 | [文档解析、身份、版本、更新与删除](D046.md) |
| D047 | [Chunking 与信息边界](D047.md) |
| D048 | [检索 Embedding、相似度、ANN 与过滤](D048.md) |
| D049 | [Sparse、Dense 与 Hybrid Retrieval](D049.md) |
| D050 | [Query 改写、Reranking 与召回/精排分工](D050.md) |
| D051 | [Context 构建、压缩、引用与拒答](D051.md) |
| D052 | [Context、Conversation History 与 Memory](D052.md) |
| D053 | [RAG 权限、隐私与 Prompt Injection 边界](D053.md) |
| D054 | [RAG 分层评估与错误归因](D054.md) |
| D055 | [GraphRAG / LightRAG 的数据流与成本](D055.md) |
| D056 | [P2：普通 RAG 与图方案对照实验](D056.md) |
| D057 | [P2 门槛：可评测、可溯源、可隔离的 RAG](D057.md) |

## M06｜可靠 Agent Runtime（D058–D067）

| 单元 | 知识框架 |
| --- | --- |
| D058 | [Workflow、LLM+Tools 与 Agent 的控制流](D058.md) |
| D059 | [Tool Contract、Schema 与错误协议](D059.md) |
| D060 | [授权、人工批准与副作用边界](D060.md) |
| D061 | [实现 Agent Loop 与显式状态机](D061.md) |
| D062 | [Timeout、Retry、Idempotency 与取消](D062.md) |
| D063 | [Checkpoint、恢复与持久化执行](D063.md) |
| D064 | [Context Router、记忆与执行预算](D064.md) |
| D065 | [Planning、Reflection 与 Multi-Agent 的边界](D065.md) |
| D066 | [框架映射与同任务对照](D066.md) |
| D067 | [P3 初版门槛：可靠执行，而非只跑通 Demo](D067.md) |

## M07｜MCP、Harness 与 Sandbox（D068–D073）

| 单元 | 知识框架 |
| --- | --- |
| D068 | [MCP 的架构与协议边界](D068.md) |
| D069 | [Transport、身份、授权与凭证边界](D069.md) |
| D070 | [MCP 工具适配与生命周期实验](D070.md) |
| D071 | [Harness 的职责与可替换边界](D071.md) |
| D072 | [Sandbox 威胁模型与资源生命周期](D072.md) |
| D073 | [协议与执行边界门槛](D073.md) |

## M08｜Evaluation、企业架构与可靠性（D074–D080）

| 单元 | 知识框架 |
| --- | --- |
| D074 | [Testing、Observability 与 Evaluation](D074.md) |
| D075 | [Grader、人工校准与不确定性](D075.md) |
| D076 | [Agent Outcome、Trajectory 与回归套件](D076.md) |
| D077 | [Multi-Tenant、IAM、Secret 与数据全链路隔离](D077.md) |
| D078 | [Model Gateway、SLO、预算与降级](D078.md) |
| D079 | [版本化评测、发布、在线监测与回滚](D079.md) |
| D080 | [企业可靠性门槛与事故演练](D080.md) |

## M09｜综合项目与架构答辩（D081–D087）

| 单元 | 知识框架 |
| --- | --- |
| D081 | [综合项目范围、业务成功与验收合同](D081.md) |
| D082 | [垂直集成：检索、模型、工具与持久状态](D082.md) |
| D083 | [事实可溯源与行动可授权](D083.md) |
| D084 | [故障注入、恢复与预算约束](D084.md) |
| D085 | [质量、成本、延迟与消融比较](D085.md) |
| D086 | [ADR、Runbook、复现与交付清单](D086.md) |
| D087 | [项目答辩与需求变化验收](D087.md) |

## M10｜独立表达与延迟验证（D088–D090；全程贯穿）

| 单元 | 知识框架 |
| --- | --- |
| D088 | [Transformer 与训练机制独立答辩](D088.md) |
| D089 | [RAG、Agent 与企业系统设计面试](D089.md) |
| D090 | [Re-baseline、证据盘点与下一阶段](D090.md) |

## 维护与验证

参考资料及版本敏感项见 SOURCES；数字例子的本地检查见 [NUMERICAL_CHECKS](NUMERICAL_CHECKS.md)，复跑脚本为 [verify_examples.py](verify_examples.py)。这些检查是教材校核，不是 P1/P2/P3 或学习者完成证据。

更新原教学卡时同时检查本目录对应 D 卡；保持编号、前置和范围一致。历史 L 编号草案不混入本套90卡。公共例子、示意代码、计划实验和真实测量必须明确区分。
