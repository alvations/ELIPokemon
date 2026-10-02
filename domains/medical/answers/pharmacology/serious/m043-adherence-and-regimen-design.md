---
id: "m043"
slug: adherence-and-regimen-design
style: serious
category: pharmacology
difficulty: intermediate
question: "What makes a regimen hard to take, why does the timing of a side effect matter more than its severity, and why is calling someone non-compliant a statement about the prescription?"
tags: [adherence, regimen-design, side-effect-timing, deprescribing, measurement-bias]
---

# Adherence is a property of a regimen meeting a life, not a property of a person.

A regimen that requires four correct actions a day, at times nobody chose, with a symptom arriving
weeks before any benefit does, is a **design**. The design was produced by a prescriber. When it
fails, the useful question is which part of the design failed, and "non-compliant" answers none of
them.

That is not a point about politeness, although it is also that. It is a point about
**tractability**. "Non-compliant" is a dead end: it names the person, implies a disposition, and
suggests no intervention. Replace it with a mechanism — the doses fall while they are asleep, the
side effect arrives before the benefit, the pack cannot be opened with arthritic hands, the
co-payment is for four items and they can afford two, nobody said it was lifelong, they stopped
because they felt better and nobody said that was the drug working — and each one names its own
fix.

Claims are marked **mechanism** mechanism, **definitional** definitional, **consensus** consensus,
or (**country-dependent**) local.

## The arithmetic of complexity

If each scheduled dose is taken with some probability independently of the others, the probability
of a fully correct day is that probability raised to the number of doses.

```
   ILLUSTRATIVE ONLY. The 0.9 below is a round number chosen to make the exponent
   legible. It is NOT an observed adherence rate and no figure here is one.

   per-dose           doses per day
   reliability      1        2        3        4        5
   ────────────────────────────────────────────────────────────
      0.95        0.95     0.90     0.86     0.81     0.77
      0.90        0.90     0.81     0.73     0.66     0.59
      0.80        0.80     0.64     0.51     0.41     0.33
   ────────────────────────────────────────────────────────────
                    ▲                                   ▲
            the SAME person, the SAME reliability per dose, and a
            regimen that works two days in three or one day in three

   ┌──────────────────────────────────────────────────────────────────────────────┐
   │  This is why reducing dose FREQUENCY is one of the few adherence            │
   │  interventions that works on mechanism rather than on motivation. It does   │
   │  not ask anyone to try harder. It removes opportunities to fail.            │
   └──────────────────────────────────────────────────────────────────────────────┘
```

Two honest caveats about that table, and they point in opposite directions.

**The independence assumption is wrong, and wrong in the pessimistic direction.** Doses cluster
around anchors — meals, waking, bedtime, a carer's visit. Miss breakfast and you miss the
breakfast dose and anything pinned to it, so failures correlate and the real distribution is
lumpier than a binomial (**mechanism**). Disruption is the dominant mode: travel, shift work,
admission to hospital, and above all discharge, where the list changes and nobody reconciles it
(**consensus**).

**And a lower frequency is not free.** A once-daily preparation is usually a modified-release one,
and a modified-release product is less adjustable, more expensive, not interchangeable with
another modified-release product of the same drug, and unforgiving of a missed dose because there
is no second chance that day. `m044` is where that trade sits. Simplification buys reliability
with flexibility.

## Why timing beats severity

This is the part most often taught backwards. For most preventive therapy:

```
   the HARM                              the BENEFIT
   ──────────────────────────────────    ────────────────────────────────────────────
   arrives within days                   arrives over years
   is PERCEPTIBLE -- nausea, aching,     is INVISIBLE -- a stroke that does not
   dizziness, a dry cough, somnolence    happen, which looks identical to no stroke
   is CERTAIN for the person who has     is PROBABILISTIC -- an absolute risk
   it: they can feel it today            reduction, never observable in one person
   is attributable: it started when      is unattributable: nothing is ever
   the tablet started                    attributable to it
   ──────────────────────────────────    ────────────────────────────────────────────

   A person who stops is doing correct inference on the evidence available to them.
   Their own data say the drug made them worse and nothing says it helped. The
   defect is not in their reasoning. It is that the only evidence they were given
   was their own symptoms.
```

So the interventions that work are the ones that change the shape of that table, not the ones that
exhort (**consensus**):

* **Pre-empt the interpretation.** A symptom predicted in advance is a confirmation that the drug
  is working; the same symptom unpredicted is evidence that it is harmful. Nothing about the
  symptom changed.
* **Use the kinetics.** Many early adverse effects are concentration-related and attenuate with
  titration, with dose timing (a sedating drug at night, a diuretic not at bedtime), or with food.
  Those are formulation and kinetic interventions, and they belong in the design rather than in a
  conversation about motivation (**mechanism**).
* **Say how long.** "Until you feel better" and "for life" are different prescriptions, and a
  person who was not told which one they have will decide for themselves.
* **Name what would make stopping right.** A drug nobody wants, for a benefit the person does not
  value, with a side effect they do, is sometimes a drug that should stop — which is `m014`'s
  territory, and stopping it deliberately is a clinical act, not a failure.

## Intentional and unintentional, and why the distinction decides the fix

