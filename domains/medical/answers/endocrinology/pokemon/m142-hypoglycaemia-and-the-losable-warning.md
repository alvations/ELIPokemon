---
id: "m142"
slug: hypoglycaemia-and-the-losable-warning
style: pokemon
category: endocrinology
difficulty: advanced
question: "Why is hypoglycaemia in insulin-treated diabetes a failure of counter-regulation rather than simply too much insulin, and how is the warning itself lost?"
tags: [hypoglycaemia, counter-regulation, glucagon, impaired-awareness, diabetes]
---

# Nothing in Generation III takes the rain down, and the alarm that would warn you is a number written on an item rather than a property of the Pokémon

One thing first, because this topic needs it said before anything else. The bar in this answer is
the **controlled variable** — the quantity a loop is holding somewhere — exactly as it is in m022
and m023. It is not anybody's wellbeing, nothing here maps a bar reaching the bottom to anything
at all, and no Pokémon in this answer stands in for a person.

With that established: **Rain**. Weather is the glucose-control hormones in this specialty, which
m021 settled and m025 built on. `Cmd_setrain` writes `B_WEATHER_RAIN_TEMPORARY` into
`gBattleWeather` and sets `gWishFutureKnock.weatherDuration = 5`, and the end-of-turn handler
decrements that counter and clears the bit when it reaches zero (**mechanism**). Two details about
that are the first half of this answer.

A second **Rain Dance** into existing rain takes the failure branch — `gMoveResultFlags |=
MOVE_RESULT_MISSED` and a message saying it did not work — and **the duration is not refreshed**
(**mechanism**). And there is no move in Generation III that ends weather. None. Searching the
decompilation for anything that clears `B_WEATHER_RAIN_TEMPORARY` finds exactly one place: the
counter reaching zero at end of turn. **Air Lock** on **Rayquaza** and **Cloud Nine** on
**Psyduck** and **Golduck** suppress what the weather *does* while leaving the weather itself
standing, and weather set by **Kyogre**'s **Drizzle** carries the permanent bit and never
decrements at all.

So the field is committed. You can add nothing to it and you cannot take it away. The clock is the
only exit.

| In the battle | What it stands for |
| --- | --- |
| **Rain**, `weatherDuration = 5`, decremented at end of turn | Insulin already given, running its own clock |
| A second **Rain Dance** **failing** instead of extending | More of it does not shorten it, and the clock is not reset |
| No Generation III move clearing weather, anywhere | Defence layer one: switching the cause off, unavailable |
| **Kyogre**'s **Drizzle** carrying the permanent bit | A supply with no off state at all |
| **Swift Swim**: the same rain, twice the effect | Exercise, where the same dose does more |
| **Air Lock**, **Cloud Nine** — effect suppressed, field intact | Blocking the consequence without removing the cause |
| An **Oran Berry** / **Sitrus Berry** at `hp <= maxHP / 2` | A defence that engages at a threshold |
| A **Figy Berry**: same half, `maxHP / 8` back, and confusion | A rescue whose own size is a problem |
| A **Liechi Berry** at `maxHP / holdEffectParam`, param **4** | A second defence, written to a *lower* threshold |
| **Gluttony** moving a quarter-threshold Berry to a half | The threshold is a parameter, not a property |
| `gStatStageRatios`, thirteen entries, −6 to +6, nowhere displayed | The size of the remaining response, and its invisibility |
| **Haze** / `Cmd_normalisebuffs`, every battler back to default | Recovery by clearing rather than by effort |
| **Shield Dust**'s `!primary` clause | Something that blocks the warning and not the event |
| **Yawn**'s `STATUS3_YAWN`, landing at the end of the *next* turn | A commitment made now that arrives later |
| `CANCELER_ASLEEP`, and **Snore** and **Sleep Talk** | Asleep: the layer that needs an action is gone |
| An item firing while asleep, because it needs no action | The layer that does not need an action is not |
| **Early Bird** subtracting 2 from the counter | A faster clock, which is not a smaller need |
| `CheckMoveLimitations` — one grey slot, eighteen causes | Defences unavailable for unrelated reasons |
| A **Persim Berry**, which clears confusion and nothing else | A rescue scoped to exactly one consequence |
| A **Lum Berry**'s `ITEM3_STATUS_ALL` | The broad-spectrum version of the same act |
| **Metagross**'s **Clear Body**, **Torkoal**'s **White Smoke** | What refuses to let the response be eroded |
| **Arbok**'s **Intimidate**, one stage on entry | Erosion arriving from outside, a step at a time |
| **Snorlax** learning **Rest** and **Snore** together | The restorative, and what works through it |

