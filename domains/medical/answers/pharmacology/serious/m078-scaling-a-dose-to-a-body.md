---
id: "m078"
slug: scaling-a-dose-to-a-body
style: serious
category: pharmacology
difficulty: intermediate
question: "Why are some doses flat, some scaled by body weight, some by body surface area and some by organ function, and why is none of those scalings the whole answer?"
tags: [dose-scaling, allometry, body-surface-area, organ-function, calculation-error]
---

# Every scaling rule is a proxy for clearance and volume. The argument is about the proxy.

A dose is not the thing you want. What you want is an **exposure** — a concentration, or an area
under a concentration–time curve — and through that an effect. `m006` establishes that exposure is
governed by exactly two quantities: **volume of distribution**, which sets what a single dose does
to the concentration, and **clearance**, which sets what a repeated dose settles at.

Neither of those can be measured at the bedside. So every dosing rule in existence picks a body
measurement that correlates with one of them and uses it as a stand-in. Weight, surface area,
estimated renal function, age, a fixed number: all four scalings and the refusal to scale are the
same kind of move. The only question is which proxy tracks the quantity you need, for this drug,
across the range of bodies you will actually meet.

Claims below are marked inline with what they rest on: (**mechanism**), (**definitional**),
(**consensus**), or (**country-dependent**).

## Two quantities, so potentially two different scalings for one drug

```
   SINGLE DOSE                            REPEATED DOSING
   ─────────────────────────────          ───────────────────────────────────
   ΔC  =  dose / V                        C(steady state)  =  dose rate / CL

   governed by VOLUME                     governed by CLEARANCE
   tracks body SIZE and composition       tracks ORGAN FUNCTION
   (where does the drug go, and is        (how fast is it got rid of, and by
    that space fat, water or protein?)     which organ?)

   CONSEQUENCE, and it is the most useful sentence in the topic:

     a LOADING dose and a MAINTENANCE dose can correctly scale on DIFFERENT
     body measurements, in the same person, on the same day.

     Loading is a volume problem: the big person needs more to fill the space,
     whatever their kidneys are doing.
     Maintenance is a clearance problem: the person with poor renal function
     needs less per day, whatever they weigh.

   Collapsing the two into one "dose adjusted for the patient" is how a correct
   loading dose gets reduced for renal impairment -- an error of exactly the
   right shape to under-treat someone at the start and then get the rest right.
```

That is (**mechanism**), and it does not depend on any particular drug.

## Flat dosing, which is the default and is usually right

Most medicines are given at a fixed dose to adults of every size, and this is not an oversight. It
is correct whenever the exposure–response relationship is flat enough over the exposure range the
population's bodies actually produce. If a three-fold spread in weight produces a spread of
exposure that still sits inside the useful range, precision buys nothing and costs something.

What it costs is the real argument, and it is a safety argument rather than a convenience one.
**Every calculation step is an opportunity for an error of a factor of ten** (**consensus**). A
flat dose has no steps. A weight-based dose has a weight to obtain, a unit to get right, a
multiplication to perform, a volume to work back to from a concentration, and a measuring device
to read. Each of those has a documented failure mode, and the magnitude of the resulting error is
not proportional to the mistake — a misplaced decimal is a ten-fold error regardless of how small
the slip was.

So the honest hierarchy is: scale only when the gain in precision is worth the added steps, and
when you do scale, remove the steps by engineering rather than by care. `m044`'s wrong-route
section is the same argument applied to a different error.

## Weight, and the assumption hidden inside milligrams per kilogram

Dosing per kilogram asserts that the quantity you need is **proportional to mass**. For clearance
that is false, and it is false in a direction that matters.

```
   CLEARANCE against MASS -- the shape, not any drug's numbers

     CL │                                   ╭──────────  proportional (∝ mass)
        │                            ╭──────╯
        │                     ╭──────╯   ╭───────────── observed: ∝ mass^b, b < 1
        │              ╭──────╯  ╭───────╯
        │        ╭─────╯ ╭───────╯
        │   ╭────╯╭──────╯
        └───┴─────┴────────────────────────────────────▶ body mass
            ▲                            ▲
        small body:                  large body:
        proportional scaling          proportional scaling
        UNDER-estimates clearance     OVER-estimates clearance
        (so mg/kg under-doses)        (so mg/kg over-doses)

   The exponent b is conventionally taken as about three quarters in population
   pharmacokinetic modelling. Treat that as a MODELLING CONVENTION with empirical
   support rather than as a measured constant for any individual drug -- the value,
   and whether a single exponent should be used at all, are argued about in the
   primary literature.
```

