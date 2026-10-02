---
id: "m030"
slug: screening-and-overdiagnosis
style: pokemon
category: oncology
difficulty: advanced
question: "Why is finding more cancer not automatically better? Explain lead-time bias, length bias and overdiagnosis, and why overdiagnosis is a real harm rather than a technicality."
tags: [screening, overdiagnosis, lead-time, length-bias, epidemiology]
---

# Three rods, one pond, and the pond never changed

Cast an **Old Rod** in Red and Blue and the code gives you a level 5 **Magikarp**. Not usually —
the routine sets the bite flag unconditionally and hands over that one species, every time. The
**Good Rod** picks at random between a **Goldeen** and a **Poliwag**. The **Super Rod** consults a
per-map table of up to four species, and in the **Safari Zone** one of the four is a **Dratini**.

Same water. Same routes. Three instruments, three catalogues, and **the pond was never once
consulted about any of it**. Everything the better rod returns was already in the water before
anyone bought it, doing nothing.

That is the entire argument about screening, and it is why *finding more cancer* is not the same
claim as *doing more good*. A screening programme takes people who feel fine, applies a test, and
changes what happens to some of them — so it is judged on whether fewer people die, not on how
much it finds (**mechanism**).

As elsewhere in this specialty: **the objects of study are instruments, encounter tables and
detection rates.** No Pokémon in this answer stands in for a person, and the analogy is dropped
entirely at the end, where the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
**consensus**, **country-dependent**.

## What the instrument returns, and what a periodic look actually samples

```
   SAME WATER, THREE RODS                 and the water is unchanged throughout

      Old Rod     ──►  Magikarp                                  1 species
      Good Rod    ──►  Goldeen, Poliwag                           2 species
      Super Rod   ──►  up to four per map; Dratini in the
                       Safari Zone                                4 species

      ── a rising catalogue is a property of the ROD.
         Read it as a property of the pond and you have made
         the central error in this whole subject.

   ─────────────────────────────────────────────────────────────────────────

   AND WHAT A PERIODIC LOOK RETURNS — a property of the SCHEDULE, not of
   the importance of anything in the water:

      you walk the same route, once every so often:  ▼   ▼   ▼   ▼   ▼

      Snorlax, asleep on Route 12,                   ✔   ✔   ✔   ✔   ✔
      exactly where it was last time                 ── found EVERY TIME

      Sudowoodo, standing in the way                 ✔   ✔   ✔   ✔   ✔
      until it is dealt with                         ── found EVERY TIME

      the Emerald roamer: Latias or Latios,          ✘   ✘   ✘   ✔   ✘
      which changes map whenever you do and
      explicitly avoids where it was two
      moves ago                                     ── almost never found

   ── the periodic look does NOT sample what is out there. It samples
      it WEIGHTED BY HOW LONG EACH THING STAYS PUT. And in screening
      that weighting is exactly backwards: the cases that linger longest
      in the detectable window are the least dangerous ones.
```

## Lead-time bias: start the clock earlier and the interval gets longer

The **Pokédex** keeps two counters, seen and caught. Suppose you measure *how long you have known
about a species* from the moment its entry first appeared. Look in the tall grass earlier in the
game and that interval is longer — and not one thing about the species has changed. You started
the clock sooner.

Survival is conventionally measured from the date of diagnosis. Move the diagnosis earlier and the
measured survival lengthens **even if the date of death is identical** (**mechanism**). Nothing
about the person or the disease has altered.

Which is why survival measured from diagnosis is close to useless for evaluating a screening
programme, and why programmes are instead judged on mortality across a whole invited population
over a defined period, invited against not invited. The denominator has to be the population and
not the diagnosed, or the bias is designed in.

## Length bias: the fixtures are always found and the roamer almost never is

Read the roamer routine in Emerald and the mechanism is explicit. Each time the player changes
maps, **Latias** or **Latios** — whichever you did not see on television — moves to a different
map within its set, and the code deliberately excludes the map it occupied two moves ago. Check
one route periodically and you will scarcely ever meet it.

Now the opposite. The **Snorlax** blocking **Route 12**, and the second one on Route 16, are
scripted fixtures: they are there until they are dealt with, so anybody walking past finds them.
**Sudowoodo** in the way in Johto is the same. The red **Gyarados** at the **Lake of Rage** is a
single fixed encounter, and it is **Shiny**, and it is exactly where everyone says it is. The
**Regirock**, **Regice** and **Registeel** chambers never move either.

A periodic survey therefore returns the fixtures and misses the roamer, and that has nothing to do
with how important either is (**mechanism**).

**Be exact about what is being mapped here, because it would be easy to read it wrongly.** The
quantity carried across is **dwell time** — how long something stays available to be found at the
place you are looking. Nothing in the game stands in for a disease's seriousness, and nothing in
it stands in for anybody who has one. The point is a property of the *schedule*.

