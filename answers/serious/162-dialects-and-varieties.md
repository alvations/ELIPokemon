---
id: "162"
slug: dialects-and-varieties
style: serious
category: translation
difficulty: advanced
question: "Why do language technologies fail on dialects and non-standard varieties?"
tags: [dialects, varieties, standard-language, normalisation, identification, fairness]
---

# Dialects and non-standard varieties

Almost every language technology is trained on a **standard written variety** — the one used in
news, government and Wikipedia. Most speech is not that. The gap between what people actually speak
and what the model was trained on is one of the largest sources of unequal performance in the
field, and it is routinely reported as noise rather than as a finding.

## What "dialect" actually covers

Four distinct situations get flattened into one word:

* **Dialect continua.** Arabic, Chinese and German varieties differ enough that "language" versus
  "dialect" is a political question, not a linguistic one. Moroccan Arabic and Gulf Arabic are not
  mutually intelligible.
* **National varieties.** `pt-BR` vs `pt-PT`, `es-MX` vs `es-AR`. Mutually intelligible, and full of
  differences that make a translation read as foreign (question 150).
* **Sociolects and ethnolects.** African-American English is a rule-governed variety with its own
  consistent grammar — and is routinely misidentified as "errors" by tools built on standard
  English.
* **Register variation.** Chat, social media, transcribed speech. Not a dialect, but it fails the
  same way and for the same reason: it is not what the training corpus contained.

## Why systems fail

```
   trained on:  standard written variety
   deployed on: everything else

   tokenizer     ─► unfamiliar spellings shatter into fragments (question 102)
   LID           ─► the variety is misidentified, or filtered out of the corpus entirely
   MT            ─► translates "into" the standard first, silently normalising away meaning
   ASR           ─► word error rate several times higher than the headline number (q125)
   moderation    ─► non-standard forms flagged as low quality or as violations
```

That fourth point compounds: because language identification and quality filters were built on the
standard variety, **dialect data gets removed from training corpora**, which makes the next model
worse on it, which justifies filtering it again. The loop is self-reinforcing and mostly invisible
unless you go looking.

## Normalise, or model directly?

The tempting engineering answer is to normalise the input to the standard variety and translate
that. Sometimes it is right — for a search index, or where the user wants standard output.

But be clear what it costs. Normalisation **discards the information carried by the choice of
variety**: identity, register, stance, irony, who the speaker is talking to. A system that
normalises before translating produces a translation of something the speaker did not say. And a
system that presents non-standard input as "corrected" is making a judgement about whose language
is correct.

Modelling the variety directly is harder — data is scarce, orthography is unstandardised, and
speakers themselves disagree about spelling — and it is the right default for anything that
represents the speaker rather than merely indexes them.

## What to actually do

* **Measure separately, always.** Break down every metric by variety. An aggregate WER or COMET
  hides a factor-of-three gap; reporting only the aggregate is how the gap survives.
* **Do not filter your corpus with a standard-variety classifier** without inspecting what it
  removes.
* **Collect with speakers, not about them** (question 164), and pay for it.
* **Support the orthographic variation** rather than picking one spelling and treating the rest as
  typos.
* **Say which variety you support.** "Spanish" is not a target (question 150). Claiming coverage you
  do not have is worse than admitting the gap.

## What an interviewer digs into next

* Why is the language/dialect distinction not a linguistic one?
* Describe the self-reinforcing loop that removes dialect data from corpora.
* When is normalising to the standard variety the right call, and what does it cost?
* Why does reporting aggregate metrics conceal this problem specifically?
