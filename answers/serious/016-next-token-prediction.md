---
id: "016"
slug: next-token-prediction
style: serious
category: fundamentals
difficulty: core
question: "How does next-token prediction produce something that looks like reasoning?"
tags: [autoregressive, language-modelling, compression, chain-of-thought]
---

# Why next-token prediction gets you so far

The objective is almost insultingly simple: maximise `Σ log P(x_t | x_<t)` over a corpus. The
question is why that produces translation, code, and multi-step reasoning.

## Compression demands understanding

Predicting the next token well over a corpus of everything humans have written **requires
modelling whatever generated that text**. Consider what it takes to place high probability on
the final token of each:

```
   "The capital of France is ___"                → factual recall
   "def fib(n): return fib(n-1) + fib(___"       → code semantics, scope
   "2 + 2 = ___"                                 → arithmetic
   "Alice put the key in her bag. Later, Alice
    reached into her ___"                        → entity + state tracking
   "The murderer, it turned out, was the ___"    → narrative-scale inference
```

None of these can be nailed by n-gram statistics. Low loss on the last one, in particular,
requires something functionally like following a plot. Shannon's framing is the useful one:
**compression and prediction are the same problem**, and to compress human text well you must
model the structure that produced it. Sutskever's phrasing — "predicting the next token well
means understanding the process that produced it" — is the same claim.

## The scale of the supervision

Every position is a labelled example. A trillion-token corpus is a trillion supervised
prediction problems, covering every topic, register, language and format humans write in, all
for free. No other objective gets that much signal that cheaply — this is the real reason
decoder-only won.

## Where "reasoning" comes from mechanically

* **Induction heads** implement in-context copying and pattern completion, which is the
  substrate for few-shot learning.
* **Chain-of-thought** matters because a transformer does a *fixed* amount of computation per
  token. A hard problem may need more serial steps than one forward pass provides — so the model
  writes intermediate results into the context and reads them back, using the token stream as
  scratch memory. This converts a depth limit into a length budget, and is why "think step by
  step" is not a mystical incantation but a compute allocation.
* **In-context learning** emerges because the training corpus contains countless passages where
  a pattern is established and then continued; learning to do that generally is just good
  next-token prediction.

## The honest limitations

* **No planning across tokens.** Generation is greedy in structure: the model commits to token
  `t` before considering `t+1`. Anything requiring backtracking must be simulated in the token
  stream.
* **Exposure bias.** Training conditions on ground truth; generation conditions on the model's
  own output, so errors compound.
* **Fitting the data distribution includes its errors.** The objective rewards predicting what a
  human *would* write, including confident nonsense. Truthfulness is not in the loss.
* **A fixed compute budget per token**, regardless of whether the token is `the` or the answer to
  a hard question. Reasoning models address exactly this by spending many tokens before
  answering.

Post-training (SFT, RLHF) is what turns a distribution-matcher into an assistant. The knowledge
comes from pretraining; the behaviour does not.

## What an interviewer digs into next

* Why is compression equivalent to prediction?
* Why does chain-of-thought increase effective compute, given fixed model depth?
* What does the model do when the correct continuation is genuinely uncertain?
* If next-token prediction is so general, why is post-training needed at all?
