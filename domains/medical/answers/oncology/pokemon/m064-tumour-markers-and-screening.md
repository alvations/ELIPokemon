---
id: "m064"
slug: tumour-markers-and-screening
style: pokemon
category: oncology
difficulty: advanced
question: "What is a tumour marker actually measuring, and why are almost none of them useful as screening tests even where they are useful for monitoring?"
tags: [tumour-markers, screening, predictive-value, assay, monitoring]
---

# Eight of sixty-five thousand five hundred and thirty-six, and the game can afford a perfect test

The **Shiny** check in Emerald is one line. `GET_SHINY_VALUE` exclusive-ORs the two halves of the
trainer ID with the two halves of the personality value, and the Pokémon is Shiny if the result is
below `SHINY_ODDS`. `SHINY_ODDS` is **8**, and the header's own comment says what that means: 8
out of 65536. One in 8192.

Two things about that test, and the second is the whole answer.

**The base rate is tiny.** For every Shiny there are 8191 that are not.

**And the test is perfect.** It has to read nothing but stored data, and one comparison answers it
exactly. There is no false positive and there cannot be one, because the thing being tested for
*is* the number being computed.

A tumour marker is in the opposite position on the second point and the same position on the
first. It reads a molecule that other things also make, applied to a population in which the
disease is rare. Put those two together and the arithmetic does the rest.

As elsewhere in this specialty: **the objects of study are assays, thresholds, stored values and
power formulae.** No Pokémon in this answer stands in for a person with cancer, and the analogy is
dropped entirely at the end, where the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
**consensus**, **country-dependent**.

## The three reasons, drawn

```
   1. THE BASE RATE DECIDES WHAT A POSITIVE MEANS

      SHINY_ODDS = 8 out of 65536.  8191 ordinary for every one.

      ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ordinary
      ▌                                                                  Shiny

      The game gets away with this because its test reads STORED DATA.
      Now suppose instead a detector that read something CORRELATED —
      and wrongly flagged even a modest fraction of ordinary Pokémon.
      With 8191 ordinary for every one, almost every alarm would be an
      ordinary Pokémon, no matter how good the detector was.

      (NOTE: no such detector exists in the games.  That paragraph is
      arithmetic applied to a real base rate, and is flagged as such.)

   ────────────────────────────────────────────────────────────────────────

   2. THE SIGNAL IS A FUNCTION OF HOW MUCH IS THERE

      Cmd_scaledamagebyhealthratio, for Water Spout and Eruption:

          base power = currentHP × 150 ÷ maxHP     ── and if that comes
                                                      out 0, it is SET TO 1

      full bar ──► 150.   nearly empty ──► 1.   The reading tracks BULK.

      And sFlailHpScaleToPowerTable runs the OTHER WAY: Flail is 200 at
      the bottom of the bar and 20 at the top.  Two moves, one quantity,
      OPPOSITE functions — so "the number is high" means nothing at all
      until you know which function you are reading.

   ────────────────────────────────────────────────────────────────────────

   3. THE READOUT IS NOT SPECIFIC TO WHAT YOU WANT

      Cmd_transformdataexecution copies the target's struct up to the pp
      field — species, types, stats, moves.  It does NOT copy HP or maxHP,
      and it sets each copied move to at most 5 PP.

      So a Ditto that has Transformed is identical in everything you read
      first, and distinguishable in EXACTLY TWO fields you have to know
      to check.  That is a raised marker with a benign cause.
```

## Reason one: the arithmetic of rarity, and why a better machine does not fix it

The proportion of positive results that are true positives depends on how common the condition is
in the tested population, as much as on the test's own characteristics (**mechanism**). Where the
disease is rare, the false positives drawn from the very large well group outnumber the true
positives drawn from the very small affected group, even when the false-positive fraction is
small.

Be clear about what kind of claim that is, because it is the single most misunderstood point in
the subject: **it is arithmetic, not a complaint about an assay.** A better machine does not fix
it. A tighter threshold trades it for lost sensitivity. Only two things genuinely move it:

* **Raise the base rate in the group you test.** This is what restricting screening to a
  higher-risk population does, and it is why eligibility criteria are part of a programme rather
  than an administrative detail.
