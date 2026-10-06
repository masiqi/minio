# AI Learning Coach — 当前学习计划入口

更新日期：2026-10-06。

## 当前有效方案

能力主线采用 [能力驱动学习方案 V2](CURRICULUM_V2.md) 的 M00–M10；本次逐日执行采用 [90 个学习日实施计划](DAILY_PLAN_90.md)，不再按旧版“每天一个主题”的 30 天表推进。

**直接阅读：[90 日总览与章节门槛](DAILY_PLAN_90.md) → [D001–D030](daily/D001-D030-foundations-training.md) / [D031–D060](daily/D031-D060-transformer-rag.md) / [D061–D090](daily/D061-D090-agent-production.md)。**

90 张卡已逐一准备前置与目标、教学链与误区、练习与交付、独立验收、未过回补与下一单元。它们是教学计划，不是未来实验已完成的声明；正式讲义仍按 DAY_TEMPLATE 展开，实际学习结果另记。

| 文档 | 用途 |
| --- | --- |
| [DAILY_PLAN_90.md](DAILY_PLAN_90.md) | 本次完整逐日实施入口、章节范围、工时假设、迁移与通过门槛 |
| [CURRICULUM_V2.md](CURRICULUM_V2.md) | M00–M10 模块、依赖、三个实践成果及深度 |
| [LEARNING_STATE.md](LEARNING_STATE.md) | 当前能力证据、旧 Day 迁移、弱点、复习与下一次入口 |
| [M02 训练机制](modules/M02-training-mechanisms.md) | T01–T08 完整教学链；细分到 D015–D026 |
| [COACH_PROTOCOL.md](COACH_PROTOCOL.md) | 提前备课、独立验证、纠错、记录与状态同步 |
| [课程审计](AUDIT_2026-10-06.md) | 原文件证据、缺口与修订理由 |
| [DAY_TEMPLATE.md](DAY_TEMPLATE.md) | 每个正式单元必须达到的讲义标准 |

COACH_PROTOCOL.md 已经通过读取核实存在；此前入口中“写入未成功、待补充”的描述不再适用。

## 编号与排程优先关系

M00–M10 是能力编号，D001–D090 是本次细粒度执行版，历史 Day 1–5 保留原含义。仓库若保留 L001 等其他粒度的稿件，按模块与能力对应，不与 D 计划叠加为第二套必修或重复计分。实际会话独立记日期。

90 个学习日不强制等于 90 个自然日；每课可拆分，也可根据真实通过证据抵扣。细化后的工时与边界以 DAILY_PLAN_90 为准，V2 的粗粒度工时不作为完成上限。不能为了赶日期省略训练机制、评估、安全或必要回补。

## 从当前状态继续

本次先完成课程修订，不要求立即补交 Day 5。恢复学习时：检查 M00 必要前置 → 补查 Token/Embedding 与 MHA 尚未验证项 → 正式进入 M02 → 再完成完整 Transformer。

历史进度不清零，提示后复述也不自动升级为掌握。已稳定的 RNN/Attention 内容不机械重问；用新条件检查真正有缺口的部分。具体证据见 LEARNING_STATE。

## 旧计划与学习结果

原 30 天计划和 Day 1–3 学习结果保存在不可变 Git 历史版本中：

[原 PLAN.md（2026-10-06 修订前）](https://github.com/masiqi/minio/blob/97eb0ce84cd6869099fb31ac866333d4ed311ffd/docs/learning/PLAN.md)

现有 [BASELINE.md](BASELINE.md)、[Day 1 完整讲义](day-01-rnn-to-attention.md)、架构、面试与 ADR 文档保留原内容。未来项目代码、测试结果和个人掌握状态未因课程设计完成而被伪造。

## Project Sources 同步边界

GitHub 是当前可写课程与状态入口；用户的偏好和规则仍以 Project Sources 为重要依据。上传的旧进度快照不会自动更新，不能把它们的“初始化”状态覆盖回当前进度。写入完成必须以实际 commit 和回读为依据。
