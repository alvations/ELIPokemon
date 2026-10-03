---
id: "m060"
slug: the-reproductive-axis-as-an-oscillator
style: serious
category: endocrinology
difficulty: advanced
question: "Every other endocrine axis holds a set point. Why is the reproductive axis a cyclical controller instead, and what does that change about reading its tests?"
tags: [reproductive-axis, gnrh, pulsatility, gonadotrophins, feedback]
---

# A controller that holds a value cannot produce an event, so this one oscillates instead

Every other axis in this specialty is a regulator. It has a target, it measures the deviation and
it corrects. The reproductive axis in the female is not that shape at all, and the reason is that
what it has to produce is not a steady concentration but a **timed event** — one ovulation, at one
moment, after a defined preparatory phase. A proportional controller holding a set point can never
generate that. So the architecture is different in three specific ways, and almost every
interpretive error in the topic comes from reading it as though it were not.

1. **The input is a frequency, not a level.** Gonadotrophin-releasing hormone is released from the
  hypothalamus in discrete pulses, and the pituitary gonadotroph responds to the **pattern** —
  pulse frequency and amplitude — rather than to the mean concentration (**consensus**).
2. **The feedback changes sign.** Oestradiol inhibits gonadotrophin output for most of the cycle
  and then, once it is high enough for long enough, drives it, producing the mid-cycle surge
  (**consensus**). No set-point loop does this.
3. **There is a built-in period.** The loop is designed to return to its own start rather than to
  settle, so "stable" is not what success looks like.

Claims below are marked (**mechanism**) where they follow from physiology and are checkable by
reasoning, (**definitional**) where the statement is what a term means, (**consensus**) where they
are settled professional agreement, and (**country-dependent**) where the answer differs between
countries and documents.

## The two architectures, side by side

```
   A SET-POINT AXIS (thyroid, cortisol, calcium)
   ─────────────────────────────────────────────
   deviation ──► controller ──► effector ──► variable corrected ──► deviation shrinks
        ▲                                                                │
        └────────────────── always negative, always ─────────────────────┘
                            settles into a band

   THE FEMALE REPRODUCTIVE AXIS
   ────────────────────────────
   hypothalamic PULSE GENERATOR ── pulses, not a level ──► gonadotroph
                                                                │
                            ┌───────────────────────────────────┤
                            ▼                                   ▼
                           FSH                                  LH
                   follicular recruitment               later, the surge
                            │                                   │
                            ▼                                   │
                     granulosa cells: OESTRADIOL, INHIBIN B      │
                            │                                   │
          ┌─────────────────┴─────────────────┐                  │
          ▼                                   ▼                  │
   LOW / RISING oestradiol            HIGH oestradiol,           │
   ⇒ NEGATIVE feedback                sustained past a           │
   (and inhibin B restrains           duration threshold         │
    FSH specifically)                 ⇒ FEEDBACK FLIPS SIGN ─────┘
          │                                   │
          │                                   ▼
          │                           THE SURGE ──► ovulation ──► corpus luteum
          │                                                            │
          │                                       progesterone + oestradiol + inhibin A
          │                                       ⇒ NEGATIVE feedback restored
          │                                                            │
          │                                       no pregnancy signal ⇒ luteolysis
          └──────────────────────── and the cycle restarts ◄───────────┘

   THE MALE AXIS, for contrast: pulsatile LH ──► Leydig cell testosterone;
   FSH ──► Sertoli cells ──► spermatogenesis and inhibin B; negative feedback
   from testosterone, from its aromatised oestradiol, and from inhibin B.
   Same hormones. No sign reversal, no monthly period — much closer to a set point,
   with a diurnal variation that peaks in the morning.
```

Two hypothalamic pulse generators, two pituitary cell responses, the same gonadotrophins and the
same steroids — and two completely different control laws, depending on whether the loop has a
sign-reversal built into it. That is the single most transferable idea in reproductive
endocrinology.

## The pharmacological paradox, which is a control fact and not a drug trick

