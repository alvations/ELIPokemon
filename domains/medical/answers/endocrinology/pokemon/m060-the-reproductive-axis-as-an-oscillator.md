---
id: "m060"
slug: the-reproductive-axis-as-an-oscillator
style: pokemon
category: endocrinology
difficulty: advanced
question: "Every other endocrine axis holds a set point. Why is the reproductive axis a cyclical controller instead, and what does that change about reading its tests?"
tags: [reproductive-axis, gnrh, pulsatility, gonadotrophins, feedback]
---

# Protect works until you hold it down. Truant works because it never does.

**Leftovers** is a set-point controller: a sixteenth of maximum HP at the end of every single
turn, unconditionally, with no rhythm and no event in it (**mechanism**). That is the shape every
other answer in this specialty has used, and it is the wrong shape for this one — because a
controller that holds a value cannot produce a **timed event**, and a timed event is what this
loop exists to produce.

So the architecture is different, in three ways that the games happen to model exactly.

1. **The input is a rhythm, not a level.** **Truant** is a counter that flips every turn, so its
  holder acts and then loafs and then acts — **Slakoth** and **Slaking** carry it as their only
  ability, and **Durant** carries it as a **Hidden Ability** (**mechanism**). The output *is* the
  pattern.
2. **Holding a signal down destroys it.** The **Protect** family shares a consecutive-use counter.
   In the Generation III decompilation the success chance runs full, then a half, then a quarter,
   then an eighth — and the counter **resets to zero the moment any other move is used**
   (**mechanism**). Pulse it and it never degrades. Hold it down and it stops being a signal at
   all.
3. **The feedback changes sign at a threshold.** **Weakness Policy** does nothing while you take
  ordinary hits, and then, on a super-effective hit, raises both offences sharply (**mechanism**).
  The same input, two signs, switched by a condition.

| In the battle | What it stands for |
| --- | --- |
| **Truant**, flipping its counter every turn | The pulse generator: the output is the rhythm |
| The **Protect** family's consecutive-use decay | Continuous stimulation desensitising |
| Any other move, resetting that counter to zero | Why pulses do not desensitise and a hold does |
| **Encore**, locking a target into repeating itself | Continuous delivery, imposed from outside |
| **Outrage**, **Thrash**, **Petal Dance** | Driving hard is not the same as driving right |
| **Weakness Policy**, on a super-effective hit | The sign reversal, above a threshold |
| **Electric Terrain**'s five turns, eight with a **Terrain Extender** | A condition with a built-in period |
| **Flail**'s base power, 20 up to 200 | The reporter, inverse, for the fourth time |
| **Taunt**, from something unrelated to this at all | An unrelated problem silencing the generator |
| **PP**, and an **Ether** restoring 10 of it | Availability: reversible, and nothing is broken |
| **Leftovers**, every turn, unconditionally | A set-point controller, for contrast |

Claims are marked (**mechanism**), (**definitional**), (**consensus**) or (**country-dependent**)
where it matters.

## The two architectures, side by side

```
   A SET-POINT CONTROLLER (the other three answers)
   ────────────────────────────────────────────────
   bar drops ──► Leftovers pays a sixteenth ──► bar recovers ──► drop shrinks
       ▲                                                             │
       └──────────── always the same sign, every turn, ──────────────┘
                     no rhythm, no event, settles

   AN OSCILLATOR
   ─────────────
   TRUANT as the generator ── acts, loafs, acts, loafs ──► the gonadotroph
                                                                │
                            ┌───────────────────────────────────┤
                            ▼                                   ▼
                      the recruiting output              the surge output
                      early, restrained                  later, and once
                            │                                   │
                            ▼                                   │
                  the condition builds on the field              │
                            │                                   │
          ┌─────────────────┴─────────────────┐                  │
          ▼                                   ▼                  │
   while it is LOW                   once it is HIGH and         │
   ⇒ it holds the generator back     has STAYED high past a      │
     (negative, the ordinary way)    duration threshold          │
          │                          ⇒ WEAKNESS POLICY FIRES ────┘
          │                                   │
          │                                   ▼
          │                           +2 and +2, all at once. THE EVENT.
          │                                                      │
          │                                 and then the ordinary negative
          │                                 restraint comes back on
          │                                                      │
          └─────────── the five turns lapse, and it restarts ◄────┘

   THE OTHER SIDE OF THE SAME AXIS, for contrast: the same generator, the same two
   outputs, the same condition on the field — and NO Weakness Policy anywhere in it,
   so no sign reversal and no period. Much closer to Leftovers, with a mild
   time-of-day variation on top.
```

