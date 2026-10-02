---
id: "m014"
slug: polypharmacy-and-deprescribing
style: pokemon
category: general-practice
difficulty: advanced
question: "Why is the number of medicines a risk factor in its own right, and what makes a decision to stop different in kind from a decision to start?"
tags: [polypharmacy, deprescribing, interactions, prescribing-cascade, medication-review]
---

# Four slots and one held item, and the fourth thing you add is the one that loses

A moveset is usually described as a count — how many of the four slots are filled — which makes it
sound like a label. It is better read as a structural claim. As the slots fill, the number of ways
the moves can get in each other's way grows faster than the number of moves, while each new move
does less than the one before it. The two curves have different shapes, they cross, and past the
crossing a perfectly good move makes the Pokémon worse. Anyone who has put **Rain Dance** and
**Solar Beam** on the same Pokémon has met the crossing: any weather except sun halves Solar
Beam's damage, so the two slots are actively fighting.

The useful distinction is therefore not four moves against two. It is a set where every slot is
still earning its place against a set that simply accumulated.

## Why the count itself is the problem

```
   REAL NUMBERS throughout.

   slots filled   pairs that can interfere   what that is
   ────────────   ────────────────────────   ──────────────────────────────────────
        1                    0               one option and nothing to clash with
        2                    1               a second option
        4                    6               one Pokémon, fully kitted
       12                   66               half a party, fully kitted
       24                  276               a party of six, four slots each

   And the other curve. The in-battle Attack multiplier at stat stage n is (2+n)/2, and
   the stage cap is +6. Bulk Up raises Attack one stage per use; Swords Dance raises it
   two, so three Swords Dances reach the cap and a fourth does nothing whatsoever.

       stage    +1      +2      +3      +4      +5      +6     beyond
       mult    ×1.5    ×2.0    ×2.5    ×3.0    ×3.5    ×4.0    ×4.0
       gain    +50%    +33%    +25%    +20%    +17%    +14%      0%

   276 and still climbing, against +14 % and then a wall. That is the crossing.
```

Four mechanisms sit under it, and naming them beats naming a number:

1. **Moves interfere in pairs and in groups.** **Sunny Day** next to **Thunder** is the cleanest
   case: Thunder's accuracy is set to 50 under sun, so one slot halves another slot's reliability.
   No single pair has to look dangerous for the set to be unreliable.
2. **The more slots are filled, the less often each gets used**, and PP is per move, so a set of
   four situational moves runs dry in different places from a set of two reliable ones. Two sets
   with the same count are not equally usable.
3. **Every move is a thing to keep track of.** Attention is finite in a battle exactly as it is
   outside one, and a set can outgrow the Trainer's ability to pick correctly under pressure.
4. **Nothing was tested together.** The sets that have been examined to destruction are the ones
   that appear in regulated formats. A party assembled from four separately sensible ideas is a
   combination nobody has ever run, and the combination is not the thing that was tested.

## The cascade

```
   REAL ITEMS AND MOVES, in the order a Trainer actually reaches for them.

   Will-O-Wisp lands ──► burned: Attack halved, chipped every turn
                              │
                              └── read as a NEW problem ──► hold a Lum Berry
                                        │
                                        └── it cures the burn and is GONE after one use
                                                  │
                                                  └──► add Rest for the full heal
                                                            │
                                                            └── Rest puts it to sleep
                                                                     │
                                                                     └──► hold a
                                                                          Chesto Berry

   And there it stops dead, because a Pokémon holds ONE item. The Chesto Berry and the
   Lum Berry cannot both be there, and whichever one is, it is no longer the Leftovers
   or the Choice Band the slot was originally for.

   Every step was locally reasonable. The error is only visible from outside the chain,
   which is why a review starts from the whole set and asks what each piece is for.
```

## Why taking something away is a different kind of decision

```
   ┌──────────────────────┬────────────────────────────┬─────────────────────────────┐
   │                      │ teaching a move            │ deleting one                │
   ├──────────────────────┼────────────────────────────┼─────────────────────────────┤
   │ where it happens     │ anywhere, straight out of  │ one house, and it is in      │
   │                      │ the bag                    │ Lilycove City               │
   │ what it costs        │ the TM, which is consumed  │ nothing — which is the       │
   │                      │ on use                     │ problem: no record of why    │
   │ when it is refused   │ only if the species cannot │ if it is the Pokémon's last  │
   │                      │ learn the move at all      │ move; and if it is the last  │
   │                      │                            │ Surf in the party AND in the │
   │                      │                            │ storage boxes               │
   │ an HM                │ learned like anything else │ cannot be replaced in the    │
   │                      │ and the HM is NOT consumed │ ordinary flow at all         │
   │ the way back         │ —                          │ Fallarbor Town, one Heart    │
   │                      │                            │ Scale, and only moves       │
   │                      │                            │ already in its own learnset  │
   └──────────────────────┴────────────────────────────┴─────────────────────────────┘
```

Three of those deserve their reasons stated.