Clinically: a test can only detect a case while that case sits in its detectable-but-asymptomatic
window, so the longer the window, the more rounds the case is available to. Slowly progressing
disease is therefore systematically over-represented among screen-detected cases; rapidly
progressing disease is under-represented and tends instead to present symptomatically between
rounds.

Two consequences, the second of which is the one people miss:

* **The screen-detected population is biologically more indolent** than the population presenting
  clinically. Comparing their outcomes compares two different populations, and the screen-detected
  group looks better even if the screening achieved nothing.
* **Interval cancers are not primarily a quality failure.** Some are missed and a programme must
  audit for those, but a proportion are a mechanical consequence of looking periodically — fast
  disease can arise and present entirely between two rounds. A programme with no interval cancers
  would be one with an implausibly short interval.

## Overdiagnosis: the thing that was real, detectable, and never going to matter

Two mechanics, both exactly on the point.

**Spinda has four spots**, and the comment in the source says it plainly: the whole thirty-two-bit
personality value is used, eight bits per spot, to place them. Every Spinda's pattern is different
from every other Spinda's. So if you set out to find an irregularity in a population of Spinda,
you will find one in every single member — not because anything is wrong with any of them, but
because **variation is the baseline** and a close enough look always finds it. The quantity being
carried across is that baseline variation and nothing else: look at naturally variable *tissue*
with a more sensitive instrument and the count of abnormal-looking findings rises, while the
tissue is exactly what it was before anyone looked.

**And a Shiny** is a real, verifiable, genuinely unusual difference — the Emerald constants put
the odds at 8 in 65,536 — which changes **nothing functional whatsoever**. Correct detection,
correct rarity, no consequence. *Real* and *consequential* are different properties, and a test
can only establish the first.

Which brings the actual definition. **Overdiagnosis is the detection of disease that meets the
diagnostic criteria but would never have caused symptoms or death during that person's life**
(**definitional**) — because it does not progress, because it regresses, or because the person
dies of something else first.

The distinction from a false positive is the whole point and is routinely got wrong. A false
positive is a wrong result, resolved by further testing. **An overdiagnosed cancer is a correct
result.** The pathology is real, the criteria are met, a second opinion confirms it, and the
diagnosis cannot be taken back. What is wrong is not the finding but the inference that the
finding needed to be made.

## How it is inferred, since it cannot be seen case by case

You cannot point at an overdiagnosed individual, so it is inferred from populations
(**mechanism**, **consensus**). The signature is recorded incidence rising after testing is
introduced or intensified, **without** a matching fall in the incidence of advanced disease and
without a fall in mortality. A test genuinely moving cases earlier should drain the late-stage
category as it fills the early one. When early-stage incidence rises and late-stage incidence does
not fall, the extra cases are additional rather than earlier.

Two standard teaching examples (**consensus** — and these are the claims in this answer a reviewer
should check first, because they are empirical and specific):

* Screening infants for one particular childhood tumour was introduced in several health systems.
  Recorded incidence rose substantially, deaths from that tumour did not fall, and the programmes
  were discontinued.
* Where neck ultrasound came into very widespread use, recorded thyroid cancer incidence rose
  steeply while mortality stayed flat.

Elsewhere the magnitude is **genuinely contested** rather than unknown. Breast screening and
prostate-specific antigen testing are the two long-running arguments, and the disagreement is
about how much, not whether. Anyone presenting either as settled is quoting one side.

## The other harms, which are not overdiagnosis

Different mechanisms, worth keeping separate (**consensus**): false positives and the cascade of
further imaging and biopsy that follows them in people who do not have the disease; harm from the
test and from the investigations it triggers; radiation where the modality involves it, small per
examination and not zero across a population; **inequity**, because a programme with socially
skewed uptake can widen outcome gaps when the benefit goes to those who attend and the burden
stays with those who do not (**country-dependent** in extent); and opportunity cost, because the
resources are competing with everything else.

## The one kind of screening that is mechanistically different, and it is Rapid Spin

This is the best distinction in the answer and it is usually lost.

**Stealth Rock** and **Toxic Spikes** are **Entry Hazards**: once set, they charge every arrival.
**Rapid Spin** and **Defog** do not detect them earlier or describe them better. They **remove**
them, and the damage then never happens at all.

Most screening finds invasive disease earlier, so its benefit rests entirely on earlier treatment
working better, and it is fully exposed to all three biases above. But some programmes find and
remove **precursor lesions**, and that changes the incidence of invasive cancer rather than only
its timing (**mechanism**). Cervical and colorectal programmes are built on it, and the signature
is different: if it works, invasive incidence itself falls. That is far stronger evidence than a
shift in stage distribution, because **a fall in incidence cannot be produced by any of the three
biases in this answer.**

So the right first question about any screening programme is which of the two kinds it is, before
any question about how well it performs.

## Where the metaphor stops

