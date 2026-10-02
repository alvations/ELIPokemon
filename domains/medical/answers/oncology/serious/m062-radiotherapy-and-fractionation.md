---
id: "m062"
slug: radiotherapy-and-fractionation
style: serious
category: oncology
difficulty: advanced
question: "What does ionising radiation actually do to a cell, and why is a course of radiotherapy divided into many small fractions instead of being given all at once?"
tags: [radiotherapy, fractionation, dna-damage, therapeutic-ratio, radiobiology]
---

# The lesion is a double-strand break, the kill is a proportion, and fractionation buys a gap

Radiotherapy works because ionising radiation damages DNA, because the lethal lesion is a
double-strand break that is not repaired or is repaired wrongly, and because the probability that
a given cell sustains one scales with dose. Everything else in the subject — why a course is
divided up, why overall time matters, why some adverse effects recover and others do not — is a
consequence of three further facts: the kill is **probabilistic**, the dose goes **only where the
beam goes**, and the tissue that limits the dose **repairs differently from the tumour**.

That last one is the whole argument for fractionation, and it is a statement about a *difference*
between two tissues, not about radiation being gentler in small amounts.

Each load-bearing claim below is marked with the kind of thing it is: **mechanism** (derivable
from the radiobiology), **definitional** (true because a convention says so), **consensus**
(widely agreed professional practice), or **country-dependent** (varies by nation, region or
institution, and changes).

## What the radiation does

Energy deposited in tissue ionises molecules along the track. Damage to DNA arises two ways
(**mechanism**):

* **Directly**, by ionisation within the DNA itself.
* **Indirectly**, by ionisation of water producing reactive species that then reach DNA. This
  route is the larger one for the photon beams in widest clinical use, and it is **oxygen
  dependent** — which is why the oxygen status of a cell changes how much a given dose achieves.

Single-strand breaks and base damage are repaired efficiently. The lesion that matters is the
**double-strand break**, and specifically the one that is not repaired or is misrepaired; a cell
carrying it typically dies when it next attempts division rather than immediately, which is why
radiation effects are expressed on the timescale of the tissue's own turnover rather than at once
(**mechanism**). Chromosomal rearrangement from misrepair is also the mechanistic basis of
radiation-associated second malignancy, which is a stochastic late effect rather than a
dose-threshold one (**consensus**).

Two properties follow immediately and are the ones most often stated loosely:

* **Cell kill is a proportion, not a number.** A dose increment removes a *fraction* of the
  surviving population, so survival falls multiplicatively. The curve approaches zero and does not
  reach it. A radical prescription is therefore chosen to achieve a high *probability* of control,
  never a certainty of it, and the honest statement of what a dose does is probabilistic
  (**mechanism**).
* **It is a local treatment.** The dose is deposited where the beam is, so radiotherapy addresses
  the volume treated and nothing outside it. This is the cleanest contrast with systemic therapy,
  and it is why a target volume is drawn, argued over, and recorded.

## Why the course is divided up

```
   ONE LARGE EXPOSURE                    THE SAME TOTAL, DIVIDED

   tumour     ████████████████  killed   tumour     ███████████████░  killed
                                                      ── nearly as much, because the
                                                         tumour repairs sublethal damage
                                                         LESS WELL between fractions

   late-                                  late-
   responding ████████████████  damaged   responding ██████░░░░░░░░░░  damaged
   normal                                 normal        ── MUCH LESS, because it repairs
   tissue                                 tissue           sublethal damage WELL, and
                                                            because it is disproportionately
                                                            sensitive to FRACTION SIZE

   ──────────────────────────────────────────────────────────────────────────────────────
   The gain is not that small doses are kinder.  It is that the GAP between
   fractions is worth more to one tissue than to the other.  Fractionation
   exploits a DIFFERENCE.  Where the difference is absent, it buys nothing.
   ──────────────────────────────────────────────────────────────────────────────────────

   AND FOUR THINGS HAPPEN IN THAT GAP, ON FOUR DIFFERENT TIMESCALES:

     REPAIR          hours        sublethal damage is repaired — and the
                                  dose-limiting late-responding tissue
                                  does this better than the tumour
     REDISTRIBUTION  hours        surviving cells move through the cell
                                  cycle, so the next fraction meets a
                                  population in more sensitive phases
     REOXYGENATION   days         as the tumour shrinks, previously
                                  hypoxic — and therefore relatively
                                  radioresistant — regions regain oxygen
     REPOPULATION    days–weeks   cells divide. This HELPS the normal
                                  tissue and HARMS control, which is why
                                  OVERALL TREATMENT TIME is a variable
                                  and an unplanned gap is a problem
```

The four processes are the classical account and they are not independent of one another
(**mechanism**, **consensus**). Three of them argue for spreading the dose out. The fourth argues
against spreading it out too far, and that is the tension every fractionation schedule is a
settlement of.

Two consequences are worth stating explicitly because they are what the schedule is for:

* **Late-responding normal tissue is disproportionately sensitive to the size of each fraction**,
  so reducing fraction size spares it more than it costs tumour control. This is the reason
  conventional radical courses are given in many small fractions (**mechanism**, **consensus**).
* **Where the tumour's fractionation sensitivity resembles that of the dose-limiting tissue, the
  argument weakens** — and in those settings fewer, larger fractions can give equivalent control
  with acceptable late effects. Which diseases those are, and what schedules are offered, is
  **consensus** in principle and firmly **country-dependent** in practice.

## Acute and late reactions are different phenomena

This distinction does more clinical work than any other in the subject (**mechanism**).

