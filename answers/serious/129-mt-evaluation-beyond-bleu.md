---
id: "129"
slug: mt-evaluation-beyond-bleu
style: serious
category: translation
difficulty: intermediate
question: "Why is BLEU a poor metric for modern machine translation, and what replaced it?"
tags: [bleu, chrf, comet, bleurt, sacrebleu, mqm, wmt]
---

# Evaluating machine translation after BLEU

BLEU was published in 2002 and it did its job: it correlated well enough with human judgement to
let a field iterate. Modern systems have moved past the range where it discriminates, and using it
to compare them is now actively misleading.

## What BLEU actually computes

Modified n-gram precision against one or more references, geometrically averaged over n = 1..4,
multiplied by a brevity penalty.

```
   reference : the cat sat on the mat
   candidate : the cat sat upon the mat        ← a perfectly good translation

   1-grams  5/6      2-grams  3/5      3-grams  1/4      4-grams  0/3
                                                          ▲
                                             one word swapped, and the 4-gram
                                             precision is ZERO. BLEU collapses.
```

The failure modes follow directly from the definition:

* **Paraphrase is punished.** Any correct rewording that breaks a 4-gram costs heavily. This
  matters more as systems get better, because better systems paraphrase more.
* **One reference is not the answer set.** There are many correct translations; BLEU knows one.
* **Morphology is invisible.** A word inflected almost-correctly scores exactly the same as a
  completely wrong word — catastrophic for morphologically rich languages (question 113).
* **Word order is barely modelled.** Beyond 4-grams, BLEU cannot see structure at all.
* **It is tokenisation-dependent**, so two papers' BLEU scores are frequently not comparable. This
  is what **sacreBLEU** exists to fix: a fixed tokenisation and a version string you must report.
* **Corpus-level, not segment-level.** BLEU on a single sentence is close to meaningless, which
  rules out using it for per-example analysis or quality gating.

## What to use instead

| Metric | What it is | When |
| --- | --- | --- |
| **chrF / chrF++** | character n-gram F-score | strong cheap default, especially for morphologically rich and agglutinative languages |
| **COMET** | neural, trained on human judgements, uses source + hypothesis + reference | the current standard for system comparison |
| **COMET-QE / reference-free COMET** | same, without a reference | when no reference exists (question 132) |
| **BLEURT** | neural regression on human ratings | similar role to COMET |
| **MQM** | human annotation with typed, severity-weighted errors | the gold standard everything else is validated against |

The WMT metrics shared tasks have found the same result repeatedly: **neural metrics correlate far
better with human judgement than BLEU**, and the gap widens as systems improve. BLEU's remaining
legitimate uses are as a cheap regression check during development, and for comparability with old
literature — clearly labelled as such.

## MQM is the thing to understand

Multidimensional Quality Metrics is not automatic. Trained annotators mark **spans** with an error
category (accuracy: mistranslation, omission, addition; fluency: grammar, register; terminology;
locale) and a **severity** (neutral / minor / major / critical). The score is a weighted penalty
sum.

Why it matters even if you never run it: it is the human signal that COMET and BLEURT are trained
and validated on, and it captures the thing automatic metrics structurally cannot — that a
**critical error** (a negation dropped, a dosage changed, a name swapped) is not "a bit worse" than
a clumsy phrasing. It is categorically different, and every averaged metric hides exactly that.

## Practical rules

* Report **COMET and chrF**, plus BLEU only for continuity. State the sacreBLEU signature and the
  COMET model version — COMET scores are not comparable across model versions.
* **Test for significance.** Paired bootstrap resampling. Differences under roughly one BLEU point
  on a normal test set are usually noise, and people ship on them constantly.
* **Check for contamination.** Public test sets (WMT, FLORES) are in web crawls. A model that has
  memorised the test set scores beautifully and translates nothing.
* **Do not average across language pairs.** A mean over pairs hides that the system is excellent
  into English and poor out of it, which is the single most common asymmetry in MT.
* **Look at outputs.** Read fifty segments. Every automatic metric will miss the failure that a
  reader notices in the first minute.

## What an interviewer digs into next

* Why does BLEU get *worse* as a metric as systems improve?
* What does chrF fix, and for which languages specifically?
* Why can't an averaged metric represent a critical error?
* How would you check a new metric is not just measuring fluency?
