---
id: "m094"
slug: the-growth-hormone-axis-as-a-pulse-train
style: pokemon
category: endocrinology
difficulty: advanced
question: "Growth hormone is secreted in bursts, so a single measurement of it is uninterpretable. How is a pulsatile system measured instead?"
tags: [growth-hormone, igf-1, pulsatility, acromegaly, dynamic-testing]
---

# Shoal Cave has an inner room for twelve hours a day, and walking in at the wrong hour proves nothing about the cave

There is a 24-entry table in the Generation III source called `tide`, one byte per hour of the
clock, and it decides whether **Shoal Cave**'s inner rooms are there at all:

```
   hour   00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23
   tide    1  1  1  0  0  0  0  0  0  1  1  1  1  1  1  0  0  0  0  0  0  1  1  1
                    └───── low ────┘                    └───── low ────┘
```

`UpdateShoalTideFlag` reads the real-time clock, indexes that table, and sets or clears
`FLAG_SYS_SHOAL_TIDE`; the map script then swaps the layout to the high-tide or low-tide version
*(mechanism)*. Walk in at nine in the morning and the ice room is not there, and neither is the
**Snorunt** that is the only thing in it — the encounter table for that room lists **Snorunt**,
**Spheal**, **Zubat** and **Golbat**, and at the wrong hour you cannot meet any of them because
the room does not exist. Walk in at four in the afternoon and it does. Nothing about the cave
changed. **The sample was a statement about the hour.**

That is the whole of this answer. The quantity you want is on a clock you do not control, it is at
the floor for most of the day, and a single reading is a true measurement of a moment and no kind
of measurement of the system.

And the detail that turns it from a nice picture into the right one: `UpdateShoalTideFlag` only
runs its check `if (IsMapTypeOutdoors(GetLastUsedWarpMapType()))` *(mechanism)*. Arrive by any
other route and the flag is **not refreshed** — you are reading a stale value from whenever it was
last set, with nothing on the screen to say so.

| In the battle | What it stands for |
| --- | --- |
| The 24-byte `tide` table | The hormone's own clock, which you do not set |
| **Shoal Cave**'s inner rooms, present or absent | A pulse, present or absent at this instant |
| The **Snorunt** you can only meet in the ice room | What a sample at the right hour finds |
| **Flail**'s band, which is now, against **Return**'s, which is the run | The instant against the integral |
| A single visit at a single hour | A single random measurement of a pulse train |
| The tide flag refreshed only from outdoors | A stale reading that does not say it is stale |
| **Eevee** → **Espeon** by day, **Umbreon** at night | One stored value, two readings, decided by the clock |
| Friendship, 0–255, stored and never shown | The integral |
| **Return**'s base power, friendship × 10 ÷ 25, max 102 | The integral read out — and its ceiling |
| **Frustration**, 10 × (255 − friendship) ÷ 25 | The same integral, read the other way up |
| The friendship bands at 100 and 200 | A response that depends on where it already was |
| A **Soothe Bell**'s ×150÷100, **rounding down** | A modifier that does nothing at low signal |
| A **Luxury Ball**, and the met-location bonus | Confounders with nothing to do with the signal |
| `ShouldSkipFriendshipChange` in three named places | A setting where the integral stops accumulating |
| **Helping Hand** from the ally, ×1.5, 0 power, 0 accuracy | The accelerator at the level above |
| **Imprison**, tonic while its user is present | The brake at the level above |
| **Arbok**'s **Intimidate** against **Metagross**'s **Clear Body** | The suppression test |
| `CalculateMonStats` overwriting, keeping no history | No stored baseline, which is the whole problem |
| **Castform**'s **Forecast** reading weather and never terrain | Two layers the code keeps apart |
| No terrain left: **Grassy**, **Psychic**, **Misty**, **Electric** all taken | A vocabulary limit, said out loud |

**This answer defers to three others.** m023 owns **Return** as the integral. m058 owns
**Intimidate** against **Clear Body** as the suppression test and **Eevee**'s two evolutions as
the clock. m060 owns the **Protect** counter. All three appear here; none is re-argued.

Claims are marked *(mechanism)*, *(definitional)*, *(consensus)* or *(country-dependent)* where it
matters.

## The pulse train, and where a single sample lands

