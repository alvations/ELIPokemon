---
id: "260"
slug: decoding-parameter-interactions
style: serious
category: optimization
difficulty: intermediate
question: "Walk me through temperature, top-k, top-p, min-p and the repetition penalties. Which of them interact badly, and why is a 'creative' preset not one dial?"
tags: [sampling, temperature, min-p, repetition-penalty, decoding]
---

# Three families, one pipeline, a fixed order

Question 034 covers what each parameter is. This one is about what they do to each other. The
useful frame is that they are not five settings on one axis of "creativity" — they are three
different operations applied in a fixed sequence to the same vector of logits:

1. **History edits.** Repetition, frequency and presence penalties, and n-gram blocking. They
   change logits based on what has already been emitted.
2. **Shape.** Temperature. Monotone, order-preserving, applied to every logit.
3. **Support truncation.** top-k, top-p, min-p, typical, top-h. They delete candidates.

The order is not a matter of taste; it is in the serving code. In `transformers`,
`_get_logits_processor` appends the repetition penalty and n-gram blocking first, then — and only
when `do_sample` is true — temperature, top-h, top-k, top-p, min-p, typical, epsilon and eta, in
that order (read first-hand from `src/transformers/generation/utils.py`; other engines are close
but not identical, which is itself a portability hazard).

```
  logits ─► repetition / frequency / presence penalty      (raw logit space)
         ─► no-repeat-ngram, grammar and other masks
         ─► [ only if do_sample=True ] ────────────────────────────────────┐
              temperature   z / T                                          │
              top-h         keep until cumulative entropy > H(p)·top_h     │
              top-k         keep the k largest                             │
              top-p         keep the smallest prefix with Σp ≥ p           │
              min-p         keep p_i ≥ min_p · p_max                       │
              typical       keep |−log p_i − H| smallest until Σp ≥ mass   │
         ─────────────────────────────────────────────────────────────────┘
         ─► sample

  Every truncation is an INTERSECTION with the ones above it.
  Whatever survives all of them is renormalised, and that is what you sample from.
```

## The mechanics that actually matter

**Temperature** divides logits by `T` before softmax. It never reorders. Because it is
multiplicative in logit space, it rescales *every* gap — including the gaps that the penalties
just created, and including the gaps that the thresholds below are about to measure.

**top-k** keeps a fixed count and is blind to entropy. **top-p** keeps the smallest prefix whose
cumulative mass reaches `p`, so it widens when the model is unsure. Both are applied here in that
order, which means `top_k` is a hard ceiling `top_p` can only tighten.

**min-p** keeps every token with `p_i ≥ min_p · p_max`: a threshold *relative to the leader*
rather than a cumulative mass. `transformers` computes it on the post-temperature softmax, and the
code carries a comment saying so deliberately. That is the interaction people miss: raising
temperature flattens the distribution, which raises the small probabilities relative to `p_max`,
which widens the min-p nucleus. Temperature moves min-p twice.

**Typical sampling** is the odd one out and the reason "top-anything" is a bad mental model. It
ranks tokens by `|−log p_i − H(p)|` — distance from the distribution's own entropy — and keeps the
closest until the mass threshold is met. **It can discard the most probable token**, because a
token that is far *less* surprising than average is as atypical as one that is far more
surprising. If you were reasoning about it as "another nucleus", you were wrong about its support.

**top-h**, newer, keeps tokens in probability order until *cumulative entropy* exceeds
`τ = H(p) · top_h`, capped at the top 100 candidates for numerical stability.

**The penalties are two different things wearing one name.** `transformers`'
`RepetitionPenaltyLogitsProcessor` does `z / penalty` when `z > 0` and `z × penalty` when `z < 0`
— so the size of the nudge depends on the sign and magnitude of the logit, and it is not a uniform
shift. OpenAI-style `frequency_penalty` and `presence_penalty` subtract `α × count` and `β ×
1[seen]` from the logit, which *is* uniform. Do not port a value from one to the other.

## The interactions that bite

* **`do_sample=False` silently discards every sampling parameter.** In `transformers` the entire
  warper block is inside `if generation_config.do_sample:`. A config with `temperature=0.7` and
  greedy decoding is a greedy config, and nothing warns you.
* **Temperature reweights the repetition penalty.** The penalty is applied to raw logits and
  temperature divides afterwards, so the effective strength scales like `penalty^(1/T)`. Lower the
  temperature and the same penalty bites harder; raise it and the penalty fades. Tuning `T` after
  tuning `penalty` invalidates the penalty.
* **The repetition penalty includes the prompt by default.** In `transformers` this is explicit in
  the docstring, with `prompt_ignore_length` as the opt-out. Consequences: the penalty's strength
  varies with prompt length, and verbatim quoting, summarisation and any task that must re-use the
  input's vocabulary degrade. The same setting is quietly a different setting for a 200-token and
  a 20,000-token prompt.
* **Penalties and structured output are close to incompatible.** JSON needs `"`, `,`, `}` and
  repeated key names; code needs `self`, indentation and closing brackets. A penalty of 1.2 over a
  long output pushes the model off its own syntax. If you are generating structure, use a grammar
  (question 262) and set the penalties to neutral.
* **Stacking truncations collapses to greedy by accident.** `top_k=20` with `top_p=0.8` and
  `min_p=0.1` is an intersection of three rules; on a confident step, all three cut to the same
  single token, and only `min_tokens_to_keep` stops the support from emptying.
* **Engines disagree on order.** A preset that behaves one way in `transformers` and another in a
  C++ or Rust server is not a bug in either; it is the pipeline order differing. Pin the engine
  when you pin the numbers.

## Why "creative" is not one dial

Creativity in generation decomposes into at least three independent questions, and a preset that
moves one of them does not move the others:

| Axis | Controlled by | Failure if you only move this |
| --- | --- | --- |
| **What is admissible at all** | top-k, top-p, min-p, typical | Tail risk: rare tokens that break the register |
| **How flat the admissible region is** | temperature | Wobble inside the same small vocabulary |
| **Pressure away from what has been said** | repetition / frequency / presence | Synonym churn and topic drift, not new ideas |

Raising temperature alone with `top_p = 0.9` mostly redistributes mass *within* an unchanged
nucleus: you get a different word, not a different idea. Raising penalties alone produces text
that avoids repeating itself and has nothing new to say. And none of the three touches the thing
people usually mean by creative — the *plan* — which lives in the prompt, in sampling several
candidates and selecting among them, or in a reasoning budget.

**How to tune.** Fix everything else, move one parameter, and measure on a task metric rather than
by reading three samples. Prefer one truncation rule, not three. min-p at 0.05–0.1 with a higher
temperature is a reasonable modern default for open-ended text; greedy or near-greedy with neutral
penalties for anything structured.

## What an interviewer digs into next

* Why is min-p computed after temperature, and what does that do to your preset?
* What does the repetition penalty do to a long prompt you are asked to quote from?
* Which truncation rule can drop the argmax, and why?
* What does `temperature` mean when `do_sample` is false?

## Where this stands, September 2026

The pipeline order, the sign-dependent repetition penalty, the `do_sample` guard, the
post-temperature min-p and the top-h rule are all **primary**: read directly from the current
`transformers` sources in this session. Everything about other engines is coverage — check the
order in the engine you actually serve on. The maths of temperature and truncation is stable and
will outlive every default in this answer.