**Unintentional** non-adherence is a practical barrier: forgetting, a pack that cannot be opened,
a regimen that cannot be fitted to a working day, a supply that ran out, a formulation that cannot
be swallowed. The fixes are practical — alignment to an existing daily anchor, a compliance aid, a
once-daily or liquid preparation, a reminder system, a smaller number of items.

**Intentional** non-adherence is a decision, and it is usually a reasonable one made on incomplete
information. The fix is the information, the shared decision, or the deprescribing. A compliance
aid imposed on an intentional decision is an irritation that changes nothing.

They coexist in the same person, for different drugs on the same list, and a question that asks
about "your tablets" as a single object will not separate them (**consensus**).

## Measuring it, and the bias in every method

Every available measure is biased, and in a known direction — so the useful skill is naming which
bias you are holding (**consensus**):

| Method | What it actually measures | Direction of the bias |
| --- | --- | --- |
| Asking | What the person thinks you want to hear | Over-reports, strongly |
| Pill counts | Tablets not in the bottle | Over-reports; tablets can be discarded |
| Refill or dispensing records | Collection from a pharmacy | Over-reports ingestion; may under-report if supplies come from elsewhere |
| Electronic monitoring | Container openings | Closest to the truth, and the measurement itself changes behaviour |
| Drug concentration | Recent exposure, confounded by kinetics | Confounds adherence with clearance; see `m041` |

The concentration row is the one that catches people out. A low trough is equally consistent with
missed doses and with fast clearance, and the number cannot separate them. Worse, concentrations
are vulnerable to the pre-appointment adherence spike: doses resumed in the days before a clinic
produce a reassuring result that describes those days and nothing else (**mechanism**).

## The layer above the consultation

Cost and co-payment structures, medicine supply and shortages, transitions of care, interpreting
and translation, health literacy, the number of different prescribers writing on one list, and
whether anybody owns the whole list. All of these are strongly country- and system-dependent
(**country-dependent**), all of them are outside the person's control, and all of them are
routinely recorded as the person's failing.

## The human stakes, said plainly

The language in this topic does real damage, and that is why this answer opens with it rather than
closing with it.

"Non-compliant" in a record follows a person. It changes how the next clinician reads them, it
invites less explanation rather than more, and it is applied unevenly — more readily to people who
are poor, who do not share the clinician's first language, who have a mental health diagnosis, or
who have already been labelled difficult. The clinical consequence is measurable in the wrong
direction: a person who expects to be blamed tells you less, and you then have less to work with.

There is also the harm from the other side. Stopping a drug can be dangerous — abrupt cessation of
some medicines causes rebound, withdrawal or loss of control of a condition, and that is a real
risk, not a rhetorical one. That makes it more important, not less, that someone feels able to say
they have stopped. A consultation in which the honest answer is punished produces a record that is
wrong, and decisions are then made on a fiction.

Nothing in this answer is advice to anyone about their own medicines, and in particular nothing
here suggests stopping or changing anything. Anyone who is finding a medicine hard to take, or who
has already stopped one, has a reason worth hearing, and the person to tell is their own
prescriber or pharmacist — who can change the design.

## What an examiner digs into next

* Same per-dose reliability, four doses a day instead of one. What happens, and why is that an
  argument about design rather than motivation?
* Why is a person who stops a statin after developing aching muscles reasoning correctly?
* Name the bias in each of the five ways of measuring adherence.
* A trough is low. Give two explanations the number cannot distinguish, and say what would.
* What does a once-daily preparation cost you, as against what it buys?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer:

* **Your national guideline body's guidance on medicines adherence and on medicines
  optimisation.** The authority for the terminology, for the intentional/unintentional distinction
  and for what is recommended in a review consultation. Country-dependent, and revised on a cycle.
* **Your national formulary's monograph** for any drug whose early adverse effects or titration
  schedule are at issue, and for the modified-release preparations that a frequency reduction
  depends on.
* **Your own institution's policy on medicines reconciliation at admission and discharge**, which
  is where the largest avoidable losses in this topic occur.
* **The primary literature** for anything quantitative about adherence rates, intervention
  effectiveness or the performance of the measurement methods above. This answer deliberately
  states no adherence figure, because the figures are population-, drug- and method-specific and a
  number quoted without its method is not informative.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only numbers in this answer are the illustrative probabilities in the
first table**, chosen to make an exponent legible; none is an observed adherence rate and none
describes any real population. Nothing here is advice about anyone's own medicines, and nothing in
it suggests starting, stopping or changing any treatment — stopping some medicines abruptly is
itself harmful, and that decision belongs with a prescriber who has the records. Practice,
terminology and the system barriers described differ by country. Anyone finding a medicine hard to
take should raise it with their own prescriber or pharmacist.

## Where this stands, October 2026

The arithmetic and the harm-before-benefit asymmetry are mechanism and do not date. The
terminology does: "compliance" gave way to "adherence" and in several countries to "concordance"
and then to plainer language about what a person decided, and the preferred term differs by
country and by specialty. What also dates is the evidence base for specific interventions —
reminder systems, compliance aids, pharmacist-led review, digital adherence monitoring — where the
trial literature has moved repeatedly and effect sizes have generally been smaller than early
enthusiasm suggested. Check the current guidance from your own national body, and the primary
literature for anything with a number on it.
