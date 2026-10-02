---
id: "m056"
slug: thyroid-axis-and-its-counterintuitive-tests
style: pokemon
category: endocrinology
difficulty: advanced
question: "Why does the three-level thyroid feedback loop make its tests counterintuitive, and what is the pituitary's output actually reporting?"
tags: [thyroid, tsh, feedback, hypothyroidism, thyrotoxicosis]
---

# You do not read the terrain. You read how hard Flail is hitting, and Flail counts the wrong way up.

A field condition is a hormone — that is the house mapping, and this answer works a different
layer of the field from the diabetes answers. **Grassy Terrain** is the condition here: set by
**Tapu Bulu**'s **Grassy Surge** the instant it enters, it gives every **grounded** Pokémon a
sixteenth of its maximum HP back at the end of every turn, runs for five turns, and runs for eight
instead if the setter was holding a **Terrain Extender** *(mechanism)*. Ambient, acting on
everything that can feel it, decaying on a clock. That is the supply.

Now the readout. You do not get to see the terrain's remaining turns, and the bar animates toward
a number rather than showing it. What you get is **Flail**, whose base power is read off the
user's own remaining HP in six bands — and it counts **upward as the bar goes down**
*(mechanism)*. The reporter is not reporting how much condition there is. It is reporting how
badly the reporter is doing without it.

| In the battle | What it stands for |
| --- | --- |
| **Grassy Terrain**, a sixteenth a turn to everything grounded | Circulating free thyroid hormone |
| **Tapu Bulu**'s **Grassy Surge**, firing on entry | The thyroid: the only thing that can set it |
| **Terrain Extender**, eight turns instead of five | A reservoir with a long half-life |
| **Flail**'s base power — six bands, 20 up to 200 | The reporter: inverse, amplified, banded |
| **Helping Hand**, an ally's ×1.5 that does nothing itself | The level above: permissive, gain-setting |
| Grounded, or not: a Flying type, **Flygon**'s **Levitate**, an **Air Balloon** | Tissue with and without the receptor |
| **Gravity**, an **Iron Ball**, **Ingrain** | What forces an unreached tissue to feel it |
| **Reflect**, halving what lands without changing what was sent | Binding protein: total against free |
| The damage roll, 85–100% of the calculated figure | Assay noise: one reading does not pin a band |
| **Disable**, four turns on the last move used | The reporter itself is the broken part |

Claims are marked *(mechanism)*, *(definitional)*, *(consensus)* or *(country-dependent)* where it
matters.

## Three levels, and what each one does

```
   LEVEL 3   the ally using HELPING HAND
                 │                 ×1.5 on the next move. It sets no terrain
                 │                 and heals nobody. It decides how loudly
                 │                 level 2 gets to speak.
                 ▼
   LEVEL 2   the FLAIL user        base power 20 · 40 · 80 · 100 · 150 · 200
                 │                 THE REPORTER. Reads its OWN bar, in 48ths,
                 │                 and counts upward as that bar falls
                 ▼
   LEVEL 1   TAPU BULU, Grassy Surge on entry
                 │
                 ▼
   THE FIELD     Grassy Terrain · five turns, or eight with a Terrain Extender
                 │
                 ▼
   WHO FEELS IT  grounded only. Flygon NEVER feels it. An Air Balloon holder
                 │              never feels it until the balloon is popped.
                 │
                 └──── and the terrain is what holds the reporter's bar up ───┐
                                                                              │
        ◄─────────────────────────────────────────────────────────────────────┘

   You read LEVEL 2. What you care about happens at WHO FEELS IT.
   Three things sit in between, and every one of them can make the read lie.
```

**Helping Hand** earns its place at the top. It has 0 base power, 0 accuracy, and boosts an ally's
move by half *(mechanism)*. It accomplishes nothing on its own and changes everything about what
the level below it manages. That is why this is a three-level structure and not a two-level one:
the gain is adjustable from above, so "the right amount" is a setting rather than a constant.

## Counterintuition one: the number counts the wrong way up

**Flail at 200 means the bar is nearly empty.** It does not mean the user is strong. Every reader
of a damage readout wants a big number to mean a lot of something, and here the big number means
there is almost nothing left. The reporter is not reporting supply. It is reporting
**dissatisfaction**, and dissatisfaction is loudest when supply is worst.

