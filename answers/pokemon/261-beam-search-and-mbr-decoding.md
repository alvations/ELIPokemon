---
id: "261"
slug: beam-search-and-mbr-decoding
style: pokemon
category: optimization
difficulty: advanced
question: "Beam search is still standard in machine translation and unused in open-ended generation. What exactly is the difference?"
tags: [beam-search, mbr, likelihood, degeneration, machine-translation]
---

# The safest possible battle is the one where nobody attacks

Searching for the single likeliest line of play is not a style of battling. It is a search for one
particular thing — the line the model thinks is most probable — and everything about where it
still works and where it died comes down to one question: **is that line any good?**

Question 035 lays out the mechanism. This one is about the part that story leaves out, which is
that the most-probable line is bad in translation too, and that the fix was not to start guessing
wildly. The fix was to change what you are looking for.

## Search harder, play worse

Put **Toxapex** on the field with **Recover**, **Toxic**, a **Black Sludge** and its Hidden
Ability **Regenerator**. Put **Blissey** and its **Soft-Boiled** behind it, and **Shuckle** behind
that. Ask any of them, every single turn, for the action least likely to lose. The answer is
Recover. It is Recover on turn two, and on turn forty, and it is correct every time: nothing bad
happens to you on a turn you spend healing, and the other side is **Badly Poisoned** anyway.

Now search harder. Look three turns ahead, then ten, then perfectly. The deeper you look, the more
clearly the ideal line resolves into **doing nothing at all, forever**. That is not a bug in the
search. It is what the search was asked for, found properly.

```
   how good the line is                      how "likely to not lose" it looks
     ▲                                         ▲
     │      ●───●                              │                       ●
     │    ●        ●                           │                 ●
     │  ●              ●                       │           ●
     │ ●                   ●                   │     ●
     │                          ●              │ ●
     └──┬───┬───┬───┬────┬─────┬──▶            └──┬───┬───┬───┬────┬────┬──▶
       1   2   4   8   50  perfect  lines          1   2   4   8   50  perfect

   The search gets strictly better at its job and the battle gets worse.
   Looking only a few lines ahead is the only thing hiding the stall.
```

Read that the right way round: keeping a handful of plans alive works in translation partly
**because it is a shallow search**. Five lines is too few to find the empty battle.

## The clock is a patch, and it tells you where the bug is

Every extra turn in a plan is another chance for something to go wrong — **Hydro Pump** is 80%
accurate, and four turns of it is 41% — so raw scoring quietly prefers plans that end early, and
the fix is to divide the score by how long the plan is. The tell is that the divisor has to be
re-tuned for every new opponent set.

The games did the same thing, twice, and both are patches on the **scoring**, not on the players.
Official matches are played on a clock, and when it runs out the win goes to whoever has more
Pokémon still standing. And competitive rulebooks carry an **Endless Battle Clause**, because
without it two Pokémon can loop until the end of time. Nobody added those rules for fun. They were
added because the most-likely-to-not-lose line is a line nobody wants to watch.

## What the loop actually is

It is not a badly trained Pokémon and it is not a quirk of keeping several plans. **It feeds
itself.** Every turn of **Recover** leaves you healthier than you were, which makes Recover look
*better* next turn than it did last turn. **Black Sludge** ticking a sixteenth of your maximum HP
back to a Poison-type at the end of every turn — **Leftovers** does the same job for everyone
else — deepens the same groove. Always taking the best-looking action
follows that groove exactly and never climbs out of it. Rolling dice escapes, because there is a
real chance of doing something else on any given turn — which is the entire reason for picking
moves by chance in the first place.

There is exactly one true terminator, and it is not clever: **PP**. Recover runs out. When nothing
is left the game hands you **Struggle**, which takes a quarter of your maximum HP every time you
use it. The loop ends when the game stops letting you loop.

## Why translation and speech kept the search

* **One right answer.** A **Gyarados** switches in — Water and Flying, four times weak to
  Electric. **Thunderbolt**. There is no interesting second option. The most likely line really is
  a good line when the field only permits one.
* **Short battles.** The bias toward short plans is bounded when the whole thing is over in three
  turns.
* **A score you can trust.** You can check the answer against the field.
* **Something outside the model.** Speech has the sound itself pushing back, the way a type chart
  pushes back on a bad guess.

## What replaced it: play the rolls, not the roll

Every damaging move rolls one of **sixteen** damage values, 85% to 100% of the calculated figure.
A serious player never plans on the top roll. They ask whether the knockout holds across **all
sixteen** — that is what "guaranteed" means — and take the line that survives the spread rather
than the one that shines on the luckiest number.

```
   Ice Beam into Dragonite, 4x weak:   ████████████████  all 16 rolls KO -> guaranteed
   the same move a little weaker:      ██████████████░░  14 of 16 rolls -> 87.5%

   most-likely line : "which single plan does it rate highest?"
   the rolls        : "which plan still works across everything that could happen?"
```

That is the whole move. Stop asking for the top-rated line; start asking which line the spread of
outcomes agrees with. Judged by anyone actually watching the battle, it wins — and it never once
asks what the single likeliest play was.

The same trick has a second name in this dataset. **Self-consistency** (question 050) is this,
with the crudest possible agreement rule: run the battle many times, take the result that comes up
most. If you can see those two as one idea, you have understood both.

## Where the old search still belongs

When you have to *find* a legal line at all under a hard restriction (question 262), when the
answer is one short field, and in speech. Not in open conversation.

## What a Gym Leader is listening for

Whether you notice that "least likely to lose this turn" and "wins the battle" are two different
questions, and that the whole history of this argument is people optimising the first and being
surprised by the second.

**Citation note.** The arXiv identifiers linked in the serious half are given from working
knowledge. `arxiv.org` is blocked from the environment this was written in, so **not one of them
was resolved while writing**. Resolve every identifier before you cite it.

## Where this stands, September 2026

All of the decoding history here is working knowledge and should be treated as coverage; resolve
the papers before quoting a number. Coverage from this session suggests the split is holding —
agreement-based picking is the research standard in translation, the old search is still the
default in speech. What will not rot is the distinction: **a trained Pokémon is a set of odds, and
choosing what to press is a second decision with its own way of being wrong.**
