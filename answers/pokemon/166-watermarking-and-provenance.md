---
id: "166"
slug: watermarking-and-provenance
style: pokemon
category: multimodal
difficulty: advanced
question: "Can you tell whether media was AI-generated, and what actually works?"
tags: [watermarking, c2pa, provenance, detection, robustness, disclosure]
---

# Ditto keeps its own HP

**Transform** copies almost everything. The species. The stats. The moves. The ability. Stand a
transformed **Ditto** next to the real **Gyarados** and there is nothing to choose between them.

**Except the HP.** Transform does not copy it. A Ditto wearing a Gyarados still has **Ditto's**
health bar.

📌 That is a watermark: a mark left in the copy, invisible in the disguise, and readable by anybody
who knows where to look.

And it is the whole subject, because **two completely different questions** get asked as if they
were one:

* 🔍 **"Is this a Ditto?"** — given the Pokémon in front of you, is it a copy? *There is no reliable
  general answer.*
* 📜 **"Where did this Pokémon come from?"** — what does its record say? *Answerable, and this is
  the one worth building.*

## Why simply looking for fakes does not work 🚫

You can train yourself to spot the Dittos you have already met. Then somebody produces a better
Transform and you are back to nothing.

⚠️ And the real problem is **the accusations you get wrong.** Suppose you are right ninety-nine
times in a hundred, and one Pokémon in a hundred is genuinely a Ditto. Now **most of the Pokémon
you accuse are real**. Aimed at a Trainer's team — at their reputation, their tournament entry —
that is not a statistic. It is a false accusation with a number attached.

📌 Treat any general *"is this a fake"* detector as unreliable, and **say so** when somebody asks
you to run one.

## The three-way trade 📐

```
                    SURVIVES HANDLING
              (trades, re-catches, screenshots, edits)
                        /\
                       /  \
                      /    \      you get roughly two of these
                     /______\
              INVISIBLE      HOW MUCH IT SAYS
        (no visible tell)    ("a copy" vs "a copy made by X on this date")
```

* 🖼️ **In pictures**, the mark survives mild handling and fades under aggressive re-working.
* 🔊 **In sound it holds up best** — there is far more room to hide in — and it matters most,
  because a copied **voice** is the highest-harm case of all (questions 138, 153).
* 📝 **In writing it is weakest.** It works over enough words and is undone by **rewording**, which
  costs nothing. Change the nickname and the mark is gone.

⚠️ **A watermark is a deterrent and an audit trail. It is not a defence against somebody who is
trying.** Designing as though it were is the mistake.

## The half that actually works: the record 🏷️

Stop interrogating the pixels. **Ask what the Pokémon carries with it.**

Every Pokémon in the games already does this. It knows **where it was met**, **at what level**,
**on what date**, **which Poké Ball caught it**, and **who its Original Trainer was**. Not inferred
from looking at it — **recorded at the moment it happened**, and carried for life.

That is provenance, and it has one property that surprises people:

📌 **It works for the genuine ones too — and that is the valuable half.** The scarce thing shortly
is not proof that a Pokémon is a Ditto. It is proof that yours is **real**: legitimately caught, on
that route, on that day. Competitive Trainers already know this — a team that cannot show where it
came from does not get to enter.

⚠️ Two honest weaknesses. **Some transfers strip parts of the record** — a Pokémon brought forward
from an old game arrives saying only that it came from somewhere distant. And **a missing record
proves nothing**: plenty of perfectly real Pokémon have incomplete histories, and treating a blank
field as evidence of forgery repeats the false-accusation problem in a new costume.

## What to actually do 🔧

* **✍️ Mark it *and* record it** — both, from the first day. Retrofitting fails for exactly the
  reason in question 158: the unmarked ones are already out there.
* **📥 Keep the record when things pass through you**, and re-sign it after an edit rather than
  discarding it.
* **👁️ Say it on the screen**, not only in the record. A visible label survives handling that a
  hidden one does not.
* **⚖️ And never present a detector's opinion as proof.** Give a likelihood with its false-accusation
  rate attached, or give nothing.