Everything above is about instruments and sampling, and a game with readable encounter tables is a
good place to see it. What follows is about people, and it is said plainly.

Overdiagnosis is not a technicality and it is not a rounding error in somebody's spreadsheet. It
means a person who felt well was told they had cancer, was treated for cancer, and carried
everything that goes with that — surgery and its consequences, systemic therapy and its
consequences, radiotherapy and its consequences, surveillance, and a diagnosis that does not go
away and that follows them through every later medical encounter and, in some systems, into
insurance and employment. And the disease was never going to trouble them. That is a serious harm
done by a well-intentioned system to somebody who was fine, and it is the reason programmes are
obliged to state their harms alongside their benefits rather than only the benefits.

It is also irreducibly impersonal, and this part matters. **Overdiagnosis is a population-level
excess, and for any individual it is unknowable.** Nobody can be told that they personally were
overdiagnosed, because the course their disease would have taken was never observable. For anyone
whose cancer was found by screening, nothing in this answer says anything about their diagnosis,
and none of it can be applied to it. And for anyone deciding whether to take up an invitation, the
relevant things are their own risk, the specific test, what is offered where they live and their
own view of the trade — a conversation with someone who knows their circumstances, not a page like
this one. No population figure appears anywhere here, because a population average cannot tell any
one person what will happen to them.

## What a Gym Leader is listening for

* Why is survival from diagnosis the wrong endpoint for a screening programme, and what is the
  right one?
* Explain length bias without using the word indolent. The roamer and the Snorlax are allowed.
* Distinguish a false positive from an overdiagnosed cancer, precisely.
* What pattern in incidence data suggests overdiagnosis, and what would argue against it?
* Why is removing a precursor lesion a fundamentally different claim from detecting disease
  earlier?
* Why are interval cancers partly a design consequence rather than purely a failure?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* Your national cancer screening programme's own published rationale, eligibility and
  benefits-and-harms information, issued by the body that runs it — the authority for who is
  invited, how often, and what harms the programme itself states.
* The national screening advisory body in your country, for the criteria it applies when deciding
  whether to recommend a programme at all.
* Your national cancer registry's published incidence and mortality series, which is the data in
  which the overdiagnosis signature described above is or is not visible.
* The systematic reviews maintained by the international evidence-synthesis collaborations, for
  the contested estimates in breast and prostate screening, read with their own stated
  limitations.
* A current epidemiology textbook, for the formal definitions of lead-time and length bias used
  above.

## Scope and safety

This is revision material about the epidemiology of screening, dressed in a game because the
game's encounter tables and detection rates are open to inspection in a way a programme's are not.
It has had no clinical review. No screening interval, age range, test performance figure or
eligibility rule appears here, and none should be inferred; screening programmes differ
substantially between countries and regions and they change, and your national programme's own
published information is the authority rather than this. Nothing here describes any individual's
situation, and nothing here is a reason for anybody to accept or decline a screening invitation —
that is a conversation with a clinician who knows the person's circumstances. Anyone affected by
cancer, their own or someone else's, should be talking to the team looking after that person. In
particular, nothing here can be applied to any individual's diagnosis: overdiagnosis is a
population-level excess and is not identifiable in a person. The analogy covers sampling and
detection and stops there: no part of it stands in for a person, and none of it says anything
about what happens to anybody.

## Where this stands, October 2026

The Pokémon facts are read from the games' own source. The Old Rod routine in Red and Blue sets
the bite flag unconditionally and returns a level 5 Magikarp; the Good Rod chooses between a
Goldeen and a Poliwag at level 10; the Super Rod indexes a per-map fishing group of up to four
species, and the Safari Zone group contains Dratini. Emerald's roamer is Latias or Latios
depending on which was seen on television, and its movement routine picks a new map within its
location set whenever the player changes maps, explicitly excluding the map it was on two moves
earlier. The Snorlax on Route 12 and Route 16 are scripted fixed encounters in Red and Blue.
Spinda has four spots, each placed from eight bits of its thirty-two-bit personality value, per
the comment in the drawing code. Emerald's shiny constant is 8 out of 65,536. The Lake of Rage
Gyarados, Sudowoodo and the sealed Regi chambers are described from working knowledge of those
games rather than from code opened here.

The clinical side: the three biases and the definition of overdiagnosis are long-standing,
formally defined and not in dispute, and the distinction between finding invasive disease earlier
and removing precursor lesions is the durable core of this answer. What is unsettled, and actively
argued, is the *magnitude* of overdiagnosis in particular programmes — breast and prostate above
all. What changes fastest is programme design: eligibility, modality, interval and whether a
programme exists at all vary by country and are revised regularly, often in response to exactly
this reasoning. No interval, age, test characteristic or survival figure is quoted, deliberately,
and the two historical examples are named by condition rather than by place or number because they
are the claims here that most need checking against a registry rather than against a revision note
like this one.
