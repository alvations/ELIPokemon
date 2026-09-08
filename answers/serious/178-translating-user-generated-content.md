---
id: "178"
slug: translating-user-generated-content
style: serious
category: translation
difficulty: intermediate
question: "What breaks when you translate chat messages and user-generated content?"
tags: [ugc, chat, noisy-text, emoji, code-switching, latency, moderation]
---

# Translating what people actually write

Every technique so far assumed edited prose. Chat messages, reviews, comments and support tickets
are not that, and a system trained on news translates them badly in specific, predictable ways.

## What is actually in the input

* **Typos, missing punctuation, no capitalisation.** The tokenizer shatters unfamiliar spellings
  into fragments (question 102), and a single typo can change the translation of a whole sentence.
* **Abbreviations and internet register**, which differ per language and change faster than any
  model's training data.
* **Emoji and emoticons**, which carry sentiment and sometimes negate the text. They also differ in
  meaning by culture (question 150) — the same emoji is affectionate in one locale and dismissive
  in another.
* **Code-switching** mid-sentence (question 107), which breaks anything that commits to one source
  language.
* **Non-standard varieties** (question 162), which are the default in informal writing.
* **Very short segments** — "ok", "same", "lol" — where there is almost nothing to condition on
  (question 136) and context is the only signal.
* **Deliberate obfuscation**: spaced-out letters, homoglyphs, leetspeak, used to evade moderation
  (question 115).

## The design consequences

**Context is not optional, it is the whole thing.** A chat turn is meaningless alone. "Same" is a
reply. Translate the thread, not the message (question 131) — and this is the case where
document-level translation has the largest measurable effect, because the segments are so short.

**Do not clean too hard.** Normalising the text to standard prose before translating destroys the
register and sometimes the meaning (question 162). Repetition ("sooooo good") is emphasis;
lowercasing is a tone. Fix what breaks the tokenizer; keep what the writer chose.

**Latency budgets are tight.** Chat translation is interactive, so this is question 143's
quality-latency curve again, with the added wrinkle that messages arrive faster than they can be
translated during an argument.

**Never translate names or handles.** `@charizard_fan` is an identifier (questions 133, 172). This
seems obvious and it ships broken constantly.

## Moderation is where it gets consequential

Translated content is moderated, and the pipeline order matters enormously:

```
   moderate AFTER translating  ─► the classifier sees fluent standard-language text
                                  and misses slurs whose force lives in the original
   moderate BEFORE translating ─► needs a classifier per language, and the
                                  low-resource ones are worst served (question 162)
```

Both orders fail differently, and the honest answer is both, plus a specific caution: **translation
launders obfuscation**. A deliberately misspelled slur may be helpfully "corrected" into a clean
rendering that passes a filter — or, in the other direction, an innocuous phrase may be translated
into something that reads as a violation. Log both the source and the translation for every
moderation decision, and never action a ban on the translation alone.

## Evaluation

Build a test set from **real messages** with their **threads**, not from cleaned-up sentences.
Report separately on: very short segments, code-switched segments, emoji-bearing segments, and
non-standard-variety segments. A single number over a mixed set is dominated by the easy majority
and tells you nothing about the cases you built the system for.

## What an interviewer digs into next

* Why does document context matter more for chat than for documents?
* What does over-normalising the input destroy?
* Why does moderation order matter, and what does "translation launders obfuscation" mean?
* Why must a chat test set include threads rather than isolated messages?
