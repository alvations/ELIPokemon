---
id: "m028"
slug: why-toxicity-is-predictable
style: pokemon
category: oncology
difficulty: advanced
question: "Why do cytotoxic agents damage the particular tissues they damage, why is the timing of that damage predictable rather than surprising, and why do immunotherapy toxicities look like autoimmunity?"
tags: [toxicity, myelosuppression, mucositis, immune-related, mechanism]
---

# The exemption list is types, not names — and the counter says when

Three mechanics from the games' own data carry this whole answer, and none of them involves
anybody standing in for a patient. **Sandstorm** exempts by property and never asks whose side
anyone is on. **Future Sight** computes its damage at the moment it is used and delivers it two
turns later. And **PP** is three different reserves drawn down at the same rate, so the smallest
one empties first.

Between them they give you: why a cytotoxic agent hits the tissues it hits, why the lowest point
comes days after the dose, why one blood count falls before another, and why immunotherapy
toxicity is autoimmunity rather than resembling it.

As in the rest of this specialty: **the objects of study are moves, items, abilities and
weather.** No Pokémon in this answer stands in for a person with cancer, and the analogy is
dropped entirely at the end, where the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
(**consensus**, **country-dependent**).

## Property, not identity — and the separate question of when

```
   Sandstorm, at the end of every turn, from the Emerald code:

       charge maxHP/16   ───► to EVERY Pokemon on the field
              │                        │
              │                        └── EXCEPT if its type is Rock,
              │                            Steel or Ground, or it has
              │                            the one exempting ability
              ▼
       and there is NO TEST of whose side anyone is on.
       The exemption is a PROPERTY. It is never an identity.

       Tyranitar, which SETS the sandstorm with Sand Stream, is
       Rock — so it is exempt by the same clause as everyone else,
       not by being the one who started it.

   ──────────────────────────────────────────────────────────────────────────

   A cytotoxic agent's exemption list reads the same way:

       in scope  ──►  "is this cell replicating or separating DNA right now?"
                      marrow progenitors, gut crypts, growing hair follicles,
                      germ-cell precursors  ────► all answer YES
       exempt    ──►  muscle, nerve, cardiac myocytes  ──► all answer NO

   ──────────────────────────────────────────────────────────────────────────

   AND THE TIMING IS A SEPARATE MECHANIC.  Future Sight:

       turn 0   move used   ─► damage CALCULATED NOW, counter set to 3
       turn 1   nothing visible happens
       turn 2   the counter runs out and the damage LANDS

       Magnitude fixed at administration.  Arrival later.  Entirely
       predictable, and invisible in between.
```

## Why the marrow, and why in that order

The marrow's progenitor compartment is among the most actively dividing tissue in the body, so it
answers yes to the only question a cytotoxic agent asks (**mechanism**). Muscle, nerve and cardiac
myocytes answer no, and they are spared for the same reason **Flygon** is spared an
**Earthquake**: **Levitate** is a property the move's own rule checks, so the exemption needs no
special pleading and no exception list of names. What makes the picture teachable is that the
three mature lineages do *not* fall together — and the reason is not the drug.

**This is PP.** Look at the pp field in the move data: **Struggle** has 1, **Cross Chop** has 5,
**Earthquake** 10, **Double-Edge** 15, **Take Down** 20, **Submission** 25. Stop restoring PP and
all six draw down under the same conditions, but they do not run out together. The one with the
smallest reserve is unusable first, and the order of failure is set by the size of each reserve,
not by anything about the thing doing the drawing down.

Mature circulating blood cells are post-mitotic — they are not dividing, so they are not the
target (**mechanism**). They live out their normal spans and are simply not replaced, because the
factory behind them has been knocked back. So the lineage whose circulating cells are
shortest-lived runs short first. Neutrophils, shortest-lived in circulation of the three, fall
first; platelets follow; red cells, whose circulating lifespan is much the longest, are slowest
and are more a feature of repeated cycles than of one (**mechanism**, **consensus**).

Two facts students usually learn separately are the same fact:

* **The lowest point comes days after the dose and recovery follows it**, because the progenitor
  pool regenerates. Future Sight's counter is the shape of it: the magnitude was fixed when the
  dose was given and the arrival is scheduled. And the recovery is **Leftovers** — a sixteenth of
  maximum HP back at the end of every turn, which is why an interval between exposures is worth
  something and a shorter one is worth less.
* **The depth and timing are reproducible for a given regimen**, which is what makes monitoring
  and supportive care plannable rather than reactive.

## Mucosa, follicles, germ cells

Same question asked, same answer given, different transit times (**mechanism**).

**Gut and oral mucosa** are renewed continuously from crypt and basal compartments, so those
compartments answer yes, and the consequence is mucosal inflammation and ulceration with altered
bowel function. The latency is the journey from the damaged dividing layer to the surface it was
meant to replace.

