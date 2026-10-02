---
id: "m047"
slug: multimorbidity-and-guidelines
style: pokemon
category: general-practice
difficulty: advanced
question: "Why do single-disease guidelines stop composing once a person has four conditions, and what has to replace them?"
tags: [multimorbidity, guidelines, treatment-burden, competing-risk, prioritisation]
---

# Both tables are right. The product is printed in neither of them

The **Type Chart** is the best-documented object in Pokémon. Every row is published, every row is
correct, and a Trainer can recite that Rock is **Super Effective** against Fire, Ice, Flying and
Bug, and **Not Very Effective** against Fighting, Ground and Steel. Nothing in that list is
contested or revised.

And it still does not tell you what **Stealth Rock** does to the thing in front of you, because
the engine does not look up a row. It looks up two rows and *multiplies them*, and then maps the
product onto a fraction of maximum HP. The answer it produces is a number that appears in neither
row, and the published chart cannot warn you about it, because having two types at once is exactly
the case a single row does not model.

## One hazard, seven real species, a sixteen-fold spread

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE CODE. The hazard routine multiplies the
   Rock modifier for type 1 by the Rock modifier for type 2, then maps:
   ×0.25 → maxHP/32   ×0.5 → maxHP/16   ×1 → maxHP/8   ×2 → maxHP/4   ×4 → maxHP/2

   species      types             Rock v t1   Rock v t2   product   damage on entry
   ──────────   ───────────────   ─────────   ─────────   ───────   ───────────────
   Charizard    Fire / Flying        ×2          ×2         ×4        maxHP / 2
   Articuno     Ice / Flying         ×2          ×2         ×4        maxHP / 2
   Skarmory     Steel / Flying       ×0.5        ×2         ×1        maxHP / 8
   Scizor       Bug / Steel          ×2          ×0.5       ×1        maxHP / 8
   Snorlax      Normal               ×1           —         ×1        maxHP / 8
   Swampert     Water / Ground       ×1          ×0.5       ×0.5      maxHP / 16
   Steelix      Steel / Ground       ×0.5        ×0.5       ×0.25     maxHP / 32

   Steelix to Charizard is a SIXTEEN-FOLD spread off one hazard, and the chart contains
   none of these numbers. But the row that matters is the middle three:

        Skarmory  ×0.5 × ×2  = ×1        three different routes
        Scizor    ×2   × ×0.5 = ×1       to the same ordinary-looking
        Snorlax   ×1          = ×1       answer

   A Trainer who reads maxHP/8 off the screen cannot tell which route produced it. Two
   of the three are products of abnormal terms that happen to cancel, and acting on
   either single term alone would have been correct by the chart and wrong here.
```

The same species makes the point from the other side. **Scizor** is exactly average against
Stealth Rock — and because Fire is Super Effective against both Bug and Steel, it takes ×4 from a
Fire move. One Pokémon, two hazards, and reading either result as a property of Scizor rather than
of the pairing gets the other one wrong.

## Then three more layers, each of which overrides the ones above it

```
   REAL MECHANICS, in the order the engine applies them. Earthquake, a Ground move,
   against Flygon, which is Ground / Dragon and whose only ability is Levitate.

   layer 1  the type product     Ground v Ground ×1  ×  Ground v Dragon ×1   =  ×1
                 │
   layer 2  the ability          Levitate sets a GROUND modifier to ×0 outright
                 │                                                            →  ×0
   layer 3  the field            Gravity, 5 turns, suspends Levitate
                 │                                                            →  ×1
   layer 4  the held item        one slot, and Heavy-Duty Boots makes its holder
                                 NOT AFFECTED BY HAZARDS AT ALL — the whole
                                 sixteen-fold table above collapses to zero

   Four layers. Each is documented. Each overrides the ones above it. And the printed
   Type Chart is layer one of four, which is why quoting it is not an answer.

   The limiting case, for completeness: Shedinja is Bug / Ghost with 1 base HP and
   Wonder Guard, which forces the modifier to ×0 for ANY damaging move that is not
   super effective. Nothing in the type chart predicts a column of zeroes.
