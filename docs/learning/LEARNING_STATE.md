# AI Learning Coach — 当前学习状态
updated: 2026-10-10
current_checkpoint_id: CP-2026-10-10-001
恢复顺序：[AGENTS](../../AGENTS.md) → [LATEST](checkpoints/LATEST.md) → [CP001完整快照](checkpoints/2026-10-10-001.md) → [D022教学卡](daily/D001-D030-foundations-training.md)。

## 已证实的最近进度
M02 / D021 已完成并收口。当前进入 D022：SGD / Momentum / Adam / Optimizer State。

本轮已建立 Momentum 的历史趋势直觉，并纠正“多个参数共用一个 Momentum 速度”的误区：optimizer state 是逐参数维护。用户能解释若 checkpoint 只保存模型参数、不保存 optimizer state，恢复训练时历史趋势丢失，需要重新积累，训练轨迹会发生变化。

Adam 已进入公式与手算阶段。用户理解每个参数滚动维护 m、v，而非保存全部历史梯度：m 保留正负以描述历史方向趋势；v 使用梯度平方以描述历史梯度尺度并避免正负抵消。

手算设 m0=v0=0、beta1=0.9、beta2=0.99、g1=+10、g2=-10，得到 m1=1、v1=1、m2=-0.1、v2=1.99。用户已能自行算出 m2，并理解 (-10)^2=100；v2 最后加法经纠正后确认 1.99。

用户进一步理解 Adam 的核心缩放 m/sqrt(v)：当两个参数 m 都为 1，A 的 v=100 时有效比例为 0.1，B 的 v=0.01 时为 10，用户独立判断 B 更新更大。

## 目前教学断点
D022 进行中。下一步从 m/sqrt(v) 后续机制继续，补必要的 bias correction 与 epsilon，然后按教学卡进入 SGD/自适应优化器对照实验、optimizer state 观察和 checkpoint 保存/恢复一致性实验。Adam 尚未完成完整费曼复述，不标记为完全掌握。

## 不重复与未完
不重复 D021 Training Loop、Gradient Accumulation、漏 step、detach/requires_grad、冻结层 forward；也不要从头重复 Momentum 历史趋势、逐参数状态、Adam m/v 基础手算，除非用于主动回忆验证。

D022 未完：bias correction、epsilon、对照实验、state 观察、checkpoint 恢复一致性、费曼收口。
后续 D023 交叉熵、D024 验证、D025 多头联合训练仍按课程依赖处理。
