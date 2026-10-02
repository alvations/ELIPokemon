---
id: "m023"
slug: glycation-marker-and-continuous-monitoring
style: pokemon
category: endocrinology
difficulty: intermediate
question: "What does glycated haemoglobin measure that a spot glucose cannot, and where does it mislead?"
tags: [hba1c, monitoring, continuous-glucose, variability, red-cell-turnover]
---

# Return's base power is the whole history. The HP bar is what is happening now. Neither is the other.

Friendship is a number from 0 to 255 that the games never show you. It rises a little with almost
everything you do and falls when things go badly, and because nothing resets it in ordinary play
it ends up carrying a record nobody had to write down *(mechanism)*. You read it through proxies.
The move **Return** has a base power of friendship multiplied by ten and divided by twenty-five,
so it tops out at 102 — the attack *is* the stored value, expressed as damage. And the friendship
checker reports it as one of six bands rather than as a number. That is an integral, and a spot
reading cannot be one, because a single glance at a value that swings all day tells you almost
nothing about its average. The integral equally cannot tell you what is happening this turn.

| In the battle | What it stands for |
| --- | --- |
| Friendship, 0–255, stored and never displayed | The long-term glycation marker's substrate |
| **Return**'s base power — friendship × 10 ÷ 25, max 102 | The reported value: a proxy for the stored one |
| The checker's six bands | A continuous quantity read out as categories |
| Band-dependent gains: +5, then +3, then +2 | A marker that moves less the higher it already is |
| **Luxury Ball** and met-location bonuses | Interference: things that move the number, not the truth |
| Trading, which sets friendship to a flat 70 | The record's carrier replaced wholesale |
| The HP bar: 48 pixels, green / yellow / red | The continuous trace, with its bands |
| **Battle Video** in the **Vs. Recorder** | Retrospective review of the whole run |

Claims are marked *(mechanism)*, *(consensus)* or *(guideline-dependent)* where it matters.

## Why the integral is weighted, and what the weighting costs

The counter is not a flat tally, and this is the part people miss. How much a single event moves
it depends on where it already sits: a level-up adds 5 while friendship is below 100, 3 from 100
to 199, and only 2 at 200 and above, and a **Protein**, an **Iron**, a **Calcium**, a **Zinc**, a
**Carbos** or an **HP Up** moves it on exactly the same sliding scale *(mechanism)*. A **Pomeg
Berry** is steeper still — 10, then 5, then 2. A bad faint goes the other way and gets *worse* as
the counter rises: 5 in the lower bands, 10 in the top one. So the weight a recent event carries
is set by the state recent history put the counter in, which is precisely what it means for an
integral to be weighted toward its recent end *(mechanism)*.

The practical consequence is that the number moves, but slowly, and it lags any genuine change in
how a Pokémon is being handled. Checking it again too soon mostly re-measures the stretch you have
already measured *(consensus)*; how soon counts as too soon is a matter for local guidance
*(guideline-dependent)*.

```
   WHAT EACH ONE SEES
   ──────────────────
   the real HP        ╭─╮      ╭──╮          ╭─╮        ╭──╮
   through the run   ─╯ ╰─╮  ╭─╯  ╰╮   ╭────╯ ╰─╮   ╭──╯  ╰──
                          ╰──╯     ╰───╯        ╰───╯
                       ▲        ▲                        ▲
   three glances       │        │                        │   three numbers,
                       ●        ●                        ●   three conclusions

   Return's power     ════════════════════════════════════   one figure for the
                      weighted to the recent end            whole stretch

   the HP bar         ∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿∿   shape, rate, direction
                      ░░ in the red ░░      ░░ in the red ░░


   THE FAILURE THE INTEGRAL CANNOT SEE
   ───────────────────────────────────
   Pokémon A    ─────────────────────────────────   steady, bar stayed green
   Pokémon B    ╱╲    ╱╲      ╱╲    ╱╲    ╱╲        swung all run, and sat in
                ╲╱▂▂▂▂╲╱▂▂▂▂▂▂╲╱▂▂▂▂╲╱▂▂▂▂╲╱▂▂▂    the red in every trough
                ╰─────── identical Return power ──────╯
```

## What it misses

**The swings, and so the time in the red.** The counter is a summary, and a summary is blind to
the distribution underneath it. A steady run and a violent one can land on the same figure, and
the violent one contains every trough the figure averaged away *(mechanism)*. This is the
limitation that matters most, because the harm from a trough is immediate while the reassuring
figure is smoothing it out.

