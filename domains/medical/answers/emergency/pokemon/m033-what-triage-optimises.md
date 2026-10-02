---
id: "m033"
slug: what-triage-optimises
style: pokemon
category: emergency
difficulty: advanced
question: "What is a triage system optimising, and why is the sickest patient not first in a mass-casualty setting?"
tags: [triage, mass-casualty, prioritisation, marginal-benefit, training]
---

# Trick Room inverts the sort key and leaves the brackets alone, and that is the whole shape

**Before anything else: nothing in this answer stands for a person.** The things being ordered in
a Pokémon battle are *actions*. The game is lent here for one idea only — what it looks like when
a system deliberately inverts its own ordering rule, how far down that inversion reaches, and what
it costs to switch on. The part of this subject that is about people is in plain prose further
down, where it belongs.

**Trick Room** is the cleanest example in the games of a rule that inverts the usual ordering on
purpose. For five turns, inside each priority bracket, the Speed comparison runs backwards: the
slower side acts first. Normally Speed is the tie-break and more of it is better. Under Trick Room
more of it is worse. Nothing about the field has changed except which direction the comparison
points, and that one flip rewrites which action resolves first in almost every exchange.

And then the three facts that make it the right analogy rather than just a flashy one.

## One: the inversion is bounded, and it stops exactly where it should

Trick Room does not touch the priority brackets. A **Quick Attack** at +1 still resolves before a
move at 0, whichever side is slower; **Whirlwind** at -6 still resolves last. All the inversion
reaches is the tie-break *inside* a bracket. Everything question m031 said about brackets being
read before Speed is still true under Trick Room — the forced ordering is untouched and only the
discretionary part flips.

```
   under the usual rule                    under Trick Room
   ──────────────────────────────────────────────────────────────────────────
   brackets, highest first                 brackets, highest first   (same)
     +5  Helping Hand                        +5  Helping Hand
     +3  Protect, Follow Me                  +3  Protect, Follow Me
     +1  Quick Attack, Mach Punch            +1  Quick Attack, Mach Punch
      0  almost everything                    0  almost everything
     -6  Whirlwind, Roar                     -6  Whirlwind, Roar
   ──────────────────────────────────────────────────────────────────────────
   inside a bracket: faster first           inside a bracket: SLOWER first
   on an exact tie:   coin flip             on an exact tie:   coin flip  (same)
   ──────────────────────────────────────────────────────────────────────────
   one thing flipped. Two things deliberately did not.
```

That bounded reach is the part worth carrying across. What inverts is the *key being sorted on*,
not the fact that a forced ordering exists. The categories, and the order in which the categories
are served, are fixed by the written system and are not up for renegotiation by whoever is
standing there — exactly as Trick Room leaves every bracket exactly where it was.

## Two: you pay for the inversion before you get anything from it

Trick Room sits at the very bottom of the priority table, below even Whirlwind — a bracket of its
own. So on the turn it is set, it resolves after everything else has already happened. The player
spends an entire action, out of a budget bounded by the four-move limit and by PP, on something
that does nothing at all by itself and only changes how later actions are ordered. **Helping
Hand** is the same kind of move from the other end of the table: +5, the highest bracket in
Emerald's data, zero direct effect, and its whole value is in what it makes a later action worth.
An action whose only product is a better allocation of other actions is a real category of move,
and the games price it honestly: it costs a full turn.

That is the economics of running a sorting pass. The scarcest thing gets spent on sorting instead
of on acting, up front, before any benefit arrives — and it is worth it only because the
improvement is spread across everything that comes afterwards.

## Three: it has to be built for in advance, and cannot be improvised

This is the most important one. A player cannot decide halfway through a battle to start
preferring slow. A roster that benefits from the inverted key has to have been assembled that way
beforehand, out of the bottom of the Speed distribution, and Emerald's own stat table shows how
specific a choice that is: **Snorlax** at base Speed 30 with base Attack 110, **Rhydon** at 40
with 130, **Camerupt** at 40 with 100, **Torkoal** at 20, and **Shuckle** at 5, which is the
floor. Those are the picks the flipped comparison rewards. Run the same inversion behind
**Ninjask** at base Speed 160, **Electrode** at 140 or **Jolteon** at 130 and all five turns are
spent handing the advantage away. The inversion is a property of a plan made in advance, not a
decision available in the moment.

The same goes for the modifiers, and they sort neatly into the two kinds. **Agility** and
**Tailwind** raise Speed and are therefore actively counterproductive under the inverted key,
while **Macho Brace**, which halves it in Emerald's turn-order routine, becomes an asset.
**Lagging Tail** is the individual-level version: it makes its holder act last *within its own
bracket*, which is reordering inside a category and never across one. Every one of those lives
below the brackets, exactly where question m031 left them.

And the games have an ability for the class-promotion version of the idea. **Triage** — the one
**Comfey** has, named exactly that — does not reorder anything individually. It lifts an entire
class of move up three brackets at once, and **Prankster** does the same thing for a different
class. That is what categories are for: you promote a class, you do not rank each case. **Follow
Me** at +3 is the designated-role version: a move with no effect of its own whose only job is to
make everything come to one place, resolved early so the redirection is in place before anything
else happens.

## What the inversion gives up

* **It is wrong about individual exchanges by construction.** Some turns under Trick Room go worse
  than they would have. The move is a bet about the aggregate over five turns.