**This answer defers to three others.** m022 owns the open loop, the committed depot and the
asymmetric cost; m023 owns what a continuous record made visible; m090 owns **Shield Dust**'s
`!primary` clause against **Safeguard**'s side-status check. All three appear here and none is
re-argued.

Clinical claims are marked (**mechanism**), (**definitional**), (**consensus**) or
(**country-dependent**). The Pokémon mechanics carry no clinical marker; the Sources section says
which decompilation each came from.

## Two thresholds in one generation's code, and nothing at the top

Here is the part of the Advance source that makes this answer work. Berries fire from
`ItemBattleEffects`, and the restorative ones and the stat ones are written with **different
thresholds**:

```
   HOLD_EFFECT_RESTORE_HP        if (hp <= maxHP / 2 && !moveTurn)
      Oran Berry   param 10         restores a FLAT amount
      Sitrus Berry param 30         ── Generation III: flat, not a fraction

   TRY_EAT_CONFUSE_BERRY(flavor) if (hp <= maxHP / 2 && !moveTurn)
      Figy Berry   param 8          restores maxHP / 8
                                    AND confuses, if the flavour disagrees
                                    with the personality value

   TRY_EAT_STAT_UP_BERRY(stat)   if (hp <= maxHP / holdEffectParam && !moveTurn
                                     && statStages[stat] < MAX_STAT_STAGE)
      Liechi Berry param 4           ── a QUARTER. Lower than the other two.

   ── and every one of them is gated on !moveTurn: the check runs at the
      end of the turn and not in the middle of an action ──
```

Three things fall out of that and all three are the clinical structure (**mechanism**).

**The threshold is a number written on an item, not a property of the Pokémon.** `maxHP /
holdEffectParam` — the level at which a defence engages is a parameter, and two defences carried
by the same Pokémon in the same generation engage at different levels. That is the ordered stack:
the layers are not graded versions of one thing, they are separate mechanisms with separate
trigger levels, and the ordering is what makes them a stack rather than a pile.

**The lower threshold is the stat-raising one**, which is the right way round for this analogy and
worth dwelling on. The defence that engages *later* is the one that changes how the Pokémon
performs rather than restoring the bar. In the real stack, the layer that engages late is also the
one that produces the warning — one mechanism, two jobs, which the serious half calls a structural
fragility. Anything that quietens it quietens both.

**A rescue can carry its own cost.** The **Figy Berry** restores an eighth and then **confuses**,
if `GetFlavorRelationByPersonality` returns a negative relation for that flavour — a
per-individual fact fixed when the Pokémon was created (**mechanism**). The real version of that
is not confusion; it is that treating a low is easy to overshoot, which produces the opposite
problem and then a destabilised trace. The serious half does not dwell on it and nor will I. The
structural point is that a defence is not free, and the games put the cost in the same macro as
the benefit. They also put the remedy for the cost in a second item: a **Persim Berry** clears
confusion and nothing else, while a **Lum Berry** carries `ITEM3_STATUS_ALL` and clears any of it
— a narrow rescue and a broad one, which is m003's **Antidote** distinction from nursing arriving
in the berry pocket.

And then the thing that is **not** there. In that whole table there is no entry for "stop the
rain". No Berry, no ability, no item in Generation III does it. The defence that works by removing
the cause does not exist in the code, and it does not exist in insulin treatment either, and that
is layer one (**mechanism**).

## Layer one is missing, layer two is an unavailable move, and the grey is the same grey

The second layer is the one that opposes the fall actively. In the battle that is a *move*, and a
move can be unavailable for reasons that have nothing to do with the move.

`CheckMoveLimitations` is a single `else if` chain, **eighteen branches long** in the current
expansion: an empty slot, zero PP, a placeholder effect, **Disable**, **Torment**, **Taunt**,
**Imprison**, **Encore**, a **Choice Scarf** lock, an **Assault Vest**, **Gravity**, **Heal
Block**, **Belch**, **Throat Chop**, **Stuff Cheeks**, Gorilla Tactics, the can't-use-twice flag,
and a final branch that opens into a switch (**mechanism**). The Advance version of the same idea
was five named mechanics in eight ORed conditions. The list has grown by a factor of two and **the
readout has not changed at all**: one slot, greyed out, with nothing on the screen saying which
branch did it.

