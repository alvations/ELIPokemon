---
id: "m006"
slug: pharmacokinetics-four-processes
style: serious
category: pharmacology
difficulty: advanced
question: "What do absorption, distribution, metabolism and excretion each contribute, and why are clearance, volume of distribution and half-life the three numbers that actually predict a drug's behaviour?"
tags: [pharmacokinetics, half-life, clearance, loading-dose, adme]
---

# Clearance and volume are the two facts. Half-life is what they produce.

Absorption, distribution, metabolism and excretion are the narrative. What you can actually reason
with is three numbers, and only two of them are independent: **clearance** (CL, the volume of
plasma irreversibly cleared of drug per unit time), **volume of distribution** (Vd, the apparent
volume the dose behaves as though it dissolved into), and the **half-life** those two produce.
Half-life is derived, not primary:

> t½ = ln2 × Vd / CL ≈ 0.693 × Vd / CL

That one line is why the three-number framing beats the four-process framing. If you know what
ageing, renal impairment, hepatic impairment or an interacting drug does to CL and Vd, you can
predict what happens to half-life, to the dosing interval, to time to steady state and to whether
a loading dose is worth giving. Reasoning the other way — from half-life back to mechanism —
fails, because two drugs with identical half-lives can have very different volumes and clearances
and behave nothing alike.

## What each of the four processes actually contributes

**Absorption** sets **bioavailability** (F): the fraction of an administered dose reaching the
systemic circulation. Intravenous administration is F = 1 by definition. Oral administration is
reduced by incomplete dissolution, incomplete uptake across the gut wall, and first-pass
extraction in gut wall and liver before the drug reaches the systemic circulation. *That is
mechanism, not guideline* — but the F of any particular formulation is a product-specific fact and
belongs to its summary of product characteristics.

**Distribution** sets **Vd**. It is an apparent volume, not an anatomical one: a drug heavily
taken up into tissue reports a Vd far larger than total body water, because Vd is defined as dose
divided by the plasma concentration that dose produces. Large Vd means plasma holds very little of
the drug at any moment — which is why haemodialysis is largely unhelpful for such drugs. Small Vd,
roughly extracellular-fluid-sized, is typical of water-soluble drugs that do not enter cells; the
aminoglycosides are the standard teaching example, and that they are both polar and renally
cleared is *consensus mechanism*, not a figure.

**Metabolism** mostly happens in the liver: phase I reactions (oxidation, largely by the
cytochrome P450 enzymes) and phase II conjugation (glucuronidation, sulfation, acetylation). Two
consequences matter more than the chemistry. A **prodrug** is inactive until metabolised, so
anything blocking the converting enzyme abolishes the effect rather than increasing it. An
**active metabolite** means the parent drug's half-life is not the duration of action.

**Excretion** removes drug unchanged, renally or in bile. Whether a drug is cleared renally
decides whether renal function changes the dose — and that is the question to ask first about any
unfamiliar drug.

Metabolism and excretion are different mechanisms that add into **one** number. Total clearance is
the sum of the organ clearances, and that additivity is why the three-number model works at all.

## The arithmetic that makes half-life useful

```
   t½ = 0.693 × Vd / CL

   ILLUSTRATIVE drug, round figures chosen to make the sum legible:
         Vd = 50 L        CL = 5 L/h
         t½ = 0.693 × 50 / 5  =  6.93 h      → call it 7 h

   half-lives     fraction LEFT after stopping     fraction of STEADY STATE reached
   ──────────────────────────────────────────────────────────────────────────────────
        1               1/2    =  50.0  %                     50.0  %
        2               1/4    =  25.0  %                     75.0  %
        3               1/8    =  12.5  %                     87.5  %
        4               1/16   =   6.25 %                     93.75 %
        5               1/32   =   3.1  %                     96.9  %   ◄── the "five"
        7               1/128  =   0.8  %                     99.2  %
   ──────────────────────────────────────────────────────────────────────────────────

   ONE table, read two ways. Washout and accumulation are the same arithmetic, because
   both are governed by the same first-order rate constant  k = 0.693 / t½.
```

Five half-lives is not a rule handed down; it is the point at which 1 − (1/2)ⁿ passes about 97%,
close enough to indistinguishable from steady state for most clinical purposes. Three half-lives
(87.5%) is often close enough to act on; seven (99.2%) is as close as anyone needs. Which you
choose depends on how steep the consequence of being 10% short is — a therapeutic-index question,
not a kinetic one.

## Why a loading dose exists, and when it does not

