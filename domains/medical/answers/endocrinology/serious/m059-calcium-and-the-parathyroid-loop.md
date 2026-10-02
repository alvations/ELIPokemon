---
id: "m059"
slug: calcium-and-the-parathyroid-loop
style: serious
category: endocrinology
difficulty: intermediate
question: "Why is calcium control the cleanest worked feedback loop in medicine, and how does the pair of calcium and parathyroid hormone locate the lesion?"
tags: [calcium, parathyroid, vitamin-d, phosphate, magnesium]
---

# One sensor, three actuators on three clocks, and a pair of numbers that says which part broke

Calcium control is the loop to learn first, because every part of it is identifiable. There is a
single controlled variable with an unusually narrow tolerance. There is a named sensor that is
physically a receptor on a single cell type. The sensor is **inhibitory**, so the controller's
output is an inverse function of the thing being controlled. There are exactly three actuators,
with time constants of minutes, hours and days. And there is a second quantity, phosphate, that
the controller moves in the opposite direction — so a panel of two numbers reads out the loop's
internal state in a way that no single number does.

Nothing else in endocrinology is laid out this plainly, which is why this topic generalises: once
the question "is the controller's output **appropriate** for the controlled variable?" is natural
here, it transfers unchanged to thyrotropin against free T4, to corticotropin against cortisol,
and to the gonadotrophins against gonadal steroid.

Claims below are marked *(mechanism)* where they follow from physiology and are checkable by
reasoning, *(definitional)* where the statement is what a term means, *(consensus)* where they are
settled professional agreement, and *(country-dependent)* where the answer differs between
countries and documents.

## Why the tolerance is narrow

Ionised calcium sets membrane excitability, and it is a cofactor for neurotransmitter and hormone
release, for muscle contraction and for the coagulation cascade *(mechanism)*. Too little and
membranes become excitable: paraesthesiae, carpopedal spasm, tetany, and in the extreme laryngeal
spasm and seizures. Too much and excitability is depressed: lethargy, constipation, muscle
weakness, confusion, polyuria from impaired renal concentrating ability, and with chronicity renal
stones and bone pain *(consensus)*. A variable with harm on both sides at close range is one a
loop has to hold tightly, and the architecture reflects that.

## The loop, drawn with its clocks

```
                        ┌──────────────── IONISED CALCIUM ◄──────────────┐
                        │                 the controlled variable        │
                        ▼                                                │
              THE SENSOR: calcium-sensing receptor                       │
              on the parathyroid chief cell                              │
              INHIBITORY — so output goes UP as calcium goes DOWN        │
                        │                                                │
                        ▼                                                │
              PARATHYROID HORMONE  (steep, inverse, sigmoid)             │
                        │                                                │
      ┌─────────────────┼──────────────────────────┐                     │
      ▼                 ▼                          ▼                     │
   KIDNEY            BONE                       KIDNEY, slow arm         │
   distal tubular    exchange, then              1-alpha-hydroxylation   │
   reabsorption ↑    resorption ↑                of 25-OH vitamin D      │
   phosphate         (osteoclasts, via           → CALCITRIOL            │
   reabsorption ↓    osteoblast signalling)            │                 │
      │                 │                              ▼                 │
      │                 │                       GUT absorption ↑         │
      │                 │                              │                 │
   MINUTES           MINUTES → HOURS                 DAYS                │
      │                 │                              │                 │
      └─────────────────┴──────────────────────────────┴─────────────────┘

   And note what the fast arm does to the OTHER number:
   PTH raises calcium and LOWERS phosphate, in the same action.
   So the PAIR moves in opposite directions, and the pair is diagnostic.
```

Three actuators on three clocks is the design feature, not an accident. A disturbance is met first
by shifting calcium that is already in the body (renal reabsorption, bone exchange), then by
mobilising it from a store (resorption), and only then by changing how much is coming in from
outside (gut absorption, requiring calcitriol to be synthesised first) *(mechanism)*. Fast, cheap,
reversible actions come first; slow, expensive, structural ones come last. That is what a
well-designed controller looks like, and it is why the time course of a calcium disturbance tells
you which arm is carrying the load.

## Vitamin D is the gain on the slow arm, not a fourth hormone

