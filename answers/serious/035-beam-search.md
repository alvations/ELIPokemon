---
id: "035"
slug: beam-search
style: serious
category: inference
difficulty: intermediate
question: "What is beam search and why is it rarely used for open-ended chat?"
tags: [beam-search, decoding, likelihood-trap, translation, degeneration]
---

# Beam search

Beam search keeps the `k` highest-scoring **partial sequences** at each step instead of committing
to one token, approximating a search for the most likely full sequence rather than the most likely
next token.

```
   beam width k = 2

   start
     ├── "The"  (-0.2) ────┬── "The cat"   (-0.5) ──┬── "The cat sat" (-0.9) ✅
     │                     │                        └── "The cat ran" (-1.4)
     │                     └── "The dog"   (-1.1) ──┬── "The dog sat" (-1.6)
     └── "A"    (-1.8) ✂️  pruned                    └── ...
         (dropped: outside the top 2 at this depth)

   score = Σ log P(token)  — kept beams are the top-k by cumulative log-prob
```

Greedy decoding is beam search with `k = 1`. Beam search fixes greedy's specific failure: a
locally-optimal token that leads into a bad continuation. With a beam you keep the alternative
alive long enough to see where it goes.

## Length normalisation

Every additional token adds a negative log-probability, so raw cumulative score favours short
sequences. Standard practice divides by a length penalty:

$$\text{score} = \frac{1}{|y|^\alpha}\sum_t \log P(y_t \mid y_{<t}), \qquad \alpha \approx 0.6\text{–}1.0$$

Getting `α` wrong is a classic bug: too low and outputs truncate early, too high and they ramble.

## Why it works for translation and fails for chat

Beam search is still standard in **machine translation and speech recognition**, and it is
genuinely better there. The reason is that those tasks are **low-entropy**: given the source, there
is essentially one correct output, and the goal really is to find the highest-probability sequence.

Open-ended generation is **high-entropy**: there are thousands of good continuations. And here the
objective itself is wrong — [Holtzman et al. (2019)](https://arxiv.org/abs/1904.09751) showed that
the most probable sequence is *not* the most human-like one. Human text has fairly high, fairly
*variable* surprisal; maximum-likelihood text has uniformly low surprisal, and reads as flat,
generic and repetitive.

```
   per-token surprisal

   human writing:  ▂▅▁▇▃▂▆▁▄▇▂▅▁▃   varied — sometimes surprising
   beam search:    ▂▂▁▂▂▁▂▂▂▁▂▂▂▂   uniformly safe — the "likelihood trap"
```

This is the **likelihood trap**: optimising harder for probability makes text worse. Beam search
also actively collapses diversity (the `k` beams typically differ by a word or two), costs `k`×
compute and `k`× KV cache, and interacts badly with the length bias above.

## Where beam search still appears in LLM work

* Constrained decoding, where you must find a sequence satisfying a grammar or schema.
* Short structured outputs — SQL, JSON, function-call arguments.
* Any task with one right answer and a scoring function you trust.
* **Diverse beam search** and **best-of-n with a reranker** are the modern relatives: generate
  several complete candidates by *sampling*, then pick with a verifier or reward model. That
  separates exploration (sampling) from selection (scoring), which is what beam search conflates.

## What an interviewer digs into next

* Why does length normalisation matter, and what does `α` do?
* Explain the likelihood trap and why it does not affect translation.
* How is best-of-n reranking different from beam search, and why is it preferred?
* What are the memory implications of beam width `k` at inference?
