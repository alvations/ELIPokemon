---
id: "m011"
slug: the-undifferentiated-presentation
style: pokemon
category: general-practice
difficulty: advanced
question: "Why does an identical finding mean something different in general practice than in a hospital clinic, and how does prevalence change what it is worth?"
tags: [bayes, prevalence, predictive-value, referral, diagnosis]
---

# The rustle is the same rustle. The floor is not the same floor.

Every patch of tall grass in Kanto carries an **encounter table**: ten slots, each holding one
species at one level, and ten fixed slot chances that never vary from table to table — 51, 51, 39,
25, 25, 25, 13, 13, 11 and 3 out of 256. The slot chances are a property of the engine. *What is
in the slots* is a property of the place. So the grass shaking is an identical event everywhere in
the region, and it means something completely different on **Route 1** than it does on the first
floor of **Mt. Moon**, and different again two floors down.

That gap is the whole subject. On Route 1 the table is exactly half **Pidgey** and half
**Rattata** — Pidgey holds slots 1, 5, 6, 7, 9 and 10 for 128/256, Rattata holds 2, 3, 4 and 8 for
the other 128 — and no amount of walking will produce a **Clefairy**, because Route 1 has no
Clefairy slot at all. On Mt. Moon 1F the table is 202/256 Zubat, 38/256 **Geodude**, 13/256
**Paras** and 3/256 Clefairy. Identical rustle. Utterly different differential.

## The arithmetic, worked

The reading taken off the battle screen is the level. Hold one finding fixed — *the number reads 8
or higher* — and run it on two floors of the same cave, hunting Clefairy for its **Moon Stone**.

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE ENCOUNTER TABLES. The slot chances are
   51 51 39 25 25 25 13 13 11 3 out of 256, in slot order, on every land table in the game.

                  MT. MOON 1F                              MT. MOON B1F
          Clefairy in 1 slot: 3/256 = 1.17%        Clefairy in 1 slot: 11/256 = 4.30%
          (Clefairy there is level 8)              (Clefairy there is level 9)
   ┌───────────┬────────────┬────────────┐  ┌───────────┬────────────┬────────────┐
   │  /256     │  Clefairy  │  not it    │  │  /256     │  Clefairy  │  not it    │
   ├───────────┼────────────┼────────────┤  ├───────────┼────────────┼────────────┤
   │  lvl ≥ 8  │         3  │       177  │  │  lvl ≥ 8  │        11  │       155  │
   │  lvl < 8  │         0  │        76  │  │  lvl < 8  │         0  │        90  │
   ├───────────┼────────────┼────────────┤  ├───────────┼────────────┼────────────┤
   │  total    │         3  │       253  │  │  total    │        11  │       245  │
   └───────────┴────────────┴────────────┘  └───────────┴────────────┴────────────┘

   catches everything   3 / 3  = 100 %         catches everything  11 / 11 = 100 %
   clears the rest     76 /253 =  30.0 %       clears the rest     90 /245 =  36.7 %
   worth of a hit       3 /180 =   1.67 %      worth of a hit      11 /166 =   6.63 %

   The same reading. Almost the same screening power. Four times the chance of being
   the Clefairy — because the floor underneath it holds four times as many Clefairy.
```

Run it in odds and the portable part separates from the local part. The ratio of hit rates is 1.00
÷ (1 − 0.300) = **1.43** on 1F and 1.00 ÷ (1 − 0.367) = **1.58** on B1F — practically the same
number, because it is a property of the reading, not of the cave:

```
   Mt. Moon 1F    starting odds   3 : 253   ×1.43 →  0.0170  →   1.67 %
   Mt. Moon B1F   starting odds  11 : 245   ×1.58 →  0.0710  →   6.63 %

   The ratio travels between floors. The starting odds do not. Learning what a reading is
   worth as a ratio is knowledge you keep; learning that level 8 means 1.67 % is knowledge
   about one floor of one cave.