Because the gonadotroph responds to a **pattern**, delivering the same molecule continuously does
the opposite of delivering it in pulses. Continuous occupancy of the receptor downregulates it,
and the axis shuts down; pulsatile delivery sustains it (**consensus**). This is why agonists of
gonadotrophin-releasing hormone are used to **suppress** the axis, after an initial stimulatory
flare as the stored gonadotrophins are released, while receptor antagonists suppress it without
that flare (**consensus**).

Nobody could deduce this from a set-point model, and students reliably get it backwards. In a
frequency-encoded system, **how** you deliver a signal determines whether it is a signal at all.

## What this changes about reading the tests

**A gonadotrophin or an oestradiol without a cycle day is not a result.** This is the commonest
interpretive error in the specialty, and it is structural rather than careless: the same value is
unremarkable in one phase and clearly abnormal in another, so a number on its own has no
interpretation to have (**mechanism**). Which day, measured from what, and what is being asked are
all part of the measurement. The conventions differ between countries and laboratories
(**country-dependent**).

**The two-level localisation rule still works, unchanged.** This is the one thing that carries
over intact from the set-point axes, and it is worth stating in exactly the same words:

| Gonadotrophins | Steroid | Where the lesion is | The name (**definitional**) |
| --- | --- | --- | --- |
| High | Low | The **gonad** | Hypergonadotrophic hypogonadism |
| Low, or inappropriately normal | Low | **Hypothalamus or pituitary** | Hypogonadotrophic hypogonadism |

Same move as thyrotropin against free T4, as corticotropin against cortisol, as parathyroid
hormone against calcium. Is the controller's output **appropriate** for what it is seeing? Four
axes, one question.

**But a third category exists here that the other axes do not really have.** Because the
controller is a frequency generator, anything that disturbs pulse frequency disturbs the whole
axis with no gland being diseased at all — low energy availability, intercurrent illness, high
training load, severe psychological stress, and hyperprolactinaemia, which suppresses the pulse
generator directly (**consensus**). The biochemistry looks central: low gonadotrophins, low
steroid. Nothing is damaged. It is **functional**, and it is reversible when the input is
restored. That last point is why prolactin is measured in this situation at all — a pituitary
problem presenting as a reproductive one is not a coincidence, it is the pulse generator being
switched off from next door.

## Ageing, and why the two sides of the axis age differently

The ovary has a finite store of follicles, established before birth and declining thereafter, and
as it depletes the gonadotrophins rise because the loop is doing exactly what the localisation
rule predicts: it is a primary gonadal failure (**consensus**). It is also entirely physiological.
The rule locates the lesion correctly and tells you nothing about whether there is a disease,
which is a useful reminder that a biochemical pattern is not a diagnosis.

The male axis declines gradually and mostly keeps its architecture, which is why the
interpretation there turns on morning sampling, on repeat measurement, and on distinguishing a
genuinely low testosterone from the fall that accompanies obesity, illness and sleep deprivation
(**consensus**). Sex hormone binding globulin is the binding-protein trap in this axis, exactly as
thyroxine-binding globulin is in the thyroid axis and cortisol-binding globulin in the adrenal
one: it changes the total without changing the free fraction, and it moves with obesity, with
insulin resistance, with thyroid status and with age (**consensus**). Three axes, one error, and
it is the same error each time.

## Polycystic ovary syndrome, stated carefully

A disordered oscillator with androgen excess is the honest short description: ovulation is
infrequent or absent, androgens are raised, and insulin resistance is common and interacts with
the axis (**consensus**). Two things need saying plainly.

First, the **diagnostic criteria are contested**. Different bodies in different countries define
it differently, the definitions have been revised more than once, and which criteria apply depends
on where you are (**country-dependent**). None appears here. A ratio of the two gonadotrophins,
which older teaching treated as diagnostic, is not part of current criteria (**consensus**).

Second, it is not a disease of behaviour. The interaction with weight is bidirectional and
mechanistic, and presenting it as a consequence of personal choices is both wrong and documented
to damage the care people receive.

