---
id: "m093"
slug: bone-remodelling-and-its-fast-markers
style: pokemon
category: endocrinology
difficulty: intermediate
question: "Bone remodelling is a slow balance. Why is it monitored with markers that move in weeks, and what can those markers not tell you?"
tags: [bone, remodelling, turnover-markers, osteoporosis, coupling]
---

# A Pomeg Berry raises the friendship counter twice as fast as an HP Up does, and takes the stock away while it does it

Two hidden counters in Generation III, both running from 0 to 255, neither of them ever shown on
the screen. That is the whole answer, and the trap is that one of them responds to everything and
the other one responds to almost nothing.

**Effort Values** are the slow stock. Each stat has its own counter, capped at 255, with 510
across all six, and nothing in the game displays any of them (**mechanism**). The visible stat is
computed from the stock, and only when `CalculateMonStats` runs — so the stock can move repeatedly
with no visible change at all until something triggers a recalculation.

**Friendship** is the fast counter. It runs 0 to 255, it is also never displayed, and it moves on
nearly every event the game has a name for. You read it out through **Return**, whose base power
is friendship × 10 ÷ 25, topping out at 102 — the integral device from the glycation answer,
carried over unchanged (**mechanism**).

Now the fact that makes the pair worth a whole answer. Feed an **HP Up** and the stock goes
**up**; the friendship change is defined as 5, 3 or 2 depending on which band it is already in.
Feed a **Pomeg Berry** and the stock goes **down**; the friendship change is defined as 10, 5 or 2
(**mechanism**). The item that **removes** the stock moves the fast counter twice as far as the
item that adds to it. The fast counter is reporting that something happened. It is not reporting
which way.

| In the battle | What it stands for |
| --- | --- |
| **Effort Values**: six counters, 255 each, 510 total, hidden | The stock of bone, and its ceiling |
| The displayed stat, recomputed only by `CalculateMonStats` | The density measurement, taken at intervals |
| **Friendship**, 0–255, hidden, read out by **Return** | A turnover marker, fast and summed |
| **HP Up**, **Protein**, **Iron**, **Calcium**, **Zinc**, **Carbos** | Deposit, one item per counter |
| **Pomeg**, **Kelpsy**, **Qualot**, **Hondew**, **Grepa**, **Tamato Berry** | Removal, one item per counter, same counters |
| A berry moving friendship 10/5/2 against a vitamin's 5/3/2 | The marker moved. Which way did the stock go? |
| `EV_ITEM_RAISE_LIMIT`, 100 against a cap of 255 | A plateau the readout does not announce |
| **Pokérus** ×2 and a **Macho Brace** ×2 on effort gain | Turnover rate, raised |
| The **Macho Brace** halving Speed while it is worn | The cost paid *while* the rate is raised |
| **Stockpile** capped at 3; **Spit Up** and **Swallow** both resetting it | Coupling: one mechanic, two phases |
| The **Protect** consecutive-use counter, reset by a gap | A signal whose pattern is part of the signal |
| **Low Kick** reading `GetPokedexHeightWeight` | A reading taken from a reference, not the individual |
| **Shuckle**'s base 230 Defence, **Blissey**'s base 255 HP | Why a population comparison hides the distribution |

**This answer defers to two others.** m059 owns the loop with its clocks. m023 owns **Return** as
the integral, and m060 owns the **Protect** counter as pulsatility — both appear here doing
narrower jobs, and neither argument is re-derived.

Claims are marked (**mechanism**), (**definitional**), (**consensus**) or (**country-dependent**)
where it matters.

## The cycle, drawn with its clocks

