---
id: "144"
slug: length-constrained-translation
style: serious
category: translation
difficulty: intermediate
question: "How do you translate when the output has a hard length limit?"
tags: [subtitles, length-control, ui-strings, expansion, line-breaking, compliance]
---

# Translating into a fixed space

Subtitles have a character limit and a reading-speed limit. UI strings have a button. Game text has
a box. Print has a column. In all of these, a translation that overflows is **not a slightly worse
translation — it is a broken product**, and no quality metric in question 129 can see the
difference.

## The expansion problem

Translating out of English usually gets longer. German and Finnish compound; Romance languages
need more words for the same idea; Russian and Polish inflect. Rules of thumb worth knowing:

```
   English → German        +10 to +35%
   English → Spanish/French +15 to +30%
   English → Russian       +15 to +30%
   English → Japanese/Chinese  often SHORTER in characters, but wider per glyph
   English → Arabic/Hebrew  similar length, and RTL, which breaks naive layout
```

Short strings expand worst. A one-word button label has no slack: "Save" is four characters and its
German rendering is eight or more. Layout designed against English is a layout that will break.

## Control mechanisms

* **Length tokens.** Bucket the desired output length (short / normal / long, or a ratio band) and
  prefix it as a control token during training and inference. The standard NMT approach — same
  mechanism as the formality tokens in question 141.
* **Prompt the constraint, then verify.** LLMs comply approximately. Always measure compliance;
  never assume it.
* **Generate n candidates, filter by length, rank by quality.** Simple, reliable, and the one most
  production systems actually use. Constraint satisfaction becomes a filter rather than a
  generation problem.
* **Constrained decoding with a length penalty** or hard truncation at beam expansion. Guarantees
  the limit and can produce a mangled ending.
* **Iterative shortening.** Translate, measure, and if over budget ask for a shorter rendering.
  Costs a round trip, produces better compressions than any single-pass method, and is what a human
  subtitler does.

## Subtitles have their own rules

Length is only half of it:

* **Reading speed** — characters per second, typically 15-21 for adults. A subtitle can be within
  the character limit and still be unreadable at the duration it is on screen.
* **Line breaking must follow syntax.** Break between clauses or before a preposition, never
  splitting an article from its noun. A poorly broken two-line subtitle is measurably harder to
  read than a well-broken one of the same length.
* **Maximum two lines**, and shot-boundary alignment: a subtitle spanning a cut is disorienting.
* **Compression is a skill, not a truncation.** Professional subtitlers drop redundancy — filler
  words, repeated names, information visible on screen — rather than clipping the end. "Well, I
  mean, I suppose we could go there" becomes "We could go." That is what "shorten this" should
  mean to your system.

## UI strings have different rules again

Placeholders (`{count}`, `%s`) must survive exactly (question 133); pluralisation is
language-specific and often needs more than two forms; and **the same English string may need
different translations in different places** — "Home" as a navigation item and "Home" as an address
field are not the same word in most languages. Passing context with each string is the fix, and
almost nobody does it.

## Evaluation

Report **compliance rate and quality together**, always:

* **Compliance**: fraction of segments within the character/CPS limit.
* **Quality on the compliant subset**, so shortening damage is visible.
* **The trade curve**: quality as a function of how tight the budget is.

A system reported at 95% compliance and no quality number may be truncating. A system reported at
high COMET and no compliance number is almost certainly overflowing, and the metric is structurally
incapable of noticing.

## What an interviewer digs into next

* Why do short strings suffer most from expansion?
* Why is generate-and-filter preferred over constrained decoding in practice?
* What does "shorten this subtitle" mean, done well?
* Why must compliance and quality be reported together?