**Pattern and timing.** Which turns the bar fell on, whether it drifts while nothing is happening,
whether one specific hit does it — all invisible in a single figure. The useful question is almost
always *when* and *why*, and an integral answers neither.

**The last few turns.** By construction the figure is weighted but slow, so a change made recently
is largely not in it yet *(mechanism)*.

## Where it misleads

Everything above assumes the counter is behaving. It is a property of a specific Pokémon's stored
data, so anything that changes that data without changing how the Pokémon has actually been
handled changes the figure *(mechanism)*.

* **The carrier gets replaced.** Trade a Pokémon and its friendship is set to a flat 70, whatever
  its entire history was *(mechanism)*. The record is no longer a record of anything that happened
  to this Pokémon. Nothing about its handling changed; the number did.
* **The starting point is not universal.** Most species begin at 70, **Chansey** and **Blissey**
  begin at 140, and **Tyranitar** begins at 35 — forty-three species start at 35 in Generation III
  alone *(mechanism)*. The same figure therefore means different things depending on what is
  holding it, and comparing two species' numbers directly is a mistake *(consensus)*.
* **Things that move the number and not the truth.** A Pokémon caught in a **Luxury Ball** gains
  an extra point on every positive event, as does one met in the region you are currently standing
  in, and a **Soothe Bell** multiplies the gains by half again while leaving every loss untouched
  *(mechanism)*. Three facts about circumstance, none about handling, all of them in the figure. A
  **Rare Candy** is worse: it buys a level outright, and the level-up pays its friendship as if
  the Pokémon had earned it. And a **Kelpsy Berry**, a **Qualot Berry**, a **Hondew Berry**, a
  **Grepa Berry** or a **Tamato Berry** raises the counter while *taking* **Effort Values** away —
  items whose whole purpose is subtraction, pushing the record up *(mechanism)*.
* **The readout and the stored value can come apart.** **Hyper Training** with a **Bottle Cap**
  raises the stat a Pokémon actually fights with while leaving the stored **Individual Values**
  exactly as they were, so the judge's verdict and the battle performance stop agreeing
  *(mechanism)*. Which of the two you are looking at is the whole question, and the answer depends
  on which tool you used *(guideline-dependent)*.
* **The bands are coarse where it matters.** The checker collapses 255 values into six phrases, so
  a Pokémon near the edge of a band and one near its other edge report identically *(mechanism)*.

There is a quieter issue too. Two Pokémon handled identically do not always end up on the same
figure, by more than the bookkeeping explains, and the reasons are argued about rather than
settled *(consensus, with genuine disagreement)*. Treat one reading near a decision point as a
measurement with a spread, not as a fact.

## The decisions taken on it are thresholds, and the threshold is not a property of the counter

The games draw one hard line across this hidden number, at 220, and crossing it is irreversible.
**Golbat** becomes **Crobat**. **Chansey** becomes **Blissey**. **Pichu**, **Cleffa**,
**Igglybuff**, **Togepi** and **Azurill** all level into something else. And **Eevee** crosses the
same line into **Espeon** by day and **Umbreon** by night — *identical counter, identical
threshold, different outcome, because the context differed* *(mechanism)*.

Three things follow and they are routinely run together. The **position** of the line is a
decision somebody made, not a fact about the counter — in the clinic the value of each diagnostic
and treatment line is a consensus choice that differs between guideline bodies and is revised
*(guideline-dependent)*. The **reading** of the same number is contextual, exactly as 220 is at
dusk: the same measurement is weighed differently in a young person with decades of exposure
ahead, in frailty, in advanced kidney disease, and in pregnancy, where separate criteria and
separate measurements apply *(consensus)*. And the **figure itself** carries a spread, so landing
on the line is not evidence of being on it. None of that is in the molecule. It is in the
agreements attached to it, which is why the threshold gets looked up rather than remembered.

## Why the bar changed the questions

The HP bar is continuous. It is drawn in forty-eight pixels and redrawn constantly, and it is
coloured in bands: green above half, yellow between a fifth and a half, red at a fifth or below
*(mechanism)*. The convenience of not having to ask is the least interesting part of it. What
changed is that a continuous display makes previously unanswerable questions answerable: how much
of the run the bar spent green, how much of it in the red, how violently it moved — and, uniquely,
**which way it is going right now** *(consensus)*. A rate is information no single glance
contains, and it is what lets you act before the problem arrives instead of after it
*(mechanism)*.