25-hydroxyvitamin D is a substrate. Parathyroid hormone drives its conversion to
1,25-dihydroxyvitamin D in the kidney, and that product is what acts on the gut *(mechanism)*.
Deficiency of the substrate therefore does not present as "low vitamin D" physiology — it presents
as a **slow arm with no authority**, so the controller compensates by running the fast arms
harder, and the measurable consequence is a raised parathyroid hormone with a calcium that may
still be normal *(mechanism)*. The loop is working. It is working hard, and that is what the
number is reporting.

## The pair, which is the whole diagnostic move

| Calcium | Hormone | What it means | Where to look |
| --- | --- | --- | --- |
| High | High, or inappropriately normal | The **gland** is not listening | Primary hyperparathyroidism; or a shifted sensor set point |
| High | Suppressed | The loop is **working and overridden** | Calcium arriving from outside: malignancy, vitamin D excess, granulomatous disease |
| Low | High | The loop is **trying** | Substrate deficiency, chronic kidney disease, malabsorption |
| Low | Low, or inappropriately normal | The **controller** is gone | Post-surgical, autoimmune, developmental; or magnesium depletion |

The phrase "inappropriately normal" is where the whole skill sits. A parathyroid hormone inside
the reference interval alongside a high calcium is **abnormal**, because a healthy sensor would
have switched the gland off *(mechanism)*. A number can be inside its range and still be the wrong
answer to the question it was asked. Readers who have internalised that sentence have the topic;
readers who read each row off a result sheet do not.

**Familial hypocalciuric hypercalcaemia deserves its place in that first row**, because it is the
cleanest set-point disease in medicine: an inactivating change in the sensor means the gland is
satisfied at a calcium the rest of the body is not, so calcium settles at a new, higher, stable
value with a parathyroid hormone that is normal or mildly raised, and the kidney — whose own
sensor is similarly affected — stops excreting calcium in proportion *(mechanism)*. It is not a
gland disease at all. It is a thermostat set two degrees high, and distinguishing it from primary
hyperparathyroidism matters because one of the two is sometimes operated on and the other should
not be *(consensus)*.

## Phosphate, and why the panel is read as a set

Parathyroid hormone reduces proximal tubular phosphate reabsorption while raising distal calcium
reabsorption, so under parathyroid drive the two move in **opposite** directions *(mechanism)*.
That single fact makes the panel readable:

* High calcium with low or low-normal phosphate, and a raised hormone: the hormone is doing it.
* High calcium with **high** phosphate: the hormone is not doing it, because the hormone would
  have dumped the phosphate — so look for calcium arriving from outside the loop, or for excess
  calcitriol activity, which raises both *(mechanism)*.
* Low calcium with high phosphate and a low hormone: the controller is absent, so phosphate is
  being retained — the post-surgical and the autoimmune picture *(mechanism)*.
* Low calcium with low phosphate and a high hormone: substrate deficiency, with the hormone
  compensating and dumping phosphate as it goes *(mechanism)*.

Chronic kidney disease deranges this deliberately-tidy picture because it breaks two things at
once — phosphate excretion **and** 1-alpha-hydroxylation — which is why its mineral disorder is
treated as its own subject with its own guidance *(country-dependent)*, and why its late,
autonomous phase is named separately as tertiary hyperparathyroidism *(definitional)*.

## Two things that will catch you, and both are mechanical

**Albumin.** Most measured calcium is bound, chiefly to albumin, and only the ionised fraction is
active and only the ionised fraction is sensed *(mechanism)*. A low albumin lowers the measured
total with no change in the physiology, which is why laboratories report an adjusted value and why
the adjustment formula differs between them *(country-dependent)*. In acute illness, and where the
adjustment is unreliable, directly measured ionised calcium is the answer. This is the same
binding-protein trap that catches total T4 and total cortisol: three axes, one error.

**Magnesium.** Severe magnesium depletion impairs both the secretion of parathyroid hormone and
its action at target tissue, so hypocalcaemia with a low or unimpressively normal hormone persists
until magnesium is corrected *(consensus)*. Nothing is wrong with the gland, the sensor or the
actuators. A cofactor is missing, and restoring it restores the whole loop at once. Hypocalcaemia
that is not responding is the specific situation in which magnesium is the thing that has been
forgotten.

