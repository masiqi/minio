# 最新教学 Checkpoint
checkpoint_id: CP-2026-10-10-002
snapshot: [2026-10-10-002.md](2026-10-10-002.md)
date: 2026-10-10

## 当前现场
- D022：SGD / Momentum / Adam / Optimizer State 仍在进行中。
- 已完成 Momentum 历史趋势、逐参数 optimizer state、Adam m/v 与 m/sqrt(v) 自适应直觉。
- 已理解平方→历史平均→开根号是类似 RMS 的尺度统计，不等于简单平均绝对值。
- 已完成 Bias Correction：理解 0 初始化导致早期 EMA 偏小、1-beta^t 的来源、修正随 t 增大自然减弱。
- 已确认 m_hat/v_hat 只用于当前参数更新，不写回内部 m/v；下一步递推继续使用未修正状态。
- 已理解 Adam 最终更新 theta，m/v 是 optimizer state，不是模型参数。
- 已能区分 Momentum 与 Adam：前者利用逐参数历史趋势，后者还依据逐参数历史梯度尺度调节有效步长。
- 已建立优化器选择工程直觉：不是 SGD < Momentum < Adam 的排行榜；优先参考成熟 recipe，再用受控实验验证。Transformer/LLM 缺少 recipe 时 AdamW 常作为自然 baseline，但不是死规则。

## 下一步
1. 用少量主动回忆确认 Bias Correction / Adam 更新链路；
2. 必要时补 epsilon；
3. 按 D022 进入 SGD（或 SGD+Momentum）与自适应优化器对照实验；
4. 观察参数、梯度、optimizer state；
5. checkpoint 保存/恢复一致性实验；
6. 费曼与面试表达收口。

不要从头重复 Momentum、m/v、Bias Correction 基础讲解。
