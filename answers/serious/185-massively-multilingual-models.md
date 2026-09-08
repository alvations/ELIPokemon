---
id: "185"
slug: massively-multilingual-models
style: serious
category: translation
difficulty: advanced
question: "What does it actually mean to say a model supports 200 languages?"
tags: [nllb, coverage-claims, long-tail, per-language-reporting, moe, deployment-threshold]
---

# "Supports 200 languages"

This is the most load-bearing unexamined claim in multilingual NLP. It is usually true in the sense
that the model **produces output** for 200 languages, and false in every sense a user cares about.

## What the claim conceals

```
   200 languages "supported"

   ~15    genuinely good: enough data, evaluated properly, usable for real work
   ~40    usable with caveats: fine for gist, unreliable for anything consequential
   ~100   produces fluent output whose relationship to the source is uncertain
   ~45    output is confidently wrong often enough to be actively harmful

   the marketing number is 200. The number of rows a user can rely on is the first one.
```

The tail is not a slightly worse version of the head. It fails **differently**: off-target output
(question 136), hallucination under weak source representation, and a quality profile that a user
of that language cannot easily distinguish from the good cases, because fluency survives long after
accuracy has gone.

## What genuinely helps at this scale

* **Language-aware capacity.** The curse of multilinguality (question 103) is a capacity problem, so
  the fixes are capacity fixes: sparse mixture-of-experts with language-informed routing, language
  adapters (question 110), or simply a bigger model. All of them buy back some of the tail.
* **Non-English-centric data.** Mining direct pairs rather than routing everything through English
  (question 130). NLLB's contribution was substantially a data contribution.
* **Sampling that does not drown the tail** (question 104) — temperature-sampled language
  distributions rather than proportional.
* **Script-aware vocabulary** so tail languages are not shredded into bytes (questions 102, 112).

## The reporting standard to hold yourself to

* **Publish per-language scores, always.** An average over 200 languages is dominated by the head
  and is not a summary of anything. Publish the distribution and the worst decile.
* **State the evaluation source for each language** — FLORES for most, which is one narrow domain
  (question 130), and say so.
* **Say which languages were evaluated by speakers** and which only by automatic metric. For a tail
  language, the automatic metric is itself untrustworthy (question 129).
* **Distinguish the four tiers above in your documentation**, in the model card, not in a footnote.

## The deployment question

The honest framing is not "do we support this language" but **"what would a speaker of this language
be able to rely on this for?"** Gisting an inbound message is a different bar from translating a
medical instruction (question 187).

So: set a quality threshold per use case, measure per language against it, and **make the tiering
visible in the product**. A system that silently gives the same interface for a language it handles
well and one it handles badly has transferred the entire risk to the user, who has no way to know.

And accept that for some languages the right answer is **not to offer it yet**, with an explanation.
That is more respectful of a speaker than fluent, confident nonsense.

## What an interviewer digs into next

* Why is an average over 200 languages not a summary?
* Why is the tail's failure mode different rather than just worse?
* What does language-informed MoE routing buy, and what does it not fix?
* How would you make quality tiering visible to a user?