```
   THE LEVEL ABOVE, and it has TWO signals, not one

   the ally's HELPING HAND ──┐   ×1.5 on the next move. 0 base power,
                             │   0 accuracy, heals nobody, sets nothing.
                             │   Pure accelerator.
                             │
   the ally's IMPRISON ──────┤   seals a shared move for as long as its
                             │   user stays on the field. Pure brake, and
                             │   in Generation III it FAILS unless the two
                             │   sides share a move at all.
                             ▼
   WHAT COMES OUT      ▲        ▲      ▲
                       █        █      █        ▲   ▲▲       bursts, not a level
                  ▲    █    ▲   █      █   ▲    █   ██
                 ─┴────┴────┴───┴──────┴───┴────┴───┴┴────── floor
                   │  │        │                  │
                   ▼  ▼        ▼                  ▼
                  low high    low                high
            four true readings, one day, one Pokémon, no information

                             │
                             ▼
   THE SLOW PRODUCT    friendship, 0-255, accumulating, never displayed
                             │
                             ▼
   THE READOUT         Return, base power 10 × friendship ÷ 25, ceiling 102
                             │
              ◄── and the levels above read the product, not the bursts ──┘
```

An accelerator and a brake at the same level is the unusual part, and the games make the asymmetry
legible. **Helping Hand** has 0 base power and 0 accuracy and accomplishes nothing by itself; it
only changes how loudly the level below gets to speak *(mechanism)*. **Imprison** is the mirror
image, and the pituitary answer works through its Generation III failure condition: the brake only
exists because the two sides share a move. Two signals, opposite signs, one output, and the output
is a **train** rather than a level because that is what an accelerator and a brake produce when
both are live.

## The integral, and what it is actually integrating

Friendship is the established mapping for this in the specialty — the glycation answer set it and
the cortisol answer reused it — and it is the right one. A stored counter from 0 to 255 that
nothing displays, moving on every event with a name, read out through **Return**, whose base power
the Generation III source computes as `10 * friendship / 25` *(mechanism)*. At `MAX_FRIENDSHIP`
that is 102 and no higher. **Frustration** runs the same arithmetic on `MAX_FRIENDSHIP -
friendship`, so the pair are one quantity read from both ends.

Four limits, all of them in the code.

**It has a ceiling.** **Return** tops out at 102, so above the point where friendship reaches 255
the readout stops distinguishing *(mechanism)*. A reading at the ceiling establishes that the
exposure is at the top of the scale; it does not grade how far past the top it is. That is the
saturation problem exactly.

**Its increments depend on where it already was.** The modifier table gives one value below 100,
another below 200 and a third above — so the same act moves the integral by different amounts at
different starting points *(mechanism)*.

**Modifiers that have nothing to do with the signal move it.** A **Luxury Ball** adds one to every
positive change. Standing in the region where the Pokémon was met adds another. A **Soothe Bell**
multiplies a positive change by 150 and divides by 100 with integer truncation, so it does
**precisely nothing** when the increment is 1 *(mechanism)*. The amplifier is invisible exactly
where the signal is smallest, which is the least convenient place for an amplifier to be
invisible.

**There are places where it simply stops accumulating.** `ShouldSkipFriendshipChange` returns true
inside the **Battle Frontier**, and outside battle inside the **Battle Pike** and the **Battle
Pyramid** — friendship does not move at all in those three, and nothing announces it
*(mechanism)*. An integral that has quietly stopped integrating reads like an integral that has
found nothing to integrate.

Set the two readouts side by side and the choice is stark. **Flail**'s base power is read off the
user's own bar at this instant, in 48ths, through a six-entry table *(mechanism)* — it is as
current as a reading can be and it is a statement about one moment. **Return**'s base power is
read off a counter that has been accumulating since the Pokémon was caught, and it is a statement
about the whole run with no moment in it anywhere. The thyroid answer reads the field through
**Flail** because a thyroid hormone sits at a level. This axis does not sit at a level, so
**Flail** has nothing to report and **Return** is the only readout left.

And the deepest limit, which the games state for me rather than against me: the integral has
**averaged the pattern away**. The bone answer's **Protect** counter is the proof that the pattern
is part of the signal — same move, opposite outcome, decided by the spacing — and the friendship
counter has no field for spacing at all. It stores a total. Whatever the shape of the exposure
was, the total is the same number.

**And one stored value can give two readings, if the clock gets a vote.** **Eevee** carries
`EVO_FRIENDSHIP_DAY` to **Espeon** and `EVO_FRIENDSHIP_NIGHT` to **Umbreon** in the Generation III
evolution data — one entry each, same friendship requirement, different outcome *(mechanism)*.
Identical stored value. Two results. The clock decided, and the clock is not in the Pokémon.

The cortisol answer uses this for "a number without the clock is not a reading". Here it does the
complementary job: it is the reason the **integral** is the thing you read and the instantaneous
value is not. The stored counter does not care what hour it is. The readout of an instant does
nothing but.

