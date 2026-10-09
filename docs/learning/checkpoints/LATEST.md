# 最新教学 Checkpoint
checkpoint_id: CP-2026-10-09-005
snapshot: [2026-10-09-005.md](2026-10-09-005.md)
date: 2026-10-09

## 当前现场
- D021 Gradient Accumulation 已在 CP004 收口。
- 本轮完成漏掉 optimizer.step() 故障实验：用户预测并实测参数不更新、Loss 固定为 0.72。
- 完成误用 detach 实验：prediction detach 后 forward 正常，到 loss.backward() 报不 require grad / 无 grad_fn 类错误。
- 用户已理解 detach 保留数值但切断梯度路径，并能区分 detach 与 requires_grad=False。
- 用户已能解释按层冻结：冻结前 50 层参数不代表跳过 forward；第 50 层输出仍是第 51 层输入。
- 下一步：按课程计划确认 D021 收口并进入下一项，不继续横向扩展冻结/Fine-tuning。
