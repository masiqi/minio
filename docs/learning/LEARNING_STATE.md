# AI Learning Coach — 当前学习状态
updated: 2026-10-09
current_checkpoint_id: CP-2026-10-09-005
恢复顺序：[AGENTS](../../AGENTS.md) → [LATEST](checkpoints/LATEST.md) → [CP005完整快照](checkpoints/2026-10-09-005.md) → [D021教学卡](daily/D001-D030-foundations-training.md)。

## 已证实的最近进度
M02 / D021：20轮 CPU PyTorch Training Loop 与 Gradient Accumulation 已完成（详见 CP003/CP004）。本轮继续完成两个故障实验。

漏掉 optimizer.step()：用户先预测 backward 虽能计算梯度，但参数不会更新，因此 Loss 不变；本地运行确认 w1/w2 不变，Loss 始终 0.72。

误用 detach：用户此前未学过该机制，本轮先建立“保留数值、切断此前梯度关系”的心智模型，再实际把 prediction detach。用户确认 forward 正常，到 loss.backward() 才出现不 require grad / 无 grad_fn 类错误，并能解释为梯度路径被主动截断。

进一步迁移：用户主动联想到 requires_grad=False，并理解可以只训练部分参数。对于 100 层模型冻结前 50 层，通常批量将前 50 层参数设 requires_grad=False，而非到处 detach。用户已正确解释被冻结层仍必须参与 forward，因为其输出仍是后续层输入。

## 目前教学断点
D021 的 Gradient Accumulation、漏 step、误用 detach 故障点均已完成。下一轮按既定课程计划确认 D021 收口并进入下一项；不要继续横向扩展 Fine-tuning/冻结策略。

## 不重复与未完
不重复 PyTorch 安装、基本 SGD、20轮 loop、Gradient Accumulation 基础机制、漏 step 现象、detach 后 forward 正常/backward 报错、冻结层仍参与 forward。
后续 D022 优化器状态、D023 交叉熵、D024 验证、D025 多头联合训练仍按课程依赖处理。跟跑/修改示例代码不等于从零独立实现完整训练器。