**Hair follicles** only answer yes while in their growth phase, which is why the effect varies
between agents, is not universal, and reverses when the progenitor compartment recovers.

**Germ-cell precursors** divide, so effects on fertility are a mechanistic consequence rather than
bad luck — and because they are mechanistic, they are foreseeable while treatment is still being
planned. That is why discussion of fertility preservation belongs before treatment starts, and is
standard practice in most systems (**consensus**, (**country-dependent**) in what is available and
funded).

## Where the rule stops, and the data says so too

Here is the honest part, and the games supply the warning themselves. **Sandstorm's exemption list
is not derived from anything.** Rock, Steel and Ground are exempt because they are enumerated in
the code as exempt — there is no deeper principle you can read off the type chart that generates
that list. A rule that explains most of a list and is then stretched to cover all of it has
stopped being a mechanism and become a mnemonic.

Three places the fast-dividing rule does not reach:

* **Nausea and vomiting are not a dividing-tissue effect.** They are receptor-mediated and
  substantially central: signals from the gut and the circulation acting on brainstem structures
  through specific neurotransmitter pathways — which is exactly why the drugs that prevent them
  target those receptors, and why prophylaxis follows the emetogenic profile of the regimen rather
  than any turnover argument (**mechanism**, **consensus**).
* **Several agents damage organs that are not proliferating at all** — cardiac, renal, auditory,
  peripheral nerve and pulmonary, depending on agent — through agent-specific biochemistry
  (**consensus**).
* **Fatigue** is multifactorial and has no single clean mechanism, which is worth saying instead
  of inventing one.

## Two different kinds of cost, and the games have both

This is the distinction that makes the section above usable, and there are three items and moves
that make it concrete.

**A cost proportional to what you delivered.** **Double-Edge**'s recoil, in the code, is the HP
actually dealt divided by three; **Take Down** and **Submission** take a quarter. Deal nothing and
you pay nothing. That is a **dose-intensity-limited** toxicity: a function of how much was given
this cycle, recovering in the gap because the damaged compartment regenerates, answered by dose
reduction, delay and supportive measures (**mechanism**, **consensus**). Myelosuppression is the
archetype.

**A flat charge per exposure, which accumulates.** A **Life Orb** takes its tenth of maximum HP
every time, whatever the attack achieved. Worse, **Badly Poisoned** multiplies a sixteenth of
maximum HP by a counter that climbs every turn — the charge grows with how long the exposure has
run. That is a **cumulative-dose-limited** toxicity: a function of the *total received over a
lifetime*, not recovering in the gap because the damaged tissue does not regenerate the way a
progenitor pool does (**consensus**). It is why lifetime totals for certain agents are recorded
and carried forward across lines of treatment and across years. A person's exposure history is
clinical information, not filing.

**And a gate before any of it.** **Belly Drum** maximises the user's Attack for half of its
maximum HP — and the code checks first: the move fails outright unless the user's current HP is
*above* half its maximum. You cannot pay the cost out of a reserve you do not have, and the game
refuses the trade rather than letting you try.

The limiting case is **Shedinja**, whose base HP in the species data is **1**. Half of 1 is 0, the
code floors that to 1, and the gate then asks for current HP strictly greater than 1 — which
Shedinja can never have. Belly Drum is not merely unwise for it; the move cannot succeed, ever.
And **Wonder Guard** does not help, because Wonder Guard governs what gets through from outside
while this cost comes out of the trade itself.

Intensive regimens work the same way: fitness and organ function are assessed as a gate at the
start, not as a consequence at the end (**consensus**). That is the same arithmetic read from the
other direction, and it is not rationing.

## Why immunotherapy toxicity is autoimmunity

Back to the sandstorm, because the code already said it. The routine checks types. It checks one
ability. **It never checks sides.** And the weather keeps running after whoever set it has left
the field — **Tyranitar** can be long gone and the **Sand Stream** it brought is still charging
everything on the field that is not Rock, Steel or Ground.

A checkpoint inhibitor blocks an inhibitory signal on T cells (**mechanism**). It supplies no
targeting and no specificity, and it does not act on the tumour at all — it removes a brake on a
system that was already there. And the brake it removes is the one holding back responses against
self. Three consequences follow with no extra observation required:

* **Any organ is in scope**, because the brake was systemic: colon, liver, lung, thyroid and
  pituitary and the other endocrine organs, skin, joints, myocardium, peripheral and central
  nervous system.
* **It is not dose-proportional**, because the drug is not the thing doing the damage. There is no
  smaller amount of a field condition.
* **The latency is variable and an event can start after treatment ends** — the weather outlasts
  the Pokémon that set it.

**So management differs in kind** (**mechanism**, (**country-dependent**) in protocol):
immunosuppression, and sometimes stopping for good, rather than the dose reduction that answers a
cytotoxic toxicity — which cannot address a process the drug is not driving. Some endocrine
effects do not resolve and need lifelong replacement (**consensus**). Cell therapies and T-cell
engagers add syndromes from cytokine release and from neurological effects, each with its own
graded pathway.

