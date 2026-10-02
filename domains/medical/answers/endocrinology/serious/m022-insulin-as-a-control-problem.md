---
id: "m022"
slug: insulin-as-a-control-problem
style: serious
category: endocrinology
difficulty: advanced
question: "Why is replacing insulin with injections intrinsically hard, and what do basal and bolus each do?"
tags: [insulin, basal-bolus, feedback, control-lag, hypoglycaemia]
---

# A closed loop with a lag of seconds, replaced by an open loop with a lag of hours

Endogenous insulin is a closed-loop controller whose sensor and actuator are the same cell.
Glucose enters the beta cell, is phosphorylated, and the resulting rise in the ATP-to-ADP ratio
closes an ATP-sensitive potassium channel; the cell depolarises, calcium enters, and stored
granules are released *(mechanism)*. Sensing, deciding and acting happen in one place,
continuously, in seconds. Replacement therapy keeps none of that. It is open-loop: the dose is
decided before the disturbance is known, delivered into a compartment the hormone was never meant
to enter, and once given it cannot be retrieved. That is the whole difficulty, and it is a control
problem before it is a pharmacology problem.

Claims below are marked *(mechanism)*, *(consensus)* or *(guideline-dependent)* where the basis is
load-bearing.

## The physiological pattern, and why it has that shape

Secretion has two components because the demands are two. Between meals and overnight a low,
continuous output holds hepatic glucose production and lipolysis in check — the **basal**
function, whose job is suppression rather than disposal *(mechanism)*. After a meal, a sharp rise
is needed to dispose of an absorbed load, and the response is biphasic: a rapid first phase from
granules already docked, then a sustained second phase from new synthesis and recruitment
*(consensus)*. That first phase exists precisely because of the lag — pre-made granules are the
only way to act faster than synthesis allows.

Two features of the natural route have no counterpart in an injection. Secretion is into the
portal vein, so the liver sees a far higher concentration than the periphery and extracts a large
fraction on first pass *(mechanism)*. And the response is amplified by gut-derived incretin
hormones, so an oral glucose load provokes more insulin than the same load given intravenously
*(consensus)*. Subcutaneous delivery abolishes the hepatic gradient and bypasses the incretin arm
entirely: the periphery is over-exposed relative to the liver, which is a structural difference,
not a dosing error.

## Where the lag enters, drawn to scale

```
   CLOSED LOOP (intact beta cell)
   ─────────────────────────────
   glucose ↑ ──► sensed ──► granules released ──► portal vein ──► liver, then periphery
      ▲           seconds        seconds              immediate        minutes
      │                                                                  │
      └──────────────── glucose ↓, secretion falls off ◄─────────────────┘
                        correction begins while the rise is still happening

   OPEN LOOP (subcutaneous replacement)
   ────────────────────────────────────
   decision ──► injection ──► subcutaneous depot ──► absorption ──► systemic ──► effect
      │            now         tens of minutes       variable       no portal     hours
      │                                                             gradient
      │                        ╎
      │                        ╎ ◄── the depot is now committed; nothing recalls it
      ▼
   measurement ◄──── sampled intermittently, and indirectly ────────────────┘

   timeline of one meal
   ─────────────────────
   food         ████████
   glucose          ▁▂▄▆███▇▅▃▂▁
   endogenous    ▁▃▆███▆▄▂▁                ← starts before the peak
   injected              ▁▂▄▆███▇▅▃▂▁▁▁    ← starts after it, and finishes later
                 ╰──────╯          ╰────╯
                  glucose rises     insulin still acting with
                  unopposed         nothing left to act on
```

The two bracketed regions are the entire clinical problem. The left one is post-meal
hyperglycaemia. The right one is the risk of glucose falling too low later, because the actuator
outlasts the disturbance *(mechanism)*. Both are consequences of dead time, not of carelessness.

## Why open-loop control of this particular variable is hard

1. **Dead time with an irreversible actuator.** Any controller with delay must predict. A
   controller that cannot withdraw its last action must predict *and* be conservative, because
   overshoot cannot be undone *(mechanism)*.
2. **The disturbances are unmeasured.** Exercise — during and for many hours afterwards — illness,
   infection, stress, sleep, alcohol, the rate of gastric emptying, hormonal cycles, injection
   site, local temperature and massage of the site all alter either the demand or the absorption
   *(consensus)*. A controller blind to its disturbances cannot be tight.
3. **The cost function is asymmetric.** Running high does harm slowly, over years. Running low
   does harm in minutes, and severe hypoglycaemia can cause seizure, loss of consciousness and
   death *(consensus)*. A rational controller facing that asymmetry biases upward, and accepts
   worse average control to avoid the fast failure *(mechanism)*.
