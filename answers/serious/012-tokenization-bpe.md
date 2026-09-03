---
id: "012"
slug: tokenization-bpe
style: serious
category: nlp
difficulty: core
question: "What is tokenization? Explain BPE and why token boundaries cause weird model behaviour."
tags: [tokenization, bpe, sentencepiece, vocabulary, unicode]
---

# Tokenization and BPE

A model cannot consume text; it consumes integers indexing an embedding table. Tokenization is
the map from strings to those integers, and the choice of map is a genuine architectural
decision with visible consequences.

The extremes are both bad:

* **Characters** — tiny vocabulary, no out-of-vocabulary problem, but sequences become 4–5×
  longer, and attention is quadratic in length.
* **Words** — short sequences, but an unbounded vocabulary, a huge embedding table, and every
  typo, name, and morphological variant becomes `[UNK]`.

**Subword** tokenization sits between: common words stay whole, rare words decompose into
pieces. Nothing is ever out-of-vocabulary because the base characters (or bytes) are always
present.

## Byte-Pair Encoding

BPE ([Sennrich et al., 2015](https://arxiv.org/abs/1508.07909), adapting a 1994 compression
algorithm) learns the vocabulary greedily from a corpus:

```
  Start:   every character is a token.
  Repeat:  find the most frequent adjacent pair; merge it into a new token;
           record the merge rule. Stop at the target vocab size.

  corpus: "low low lower newest widest"

  step 0   l o w _ l o w _ l o w e r _ n e w e s t _ w i d e s t
  step 1   pair ("e","s") ×2  →  merge          ... n e w es t ... w i d es t
  step 2   pair ("es","t") ×2 →  merge          ... n e w est ... w i d est
  step 3   pair ("l","o")  ×3 →  merge          lo w _ lo w _ lo w e r ...
  step 4   pair ("lo","w") ×3 →  merge          low _ low _ low e r ...

  final vocab: {l,o,w,e,r,n,s,t,i,d,_, es, est, lo, low, ...}
  merge list is ORDERED — encoding replays it in the same order.
```

**Byte-level BPE** (GPT-2 onward) starts from the 256 possible *bytes* rather than Unicode
characters, so any string in any language, plus emoji and binary junk, is representable with
zero `[UNK]`. **SentencePiece** treats the raw string including spaces as the unit (encoding a
leading space as `▁`), which makes tokenization reversible and language-agnostic — important for
languages that do not delimit words with spaces. **WordPiece** (BERT) is BPE's cousin: it merges
the pair that maximises corpus likelihood rather than raw frequency.

## Why tokenization causes visible weirdness

Almost every "LLMs are dumb" party trick is a tokenization artifact:

* **Counting letters.** *"How many r's in strawberry?"* The model sees `str|aw|berry`, not
  letters. Asking it to count characters is asking it to introspect a representation it never
  had.
* **Arithmetic.** `1234` may tokenize as `12|34`, `123|4`, or `1|234` depending on context, so
  digit alignment for carrying is inconsistent. Models that tokenize digits individually
  (or right-to-left in groups of three) do measurably better arithmetic.
* **Reversal and spelling tasks** fail for the same reason as counting.
* **The prompt-boundary trap.** `"Hello"` and `" Hello"` are *different tokens*. A prompt ending
  in a trailing space puts the model in a state its training data rarely contains, and quality
  drops. This is why chat templates are picky about whitespace.
* **Glitch tokens.** Strings like `SolidGoldMagikarp` — present in the tokenizer's training
  corpus but nearly absent from the LM's — have essentially untrained embeddings and produce
  bizarre outputs.
* **Multilingual tax.** A tokenizer fit mostly on English spends 2–4× more tokens on the same
  meaning in Thai, Hindi or Burmese. That is directly more cost, more latency, and less
  effective context for those users — a real fairness issue, not a curiosity.

## Practical implications

* Vocabulary size trades embedding/softmax parameters against sequence length. 32k–256k is the
  usual band; larger vocabularies have become more attractive as context costs rose.
* You **cannot** change the tokenizer of a trained model without retraining the embedding and
  output layers.
* Token counts, not word counts, drive cost. Code, JSON and non-Latin scripts are denser in
  tokens than prose.

## What an interviewer digs into next

* Why byte-level rather than character-level BPE?
* Why is BPE's merge list order-dependent, and what happens if you apply merges out of order?
* How would you design a tokenizer to make arithmetic work better?
* What is a glitch token and what does it tell you about embedding initialisation?
