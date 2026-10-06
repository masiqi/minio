# 技术资料与来源边界（S01–S23）

核验日期：2026-10-06。供教师核对与学习者选读，不要求每课通读全部资料。

## 原计划与新增内容怎样区分

D001–D090 的编号、主题、前置及正式练习/验收，以仓库三册 daily 教学卡为依据。本次读取基准提交：`1951878703e008e82e3c83b38b9d0e65b69cbe2c`，具体文件哈希见 [AUDIT](AUDIT.md)。

知识框架里的小数值例子、手算展开、工程场景、自测与答案是本次原创教学展开。外部论文/官方文档用于核对机制和边界，不表示它们规定了本课程日程，也不把本课示例伪装成论文实验或用户项目实测。

API、规范、价格、模型能力和框架维护状态会变化。以下是本次核查入口；实际实施前固定适用版本并重新核对。PyTorch 页面本次指向2.14，不要求学习者现有环境必须使用该版本。网址含 main/latest 的资料尤其不能当作永久固定契约。

## S01

**张量、轴与可复现性。** 用于 D001/D002/D005/D006 等。

[PyTorch Tensor 教程](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)；[Reproducibility](https://docs.pytorch.org/docs/2.14/notes/randomness.html)。重点核对 shape/dtype/device、索引操作以及同 seed 不保证跨环境完全一致的边界。

## S02

**线性层及权重约定。** 用于 D003/D020/D031 等。

[PyTorch Linear](https://docs.pytorch.org/docs/2.14/generated/torch.nn.Linear.html)。数学行向量约定 XW 与框架 out×in 存储、x·weightᵀ 的关系需要区分。本套矩阵梯度与具体数字为教学推导。

## S03

**Softmax 与归一化轴。** 用于 D004/D010/D023。

[PyTorch Softmax](https://docs.pytorch.org/docs/2.14/generated/torch.nn.Softmax.html)。关注归一化的维度、shape 与概率含义；分类损失的实际输入要求另见 S08。

## S04

**Tokenizer 与 Embedding。** 用于 D007/D008。

[Hugging Face Tokenizer summary](https://huggingface.co/docs/transformers/main/en/tokenizer_summary)；[PyTorch Embedding](https://docs.pytorch.org/docs/2.14/generated/torch.nn.Embedding.html)。教学词表与 ID 是假设例子，不是某生产模型的分词结果。

## S05

**Attention 与经典 Transformer。** 用于 D009–D014、D025、D027–D030。

[Attention Is All You Need，HTML 全文](https://arxiv.org/html/1706.03762v7)。核对 Scaled Dot-Product、Multi-Head、位置编码、FFN、残差与原始 encoder-decoder。经典架构不等于每一种现代 LLM；输入缩放、mask 与位置约定需明确。

## S06

**Autograd 与计算图。** 用于 D016/D018–D021/D025/D026。

[PyTorch Automatic Differentiation](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)。关注链式传播、图路径、叶梯度与 detach。局部导数和矩阵手算不把梯度解释为因果责任。

## S07

**优化、训练状态与保存恢复。** 用于 D015/D017/D021/D022/D034/D035。

[Optimization 教程](https://docs.pytorch.org/tutorials/beginner/basics/optimization_tutorial.html)；[SGD](https://docs.pytorch.org/docs/2.14/generated/torch.optim.SGD.html)；[AdamW](https://docs.pytorch.org/docs/2.14/generated/torch.optim.AdamW.html)；[Saving and Loading Models](https://docs.pytorch.org/tutorials/beginner/saving_loading_models.html)。教程示意不替代项目的完整安全加载、配置和恢复策略。

## S08

**分类损失与 logits。** 用于 D023/D031/D032。

[CrossEntropyLoss](https://docs.pytorch.org/docs/2.14/generated/torch.nn.CrossEntropyLoss.html)。核对类别轴、原始 logits 输入、ignore_index、权重与 reduction；本卡简单平均示例明确不含所有加权变体。

## S09

**归一化。** 用于 D029。

[LayerNorm](https://docs.pytorch.org/docs/2.14/generated/torch.nn.LayerNorm.html)；[RMSNorm](https://docs.pytorch.org/docs/2.14/generated/torch.nn.RMSNorm.html)。关注 normalized_shape、当前输入统计、epsilon 和可学习参数，不把常见使用轴当成 API 唯一能力。

## S10

**因果语言模型与训练目标。** 用于 D030–D036。

[Hugging Face Causal language modeling](https://huggingface.co/docs/transformers/tasks/language_modeling)。重点核查 token 标签、损失与训练/生成的职责；label shift 在模型或数据侧执行需按实际实现确认。

## S11

**生成策略。** 用于 D038。

[Generation strategies](https://huggingface.co/docs/transformers/generation_strategies)。Temperature、Top-K/Top-P、EOS 与采样的具体边界配置依实现；低温不被当作事实正确性保证。

## S12

**KV Cache 与推理成本。** 用于 D039/D041。

[KV cache strategies](https://huggingface.co/docs/transformers/kv_cache)。缓存布局、位置处理和策略以具体模型/版本为准；文档机制不能冒充用户设备上的加速测试。

## S13

**RoPE 与 GQA。** 用于 D040。

[RoFormer](https://arxiv.org/abs/2104.09864)；[GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245)。本卡二维旋转及缓存数量是教学例子，不是长上下文质量保证。

## S14

**Attention 访存优化。** 用于 D041。

[FlashAttention](https://arxiv.org/abs/2205.14135)。区分精确 Attention 的运算关系和显式中间量/访存成本，不将其说成通用线性复杂度替代。

## S15

**参数高效适配与偏好目标。** 用于 D042/D043。

[LoRA](https://arxiv.org/abs/2106.09685)；[Direct Preference Optimization](https://arxiv.org/abs/2305.18290)。本轮要求低秩增量小实验和目标/边界解释，不声称完成大型模型适配或完整 RLHF 实验。

## S16

**向量索引与检索/精排。** 用于 D048–D050 等。

[Faiss 官方文档](https://faiss.ai/)；[Sentence Transformers Retrieve & Re-Rank](https://www.sbert.net/examples/sentence_transformer/applications/retrieve_rerank/README.html)；[Elasticsearch Similarity / BM25](https://www.elastic.co/docs/reference/elasticsearch/index-settings/similarity)。需要区分索引近邻召回与业务证据召回，融合方式通过对照选择。

## S17

**LightRAG 机制。** 用于 D055/D056。

[LightRAG: Simple and Fast Retrieval-Augmented Generation](https://arxiv.org/abs/2410.05779)。实际源码单元应由 GitHub 连接器读取官方固定版本。未提供用户私有代码时，不声称审查过用户系统；GraphRAG 是更广的一类方案，不等于单一实现。

## S18

**Workflow、Agent 与工具编排。** 用于 D037/D058–D067/D071。

[Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)。用作工作流/自主控制、简单基线与工具工程的机制参考。具体状态机、错误码、业务审批方案属于本课程设计，不是统一行业协议。

## S19

**幂等与持久化执行。** 用于 D062/D063/D066/D078/D084。

[AWS Builders' Library: Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/)；[LangGraph Persistence](https://docs.langchain.com/oss/python/langgraph/persistence)。框架持久化仅作一个实现参照，不自动解决任意外部副作用一致性，也不构成固定选型推荐。

## S20

**MCP 规范与授权边界。** 用于 D068–D073。

[MCP specification 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28)；[Authorization](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization)。本次 latest 跳转到该版本；不是永久最新声明。Transport、协商、认证与取消细节实施时按固定规范和 SDK 校核，不把不同传输混用。

## S21

**Prompt Injection 与执行隔离。** 用于 D053/D060/D069/D072/D077/D083。

[OWASP LLM01: Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)；[Docker Engine security](https://docs.docker.com/engine/security/)。来源支持分层边界意识，不证明本项目已经具备生产安全。测试必须在授权隔离环境，不把 mock 拒绝当作真实 microVM 评估。

## S22

**Agent Evaluation。** 用于 D045/D054/D074–D076/D080/D085 等。

[Anthropic: Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)，发表于2026-01-09。核对 task、trial、grader、trace/outcome 与评价校准；本课程的题集规模、场景和通过门槛是本项目设计，不是从文章得到统计充分性保证。

## S23

**服务目标与工程可靠性。** 用于 D078–D080/D086。

[Google SRE: Service Level Objectives](https://sre.google/sre-book/service-level-objectives/)。帮助区分服务指标、目标与用户体验。具体 Gateway、发布策略和 Runbook 应由项目需求与实验验证，不由参考书自动保证。

## 使用限制

外部资料帮助核查技术；90张框架不是论文复制或版本永久快照。例子中数值、词表、假租户、价格和结果若标为教学示意，就不能引用为生产事实。正式实验需记录实际版本、配置、数据授权与结果，学习状态需另经独立/延迟验证。
