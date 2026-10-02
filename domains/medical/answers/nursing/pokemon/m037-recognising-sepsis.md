---
id: "m037"
slug: recognising-sepsis
style: pokemon
category: nursing
difficulty: advanced
question: "Why is the response to suspected sepsis organised as a time-critical bundle, and what does that design trade away?"
tags: [sepsis, deterioration, bundles, antimicrobial-stewardship, screening]
---

# A Seen entry is not an Own entry, and the Pokédex is honest about which one you have.

The Advance-game **Pokédex** keeps two separate counts, and the difference between them is the
cleanest statement of a screening problem in any video game. Open the entry for something you have
merely **seen** and you get the number, the name and the sprite. The species category, the height,
the weight and the entire description come back as placeholder marks. All of that detail is gated,
in the code, on whether you have **owned** one.

So the Dex says, without apology: *something was here, I can tell you which slot it goes in, and I
cannot tell you what it is.* That is a positive screen. You act on the Seen entry. The Own entry
arrives later, and it arrives whether or not you waited for it.

## Why the turn you spend deciding is more expensive than the last one

The **Badly Poisoned** condition is the games' one escalating cost. A sixteenth of maximum HP on
the first turn, two sixteenths on the second, three on the third, climbing with a counter that
does nothing but climb. Ordinary poison takes a flat share forever. Badly Poisoned takes a growing
one, which means the price of the turn you spend thinking is strictly higher than the price of the
turn before it.

And the counter is **not printed anywhere**. The status slot shows one icon, the icon says the
condition, and the icon does not say "counter at five". A Pokémon at counter two and a Pokémon at
counter seven look identical on screen and are in completely different positions. Whether a
reading is early or late depends entirely on whether anybody watched it get there.

## Why a bundle, and not a list done in order

This is the structural heart of it, and the games already contain the distinction.

In a **single battle** you get **one action per turn**. In a **double battle** you get **two, in
the same turn**. Two Pokémon, two chosen actions, one tick of every end-of-turn effect. If the two
things you need done are independent, doing them in a double costs one turn and doing them in a
single costs two — and the Badly Poisoned counter advances in between.

A bundle is the move from singles to doubles. Nothing more mysterious than that.

```
   ONE ACTION PER TURN                         TWO ACTIONS, ONE TURN
   turn 1:  look at the screen                 turn 1:  look at the screen
   turn 2:  take the reading          vs       turn 2:  take the reading ┊ act
   turn 3:  act                                turn 3:  reassess
   turn 4:  reassess
   ─────────────────────────────────            ─────────────────────────────────
   three counter ticks before you act           one. Same actions. Same player.

   AND THE ORDERING INSIDE A TURN IS FREE, because the games have PRIORITY:
     Helping Hand   +5   ─┐
     Protect        +4    │  these resolve BEFORE anything in bracket 0,
     Quick Attack   +1    │  without costing a separate turn
     almost everything  0 ─┘
   So "this must happen before that" and "this must not delay that" are not in
   conflict. They are different axes. One is priority; the other is the turn.

   And the second thing a bundle does: it turns N decisions, each of which one
   person can quietly defer, into ONE decision that cannot be.
```

**Helping Hand** at +5 is worth dwelling on, because it is the games' purest example of an action
whose entire value is that it lands before the thing it supports, in the same turn, for nothing.
The request that must precede the main action and must not delay it is a solved problem in the
rulebook.

## What the design gives up

**The net is wide on purpose, and a wide net catches things.** A screening trigger built to notice
trouble early will fire on a Pokémon that is merely tired, merely one stage down, merely holding a
**Life Orb** on purpose. Most of what it flags is not the thing. That is not a defect in the tool;
it is the price that was paid deliberately for not missing the one that was.

**The aggressive option has a standing bill.** A **Life Orb** boosts its holder's moves and takes
a **tenth** of maximum HP every time it lands a hit. It is a genuinely strong item. The cost is
paid on every hit, including the ones that turned out not to be needed, and it is paid by the
Pokémon holding it.

**The same intervention has opposite signs on different Pokémon.** Set **Rain Dance** and a
Water-type gains, a Fire-type's moves are halved, **Thunder** and **Hurricane** stop missing, and
a **Dry Skin** holder gains HP while in harsh sun the same ability takes extra damage. Nothing
about the weather itself tells you which Pokémon is in front of you. Reach for the same field
condition every time and you will help two Pokémon in six and hurt three.

**The reflex defence stops working, and the game says so in the item text.** **Protect** has a
printed description that reads "Evades attack, but may fail if used in succession", and the
Advance code pins exactly what that means: full success the first time, then **a half**, then **a
quarter**, then **an eighth** on consecutive uses, resetting the moment you do something else.
Used once when it matters, it is one of the best moves in the game. Used every turn as a reflex,
it is a coin flip and then worse. That is the whole argument about reaching for the broadest thing
by default.

