---
id: "m050"
slug: health-inequality-as-mechanism
style: pokemon
category: general-practice
difficulty: advanced
question: "Why is the inverse care law a mechanism rather than a complaint, and what does treating it as a mechanism change?"
tags: [health-inequality, inverse-care-law, access, equity, proportionate-universalism]
---

# A multiplier, awarded for having already won, and switched off in a link battle

**Red** and **Blue** contain a routine most Trainers never learn about, and it is the cleanest
statement of a compounding advantage in the whole game. Four of the eight badges silently raise
your own Pokémon's stats in battle, by an eighth each:

```
   REAL NUMBERS, FROM THE CODE. The boost is applied for badges whose bit position is
   even, and the operation is stat := stat + (stat >> 3), which is ×1.125, capped at 999.

   badge            from                            raises
   ──────────────   ─────────────────────────────   ──────────────────
   Boulder Badge    Brock, Pewter City              Attack   ×1.125
   Thunder Badge    Lt. Surge, Vermilion City       Defence  ×1.125
   Soul Badge       Koga, Fuchsia City              Speed    ×1.125
   Volcano Badge    Blaine, Cinnabar Island         Special  ×1.125

   And the other four — Cascade, Rainbow, Marsh, Earth, from Misty, Erika, Sabrina and
   Giovanni — give no stat boost at all. Those are the four that set the obedience
   thresholds instead. The eight badges split perfectly in two, even bits and odd bits,
   and nobody is told which four do which.
```

Three things about that routine, and they are the argument.

## It is a relative boost, so the absolute gap widens even when it is applied fairly

```
   REAL ARITHMETIC. The engine adds stat >> 3, which is an eighth, truncated.

   two Pokémon, same Trainer, same four badges, boost applied EQUALLY to both:

                      before    + (stat>>3)    after
   ┌──────────────┬───────────┬─────────────┬──────────┐
   │ the weaker   │    60     │     + 7     │    67    │
   │ the stronger │   160     │     + 20    │   180    │
   ├──────────────┼───────────┼─────────────┼──────────┤
   │ mean         │   110     │             │  123.5   │   ▲ up 13.5
   │ ABSOLUTE GAP │   100     │             │   113    │   ▲ up 13
   │ ratio        │   2.67    │             │   2.69   │   ─ essentially flat
   └──────────────┴───────────┴─────────────┴──────────┘

   Both improved. The boost was identical in rule and in proportion. The gap got wider,
   because an eighth of 160 is not an eighth of 60. Nothing unfair happened in the
   application and the distribution still got less equal.

   And at the top the cap bites, which is the other direction of the same point:

      a stat already at 950  ──►  950 + 118 = 1068, truncated to the 999 ceiling
                                  the boost is partly thrown away at the top, and
                                  fully delivered in the middle
```

## It is awarded for having already succeeded, and the award is sequenced

The boost arrives only after you have beaten the Gym that grants it, and the Gyms come in a
largely fixed order — **Pewter City**, then **Cerulean City**, then **Vermilion City**, then
**Celadon City**, **Fuchsia City** and **Saffron City** with some latitude between them, then
**Cinnabar Island**, and **Viridian City** last of all. So the Trainer who is struggling at
**Brock** has none of the four boosts, and the Trainer who is already through **Blaine** has
all four. The help is distributed in proportion to how little of it you
need, by design, and no individual decision anywhere in the game produced that. The ordering did.

## And it does not apply in a link battle

The routine's first instruction checks whether this is a link battle and **returns immediately if
it is**. So in the one format where two Trainers are compared like with like, the advantage is
switched off entirely and cannot be seen.

That is the measurement problem in one line of assembly. An evaluation conducted under tournament
conditions will report, correctly, that badges make no difference to stats — and it will be
describing a format that has the mechanism disabled. The gradient exists only in the overworld,
which is the part nobody measures.

## The priced route that does not exist

