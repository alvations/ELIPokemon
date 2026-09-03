---
id: "042"
slug: chunking-strategies
style: pokemon
category: rag
difficulty: intermediate
question: "How do you chunk documents for retrieval, and why does it matter so much?"
tags: [chunking, rag, semantic-chunking, late-chunking, context-window]
---

# Chunking: how do you cut up the scouting reports?

You've got a stack of scouting reports and you want to look things up fast. So you cut them into
cards and file them.

**How big do you cut the cards?** This sounds like a trivial question. It is the single most
important decision in the whole system, and it's the one everyone rushes.

## The tension ✂️

```
  🔬 TINY CARDS (a sentence each)      📜 BIG CARDS (a whole report each)
  ─────────────────────────────        ────────────────────────────────
  ✅ each card is about ONE thing,     ✅ everything you need is on it
     so filing it is easy              ❌ the card is about eight topics,
  ❌ "it's weak to Electric"               so it files under nothing in
     — WHAT is? The card               ❌   particular and matches every
     doesn't say.                          search weakly
  ❌ the answer gets split across      ❌ you read four irrelevant
     two cards                            paragraphs to find one line
```

Tiny cards file beautifully and say nothing. Big cards say everything and file terribly.

## The trick that resolves it 🎯

> **File by the small card. Hand over the big one.**

Index every sentence individually — precise, easy to find. But when a sentence matches, **hand over
the whole section it came from.**

Best of both: you found it because the sentence was specific, and you can *use* it because you got
the context. This one pattern fixes most bad retrieval systems.

## How to cut, worst to best 📋

**1. ✂️ Every 500 words, with a bit of overlap.** Crude — cuts mid-sentence, mid-thought. But the
overlap means an answer split across a cut appears whole on *one* of the two cards. Honestly about
80% as good as anything cleverer. **Start here.**

**2. 📐 Cut at natural breaks.** Try paragraph breaks first; if a paragraph's too long, sentence
breaks; then words. Respects the writing's own structure without needing to understand it. The
sensible default.

**3. 🏷️ Cut at section headings — and write the heading on every card.**

This is the big cheap win nobody does. Instead of a card reading:

> *"It's weak to Electric and typically runs Leftovers."*

...write:

> **`Gym Report > Water Teams > Gyarados:`** *"It's weak to Electric and typically runs Leftovers."*

Same card. Now it's *findable*, because the card carries its own address. Costs nothing.

**4. 🧠 Cut where the topic changes.** Read through and cut wherever the subject shifts. Sounds
obviously correct. In practice it beats good heading-based cutting less often than its popularity
suggests.

**5. 📖 Read the whole report first, THEN cut.** The elegant one.

Read the entire report end to end. *Then* cut it into cards. Because you read it whole, when you
file the card that says *"it's weak to Electric"*, **you know what "it" is** — and you file it under
Gyarados, where it belongs.

Same words on the card. Vastly better filing, because the filing clerk had context the card
doesn't.

**6. ✍️ Write a note on each card explaining where it came from.** Have someone read each card and
scribble a one-line orientation on top. Expensive to set up, and it cuts lookup failures a lot.

## What actually matters 📌

**Start simple, then measure.** Cut at natural breaks, ~500 words, write the headings on. Then build
a test — *"here's a question, here's the card that should come back"* — and try three cutting
strategies.

A half-day of that routinely beats weeks of fiddling with everything downstream, because **no
amount of clever searching finds an answer you cut in half.**

**And clean the reports first.** 🧹 If every page has the same letterhead, page number, and footer,
then every single card contains that boilerplate — and now every search matches every card,
because they all share the same junk. Strip it before you cut.
