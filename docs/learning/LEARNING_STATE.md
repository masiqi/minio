# AI Learning Coach — 当前学习状态
updated: 2026-10-10
current_checkpoint_id: CP-2026-10-10-002
恢复顺序：[AGENTS](../../AGENTS.md) → [LATEST](checkpoints/LATEST.md) → [CP002完整快照](checkpoints/2026-10-10-002.md) → [D022教学卡](daily/D001-D030-foundations-training.md)。

## 已证实的最近进度
M02 / D021 已完成。当前 D022：SGD / Momentum / Adam / Optimizer State 进行中。

用户已建立 Momentum 的逐参数历史趋势、Adam 的 m/v 两份逐参数统计、m/sqrt(v) 自适应缩放直觉。已理解平方梯度历史统计再开根号得到类似 RMS 的尺度估计，大梯度会被平方更突出。

Bias Correction 已讲透到必要机制：m0=v0=0 导致早期 EMA 系统性偏小；m_hat=m/(1-beta1^t)、v_hat=v/(1-beta2^t) 用于当前参数更新，修正值不写回 m/v；随着 t 增大 beta^t→0，修正自然趋弱。用户能正确判断下一步递推继续使用未修正状态。

已理解最终参数更新 theta_t = theta_(t-1) - alpha*m_hat/(sqrt(v_hat)+epsilon)，并明确 theta 是模型参数，m/v 是 optimizer state。

用户已能区分 Momentum 与 Adam：两者都利用逐参数历史；Adam 额外根据每个参数自己的历史梯度尺度调节有效步长。优化器选择方面已建立“成熟 recipe + trade-off + 受控实验”的工程判断，不把 SGD/Momentum/Adam 当成等级排行榜。

## 当前教学断点
用户下班，停止于优化器选择讨论。D022 尚未收口。

## 下一次直接继续
先用 1-2 个主动回忆问题确认 Bias Correction / Adam 更新链路；必要时补 epsilon；随后严格按 D022 做 SGD（或 SGD+Momentum）与自适应优化器对照实验，观察参数/梯度/optimizer state，再做 checkpoint 保存恢复一致性实验，最后费曼与面试表达收口。

## 不重复与未完
不从头重复 D021、Momentum 动机、逐参数 state、+10/-10 m/v 手算、Bias Correction 基础机制，除非主动回忆验证需要。
D022 未完：epsilon（如需要）、对照实验、state 观察、checkpoint 恢复一致性、费曼收口。
