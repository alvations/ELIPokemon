---
id: "m065"
slug: randomisation-against-registries
style: pokemon
category: oncology
difficulty: advanced
question: "What does randomisation buy in an oncology trial that no amount of analysis of a registry can buy, and where is a registry the better instrument?"
tags: [clinical-trials, randomisation, confounding, registries, evidence]
---

# Horn Drill is accuracy 30, and your own battle log will tell you it is not

Here is the chance Emerald actually computes for an OHKO move, from `Cmd_tryKO`:

```
chance = move accuracy + (attacker's level − target's level)
```

and the whole thing fails outright unless the attacker's level is at least the target's. The
margins answer in this specialty used that routine to make a point about certainty. This answer
uses the **level-difference term**, because it is confounding by indication in one line of code.

**Horn Drill**'s accuracy field is 30. Now go and look at a log of your own battles and it will
have succeeded far more often than that — because you only ever reached for it when you were
comfortably over-levelled, and the level difference is added straight into the chance. The move
never changed. Your *selection* of when to use it did, and your log recorded the result without
recording the reason.

That is the entire problem with comparing treatments in a registry of routine care, and nothing
you do to the log fixes it.

**A warning about what is and is not being compared, because it matters more here than anywhere
else in this specialty.** The thing randomised in a clinical trial is a **person**. Nothing in
this answer stands in for one. What is carried across is the *procedure*: the thing allocated is a
**move**, the confounder is the **player's choice of when to use it**, and the registry is the
**battle log**. The analogy is about allocation and record-keeping, and it is dropped entirely at
the end, where the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
(**consensus**, **country-dependent**).

## The two instruments, drawn

```
   YOUR OWN BATTLE LOG                        METRONOME

   which move got used?                       which move got used?
     ▲                                          ▲
     │ YOU chose it, on the basis of            │ Cmd_metronome drew
     │ the level gap, the type matchup,         │ (Random() & 0x1FF) + 1,
     │ whether Lock-On had landed, and          │ retried if out of range,
     │ a general sense of how it was            │ and rejected anything on
     │ going                                    │ sMovesForbiddenToCopy
     │                                          │
     ▼                                          ▼
   the "used" group differs in the           the groups differ in the
   MOVE and in the SITUATION                 MOVE, and in the situation
     │                                        only by chance — which is a
     │                                        quantity with a DISTRIBUTION
     ▼
   adjust for what the log recorded
     │                                          │
     │ the move, the result, maybe               ▼
     │ the levels                               the difference is
     │ … and NOT whether Lock-On had            ATTRIBUTABLE, and what is
     │ been used, NOT whether the               left over is a sampling
     │ target had Sturdy — two things            distribution
     │ that FULLY DETERMINE the
     │ outcome and are not fields
     ▼
   RESIDUAL CONFOUNDING, of a size the
   log cannot bound

   ─────────────────────────────────────────────────────────────────────────────

   AND THE TRADE RUNS BOTH WAYS:

   Metronome   narrow pool, forbidden list  ──►  clean comparison,
                                                 and a pool nobody
                                                 would ever play from
   the log     every battle you ever had    ──►  useless for "which move
                                                 is better", and the ONLY
                                                 record of what actually
                                                 happens
```

## Why adjusting the log does not work

Regression, propensity scores and matching all do one thing: they condition on what was
**recorded** (**mechanism**). That is useful, and it is bounded by the fields the log has.

The OHKO routine supplies three gaps, and each has an exact clinical counterpart:

* **The recorded variable is not the underlying variable.** If your log holds the level gap as a
  bucket rather than a number, the adjustment is for the bucket. Performance status as entered is
  a coarse, observer-dependent summary of something continuous, and comorbidity as coded is what
  was coded.
* **The thing that actually decided it is often not a field at all.** `Cmd_tryKO` checks
  `STATUS3_ALWAYS_HITS`, which **Lock-On** and **Mind Reader** set, and it jumps straight to
  `BattleScript_SturdyPreventsOHKO` if the target has **Sturdy**. Those two conditions *determine*
  the outcome, and no ordinary battle record contains either of them. The clinician's overall
  impression of a person is in exactly that position: frequently the strongest single predictor,
  precisely what decided the allocation, and never a field.
