# 最新教学 Checkpoint
checkpoint_id: CP-2026-10-09-004
snapshot: [2026-10-09-004.md](2026-10-09-004.md)
date: 2026-10-09

## 当前现场
- D021 Gradient Accumulation 核心实践已完成：用户实际经历错误版本（不清 grad 但每轮 step）、3步累积未缩放导致 Loss 发散、改为 loss/accumulation_steps 后恢复稳定。
- accumulation_steps=3 修正后参数每3轮更新；20轮末用户观察 loss≈0.2205，与普通训练第6次更新 loss_after=0.220511 基本对齐。
- 用户已能费曼解释显存不足时用多个 mini-batch 累积梯度来实现更大的 effective batch，并指出更大 Batch 不保证更好效果。教师只补正 backward/step/zero_grad 的表达顺序。
- 下一步：按计划核对 D021 是否还有必做故障测试；若核心门槛已满足则继续下一子项，不重复 Gradient Accumulation 基础定义或本轮实验。