```
   ONE SITE, in sequence. The widths are the point.

   trigger      REMOVAL                  pause    DEPOSIT
     ·          ████████                    ·      ████████████████████████
                the Pomeg Berry's phase            the HP Up's phase
                weeks                              months
                                                        then the stat is
                                                        recomputed at last
                                                        ░░░░░░░░░░░░░░░░░░░░
                                                        longer still

   ── WHAT THE FAST COUNTER SEES ─────────────────────────────────────────────

   Friendship moves on EVERY event with a name: a level, a vitamin, a berry,
   128 steps of walking, a battle against a Leader or the Elite Four. It is a
   SUM over everything happening anywhere, right now, to one Pokémon.

   It has no site. It has no direction. It has a band, and that is all.

   ── WHY RAISING THE RATE LOWERS THE READING ALL BY ITSELF ──────────────────

   Macho Brace OFF    ·──────┐                 effort gain ×1
                             └─ Speed intact

   Macho Brace ON     ·─┐ ·─┐ ·─┐ ·─┐ ·─┐      effort gain ×2
                        └───┴───┴───┴───┴─ and Speed HALVED the whole time

   GetWhoStrikesFirst applies the Macho Brace halving BEFORE the paralysis
   quartering, every turn the brace is worn. The stock is being built faster
   and the measurable performance is worse for exactly as long as that lasts.
   Take the brace off and the measurement recovers without the stock changing.
```

## Coupling: one counter, two items, and they are the same mechanic

Look at what the Generation III item data actually says. **HP Up** carries `ITEM4_EV_HP` with
`ITEM6_ADD_EV`. A **Pomeg Berry** carries `ITEM4_EV_HP` with `ITEM6_SUBTRACT_EV`. **Protein** and
a **Kelpsy Berry** are the same pair for Attack. **Iron** and a **Qualot Berry** for Defence,
**Calcium** and a **Hondew Berry** for Special Attack, **Zinc** and a **Grepa Berry** for Special
Defence, **Carbos** and a **Tamato Berry** for Speed (**mechanism**).

Six counters, twelve items, and every item is addressed to a counter rather than to a direction.
Deposit and removal are not two systems that happen to touch the same number. They are **one field
in the save data with two accessors**, and that is the shape of the real thing: suppress the
removal phase and the deposit phase falls with it, after a delay, because there was only ever one
process (**consensus**). A reader who expects to block removal and watch deposit rise has assumed
two levers where the data has one field.

The **Stockpile** family says the same thing from the other direction. **Stockpile** caps the
counter at 3 and a fourth use sets `MOVE_RESULT_MISSED`. **Spit Up** does nothing at all at 0, and
when it does fire its damage is the base figure times the counter and then the counter goes
**straight back to 0**. **Swallow** also does nothing at 0, restores `maxHP / (1 << (3 -
counter))` — a quarter at one layer, a half at two, all of it at three — and also resets to 0
(**mechanism**). And the detail that makes it: **Swallow** used at full HP wipes the counter and
heals nothing. You cannot spend what was not laid down, you cannot spend part of it, and spending
it where it cannot go anywhere throws it away.

## Why the pattern of a signal matters as much as its amount

The cleanest mechanic in the games for this is the **Protect** counter, which the
reproductive-axis answer already owns and which does a different job here. `Cmd_setprotectlike`
reads `gLastResultingMoves` and, if the last resulting move was not **Protect**, **Detect** or
**Endure**, sets `protectUses` back to **zero** before it rolls (**mechanism**). Use the same move
in a run and the success rate collapses — 1, then a half, then a quarter, then an eighth in
Generation III. Space the same move out and it works every time.

Same move. Same user. Opposite outcome, decided entirely by **the shape of the exposure**. That is
the fact to carry: for several loops in this specialty the pattern is part of the signal, and a
readout that integrates the pattern away has thrown information out before you ever looked at it
(**consensus**). The calcium answer handles the loop that holds the field steady; this one is
about what the field does to the tissue.

Two further settings worth naming, both verified. The gain multipliers stack onto rate and not
onto balance: **Pokérus** doubles effort gain and a **Macho Brace** doubles it again, and neither
of them changes which direction the counter is going (**mechanism**). And `EV_ITEM_RAISE_LIMIT` is
100 while the per-counter cap is 255 — so a vitamin simply stops working a long way below the
ceiling, with nothing on the screen to say that it has (**mechanism**). A plateau, unannounced.

## What the fast counter cannot tell you

Five limits, and every one of them is in the code rather than in the quality of the reading.

**It has no direction.** 10/5/2 from the berry against 5/3/2 from the vitamin: the counter moved
further for the act that *emptied* the stock. Nothing about the number distinguishes them
(**mechanism**).