* **You cannot adjust for a variable you did not know mattered.** Nobody reading a Red and Blue
  battle log adjusted for Sturdy, because Sturdy did not exist yet.

So the point that gets taught too weakly: **residual confounding has no upper bound you can
compute from the data.** A beautifully propensity-matched registry analysis can be balanced on
every recorded field and still be wrong by a wide margin, in the direction the allocation was made
in.

## What Metronome buys, and the forbidden list is the other half of it

`Cmd_metronome` is short and every part of it is doing one of two jobs.

It draws `(Random() & 0x1FF) + 1` — a uniform index into the move table — and retries if that
lands above the real move count, because 355 to 511 are not moves. Then it walks
`sMovesForbiddenToCopy` and, if the drawn move is on the list, draws again. The list begins
**Metronome**, **Struggle**, **Sketch**, **Mimic**, and then — this is the good part — a sentinel
named `MIMIC_FORBIDDEN_END`, after which come **Counter**, **Mirror Coat**, **Protect**,
**Detect**, **Endure**, **Sleep Talk**, **Thief**, **Follow Me** and **Snatch**.

Two things follow, and together they are the whole of trial design (**mechanism**):

* **The draw knows nothing about why you would have wanted the move.** It is not influenced by the
  level gap, the matchup or how the battle is going. That is what makes the comparison
  attributable, and it is the one thing no amount of analysis of your own log can manufacture.
  Randomisation does not make the groups identical; it makes them differ only by chance, and
  chance is a thing with a distribution. An unbounded unknown is traded for a quantified one.
* **The forbidden list is the eligibility criteria**, and the sentinel is the fact that different
  designs read different amounts of it. **Mimic** reads only up to `MIMIC_FORBIDDEN_END`;
  Metronome reads the whole thing. One pool, two procedures, two exclusion lists — which is
  exactly how two trials of the same disease end up with different populations and therefore
  different answers.

And the external-validity problem is in the same list. **The pool Metronome draws from is not a
pool anybody would play from.** Narrow eligibility is what makes the comparison clean and is also
what makes the result unlike real practice. That tension is not a flaw in trials; it is the price
of the thing they buy.

## The machinery that protects the draw, and what each piece does

These get run together and they do different jobs (**mechanism**, **consensus**).

**Allocation concealment** is the one whose failure is fatal: whoever enrols must not be able to
see or steer the next assignment. Note that Metronome's draw happens *inside* the move's own
routine, after the turn has been committed — the player does not get to see what came up and then
reconsider. It is **not** blinding, and it is required whether or not blinding is possible.

**Blinding** protects what happens after allocation, and **Team Preview** is the clean
counter-example: from the fifth generation on, both sides see both teams before the battle begins
and each adapts its lead to what it saw. Knowledge of the allocation changed the behaviour, and
nothing about the allocation itself had to be compromised for that to happen. Clinically, blinding
matters most for subjective or adjudicated endpoints and least for all-cause death — which is why
an open-label trial with a hard endpoint can be sound while an open-label trial with an assessed
endpoint is fragile.

**Intention to treat** is the **Choice Band**. Once the holder has used a move, `choicedMove` is
set and `CheckMoveLimitations` marks every other move unusable — the commitment is fixed at the
moment of the first choice and does not relax because the situation changed. **Thrash** and
**Outrage** are the same shape and worse: `EFFECT_RAMPAGE` runs its course whether or not it is
still a good idea, and their target field is `MOVE_TARGET_RANDOM`, so you do not even get to
redirect it.

Clinically, everyone is analysed in the arm they were allocated to, whatever they received, and
the reason is structural rather than conservative: any other analysis set is defined partly by
events that happened *after* randomisation, and selecting on those puts back exactly the
prognosis-dependent selection the draw removed. A per-protocol analysis answers a different
question and usually cannot answer it.