Two generators, two outputs, the same condition, and two completely different control laws — the
difference being entirely whether a sign reversal is wired into the loop. That is the single most
transferable idea on this page.

## The paradox, which is a mechanic and not a trick

Because the responder reads the **pattern**, delivering the same thing continuously does the
opposite of delivering it in pulses. Here is the verified mechanic again, because it is the whole
argument: `protectUses` increments on each consecutive success and is **reset to zero whenever the
last resulting move was not one of the family** (**mechanism**). So four pulses of **Protect**,
spaced out, all land. Four in a row and the fourth has an eighth of the chance.

Now put **Encore** on it. Encore locks the target into repeating the move it just used, which
means the counter can never reset and the move degrades to nothing (**mechanism**). **Forcing
continuity is how you switch the system off**, and it looks like driving it harder.

Students get this backwards reliably, and the reason is that they are reasoning from a set-point
model where more of a signal means more of a response. In a frequency-encoded system, **how** you
deliver something decides whether it is a signal at all.

**Outrage**, **Thrash** and **Petal Dance** make the same point from the other end: locked in for
two or three turns, unable to choose anything else, and confused at the end of it (**mechanism**).
Sustained, unopposed, maximum drive, and the result is a loss of coordination rather than a
stronger effect.

## What this changes about the readout

**A reading without the turn number is not a reading.** This is the commonest mistake in this
topic and it is structural rather than careless: the same value is unremarkable on turn two of a
cycle and plainly wrong on turn four, so a number on its own has no interpretation to have
(**mechanism**). Which turn, counted from where, and what you are asking are all part of the
measurement. The conventions differ by country (**country-dependent**).

**The two-level rule survives intact**, and it is worth stating in exactly the same words as the
other three answers:

| The reporter | The condition | Where the fault is |
| --- | --- | --- |
| **Flail** loud | Gone | The **setter** — nothing can produce it |
| **Flail** at 20, or quietly at 40 | Gone | The level **above** the setter |

Fourth time. Same question every time: **is Flail as loud as the field says it should be?**

**And here there is a third category the other axes barely have.** Because the controller is a
rhythm generator, anything that disturbs the rhythm takes the whole axis down without any setter
being damaged. The clean picture is **PP**: run the generator's move to zero and it cannot pulse,
and an **Ether** or a **Leppa Berry** restoring 10 PP brings everything back at once, because
nothing was ever wrong (**mechanism**). The other clean picture is **Taunt**, which prevents
status moves for a few turns and can be thrown by something with no connection to this axis
whatsoever (**mechanism**). The reporter goes quiet, the condition lapses, and the fault is next
door.

## Where the games have no honest picture, and I am not going to invent one

The cycle above restarts because the terrain timer lapses and the setter comes back in. Real
oscillators of this kind run on a **store that is laid down once and only ever depletes**, and
when it is exhausted the condition cannot be set again however intact everything else is — at
which point the reporter climbs to its top band and stays there, and the loud reporter is the loop
working correctly rather than anything going wrong.

The games have no mechanic for that. **PP** depletes but an **Ether** restores it; a setter can be
off the team but that is an absence rather than an exhaustion. The nearest honest thing is the
diabetes answer's first failure mode — **no setter on the team at all** — and it is a picture of
absence, not of a store running out (**mechanism**). So this part of the loop has no analogy here,
and saying so is better than bending a mechanic until it fits.

And one more thing I have deliberately not used. Pokémon has an entire breeding system — the **Day
Care**, egg groups, a **Destiny Knot** — and it would have been the obvious place to go. It is not
used anywhere in this answer, on purpose, and the reason is in the next section.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

The reason the breeding mechanics are absent is simple. This axis governs whether someone can have
a child, when puberty happens, and the transition through menopause. Mapping any of that onto
compatibility rules and egg groups would be mapping a person's body, and a person's hopes, onto a
game mechanic for producing creatures. The analogy is for the **controller** — rhythms,
thresholds, sign reversals — and it stops at the controller. Whimsy about a mechanism is useful.
Whimsy about this would be grotesque.

Everything above is a description of a control system. Infertility is one of the most distressing
experiences in medicine, and it is routinely investigated through exactly the numbers described
above. A result sheet is not the thing. It is a partial measurement of one part of a system, taken
on one day, and its meaning is settled in a conversation and not on a page.

Three specific things, said directly.

