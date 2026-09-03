---
id: "037"
slug: evaluating-llms
style: serious
category: evaluation
difficulty: core
question: "How do you evaluate an LLM, and what are the common pitfalls?"
tags: [evaluation, benchmarks, elo, human-eval, task-specific-evals]
---

# Evaluating an LLM

There is no single number. Evaluation is a portfolio, and choosing the portfolio is the skill.

```
 ┌─ AUTOMATIC, REFERENCE-BASED ────────────────────────────────────────┐
 │  MMLU, GSM8K, HumanEval, GPQA, MATH, IFEval …                       │
 │  ✅ cheap, reproducible, comparable                                  │
 │  ❌ contamination, saturation, prompt-format sensitivity, ≠ your task │
 ├─ AUTOMATIC, REFERENCE-FREE ─────────────────────────────────────────┤
 │  perplexity; LLM-as-judge; verifiable checks (unit tests, parsers)   │
 │  ✅ scales, no labels; verifiable checks are genuinely trustworthy    │
 │  ❌ judges have biases; perplexity ≠ quality                          │
 ├─ HUMAN ─────────────────────────────────────────────────────────────┤
 │  pairwise preference, Likert rubrics, expert review, Arena Elo       │
 │  ✅ closest to what you actually mean by "good"                       │
 │  ❌ expensive, slow, noisy; ~70–80% inter-annotator agreement ceiling │
 ├─ PRODUCTION ────────────────────────────────────────────────────────┤
 │  A/B tests, task completion, thumbs-up rate, escalation rate, cost   │
 │  ✅ the only measurement of the thing you actually care about         │
 │  ❌ slow, confounded, needs traffic                                   │
 └─────────────────────────────────────────────────────────────────────┘
```

## The pitfalls

**1. Contamination.** Public benchmarks leak into training corpora. A jump on MMLU may be
memorisation. Detect it with n-gram overlap against training data, canary strings, or
**held-out/refreshed** variants (GSM1k, LiveBench, and similar recently-authored sets).

**2. Saturation and ceiling effects.** When frontier models score 88–92% on a benchmark, the
remaining gap is dominated by label errors. MMLU has a measurable fraction of wrong gold answers.
Above ~90%, you are measuring the annotators.

**3. Prompt-format sensitivity.** The same model can move 10+ points on MMLU depending on
answer-option ordering, whether it is scored by log-likelihood or generation, and the few-shot
template. Two papers reporting different numbers for the same model are usually both right.

**4. Benchmarks are not your task.** MMLU tells you almost nothing about whether the model can
handle your customer-support tickets. **Build a task-specific eval set** — even 100 hand-labelled
examples from your real distribution beat any public benchmark for a product decision.

**5. Single-number thinking.** A model can be better at reasoning and worse at instruction
following. Report a profile, and always alongside cost and latency.

**6. Evaluating only the happy path.** Test adversarial inputs, refusals, ambiguous requests,
non-English input, very long inputs, and malformed data. Production failures live there.

**7. No statistical rigour.** On 200 examples, a 3-point difference is noise. Report confidence
intervals; run multiple seeds; use paired tests since the same items are scored by both models.

## Building an eval you can trust

1. **Sample from real traffic**, not from your imagination. Your intuitions about the input
   distribution are wrong.
2. **Stratify** by the categories you care about, including rare-but-costly ones.
3. **Write the rubric before looking at outputs**, or you will rationalise.
4. **Hold out a private set.** Anything you optimise against stops being a measurement.
5. **Version it.** Eval sets change; results are only comparable within a version.
6. **Measure inter-annotator agreement.** If humans agree only 60%, no model can score above that
   ceiling and your rubric needs work.

## What an interviewer digs into next

* How would you detect contamination without access to the training data?
* Why does prompt format move benchmark scores so much?
* You have 500 support tickets and a week. Describe your eval.
* How do you decide whether a 2-point benchmark gain is real?