**It has no site.** `AdjustFriendship` is called for one Pokémon, not for one stat, and the same
increment arrives whichever of the six counters was touched (**mechanism**).

**Its response depends on where it already was.** The increment is chosen by band — one value
below 100, another below 200, a third above — so the identical act moves the counter by different
amounts at different starting points (**mechanism**). A change is not comparable with a change
measured from somewhere else on the scale.

**Things with nothing to do with the stock move it.** A **Luxury Ball** adds one to every positive
change. Standing in the region where the Pokémon was met adds another one. A **Soothe Bell**
multiplies a positive change by 150 and divides by 100, **rounding down** — so it does precisely
nothing when the increment is 1 (**mechanism**). Three modifiers, none of them about the stock,
and one of them invisible exactly when the signal is smallest.

**It is not the stat and it is not a prediction.** **Return** at 102 tells you the counter is at
its ceiling and tells you nothing whatever about the six counters that actually decide what the
Pokémon can do (**mechanism**).

One honest note, because this is the place the mapping diverges from the thing it is mapping.
Friendship is a **running total** — it accumulates and does not decay — whereas a real turnover
marker reports the *current rate* and falls when the rate falls. The five limits above hold for
both, and the directionlessness holds exactly. The accumulation does not: a turnover marker will
come back down, and the counter in the cartridge will not. The growth-hormone answer uses the same
counter for the job it genuinely fits, which is an integral, and says so there.

## And the slow reading has its own problems

`Cmd_weightdamagecalculation` is the one to look at, because it does the thing a projected
measurement does. **Low Kick**'s base power is set by walking `sWeightToDamageTable` against
`GetPokedexHeightWeight(...)` — the **Pokédex entry's figure for the species**, identical for
every individual of it (**mechanism**). The move is not measuring the Pokémon in front of it. It
is reading a reference table and calling the answer a property of the individual.

In later generations the recorded figure is modified before the move reads it, and the expansion's
own comment pins the order: **Autotomize** is applied first, then **Heavy Metal**, **Light Metal**
and a **Float Stone** (**mechanism**). So four things can change the number the move reads without
changing the thing being read — which is the whole problem with a reading taken through a
projection, and the reason a value is not interpretable without knowing which reference produced
it.

The other half of that problem is the comparison. **Shuckle**'s base 230 Defence and **Blissey**'s
base 255 HP are real outliers in a real distribution, and any statement of the form "this one is
*n* steps from the usual" is a statement about which distribution you chose (**mechanism**).
Change the reference set and the same Pokémon's standing changes without the Pokémon changing.
Which reference is used, and what is done at which point on it, is local (**country-dependent**).

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of a slow stock with a fast, directionless, summed marker sitting
over it; of deposit and removal being one process rather than two; and of a reading taken through
a projection against a chosen reference. The picture is fair. Nothing above stands in for a person
— the counters are counters.

Most bone loss produces no symptoms at all until a fracture, which means nearly everything done
about it is done on the strength of a number rather than on how someone feels. That puts real
weight on understanding what the number is. It is also why someone can be told their reading has
improved while they are no better off, and told it has not moved while treatment is doing exactly
what it is supposed to do.

The commonest harm here is not a drug side effect. It is a fracture in someone whose risk was
never assessed, often after an earlier fracture that was recorded as an injury and not read as
information. The second commonest is the mirror image: long-term treatment started on a single
reading that one of the measurement artefacts above had raised or lowered.

Body size interacts with the measurement for the same geometric reason the projection argument
above describes, and the relationship between body weight and fracture is site-dependent rather
than uniform. That is a property of a measurement and of mechanics, and it is worth saying as one
rather than as anything about a person's habits.

And a note about who is reading. Someone reading this may have had a density scan, or be taking
something for their bones. If that is you: nothing above is a threshold, a target, a duration or a
plan. What a reading means, whether treatment is working and how long it should go on are
judgements made against a whole picture by the team that holds it — not from an analogy about
hidden counters.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national or specialty-society guidance on the assessment and management of osteoporosis,
  for risk assessment, the thresholds applied to a density reading, treatment duration and review
  intervals. These differ substantially between countries.