**These tests do not predict an individual's fertility.** They describe the state of an axis.
Markers of ovarian reserve in particular are very widely misread — by patients and clinicians both
— as a forecast for one person. They are not, and the gap between what they measure and what
people are told they measure is a recognised problem.

**Menopause is not a pathology.** It is the physiological end of a finite store, and rising
gonadotrophins are the loop working correctly. Whether and how symptoms are treated is a decision
made with a person, it has moved substantially over two decades, and it differs between countries.

**Polycystic ovary syndrome is not a disease of behaviour.** Its diagnostic criteria are genuinely
contested and differ between the bodies that publish them, so none appear here. Its interaction
with weight is bidirectional and mechanistic, and presenting it as a consequence of personal
choices is both wrong and documented to damage the care people receive.

**Puberty, its timing, and anything concerning gender are out of scope.** Same axis, almost none
of the same considerations, clinical and ethical frames that differ between countries, and nothing
that material pitched at mechanism can usefully add. Local specialist guidance is the authority.

A note about who is reading. Someone reading this is quite likely to be in the middle of fertility
investigation, or to have had a result nobody explained, rather than revising for a paper. If that
is you: nothing above is about your case or your chances. The person who ordered the test is the
person who can say what it means for you, and no analogy about rhythms can stand in for that.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* The polycystic ovary syndrome guideline issued in your country, or the international
  evidence-based guideline your national body has adopted, for the criteria that apply where you
  are — they differ.
* Your national guideline on the assessment and management of infertility, for what is measured,
  when, and what the results are used for.
* Your national guideline on menopause, for the current position on symptom management.
* The specialty society guidance on male hypogonadism issued in your country, for sampling
  conditions and the interpretation of a low testosterone.
* **Your own laboratory's handbook**, for its assays, its phase-specific reference intervals and
  the sampling conditions each measurement needs.
* A current reproductive endocrinology textbook, for pulse generator physiology, the sign reversal
  of steroid feedback, inhibin biology and sex hormone binding globulin.

The Pokémon side is different and is sourced properly. The **Protect** family's success-rate table
and the fact that its counter resets when the last resulting move was not one of the family,
**Truant**'s per-turn counter flip and its presence on **Slakoth** and **Slaking** with **Durant**
carrying it as a **Hidden Ability**, **Weakness Policy**'s sharp rise in both offences on a
super-effective hit, **Flail**'s six-band power table, the five-turn and eight-turn terrain
timers, **Leftovers**' sixteenth and the **Ether** and **Leppa Berry** restoring 10 PP were all
read from the pokeemerald and pokeemerald-expansion decompilations rather than from memory. The
generation-dependence of the **Protect** ratio is flagged where it is used.

## Scope and safety

The Pokémon here is doing one job: making the difference between a set-point controller and an
oscillator concrete, and showing why a frequency-encoded signal behaves backwards under continuous
delivery. It is not a clinical reference, not a decision aid, not a fertility assessment, and not
about any individual's care or any individual's chances. **No reference intervals, cycle-day
thresholds, diagnostic criteria or doses appear here on purpose** — they differ between
laboratories, countries and guideline bodies and they are revised. Puberty, its timing, and
anything concerning gender are explicitly out of scope and are matters for local specialist
guidance. The game's breeding mechanics are deliberately not used anywhere, for the reason given
above. Nothing here has had clinical review. If someone is unwell now, contact local emergency
services, and if someone is distressed, the right contact is a person and not a page.

## What a Gym Leader digs into next

* Why can **Leftovers** never produce an event, however large you make the sixteenth?
* Why does **Encore** switch a system off by making it repeat itself?
* Why do four spaced **Protect**s all land when four consecutive ones do not?
* Why is a reading without the turn number uninterpretable rather than merely imprecise?
* Why does a **Taunt** from something unrelated produce a picture that looks like the level above
  has failed?

## Where this stands, October 2026

The architecture — a rhythm as the signal, desensitisation under continuous delivery, a sign
reversal above a threshold, and the contrast with a set-point controller — is mechanism and does
not date. The two-level rule is stable. What dates on the Pokémon side is the constants: the
**Protect** family's consecutive-use ratio is the Generation III table above and has been retuned
since, terrains and the **Surge** abilities exist only from Generation VI and VII, and **Durant**
carries **Truant** as a **Hidden Ability** rather than as its standard one. Check the current
generation's data. On the clinical side almost everything moves and moves fast — the criteria for
polycystic ovary syndrome, the position on menopause symptom management, what fertility assessment
measures and how it is reported, the interpretation of a low testosterone, and every reference
interval involved — so check current local guidance and your own laboratory's handbook.
