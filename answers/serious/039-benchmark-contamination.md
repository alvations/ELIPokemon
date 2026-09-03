---
id: "039"
slug: benchmark-contamination
style: serious
category: evaluation
difficulty: intermediate
question: "What is benchmark contamination and how do you detect it?"
tags: [contamination, data-leakage, canary, livebench, memorisation]
---

# Benchmark contamination

Contamination is test data appearing in training data. Since pretraining corpora are web-scale
scrapes and benchmarks live on the public web — in the original repository, in papers, in blog
posts, in Hugging Face datasets, in Stack Overflow answers — the default assumption for any
benchmark more than a year or two old should be that it is **partially contaminated**.

The consequence is not a slightly inflated score. It is that the benchmark stops measuring
generalisation and starts measuring memorisation, which is precisely the capability you did not
want to measure.

## Flavours

| Type | Description |
| --- | --- |
| **Direct** | The exact test items are in the training corpus. |
| **Indirect** | Paraphrases, translations, or discussions of the items are. |
| **Solution leakage** | The questions are absent but worked solutions are present. |
| **Distributional** | Not the items, but a very similar synthetic set generated from them. |
| **Post-hoc** | Contamination introduced *after* release, e.g. via user-submitted evaluation traffic. |

## Detection

**With training-data access:**
* n-gram overlap (e.g. any 13-gram from the test item appearing in training) — the standard method.
* Exact and near-duplicate hashing (MinHash/LSH).
* **Canary strings** — a unique GUID embedded in the benchmark file. If the model can reproduce it,
  the file was in the corpus. BIG-bench pioneered this. Cheap, and everyone should do it.

**Without training-data access** (the realistic case for API models):
* **Order sensitivity.** For a multiple-choice set, a clean model's accuracy should not depend on
  the order of the *examples*. A contaminated model has memorised the canonical ordering and drops
  measurably when the set is shuffled ([Oren et al., 2023](https://arxiv.org/abs/2310.17623)).
* **Guided prompting.** Ask the model to complete an item given only its first half plus the
  dataset name. Verbatim reproduction of the rest is strong evidence.
* **Perplexity gap.** Anomalously low perplexity on the benchmark relative to comparable text.
* **Membership inference** via min-k% probability of the rarest tokens.
* **Performance discontinuity by date.** Score on items published before the training cutoff
  versus after. A large gap is the cleanest signal available, and it is what
  [LiveCodeBench](https://arxiv.org/abs/2403.07974) is built on.

## Mitigation

* **Freshly authored benchmarks** with a hard release date after training cutoffs: LiveBench,
  LiveCodeBench, GSM1k (a from-scratch reconstruction of GSM8K that revealed accuracy drops of up
  to 13 points for some model families — direct evidence of contamination in the original).
* **Private held-out sets** administered by a third party.
* **Dynamic benchmarks** with rotating items.
* **Perturbation**: change names, numbers, and surface form. A model that understood the problem is
  unaffected; a model that memorised it degrades.
* **Canaries in every new benchmark**, plus a machine-readable no-train declaration (which is
  advisory only, but establishes intent).

## The honest framing for an interview

Contamination is **not** primarily an integrity problem — most of it is accidental, and complete
avoidance is impossible when training on the open web. It is a *measurement validity* problem. The
right response is not accusation but methodology: prefer fresh and private evals, report contamination
checks alongside scores, treat any single public benchmark number as weak evidence, and — for
product decisions — evaluate on your own data, which has the useful property of not being on the
internet.

## What an interviewer digs into next

* How does the order-sensitivity test work, and why does it indicate memorisation?
* Why is contamination hard to fully avoid even with good intentions?
* What did GSM1k demonstrate?
* Design a contamination-resistant evaluation for a coding assistant.