* **Follow a positive with an independent second test** whose errors are uncorrelated with the
  first's — not a repeat of the same one.

The games supply the first of those as a real mechanic. The **Masuda Method** and the **Shiny
Charm** both raise the Shiny rate; they do not improve any detector, they change the
denominator. Which is exactly the clinical move, and it is the only one of the two that a
programme controls directly.

And every false positive costs something: further imaging, invasive investigation, and a stretch
of being treated as somebody who might have cancer. Those are harms a programme is obliged to
count (**consensus**), and the screening answer in this specialty argues that at length.

## Reason two: Water Spout reads the bar, and Flail reads it backwards

This is the best pair of facts in the answer and both are in the code.

**Water Spout** and **Eruption** are both 150 base power in the move data, and both route through
`Cmd_scaledamagebyhealthratio`, which is three lines: base power becomes
`currentHP × power ÷ maxHP`, **and if that division gives zero it is set to 1**. A **Wailord** at
a full bar fires a 150-power Water Spout. The same Wailord near the bottom of the bar fires
something worth 1.

So the reading tracks **bulk** (**mechanism**). The clinical consequence is uncomfortable and
unavoidable: **a marker's sensitivity is lowest for small-volume disease**, which is exactly the
disease a screening programme exists to find. A marker that detects advanced disease reliably and
early disease unreliably has its sensitivity in the wrong place for screening and in precisely the
right place for monitoring.

Two further properties fall out of the same formula:

* **A marker produced by only some tumours of a type cannot exclude disease.** A normal result
  means either nothing there or a non-producing tumour, and the reading does not distinguish them
  (**mechanism**).
* **"Undetectable" is a statement about the floor.** `Cmd_scaledamagebyhealthratio` never returns
  0; it returns 1. Neither does the health bar, which the response-assessment answer in this
  specialty took apart, and neither does **Super Fang**. Three separate routines in one game, each
  refusing to report zero while anything remains. Every assay has a lower limit of detection, and
  a result at that limit is the limit's result, not the molecule's absence (**definitional**).
  This matters most where a marker is used to look for recurrence after treatment intended to
  cure.

And then the sting, which is the `sFlailHpScaleToPowerTable` from the margins answer read the
other way round. **Flail** and **Reversal** are 200 base power at the bottom of the bar and 20 at
the top. Water Spout and Flail are functions of the *same* quantity with *opposite* slopes. A
number on its own is uninterpretable; you have to know which function produced it. Which is why a
marker is only ever read against a baseline and a direction of travel, never as a bare value.

## Reason three: Transform, and the two fields you have to know to check

`Cmd_transformdataexecution` copies the target's `BattlePokemon` struct from the top up to the
offset of the `pp` array. That takes species, types, every stat, the ability and all four moves.
It stops before `pp`, `hp` and `maxHP`, so those are **not** copied, and the routine then writes
each copied move's PP as the lesser of the move's own PP and **5**.

A **Ditto** that has used **Transform** into an **Alakazam** therefore *is* an Alakazam in
everything the interface shows you first, and differs in exactly two places: it kept its own HP,
and every move it now has reads 5 PP or fewer. Two tells, and you have to know to look for them.

That is a raised marker with a benign cause (**consensus**). Most markers are neither
cancer-specific nor organ-specific: they are raised by benign disease of the same organ, by
inflammation anywhere, by smoking, by pregnancy, by impaired renal or hepatic handling, and
sometimes by nothing that is ever identified. A raised result is a reason to ask a *different*
question, with a different instrument — check the PP, not the sprite — rather than an answer.

## The handful that genuinely are specific, and the games have those too

Read the stat modifiers in Emerald's damage calculation and there is a short run of
`if (species == ...)` conditions. Each is an item whose effect exists for one or two species and
for nobody else:

* **Thick Club** doubles Attack, for **Cubone** or **Marowak**.
* **Light Ball** doubles Special Attack, for **Pikachu**.
* **Deep Sea Tooth** doubles Special Attack and **Deep Sea Scale** doubles Special Defense, for
  **Clamperl**.