## Pushing both ways, which is one sentence

Unchanged from every other answer in this specialty: **push the loop in the direction it should
resist.**

**Too little is tested by provoking a burst.** Supply the condition from outside, or send the
setter in deliberately, and watch whether anything happens — the finding is the *response*, not
any value *(consensus)*. Which provocation, how, under what supervision and what counts as a
response differ by country and by laboratory, some are not available everywhere, and none of it is
here *(country-dependent)*.

**Too much is tested by suppressing.** Send in **Arbok** and its **Intimidate** lowers every
opposing battler's Attack by one stage on entry. If the stage drops, the stat was being held in
the ordinary way and it obeys. If **Metagross** is out with **Clear Body**, or **Torkoal** with
**White Smoke**, nothing moves at all *(mechanism)*. You never measured anything. You pushed, and
the answer was in whether it gave.

That is the cortisol answer's device, reused deliberately and without modification, and the fact
that two independent axes land on the same test is the point: **the shape belongs to the problem,
not to the convention.** In a train of bursts you cannot show too much from one tall burst,
because tall bursts are what the system does. What you can show is that the **off state has
gone**.

## The slow version, and why there is no stored baseline

`CalculateMonStats` reads the old maximum only to work out a delta, writes the new value over it,
and keeps **no record of the trajectory anywhere** *(mechanism)*. The game shows you a stat. It
has never shown you the stat you had a hundred levels ago, and there is nothing in the save data
to go and look at.

That is the actual difficulty with a slowly accumulating change, and the games model it exactly:
not that the change is subtle, but that **the comparator does not exist**. Which is why the useful
history in the real version is always indirect — something that used to fit and no longer does, or
a photograph from a decade ago.

## The mapping I am declining, and where the games give me nothing

Two refusals, both deliberate.

**A low-level Pokémon is not a short child, and I am not going to write it that way.** Level is
the obvious mapping and it would have scored perfectly well. It requires a creature to stand in
for a person whose growth is the subject, which the specialty's conventions rule out for good
reason, and the serious half says in its opening that a child's growth is a different subject with
its own methods. The subject here is a pulse train and its integral. **Rare Candy** appears
nowhere in this answer and that is not an oversight.

**And the games keep two layers apart that the real system does not.** Weather is the
glucose-control hormones in this specialty and terrain is the axis hormones. **Castform**'s
**Forecast** is where you can read the separation straight out of the code: the expansion handles
it under a weather form-change, calling `GetWeather()`, and there is **no terrain branch in it at
all** *(mechanism)*. Set **Grassy Terrain** under a **Castform** and nothing whatever happens to
it. The real axis hormone antagonises insulin action directly, so the two layers genuinely
interfere. I have no mechanic for that and I am not inventing one: it is in the plain prose below.

A third refusal, and it is an inventory problem rather than a taste one. The four terrains are
spoken for — **Grassy Terrain** is thyroid hormone, **Psychic Terrain** cortisol, **Misty
Terrain** calcium and **Electric Terrain** the reproductive clock, set in this specialty by **Tapu
Bulu**, **Tapu Lele**, **Tapu Fini** and **Tapu Koko** respectively — and the games give exactly
four, one at a time. There is no fifth terrain for this axis and I am not going to pretend there
is one, which is why this answer is built on a clock and a counter instead of on a field
condition.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of a bursty output under an accelerator and a brake, of why a single
sample of such a thing carries no information, and of what you gain and what you throw away by
reading a slow accumulating product instead. The picture is fair. Nothing above stands in for a
person, and nothing above stands in for a child.

Acromegaly is characteristically diagnosed many years after it began, and the features noticed
first are ones people are often blamed for or told to live with. Someone reassured repeatedly who
then turns out to have had a secreting adenoma for a decade has usually absorbed some of that
along the way. That is a harm the diagnostic process caused and it is worth naming as one rather
than reporting as an interesting lag.

Growth hormone in excess also antagonises insulin action, so new glucose intolerance can be the
first thing anybody notices. That matters practically: the axis hormone is interfering with the
metabolic hormones rather than running alongside them, and the person may be investigated for one
thing while the other is the cause.

Because the diagnosis so often depends on an old photograph, it frequently depends on someone
outside the consultation noticing — a relative, a dentist, an optometrist. That changes who needs
to be able to recognise it.

