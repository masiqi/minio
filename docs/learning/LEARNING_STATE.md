# AI Learning Coach — 当前学习状态
updated: 2026-10-09
current_checkpoint_id: CP-2026-10-09-004
恢复顺序：[AGENTS](../../AGENTS.md) → [LATEST](checkpoints/LATEST.md) → [CP004完整快照](checkpoints/2026-10-09-004.md) → [D021教学卡](daily/D001-D030-foundations-training.md)。

## 已证实的最近进度
M02 / D021：20轮CPU PyTorch Training Loop 已完成（完整日志见CP003）。随后完成 Gradient Accumulation 核心实验：用户先观察到不清梯度但每轮 step 会造成异常波动；改成每3次 backward 才 step 后，未缩放 Loss 导致十万量级发散；使用 (loss / accumulation_steps).backward() 后恢复稳定。修正版20轮末用户观察 loss≈0.2205，与普通训练第6次更新的0.220511基本一致。

用户已经能够独立解释 Gradient Accumulation 的工程动机：显存不足时把逻辑大 Batch 拆成多个 mini-batch，每个 mini-batch backward 并保留梯度，达到累积步数后统一 step/zero_grad，从而实现更大的 effective batch。更大 Batch 不自动意味着更好的训练效果。

## 目前教学断点
D021 Gradient Accumulation 核心机制与工程动机已收口。下一轮按90日计划和D021教学卡核对是否还有必做故障测试；若当前门槛已满足则进入计划下一子项。不要继续横向深挖 Batch Size 泛化理论，也不要重复本轮基础费曼题。

## 不重复与未完
不重复PyTorch安装、-12/-6、正梯度方向、基本epoch计数、单次SGD、20轮loop、Gradient Accumulation基础定义/显存动机/同Batch三次平均等价一次更新。
D019 detach排错、D020矩阵梯度及后续D022优化器状态、D023交叉熵、D024验证、D025多头联合训练仍按课程依赖处理。跟跑/修改示例代码不等于从零独立实现完整训练器。