* **Metal Powder** doubles Defense, for **Ditto**.
* **Soul Dew** raises Special Defense, for **Latias** or **Latios** — and the same line excludes
  it in **Battle Frontier** battles, which is a ruleset overriding a mechanic and is worth
  noticing.

There are only a handful, each is tied to one or two species, and outside that list the item does
nothing. That is exactly the position of the markers that genuinely are diagnostic
(**consensus**), and the pattern in them is that they are nearly disease-specific **in a defined
context**:

* **Germ-cell tumours**, where the markers are built into the staging and risk classification
  rather than bolted on.
* **Thyroglobulin after total thyroidectomy** — the context is what makes it specific, because the
  tissue that normally makes it has been removed.
* **The paraprotein in plasma cell disorders**, which is a product of the clone itself.

And one genuinely contested case rather than a settled one: **prostate-specific antigen** is
organ-specific and not cancer-specific, and the long argument about it is not about whether it
detects disease but about overdiagnosis and what follows a positive. Policy differs markedly
between countries (**consensus** that it is contested, firmly **country-dependent** in what is
offered).

## What markers are for, and why every argument above reverses

Monitoring. And the reason it works is that all three reasons invert (**consensus**):

* **The population becomes one person already known to have marker-producing disease**, so the
  base rate is no longer the problem.
* **The comparison is to their own earlier value**, not to a population threshold, so differences
  between people stop mattering.
* **Changing bulk is the actual question**, so the Water Spout dependence is the signal rather
  than the limitation.

Which brings in the practicalities that separate competent use from superstition:

* **A baseline before treatment is required**, or there is nothing to read a trend against.
* **The series must be on one assay and platform.** This is the **Pokédex number** problem from
  the staging answer: the same species carries a Hoenn number and a National number, and Emerald
  ships conversion tables in both directions because a bare number is not a statement until you
  know which list it indexes. Two assays for nominally the same marker are two registries, and a
  change of laboratory can look exactly like a change in disease (**consensus**).
* **The rate of fall after treatment carries information**, because the molecule has its own
  clearance; a fall slower than its kinetics predict means something.
* **A change smaller than the noise is not a change.** The **Damage Roll** argument from the
  response-assessment answer applies directly: markers vary between measurements in a stable
  person, and one value crossing a threshold is weaker evidence than a trend.
* **Interference is real.** Very high concentrations can read falsely low on some immunoassay
  formats, and heterophile antibodies can produce spurious results; an implausible number is a
  reason to ring the laboratory (**consensus**).

## Where the metaphor stops

Everything above is arithmetic, thresholds and assay behaviour, and a game with a one-line Shiny
check is a good place to see what a base rate does. What follows is about people, so it is said
plainly and without the analogy.

Someone having a marker measured to monitor a known cancer is waiting for a number they have
learned to read as a verdict — repeatedly, often every few weeks, for years. The waiting is its
own burden, it is widely recognised and named, and it is not cancelled by the number being
reassuring on any particular occasion. A rise that turns out to be ordinary variation still costs
that person the weeks in which they did not know that, and nobody gives those back.

A false positive in a screening context is not a neutral event either. It is a stretch of time in
which somebody who was well is investigated for cancer, with everything that goes with that, and
for some people the anxiety does not fully resolve even once the result is clear. Counting that as
a harm is not a technicality. It is the reason a programme that finds more disease is not
automatically doing more good.

And none of this says what will happen to any individual. A marker is a measurement of a molecule,
not a statement about a person's future, and no figure of any kind appears in either half of this
answer for that reason.

## What a Gym Leader is listening for

* The Shiny check has a tiny base rate and no false positives. Which of those two facts does a
  tumour marker share, and which does it not?
* Masuda Method and Shiny Charm raise the rate. Which half of the predictive-value problem does
  that address, and which does it leave alone?
* Water Spout at a full bar and Flail at a full bar. Why does that pair mean a bare marker value
  is uninterpretable?
* Three routines in one game refuse to report zero. What is the clinical statement that makes?
* A Transformed Ditto differs in exactly two fields. What is the clinical move that corresponds to
  checking them?