A second problem sits on top of that one: **"weight" is not one variable** (**consensus**). A drug
that distributes into adipose tissue has a volume that tracks total body weight; a drug that stays
in lean tissue and water does not, and for such drugs an ideal or adjusted body weight is used
instead. Which weight descriptor a given drug uses is drug-specific and is in the product's own
information, not derivable from first principles.

## Surface area, and the arithmetic reason it differs from weight

Body surface area is computed from height and weight by one of several published formulas, which
agree in the middle of the range and disagree at the extremes (**consensus**). Its persistence is
mostly historical: it was the scaling used to translate doses between species in early toxicology,
and for cytotoxic drugs it tracked marrow toxicity better than mass did.

But the reason it gives *systematically different answers* from weight is pure geometry, and it is
worth being able to derive on demand:

```
   Take a body and double every linear dimension.

      length   ×2
      AREA     ×4        (length²)
      MASS     ×8        (length³)

   So area / mass  is HALVED. The small body has more surface per kilogram.

   DOSE PER UNIT AREA therefore gives the small body MORE PER KILOGRAM than the
   large one, and dose per kilogram gives it less. The two rules do not merely
   differ by a constant -- they diverge in opposite directions as size changes,
   and they cross somewhere in the middle of the population.

   Note also what surface area is: a function of height AND weight. Weight-based
   dosing throws the height away. Whether that is a loss depends entirely on
   whether the quantity you need correlates with the discarded dimension.
```

Surface area is also widely criticised, and the criticism is specific: for many cytotoxic drugs it
explains only a small part of the between-person variation in clearance, so it adds calculation
steps and a false air of individualisation without much precision (**consensus**). It nonetheless
remains the convention for much of cytotoxic chemotherapy, because displacing a dosing convention
for drugs with narrow margins requires evidence that the replacement is better — and where that
evidence has been produced, conventions have changed, several therapeutic antibodies having moved
to flat dosing on exactly that basis (**country-dependent**).

## Organ function, which is not a size at all

The third scaling drops the body-measurement idea entirely and estimates the eliminating organ's
capacity.

* **Renal.** Where a drug is cleared by the kidney, an estimate of filtration is a far better
  proxy for its clearance than any measure of size. One trap here is almost universal and worth
  stating: estimated glomerular filtration rate is routinely reported **indexed to a standard body
  surface area**, so that it compares like with like for staging kidney disease — and for drug
  dosing what is wanted is the person's **absolute** clearance, un-indexed. Using the indexed
  figure for dosing misestimates it in bodies far from average size, in the direction of their
  deviation (**consensus**). The laboratory report prints which it is giving you; which estimating
  equation is used, and how the un-indexed figure is obtained, is (**country-dependent**).
* **Hepatic.** There is no single number of the same kind, which is the whole of `m042`'s
  argument: the liver does several separable jobs that fail at different rates, so hepatic dosing
  advice is categorical rather than continuous and is drug-by-drug.

## Why none of them is the whole answer

Five reasons, and each points at a different section above.

1. **A scaling addresses exposure, not response.** If the variability is in the target rather than
   in the kinetics, no dose rule reaches it. `m077` is the sign-flip version of this.
2. **The right exposure depends on what you are treating.** One drug can correctly carry two
   different dose rules for two indications, which means the question "what is the dose" is
   under-specified until the indication is named (**mechanism**).
3. **Every proxy degrades at the extremes of body composition** — and extremes are
   over-represented among the people who need the drug, which is the worst possible place for a
   proxy to be weakest.
4. **A proxy is only as good as its correlation with clearance for that drug**, and that
   correlation is a property of the drug and not of the scaling. There is no such thing as a drug
   being "correctly dosed by surface area" in the abstract.
5. **The scaling chooses the first dose, not the dose.** After that you observe: the effect where
   it is measurable, the concentration where it is worth measuring under the five conditions
   `m041` sets out, and the toxicity either way. A scaling rule is a prior. Treating it as the
   answer is the mistake this whole topic exists to prevent.

## The human stakes, said plainly

The dominant mechanism of serious harm in this topic is not a mis-chosen scaling. It is
**arithmetic**.

Weight-based and area-based regimens require a measurement to be obtained, recorded in the right
units, multiplied, converted from a mass to a volume of a particular concentration, and then
measured out. Every one of those steps has produced documented ten-fold errors, and the three
recurring ones are a decimal point, a unit confusion, and a weight that was estimated or
remembered rather than measured. The error is not proportional to the slip: there is no such thing
as a small decimal-point mistake.

