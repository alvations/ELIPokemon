---
id: "m044"
slug: formulation-and-route
style: serious
category: pharmacology
difficulty: intermediate
question: "Why does the same drug behave differently by route, and what does a modified-release preparation actually modify?"
tags: [route-of-administration, bioavailability, modified-release, first-pass, dose-dumping]
---

# A route sets how much arrives and how fast. Modified release changes only the rate of input.

The active moiety is identical. What a route and a formulation control is exactly three things:
the **fraction** that reaches the systemic circulation (bioavailability, F), the **rate** at which
it gets there (which sets the peak concentration and the time to it), and the **barriers** it
crosses on the way (which is what determines the first two). Every fact in this topic is one of
those three, and nothing in it changes clearance, elimination half-life or the drug's intrinsic
activity.

Say that last part out loud, because it is the sentence that makes modified release make sense: a
modified-release tablet does **not** change how fast the body gets rid of the drug. It changes how
fast the drug goes in. The two are different processes and the formulation only touches one of
them.

Claims are marked **[M]** mechanism, **[D]** definitional, **[C]** consensus, or **[L]** local.

## Route by route, in terms of fraction and rate

```
   route            F                          rate of input            first pass?
   ──────────────────────────────────────────────────────────────────────────────────────
   intravenous      1, BY DEFINITION           yours to choose          bypassed
                    (not "high" -- F = 1 is
                     what defines the term)
   oral             variable: dissolution,     slow, and food-          FULL gut wall
                    gut-wall and hepatic        dependent               AND liver
                    extraction, transit
   sublingual       higher for high-           fast                     bypassed: venous
   / buccal         extraction drugs                                    drainage avoids
                                                                        the portal vein
   rectal           partial and variable       moderate                 PARTIAL -- mixed
                                                                        venous drainage
   transdermal      low per unit area but      very slow, and a skin    bypassed
                    sustained                   depot keeps delivering
                                                AFTER removal
   inhaled          large absorptive area;     fast where systemic      bypassed
                    usually chosen for LOCAL   arrival is wanted
                    delivery with a small
                    systemic fraction
   intramuscular    usually near-complete      a depot: rate depends    bypassed
   / subcutaneous                               on PERFUSION, so it is
                                                unreliable in shock
   intrathecal      the route exists because   immediate, at the site   bypassed and
                    the barrier excludes the                            irrelevant
                    drug by another route
   ──────────────────────────────────────────────────────────────────────────────────────

   Read the table as three columns of consequence, not eight routes to memorise:
     · an F column that explains which routes are interchangeable and which are not;
     · a rate column that explains onset, and why a depot fails in a shocked patient;
     · a first-pass column that explains why liver disease moves the ORAL dose only.
```

Two of those rows carry most of the clinical weight.

**Intramuscular and subcutaneous absorption depends on perfusion.** In shock, peripheral perfusion
falls, so the depot is not absorbed and the drug is not where you think it is — and when perfusion
is restored the accumulated depot arrives at once. That is why the intravenous route is used when
the situation is unstable, and it is a mechanism rather than a preference **[M]**.

**Intrathecal doses are orders of magnitude smaller than systemic ones**, because the compartment
is small and the drug was given by that route precisely to avoid dilution in the body. A systemic
dose given intrathecally is therefore catastrophic, and the never-event status of that error in
several countries is the reason the route carries distinct labelling and distinct checking
procedures **[C]**, which are local and absolute **[L]**.

## First pass, and the one piece of algebra worth memorising

