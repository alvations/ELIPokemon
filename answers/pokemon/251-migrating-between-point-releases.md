---
id: "251"
slug: migrating-between-point-releases
style: pokemon
category: open-weights
difficulty: advanced
question: "A point release lands on the same architecture with a much better index score. How do you decide whether to migrate?"
tags: [qwen, regression-testing, migration, evaluation, serving]
---

# It came back from the **Day Care** three levels higher and one move short

Leave a Pokémon with the **Day Care** couple on the road below **Goldenrod City** and walk. It
keeps gaining levels while you are gone, you pay by the level, and it is the cheapest training in
**Johto**. Then you collect it, and it is missing a move. Not because anything went wrong —
because that is the rule. **When a Pokémon in the Day Care learns a move on level-up, the new one
overwrites whatever is sitting in the top slot, and nobody asks you first.**

Leave a **Gyarados** there with **Earthquake** in slot one. Collect a stronger **Gyarados** with
no Earthquake. And in the old cartridges a **TM** was single-use, so the move you spent it on is
gone for good.

That is a point release on an unchanged architecture. **The level went up. Something was deleted.
You were not asked.** And it is the most dangerous kind of upgrade precisely because the receipt
only shows the good half.

Qwen3.8-27B against Qwen3.6-27B is the clean case: same 64 layers, same 5,120 hidden size, same
range, same vocabulary, and **38 against 52** from an outside judge. The shelf that serving
frameworks keep has no separate row for either of them, because there is no new species to carry
(question 250). Every point of that gain is raising. So is everything that went missing.

## What you can read on the summary screen, and what you cannot

```
   on the summary screen                   nowhere on it
   ─────────────────────────────────       ──────────────────────────────────────
   species, base stats, vocabulary    │    which match-ups it still wins
   the range, the tensor shapes       │    how long it takes before it moves
   the command you serve it with      │    whether it still calls for help
   the memory it sits in              │    whether it stops where it used to stop
   ─────────────────────────────────  │    what happens on a move it cannot learn
        ALL UNCHANGED                 │         ALL OF IT CHANGED
                                      │
                       the request form has the left column only
```

Four reports from the lab's own board show the exact shapes to test for:

- **One match-up collapsing.** Issue #238: the newer 27B corrupts Tamil suffixes on medical text
  that the older one handled — **13–27% acceptable against 93%** on a 60-item batch, across three
  different ways of compressing it, which is why the reporter blames the raising and not the ball.
- **It stops in the wrong place.** Issue #231: output truncated unexpectedly.
- **A move that used to work stops working.** Issue #236: tool calls go unreliable on long prompts
  with thinking switched off.
- **A move it simply cannot be given.** Issue #217 records the refusal, word for word: `Unexpected
  reasoning effort high. Supported types are xhigh (default), medium, and low.` Offer **Snorlax**
  the **HM** for **Fly** and it does not fly badly — the screen simply says no, every time, on the
  first attempt (question 220).

That last one is not a weakness. It is an illegal moveset, and it is the cheapest of the four to
catch.

## The gauntlet, in order

Say the asymmetry first, because it sets the default. **Staying put costs you a slow, widening
gap. Swapping badly costs you one match, sharply, in front of a badge you needed.** Slow and vague
against fast and specific. So the default is: keep the team you have, and make the new one earn
the slot.

```
   GATE 1  legality       is the moveset legal? control strings, the template,
                          the parser, the stop tokens        → hours, yes or no
   GATE 2  contract       does it still hand back what the harness expects?
                          valid JSON, schema, truncation     → a day, thresholded
   GATE 3  the match-ups  YOUR frozen list of battles, scored ONE BY ONE and
                          never averaged                     → the real work
   GATE 4  the bill       PP and turns at YOUR settings, p50 and p99, with the
                          truncation rate beside it          → the surprise
   GATE 5  shadow         a Bug Catcher on Route 1 — a battle nobody records
   GATE 6  canary         a small share of real battles, rollback rehearsed,
                          the old one still in the box       → until it is dull
```

**Gate 3 is where Trainers cheat.** "It went up three levels" is the *average*. The question is
whether it still beats **Whitney**'s **Miltank**, **Morty**'s **Gengar**, **Jasmine**'s
**Steelix**, **Pryce**'s **Piloswine** and **Clair**'s **Kingdra** — five questions, five answers,
and Johto hands you the list in a fixed order for free. Pool them and a 93-to-20 collapse on one
disappears inside a fourteen-point gain. Your match-ups come from the Gyms you actually have to
walk into, not from somebody else's league table.

**Gate 4 is where the cheap training stops being cheap.** Same species means the same cost per
turn — it does not mean the same number of turns. One that now thinks at its top notch by default,
and that Trainers report burning tens of thousands of turns of deliberation on trivial questions,
is a different bill on identical hardware.

## The cheap things everybody skips

- **Write the gauntlet down before you meet the candidate.** A list drawn up after watching it
  battle is a description of that Pokémon.
- **Keep the old logs and compare them side by side**, not just the win rate. Fifty diffs, read by
  a human, find classes of change no scoreboard was built for.
- **Some of what the Day Care deleted is recoverable and some is not.** Anything on its own
  level-up list, the **Move Reminder** will put back for a **Heart Scale**. What you paid a
  single-use TM for, nobody will. Knowing which is which *is* the regression suite.
- **Keep the old one in the box, healed and ready for the whole canary.** A **Pokémon Center**
  trip is cheap; a switch you have never practised is a wish.
- **Change one thing.** Re-teaching your prompts and swapping the Pokémon in the same week makes
  the result unreadable; your prompts were written around the *old* one's weak spots.

## What a Gym Leader is listening for

That a number on a scoreboard opens an evaluation and never closes one. Then that your first gate
is legality rather than strength, because it is binary, cheap, and the most common reason a swap
fails on day one. The strongest answers say the asymmetry out loud and take the consequence: on a
same-species point release the default is **stay**, and the interesting question is what the
gauntlet would have to show to move you.

## Where this stands, September 2026

The four reports (#217, #231, #236, #238) and their numbers are read directly from the Qwen team's
own issue board — Trainers' reports on the right noticeboard, not the lab's claims, and not re-run
here. The missing shelf row is read directly from the serving framework's source. **The 38 and 52,
the two checkpoints' matching configurations, and the reports of very long default deliberation
are coverage**, because the model cards and the blog are behind an egress block; those are the
authorities. The issue numbers will rot within weeks. The gauntlet, and the asymmetry that orders
it, will not.
