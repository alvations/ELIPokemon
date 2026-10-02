---
id: "m013"
slug: screening-and-its-harms
style: pokemon
category: general-practice
difficulty: advanced
question: "Why is a screening programme not simply more testing, and what do lead-time bias, length bias and overdiagnosis each do to its apparent benefit?"
tags: [screening, overdiagnosis, lead-time-bias, length-bias, public-health]
---

# Sweeping the grass on purpose is a different act from meeting something in it

A **Super Rod** is cast by a Trainer who wants a specific thing from a specific pool. A sweep of a
whole floor is something else: it goes out to a population of grass that is, slot for slot,
overwhelmingly ordinary, and it looks for something that is not. The default in the second case —
walking past — is genuinely fine, and that inverts who has to prove what. A sweep has to show it
does more good than the **Poké Ball**s, the money and the box slots it spends, because those are
spent on the ordinary slots, which is nearly all of them.

So "more encounters is better" is not a cautious claim, it is a strong one. The **White Flute**
raises the encounter rate by half and the **Black Flute** halves it; a **Cleanse Tag** in the
lead's hand cuts it to two thirds. Not one of them touches a single slot in the table. More
encounters, same disease. That is the whole trap, and three specific artefacts make a sweep look
as though it has beaten it.

## Lead-time: the clock started earlier, the event did not move

```
   REAL NUMBERS. Zubat evolves into Golbat at level 22. That threshold belongs to Zubat
   and nothing a Trainer does moves it. Mt. Moon's tables offer Zubat at six levels.

   level  6 ──────────── 8 ──────────── 11 ──────────── 12 ─────────────── 22
     │                   │               │               │                  │
   1F slot 5         1F slot 1       1F slot 9       B2F slot 9          GOLBAT
   (earliest)                                        (latest)

   met at level  6  →  16 levels of having known about it  →  Golbat at 22
   met at level 12  →  10 levels of having known about it  →  Golbat at 22

   The interval measured from first sighting got sixty per cent longer. The level at
   which Golbat arrives did not move by one.
```

Counting from the moment you first saw it is not a measure of anything, because a sweep moves that
moment by construction. The only count that cannot be gamed is what happened to the whole floor —
every Trainer who walked in, including the ones who never met the thing — against a floor nobody
swept. Registering more in the **Pokédex**, registering them earlier, and registering them at
lower levels are all perfectly compatible with having achieved nothing.

## Length bias, and its limiting case

```
   REAL NUMBERS. Mt. Moon 1F, 256 rolls of the table. Slot chances in slot order are
   51 51 39 25 25 25 13 13 11 3 out of 256.

   species      slots held   chance /256   comes out per 256 rolls
   ──────────   ──────────   ───────────   ───────────────────────
   Zubat             6            202               202
   Geodude           2             38                38
   Paras             1             13                13
   Clefairy          1              3                 3

   Paras and Clefairy hold one slot each. Yet Paras comes out more than four times as
   often, because its single slot is slot 8 at 13/256 and Clefairy's is slot 10 at 3/256.
   And Zubat comes out 202 / 3 = 67.3 times for every Clefairy.

   A sweep samples SLOTS, not species. What it brings back is whatever occupies the most
   of the table, which is not the same question as what is worth finding.
```

Taken to its limit, the sweep spends everything it has on the wide slots and never reaches the
narrow one.

```
   REAL NUMBERS. Party holds 6. Twelve boxes hold 20 each. 246 slots in total.

   catching everything that comes out of 256 rolls of Mt. Moon 1F:
        Zubat 202      Geodude 38      Paras 13      Clefairy 3   =  256 catches
        storage available                                         =  246 slots

   Storage fills around roll 246, which is about where the third Clefairy was due. The
   engine then refuses the throw outright: party full and box full is a hard stop, and the
   Clefairy standing in front of you cannot be caught at all.

   Signature of having over-swept:
        OWN counter in the Pokédex     ▲  rises, and stays risen
        badges                         ─  flat
        the six in the party           ─  unchanged
```

Three things about that are worth saying precisely, because they are counter-intuitive.

* **It is not a mistaken identification.** Every Zubat caught really was a Zubat. The throw
  worked. The catch is correct and it still should not have happened.
* **No single catch can be labelled as the wasteful one.** Once a Zubat is in a box it looks
  exactly like a Zubat you needed, and the ones you needed look exactly like the ones you did not.
  The waste exists only when you count the whole box. That is why it is so hard to talk about one
  at a time: the honest statement is about a rate, and what is in front of you is not a rate.
* **The cost is the full cost of the catch.** The ball, the money that would have bought a **Great
  Ball**, the trip back to the **Pokémon Center**, the box slot, and the one that actually bites —
  the Clefairy you then cannot accept.

## Why the decision belongs to the floor and not to the step