```
   F  =  f(absorbed)  ×  ( 1 − E )          E = the EXTRACTION RATIO of gut wall + liver

   ILLUSTRATIVE round figures:

   HIGH-extraction drug      E = 0.9   →   F = 0.10   so the oral dose must be about
                                                      ten times the intravenous one
   LOW-extraction drug       E = 0.1   →   F = 0.90   oral and intravenous doses are
                                                      nearly the same

   NOW DISTURB IT. Halve E in each case:

   high-extraction    E 0.9 → 0.45   F 0.10 → 0.55     5.5× the exposure
   low-extraction     E 0.1 → 0.05   F 0.90 → 0.95     1.06× the exposure
                                                        ▲
                     The SENSITIVITY to anything that disturbs first pass is a
                     property of E. The same liver disease, the same interacting
                     drug, the same grapefruit: enormous for one drug, invisible
                     for the other, and it is the extraction ratio that tells you
                     which. m042 is the impairment half of this.
```

A high extraction ratio also means a **variable** F, because a small change in a large extraction
produces a large change in the small remainder. That variability is why some drugs are available
only as injections, and why two oral products of the same high-extraction drug are harder to show
equivalent **[M]**.

## What modified release actually modifies

The vocabulary first, because the terms are used loosely and they mean different things **[D]**:

* **Delayed release** — an enteric coat that withholds release until the pH rises past the
  stomach. It changes **when** release begins. It does not change how much is released or over how
  long. Its purposes are to protect an acid-labile drug from the stomach, or to protect the
  stomach from the drug, or to deliver to the colon.
* **Extended, sustained, prolonged or controlled release** — the input is spread over hours. It
  changes the **rate**.
* **Modified release** — the umbrella term covering both.

And here is what it does to the curve:

```
   SAME DOSE, SAME DRUG, SAME CLEARANCE. Only the input rate differs.

   C │      ╭╮                       ◄── immediate release: high peak, deep trough
     │     ╱  ╲         ╭╮
  ───┼────╱────╲───────╱──╲─────────────── upper edge of the useful range
     │   ╱      ╲     ╱    ╲
     │  ╱  ╭─────────────────╮        ◄── modified release: flatter, same area
     │ ╱  ╱     ╲   ╱         ╲──╮
  ───┼╱──╱───────╲─╱─────────────╲──────── lower edge of the useful range
     │  ╱         ╲               ╲
     └────────────────────────────────────────────────► time

   WHAT CHANGED          WHAT DID NOT CHANGE
   ──────────────────    ─────────────────────────────────────────────
   peak: LOWER           total exposure (area under the curve), in a
   time to peak: LATER   well-designed product
   trough: HIGHER        clearance
   doses per day: FEWER  elimination half-life
                         the drug's intrinsic activity
```

Three consequences follow, and they are the reason anyone bothers:

1. **Fewer doses a day**, which is an adherence intervention that works on mechanism rather than
   on motivation — `m043` has the arithmetic.
2. **A flatter profile**, so fewer peak-related adverse effects and fewer trough-related failures.
   For a drug whose adverse effect tracks the peak, that is the whole point of the product.
3. **A longer apparent half-life** — and this one is a trap. If absorption is slower than
   elimination, the decline you observe after the last dose is the **absorption** rate, not the
   elimination rate. The terminal slope you measure belongs to the formulation, not to the drug.
   That is the "flip-flop" situation, and it means the half-life quoted for a modified-release
   product is not the drug's half-life **[M]**.

## Why these products are not crushed, split or chewed

The rate-controlling mechanism **is the dosage form** — a matrix, a membrane, a coated pellet, an
osmotic pump. Destroy it mechanically and the whole dose becomes immediately available: **dose
dumping**, which converts a day's exposure into a single peak. For a drug with a narrow margin
that is a toxic dose administered correctly in every respect except the one that mattered **[C]**.

Two corollaries that follow from the same fact:

* **Modified-release products of the same drug are not assumed interchangeable with each other.**
  They release by different mechanisms over different profiles, so bioequivalence must be shown
  for the specific pair rather than inferred from the shared active ingredient. Some products are
  therefore prescribed and dispensed **by brand**, and which ones is a regulatory decision that
  differs by country **[L]**.
* **For a narrow-index drug, the standard bioequivalence acceptance limits may not be narrow
  enough**, which is why several regulators apply tighter criteria to those products. The limits
  themselves are regulator property and this answer does not state them; `m008` is the index half
  of the argument.