**Stratification and minimisation** balance strong prognostic factors across arms. They narrow the
spread and make the result more credible; they do not remove a bias, because the draw had already
dealt with bias in expectation.

**Pre-specification** fixes the endpoint, the analysis and any margin before the data are seen.
The **Damage Roll** argument from the response-assessment answer is why a margin has to be
declared and has to be wide: Emerald multiplies every hit by a whole number of per cent from 85 to
100, sixteen values drawn at random, so a difference smaller than the noise is not a difference.
And a declared margin is a **Regulation** set named in the invitation, not a number discovered
afterwards: it states how much worse the new option may be while still being worth having, and
whether that margin was reasonable is an argument rather than a calculation. **Failing to show
inferiority is not showing equivalence** — an underpowered trial fails to show most things.

One more, which is prior to all of it: a single-arm study reporting a response proportion cannot
support a comparative claim, however large the proportion, because there is nothing to subtract.
That is a narrower point than the one the response-assessment answer makes about imaging and
survival being different propositions, and it comes first.

## Where the log is the better instrument, and it genuinely is

A battle log is not a weak trial. It is a different instrument, and the **Vs. Recorder** and the
**Battle Video** exist precisely because some questions need one (**consensus**):

* **Generalisability.** Trial eligibility criteria select people who are younger, fitter and with
  fewer other conditions than the clinic — the forbidden list again. Whether a result transfers to
  the population actually being treated is a question a trial structurally cannot answer about
  itself, and a large unselected record can. * **Rare and late events.** A trial is too small and
  too short to see them. Late cardiac effects, second malignancies and uncommon severe toxicities
  are registry and pharmacovigilance questions. * **Patterns of care and inequity.** Who is
  offered what, who is referred, how long they wait, and how that varies by place and by
  deprivation are questions about the *system*. No trial asks them. * **Signal generation**,
  including the first hint that something is wrong with something already in use.

Where randomisation is genuinely impossible, specific designs partly substitute — natural
experiments, instrumental-variable approaches, and target-trial emulation with its assumptions
written down. Each swaps the assumption randomisation makes unnecessary for a different untestable
one, which is a reasonable bargain stated and a bad one hidden (**consensus** that they have a
role; genuinely contested how much weight they bear).

The honest summary: the log tells you what is happening, and the draw tells you what a move does.
Asking either to do the other's job is the error, and it is made in both directions.

## Where the metaphor stops

Everything above is allocation and record-keeping, and a game that computes its chances in
readable code is a good place to see what a selection step does to a log. What follows is about
people, so it is said plainly and without the analogy.

Someone deciding whether to enter a randomised trial is being asked to accept that the treatment
they get will be chosen by a process that is indifferent to them — specifically, personally, at a
moment when they would very much like somebody to choose on their behalf. That is a real thing to
ask of a person, and the inferential argument being correct does not make it easier. The ethical
basis for asking is genuine uncertainty about which arm is better, and where that uncertainty is
absent the question should not be asked at all.

Taking part also costs time: extra visits, extra investigations, extra forms, often more travel.
People take that on, frequently in the hope of helping others as much as themselves, and the
evidence that results is the reason anything in oncology has improved at all. That is worth saying
directly rather than folding into a methods section.

And the generalisability paragraph above is not an abstraction. Trials have historically
under-enrolled older people, people with other illnesses, and people from several ethnic and
socioeconomic groups, which means the evidence base is thinnest for some of the people who most
need it. That is a harm produced by how the evidence was gathered, not a limitation of arithmetic,
and it is being worked on rather than solved. No figure of any kind appears in either half of this
answer, and that is deliberate.

## What a Gym Leader is listening for

* The OHKO chance adds the level difference. Explain in one sentence why your own battle log
  overstates Horn Drill, without using the word *bias*.
* Lock-On and Sturdy both determine the outcome and neither is a field in the log. Which
  methodological problem is that, and why can it not be bounded?
* Metronome's draw and Metronome's forbidden list do two completely different jobs. Name both.
* Mimic reads only part of that list. What does the sentinel in the middle of it correspond to?
* Choice Band locks you into your first move. Which analysis convention is that, and why does it
  follow from the draw rather than being cautious?