```

## When two correct recommendations are opposites

This is the layer that has no equivalent in a single-species table at all, because it needs two
species to exist at once.

**Rain Dance** sets rain for 5 turns — 8 if the user holds a **Damp Rock** — and under rain the
engine multiplies Water-type damage by 1.5 and Fire-type damage by 0.5. **Sunny Day** does the
mirror image with a **Heat Rock**: Fire ×1.5, Water ×0.5.

So consider a party holding both **Blastoise** and Charizard. The single-species reasoning for
Blastoise says *set rain*. The single-species reasoning for Charizard says *never set rain*. Both
are correct. The field is one field. There is no weather that satisfies both, and no amount of
re-reading either recommendation produces a third option, because neither recommendation was
written in the knowledge that the other Pokémon existed.

Two further details that follow, and they are the ones a careful Trainer gets wrong:

* **Protecting one from the other's treatment costs the item slot.** A **Utility Umbrella** sets
  the weather multiplier back to ×1.0 for whoever holds it. That genuinely solves the conflict —
  and it is now holding an umbrella instead of **Leftovers** or a **Choice Band**, and a Pokémon
  holds one item. This is the cascade from the four-slot problem arriving by a different door.
* **A weather benefit has a horizon and the hazard cost does not.** Rain runs 5 turns, or 8 with
  the rock, and then stops. Stealth Rock is paid on every entry for the rest of the battle. A
  recommendation whose benefit expires in five turns is a different recommendation when the thing
  it is competing against is permanent.

And one more, because it is the cleanest case of an intervention that helps one condition while
being a harm in another: **Sandstorm** multiplies a Rock-type defender's effective Special Defence
by 1.5, which is a real and substantial gift, while being a damaging weather for everything on the
field that is not Rock, Ground or Steel. In a party of six, that is one Pokémon's treatment and
five Pokémon's side effect, decided by a single move.

## What replaces reading four tables

Not nothing, and not vibes. A prioritised plan, which is a harder thing to write and the only
thing that can exist:

* **Decide what the party is for, before ranking anything.** Without a stated objective there is
  no ordering relation and prioritisation is arbitrary. Two Trainers with identical six Pokémon
  will rank speed, bulk and coverage differently, and the ranking is theirs to supply.
* **Write down which recommendation you are deliberately not following.** Leaving Charizard with
  no answer to Stealth Rock is a decision; not having noticed is a gap. From outside they look
  identical, and only one of them can be reviewed.
* **Count the slots as a cost on the same page as the benefits.** Four moves and one held item,
  per Pokémon, and every recommendation spends from them.
* **Prefer the mechanism to the table where they diverge.** The multiplication composes. The
  published rows do not. Reasoning from how the layers combine is the only tool available once no
  row covers the combination.
* **Name the horizon for everything you keep.** Five turns, eight turns, or permanent.

## The counterweight, stated as strongly as the argument

Complexity is not a reason to do less. **Heavy-Duty Boots** is a real fix that voids the entire
sixteen-fold table for one slot of one Pokémon, and the commonest error in a party assembled by a
Trainer who has concluded that the interactions are too tangled to reason about is not
over-treatment — it is a gap. A party that drops every answer because the answers interact loses
to a party that picked a priority and accepted a known cost somewhere else. The two questions —
what is composing badly, and what is missing entirely — are the same review.

## Where the metaphor stops

Four conditions is one life. The person is doing the integration already — across appointments, in
the gaps between letters, with no clinical training and no access to the reasoning that produced
any of the four plans. When a service says it is hard to combine four guidelines, it is describing
work it has handed to the least-equipped person in the system.

The experience of multimorbidity, as people describe it, is less about any single condition than
about the volume of the apparatus: the letters, the differing instructions, the having to explain
the whole history again to each new clinician, the appointments that conflict, the sense that
every clinician is confident about their slice and nobody is responsible for the whole. That
burden is not an inconvenience around the edge of care. For many people it is the dominant part of
living with illness, and it is almost entirely invisible in the record.

Two things follow that are worth saying directly. Asking what matters most to someone is not a
soft skill bolted onto a technical decision — in this situation it is the technical step without
which the decision cannot be made at all. And a conversation about a shortened horizon has to be
offered when there is time for it, not discovered inside a medication review, and the person
decides how far it goes.

## What a Gym Leader is listening for

Whether the Trainer says *the engine multiplies* without being prompted, rather than reciting the
chart. Then the middle three rows: three routes to maxHP/8, and why a composed answer that looks
ordinary is not evidence that anything is ordinary. Then the override stack, in order, including
which layer beats which. Then the weather case, argued from both Pokémon at once. Then the horizon
— five turns against permanent. Then the counterweight, offered unprompted. Then the hard one: how
you would tell a party that was properly prioritised from one that simply gave up, given that both
leave recommendations unfollowed.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../for-agents/SOURCES-general-practice.md`](../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The national guideline on multimorbidity or on the care of people with several long-term
  conditions, issued by the body that governs the reader's practice, which is the document that
  states the prioritisation approach expected locally *[country-dependent]*.
* The eligibility criteria sections of the pivotal trials behind any specific recommendation being
  applied, which is where the applicability question is actually settled.
* Any systematic review of the representation of multimorbidity in randomised trials, in the
  clinical-epidemiology literature, for the scale of the exclusions.
* The published literature on treatment burden and on the cumulative complexity of care, for the
  vocabulary and for the instruments that attempt to measure it.
* Any analysis of time-to-benefit for the specific intervention in question, which is the number
  that makes the competing-risk argument concrete rather than rhetorical.
* The reader's own organisation's structured medication review and care-planning templates, for
  what is locally expected to be recorded about recommendations deliberately not followed.

The Pokémon figures are a separate matter and are not covered by the line above. The Generation
III type chart rows quoted, the hazard routine multiplying the modifier for each of the
defender's types and mapping the product onto maxHP/32, /16, /8, /4 and /2, the type pairings and
base HP of Charizard, Articuno, Skarmory, Scizor, Snorlax, Swampert, Steelix, Flygon and Shedinja,
Levitate zeroing a Ground modifier unless Gravity is active, Gravity lasting 5 turns, Wonder Guard
zeroing anything not super effective, Heavy-Duty Boots exempting its holder from hazards
altogether, rain and sun multiplying Water and Fire damage by 1.5 and 0.5, weather lasting 5 turns
or 8 with the matching rock, the Utility Umbrella restoring ×1.0 for its holder, Thick Fat halving
Fire and Ice, and sandstorm multiplying a Rock-type's Special Defence by 1.5 from Generation IV
onward, were all read directly from the pret and rh-hideout decompilation projects, which this
environment can reach.

## Scope and safety

This is revision material about how clinical recommendations are combined, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and nothing here should inform what any individual takes, stops or attends — that belongs
with the clinicians and the pharmacist who hold the person's full list and know their
circumstances. No medicine, class, condition pairing, target or threshold is named here on
purpose. The Pokémon multipliers are real and are standing in for a shape; no clinical figure
should be read out of them, and the sixteen-fold spread above is a fact about an entry hazard and
nothing else. Formularies and guidelines differ by country and are revised, and the local versions
are the authority — this is not. If someone is unwell right now, the relevant action is to contact
local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The structural argument — that a guideline is a conditional recommendation and that the condition
fails under multimorbidity — is mainstream and stable, and has been for long enough that national
guidance on the topic now exists in several countries. What continues to move is the practical
apparatus: how combined reviews are specified and funded, whether incentive frameworks reward a
single prioritised plan or a set of disease-specific indicators, and how time-to-benefit estimates
are published for individual interventions. Risk-prediction tools built for people with several
conditions are arriving and are not yet well validated across populations. The Pokémon mechanics
quoted are generation-pinned where they differ between generations and are otherwise stable
because the games are finished. Take the local prioritisation framework, and any specific
time-to-benefit figure, from current sources rather than from here, as of October 2026.