That is the shape of a defence that is simply not available. An empty slot and a slot greyed out
by **Imprison** look nothing like each other in the data and identically on the screen. The
glucagon response to a fall is lost early in type 1 diabetes, and lost **specifically to that
stimulus** while the capacity to secrete in response to other things may be intact (**consensus**)
— which is precisely the shape of a greyed-out slot rather than an empty one. The move is in the
moveset. The Pokémon knows it. It cannot be selected right now, and the reason is in a store you
are not looking at.

## Gluttony moves the threshold, and nothing moves it the other way

So the thresholds are parameters. Can anything change one during a battle? Yes, once, in one
direction:

```
   if (hpFraction <= 4 && GetItemPocket(itemId) == POCKET_BERRIES
        && gBattleMons[battler].hp <= gBattleMons[battler].maxHP / 2
        && IsAbilityAndRecord(battler, GetBattlerAbility(battler), ABILITY_GLUTTONY))
       return TRUE;
```

**Gluttony** takes a Berry written to a quarter and fires it at a **half** instead
(**mechanism**). The **Liechi Berry** is unchanged. **Gluttony** has moved the level at which the
alarm sounds, upward — earlier, with more of the bar left.

That is one half of the real phenomenon exactly. In somebody whose glucose has been running high
for a long time, the symptomatic threshold shifts **up**, so the warning arrives at a level that
is not low and arrives unmistakably (**consensus**). **Gluttony** is that, and it demonstrates the
thing worth proving: the trigger level is a variable, not a damaged setting.

And here the games give me nothing for the direction that matters most, so I will say so rather
than invent it. **There is no ability anywhere that moves a Berry threshold down.** Nothing in the
code makes an alarm fire later than its parameter says, and nothing makes the parameter drift with
history. The real system does exactly that — recent hypoglycaemia lowers the level at which the
warning engages, repeatedly, until the warning can arrive at or below the level at which thinking
is already affected (**consensus**) — and I have no mechanic for it. **Gluttony** run backwards is
not a mechanic; it is a wish. The next section is what the games *do* give me, which is the
**size** of the response rather than its trigger level.

## Thirteen entries, and not one of them is displayed

`gStatStageRatios` is thirteen rows long and it is worth reading as data rather than as a rule:

```
   stage   −6    −5    −4    −3    −2    −1     0    +1    +2  …  +6
   ratio  10/40 10/35 10/30 10/25 10/20 10/15 10/10 15/10 20/10 … 40/10
          ÷4                                   ×1                ×4
```

A stat stage is not a stat (**mechanism**). It multiplies the computed value and is stored nowhere
on the Pokémon; `Cmd_normalisebuffs` — which is **Haze** — writes `DEFAULT_STAT_STAGE` into every
stat of **every battler on the field**, and switching out discards the stages too.

Three properties, and each carries a clinical fact.

**It degrades one step at a time, and the steps are not equal.** From 0 to −1 costs a third of the
value; the step from −5 to −6 is a much smaller absolute loss on an already small number. A
defence that has been eroded repeatedly loses most of its size early and then declines slowly into
near-uselessness, which is why a history of several episodes matters more than a history of one.

**Nothing on the screen is the number.** There is no readout of the current stage anywhere in the
interface. You infer it from damage that came out lower than you expected — which is to say **you
find out what the stage was by needing it**. That is impaired awareness stated as a data-storage
fact: the person does not know the warning has gone until the occasion on which it fails to arrive
(**mechanism**).

**It is cleared, not rebuilt.** **Haze** does not raise anything. It deletes the modifiers and
lets the stored value show through, and the stored value was never damaged. That is the most
consequential claim in the serious half: the threshold shift is **functional**, and scrupulous
avoidance of hypoglycaemia over a period restores symptomatic awareness and some of the
counter-regulatory response (**consensus**). The underlying machinery was not broken. It was being
multiplied by 10/40 and nobody could see the multiplier.

