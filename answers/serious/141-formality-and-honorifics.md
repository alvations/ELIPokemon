---
id: "141"
slug: formality-and-honorifics
style: serious
category: translation
difficulty: intermediate
question: "How do you control formality and honorifics in translation?"
tags: [formality, keigo, t-v-distinction, register, control-tokens, cocoa-mt]
---

# Formality and honorifics

English barely marks social distance. Most languages mark it obligatorily, on every sentence. That
mismatch means a translator out of English must **make a choice the source never encoded**, and
must make the same choice consistently for an entire document.

## What has to be decided

| Language | What is marked | How wrong looks |
| --- | --- | --- |
| French, German, Spanish, Russian | T-V distinction (tu/vous, du/Sie) | insulting or absurdly stiff |
| Japanese | teineigo (polite), sonkeigo (respectful), kenjōgo (humble) — three axes | rude, or comically over-deferential |
| Korean | multiple speech levels, plus honorific verb forms and address terms | socially unreadable |
| Hindi, Tamil, Javanese, Thai | pronoun and verb-level respect systems | wrong relationship implied |

These are not stylistic garnish. In Japanese and Korean, choosing the level is a claim about the
relationship between speaker and listener, and every verb in the sentence carries it.

## The core problem: the source underspecifies

```
   English source:  "Can you send me the file?"
                              │
        ┌─────────────────────┼─────────────────────┐
   "Peux-tu ...?"      "Pouvez-vous ...?"      "Pourriez-vous ...?"
    a friend            a customer              a formal request

   All three are correct translations. Exactly one is right for YOUR context,
   and the source contains nothing that distinguishes them.
```

The model has to guess, so it guesses by prior — usually whatever dominated its training data,
which for many pairs is the formal register from news and official documents, and for others the
informal register from subtitles and forums. Neither is a neutral default. **There is no neutral
option**; declining to choose just means choosing by accident.

## How to control it

* **Control tokens.** Prefix the source with `<formal>` / `<informal>` during training and
  inference. The classic NMT approach; effective, needs formality-annotated training data.
* **Instruct an LLM.** Say it in the prompt. Works well, and compliance degrades over long
  documents — check the last segments, not the first.
* **Fine-tune per register.** An adapter per formality level (question 134).
* **Post-hoc rewriting.** Translate, then run a formality transfer model. Extra latency, but it
  decouples the concern and lets you re-render one translation at several levels.

Whatever you choose, **decide once per document and hold it** (question 131). A message that opens
with `vous` and closes with `tu` reads as either careless or as a deliberate shift in relationship,
and neither was intended.

## The metadata you should be passing and probably are not

The right formality is a function of context the translation system usually never sees: who is
speaking to whom, in what channel, in what relationship. A support reply to a customer, a message
between colleagues, and a marketing email are three different registers, and your system almost
certainly knows which is which *upstream* of translation. Pass it in. Inferring register from the
sentence is guessing at something you already know.

## Evaluation

* **CoCoA-MT** and similar contrastive sets give source segments with both formal and informal
  reference translations and measure whether the system produced the requested one. This is the
  right instrument, for the same reason as in question 131: **corpus-level quality metrics cannot
  see formality at all.** A system that gets every T-V choice wrong loses almost nothing on COMET.
* **Consistency rate within a document** — does the register flip?
* **Compliance under load**: measure formality accuracy at segment 1 and at segment 200. LLM
  instruction-following decays, and the average across a document hides it.

## What an interviewer digs into next

* Why is there no neutral default for T-V?
* Why can't corpus BLEU or COMET measure formality control?
* What context should the caller pass, and why is inferring it worse?
* How would you test that formality holds across a long document?
