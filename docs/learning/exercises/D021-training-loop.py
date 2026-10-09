import torch


def main() -> None:
    # 同一组两样本；明确使用 CPU 和 float32。
    x = torch.tensor([2.0, 3.0], dtype=torch.float32, device="cpu")
    y = torch.tensor([10.0, 13.0], dtype=torch.float32, device="cpu")

    # 从上一实验的初始参数重跑，以便第 1 轮复现已知结果。
    # 只在循环外初始化，后续轮次沿用更新后的参数。
    w1 = torch.tensor(4.2, dtype=torch.float32, device="cpu", requires_grad=True)
    w2 = torch.tensor(1.6, dtype=torch.float32, device="cpu", requires_grad=True)
    optimizer = torch.optim.SGD([w1, w2], lr=0.1)
    epochs = 20

    print("epoch | w1_after | w2_after | loss_before | loss_after | A_after | B_after")

    # 本实验把全部两个样本作为一个 Batch，每个 epoch 更新一次。
    for epoch in range(1, epochs + 1):
        optimizer.zero_grad()  # 本实验不做跨轮梯度累积。

        # 每轮用当前参数重新前向计算，得到新的计算图。
        prediction = x * w1 + w2
        loss = ((prediction - y) ** 2).mean()
        if not torch.isfinite(loss).item():
            raise RuntimeError(f"第 {epoch} 轮 Loss 出现 NaN/Inf，停止更新。")
        loss_before = loss.item()

        loss.backward()
        optimizer.step()

        # 更新后重新计算，仅用于观察，不参与这次反向传播。
        with torch.no_grad():
            new_prediction = x * w1 + w2
            sample_losses = (new_prediction - y) ** 2
            loss_after = sample_losses.mean().item()

        print(
            f"{epoch:5d} | {w1.item():8.4f} | {w2.item():8.4f} | "
            f"{loss_before:11.6f} | {loss_after:10.6f} | "
            f"{sample_losses[0].item():7.4f} | {sample_losses[1].item():7.4f}"
        )


if __name__ == "__main__":
    main()