* Team Preview compromises nothing about allocation and changes behaviour anyway. What distinction
  does that illustrate?
* Name three questions the Vs. Recorder answers better than any Metronome experiment could.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific
to this answer:

* A current standard textbook of clinical epidemiology or of clinical trial design, for
  confounding by indication, the limits of adjustment, and the distinction between allocation
  concealment and blinding.
* The reporting guideline for randomised trials, and the companion guideline for observational
  studies, published by the respective international reporting-guideline initiatives — the most
  compact statement of what each design must disclose and therefore of what each can support.
* The clinical trials guidance issued by your national medicines regulator and by your national
  research ethics framework, for what is required where you are. These differ between countries.
* Your national cancer registry's published methodology, for what it records, how completely, and
  what it explicitly does not support.
* The primary literature, for any claim about a specific trial and for the live methodological
  argument about target-trial emulation and real-world evidence.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about study design and inference, dressed in a game so that the effect
of a selection step on a record is concrete. It has had no clinical review. It is not a trial
protocol, not a statistical reference, and **not a guide to whether anybody should enter a trial**
— that is a conversation with the team looking after that person, who know the trial, the
eligibility criteria and the individual's circumstances, none of which are here. No effect size,
power calculation, margin, significance threshold or participation figure appears here and none
should be inferred. Regulatory and ethical requirements differ by country and are revised; yours
govern. Anyone affected by cancer — their own diagnosis or someone else's — should be talking to
their clinical team about what is open to them, which is a question with a local answer. The
analogy carries allocation and record-keeping only: the thing randomised in a trial is a person,
no part of this game stands in for one, and none of it says anything about what happens to
anybody.

## Where this stands, October 2026

The Pokémon facts are read from Emerald's own source. `Cmd_tryKO` computes the chance as the
move's accuracy plus the attacker's level minus the target's, requires the attacker's level to be
at least the target's, jumps to `BattleScript_SturdyPreventsOHKO` when the target has Sturdy, and
checks `STATUS3_ALWAYS_HITS` — which Lock-On and Mind Reader set — before any of that. Horn Drill
carries accuracy 30, power 1 and 5 PP in the move data. `Cmd_metronome` draws
`(Random() & 0x1FF) + 1`, retries when that exceeds the move count — with the source's own comment
noting that 355 to 511 are not valid moves — and rejects anything in `sMovesForbiddenToCopy`,
whose entries are quoted above in their file order, including the `MIMIC_FORBIDDEN_END` sentinel
that Mimic stops at. Choice Band's lock is in `battle_util.c`: once `choicedMove` is set,
`CheckMoveLimitations` marks every other move unusable. Thrash and Outrage are both
`EFFECT_RAMPAGE` at 90 base power with `MOVE_TARGET_RANDOM`. The damage roll of 85 to 100 is
established in the response-assessment answer in this specialty and is not re-derived here. Team
Preview, the Vs. Recorder, the Battle Video and Regulation sets are later-generation additions
described from working knowledge of those games rather than from code opened here, and are flagged
as such rather than left to imply otherwise.

The inferential core will not date. Confounding by indication, the limitation of adjustment to
recorded covariates, and the specific thing randomisation buys are properties of the logic rather
than of current practice.

What is genuinely active, and contested, is how much weight non-randomised evidence should carry.
Target-trial emulation, external and synthetic control arms, and registry-based comparative
analyses are all being argued over and are treated differently by different regulators, and the
pressure to use them is real — partly because some biomarker-defined populations are genuinely too
small for a conventional randomised trial. Trial designs are moving too: platform and basket
designs, adaptive allocation, decentralised conduct, and pragmatic trials embedded in routine care
as an attempt to get the draw and the generalisability at once. None of that changes the argument
above; all of it changes what the best available evidence for a given question looks like. No
regulator's current position is quoted here, deliberately — those move, they differ between
jurisdictions, and they belong to the regulator's own documents rather than to a revision note
like this one.
