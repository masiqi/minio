# Day 1 — RNN Structural Limitations → Why Attention

Date: 2026-09-29

## Learning objective

Build a causal mental model for why Attention was needed before learning Q/K/V implementation details.

## Core takeaways

1. RNN does not re-read every prior token at each step. It combines the current input with the previous hidden state.
2. Historical information must travel through sequential hidden-state transitions. Long-distance dependencies therefore have long information paths.
3. LSTM/GRU improve the ability to preserve useful information, but recurrence and sequential dependency remain.
4. Attention changes the interaction pattern: a token can directly gather information from relevant positions rather than requiring that information to traverse the entire recurrent chain.
5. Removing recurrent dependency also improves training parallelism.
6. Attention does not mean sequence length is free; standard self-attention has important length-related compute/memory costs.

## Important distinctions discovered today

### Hidden state

A hidden state is a learned vector representation carrying information from previous recurrent steps. It is not a literal copy or ZIP archive of the previous text.

### Fixed token importance vs dynamic relevance

Incorrect initial model: each token owns a fixed attention weight.

Correct direction: attention relevance is computed dynamically between positions in the current context. The same token can receive different attention depending on which position is querying and what the surrounding context is.

### Token embedding vs contextual representation

Two occurrences of the same token may start with the same token embedding. Different positions and different contextual interactions can cause their later Transformer representations to diverge.

## Feynman result

Final learner explanation captured the required causal chain:

- long sequential processing can weaken the effective use of early information;
- Attention shortens the information-interaction path;
- relevant earlier information can be used more directly.

Day 1 minimum acceptance: PASSED.

## Remaining gaps to revisit

- Hidden state needs another retrieval/review to become fluent.
- LSTM/GRU mechanism is not yet learned; only the role relative to recurrence is needed at this stage.
- Do not describe Attention as having no path.
- Do not describe attention weights as token-owned fixed values.
- Q/K/V mechanism is intentionally deferred to Day 2.

---

# Day 2 Prework — Self-Attention and Q/K/V

Target time: 20–30 minutes.

## Goal

Do not memorize the attention formula. Arrive at Day 2 able to reason about the problem Q/K/V is designed to solve.

## Read / think in this order

### 1. Reconstruct Day 1 from memory — 3 minutes

Without notes, answer aloud:

- Why is long-distance information interaction structurally difficult in an RNN?
- What does LSTM improve, and what structural limitation remains?
- What does Attention change about the information path?

### 2. Establish the input mental model — 5 minutes

Review only this pipeline:

Text → tokenizer → token IDs → token embeddings → positional information → Transformer processing → contextual representations

Questions to bring to class:

- If two identical tokens start with the same embedding, what information can distinguish their roles?
- Why is a token embedding alone insufficient to represent meaning in context?

### 3. Build Q/K/V intuition — 10 minutes

Use an information-retrieval analogy, but do not treat it as a literal implementation:

- Query: what information am I looking for right now?
- Key: what kind of information might this position match/provide?
- Value: if this position is relevant, what information should actually be passed onward?

Think about why matching and transferred content might need separate representations.

Example:

"I have a bank card. I got another card for my child. Yesterday my child found that it did not work."

For the position corresponding to "it":

- What is it trying to resolve?
- Which earlier positions should be candidates?
- Why should the mechanism first determine relevance and then aggregate useful information?

Do not calculate numbers yet.

### 4. Optional formula preview — maximum 5 minutes

You may look at the scaled dot-product attention formula once, only to recognize its shape. Do not memorize it yet.

Questions to notice:

- Which part appears to compute relevance?
- Which part appears to carry content?
- Why might softmax be used?

Day 3 will cover the detailed computation, scaling, softmax, weighted sum, and multi-head attention.

## Day 2 diagnostic questions

Come prepared to answer these without notes:

1. Why not use the same vector directly for everything instead of creating Q, K, and V?
2. What conceptual job is done by Q–K interaction?
3. Why is V needed after relevance has already been computed?
4. Why are Q/K/V learned projections rather than three unrelated copies of text?

These are diagnostic questions, not homework requiring perfect answers.

## Suggested primary reference

Read the Transformer paper's model/attention sections selectively rather than reading the whole paper. Focus on the motivation and the definition of scaled dot-product attention. Use a visual explainer only as a secondary aid.

## Day 2 acceptance target

By the end of Day 2, independently explain:

- what Self-Attention is trying to compute;
- the conceptual roles of Q, K, and V;
- why Q/K determine dynamic relevance while V carries information to be aggregated;
- how this produces context-dependent representations;
- what parts are analogy versus the actual mathematical mechanism.