* **Your laboratory's handbook**, for which turnover markers it offers, the sampling conditions
  they require, the platform in use and whether its values compare with anybody else's.
* Your radiology or nuclear medicine department's guidance, for the sites measured and the
  reference population used.
* Your national formulary, for anything about an antiresorptive or anabolic bone agent.
* A current textbook of bone biology or endocrinology, for the remodelling cycle and its phase
  durations, the ligand and decoy-receptor pair that couples the two cell populations, the
  remodelling-space argument, and the contrast between continuous and intermittent parathyroid
  hormone exposure.

The Pokémon side is different and is sourced properly. `MAX_PER_STAT_EVS` being 255,
`MAX_TOTAL_EVS` 510, `MAX_FRIENDSHIP` 255 and `EV_ITEM_RAISE_LIMIT` 100; the twelve vitamin and
berry effect entries with their `ITEM6_ADD_EV` and `ITEM6_SUBTRACT_EV` flags and the counter each
is addressed to; `VITAMIN_FRIENDSHIP_CHANGE` being 5/3/2 against `EV_BERRY_FRIENDSHIP_CHANGE`'s
10/5/2; the three friendship bands at 100 and 200; the **Soothe Bell**'s 150-over-100 with its
rounding down; the **Luxury Ball** and met-location increments; **Pokérus** and the **Macho
Brace** each doubling effort gain; the **Macho Brace** halving Speed before the paralysis
quartering in `GetWhoStrikesFirst`; **Stockpile**'s cap of 3, **Spit Up**'s multiply-and-reset and
**Swallow**'s `maxHP / (1 << (3 - counter))` with its full-HP waste; the **Protect** counter's
reset on `gLastResultingMoves`; **Return**'s friendship × 10 ÷ 25 ceiling of 102; **Low Kick**
reading `GetPokedexHeightWeight`; the weight-modifier ordering comment naming **Autotomize**
before **Heavy Metal**, **Light Metal** and a **Float Stone**; and **Shuckle**'s and **Blissey**'s
base stats were all read from the pokeemerald and pokeemerald-expansion decompilations rather than
from memory. One thing was checked and is **not** claimed, because it would have been wrong: the
bitter field medicines — **Energy Powder**, **Energy Root**, **Heal Powder** and a **Revival
Herb** — do **not** lower friendship in Generation III. There is no such event in
`sFriendshipEventModifiers`, whatever later generations do.

## Scope and safety

The Pokémon here is doing one job: making it concrete that a fast summed counter reports rate
rather than balance, that deposit and removal are one mechanic, and that a slow reading taken
through a projection against a chosen reference has limits of its own. It is not a clinical
reference, not a decision aid, and not about any individual's care. **No score thresholds, marker
reference intervals, least-significant-change figures, doses or treatment durations appear here on
purpose** — they differ between countries, institutions and assay platforms and are revised, and a
revision page is the wrong place to get them from. Check the formulary, your local guidance and
your laboratory's handbook. Nothing here has had clinical review.

## What a Gym Leader digs into next

* Why does a **Pomeg Berry** move the fast counter further than an **HP Up** does?
* Why does blocking the removal phase lower the deposit phase as well?
* Why does a **Macho Brace** make the measurement worse for exactly as long as it makes the stock
  grow faster?
* Why does the **Protect** counter mean that the same move used twice is not the same signal?
* Why is **Low Kick**'s power not a measurement of the Pokémon it hits?

## Where this stands, October 2026

The stock-against-marker structure, the one-field-two-accessors coupling, the pattern argument and
the projection argument are mechanism and do not date. What dates on the Pokémon side is the
constants and the implementation: the 510 total cap is a Generation III introduction, the vitamin
limit of 100 was lifted in later generations, friendship was reworked and partly renamed from
Generation VIII, **Stockpile** gained stat boosts from Generation IV, the **Protect** chain's
failure arithmetic has been revised more than once, and **Heavy Metal**, **Light Metal**, a
**Float Stone** and **Autotomize** are all post-Generation-III. Check the current generation's
data. On the clinical side everything procedural and numeric moves — recommended markers and their
sampling conditions, reference populations, thresholds, risk calculators and treatment durations —
so check current local guidance and your laboratory's handbook.