The consequences go further than the battle. Troughs nobody was watching for became visible.
Swings became a quantity instead of an impression. And review stopped being one figure discussed
afterwards and became a shape discussed with whoever was holding the controller.

The limitations follow from the same mechanics. The bar is **animated** toward the stored value
over several frames, so it trails the real number and trails it worst exactly when the real number
is moving fastest *(mechanism)*. It is quantised to forty-eight pixels, so small moves do not
show. For the opponent's Pokémon you get the bar and never the number at all, so what you can
measure depends on whose Pokémon it is. And the low-HP alarm, which starts in the red band and
does not stop, is the original case of an alert that people learn to ignore. Published agreements
exist about which summary figures to use and what counts as good; they differ by document and
population, local guidance is the authority, and **no target values appear here**
*(guideline-dependent)*.

Used together the division of labour is clean. **Return**'s power for the long view. The bar for
the shape and the direction. The **Battle Video** in the **Vs. Recorder** for going back over the
whole thing turn by turn, which is where most of the value actually lands. And the real stored
number whenever the tool you are using says you need it.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

A hidden counter read through a proxy is a fair picture of the measurement. It is not a fair
picture of what the measurement is used for. A single glycation value has become, in a great many
consultations, a proxy for whether someone has been good — and that is a misuse of a number
carrying a confidence interval, an interference profile and a dependence on red-cell biology that
has nothing to do with anybody's effort. The same misuse runs the other way and is more dangerous:
a value that looks reassuring can be the average of a trace that goes dangerously low every night.
Those lows are hypoglycaemia, the harm from them is immediate, and the number that averaged them
away is not a reason for reassurance.

The continuous trace has the same double edge. It makes self-management visible, which helps, and
it makes it surveillable, which can be used to judge. A trace shown in a consultation is a record
of somebody's nights, meals, illnesses, shifts and mistakes. It should be read as information
about a condition and not as evidence about a person, and the reason for saying so is that it
frequently is not.

A note about who is reading. Someone reading about glucose monitoring is more likely to be living
with it than revising it. If that is you: there are deliberately no target values anywhere on this
page, because the published ones are population agreements that differ between documents, and what
applies to you is set with your own clinical team. A reading that worries you is a reason to
contact them, not a reason to act on anything in an analogy about a hidden counter.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md).
Specific to this answer:

* Your national diabetes guideline's sections on monitoring and on glycaemic targets, from the
  body that issues it, which is the authority on any target value and on measurement frequency.
* The American Diabetes Association's annual standards of care document, for its chapter on
  glycaemic assessment and monitoring technology.
* The consensus statements of the Advanced Technologies and Treatments for Diabetes meetings, for
  the agreed continuous-glucose metrics and their definitions.
* The International Federation of Clinical Chemistry's reference material on standardising the
  glycated haemoglobin measurement, and the question of which reporting units your laboratory
  uses.
* Your own laboratory's handbook: which assay method it runs, which haemoglobin variants that
  method is affected by, and what it says about results in kidney disease.
* The manufacturer's instructions for the specific continuous sensor in use, for its accuracy
  claims, interfering substances and confirmatory-testing requirements.

## Scope and safety

The Pokémon is doing one job here: showing what an integrated hidden counter can and cannot tell
you next to a continuous display. It is not a monitoring protocol and not about any individual's
care. **No clinical thresholds, target ranges or reporting values appear here** — the real ones
differ between guidelines, between reporting units and between populations, and they are revised,
so local guidance and the laboratory handbook are the authorities. Every number on this page is a
quantity in a video game and converts to nothing. Nothing here has had clinical review. Where the
trace shows a trough, the consequence is hypoglycaemia, which is described plainly in the rigorous
answer and is not material for a battle analogy. If someone is unwell now, contact local emergency
services.

## What a Gym Leader digs into next

* Why does the same event move friendship by different amounts at different points?
* What does trading do to the record, and why does it not matter how the Pokémon was handled
  before?
* What can a rate of change tell you that no single glance can?

## Where this stands, October 2026

The structure — a hidden counter, integrated over time, read through a coarse proxy — is mechanism
and does not date. The cast does: band boundaries, which bonuses apply, the existence of **Hyper
Training** at all and the exact arithmetic behind **Return** have all shifted across generations,
so check the current generation's data. On the clinical side the reporting units, assay
interference profiles, agreed continuous-monitoring metrics and every target attached to them are
current agreements and they move. Read the document, not a remembered figure.