**The game treats removal as a specialist act and addition as routine.** A **TM** works from the
bag, in seconds, anywhere — and it is consumed, so the addition is also irreversible in the sense
that matters: the resource is spent. Deleting requires a trip to a named house in Lilycove City.
Nothing about that is an accident of design. Removal is where the damage happens if you get it
wrong, so the game put friction in front of it.

**The last-Surf check is the model for every withdrawal.** The Move Deleter does not just look at
the Pokémon in front of him. He checks the rest of the party and then every box in storage, and if
nothing else knows **Surf** he refuses, because the alternative is a Trainer stranded on a
shoreline with no way across. A withdrawal decision that only looks at the one thing in front of
it has not been made properly. And he refuses outright to delete a Pokémon's only move — there is
a floor, and it is not zero.

**The way back is narrow and it costs.** Fallarbor Town's relearner will restore a move, but only
one already in that species' own learnset, and only for a **Heart Scale**. So the sensible plan
states in advance what would bring the move back and confirms that bringing it back is possible at
all. A removal with no stated route back is a gamble; a removal with one is a deliberate trial,
and those are two different acts even when the keystrokes are identical.

## Where the metaphor stops

Some medicines produce their benefit over a long horizon. Where that horizon and a person's
circumstances no longer match, the balance that justified starting may genuinely no longer hold,
and noticing that is part of good care rather than a withdrawal of it. It is not a judgement about
anybody's worth and it is not a rationing argument. It is also not a conversation that should
arrive as a surprise inside a medication review, which is the practical reason it belongs in an
anticipatory discussion held while there is time for it, with the person themselves deciding what
matters to them.

The other half of the same section, which is easier to forget because nobody reports it. Taking
fifteen medicines is itself a daily experience — the timing, the counting, the swallowing, the
collecting, the cost where there is one, and the constant reminder of being a person with fifteen
conditions. That burden falls on the person and is largely invisible to whoever writes the
prescriptions, because it rarely arrives in a consultation as a complaint about medicines. It
arrives as tiredness, or as not taking them, and both get read as something else.

## The thing not to take away

The counterweight. A Pokémon that has run every move out of PP is reduced to Struggle, which
damages it every time it is used, and a party built on the principle that fewer moves are safer
loses to one that is simply well chosen. The commonest error in a party that has been pruned too
hard is a gap, not a clash. The two questions — what has stopped earning its slot, and what is
missing — are the same review, and a review that only subtracts is as unexamined as one that only
adds.

## What a Gym Leader is listening for

Whether the Trainer separates a set that is full from a set that is cluttered, instead of treating
the count as the verdict. Then the cascade, with a real pair. Then the content of a removal plan,
including what would bring the move back, which is the part most people leave out. Then whether
they would check the boxes as well as the party before deleting anything. Then who is actually
making the decision.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The reader's national or regional formulary, which is the authority for every interaction, dose
  and withdrawal schedule referred to in general terms here (**country-dependent**).
* The national guideline on multimorbidity or on medicines optimisation issued by the body that
  governs the reader's practice, for the definition of appropriate versus problematic polypharmacy
  and for the structure of a medication review (**country-dependent**).
* Any published, maintained screening tool for potentially inappropriate prescribing in older
  people — several exist, issued by different academic groups and updated periodically — read in
  its current edition rather than from memory.
* The reader's national medicines regulator's summary of product characteristics for any specific
  medicine being considered, which is where withdrawal and rebound phenomena are documented
  (**country-dependent**).
* Any systematic review of deprescribing trials in the clinical-pharmacology literature, for how
  thin the withdrawal evidence base is compared with the initiation evidence base.
* The reader's own organisation's structured medication review template, for what is locally
  expected to be recorded.

The Pokémon figures are a separate matter and are not covered by the line above. The stat-stage
multipliers and the +6 cap, Swords Dance being a two-stage boost, Thunder's accuracy under sun,
Solar Beam being halved by any weather except sun, the one-item-per-Pokémon rule, the TM being
consumed on use while an HM is not, the refusal to replace an HM move in the ordinary flow, and
the Move Deleter in Lilycove City with his last-move and last-Surf checks against both the party
and storage, were all read directly from the pret decompilation projects, which this environment
can reach.

## Scope and safety

This is revision material about how a prescribing decision is structured, written for someone
already training in or qualified for the field. It is not a clinical reference, not a decision
aid, and nothing here should inform what any individual takes or ceases to take — that belongs
with the prescriber and the pharmacist who hold the person's full list. No medicine, class, dose,
interval or withdrawal schedule is named here on purpose. The Pokémon numbers are real, they stand
in for a shape, and no clinical figure should be read out of them. Formularies and interaction
data differ by country and change; the local formulary is the authority and must be checked before
anything reaches a patient. If someone is unwell right now, the relevant action is to contact
local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The structural argument — that the ways things can interfere grow faster than the number of
things, while each addition is worth less — is settled and is not expected to move. Treating a
withdrawal as an intervention that needs a plan and a stated route back is now mainstream rather
than novel, which was not true a decade ago. What continues to move is the evidence for
withdrawing specific classes, the content of the published screening tools, and the structure of
the funded medication review, all of which differ by country; take those from current local
sources rather than from here. The Pokémon mechanics quoted are from the games as shipped and are
stable. Correct as a description of consensus in October 2026.