```
   REAL CODE, REAL TEXT. The Bike Shop in Cerulean City.

   the menu's price string                 "¥1000000"
   the player's money field                3 bytes of BCD  →  maximum ¥999 999

   so the price is ONE YEN above the largest number the game can hold, and there is
   no path in the shop's script that sells a Bicycle for money at all. Choose BICYCLE
   and the clerk prints the cannot-afford line unconditionally. Your balance is never
   even checked.

   the route that works:
        Bike Voucher in the bag  ──►  the clerk hands over the Bicycle and takes
                                      the voucher. Money is irrelevant.

   where the voucher comes from:
        the Pokémon Fan Club chairman, in Vermilion City, who offers to tell you a
        story about his Pokémon. Say YES and you get the voucher. Say NO and the
        script goes to the branch that gives you nothing.

   Same bicycle. Two routes. The priced route is a fiction, and the working route is
   paid for in being in the right room, talking to the right person, and having the
   time and the patience to sit through a story.
```

## The price per unit falls as you get further along

This is the mechanism with the most verified arithmetic behind it, and it runs in exactly the
wrong direction.

```
   REAL PRICES AND REAL HEAL AMOUNTS, FROM THE CODE.

   item            heals     price     per HP    first on sale in
   ─────────────   ───────   ───────   ───────   ─────────────────────────────────
   (nothing)         —         —         —       Viridian City sells NO HP item
   Potion            20       ¥300      ¥15.00   Pewter City
   Super Potion      50       ¥700      ¥14.00   Vermilion City
   Hyper Potion     200     ¥1 500      ¥7.50    Cinnabar Island, Saffron City
   Fresh Water       50       ¥200      ¥4.00    Celadon Department Store roof
   Soda Pop          60       ¥200      ¥3.33    Celadon Department Store roof
   Lemonade          80       ¥200      ¥2.50    Celadon Department Store roof

   Six-fold. And the vending machine is its own joke: the sign above it reads ¥200,
   ¥300 and ¥350, and the code deducts ¥200 whichever you pick — so the best value in
   Kanto is also mispriced on the label, in the customer's favour, on a roof.

   The same ladder runs through the Repels, and here the per-unit cost is the point:

   item            steps     price     per step   first on sale in
   ─────────────   ───────   ───────   ────────   ────────────────────────────────
   Repel             100      ¥350      ¥3.50     Cerulean City
   Super Repel       200      ¥500      ¥2.50     Lavender Town, Celadon City
   Max Repel         250      ¥700      ¥2.80     Cinnabar Island, Saffron City

   A Trainer in Cerulean City can buy only the ¥3.50-per-step option. The ¥2.50 one
   exists, is cheaper outright AND cheaper per step, and is four cities away. Paying
   forty per cent more per step is not a choice that Trainer made.
```

## Two more, briefly, because they are the same shape

**The experience split pays whoever was already in the battle.** The routine divides the defeated
Pokémon's base stats, catch rate and base experience by the number of Pokémon gaining experience,
and it only pays the ones whose gain-experience flag is set — which is to say, the ones that were
actually sent out. Whatever needed the experience most had to survive being sent out in order to
receive any of it. And the multipliers compound in the same direction: a trainer battle pays 1.5×,
and a traded Pokémon earns 1.5× on top.

**The Day Care charges at collection, not at deposit.** The fee is ¥100 per level gained plus a
flat ¥100, and if you cannot pay it, the script sends you away and the Pokémon stays there. A
charge at the point of collection is a filter on whoever has the money at the moment they need
the thing back, which is not the same set of people as those who needed it.

## The honest limit of all of this

Most of what makes a party strong is not the badge boost. It is base stats, type coverage, levels
and move choice, and a Trainer who explains every loss by the four badges has stopped reading the
**Type Chart**. An eighth is an eighth; it is real, it compounds, and it is nowhere near the
largest term.

The defensible version of the claim is narrower and still substantial: the badge mechanism, the
city ladder, the voucher and the vending machine are not the main reason one party is stronger
than another, and they do all push in the same direction, and every one of them was a design
decision that could have been made differently.

## Where the metaphor stops

Every mechanism above is also an experience. Being the person who cannot get through on the
telephone at eight in the morning because they are already at work. Being the person who has
explained the same history six times because nobody is their clinician. Being the person whose
new symptom is read against a diagnosis already in the file. Being the person who was offered the
same leaflet as everybody else and for whom it was written in a register they do not read. None
of that arrives in a consultation as a complaint about access; it arrives as lateness, as
non-attendance, as apparent disengagement, and all three get recorded as facts about the person.