The honest limit, here where it is used: **Haze** is instantaneous and real recovery is not — it
takes a sustained period of avoidance, and how complete it is and how fast differs between people
and is where the evidence is least precise (**consensus**). And a **stat stage** does not degrade
by itself from being used. **Intimidate** on an **Arbok**, an **Icy Wind**, a **Growl** —
something from outside has to lower it, and the games even provide the refusal: **Metagross**'s
**Clear Body** and **Torkoal**'s **White Smoke** block an opposing stage drop outright, which is
the closest the cartridge comes to the real protective measure, since the only reliable way to
keep the response is not to spend it. The real loop lowers its own defence as a *consequence of
the defence being needed*, and no single mechanic in Pokémon does that; the nearest honest
statement is that the thing lowering the stage and the thing the stage was defending against are
the same event, which the games never arrange.

## Yawn, and what still fires when nothing can act

**Yawn** is the best mechanic in the cartridge for the overnight case. `STATUS3_YAWN` is set now
and does nothing now; the counter is decremented at end of turn, and when it empties the battler
is put to sleep for `(Random() & 3) + 2` turns — two to five (**mechanism**). It fails outright if
there is already a status, or against **Insomnia** or **Vital Spirit**, or while an **Uproar** is
running. A commitment made on one turn, landing on a later one, with the decision long since made.

And then `CANCELER_ASLEEP`, which is where the two layers separate cleanly:

```
   CANCELER_ASLEEP:
      decrement the sleep counter   (by 2 if the ability is EARLY BIRD)
      if still asleep:
          if the chosen move is not SNORE and not SLEEP TALK
              → HITMARKER_UNABLE_TO_USE_MOVE.  The action does not happen.
```

**A move requires being awake. An item does not.** The Berry checks in `ItemBattleEffects` test
the bar and `!moveTurn` and nothing else — a sleeping Pokémon still eats its **Sitrus Berry** at a
half, because eating it is not an action it takes (**mechanism**). **Snore** and **Sleep Talk**
are the two named exceptions and they are exceptions precisely because somebody wrote them into
the condition. m043 made the same point from the other end, with **Snorlax** learning **Rest** and
**Snore** as a pair: the restorative and the one thing that still works through it arrive
together.

That is the overnight problem with no padding. The behavioural layer needs an awake person who
notices, decides and reaches something, and sleep removes all three; the hormonal layer does not
need any of them, and during sleep the sympathoadrenal response to a fall is **also** reduced
(**consensus**). Both remaining layers are at their weakest simultaneously, which is why overnight
episodes were largely invisible until a continuous record existed to show them — m023's argument,
arriving at its most useful case.

**Early Bird** is the footnote that m074 already drew in nursing: it subtracts 2 from the counter
instead of 1. It is a faster clock, not a smaller need, and it changes nothing about what was
unavailable while the counter was running.

## Rain that does more than it did, and effects blocked without the cause being touched

Two short ones that complete the picture.

**Swift Swim** doubles its holder's Speed while rain is up (**mechanism**). The rain has not
increased. The same field is producing twice the effect because something about the battler
changed. That is exercise: glucose utilisation rises during activity and insulin sensitivity stays
raised for many hours afterwards, so a dose given in the morning does more in the evening than it
did when it was given (**consensus**). And the field's clock keeps running regardless — weather
outlives the thing that set it, which is m009's **Drizzle** device and the reason the long tail is
the hazard rather than the activity.

**Air Lock** and **Cloud Nine** suppress what weather does and leave the weather bit set
(**mechanism**). The field is still raining; nothing reads it. m090's **Shield Dust** is the
sharper version of the same idea: its clause requires `!primary`, so it blocks a secondary effect
and lets a primary one straight through — which is why it stops some things and not
**Will-O-Wisp**. Something that removes the signal and not the state is a recognisable category,
and beta-adrenoceptor blockade attenuating adrenergic symptoms without touching the glucose
belongs to it (**consensus**).

## The mapping I am declining

Three refusals.

**Nothing here stands in for a frightened person, and nothing stands in for a severe episode.**
This is the topic in the specialty where that line is nearest, and the rule is not negotiable: a
bar reaching the bottom maps to nothing in this answer, fainting maps to nothing, and there is no
mechanic anywhere above for seizure, for loss of consciousness, or for somebody else having to
help. Those are in the plain prose below, said directly, and the reason they are there rather than
here is that whimsy about a mechanism is useful and whimsy about an outcome is grotesque.

