---
id: "004"
slug: encoder-decoder-vs-decoder-only
style: serious
category: transformers
difficulty: core
question: "What is the difference between encoder-only, decoder-only, and encoder-decoder architectures?"
tags: [bert, gpt, t5, architecture, causal-mask]
---

# Encoder-only vs decoder-only vs encoder-decoder

All three are stacks of the same transformer block. What differs is the **attention mask** and
therefore the training objective they can support.

```
 ENCODER-ONLY (BERT)          DECODER-ONLY (GPT)         ENCODER-DECODER (T5)
 ────────────────────         ──────────────────         ────────────────────
  bidirectional mask           causal mask                encoder: bidirectional
  every token sees all         token i sees ≤ i           decoder: causal
                                                          + cross-attention

   ┌─┬─┬─┬─┐                   ┌─┐                        ┌─────────┐
   │▓│▓│▓│▓│  t1               │▓│░│░│░│  t1              │ ENCODER │◄── source
   │▓│▓│▓│▓│  t2               │▓│▓│░│░│  t2              └────┬────┘
   │▓│▓│▓│▓│  t3               │▓│▓│▓│░│  t3                   │ K,V
   │▓│▓│▓│▓│  t4               │▓│▓│▓│▓│  t4              ┌────▼────┐
   └─┴─┴─┴─┘                   └─┴─┴─┴─┘                  │ DECODER │──► target
   ▓ = can attend              ░ = masked out             └─────────┘

  objective: MLM              objective: next token       objective: seq2seq
  output: one vector/token    output: a distribution      output: a distribution
  use: classify, embed        use: generate anything      use: translate, summarise
```

## Encoder-only

Every token attends in both directions, so representations are maximally contextual — a token
knows its right-hand context too. Trained with **masked language modelling**: corrupt ~15% of
tokens, predict them. Great for classification, NER, retrieval embeddings, reranking. Cannot
generate autoregressively, because there is no valid way to sample a sequence when every
position depends on positions that do not exist yet. BERT, RoBERTa, DeBERTa, and essentially
every modern embedding and cross-encoder model.

## Decoder-only

Causal mask. Trained on plain next-token prediction over raw text, which means **every token
is a training signal** — no 15% masking budget, no corruption scheme to design. This density,
plus the fact that any task can be written as text continuation, is why decoder-only won.

The apparent handicap — a token cannot see its right context — largely evaporates because
prompt tokens still see everything before them, and instructions are placed before the content
they govern. GPT, Llama, Mistral, Qwen, DeepSeek, and essentially every current chat model.

## Encoder-decoder

The encoder reads the source bidirectionally once; the decoder generates causally while
**cross-attending** to the encoder's keys and values. Trained with span corruption (T5) or
translation pairs. The inductive bias is a clean split between "understand this fixed input"
and "produce this variable output", which is genuinely well matched to translation, speech
recognition, and summarisation.

Costs: roughly 2× the parameters for a given depth (two stacks plus cross-attention), a more
complicated serving path, and no reuse of the source-side compute across turns of a
conversation.

## Why the field converged on decoder-only

1. **Objective density** — every position contributes loss.
2. **Task universality** — classification, extraction and translation are all just
   continuations, so one model and one serving stack covers everything.
3. **Simplicity at scale** — one stack, one mask, one kernel; easier to shard and to optimise.
4. **In-context learning** — prefix conditioning gives few-shot behaviour for free.
5. **KV caching** — the causal mask means past keys/values are immutable and reusable, which
   makes incremental decoding cheap.

Encoder-only models did not die; they moved to where bidirectionality is decisive and
generation is not needed — embeddings and rerankers. Encoder-decoders persist in speech and
translation, where the input/output asymmetry is real.

## What an interviewer digs into next

* Why can't you just sample from BERT? (Gibbs-style tricks exist and are bad — why?)
* What is a prefix-LM, and where does it sit between these three?
* Which architecture would you pick for a reranker, and why not a decoder?
* How does the causal mask make the KV cache possible?
