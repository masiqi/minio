# 最新教学 Checkpoint
checkpoint_id: CP-2026-10-10-001
snapshot: [2026-10-10-001.md](2026-10-10-001.md)
date: 2026-10-10

## 当前现场
- D021 已收口，当前正式进入 D022：SGD / Momentum / Adam / Optimizer State。
- 已理解 Momentum 利用历史趋势，且 optimizer state 是逐参数维护，不是整个模型共用一个速度。
- 已理解只保存模型参数、不保存 optimizer state 会丢失历史趋势，恢复训练轨迹会变化。
- Adam 已讲到两份逐参数统计：m 表示历史梯度趋势，v 表示历史梯度平方尺度。
- 已手算 beta1=0.9、beta2=0.99、g1=+10、g2=-10：m1=1、v1=1、m2=-0.1、v2=1.99。
- 已理解 +10/-10 在 m 中会抵消、在 v 中因平方不会抵消。
- 已通过 m/sqrt(v) 对比自行算出：m 都为 1 时，v=100 对应 0.1，v=0.01 对应 10，因此历史尺度会改变有效更新。
- 下一步：继续 Adam 必要机制（bias correction、epsilon）后进入 D022 对照实验和 checkpoint 保存/恢复实验；不要从头重复 Momentum/Adam 基础直觉。