**Acute reactions** occur in rapidly renewing tissues — mucosa, skin, marrow where it is in the
field — because the dividing compartment is hit and the surface it supplies is then not replaced.
They appear during or shortly after the course, they track the overall intensity and the volume
treated, and they **recover**, because the progenitor compartment regenerates. The same turnover
argument that predicts cytotoxic toxicity predicts these.

**Late reactions** occur in slowly renewing or non-renewing tissue — fibrosis, vascular and
microvascular injury, neural injury — appear months to years afterwards, are governed strongly by
**fraction size** rather than by overall intensity, and largely do **not** recover
(**consensus**). They are what actually limits a radical dose, and they are why fraction size is
not a free parameter.

The practical reading: an acute reaction is managed and waited out; a late reaction is prevented
at the planning stage or not at all.

## The therapeutic ratio, and the two levers on it

Everything in radiotherapy is the ratio of effect on the target to effect on normal tissue, and
there are exactly two ways to improve it (**mechanism**):

* **Physically** — put less dose in normal tissue for the same dose in the target. This is what
  planning, immobilisation, image guidance, conformal and modulated delivery, brachytherapy and
  charged-particle beams are all for. The dose–volume relationship matters as much as the dose:
  the same dose to a small volume of an organ is a different proposition from the same dose to all
  of it.
* **Biologically** — exploit a difference between the target and the normal tissue. Fractionation
  is the oldest and most reliable such lever. Concurrent radiosensitising systemic therapy is
  another, and it works by widening the difference at the cost of adding toxicity (**consensus**,
  with **country-dependent** regimens).

Which is why "more dose" is never the whole answer and "less dose" is never a safe default.

## The human stakes, said plainly

Everything above is physics, repair kinetics and scheduling, and that is the right register for
understanding why a course looks the way it does. It is not the register for what a course is like
to go through.

A radical course means attending for treatment repeatedly over weeks, often while already
exhausted, often alongside other treatment, and often a long way from home. Acute reactions in a
treated field are painful and can interfere with eating, swallowing, washing and sleeping, and
calling them self-limiting is accurate and is not reassurance. Late effects are permanent, they
are the ones people live with for the rest of their lives, and the fact that they were weighed
carefully at planning does not make them smaller for the person who has them. Fertility, sexual
function, continence, lymphoedema, appearance and cognition are all in scope depending on the
site, and each of them is somebody's life rather than an entry in a constraint table.

The possibility of a radiation-associated second malignancy is also real, and it is a genuinely
difficult thing to hold alongside a treatment given with curative intent. None of the arithmetic
above says what will happen to any individual, and no figure of any kind appears in this answer
for that reason.

## What an examiner digs into next

* Why does a cell carrying an unrepaired double-strand break usually die at its next division
  rather than immediately, and what does that do to the timing of effects?
* Fractionation spares normal tissue. Spares it *relative to what*, and what happens to the
  argument if the tumour and the dose-limiting tissue have similar fractionation sensitivity?
* Three of the four Rs argue for prolonging a course and one argues against. Which, and why does
  that make overall treatment time a variable rather than an administrative detail?
* Why is an acute reaction managed and a late reaction prevented?
* Why does the indirect mechanism make oxygen status matter, and what does reoxygenation have to
  do with the schedule?
* Why is a radical dose a statement about probability rather than about certainty?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific to
this answer:

* A current standard textbook of radiobiology, for the damage mechanisms, the survival-curve
  argument, the four Rs and the fraction-size dependence of late-responding tissue. This is the
  authority for everything marked **mechanism** here.
* Your national or regional body for radiotherapy practice and its published dose-fractionation
  guidance, for which schedules are used for which indication where you work. These differ
  materially between countries.
* Your centre's own radiotherapy protocols and its normal-tissue dose constraints, which are the
  documents that bind local practice and which are the only place a constraint should be read
  from.
* The consensus normal-tissue tolerance literature your planning service works to, for the
  dose–volume relationships named in general terms above.
* The primary literature, for any claim about hypofractionation in a specific disease, which is an
  active area and is where practice has moved most in recent years.

## Scope and safety

This is revision material about radiobiology and schedule design, written for someone already
training in the field. It has had no clinical review. **No dose, fraction size, number of
fractions, fractionation-sensitivity value or normal-tissue constraint appears here, and none
should be inferred** — those belong to the protocol and the planning system, which are the
authority, and this is not. Fractionation schedules differ substantially between countries,
regions and centres and are revised; yours governs. Nothing here describes any individual's
treatment or situation, and nothing here is a guide to managing a reaction in a real person.
Anyone affected by cancer — their own diagnosis or someone else's — should be talking to the
clinical team looking after that person, who have the plan, the images and the history, none of
which are here. Anyone unwell during a course of treatment should use the acute oncology or
on-treatment review route their centre gave them rather than reading this.

## Where this stands, October 2026

The radiobiology is old and stable. The damage mechanisms, the primacy of the double-strand break,
the multiplicative survival argument, the four Rs and the greater fraction-size sensitivity of
late-responding tissue have been the standing account for decades and are the part of this answer
least likely to date.

What has moved, and is still moving, is the schedule. The direction of travel in several diseases
has been towards fewer and larger fractions where the biology allows, and towards tighter physical
conformality — image guidance, stereotactic delivery, and charged-particle beams where available.
Uptake is uneven between countries and between centres within a country, and availability rather
than evidence is often the determining factor. No schedule, dose or constraint is quoted here
deliberately: those are exactly the facts that date, and they belong to the protocol in force
where the reader works rather than to a revision note like this one.