The response that has worked has not been to ask people to check more carefully. It has been to
remove the arithmetic from the point of care — pre-calculated dosing charts, dose banding,
standardised infusion concentrations, ready-to-administer preparations, independent double-checks
built into the task rather than requested, and prescribing systems that refuse an implausible
figure. That is the same engineering answer `m044` describes for wrong-route errors, and it is
correct for the same reason: the error is rare, catastrophic and not a failure of diligence.

It is also worth naming where this falls. Weight-based and area-based dosing is concentrated in
paediatric practice and in oncology, and so, therefore, is the engineering. That is not a comment
about any patient group; it is a statement about where the arithmetic lives and where the
safeguards consequently have to be built.

Nothing in this answer provides a dose, a scaling rule for any drug, or a weight descriptor for
any product. Those are in the formulary, in the product's own information and in your local
paediatric or chemotherapy dosing reference, and those documents are the authority. Anyone with a
question about a dose they have been given should ask their prescriber or pharmacist, who can
check it against the product information in a few seconds.

## What an examiner digs into next

* Which of volume and clearance governs a loading dose, and what does that imply about reducing a
  loading dose for renal impairment?
* Double every linear dimension of a body. What happens to the ratio of surface area to mass, and
  what does that do to the two dosing rules?
* Why does milligrams per kilogram over-dose the large and under-dose the small, relative to
  observed clearance?
* An estimated filtration rate comes back indexed to a standard surface area. Why is that the
  wrong figure for dosing, and in which direction does it err?
* Give three reasons surface-area dosing is criticised and one reason it has not been abandoned.
* Why is "scale only when the precision is worth the steps" a safety argument rather than a
  convenience one?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer:

* **The product's own approved prescribing information**, for the dose, the scaling rule, and
  crucially *which weight descriptor* it uses — total, ideal, adjusted or lean. That is a
  product-level fact and is not derivable.
* **Your national paediatric formulary or children's dosing reference**, which exists separately
  from the adult formulary in several countries precisely because weight-based dosing needs its
  own apparatus. It is the authority for anything in that territory and this answer is not.
* **Your institution's injectable medicines guide and its chemotherapy dosing and dose-banding
  policy**, for standardised concentrations, banding tables and the required checks. These are
  local, they override general advice, and they are what you will be held to.
* **Your national renal association's or laboratory network's guidance on reporting and using
  estimated glomerular filtration rate**, for the indexed-against-absolute distinction, for which
  estimating equation is in use, and for how the absolute figure should be obtained. This differs
  by country and has been revised.
* **A current clinical pharmacokinetics textbook's chapter on dose individualisation and
  allometry**, for the scaling exponent, the derivation of the area-to-mass relationship, and the
  distinction between size and function as scaling variables.
* **The primary literature**, for the surface-area controversy in cytotoxic dosing, for the
  evidence behind flat dosing of therapeutic antibodies, and for the value and applicability of
  any allometric exponent. All three are contested and this answer states no figures from them.
* **Your national patient-safety body's alerts** on dose calculation errors and on paediatric
  dosing, for what has actually gone wrong and what was changed in response.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **It contains no doses and no dosing rule for any drug.** The only numbers
in it are the geometric ones — doubling a linear dimension multiplies area by four and mass by
eight — and a named modelling convention that is explicitly flagged as a convention rather than a
measurement. Nothing here indicates how any medicine should be dosed for anyone, and in particular
nothing here is a paediatric dosing method: that territory has its own reference works and they
are the authority. Anyone with a question about a dose they have been given should ask their
prescriber or pharmacist rather than work it out from anything on this page.

## Where this stands, October 2026

The mechanism — exposure as the target, volume and clearance as the two quantities, the geometry
of area against mass, and function rather than size as the better proxy for an eliminating organ —
is mechanism and does not date. Three things do. The **allometric exponent**, and whether a single
exponent is the right model at all, remains argued in the population pharmacokinetics literature.
The **surface-area convention in cytotoxic dosing** is under active challenge and has already been
displaced for several products, so which drugs are dosed which way is a moving list. And the
**reporting and estimating of renal function** has changed in several countries within the last
few years, including which equation is used and what variables it includes, which directly changes
the figure a dosing decision is based on. Check the product information, your paediatric or
chemotherapy dosing reference, and your own laboratory's reporting convention.