**I am not using confusion as fear.** The **Figy Berry** confuses, and the temptation to read that
as the cognitive state of a person in the middle of an episode is obvious and it is wrong — it
would put a creature in the place of somebody impaired and distressed. I used the **Figy Berry**
for the one thing it legitimately carries, which is that a rescue has its own cost written into
the same macro, and stopped.

**And I am not inventing a mechanic for the threshold that drifts.** The section above says this
where it matters rather than here, which is the convention this specialty has settled on.
**Gluttony** moves an alarm level in one direction and nothing in the games moves one in the
other, so the central phenomenon of this topic — a warning level that falls each time the warning
is used — has no mechanic and gets a plain statement instead. That costs this answer the cleanest
picture it could have had, and inventing a hold effect for it would have been a lie about a
cartridge in an answer about a thing people are hurt by.

## Where the metaphor stops

It stops here, and the rest of this section has no Pokémon in it.

Everything above is a picture of a committed input with its own clock, a stack of defences with
separate trigger levels written as parameters, a response whose magnitude is multiplied by
something nothing displays, and two settings — asleep, and after exertion — in which the remaining
defences are weakest at the same time. The picture is fair. What follows is what the picture
cannot carry.

Hypoglycaemia is frightening while it happens and frequently frightening afterwards. Mild episodes
are disruptive, exhausting and embarrassing in public. Severe episodes can cause seizure, loss of
consciousness and death. Somebody who has had a severe episode — or who has watched one happen to
somebody they love — afterwards lives with knowing it can happen again, and the mechanism
described above is specifically a mechanism for losing the warning that it is about to.

So fear of hypoglycaemia is a rational response to an accurately judged hazard. It is routinely
written down as non-adherence, as poor control, or as anxiety. Somebody running their glucose
deliberately high because an episode once arrived with no warning is not failing to understand the
risk; they are trading one risk against another using information about themselves that no
printout contains.

Impaired awareness also has consequences that are not clinical. Driving is regulated specifically
in many countries, the rules differ and they change, and they are a matter for the licensing
authority where somebody lives and for their own clinical team. Nothing resembling those rules is
on this page.

And the cost does not fall only on one person. Help during a severe episode usually comes from a
partner, a parent, a colleague or a stranger, and the people who give it remember it. That belongs
in any honest account of what this diagnosis costs.

A note about who is reading. Anybody reading about hypoglycaemia is more likely to be living with
it than revising it. If that is you: there are deliberately no glucose numbers, thresholds or
targets anywhere on this page, and nothing here is about your regimen. If an episode is happening
now, treat it the way your own team has agreed with you. If somebody cannot be roused or is having
a seizure, call emergency services. And if episodes are arriving without warning, that is a
specific reason to contact your own team — because that state is treatable, and it is not
something to be endured more carefully.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

See [`../../../for-agents/SOURCES-endocrinology.md`](../../../for-agents/SOURCES-endocrinology.md)
for the standing documents of this specialty. Specific to this answer:

* Your national or specialty-society guidance on hypoglycaemia in diabetes, for how episodes are
  classified and graded, how awareness is assessed, and what is recommended when awareness is
  impaired.
* **Your own institution's protocol** for treating hypoglycaemia, including in somebody who cannot
  swallow or cannot be roused. No treatment appears here and that protocol is the authority.
* Your national or specialty-society guidance on glucose monitoring and automated insulin
  delivery, for eligibility — in several countries impaired awareness is itself one of the
  grounds, and the criteria differ.
* **The driving and licensing authority where you live.** Those rules are statutory,
  country-specific and revised.
* A current textbook of diabetes or endocrine physiology, for the ordered defence stack, the
  specificity of the lost glucagon response, and the experimental basis of the bidirectional
  threshold shift.
* **The primary literature**, for how completely and how quickly impaired awareness reverses,
  which is the claim this answer is least able to make precise.