* **It is conditional, and the condition can be misread.** Trick Room against a team already
  slower than yours is a straight self-inflicted loss. The inversion only pays when the thing it
  assumes is actually true.
* **It expires.** Five turns, and the counter is not displayed anywhere.
* **The irreducible variance stays.** On an exact Speed tie in the same bracket, both the ordinary
  rule and the inverted one call a random number and flip a coin. **Quick Claw**'s roll — one turn
  in five, by the parameter in Emerald's item table — is unplannable under either. No sorting rule
  promises a single answer where the situation does not contain one.

## Where the metaphor stops

No metaphor for this part. It is read straight.

What a triage system optimises is the number of people who survive across everyone who presented,
under a resource that genuinely binds within the window where treatment still changes anything. In
routine practice the resource does not bind, so *the best outcome for the person in front of me*
and *the most survivors overall* agree, and going to the most unwell person first is correct.
Under a binding constraint they stop agreeing, and the ranking that matters is expected lives
gained per unit of resource spent — which puts the severely injured but salvageable first, and
does not put the most severely injured first, because that group needs an enormous share of the
resource for a small change in probability. The objective did not change. The constraint did. That
is **mechanism**, and it is checkable by reasoning rather than by citation.

And every system of this kind contains a category for people whose injuries are not survivable
with the resource available. That is the hardest thing in this entire subject. It will not be
illustrated, softened or made charming. It is a decision forced by a constraint nobody chose, it
carries a real moral cost that no arithmetic discharges, and it is distressing for everyone near
it, most of all for whoever had to make it. Services that use these systems also run debriefing,
peer support and occupational health provision for exactly that reason, and those are part of the
system rather than an afterthought. Those routes exist precisely for this, and they are the right
place to take it — which is worth knowing before anyone needs them.

The reason the inversion has to be *trained* rather than merely explained is the Trick Room point
above, with the game taken out of it: it is an override of a reflex that is correct everywhere
else and has been reinforced thousands of times, and overrides of well-practised reflexes fail
under pressure unless the override has been rehearsed under something like pressure. It is also
why the sorting role is assigned to somebody who is not treating. One person cannot hold both
objectives at once; the one looking back at them wins.

## What a Gym Leader is listening for

* What exactly does Trick Room invert, and what are the two things it deliberately leaves alone?
* Why does it sit below Whirlwind in the table, and what does paying that cost up front correspond
  to?
* Why can a team not switch to the inverted key halfway through?
* What does an ability that promotes a whole class of move three brackets at once illustrate that
  reordering individuals would not?
* What does the Speed-tie coin flip say about the limits of any sorting rule?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* **The reader's own service or employing organisation's** major-incident and mass-casualty triage
  policy, which names the triage tool actually in use where they work, its categories and its
  criteria. That is the governing document, and it is the one this answer deliberately does not
  reproduce.
* **The reader's regional or national trauma network's** major-incident guidance, which sets out
  how the constrained mode is declared and by whom.
* The current life support and major-incident guidance issued by **the national resuscitation
  council for the country the reader practises in**. The councils differ from one another and each
  revises on its own cycle.
* The current consensus on science with treatment recommendations issued by **the International
  Liaison Committee on Resuscitation**, for the evidence synthesis the national councils write
  from.
* **The reader's own organisation's** staff support, debriefing and occupational health provision,
  which is the right route for the part of this subject that is not academic.

No triage tool is named, no category labels are given, no criteria or thresholds are stated,
nothing is quoted, and no guideline number or document title is given, because none was opened.
The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

**If someone is unwell right now, call your local emergency number.** This is not for use during
an emergency, and reading this instead of calling for help would be worse than doing nothing at
all.

This is revision material about *what a triage system is optimising and why*, written for someone
already trained, and the Pokémon framing covers the shape of an inverted ordering rule and nothing
else — no Pokémon or character here stands for a person. It is deliberately not a protocol and is
not usable as one: it names no triage tool, lists no categories, states no criteria or thresholds,
and contains no sequence of actions, rates, depths, ratios, doses or settings. Triage tools and
major-incident policies **differ between countries, services and institutions**, and resuscitation
guidance **differs between national councils and is revised on a cycle**. The reader's own service
policy and national council are the authority; this is not, and it has had no clinical review.
Nothing here describes any real person, case, incident or institution.

## Where this stands, October 2026

Of the Pokémon facts, the ones pinned to source are the Emerald bracket values above, from
`src/data/battle_moves.h`; the Speed-tie coin flip and the Macho Brace halving from
`GetWhoStrikesFirst` in `src/battle_main.c`; Quick Claw's one-in-five parameter from
`src/data/items.h`; and every base Speed and base Attack quoted above from
`src/data/pokemon/species_info.h`. **Trick Room, Lagging Tail, Tailwind, Prankster and the ability
Triage all postdate Emerald and were not read from either decompilation available here** — Trick
Room's position below Whirlwind, its five-turn duration, the reversal applying inside brackets
rather than across them, Lagging Tail acting within a bracket, and Triage promoting healing moves
by three brackets are all stated from working knowledge of later generations, and a reader who
wants them exact should check the generation they are playing. On the clinical side the
constrained-optimisation account, the separation of roles and the need for rehearsal are
mainstream **mechanism**; every specific — which tool, how many categories, what observations, who
declares — is **service-dependent**, differs between neighbouring services, and is revised. Dated
October 2026.