And a note about who is reading. Someone reading this may be in the middle of being investigated
for this, or living with treated disease. If that is you: nothing above is a threshold, a
protocol, a dose or a reassurance. A dynamic test result means something only in the sequence it
was taken in and alongside the rest of the picture, and that reading belongs to the team that
ordered it — not to an analogy about tide tables.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national or specialty-society guidance on acromegaly, for the diagnostic sequence, the
  suppression test as conducted where you work, and the criteria used.
* Your national or specialty-society guidance on adult growth-hormone deficiency, for which
  provocative test is recommended, its contraindications and the criteria applied. This differs
  markedly between countries and some agents are not available everywhere.
* **Your laboratory's handbook**, for the assays it runs, the age-appropriate references it
  reports against and the sample handling required.
* **Your own institution's protocol** for conducting any dynamic pituitary test, including the
  supervision it requires.
* A current endocrinology textbook, for the two-input control of the axis, the hepatic production
  and binding-protein biology of the growth factor, the saturating exposure-to-integral
  relationship, and the dependence of the tissue response on the pattern of exposure.

The Pokémon side is different and is sourced properly. The 24-byte `tide` table with its exact
hours, `UpdateShoalTideFlag`'s `IsMapTypeOutdoors(GetLastUsedWarpMapType())` guard and the **Shoal
Cave** map scripts that read `FLAG_SYS_SHOAL_TIDE`; `EVO_FRIENDSHIP_DAY` to **Espeon** and
`EVO_FRIENDSHIP_NIGHT` to **Umbreon** on one **Eevee** entry; `MAX_FRIENDSHIP` being 255;
**Return**'s `10 * friendship / 25` and **Frustration**'s `10 * (MAX_FRIENDSHIP - friendship) /
25`; the three friendship bands at 100 and 200; the **Soothe Bell**'s `(150 * mod) / 100` with
integer truncation; the **Luxury Ball** and met-location increments; `ShouldSkipFriendshipChange`
naming the **Battle Frontier**, the **Battle Pike** and the **Battle Pyramid**; **Helping Hand**'s
0 power and 0 accuracy; **Imprison**'s shared-move failure condition; **Intimidate** against
**Clear Body** and **White Smoke**; **Flail**'s six-entry table on 48ths of the user's own bar;
the encounter table for the low-tide ice room listing **Snorunt**, **Spheal**, **Zubat** and
**Golbat**; **Castform**'s **Forecast** being handled as a weather form change with no terrain
branch; and `CalculateMonStats` keeping no record of a previous stat were all read from the
pokeemerald and pokeemerald-expansion decompilations rather than from memory. One thing is **not**
claimed and was deliberately checked first: the bitter field medicines do **not** lower friendship
in Generation III, so no confounder in this answer rests on them.

## Scope and safety

The Pokémon here is doing one job: making it concrete that a single sample of a bursty process is
a statement about the moment, and that the alternative is a slow product which buys you a number
at the price of the pattern. It is not a clinical reference, not a decision aid, and not about any
individual's care. **No doses, agents, thresholds, assay cut-offs or test protocols appear here on
purpose** — dynamic pituitary testing carries real risk, is conducted under supervision, and
differs between countries and institutions. Check the formulary and your local protocol. Nothing
here has had clinical review. The assessment of growth in a child is a separate subject, is not
covered here, and no Pokémon in this answer stands in for a child.

## What a Gym Leader digs into next

* Why is one visit to **Shoal Cave** a true observation and no information about the cave?
* Why is a tide flag that was last set elsewhere worse than no flag?
* Why does **Return** stop telling you anything once friendship reaches 255?
* Why is a **Soothe Bell** invisible exactly when the increment is 1?
* Why does the test for too much take the shape of sending in **Arbok** rather than reading a
  number?
* Why has **Flail** nothing to say about this axis when it is the right readout for the thyroid
  one?

## Where this stands, October 2026

The bursty architecture, the accelerator-and-brake control, the reason one sample carries no
information, and the integral's ceiling, baseline-dependence and pattern-blindness are mechanism
and do not date. What dates on the Pokémon side is the constants and the cast: the **Shoal Cave**
tide table is Generation III and Ruby and Sapphire differ from Emerald in parts of the Frontier
that reads the friendship guard, time-of-day encounters are a Generation II feature that
Generation III does not have, friendship was reworked and partly renamed from Generation VIII, and
**Intimidate**'s interaction with abilities that block it has been revised more than once. Check
the current generation's data. On the clinical side everything procedural and numeric moves —
provocative agents and their availability, how the suppression test is run, the criteria applied,
assay standardisation and the references in use — so check current local guidance, your own
institution's protocol and your laboratory's handbook.
