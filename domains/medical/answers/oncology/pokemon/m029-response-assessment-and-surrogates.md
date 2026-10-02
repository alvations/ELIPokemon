---
id: "m029"
slug: response-assessment-and-surrogates
style: pokemon
category: oncology
difficulty: advanced
question: "Why is deciding whether a cancer treatment is working harder than it sounds, what does a structured response criterion actually buy, and why is a better scan not the same thing as a longer life?"
tags: [response-assessment, surrogate-endpoints, imaging, measurement, endpoints]
---

# The bar is forty-eight pixels wide, and it never shows empty while anything is left

The game knows an exact number. You are not shown it. What you are shown is a bar, and the code
that draws it is three lines long: the current value times forty-eight, divided by the maximum, in
integer arithmetic — **and then, if that came out as zero while anything at all remains, it is
forced back up to one.**

Every property of response assessment is in those three lines. The readout is quantised. The
quantisation is deliberate. And the bottom of the scale is a floor rather than a zero, so *looks
like nothing left* is a statement about the instrument.

As elsewhere in this specialty: **the objects of study are readouts, thresholds and stat tables.**
Nothing here stands in for a person, and the analogy is dropped at the end, where the subject
changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
(**consensus**, **country-dependent**).

## What the readout does to the number

```
   THE EXACT VALUE          an integer the game holds and never shows you
        │
        ▼
   THE BAR                  value × 48 ÷ maximum, integer division
        │                   ── 48 steps. Anything finer than a forty-eighth
        │                      is INVISIBLE. Information destroyed on purpose.
        │
        │                   ── and: if that division gives 0 while the value
        │                      is still above 0, the code RETURNS 1 INSTEAD.
        │                      The bar is never empty while anything remains.
        ▼
   THE COLOUR               above 50% of the pixels      ── green
        │                   above 20% of the pixels      ── yellow
        │                   anything else above zero     ── red
        │                   ── 48 steps collapsed into 3 WORDS, at published
        │                      thresholds. Two people now agree on the word.
        ▼
   WHAT SOMEBODY SAYS       "it's going well"
                            ── a claim about the battle, inferred from a
                               convention applied to a quantised proxy

   ────────────────────────────────────────────────────────────────────────

   AND THE NOISE, which decides how big a threshold has to be:

   the Damage Roll multiplies every hit by a whole number of per cent
   from 85 to 100 — sixteen values, one picked at random.

   85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100
   └──────────────── fifteen points wide ──────────┘

   A single reading cannot tell a real change from the die. Any threshold
   for declaring change must be WIDER THAN THIS, or it reports the die.
```

## Why the measurement is hard, mechanically

**A bar is a proxy, and 48 steps is the whole of its resolution.** One linear readout standing in
for the real quantity loses information before anyone interprets it, and the loss is not an
oversight — a bar is far easier for two people to agree about than an exact number they cannot
see. A scan is the same trade (**mechanism**): a linear diameter standing in for an irregular
three-dimensional volume, chosen precisely *because* diameters are more reproducible between
observers than volumes are, even though a volume would be more faithful. Reproducibility is what
the chain is optimised for, not accuracy.

**The noise is not small compared with the changes of interest.** The **Damage Roll** spans
fifteen points, and a **Critical Hit** lands on its own schedule on top of that, so one
observation is compatible with a range of truths. Clinically: the same lesion measured by two
readers, or by one reader twice, or on two machines, gives different numbers — so a threshold for
declaring change must sit *above* that spread or the criterion will faithfully report the cursor
(**mechanism**).

**A total can hide its own parts.** **Blissey**'s base stats are 255 HP, 10 Attack, 10 Defense, 55
Speed, 75 Special Attack and 135 Special Defense. The total is 540 and it tells you nothing about
the shape: that one entry is the largest in the game and two others are among the smallest. Add
several readouts into one number and the total can fall while individual components move in
opposite directions — which is why criteria also require attention to unequivocal new disease
rather than trusting the sum alone (**mechanism**).

**And some of what matters has no bar at all.** The game shows you no readout for how many turns
of **Leftovers** recovery you have banked, or for an opponent's remaining PP. Clinically: bone
disease, effusions, peritoneal and leptomeningeal disease, diffusely infiltrating disease —
present, consequential, and not amenable to a diameter. Criteria handle these as their own
category rather than pretending otherwise (**consensus**), which is honest, and which also means
the headline category rests on the measurable subset.

## What the structured criterion buys — and it is the colour bands

This is the part worth dwelling on, because the game contains an actual, published response
criterion.

Nobody has to argue about green, yellow and red. The thresholds are fixed in the code at more than
half the pixels and more than a fifth of them, and they are applied to the *quantised* readout
rather than to the exact number. Two players watching the same bar will disagree about the pixel
and agree about the colour. That is the entire function of a structured response criterion
(**definitional**, **consensus**):

