# AI Learning Coach — 当前学习计划入口

更新日期：2026-10-09。

## 先恢复现场，再选择课程

**教练/代理首先读取根目录 [AGENTS.md](../../AGENTS.md)，执行“每轮回答后判断是否保存”的规则。** 每轮要判断，但只在有新的有效证据、教学现场变化或交接需求时写 checkpoint；不要等用户提醒。

**继续学习、新会话或换设备后，读取 [最新教学 Checkpoint](checkpoints/LATEST.md)，再读它指向的完整快照、[当前学习状态](LEARNING_STATE.md)与对应日卡。** 快照记录已问已答、实测输出、设备/代码状态和下一动作。不要仅凭旧日报或聊天印象重问基础题。

Checkpoint 保存和恢复规则见 [checkpoints/README.md](checkpoints/README.md)。本入口只提供动态链接，不保留一段会随学习过期的固定“从头检查”指令。

## 当前有效方案

能力主线采用 [能力驱动学习方案 V2](CURRICULUM_V2.md) 的 M00–M10；逐日执行采用 [90 个学习日实施计划](DAILY_PLAN_90.md)，不再按旧版“每天一个主题”的 30 天表推进。

**教学卡：[90 日总览与章节门槛](DAILY_PLAN_90.md) → [D001–D030](daily/D001-D030-foundations-training.md) / [D031–D060](daily/D031-D060-transformer-rag.md) / [D061–D090](daily/D061-D090-agent-production.md)。**

**课前预习与课后复习：[90 个单元知识框架总目录](knowledge/README.md)。** 每单元一份独立 Markdown，包含概念链、公式/例子、易错边界、自测与折叠核对要点；与本计划 D001–D090 一一对应，不另起编号。看过材料不自动改变学习状态，正式验收使用未见题。

90 张卡已逐一准备前置与目标、教学链与误区、练习与交付、独立验收、未过回补与下一单元。它们是教学计划，不是未来实验已完成的声明；正式讲义仍按 DAY_TEMPLATE 展开，实际学习结果另记。

| 文档 | 用途 |
| --- | --- |
| [AGENTS.md](../../AGENTS.md) | 代理入口、每轮 checkpoint 判定、正常教学与持久化的执行顺序 |
| [最新Checkpoint](checkpoints/LATEST.md) | 动态恢复指针；必须再读完整快照，不凭一句进度猜下一题 |
| [Checkpoint协议](checkpoints/README.md) | 保存字段、触发、问答去重、冲突处理与回读要求 |
| [DAILY_PLAN_90.md](DAILY_PLAN_90.md) | 完整逐日实施入口、章节范围、工时假设、迁移与通过门槛 |
| [知识框架总目录](knowledge/README.md) | 90 个单元的预习地图、机制例子、复习自测与核对；不替代实际验收 |
| [知识框架核查](knowledge/AUDIT.md) | 对齐的计划版本、编写边界与数值检查 |
| [CURRICULUM_V2.md](CURRICULUM_V2.md) | M00–M10 模块、依赖、三个实践成果及深度 |
| [LEARNING_STATE.md](LEARNING_STATE.md) | 当前能力证据、旧 Day 迁移、弱点、复习；与最新Checkpoint保持一致 |
| [M02 训练机制](modules/M02-training-mechanisms.md) | T01–T08 完整教学链；细分到 D015–D026 |
| [COACH_PROTOCOL.md](COACH_PROTOCOL.md) | 提前备课、独立验证、纠错、记录与版本核验 |
| [课程审计](AUDIT_2026-10-06.md) | 核查发现和修订依据 |
| [DAY_TEMPLATE.md](DAY_TEMPLATE.md) | 每个正式单元必须达到的讲义标准 |

## 编号与排程优先关系

M00–M10 是能力编号，D001–D090 是细粒度执行版，历史 Day 1–5 保留原含义。仓库若保留 L001 等其他粒度的稿件，按模块与能力对应，不与 D 计划叠加为第二套必修或重复计分。实际会话独立记日期，Checkpoint有独立ID。

90 个学习日不强制等于 90 个自然日；每课可拆分，也可根据真实通过证据抵扣。细化后的工时与边界以 DAILY_PLAN_90 为准，V2 的粗粒度工时不作为完成上限。不能为了赶日期省略训练机制、评估、安全或必要回补。

## 从当前状态继续

实际断点以最新Checkpoint为准；保留已完成证据与未通过前置。已开始后续单元的局部实践，不等于之前所有单元通过。恢复时不清零、不强迫补交错位的旧Day5，也不以同一题更换数字作为自动开场。

历史进度不清零，提示后复述也不自动升级为掌握。复习应有具体能力目标和间隔/迁移依据；不能把教练丢失进度当成学生需要重学。

## 旧计划与学习结果

原 30 天计划和 Day 1–3 学习结果保存在不可变 Git 历史版本中：

[原 PLAN.md（2026-10-06 修订前）](https://github.com/masiqi/minio/blob/97eb0ce84cd6869099fb31ac866333d4ed311ffd/docs/learning/PLAN.md)

现有 [BASELINE.md](BASELINE.md)、[Day 1 完整讲义](day-01-rnn-to-attention.md)、架构、面试与 ADR 文档保留原内容。历史学习日报不改写为今天的结论。本次只更新恢复机制与真实状态，不重写90单元教学卡或宣称未完成项目已实现。

## Project Sources 同步边界

GitHub 是当前可写课程与状态入口；用户的偏好和规则仍以 Project Sources 为重要依据。上传的旧进度快照不会自动更新，不能把它们的“初始化”状态覆盖回当前进度。写入完成必须以实际 commit 和回读为依据。