```
   target concentration  C = 10 mg/L     (ILLUSTRATIVE; a real target comes from the
                                          formulary and from the assay doing the measuring)

   loading dose      =  Vd × C / F   =  50 L  × 10 mg/L   =  500 mg    (F = 1)
                        ▲                                   ▲
                        VOLUME only                         fills the space

   maintenance rate  =  CL × C / F   =  5 L/h × 10 mg/L   =  50 mg/h   (F = 1)
                        ▲                                   ▲
                        CLEARANCE only                      replaces what is lost

   ┌──────────────────────────────────────────────────────────────────────────────┐
   │  no loading dose : C reaches 96.9 % of target after 5 × 7 h  ≈  35 h         │
   │  loading dose    : C is at target after one dose, then held at 50 mg/h       │
   └──────────────────────────────────────────────────────────────────────────────┘

   The two are computed from DIFFERENT numbers. Someone whose clearance is halved needs
   the SAME loading dose and HALF the maintenance rate. Getting that backwards is the
   most common pharmacokinetic error in an exam answer.
```

A loading dose exists for exactly one reason: steady state arrives on a timetable set by half-life
and nothing else, and sometimes that is slower than the clinical need. It is a standard approach
for drugs with a long half-life — digoxin and amiodarone are the two always named, and that they
are loaded *because* their half-lives are long is consensus, while any actual regimen is formulary
territory and differs between countries.

A loading dose is **not** used when: the half-life is short enough that steady state arrives
quickly anyway; the therapeutic index is narrow enough that overshooting is worse than waiting; Vd
is poorly known in the person in front of you, since the loading dose is computed from it; or the
effect is not driven by plasma concentration at all — an irreversible inhibitor's duration is set
by the turnover of the thing it inhibited, not by its own half-life.

## What moves the numbers

* **Renal impairment** reduces CL for renally cleared drugs, so half-life lengthens and the
  maintenance rate must fall. Whether dose or interval is adjusted is drug-specific.
* **Hepatic impairment** reduces metabolic CL, and may also reduce albumin, which changes binding
  and so Vd. Two effects, different directions, poorly predictable together.
* **Body composition** changes Vd without touching CL, and the direction depends on whether the
  drug distributes into water or into fat. This is why some drugs are dosed on total body weight,
  some on ideal body weight, and some flat.
* **Age** changes both, at both extremes of life, and not proportionally.
* **Saturable metabolism** breaks the model: once elimination is at capacity, clearance is no
  longer constant and half-life stops being a meaningful number. Phenytoin is the standard
  example, and that is mechanism rather than guideline.

## The human stakes, said plainly

The sections above are arithmetic. What the arithmetic is for is not.

Kinetics is where a great deal of avoidable harm in medicine actually happens. The people in whom
clearance is reduced or volume is altered — those with renal or hepatic impairment, the very old,
the very young, the very underweight or the critically ill — are the same people least able to
absorb a dosing error, and the error is usually a correct calculation applied to the wrong
assumption rather than a slip in the multiplication. Loading doses in particular are a recognised
source of serious harm, because they are large by design and because the arithmetic that produces
them depends on a volume nobody measured.

None of that is bad luck. A dosing error is something done to a person by a system, and the honest
name for it is iatrogenic harm. The equations above are a way of understanding why a dose is what
it is; they are not a calculator, and nothing in this answer should be used to work out an amount
for anyone. Anyone with a question about a medicine they are taking should raise it with their own
prescriber or pharmacist.

## What an examiner digs into next

* Why does a large Vd make dialysis unhelpful?
* Someone's clearance halves. What happens to the loading dose? (Nothing.)
* Why is half-life the wrong number to quote for an irreversible inhibitor?
* Given two concentrations, how would you tell saturable kinetics from an adherence problem?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

* Your national formulary's monograph for any drug named above — in the United Kingdom the British
  National Formulary, published by NICE with the pharmaceutical press; elsewhere the equivalent
  national formulary. Authority for every dose, interval and target concentration.
* The summary of product characteristics (European Union and United Kingdom) or the regulator-
  approved prescribing information (for example the label approved by the United States Food and
  Drug Administration) for the specific formulation. Authority for bioavailability, half-life and
  whether loading is part of the licensed approach.
* Your national formulary's guidance on prescribing in renal impairment and in hepatic impairment.
* A standard clinical pharmacology textbook for the derivation of the first-order equations above.
  The algebra is checkable from first principles and needs no citation to be verified.
* Your local therapeutic drug monitoring service or laboratory handbook for assay-specific
  reference ranges and sampling times, which differ between laboratories and between countries.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **Every number above is either an illustrative round figure chosen to make
the arithmetic legible, or a general principle.** None is a dose, a target or a threshold for any
person. Practice differs between countries and between formularies, and where it does this answer
says so rather than picking one. Nothing here should be used to make a decision about anyone's
treatment, including your own; the formulary, the product information and local guidance are the
authority. Anyone with a question about a medicine they are taking should raise it with their own
prescriber or pharmacist.

## Where this stands, October 2026

The equations above are definitions and algebra, and they do not date. What dates is everything
attached to a particular drug: licensed indications, target concentrations, renal dosing tables
and whether loading is recommended at all. All of that moves, and it moves at different times in
different countries. Check the current formulary.