The part that should be stated without hedging: a pattern of outcomes that tracks who someone is
rather than what they have is not an unfortunate by-product of a system under strain. It is the
system's output, and it is produced by arrangements that people chose and can choose differently.
Describing it as a mechanism is not a way of removing responsibility — it is the only way of
locating it somewhere it can be acted on.

## What a Gym Leader is listening for

Whether the Trainer names mechanisms rather than restating that the game is unfair. Then the
arithmetic, unprompted, because it is the point most often missed: 60 → 67 and 160 → 180, both
improved, gap wider. Then the link-battle check, and what it means that the advantage is invisible
in the only format anyone compares results in. Then the bicycle: that the priced route is
unrepresentable and the working route costs patience. Then the per-step Repel ladder, with the
¥3.50 and the ¥2.50 the right way round. Then the honest limit — how much of the gap the badges
actually account for — and why overstating it is also a failure.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The original paper in which the inverse care law was named, by the general practitioner who
  proposed it, read in full rather than from the phrase — the mechanisms are in the paper and the
  phrase on its own has become a slogan.
* The major national reviews of health inequality commissioned in the reader's own country, which
  are where proportionate universalism and the social-determinants framing are set out at length
  *[country-dependent]*.
* The World Health Organization's published work on the social determinants of health, for the
  framework and for the international comparisons.
* The capitation or allocation formula used to fund primary care in the reader's own system,
  including its need adjustment, which is the document in which the supply mechanism is either
  corrected or embedded *[country-dependent]*.
* Any published analysis of coverage, uptake or outcome by deprivation, ethnicity or disability
  for the specific programme in question, which is the only place a gradient can be seen at all.
* The health-services-research literature on intervention-generated inequality, for the general
  result that interventions requiring individual agency tend to widen gradients.

The Pokémon figures are a separate matter and are not covered by the line above. The badge
stat-boost routine, its even-bit selection of the Boulder, Thunder, Soul and Volcano Badges, the
stat := stat + (stat >> 3) operation, the 999 cap, and its immediate return in a link battle; the
four remaining badges being the obedience ones; the Gym order and the city each Leader is in; the
Bike Shop's ¥1 000 000 price string, the player's money being three bytes of BCD, the absence of
any money path for the Bicycle and the voucher path that replaces it; the Pokémon Fan Club
chairman's yes-or-no branch; the Gym order and the fact that Viridian's opens last; the heal
amounts and prices of the Potion, Super Potion, Hyper
Potion, Fresh Water, Soda Pop and Lemonade, the vending machine deducting ¥200 for all three
drinks, and the mart inventory of every city including Viridian City's lack of any HP item; the
Repel step counts and prices and which marts stock which; the experience routine dividing base
stats, catch rate and base experience by the number of Pokémon gaining experience and paying only
those whose flag is set; the 1.5× multipliers for a trainer battle and for a traded Pokémon; and
the Day Care's ¥100-per-level fee charged at collection, were all read directly from the pret
decompilation projects, which this environment can reach.

## Scope and safety

This is revision material about how a health system distributes care and why that distribution has
clinical effects, written for someone already training in or qualified for the field. It is not a
clinical reference, not a decision aid, and not for use in making a decision about any person's
care. The Pokémon prices, boosts and ladders are real and are standing in for a mechanism; none of
them is a measured value for any programme or population and no clinical figure should be read out
of them. Funding formulas, access arrangements, charges at the point of use and the shape of the
gradient itself differ substantially between health systems, and local data is the authority on
the local gradient — this is not. If someone is unwell right now, the relevant action is to
contact local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The inverse care law itself, and the mechanisms listed here, are long established and are not in
dispute. The arithmetic by which an evenly applied relative improvement widens an absolute gap is
settled and is still routinely omitted from evaluations, which is why it is given the most space
above. What is moving fast is the access layer: triage-first and digital-first contact models,
remote consulting, and app-mediated booking have all scaled since the start of the decade, and the
evidence on their equity effects is genuinely mixed and still accumulating — some channels have
widened access for people in inflexible employment while narrowing it for people without reliable
connectivity, language or digital identity. Funding formulas and their need adjustments are
revised on political rather than scientific cycles. The Red and Blue numbers are stable because
the games are finished. Take local gradient data, local access arrangements and the current
allocation formula from current sources rather than from here, as of October 2026.