* **Agreement.** Two radiologists, two centres, two trials, one vocabulary.
* **A threshold above the noise**, so a reported change is probably not a cursor.
* **A rule fixed in advance**, which removes the freedom that would otherwise let the reader
  choose the answer.

The widely used solid-tumour framework specifies which lesions may be measured, how many, how they
are summed and what change in the sum earns which word. The lymphomas use a different framework
built on metabolic imaging, because a nodal mass that shrinks slowly is badly described by size.
And immunotherapy-specific variants exist because apparent early enlargement can precede response,
so they require confirmation before progression is declared (**definitional**, **consensus**).

The thresholds in that solid-tumour framework are set above measurement noise — roughly a third of
the summed diameters down for a partial response, roughly a fifth up together with an absolute
minimum for progression. **Those are shapes, given to show the reasoning, and not figures to
quote.** The exact numbers and the rules for new and non-measurable disease are definitional, they
belong to the published criteria, and the criteria are revised. Read them there.

## And now the floor, which is the best fact in this answer

`if (result == 0 && hp > 0) return 1;`

The bar will not show empty while anything is left. Deliberately. So when the bar looks gone, what
you have learned is that the remaining amount is **below one forty-eighth of the maximum** — which
is a statement about the resolution of the bar and not about the quantity being measured.

That is a complete response on imaging, exactly (**mechanism**). It means no disease is visible at
the resolution of the modality used, by the rules of the criterion applied. It does not mean no
disease. The distinction is not pedantry; it is the reason treatment and follow-up do not simply
stop when the images clear.

And whatever sits below the resolution is not thereby unimportant. A **Focus Sash** leaves its
holder on a single point of HP, and **Sturdy** in the modern games does the same from full health:
the quantity the bar can no longer resolve is the quantity the whole position now turns on. Small
and invisible are not the same property as absent.

**Two further ways the readout answers a different question than the one asked.** **Substitute**
costs a quarter of maximum HP and then absorbs the hits — so what the incoming damage is being
subtracted from is the Substitute, not the Pokémon behind it, and reading the bar tells you about
the wrong object. Clinically, a treated lesion can leave a residual mass that is fibrosis rather
than disease, and a lesion that has not shrunk at all can be metabolically dead (**consensus**).
And **Zoroark**'s **Illusion** presents as something it is not until it takes a damaging hit — the
readout you were reasoning from was attached to the wrong thing entirely. A tumour marker that
moves for an unrelated reason is that failure, which is why a marker is an adjunct to the
assessment and never a replacement for it (**consensus**).

**And the readout only updates when the game checks.** Weather and status damage are applied at
the end-of-turn routine, in a fixed order, which means the *apparent* timing of an effect is a
property of the schedule rather than of the effect. Clinically, an interval that ends at a scan
depends on when the scans were (**mechanism**): two arms imaged on different schedules are not
comparable, and spacing the scans further apart lengthens the measured interval while changing
nothing at all about the disease.

## The surrogate: one number that correlates, and misranks exactly where it matters

**Base Stat Total** is the summary number everybody reaches for. Add the six base stats and you
have a single figure that broadly tracks how formidable a Pokémon is. It is a surrogate, it is
useful, and the games contain its failure modes by name.

**Slaking**'s base stats in the species data are 150 HP, 160 Attack, 100 Defense, 100 Speed, 95
Special Attack and 65 Special Defense. That totals **670** — among the very highest in the game.
Its ability is **Truant**, and in the battle code Truant flips a one-bit counter each turn, so it
acts only on alternate turns. The surrogate is not wrong about the stats. It is simply blind to
the thing that decides the outcome.

**Regigigas** carries the same total of 670 and **Slow Start**, which halves its Attack and its
Speed for the first several turns it is on the field. Two Pokémon, one number, two different
abilities voiding it — and the number cannot see either.

**Shedinja** is the same failure in the other direction: base HP of **1**, a total that looks
derisory, and **Wonder Guard**, which discards everything that is not super effective.
**Eviolite** is the same miss again from outside the stat line, raising the defences of anything
that can still evolve, so the published numbers understate what is actually on the field. And
**Spinda** sits at exactly 60 in all six, so its total says nothing about it that is not also true
of a great many other Pokémon.

That is a surrogate endpoint's failure mode precisely (**mechanism**). A surrogate is a
measurement used in place of the outcome that matters, because it comes earlier or is easier to
see — response proportions and the progression-free and disease-free intervals standing in for
overall survival and for quality of life (**definitional**). They exist for a real reason, and
they fail in characteristic ways:

* **A surrogate measured on a schedule inherits the schedule** — the end-of-turn problem above.
* **Unblinded assessment biases it.** A reader who knows the arm has a thumb on the scale, which
  is what independent blinded review is for — and the games already have the machinery, because a
  **Battle Video** saved on the **Vs. Recorder** can be handed to somebody who was not there and
  did not choose the moves.
* **Informative censoring.** If people leave a study for reasons connected to how they are doing,
  what remains is not a random sample.