## The human stakes, said plainly

This is the section that matters most in this answer, and the register changes for it.

Everything above is a description of a control system. The things it controls include whether
someone can have a child, when puberty happens, and the transition through menopause — and those
are not control problems to the people living them. Infertility is one of the most distressing
experiences in medicine and it is routinely investigated through exactly the numbers described
above. A result sheet is not the thing. It is a very partial measurement of one part of a system,
taken on one day, and its meaning is settled in a conversation and not on a page.

Three specific things.

**The tests above do not predict an individual's fertility.** They describe the state of an axis.
Markers of ovarian reserve in particular are very widely misread, by patients and clinicians both,
as a forecast for one person; they are not, and the gap between what they measure and what people
are told they measure is a recognised problem (**consensus**).

**Menopause is not a pathology.** It is the physiological end of a finite store, and the rising
gonadotrophins are the loop working correctly. Whether and how symptoms are treated is a decision
made with a person, it has moved substantially over the past two decades, and it differs between
countries (**country-dependent**).

**Puberty, its timing, and anything concerning gender are outside what this page covers.** They
involve the same axis and almost none of the same considerations, the clinical and ethical frames
differ between countries, and material pitched at mechanism has nothing useful to add. Local
specialist guidance is the authority.

A note about who is reading. Someone reading this is quite likely to be in the middle of fertility
investigation, or to have had a result they did not understand, rather than revising for a paper.
Nothing here describes any individual's case or any individual's chances. If a number on your own
results is worrying you, the person who ordered it is the person who can tell you what it means in
your case, and nothing here can substitute for that.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* The guideline on polycystic ovary syndrome issued in your country, or the international
  evidence-based guideline your national body has adopted, for the diagnostic criteria that apply
  where you are — they differ.
* Your national guideline on the assessment and management of infertility, from the body that
  issues it, for what is measured, when in the cycle, and what the results are used for.
* Your national guideline on menopause, for the current position on symptom management, which has
  changed substantially and continues to.
* The specialty society guidance on male hypogonadism issued in your country, for sampling
  conditions and the interpretation of a low testosterone.
* **Your own laboratory's handbook**, for its assays, its cycle-phase-specific reference intervals
  and the sampling conditions each measurement needs.
* A current reproductive endocrinology textbook, for pulse generator physiology, the sign reversal
  of oestradiol feedback, inhibin biology and sex hormone binding globulin.

## Scope and safety

This is revision material about control architecture and test interpretation, written for someone
training in or qualified for the field. It is not a clinical reference, not a decision aid, not a
fertility assessment, and not about any individual's care or any individual's chances. **No
reference intervals, cycle-day thresholds, diagnostic criteria or doses appear here on purpose** —
they differ between laboratories, countries and guideline bodies and they are revised. Puberty,
its timing, and anything concerning gender are explicitly out of scope and are matters for local
specialist guidance. Nothing here has had clinical review. If someone is unwell now, contact local
emergency services, and if someone is distressed, the right contact is a person and not a page.

## What an examiner digs into next

* Why can a set-point controller not produce a timed event?
* Why does continuous administration of a receptor agonist suppress an axis that pulses?
* Why is a gonadotrophin result without a cycle day uninterpretable rather than merely imprecise?
* Why does hyperprolactinaemia produce a biochemical picture that looks central?
* Why do rising gonadotrophins at menopause mean the loop is working correctly?

## Where this stands, October 2026

The architecture — frequency encoding, the sign reversal, the built-in period, and the contrast
with the male axis — is mechanism and does not date. The two-level localisation rule is stable.
What moves, and moves fast, is everything else: the diagnostic criteria for polycystic ovary
syndrome, the position on menopause symptom management, what is measured in fertility assessment
and how the results are presented, the interpretation of low testosterone in men, and every
reference interval involved. All of those are country-dependent and under active revision. Check
current local guidance and your own laboratory's handbook.
