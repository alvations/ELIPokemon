---
id: "m021"
slug: two-mechanisms-type-1-type-2
style: pokemon
category: endocrinology
difficulty: intermediate
question: "Type 1 and type 2 diabetes are diagnosed by the same measurement. Why are they different diseases?"
tags: [diabetes, type-1, type-2, insulin-resistance, beta-cell]
---

# The field says RAIN in both battles. In one there is no Kyogre, in the other there is a Golduck.

A field condition is a signal, and the HP bar is what you read off the outcome. Both of these
battles show the same bar: falling, turn after turn, for reasons the bar does not state. In the
first, nothing on the team can set rain at all — **Kyogre** is not there and never was, so
**Drizzle** never fires and the condition is simply absent. In the second, Kyogre is standing on
the field and the weather readout says it is raining, and **Golduck** is out opposite with **Cloud
Nine**, which switches off every weather effect on the field without clearing the weather
*(mechanism)*. Signal missing against signal ignored. One bar, two faults, and which fault it is
decides your next six turns.

| In the battle | What it stands for |
| --- | --- |
| Rain, as a field condition | The hormone — ambient, acting on everything, decaying |
| **Kyogre**'s **Drizzle**, firing on entry | The beta cell, secreting as soon as it senses |
| **Toxicroak**'s **Dry Skin**, +1/8 max HP per turn in rain | Tissue taking the load up because it was told to |
| Harsh sunlight, from **Groudon**'s **Drought** | The counter-regulatory, fuel-mobilising state |
| **Solar Power**: +50% Sp. Atk, −1/8 max HP per turn in sun | Burning the body for fuel, which is ketogenesis |
| **Cloud Nine** / **Rayquaza**'s **Air Lock** | Resistance: condition present, nothing responds |
| **Rain Dance** from the move list | Replacement from outside, by hand, on a clock |
| The HP bar | The glucose on the meter |

Claims are marked *(mechanism)*, *(consensus)* or *(guideline-dependent)* where it matters.

## The loop, and the two places it breaks

```
   INTACT                        BREAK ONE                     BREAK TWO
   ──────                        ─────────                     ─────────
   bar starts falling            bar starts falling            bar starts falling
        │                             │                             │
        ▼                             ▼                             ▼
   Kyogre senses it              NO Kyogre ON THE TEAM         Kyogre senses it
        │                             ╳                             │
        │ lag: a turn                 │  nothing can set it         │ lag: a turn
        ▼                             │                             ▼
   Drizzle fires, rain up             │                     Drizzle fires, AND fires
        │                             │                     again, and again  ↑↑↑
        │ lag: end of turn            │                             │
        ▼                             ▼                             ▼
   Dry Skin takes its 1/8,       no condition reaches          GOLDUCK IS ON THE FIELD
   Swift Swim doubles Speed      the field at all              Cloud Nine gates it all  ╳
        │                             │                             │
        ▼                             ▼                             ▼
   bar recovers                  sun takes over unopposed      rain is up and does
   LOOP CLOSES                   → Solar Power burns 1/8       nothing → NO burn either
        │                             │        every turn            │
        └── settles in a band    ── runs out fast ──           ── grinds down slowly ──

   Same bar. Different missing piece. Different move.
```

Two lags sit in that diagram and they matter more than the arrows do. Drizzle fires the instant
Kyogre enters, but **Dry Skin**'s eighth and **Swift Swim**'s doubled Speed are only cashed at the
end of the turn, and the weather and the response have different clocks *(mechanism)*. Worse, the
condition outlives its source: in Generation III the rain Drizzle sets has no timer at all and
stays for the rest of the battle, while from Generation VI it runs five turns, or eight while the
setter holds a **Damp Rock** *(mechanism)*. A loop with that much delay in it does not hold a
value. It ranges inside a band, which is what a healthy bar does.

## Break one: the setter is not on the team

Nothing destroyed the ability. There was never a holder. **Vileplume** has **Chlorophyll** and
**Magikarp** has **Swift Swim**, and neither of them can produce a drop of rain — carrying the
*response* is not carrying the *source*, and a team can be stacked with readers of a condition it
has no way to create *(mechanism)*.

The tell is not the weather readout, because the readout looks identical however the rain arrived.
The tell is what is standing on the field. And once you have used **Rain Dance** yourself, the
readout tells you nothing at all about the opponent's team, because your own move is now in the
measurement *(mechanism)*. That is the whole reason you look for the setter rather than the
condition.

With no setter, sunlight from **Groudon** goes unopposed, and **Solar Power** runs every single
turn: Special Attack up by half, an eighth of maximum HP gone, and no way to switch the ability
off *(mechanism)*. The bar does not drift down. It falls in eighths, and eight turns is the whole
battle. Rain Dance here is not an escalation. It is the missing piece, needed from turn one and
every five turns after that, forever.

A common error is to assume from the readout what kind of team you are facing. Teams without a
setter turn up at every level and in every format, and are routinely misread on the first turn
*(consensus)*.

## Break two: the condition is up and the field is deaf to it

Here the loop runs. Kyogre is in and the rain is real; Cloud Nine simply means no
weather-dependent effect resolves *(mechanism)*. So the earliest sign of trouble is not a bad
readout — it is Kyogre switching in and out to keep re-setting a condition that is already there,
which looks like effort and accomplishes nothing *(mechanism)*. The bar only starts to move once
the setter can no longer keep up, and when Kyogre finally faints there is no rain even nominally.