**And clearing the icon is not the same as removing the cause.** A **Full Heal** clears every
status condition and restores no HP. A **Toxic Orb** badly poisons its holder in battle. Use the
Full Heal on a Pokémon that is still holding the Orb, and the icon clears, and the end of the turn
puts it straight back — because the Orb never went anywhere. The icon was the response. The Orb
was the source. Treating the first and not the second is a loop, and the loop costs a turn each
time round.

## When the thing in front of you is labelled as something else

**Shedinja** has a maximum HP of **1**, forever, because its base HP really is 1. **Slaking** has
base stats of 150/160/100 and **Truant**, so it moves only every other turn — a Slaking doing
nothing this turn is not deteriorating, that is Tuesday. Both are reused from the early-warning
read for the same reason they matter here: **a reading that is normal for this one and alarming
for everything else is where a tuned trigger does its worst work, in both directions.**

And the harder case. **Zoroark** has **Illusion**, and the code is precise about it: the Pokémon
comes onto the field displaying the species of the **last conscious Pokémon in the party**, and
the disguise ends **when it takes damage** — not when you look at it harder, not when you check
the screen twice. A thing that presents as something else, and only reveals itself when something
actually happens to it, is the atypical presentation. No amount of inspection does what the first
real event does.

## The stop has no prompt

The games will offer you the bag. Nothing in them ever asks whether the item is still needed,
whether the weather you set is still helping, or whether the thing you reached for two turns ago
should come back off. Beginning has a menu. Stopping has nobody's attention at all, and the longer
something runs unexamined the more it has become part of the field rather than a choice.

## Where the metaphor stops

The mechanisms above are mechanisms. What they are attached to is not, and both directions are
real.

Sepsis kills a great many people every year, and a substantial share of those deaths follow a
recognisable period during which somebody could have acted sooner. Families' accounts of those
cases say the same thing with striking consistency: the concern existed, it was voiced, and it did
not reach a decision in time. Every bundle, trigger and screening tool in this area is a response
to that, and that is why they are mandated rather than suggested.

The other half is real too, and easier to forget because its victims are diffuse. Treating
everyone who screens positive as though they have sepsis harms some of them, and feeds a
resistance problem that will outlast everyone reading this. Holding both of those at once, without
using either to excuse inaction on the other, is what competence in this topic looks like. There
is no game in it.

## What Nurse Joy is listening for

The difference between a Seen entry and an Own entry, and which one a positive screen hands you.
Why the counter that climbs makes the cost of a turn non-constant — and why the counter is not on
the screen. What the local trigger is tuned for, and what it will fire on that is not the thing.
Which two actions genuinely have an ordering constraint, and which were only ever serialised out
of habit. Where the Toxic Orb is, because the icon will come back if nobody finds it. And what
makes somebody stop, given that nothing prompts it.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../for-agents/SOURCES-nursing.md`](../../for-agents/SOURCES-nursing.md). Specific to this
answer:

* The international consensus definitions of sepsis and septic shock, issued by the collaborating
  critical care societies, for the definitional material.
* The international campaign guidelines on the management of sepsis and septic shock, for the
  bundle structure and for the fluid and antimicrobial recommendations, which have been revised
  repeatedly.
* The reader's own national guidance on recognising and responding to sepsis, and the reader's
  institutional sepsis screening tool and pathway — the authority for every trigger, time window
  and named action, none of which appears here.
* The reader's national antimicrobial stewardship guidance, for de-escalation and review.
* A standard critical care or applied physiology textbook, for the organ-dysfunction mechanism.
* The primary literature on time-to-antimicrobial and outcome, which is the most contested claim
  in this pair and should not be taken from any secondary summary, this one included.
* The reader's national guidance on sepsis in pregnancy and the puerperium, in neutropenia, and in
  children, for the three populations whose pathways differ.

Separately, and unlike the above: the Pokédex gating of category, height, weight and description
on the caught flag; the Protect consecutive-use fractions; the priority values; the Life Orb
share; the Toxic Orb and Full Heal behaviour; the Shedinja and Slaking figures; and the Illusion
trigger were all read directly out of the public disassemblies of the games and their expansion,
which this environment could reach. The Protect text is the game's own printed description.

## Scope and safety

This explains why a class of protocol is designed the way it is, for someone already training in
or qualified for clinical practice. **It is not a sepsis bundle and deliberately does not contain
one** — no trigger values, no time windows, no fluid volumes, no antimicrobial choices. The only
numbers in it belong to a video game. Those clinical values are set nationally and
institutionally, they differ, and they are revised; the reader's own pathway is the authority and
this is not. It has had no clinical review. Nothing here is for use in an emergency or for a
decision about any person's care. If someone is unwell right now, the local emergency number is
the correct response.

## Where this stands, October 2026

The physiology and the definitional framework are stable. Almost everything procedural around them
has moved within living memory and will move again: the screening tools and the physiological
score behind them, the time windows and whether they should be mandated at all, the fluid
recommendations, the place of lactate, and the balance struck against antimicrobial stewardship.
This area has been more actively contested than most of nursing practice, and a reader should
expect the version they were taught to have been superseded. The Pokédex, by contrast, has gated
the description on the caught flag since Kanto, and has never once pretended a Seen entry was more
than it is.