4. **The opposing arm of the loop is also damaged.** In long-standing type 1 the glucagon response
   to falling glucose is lost and adrenergic warning symptoms blunt, a state called impaired
   awareness of hypoglycaemia *(consensus)*. Repeated lows lower the threshold at which warning
   appears, so the system that should rescue an overshoot degrades with each overshoot — a
   positive feedback loop layered on top of a broken negative one.
5. **The measurement is not the controlled variable.** Sensors report interstitial glucose, which
   trails plasma glucose during rapid change *(mechanism)*. Controlling a lagged estimate of a
   variable through a lagged actuator is the textbook recipe for oscillation.

## What basal and bolus actually are

They are not two sizes of the same thing; they do different jobs. Basal replacement substitutes
for the suppressive background, and should ideally be flat and uneventful, so that between meals
and overnight glucose neither climbs nor falls *(mechanism)*. Bolus replacement substitutes for
the prandial surge, and must be matched in both size and timing to an absorption curve nobody can
measure directly *(mechanism)*. Getting a basal wrong shows as drift when nothing is happening;
getting a bolus wrong shows as a spike or a fall tied to a meal. Distinguishing the two from a
glucose record is the main diagnostic skill in this area, and the reason records are reviewed by
period rather than as a daily average.

Automated insulin delivery closes part of the loop — sensor to algorithm to pump — and measurably
improves time spent in range *(consensus)*. It does not remove the lag. The algorithm still acts
through a subcutaneous depot, so it cannot respond faster than the insulin can, which is why
announcing meals still helps and why the remaining failures cluster around rapid change
*(mechanism)*.

## The human stakes, said plainly

The control problem above is an abstraction. The cost of it is not.

Hypoglycaemia is the limiting factor in insulin therapy, and it is the reason the loop is run
deliberately loose. Mild episodes are unpleasant, disruptive and frightening. Severe episodes
cause seizure, loss of consciousness and death. Impaired awareness of hypoglycaemia removes the
warning that would otherwise allow self-rescue, and it is caused by the thing it makes more
dangerous. Fear of hypoglycaemia is therefore a rational response to a real hazard, not
non-adherence, and it is routinely recorded as the latter.

The daily burden is the part a control diagram hides. Replacing a continuously regulated hormone
by hand means dozens of decisions a day, every day, with no days off, under an asymmetric penalty
and with disturbances nobody can measure. Numbers that look poor on a printout are usually not a
failure of effort. The problem is, in the strict sense described above, not solvable with the
available actuator — and a person who has been managing it for twenty years has been doing
something genuinely difficult for twenty years.

A note about who is reading. Someone reading about insulin is more likely to be living with it
than revising it. If that is you: nothing on this page is about your regimen, there are
deliberately no doses or ratios here, and the only people who can change anything about it are you
together with your own clinical team. If hypoglycaemia is happening now, treat it the way your own
team has agreed with you, and if someone cannot be roused, call emergency services.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md).
Specific to this answer:

* Your national formulary — in the United Kingdom the British National Formulary, elsewhere the
  equivalent national formulary — for every insulin preparation's onset, profile and duration, and
  for the warnings attached to each. This is the authority on anything quantitative about insulin.
* The summary of product characteristics, or the equivalent approved product information, for the
  specific preparation in question.
* Your national diabetes guideline's sections on insulin therapy in type 1 diabetes and on
  hypoglycaemia, from the body that issues it.
* Your local hospital's or trust's insulin safety policy and its insulin prescription chart
  guidance, which is what governs practice at the bedside.
* A diabetes or endocrinology textbook chapter on beta-cell secretory physiology, the incretin
  effect and first-pass hepatic extraction.
* The consensus statements of the Advanced Technologies and Treatments for Diabetes meetings, for
  how continuous-glucose metrics and automated delivery are currently assessed.

## Scope and safety

This explains why insulin replacement is a hard control problem. It is not a guide to giving
insulin, and it is not about any individual's care. **It contains no doses, no ratios, no
correction factors and no rates, and that is deliberate** — nothing here should permit a dose to
be calculated, and a number that looked helpful would be the most dangerous thing on the page.
Insulin is a high-risk medicine; the formulary, the product information and local insulin safety
policy are the authorities. Nothing here has had clinical review. If someone is unwell now, or if
hypoglycaemia is suspected and they cannot be roused, contact local emergency services.

## What an examiner digs into next

* Why does a first-phase insulin response exist at all?
* What does subcutaneous delivery do to the liver-to-periphery insulin gradient, and why does that
  matter?
* Why does impaired awareness of hypoglycaemia make the control problem harder rather than just
  more dangerous?

## Where this stands, October 2026

The control argument is mechanism and does not date. What dates quickly is the technology — sensor
accuracy, algorithm behaviour, available preparations and the licensing of each — along with every
number attached to it. Treat any specific figure you remember as out of date until the formulary
or product information confirms it.
