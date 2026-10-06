# AI Learning Coach — 当前学习计划入口

更新日期：2026-10-06。

## 当前有效方案

请从 [能力驱动学习方案 V2](CURRICULUM_V2.md) 开始，不再按旧版“每天一个主题”的 30 天表推进。

| 文档 | 用途 |
| --- | --- |
| [CURRICULUM_V2.md](CURRICULUM_V2.md) | M00–M10 模块、依赖、工作量、三个实践成果及验收 |
| [LEARNING_STATE.md](LEARNING_STATE.md) | 当前能力证据、旧 Day 迁移、弱点、复习与下一次入口 |
| [M02 训练机制](modules/M02-training-mechanisms.md) | T01–T08 的完整教学链路，不再作为临时支线 |
| [课程审计](AUDIT_2026-10-06.md) | 实际文件证据、缺口与修订理由 |
| [DAY_TEMPLATE.md](DAY_TEMPLATE.md) | 每个正式单元必须达到的讲义标准 |

教学执行要求以 V2 第 7、9、11 节、审计第 6 节与原 Project Rules 为准。单独的 COACH_PROTOCOL.md 写入未成功，不把它当作已存在的必读文件；V2 中对该文件的引用目前为待补充引用。

## 从当前状态继续

本次先完成课程修订，不要求立即补交 Day 5。恢复学习时：检查 M00 必要前置 → 补查 Token/Embedding 与 MHA 尚未验证项 → 正式进入 M02 → 再完成完整 Transformer。

历史进度不清零，提示后复述也不自动升级为掌握。用模块编号与证据推进，具体见 LEARNING_STATE。

## 旧计划与学习结果

原 30 天计划和 Day 1–3 学习结果保存在修改前的不可变 Git 历史版本中：

[原 PLAN.md（2026-10-06 修订前）](https://github.com/masiqi/minio/blob/97eb0ce84cd6869099fb31ac866333d4ed311ffd/docs/learning/PLAN.md)

现有 [BASELINE.md](BASELINE.md)、[Day 1 完整讲义](day-01-rnn-to-attention.md)、架构、面试和 ADR 文档保留原内容。本次没有生成尚未存在的项目代码或伪造学习通过结果。

## Project Sources 同步边界

GitHub 是当前可写课程与状态入口；用户的偏好和规则仍以 Project Sources 为重要依据。上传的旧进度快照不会自动更新，不能把它们的“初始化”状态覆盖回当前进度。