Two last mechanics, both real and both limited. An **Air Balloon** keeps its holder out of scope
until the first thing lands on it, and then it is gone — a protection that holds only until it
does not. And **Magic Guard**, which Clefairy was given from the fourth generation on, blocks
indirect damage without touching the move's power: the shape of supportive care, something that
intercepts a cost without blunting the agent. Real mechanic, real principle, and not a promise
that every cost has an interceptor. Most do not.

## Where the metaphor stops

Everything above is mechanism, and the analogy earns its keep there: it makes the list derivable
instead of memorised and the timing plannable instead of alarming. It is not the thing itself, and
this answer is not going to end as though it were.

Low neutrophils are not a number on a chart. A fever in that setting is time-critical, and
services are built around getting people assessed fast for exactly that reason. Mucositis is
painful and can stop someone eating or drinking. Hair loss is not a cosmetic footnote and nobody
should present it as one. Effects on fertility change the shape of people's lives, which is why
that conversation belongs before treatment rather than after it. Fatigue is often the thing people
rate as hardest, and it is the one this answer has the least mechanism for.

None of that is made smaller by being predictable. Being able to derive an adverse-effect list is
a different skill from being any use to someone who is living through one, and nothing in a game
speaks to the second. These things happen to people, not to anything in the data quoted above, and
that distinction is the reason the analogy stops at this heading every time.

## What a Gym Leader is listening for

* Why does the neutrophil count fall before the platelet count? Answer in terms of reserves, not
  drugs.
* Why is the lowest point days after the dose rather than hours?
* Name an adverse effect the fast-dividing rule does not explain, and say what does explain it.
* Why are lifetime cumulative totals recorded for some agents and not others?
* Derive the consequences of checkpoint blockade from what a checkpoint is for.
* Why is dose reduction the wrong instinct for an immune-related adverse event?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md).
Specific to this answer:

* The summary of product characteristics, or equivalent national prescribing information, for any
  specific agent — the authority for its toxicity profile and for any cumulative limit.
* Your centre's systemic anticancer therapy protocols and its pathway for suspected neutropenic
  sepsis, which is a local document and the only one that governs local practice.
* The published management guidance for immune-related adverse events issued by your national or
  regional oncology professional body, and your centre's local version of it.
* The adverse-event grading terminology your service reports against, as published by the body
  that maintains it.
* Your national or regional guidance on fertility preservation before systemic anticancer therapy,
  for what is offered and funded where you are.
* A current standard haematology text, for the circulating lifespans the ordering argument above
  depends on.

## Scope and safety

This is revision material about mechanism, dressed in a game so the timing and the targeting stay
concrete. It has had no clinical review. No dose, cumulative limit, monitoring interval,
blood-count threshold or management step appears here, and none should be inferred; the formulary,
the local protocol and the local sepsis pathway are the authority, and this is not. Practice
differs by country, region and institution and changes. Nothing here describes any individual's
situation, and nothing here is a guide to recognising or managing a toxicity in a real person.
Anyone affected by cancer — their own diagnosis or someone else's — should be talking to the
clinical team looking after that person, and anyone unwell now should use their local emergency or
acute oncology route rather than reading this. The analogy covers mechanism and nothing else: no
part of it stands in for a person, and none of it says anything about what happens to anybody.

## Where this stands, October 2026

The Pokémon facts are read from the games' own source. Sandstorm charges a sixteenth of maximum HP
at the end of each turn, exempts Rock, Steel and Ground types and one ability, and its routine
contains no test of which side a Pokémon is on. Future Sight sets a counter of 3 and stores its
damage, calculated at the moment of use, to be applied when the counter runs out. The pp fields
quoted are Struggle 1, Cross Chop 5, Earthquake 10, Double-Edge 15, Take Down 20, Submission 25;
Double-Edge's recoil is the HP dealt divided by three and Take Down's and Submission's a quarter
of it. Badly poisoned damage is a sixteenth of maximum HP multiplied by a counter that increments
each turn to a cap. Belly Drum sets Attack to its maximum stage, costs half of maximum HP, and
fails unless current HP is above half. Life Orb, Air Balloon and Magic Guard are later-generation
additions described from working knowledge of those games rather than from code opened here, as is
the note about Clefairy gaining Magic Guard in the fourth generation.

The clinical argument — kinetic selectivity producing a turnover-ranked toxicity list, circulating
lifespan producing the order and the delay, checkpoint release producing autoimmunity — is
long-standing and durable. What changes is the supportive care, the grading terminology, the
management pathways for immune-related events, and which agents carry which cumulative limits. No
agent, number, threshold or trial is named, deliberately. Those facts date, and they belong to the
prescribing information and the local protocol rather than to a revision note like this one.