A drug that cannot be swallowed whole therefore needs a **different preparation**, not a modified
one — a liquid, a dispersible form, a patch, an injection — and finding that preparation is a
formulation problem with a formulation answer.

## The human stakes, said plainly

Two of the errors described above are among the most serious in medicine, and they should be named
without ornament.

A **wrong-route administration** — something intended for a vein given into the spinal fluid, or
the reverse — has killed people, repeatedly, in several countries. The response has not been to
ask people to be more careful. It has been to change the physical design: distinct connectors,
distinct labelling, distinct storage, mandatory independent checks, and in some systems removing
the possibility of the two ever being in the same room. That is the correct response to an error
that is catastrophic and rare: engineer it out rather than exhort against it.

**Dose dumping** from a crushed modified-release tablet is the quieter one, and it happens for
sympathetic reasons — someone cannot swallow, a tube needs to be used, the tablet is halved to get
a smaller dose. The person doing it is almost always trying to help.

In both cases the harm was caused by the care rather than by the illness, and the honest word is
iatrogenic. Naming it that way is what makes it reportable, auditable and preventable, and it
locates the fault in a system that allowed the substitution rather than in whoever was holding the
pot.

Nothing in this answer should be used to decide whether any particular preparation can be crushed,
split, or given by any route. That information is product-specific, it is in the product's own
documentation, and a pharmacist can answer it in a sentence. Anyone who cannot swallow a medicine
they have been given should ask their prescriber or pharmacist rather than modify it.

## What an examiner digs into next

* Why is intravenous bioavailability 1 by definition rather than by measurement?
* Two drugs, extraction ratios of 0.9 and 0.1. Which one does liver disease move, and by how much?
* A modified-release product's quoted half-life is longer than the drug's. Explain, without saying
  the drug changed.
* Why is an intramuscular dose unreliable in shock, and what happens when perfusion returns?
* Why can two modified-release products of the same drug not be assumed interchangeable?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer:

* **The summary of product characteristics or regulator-approved prescribing information** for the
  specific product. It is the only authority for that product's bioavailability, its release
  mechanism, whether it may be crushed or halved, and which routes it is licensed for. A general
  rule about "modified-release tablets" is not a statement about the one in your hand.
* **A specialist reference on administering medicines to patients who cannot swallow**, or your
  institution's equivalent. Several countries maintain one; it is the document that answers the
  crushing question properly.
* **Your national medicines regulator's bioequivalence guidance**, for the acceptance criteria,
  for the tighter criteria applied to narrow therapeutic index products, and for which products
  must be prescribed by brand. Country-specific.
* **Your institution's injectable medicines policy and its policy on intrathecal administration.**
  The latter is typically mandatory, separately audited, and not negotiable locally.
* **Your national patient-safety body's alerts** on wrong-route administration, for what has
  actually gone wrong and what was changed in response.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **Every number in this answer is an illustrative round figure** chosen to
make the extraction-ratio and release-profile arithmetic legible; none is a real product's
bioavailability, dose, or bioequivalence limit. In particular, nothing here indicates whether any
specific preparation can be crushed, split, dispersed or given by a different route — that is
product-specific information held in the product's own documentation, and a pharmacist is the
fastest route to it. Nothing here should be used to make a decision about anyone's treatment,
including your own. Anyone who cannot swallow a medicine should ask their prescriber or pharmacist
rather than alter it.

## Where this stands, October 2026

The three-variable framing — fraction, rate, barrier — is mechanism and does not date, and the
extraction-ratio algebra is a definition. What dates is everything product-specific and everything
regulatory: which products exist in which release forms, which must be prescribed by brand, what
the bioequivalence acceptance criteria are and which products attract the tighter ones, and the
device-standard changes that have been introduced in several countries to engineer out wrong-route
connections. Those are regulator and national-safety-body decisions, they differ between
countries, and they change. Check the current product information and your own regulator.