* **The chain can break at the last link.** A treatment can delay the measured event without
  extending life — because of what follows it, because subsequent treatment differs between arms,
  or because the mechanism that moved the surrogate does not translate. Truant is this: the stat
  total moved and the thing you cared about did not.
* **Validation is a trial-level claim, not a patient-level one** (**consensus**). That people
  whose disease responds tend to fare better is a *prognostic* observation; it does not establish
  that a treatment improving response improves survival. Establishing that needs treatment effects
  to correlate across many trials, which has been shown convincingly in some diseases and not in
  others.

**The field genuinely disagrees** about which surrogates are acceptable for which purpose, and
regulators in different jurisdictions weigh them differently (**consensus**,
**country-dependent**). Anyone presenting this as settled has not read the argument.

## Where the metaphor stops

Everything above is about instruments, thresholds and inference, and a game is a good place to
look at those. What follows is about people, so it is said plainly and without the analogy.

An imaging response is an observation about images. It is real evidence, often the best available
early, that something is happening. It is **not** the same proposition as *this person will live
longer*, and it is **not** the same proposition as *this person will feel better*. Those are
different claims needing different evidence, and the second is frequently the one that matters
most to the person and is measured least. Imaging can improve while someone feels worse, because
the treatment doing the shrinking has its own costs, and that combination is not a paradox — it is
two different things being measured.

A population statistic of any kind is an average over a large and varied group, assembled in the
past, under the treatments and the imaging of that time. It cannot say what will happen to any one
person within it, because any one person differs from that average in exactly the ways the average
has no language for. That is a limit on what the arithmetic can do, not a reluctance to say the
hard thing, and it is why no survival figure or response proportion appears anywhere in either
half of this answer.

## What a Gym Leader is listening for

* Why is a coarse readout sometimes better than an exact one, and what is the trade?
* Why must a threshold for declaring change be wider than you would expect?
* What does an empty-looking bar actually tell you, given the floor in the code?
* How does the scan interval change a progression-free interval with no change in biology?
* What is the difference between a prognostic association and a validated surrogate?
* Why does Slaking's total of 670 misrank it, and what is the clinical equivalent?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md).
Specific to this answer:

* The response-evaluation criteria your centre or trial actually uses, in their current published
  revision, from the group that maintains them — the authority for every threshold, every
  lesion-selection rule and every category definition sketched above.
* The disease-specific response framework where one applies, including the metabolic-imaging-based
  classification used in the lymphomas, as published by the body that maintains it.
* The immunotherapy-specific variant of the solid-tumour criteria, from the same source, for how
  apparent progression is confirmed.
* The regulatory guidance on acceptable endpoints published by the medicines regulator in your
  jurisdiction, which differs between jurisdictions and changes.
* The protocol of any trial whose results you are reading, for its imaging schedule, its blinding
  arrangements and its pre-specified endpoints — the three things that decide what its headline
  number means.

## Scope and safety

This is revision material about measurement and inference, dressed in a game because a game's
readouts are open to inspection in a way a scanner's are not. It has had no clinical review. No
threshold, interval or criterion is quoted here as fact, and none should be acted on; the
published criteria in their current revision, and your local radiology and trial protocols, are
the authority, and this is not. Criteria and the regulatory acceptability of surrogate endpoints
differ between countries and are revised. Nothing here describes any individual's situation, and
nothing here interprets anybody's scan. Anyone affected by cancer — their own diagnosis or someone
else's — should be talking to the clinical team looking after that person, who have the images,
the history and the context, none of which are here. The analogy covers measurement and stops
there: no part of it stands in for a person, and none of it says anything about what happens to
anybody.

## Where this stands, October 2026

The Pokémon facts are read from the games' own source. The health bar is forty-eight pixels wide;
the scaling function is current value times that width divided by the maximum in integer
arithmetic, and it returns 1 rather than 0 whenever the value is above zero; the colour thresholds
are more than fifty per cent and more than twenty per cent of the filled pixels. The Damage Roll
is a whole number of per cent from 85 to 100. Slaking's base stats are 150, 160, 100, 100, 95 and
65, totalling 670, and Truant's implementation flips a one-bit counter each turn so the Pokémon
acts on alternate turns. Shedinja's base HP is 1 and its ability is Wonder Guard; Spinda's six
base stats are all 60. Weather and status damage are applied in a fixed end-of-turn routine.

The clinical reasoning is durable: a diameter proxies a volume, a threshold must exceed
measurement noise, a category is a convention, and a surrogate is a chain of inference whose last
link has to be demonstrated rather than assumed. The specifics are not: criteria are revised,
frameworks multiply, and the endpoints regulators accept move and differ between jurisdictions.
The two approximate thresholds mentioned above are shapes rather than the criterion, and no trial,
guideline number or survival figure appears here, deliberately — those are the facts that date,
and the ones most damaging to get wrong.