The graded version is more honest than the switch. **Cloud Nine** and **Air Lock** are
all-or-nothing, but a real team's responsiveness is a fraction: rain is worth a great deal to a
side built on **Swift Swim** and **Dry Skin** users, and almost nothing to a side carrying one,
and that fraction is what actually varies *(mechanism)*.

That long quiet phase is why break two is noticed late. The setter can mask it for a very long
time *(consensus)*, which is also why the side often arrives with **Stealth Rock** already down
and hazards already stacked — not coincidences, the same neglected field.

And residual rain explains why the bar grinds rather than plummets, for a reason that is purely
quantitative. **Solar Power only triggers in harsh sunlight.** One single turn of rain switches it
off completely — and one turn of rain gives Dry Skin exactly one eighth back, which against twenty
turns of accumulated loss is nothing *(mechanism)*. A trace of the condition is enough to stop the
burn and nowhere near enough to fix the bar. That is also why break two usually ends in a long
grind rather than a fast burn, and why the occasional side does burn anyway, so this is a tendency
and not a rule *(consensus)*.

## Why the same bar means something different

* **Implied trajectory.** In break one the bar is on a curve with nothing restraining it. In break
  two the same value usually reflects a slow grind with some regulation left *(mechanism)*.
* **Implied company.** Break two arrives with hazards and chip damage that have been accumulating
  for many turns. A fresh break one usually does not *(consensus)*.
* **Implied urgency.** Whether **Solar Power** is currently burning is asked differently in each,
  and the answer changes what you do this turn *(guideline-dependent)*.
* **Implied answer.** Break one needs the condition supplied from outside, around a source that
  does not exist. Break two has levers in several places — the setter, the gate, the fraction of
  the side that can read the condition, and the hazards underneath — and the bar can be brought
  back, which in break one it cannot *(consensus)*.

## Telling them apart is not done from the readout

A **Castform** changing form, a **Politoed** or a **Pelipper** carrying Drizzle in a later
generation, an **Abomasnow** with **Snow Warning**, a **Tyranitar** with **Sand Stream** — all of
them produce a weather readout, and several produce a falling bar *(consensus)*. You tell them
apart from what is on the field, what is in the bag, and sometimes from the team preview — and the
honest statement is that a meaningful share of first-turn reads are wrong, which is why you revise
the read instead of committing to it.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of a feedback loop breaking in two different places. The loop is a
fair picture. What the two failures mean for a person is not a battle, and is not funny.

Type 1 diabetes means insulin from the day of diagnosis, for life, with no version of the
condition that is managed without it. Type 2 diabetes is not a milder type 1, and the widespread
framing of it as self-inflicted is both wrong and harmful: insulin resistance has genetic, ethnic
and socioeconomic determinants that nobody chooses, and treating a diagnosis as a moral verdict
damages the relationship that the next thirty years of care depends on.

Getting the two confused causes specific harm, which is why the question is worth asking at all.
Someone with type 1 labelled as type 2 can be managed without insulin until they reach
ketoacidosis, which is a medical emergency and sometimes a fatal one. Someone with monogenic
diabetes labelled as type 1 may be given lifelong insulin they did not need. Both happen.

And a note about who is reading. More than in most specialties, someone reading about diabetes is
likely to be living with it rather than revising it — this is a condition people manage
themselves, every day, with no days off. If that is you, none of the above is about your case, and
the label on your records is a clinical judgement made by your own team with information this page
does not have. It is not something to re-derive from an analogy about weather.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* The World Health Organization's classification of diabetes mellitus — for what the categories
  are and the stated basis for each one.
* Your national diabetes guideline from the body that issues it — in the United Kingdom the
  National Institute for Health and Care Excellence, elsewhere the equivalent national authority —
  specifically its sections on diagnosis and classification.
* The American Diabetes Association's annual standards of care document, for its classification
  and diagnosis chapter, which is revised yearly.
* Your laboratory's own handbook, for which islet autoantibody and C-peptide assays it runs and
  how it reports them.
* A current general endocrinology or diabetes textbook, for beta-cell secretory physiology and for
  the quantitative difference between insulin's antilipolytic and glucose-disposal effects.

## Scope and safety

The Pokémon here is doing one job: making a feedback loop and its two failure modes concrete. It
is not a clinical reference, not a decision aid, and not about any individual's care. **No
diagnostic thresholds or targets appear here on purpose** — the real cut-offs, and the units they
are reported in, differ between countries and guideline bodies and are revised, so local guidance
is the authority and this page is not. Nothing here has had clinical review. The metaphor covers
mechanism and stops there: the outcomes of either failure are not material for a battle analogy,
and they are described plainly in the rigorous answer. If someone is unwell now, contact local
emergency services.

## What a Gym Leader digs into next

* Why do you look for the setter rather than the weather readout, once you have used Rain Dance
  yourself?
* Why is the earliest sign of break two a setter working hard with a readout that looks fine?
* Why does one turn of rain stop Solar Power dead without fixing the bar?

## Where this stands, October 2026

The loop and its two breaks are mechanism and do not date. What does date is the cast: which
species carry Drizzle and Drought has changed across generations — Politoed and Pelipper acquired
Drizzle long after Kyogre did — and so has whether ability-set weather carries a timer. Check the
current generation's chart, and for the clinical side check current local guidance for anything
numeric.
