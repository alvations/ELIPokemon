---
id: "013"
slug: context-length-limits
style: pokemon
category: transformers
difficulty: intermediate
question: "Why is context length limited, and what actually breaks when you extend it?"
tags: [context-length, long-context, lost-in-the-middle, needle-in-haystack]
---

# Why your Trainer can't remember a 400-turn battle

Everyone assumes the limit is memory. It's four different limits wearing a trenchcoat.

## Wall 1: everyone must scout everyone 🔍

Every Pokémon on the field sizes up every other Pokémon — Garchomp against Ferrothorn against
Toxapex, all at once. Ten Pokémon is 100 comparisons. A
hundred Pokémon is 10,000. A thousand is a million.

Double the roster, **quadruple** the scouting. This is the one everybody knows about.

## Wall 2: the notebook 📓

Every Pokémon that has appeared gets an entry — Politoed's Drizzle, Kingdra's Swift Swim — and the
notebook is **per battle**. Running forty
battles at once means forty notebooks on the desk. Stretch each battle to 400 turns and suddenly
you can only run four.

In practice this is what actually caps you. Not "can the Trainer handle it" — "how many
notebooks fit on the desk."

## Wall 3: slot numbers past the end of the party 🎫

Your Trainer learned on parties of six — the belt holds six, the PC box is somewhere else. Their
sense of "slot" was calibrated for six. Hand them Pokémon #847 and they're reading a slot number that has never existed in their life. They can be
retrained to stretch — but not for free, and not by just asking nicely.

## Wall 4: nobody has ever *played* a 400-turn battle ⏳

The underrated one. Real battles are 20 turns. Even a Toxapex stall war rarely passes 60. There is almost no footage of
a genuine 400-turn match where turn 380 hinges on something from turn 4.

So even a Trainer *advertised* as handling 400 turns has barely practised on real ones. Their
long-game training footage is mostly short matches stapled end to end — which teaches them to
handle a long log, not to actually *reason across* one.

## What actually goes wrong 🎯

Here's the distinction that matters, and the one people miss:

```
  ✅ "Somewhere in this 400-turn log, someone used Splash. Find it."
     Nearly perfect. Modern Trainers ace this. Solved problem.

  ❌ "Their Gyarados was burned on turn 12, they switched on turn 180,
      and the weather changed on turn 340 — what's their win condition?"
     Falls apart well before turn 400.
```

**Finding** something in a long log is easy. **Combining three things** scattered across it is
where they break. Don't let a Trainer's needle-finding score convince you they can strategise
across the whole match.

## Lost in the middle 🌫️

And the failure isn't uniform. Ask about a turn from the middle of a long battle:

```
   recall │██                                                    ██
          │███                                                  ███
          │████                                                ████
          │  █████                                          █████
          │      ████████                            ████████
          │           ███████████████████████████████
          └──────────────────────────────────────────────────────►
           opening                the murky middle              recent

   Turn 3?    Crystal clear — that was the lead, everyone remembers the lead.
   Turn 380?  Crystal clear — that was thirty seconds ago.
   Turn 190?  ...something about a Ferrothorn? Or was it Skarmory?
```

Openings are memorable. Recent turns are fresh. **The middle is a swamp.** Exactly like a human
watching a long tournament, and for a similar reason: in every match your Trainer ever studied,
the important stuff was at the start or the end.

## Two more things that quietly rot 🕳️

**Your instructions get buried.** Told your Trainer "never switch Ferrothorn into Fire moves" on
turn 1?
By turn 300 that one sentence is competing with 299 turns of chaos. It's still technically in
there. It is not winning.

**More log, more ways to be misled.** A 400-turn battle contains far more irrelevant detail than
a 20-turn one, and every piece of it is a chance for the Trainer to latch onto the wrong thing.

## How to actually use a long window 📌

* Treat the advertised turn limit as a **capacity, not a target**. Shortest log that contains
  what's needed wins — on accuracy *and* on cost.
* Put your instructions at the **top and repeat them at the bottom**. Both ends are memorable;
  the middle is not.
* **Pull out the relevant turns and hand over just those.** A five-turn briefing usually beats a
  400-turn log. Cheaper, faster, and often more accurate.
* Test on **your** multi-hop question — *"given the Stealth Rock and the burn, does Charizard still
  win?"* — not on needle-finding. Needle-finding is a solved score
  that tells you nothing about whether the Trainer can actually strategise.