## Counterintuition two: the bands are not evenly spaced, and the floor is blind

Here is the actual table from the Generation III decompilation, which computes the user's HP as a
fraction of 48 and walks a list *(mechanism)*:

```
   HP, in 48ths     ≤1    ≤4    ≤9    ≤16   ≤32   else
   base power       200   150   100   80    40    20
                    └── steep, down here ──┘   └ flat across the top third ┘
```

Two things fall out of that shape. The reporter is **sensitive near the bottom**: between 4/48 and
1/48 of the bar it jumps from 150 to 200, so a sliver of change moves it a long way. And the
reporter is **blind across the top**: a full bar and a two-thirds bar both give base power 20
*(mechanism)*. A floor is a floor. Once Flail is sitting at 20 you cannot tell how far past 20 the
situation is, because there is no number below it — which is exactly why you stop asking the
reporter and go and look at the terrain itself.

One honest note, because it is the place this analogy understates reality: the real reporter's
sensitivity sits in the **opposite** corner. It resolves deficits so small that the bar would
barely have moved. Flail is flat where the real thing is sharpest. The shape is right; the
asymmetry points the other way, and the serious answer says so.

## Counterintuition three: the condition outlives its setter, so the reporter lags

Terrain does not stop when **Tapu Bulu** leaves. It runs its five turns — eight with a **Terrain
Extender** — and then lapses, and nothing about the field announces which turn you are on
*(mechanism)*. So the reporter's bar is being held up by something whose source left several turns
ago, and Flail's band is reporting a stretch of the battle that is already over.

Check again immediately after anything changes and you mostly re-measure the turns you have
already measured *(consensus)*. How many turns to let run before you look again is a matter for
local guidance *(country-dependent)*.

## Counterintuition four: the reporter is void when the reporter is what broke

**Disable** shuts off the last move used for four turns from Generation V, four to seven in
Generation IV, and two to five before that *(mechanism)*. Disable the Flail user's Flail and you
get no reading at all, while the bar sits exactly where it was. Worse than that: the *absence* of
a big number reads as reassurance. Nothing is complaining, so nothing must be wrong.

This is why you look at the field as well as the reporter whenever the reporter might itself be
the casualty — and it is why the one really dangerous pattern is a **quiet reporter over a bare
field**. No Flail, no terrain. The loop is open and the readout says everything is fine.

The mirror image is rarer and is the reason the rule is stated as a **pair**: a big Flail and a
terrain that is clearly up at the same time is not a pattern the simple rule can explain, and it
sends you looking at the reporter rather than at the setter *(consensus)*.

## Counterintuition five: what was sent is not what lands

**Reflect** halves incoming physical damage for five turns, eight while the setter holds **Light
Clay**, and it changes nothing whatsoever about the attacker *(mechanism)*. Flail at 200 into
Reflect lands like Flail at 100. If you are grading the attacker by what the defender felt,
Reflect has made you wrong about the attacker — and nothing in the attacker changed.

That is the whole of total-against-free, and it is why the field is read for the **free** quantity
rather than the gross one. The same trap in a smaller size is the damage roll: every hit lands for
85–100% of the calculated figure *(mechanism)*, so a single observed number does not pin a band,
and a **Critical Hit** will hand you a figure that belongs to no band at all.

## Who actually feels it, which is not everybody

Terrain reaches **grounded** battlers only. A Flying type is out of reach, **Flygon** is out of
reach because **Levitate** is its only ability, an **Air Balloon** holder is out of reach until
the balloon pops, and **Claydol** and **Lunatone** are out of reach too *(mechanism)*. None of
them takes the sixteenth a turn and none of them is any part of what the reporter is reporting.

Then **Gravity** lands, or the Pokémon is holding an **Iron Ball**, or **Ingrain** has rooted it —
and now it is grounded, and now the terrain reaches it *(mechanism)*. The condition did not
change. Who could feel it did.

That is the layer the reporter cannot see at all. One field-wide number, and six Pokémon with six
different relationships to it.

## The pattern table, which is the actual skill

