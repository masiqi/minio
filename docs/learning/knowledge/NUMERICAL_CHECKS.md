# 教材数值例子核查

日期：2026-10-06。检查对象是知识框架中明确列出的教学数字，不是学习者作业或实际项目质量。

## 执行结果

在本次可用本地 Python 环境中运行同目录 `verify_examples.py`，仅使用标准库、无外部请求、无 GPU/模型训练或付费调用。

```text
Ran 26 tests
OK
```

运行方式：从仓库根目录执行 `python docs/learning/knowledge/verify_examples.py`。需要 Python 3.10 或更新版本；脚本不修改仓库或用户数据。

## 覆盖范围

| 单元 | 实际核对内容 |
| --- | --- |
| D003 | 4→2 线性映射结果；低维碰撞反例 |
| D004 | Softmax 的指定概率；同加常数不变 |
| D005 | transpose 与同 shape reshape 的元素差别 |
| D010 | 三个二维 Value 加权结果 [1.4,2.2] |
| D012/D013 | 小维度正余弦编码、频率对数量、Head 宽度 |
| D015/D016 | 平方损失；有限差分核对解析导数 |
| D017/D018 | 步长过大反例；双参数链式梯度与共同更新 |
| D020 | 矩阵投影的参数/输入梯度 |
| D021/D022 | step 数量；Momentum 示例 |
| D023/D026 | 交叉熵数值；完整小图的一次更新 |
| D028/D029 | 残差结果；LayerNorm/RMSNorm 小向量计算 |
| D030/D031 | Cross-Attention shape；LM Head logits |
| D038/D039 | 候选重归一化；KV Cache 数量 |
| D040/D042/D048 | 相对旋转恒等式；低秩参数数目；dot/cosine |

## 边界

本脚本没有自动验证90篇全文语义、所有链接、协议兼容性或未来实验，更不代表已经训练 P1、建好 P2/P3 或证明学习者掌握。浮点对照使用指定容差；Mask 全遮挡等不属于该有限 Softmax helper 的实现范围。

教材的原计划对齐与边界检查见 [AUDIT](AUDIT.md)，参考资料见 [SOURCES](SOURCES.md)。