The Pokémon side is different and is sourced properly. `Cmd_setrain` writing
`B_WEATHER_RAIN_TEMPORARY` with `gWishFutureKnock.weatherDuration = 5`, taking the
`MOVE_RESULT_MISSED` branch on existing rain without refreshing the counter, and the end-of-turn
decrement being the only thing in the Advance source that clears that bit; the permanent bit on
**Kyogre**'s **Drizzle** never decrementing; `HOLD_EFFECT_RESTORE_HP` firing at `hp <= maxHP / 2
&& !moveTurn` with the **Oran Berry**'s `holdEffectParam` of 10 and the **Sitrus Berry**'s flat 30
in Generation III; `TRY_EAT_CONFUSE_BERRY` firing at the same half, restoring `maxHP /
holdEffectParam` with the **Figy Berry**'s param of 8, and confusing on a negative
`GetFlavorRelationByPersonality`; `TRY_EAT_STAT_UP_BERRY` firing at `maxHP / holdEffectParam` with
the **Liechi Berry**'s param of 4 and its `statStages[stat] < MAX_STAT_STAGE` guard;
**Gluttony**'s condition in the expansion moving a quarter-threshold Berry to a half;
`gStatStageRatios`' thirteen rows from 10/40 to 40/10 and `Cmd_normalisebuffs` writing
`DEFAULT_STAT_STAGE` to every stat of every battler; **Yawn** setting `STATUS3_YAWN` and producing
`(Random() & 3) + 2` turns of sleep, failing against an existing status, **Insomnia**, **Vital
Spirit** or an **Uproar**; `CANCELER_ASLEEP` subtracting 2 under **Early Bird** and setting
`HITMARKER_UNABLE_TO_USE_MOVE` for anything but **Snore** and **Sleep Talk**; **Cloud Nine** being
on **Psyduck** and **Golduck**; and `CheckMoveLimitations`' eighteen branches in the current
expansion against the Advance version's eight ORed conditions were all read from the pokeemerald
and pokeemerald-expansion decompilations rather than from memory. **Gluttony**, **Heal Block** and
**Gravity** are Generation IV or later and a **Damp Rock** is too; **Shield Dust**'s `!primary`
clause is the Advance implementation. The claim that **nothing** in Generation III clears weather
was checked by searching for every write that clears the weather bits, and the end-of-turn
duration tick is the only one.

## Scope and safety

The Pokémon here is doing one job: making it concrete that a layered defence has separate trigger
levels written as parameters, that the response's magnitude is multiplied by something nothing
displays, and that the layer which needs an action and the layer which does not fail in different
circumstances. It is not a clinical reference, not a decision aid, not a treatment protocol, and
not about any individual's care. **No glucose values, thresholds, targets, carbohydrate
quantities, doses or agents appear here on purpose** — a number on this page would be read as a
threshold by somebody who needed their own, and the levels that matter are individual and are set
with a clinical team. Check your own institution's protocol and your national guidance. Nothing
here has had clinical review. No Pokémon in this answer stands in for a person, for an episode, or
for an outcome, and hypoglycaemia that is happening now is not a reading problem.

## What a Gym Leader digs into next

* Why does a second **Rain Dance** fail instead of extending, and why is that the whole of layer
  one?
* Why is a threshold written on the **item** rather than on the Pokémon, and what does that make
  the defence stack?
* Why is the **Liechi Berry**'s quarter the right way round for this analogy?
* Why does **Gluttony** prove the trigger level is a variable, and why can the games not run it
  backwards?
* Why is "nothing displays the stat stage" the same statement as impaired awareness?
* Why does **Haze** clear rather than raise, and what does that say about what is recoverable?
* Why does a **Sitrus Berry** fire while its holder is asleep when a move does not?
* Why does **Swift Swim** mean the same rain is doing more, and why is the tail the hazard?

## Where this stands, October 2026

The committed input with its own clock, the ordered thresholds, the one-grey-many-causes readout,
the difference between a multiplier and a stored value, and the separation between a defence that
needs an action and one that does not are mechanism and do not date. What dates on the Pokémon
side is the constants and the cast: the five-turn weather duration and the flat **Sitrus Berry**
are Generation III and both changed later — pinch-Berry thresholds and the **Sitrus Berry**'s
percentage restoration are Generation IV revisions; **Gluttony**, **Gravity** and **Heal Block**
are Generation IV additions; weather-setting items and later weather rules changed the "nothing
clears it" claim, which is specifically an Advance claim; and `CheckMoveLimitations` has grown
from eight conditions to eighteen branches and will grow again. Check the current generation's
data. On the clinical side every number moves — classification and grading of episodes, awareness
instruments, glucose values and targets, treatment protocols, technology eligibility, education
programme content, and the statutory driving rules, which are revised independently of any
clinical guideline. Check current local guidance, your own institution's protocol and the
licensing authority where you live.