| Flail | The terrain | Where the fault is |
| --- | --- | --- |
| 200 | Not up | The setter — nothing can produce the condition |
| 150 | Up, visibly | Discordance: the reporter complains, the field looks fine |
| 20 | Up and plainly over-long | The condition is excessive, from somewhere |
| 20 | Not up | Discordance the other way, and the quiet one |
| 20 | Not up, and Flail is **Disabled** | The reporter is the casualty. The dangerous read |
| 200 | Up | No simple rule covers it. Go and look at the reporter |

Read as a table it looks like memorisation. It is one question: **is Flail as loud as the field
says it should be?** That question is the whole of this specialty, and it comes back unchanged for
the other three field layers and their own setters.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of a three-level control loop read through its controller's output.
The loop is a fair picture. What the readings mean for a person is not a battle.

Three things matter to people rather than to examiners. "Subclinical" is a word about a pair of
numbers being discordant — nothing more *(definitional)* — and a great many people have heard it
as "your symptoms are not real". Those are unrelated claims. Whether a discordant pair is treated
is genuinely contested, differs between guideline bodies, varies with age and with pregnancy, and
is a judgement made with a person rather than read off a table.

Hypothyroidism is one of the commonest conditions managed by lifelong replacement, and people
living with it frequently report symptoms persisting after their numbers normalise. The loop drawn
above does not explain that. The honest position is that the explanation is incomplete, not that
the report is wrong.

And a note about who is reading. Thyroid disease is common, so someone reading this is more likely
to be living with it than revising it. If that is you: nothing above is about your results. A
reference interval belongs to the laboratory that issued it and the interpretation belongs to the
team that ordered the test. Neither is something to re-derive from an analogy about terrain.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national thyroid guideline from the body that issues it — in the United Kingdom the
  National Institute for Health and Care Excellence, elsewhere the equivalent national authority —
  for testing strategy and for subclinical disease.
* The guidance your national or regional association of clinical biochemistry publishes on thyroid
  function testing, which is where testing-strategy reasoning is set out most explicitly.
* **Your own laboratory's handbook**, for the assay platform, the reference intervals it issues,
  its pregnancy-specific interpretation and the interferences it is susceptible to.
* A current endocrinology textbook, for the reporter relationship, deiodinase biology, receptor
  isoform distribution and the half-life of the circulating hormone.

The Pokémon side is different and is sourced properly. **Flail**'s six-band power table, the
terrain duration of five turns and eight with a **Terrain Extender**, the grounded-only rule and
its exemptions, **Grassy Terrain**'s sixteenth a turn, **Helping Hand**'s ×1.5, **Reflect** with
**Light Clay**, **Disable**'s per-generation durations and **Grassy Surge** on **Tapu Bulu** were
all read from the pokeemerald and pokeemerald-expansion decompilations rather than from memory.
Generation-dependent figures are pinned to their generation above.

## Scope and safety

The Pokémon here is doing one job: making a three-level control loop and its inverted, amplified,
lagging readout concrete. It is not a clinical reference, not a decision aid, and not about any
individual's care. **No reference intervals, thresholds, doses or re-testing intervals appear here
on purpose** — they differ between laboratories, countries and guideline bodies, they are revised,
and the units differ too. Your laboratory and your local guidance are the authority and this page
is not. Nothing here has had clinical review. The metaphor covers mechanism and stops there: what
either direction of thyroid disease is like to live with is not material for a battle analogy, and
it is addressed plainly above. If someone is unwell now, contact local emergency services.

## What a Gym Leader digs into next

* Why do you read the Flail user rather than count the terrain's turns?
* Why can a full bar and a two-thirds bar both give base power 20, and what does that cost you?
* Why is a quiet reporter over a bare field the read that should worry you most?
* Why does **Reflect** make you wrong about the attacker without changing the attacker?

## Where this stands, October 2026

The loop, the inverted reporter and the lag are mechanism and do not date. What dates on the
Pokémon side is the cast and the constants: terrains arrived in Generation VI, **Grassy Surge**
and the other Surge abilities in Generation VII, and **Rillaboom**, **Pincurchin** and
**Indeedee** carry theirs as **Hidden Abilities** rather than as their standard one. **Disable**'s
duration has changed three times. Check the current generation's data. On the clinical side,
everything numeric and everything contested is what moves — reference intervals, re-testing
intervals, treatment thresholds for subclinical disease, and the place of combination therapy — so
check current local guidance and your own laboratory's handbook.