The table is a property of the place. A single step samples it; it does not describe it. So the
real decision — sweep this floor or not — is made with counts nobody collects while walking: how
many rolls, how many of them ordinary, how many balls, how many box slots, how many trips back,
against how many of the thing actually worth having. Per step it is always a tiny chance of
something good and a tiny cost, spread over an enormous number of steps.

Standing in the grass is the opposite. It is one roll, and the honest thing to say about it
involves a prize you probably will not get and a cost you probably will not pay. What makes that
tractable is giving both directions in the same units over the same number of rolls, and being
plain that the recommendation is about the floor, not about this step.

**Which tools a region even has is local.** The flutes are a Hoenn item and no Trainer in Kanto's
Red or Blue has one. The tables themselves differ between versions of the same region: Red's Route
4 holds **Ekans** in four slots where Blue's holds **Sandshrew**, Red's **Viridian Forest** fills
six of its eight ordinary slots with **Weedle** and **Kakuna** where Blue's fills them with
**Caterpie** and **Metapod**, and slot 9 of the **Safari Zone**'s centre area is **Scyther** in
Red and **Pinsir** in Blue — the rarest slot in that area is **Chansey** in both. A Trainer who
compares two versions and concludes that one of them must be wrong has usually read neither table.

## Where the metaphor stops

Overdiagnosis is a harm done to a well person. It is worth refusing the softer phrasings, because
the softer phrasings are what let it be filed as an accounting adjustment. Someone who was never
going to be troubled by a disease is given its name, its investigation, its treatment and its
complications, and afterwards lives as a person who has had it. None of that is a statistical
artefact; the statistics are only how the harm becomes visible at all.

The cruelty in the structure is that the person can never find out which they were. The one whose
life was saved and the one who was harmed look identical to themselves, to their family and to
their clinician, and both are sincerely grateful. That asymmetry is why an honest public case for
a programme is so hard to make: its beneficiaries are identifiable and will say so, while the
people it harmed believe they were beneficiaries and will say so just as loudly. Anyone presenting
a programme has to resist the testimony that is easiest to obtain.

Two obligations follow. An invitation is a system acting on someone who did not ask, so the duty
to inform is higher than for a test somebody requested, not lower — and material written to raise
uptake is not information, whatever else it is. And the benefit has to be checked for where it
lands: uptake is consistently lowest among the people carrying the most disease, so a programme
can show a real average benefit while bypassing those who needed it most, which widens a gap
rather than closing one.

## What a Gym Leader is listening for

Whether the Trainer throws out "I found it earlier" as evidence without being asked to. Then
whether they can keep slot width and wasted catches apart instead of calling both bad luck. Then
what over-sweeping looks like in the Pokédex counters, and why it takes a very long walk to see
it. Then the hard part: how to describe a tiny chance and a tiny cost over the same number of
rolls, and what to do when someone just wants to be told whether to walk in.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* The World Health Organization's published principles for screening, in its original form and in
  the later revisions issued by the same organisation, for the conditions a programme must meet.
* The published rationale, age range and interval for each programme operating in the reader's own
  country, issued by that country's national screening body or equivalent committee
  *[country-dependent]*.
* The information leaflet the reader's own national programme sends with its invitations, which is
  the document that actually states the benefits and harms to the public in that country.
* Any standard textbook of epidemiology or public health, for lead-time bias, length-biased
  sampling, and the relationship between incidence, prevalence and sojourn time.
* The methods chapter of any randomised trial of a screening programme, for why outcomes are
  analysed by invitation rather than by attendance.
* Any systematic review of overdiagnosis for the specific disease in question, in the
  epidemiological literature, for the estimated magnitude — which is contested and whose range
  between estimates is wide.

The Pokémon figures are a separate matter and are not covered by the line above. The slot chances,
the Mt. Moon 1F and B2F tables, Zubat's level-22 evolution, the Route 4, Viridian Forest and
Safari Zone version differences, the flute and Cleanse Tag encounter-rate modifiers, the party and
box capacities, and the refusal to throw a ball when both are full, were all read directly from
the pret decompilation projects, which this environment can reach.

## Scope and safety

This is revision material about how a public-health intervention is evaluated, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and nothing here should inform whether any individual attends a screening appointment — that
conversation belongs with the person's own clinician and with the information their national
programme publishes. No age range, interval or threshold appears here on purpose, because those
figures differ by country and are revised. The encounter numbers are real, they stand in for a
mechanism, and no clinical figure should be read out of them. If someone is unwell right now, the
relevant action is to contact local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

Lead-time bias, length-biased sampling and the waste that follows from over-detection are
long-settled facts and are not in dispute. What is contested, and moving, is the *size* of the
waste for several specific programmes and the resulting decisions about whom to invite and how
often. Those decisions are being revised in several countries, in both directions, and in places a
single population-wide interval is being replaced by risk stratification. Anyone relying on a
specific interval or age range should take it from their own national programme's current
publication rather than from here. The Mt. Moon and Kanto numbers are from Red and Blue and are
stable because the games are finished. Correct as a description of consensus in October 2026.