```

Go one floor deeper and the gradient continues: on **Mt. Moon B2F** Clefairy holds two slots,
13/256 and 3/256, for 16/256 = **6.25%**. One cave, three floors, and the identical rustle is
worth 1.17%, then 4.30%, then 6.25%.

## Why the first patch of grass is genuinely a different place

Four mechanisms, none of them about how good the Trainer is:

1. **The thing being hunted is rare where most walking happens.** On Mt. Moon 1F, Zubat holds six
   of the ten slots. Sixty-seven Zubat come out for every Clefairy, so anything that pulls in
   false alarms will pull in far more Zubat than Clefairy however good the reading is.
2. **Everything arrives early and underdeveloped.** Route 1's Pidgey are level 2 to 5. Nothing has
   evolved, nothing has the moves it will eventually have, and the sprite that walks into the
   battle is the least distinguishable version of itself it will ever be.
3. **A filter upstream changes the table downstream — a Repel is exactly that.** The engine rolls
   the slot *first* and only then cancels the encounter if the level is below the lead's. With a
   level-10 lead on B2F, 129/256 of rolls survive and 16 of them are Clefairy: 16/129 = **12.4%**,
   double the unfiltered 6.25%, and no slot in the table was touched. What also happens is that
   the per-step chance of meeting anything at all drops from 10/256 × 256/256 = 3.9% to 10/256 ×
   129/256 = 2.0%. Fewer encounters, each one worth more. That is a referral.
4. **The two jobs are different.** A walk down Route 1 is about establishing that nothing unusual
   is there. Standing in front of a filtered table is about identifying which unusual thing it is.
   A reading chosen for one job is often the wrong instrument for the other.

## What follows at the edge of the grass

* **Confirming and excluding are different operations.** On Route 1, a reading that says "this is
  the rare one" is informative, because almost nothing is; a reading that says "this is the common
  one" told you what you already knew. Deep in the cave that inverts.
* **Steps are an instrument.** The encounter rate is 25/256 per eligible step on Route 1 but only
  10/256 anywhere in Mt. Moon and 8/256 in **Viridian Forest**, where **Pikachu** sits in the last
  two slots at 14/256. A second lap of the same patch samples the table again, and it is the
  cheapest instrument there is — it costs no **Poké Ball** and no **Great Ball**.
* **A reading measured in one place misleads in another.** The level ranges differ by floor, so
  the same reading has 30.0% clearing power on 1F and 36.7% on B1F. It was never one fixed
  property.
* **Rate and table answer different questions.** The **Safari Zone**'s centre area runs at 30/256
  per step — the highest in Kanto, matched only by its own other three areas — and its last slot
  is **Chansey** at 3/256. A high rate is not a high yield.
* **Which table a place has is a local fact.** The same place is not the same place between
  versions: Red's Route 4 holds **Ekans** in four slots where Blue's holds **Sandshrew**, Red's
  Viridian Forest fills six of its eight ordinary slots with Weedle and Kakuna where Blue's fills
  them with Caterpie and Metapod, and slot 9 of the Safari Zone's centre area is **Scyther** in
  Red and **Pinsir** in Blue. Nobody should carry a table across the boundary.

## Where the metaphor stops

A low prior probability is a statement about a population, and it is delivered to one person. Both
halves of that sentence are true at once, and the harm lives in the gap between them. Of the
people told that something is probably nothing, a small number have the thing — and for them the
reasoning was not careless, it was correct and it was wrong about them. Holding both of those at
the same time is what makes a significant-event review useful rather than an exercise in blame,
and it is also what makes the safety-net in the next question a requirement rather than a nicety.

The harm runs in the other direction too, and is less often counted. Reading a positive result at
a clinic's predictive value when it was produced in a waiting room sends well people into
investigation they did not need: procedures with their own complications, time away from work and
family, and a lasting change in how someone understands their own body. A cascade of investigation
started by one over-read result is a real injury, and the person at the end of it has no way to
know it was avoidable.

And the part that is not statistical at all. The prior a clinician actually uses is not a
published figure; it is partly an impression of the person in front of them. Where that impression
tracks who someone is rather than what they have — their weight, their first language, a
psychiatric diagnosis in their record, their race, how many times they have been in — then
base-rate reasoning stops being arithmetic and becomes a mechanism for not believing people. This
is a documented pattern, not a theoretical risk, and better arithmetic does not fix it. The
question that does some work is whether the same finding in a different person would have been
given the same weight.

## What a Gym Leader is listening for

Whether the Trainer reaches for the ratio rather than the raw percentage, and can say why one
travels and the other does not. Then the direction: is the reading being used to confirm or to
exclude, and is it any good at that direction. Then the honest part — the slot chances are printed
in the engine, but which table a given patch of grass has is something a Trainer learns by walking
it, and that is the term carrying the most uncertainty in the entire calculation.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* Any standard clinical-epidemiology or evidence-based-medicine textbook, for the two-by-two
  table, likelihood ratios and the derivation of predictive value from prevalence.
* The published methodology of the diagnostic accuracy study behind any specific test being
  considered — specifically its stated setting and recruitment, which is what determines whether
  its quoted figures transfer to a primary-care population.
* The suspected-cancer or urgent-referral criteria issued by the national or regional body that
  governs the reader's own practice, for the thresholds that set a downstream clinic's prevalence
  (**country-dependent**).
* Any reporting-standards statement for diagnostic accuracy studies, issued by the relevant
  methodology group, for what a study must disclose about its setting and spectrum.

The Pokémon figures are a separate matter and are not covered by the line above. The slot chances,
the per-step encounter rates, the encounter tables for Route 1, Mt. Moon 1F, B1F and B2F, Viridian
Forest, Route 4 and the Safari Zone's centre area, and the order in which the engine rolls a slot
and then applies a Repel, were all read directly from the pret decompilation projects, which this
environment can reach.

## Scope and safety

This is revision material about reasoning, written for someone already training in or qualified
for the field. It is not a clinical reference, not a decision aid, and not for use in making a
decision about any person's care. The encounter numbers are real; they are standing in for a
mechanism, and no clinical figure should be read out of them. The clinical half of this pair
attaches no sensitivity, specificity or prevalence to any real test on purpose, and neither does
this one. Referral criteria and the resulting case mix differ by country, region and institution —
local guidance is the authority, and this is not. If someone is unwell right now, the relevant
action is to contact local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The mechanism — that what a finding is worth depends on the table underneath it, while the ratio
it carries does not — is settled and is not expected to move. The encounter numbers quoted are
from Red and Blue and are stable because the games are finished. What moves on the clinical side,
and quickly, is which tests exist in primary care, what they actually measure, and the referral
thresholds that set downstream prevalence. Re-check all three against current local guidance
rather than taking them from here, as of October 2026.