## Why post-surgical hypocalcaemia has the time course it has

Remove or devascularise parathyroid tissue and the actuators are all intact while the controller
is suddenly absent. The fast arms stop first, because they are the ones under moment-to-moment
hormonal control, so calcium falls over hours to days rather than instantly *(mechanism)*. The
slow arm persists longer, because calcitriol already made does not vanish. And the recovery, if
the remaining tissue recovers, follows the reverse order. That ordering — fast arm out first, slow
arm out last — is readable straight off the diagram, which is the point of drawing it.

## The human stakes, said plainly

Two things here matter to people rather than to examiners.

Primary hyperparathyroidism is often found incidentally on a blood test taken for something else,
in someone who feels well. The decision about what to do then is genuinely contested, depends on
age, bone density, kidney function and calcium level, and differs between the guideline bodies
that publish on it *(country-dependent)*. "Your calcium is high" is not a diagnosis and is not a
plan, and a great deal of avoidable alarm comes from the gap between an abnormal number and a
conversation about what it means.

Chronic hypoparathyroidism after neck surgery is a condition people live with permanently, managed
with an external supply of something the body normally regulates minute by minute, with the
symptoms of being slightly under-replaced and slightly over-replaced both unpleasant and both
common. It is frequently described as under-recognised by the people living with it, and that
description is worth taking at face value.

A note about who is reading. Someone reading this may have been told their calcium is abnormal.
Nothing here is a threshold, a target or a plan. A calcium result is interpreted alongside
albumin, phosphate, kidney function, the hormone and the clinical picture, by the team that
ordered it — reading a single number against a table on a revision page is exactly the error this
answer is about.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national guideline on hyperparathyroidism and on the investigation of hypercalcaemia, from
  the body that issues it, for referral and intervention criteria — which differ between
  countries.
* Your national or regional guidance on chronic kidney disease mineral and bone disorder, which is
  a separate document from the general calcium guidance and governs that whole situation.
* **Your own laboratory's handbook**, for its reference intervals, the albumin-adjustment formula
  it applies, whether it offers directly measured ionised calcium and under what conditions, and
  the assays it runs for parathyroid hormone and vitamin D metabolites.
* Your national formulary, for anything about calcium, vitamin D or active vitamin D analogue
  preparations, and for the monitoring they need.
* A current endocrinology or renal textbook, for calcium-sensing receptor biology, the sigmoid
  secretion curve, 1-alpha-hydroxylase regulation and the renal handling of phosphate.

## Scope and safety

This is revision material about mechanism and the interpretation of a panel, written for someone
training in or qualified for the field. It is not a clinical reference, not a decision aid, and
not about any individual's care. **No reference intervals, thresholds, doses, adjustment formulae
or intervention criteria appear here on purpose** — they differ between laboratories, countries
and guideline bodies, they are revised, and the units used to report calcium differ too. Your
laboratory and your local guidance are the authority and this page is not. Severe hypocalcaemia
and severe hypercalcaemia are both medical emergencies and neither is described here. Nothing here
has had clinical review. If someone is unwell now, contact local emergency services.

## What an examiner digs into next

* Why is a parathyroid hormone inside the reference interval sometimes the abnormal result?
* Why does the controller move calcium and phosphate in opposite directions, and what does the
  pair buy you?
* Why does magnesium depletion produce hypocalcaemia that does not respond until magnesium is
  corrected?
* Why does post-surgical hypocalcaemia fall over hours to days rather than immediately?
* Why is familial hypocalciuric hypercalcaemia not a gland disease?

## Where this stands, October 2026

The loop, its sensor, its three actuators and their clocks, the inverse secretion curve and the
phosphate relationship are mechanism and do not date. The pair-reading rule is stable and
generalises. What moves is everything numeric and procedural: reference intervals, albumin-
adjustment formulae, which vitamin D metabolite is measured and when, the intervention criteria
for primary hyperparathyroidism, and the whole of the chronic kidney disease mineral guidance,
which is revised on its own cycle and differs between countries. Check current local guidance and
your own laboratory's handbook.