* Thick Club works for two species and nobody else. Name the clinical markers that are in that
  position and say what makes them exceptions.
* Why must a marker series stay on one assay, and which earlier answer in this specialty is that
  the same argument as?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific
to this answer:

* **Your own laboratory's handbook**, for the assay in use, its reference interval, its lower
  limit of detection, its known interferences, and whether a result is comparable with a
  historical one. No general account replaces it.
* The guidance on tumour marker use published by your national clinical biochemistry or laboratory
  medicine professional body, for which markers are recommended for which purpose and which are
  explicitly not recommended for screening.
* Your national screening programme's published documentation, for what is and is not offered
  where you are and on what grounds. Marker-based screening policy differs sharply between
  countries.
* The disease-specific guidance for germ-cell tumours, differentiated thyroid cancer and plasma
  cell disorders, for how markers are embedded in staging, risk classification and response
  assessment there.
* A current standard textbook of clinical chemistry, for assay formats, interference and the
  biological-variation argument.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about what a marker measures and what a result can support, dressed in a
game so that the base-rate argument is concrete. It has had no clinical review. **No reference
interval, threshold, detection limit, half-life, sensitivity, specificity or predictive value
appears here, and none should be inferred** — those are properties of a particular assay in a
particular laboratory, they do not transfer, and the laboratory handbook is the authority. This is
not a guide to interpreting anybody's result and it describes no individual's situation. Screening
policy differs by country and is revised; yours governs. Anyone affected by cancer — their own
diagnosis or someone else's — should be talking to the clinical team looking after that person,
who have the results, the history and the context, none of which are here. The analogy carries
arithmetic and measurement only: no part of it stands in for a person, and none of it says
anything about what happens to anybody.

## Where this stands, October 2026

The Pokémon facts are read from Emerald's own source. `GET_SHINY_VALUE` is the exclusive-OR of the
high and low halves of the trainer ID with the high and low halves of the personality value, and
the comparison is against `SHINY_ODDS`, which is defined as 8 with the comment that the
probability is 8 over 65536. `Cmd_scaledamagebyhealthratio` computes base power as current HP
times the move's power divided by maximum HP and sets the result to 1 if it would be 0; Eruption
and Water Spout are both 150 base power in the move data, and Wailord learns Water Spout at level
44 on its own level-up list. `sFlailHpScaleToPowerTable` is six pairs from 1→200 to 48→20.
`Cmd_transformdataexecution` copies the target's struct up to the offset of the `pp` array — which
excludes `pp`, `hp` and `maxHP` — and then writes each copied move's PP as the lesser of the
move's own PP and 5. The species-keyed item conditions are single `if` statements in the base
damage calculation in `src/pokemon.c`: Thick Club for Cubone or Marowak doubling Attack, Light
Ball for Pikachu doubling Special Attack, Deep Sea Tooth and Deep Sea Scale for Clamperl, Metal
Powder for Ditto doubling Defense, and Soul Dew for Latias or Latios raising Special Defense with
an explicit exclusion in Battle Frontier battles. Light Ball doubles only Special Attack in
Emerald; it was widened in a later generation and that later behaviour is not claimed here. The
Masuda Method and the Shiny Charm are later-generation additions described from working knowledge
of those games rather than from code opened here, as is the Gen VI change to the Shiny rate, which
is why the figure quoted above is Emerald's.

The clinical arithmetic is permanent. The dependence of predictive value on prevalence, the bulk
dependence of marker concentration, and the non-specificity of most markers are structural, and
they are why the general position — markers for monitoring, not for population screening — has
been stable for a long time (**consensus**).

What moves is the technology rather than the logic. Multi-cancer early detection assays based on
circulating tumour DNA and related analytes are under active evaluation, and every argument above
applies to them unchanged: in a low-prevalence population, predictive value is governed by
prevalence, and detecting something earlier is not the same as doing more good. Whether any of
them earns a place in a programme is open as of this date and is being answered differently in
different countries. No performance figure for any such assay is quoted here, deliberately —
those are the facts most likely to date, they are contested, and they belong to the primary
literature and the programme documentation rather than to a revision note like this one.
