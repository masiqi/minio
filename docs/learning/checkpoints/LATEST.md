# 最新教学 Checkpoint

checkpoint_id: CP-2026-10-09-002

snapshot: [2026-10-09-002.md](2026-10-09-002.md)

记录日期：2026-10-09。状态：用户恢复学习；多轮Training Loop完整脚本已布置，待用户运行。

## 恢复顺序

遵循根[AGENTS.md](../../../AGENTS.md)，读本页指定完整快照，再读[当前状态](../LEARNING_STATE.md)、[教学协议](../COACH_PROTOCOL.md)和D021原卡。不要仅凭标题重新问基础题。

## 一屏定位

- 已有用户证据：CPU环境可用，单样本Autograd、Batch平均梯度、SGD单步均跑通。
- 最后用户实测：参数约(3.84,1.48)，平均Loss=0.3528001308441162；不要用教练自测替代用户证据。
- pending_task: TASK-D021-LOOP-01，运行[20轮训练脚本](../exercises/D021-training-loop.py)，建议本地名training_loop_demo.py，贴第1、2轮及最后3轮或完整日志。
- 新脚本显式从(4.2,1.6)重跑，x=[2,3],y=[10,13]，CPU/float32，mean平方误差，SGD lr=.1，每epoch全数据一个Batch；参数只初始化一次。
- 下一动作：接收日志或代码疑问，分析逐轮变化；不是重新布置同一脚本，更不是复问epoch、更新方向或安装。
- 用户多轮运行尚未确认；梯度累积代码、detach排错、D020矩阵梯度、验证集实验与完整D021验收仍未完成。

历史证据见CP001，当前待办以本快照为准。此处不是后台程序或训练模型checkpoint。
