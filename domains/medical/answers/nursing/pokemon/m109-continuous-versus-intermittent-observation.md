---
id: "m109"
slug: continuous-versus-intermittent-observation
style: pokemon
category: nursing
difficulty: advanced
question: "What does continuous monitoring actually buy over intermittent observation, and why is detection not the limb that usually fails?"
tags: [monitoring, observations, alarm-fatigue, escalation, deterioration]
---

# The alarm is one bit off a 48-pixel band, and a second battler in trouble gets no alarm.

Emerald has a continuous monitor with an audible alarm, and it is implemented in about thirty
lines. Reading them is the fastest route into why "more monitoring" is not the same thing as
better care.

Markers used below, because this half carries clinical claims. (**mechanism**) means it follows
from the structure of the measurement; (**definitional**) is what the word means; (**consensus**)
is mainstream agreement across major guidance; (**country-dependent**) means the reader's own
policy decides. Code blocks carry no marker. No interval, alarm limit or monitoring threshold
appears anywhere here.

## The alarm's threshold is a property of the display, not of the thing it watches

```
   u8 GetScaledHPFraction(s16 hp, s16 maxhp, u8 scale)
   {
       u8 result = hp * scale / maxhp;
       if (result == 0 && hp > 0)
           return 1;                      ◄── never reports zero while anything remains
       return result;
   }

   u8 GetHPBarLevel(s16 hp, s16 maxhp)
   {
       if (hp == maxhp)                               result = HP_BAR_FULL;
       else {
           u8 fraction = GetScaledHPFraction(hp, maxhp, B_HEALTHBAR_PIXELS);
           if      (fraction > (B_HEALTHBAR_PIXELS * 50 / 100))  result = HP_BAR_GREEN;
           else if (fraction > (B_HEALTHBAR_PIXELS * 20 / 100))  result = HP_BAR_YELLOW;
           else if (fraction > 0)                                result = HP_BAR_RED;
           else                                                  result = HP_BAR_EMPTY;
   ──────────────────────────────────────────────────────────────────────────────────────────
   The band is computed from the PIXEL fraction, not from the HP. `B_HEALTHBAR_PIXELS` is 48 —
   m001's number, and the same 48 m063 finds the Flail table reusing. So the alarm limit is
   a property of how wide the bar is drawn, and because the forced `return 1` means the
   fraction is never zero while any HP remains, HP_BAR_EMPTY is unreachable in a live
   battler: the RED band holds EVERYTHING from the 20 per cent edge down to one point.
```

That is the first and largest cost of a threshold alarm. **It has no severity and no rate.** The
alarm at the top of the red band and the alarm at the bottom of it are the same alarm, played at
the same volume, with nothing distinguishing a battler that has just crossed from one that has
almost nothing left. A monitor converts a continuous quantity into a binary, and the binary is all
it can transmit.

And because the band is a *proportion*, the same alarm means a different quantity in different
subjects. **Blissey**'s base HP is **255**; **Magikarp**'s is **20**; **Wailord**'s is **170**.
The 20 per cent edge of the red band sits at a completely different number of points in each of
them, so one threshold, applied uniformly, reports a different amount of remaining reserve
depending on who it is attached to. That is m006's **Super Fang** problem — a proportion and an
absolute are not the same quantity — arriving at the alarm limit rather than at the dose, and it
is the argument for setting limits per person instead of accepting the ward default.

## One bit latches it, and a second battler crossing the line gets nothing

```
   void HandleLowHpMusicChange(struct Pokemon *mon, u8 battler)
   {
       if (GetHPBarLevel(hp, maxHP) == HP_BAR_RED)
       {
           if (!gBattleSpritesDataPtr->battlerData[battler].lowHpSong)
           {
               if (!gBattleSpritesDataPtr->battlerData[BATTLE_PARTNER(battler)].lowHpSong)
                   PlaySE(SE_LOW_HEALTH);          ◄── read the condition above it
               gBattleSpritesDataPtr->battlerData[battler].lowHpSong = 1;
           }
       }
   ──────────────────────────────────────────────────────────────────────────────────────────
   In a double battle, if the PARTNER's alarm bit is already set, the second battler crossing
   the threshold plays NO SOUND AT ALL. Its own bit is still set — the state is recorded — but
   nothing announces it. One alarm covers two battlers, and the second crossing is
   audibly indistinguishable from nothing happening at all.
```

Alarm coalescing, implemented in one `if`. And then the stop condition:

```
   void BattleStopLowHpSound(void)
   {
       ... lowHpSong = 0;  (both, in a double)
       m4aSongNumStop(SE_LOW_HEALTH);
   }
   ──────────────────────────────────────────────────────────────────────────────────────────
   Called twice inside `HandleEndTurn_BattleWon` — once on the Frontier branch, once on the
   local-trainer branch. The alarm is silenced BY WINNING, by an event somewhere else
   entirely, and not by the battler it was about getting better.
```

The clinical content is the same shape. A threshold alarm on a noisy single channel produces
non-actionable alarms at a rate set by where the threshold sits, and in monitored clinical areas
most alarms are not actionable. (**consensus**) The documented consequences are desensitisation,
slower response, limits widened to stop the noise, and alarms switched off; harm has been
attributed to it, and it has been the subject of national safety alerts in more than one country.
(**consensus**; the alerts are (**country-dependent**).) Alarm fatigue is a property of the
system's design, not of the staff's attitude. (**mechanism**)

## The monitor watches one channel, and the readout lags the state

```
   static void UpdateStatusIconInHealthbox(u8 healthboxSpriteId)
   {
       ...
       status = GetMonData(&gPlayerParty[...], MON_DATA_STATUS);
       if      (status & STATUS1_SLEEP)     ... SLP
       else if (status & STATUS1_PSN_ANY)   ... PSN
       else if (status & STATUS1_BURN)      ... BRN
       else if (status & STATUS1_FREEZE)    ... FRZ
       else if (status & STATUS1_PARALYSIS) ... PRZ
       else { statusGfxPtr = GetHealthboxElementGfxPtr(HEALTHBOX_GFX_39); ... return; }
   ──────────────────────────────────────────────────────────────────────────────────────────
   One field read, five branches, and an else that draws the blank. m102 counts nine
   end-of-turn HP sinks held in five different stores against this one function reading one
   of them — so four of the nine are invisible on screen while they are happening. The
   display is not a summary of the state. It is a summary of ONE FIELD of the state.
```

Name the two groups and the gap becomes impossible to unsee. The five things that *do* draw an
icon are the `status1` bits, and the moves that set them are ordinary: **Spore** for sleep,
**Will-O-Wisp** for burn, **Thunder Wave** for paralysis, **Ice Beam**'s secondary for freeze,
**Toxic** and its relatives for the two poison bits that share one graphic — which is m024's and
m054's device, two trajectories under one PSN icon.

Everything else that changes HP at the end of a turn lives somewhere the healthbox never reads:

```
   what it does at end of turn      which store holds it            drawn on the healthbox?
   ──────────────────────────────── ─────────────────────────────── ────────────────────────────
   Leech Seed drains                 STATUS3_LEECHSEED, bit 2 of    no
                                     gStatuses3
   Ingrain heals                     STATUS3_ROOTED, bit 10 of the  no
                                     same word
   Nightmare drains                  STATUS2_NIGHTMARE, bit 27      no
   Curse drains                      STATUS2_CURSED, bit 28         no
   Bind, Clamp, Fire Spin,           STATUS2_WRAPPED, bits 13-15    no
   Whirlpool and Wrap drain          (three bits: it is a counter)
   Sandstorm and Hail damage         gBattleWeather, a global       no — and it is on the field,
                                                                    not on the battler at all
   Leftovers heals, Rain Dish heals  the held item and the Ability   no
   ─────────────────────────────────────────────────────────────────────────────────────────────
   Seven rows, four stores, and not one of them has a pixel. The alarm fires on HP, so a
   battler losing HP to any of these sets off the same single sound with no indication of
   which. And m001's point is the limiting case: Slaking's Truant is a standing property that
   decides whether it can act at all, and there is nothing anywhere on the healthbox for it.
```

And `CalcNewBarValue` adds the latency. The displayed bar holds its own `*currValue` and is moved
toward the real figure by a fixed step per call, returning `-1` only once it has caught up. What
is on the screen is therefore behind what is in memory, by a delay that is a property of the
animation and not of the battler. A monitor's reading is a measurement plus a transport delay,
always.

That is the second cost: **a monitor narrows while it deepens.** It watches one or two channels at
high rate and nothing else at all, and the attention it attracts is attention moved off the
person. The best-attested independent signal of deterioration is a clinician's or a relative's
concern that someone does not look right, which is why concern-based escalation sits in guidance
beside the numbers — and it is not a channel any monitor has. (**consensus**)

## The sampling rate belongs to the turn, and nothing can change it

`TurnBasedEffects` is the end-of-turn pass, and its case list is a roster. Eleven field-level
cases first — the ordering, then **Reflect**, **Light Screen**, **Mist**, **Safeguard** and
**Wish**, then the four weather clocks and a count — and then nineteen per-battler cases before
the one that ends the loop, which in move terms are **Ingrain**, the Abilities, held items twice
over, **Leech Seed**, poison, bad poison, burn, **Nightmare**, **Curse**, the **Wrap** family,
**Uproar**, **Thrash**, **Disable**, **Encore**, **Lock-On**, **Charge**, **Taunt** and **Yawn**.
The whole list runs **once per turn, in that fixed order, regardless of how much happened during
the turn.** A battler hit three times in a double battle still gets exactly one **Leftovers**
tick, because the tick rate is set by the turn structure and not by the event rate.

```
   event duration vs the turn            what the end-of-turn pass sees
   ───────────────────────────────────── ──────────────────────────────────────────────────────
   slower than a turn                    catches it, and catches it repeatedly
   about one turn                        catches it late, and cannot give you a rate
   entirely inside one turn              nothing. No case fires, no message prints, and the
                                          state at the end of the turn is a true record
   ──────────────────────────────────────────────────────────────────────────────────────────
   A normal reading is a negative finding about an INSTANT. It is routinely read as a negative
   finding about an INTERVAL, which is m073's pertinent-negative collapse reaching the same
   place by a different road.
```

And here the games have nothing, which is worth saying where the device is used. **There is no
mechanic for changing the sampling interval.** No item, move or ability makes the engine check one
battler more often than another; the turn is the turn. The clinical answer to this whole question
is an **individualised monitoring plan** — what is watched, how often, by whom, what change
triggers what, and when the plan is reviewed (**consensus**; the format is
(**country-dependent**)) — and the cartridge has no object that corresponds to it. The commonest
real defect is exactly the engine's behaviour: the frequency is set by the ward's routine rather
than by the person's trajectory.

## The limb the alarm cannot reach

Every mechanism above is detection. Not one of them is a response. `PlaySE(SE_LOW_HEALTH)` does
nothing to the battler, nothing to the turn order and nothing to the outcome; it is a speaker.
Whether anything happens next depends entirely on the player, who may be looking at the move menu.

The response to deterioration is conventionally split into an **afferent limb** — measure, record,
recognise, escalate — and an **efferent limb** — someone answers, attends, assesses and acts.
(**definitional**, from the rapid-response literature.) The recurring finding in reviews of
in-hospital deterioration is that abnormal observations were frequently present and documented
beforehand, and that the failure lay in recognition, escalation or response rather than in
detection. (**consensus**)

```
   the chain                        limb       what continuous monitoring changes
   ──────────────────────────────── ────────── ──────────────────────────────────────────────
   the measurement is taken          afferent   it is taken constantly instead of hourly
   it is recorded                    afferent   automatically, and in more detail
   the threshold is recognised       afferent   an alarm sounds — subject to everything above
   escalation is made                ────────   NOTHING. This is the boundary and the
                                                 commonest point of total failure
   somebody answers                  efferent   nothing
   they attend and assess            efferent   nothing
   a decision is made and done       efferent   nothing
   ─────────────────────────────────────────────────────────────────────────────────────────
   Three rows improved, four untouched, and the failures are in the four. Where the efferent
   limb is the bottleneck, improving the afferent one produces a longer record of a
   deterioration nobody acted on — and a continuous record nobody read is WORSE than none,
   because it documents in detail that the information was available. (mechanism)
```

So the interventions that change outcomes here are the unglamorous back-half ones: an escalation
route that always answers, a threshold that needs no permission to use, a response team with the
authority to act, and a culture where escalating and being wrong is cheap. m002 is the full
argument about why the criteria are written as numbers; this is why the numbers are not the part
that fails.

One last limit from the code, because it is exactly the clinical trap.
`HandleBattleLowHpMusicChange` calls the alarm only for `B_POSITION_PLAYER_LEFT` and
`B_POSITION_PLAYER_RIGHT`. The opposing side's HP never makes a sound at all. A monitor is
attached to one part of the room, and the absence of an alarm is evidence about that part and
about nothing else. m107's version of this is the one that bites hardest: a saturation inside a
target range is fully compatible with a rising carbon dioxide, so a continuously normal channel
can accompany a deterioration the monitor has no access to. (**mechanism**, **consensus**)

## Where the metaphor stops

It stops completely at continuous human observation, and that is the half of this subject the
analogy must not be allowed near.

Enhanced, constant or one-to-one observation is often discussed as the maximum setting of the same
dial. It is not. What it buys is the capacity to intervene inside the duration of the event — a
fall takes a fraction of a second, and no monitor shortens that — along with orientation,
reassurance and noticing everything that is not on a channel. Its costs are different costs: it is
experienced as surveillance; it is frequently allocated to the least experienced person available,
which inverts the skill requirement; it is expensive, so it is rationed by availability rather
than by need; and it can substitute for addressing the cause, containing a consequence while the
reason continues. It needs an indication, a review point and a plan for stopping.

Being watched is not a neutral experience, and the people most likely to be continuously observed
are those least able to consent to it or to object. From the inside it can be being guarded rather
than being cared for, and almost the whole difference is whether the person doing it talks to
them, explains what is happening, and treats it as time spent with somebody rather than a shift
spent on a chair.

Where observation is in place because of risk to the person themselves — self-harm, severe
distress, a mental-health crisis — the subject sits inside a legal and ethical framework about
capacity, consent, restriction of liberty and least restrictive practice. That framework differs
profoundly between countries, it is not a bedside judgement, and nothing in a revision answer,
least of all one built out of a video game, should be used to reason about it. The reader's own
legal framework and safeguarding route are the only authority. It is named here rather than
explained here, because leaving it out would misrepresent what the word "observation" covers.

Two smaller things that belong to real people. Alarms are experienced and not only responded to:
continuous audible alarms are a documented cause of sleep deprivation in hospital, sleep
deprivation is a delirium precipitant, and the person in the next bed is awake too. And being
monitored is often understood by patients and families as being watched over, so taking a monitor
off — usually good news — is frequently heard as being abandoned. Saying why takes one sentence
and is routinely omitted.

And the context: observation frequency is set by staffing at least as much as by clinical need. An
institution that answers a missed deterioration by increasing the required frequency without
changing the staffing has made its records worse and its care no better.

## What Nurse Joy is listening for

The sampling argument, with an example of each relation between event duration and interval. Why a
normal set of observations is a statement about an instant. The three things continuous monitoring
buys and the four it costs. Why alarm fatigue is a design property rather than an attitude. The
afferent and efferent limbs, and the evidence about which fails. Why a continuous record nobody
reads is worse than none. What an individualised monitoring plan contains and who authorises it
locally. Why enhanced human observation is a different intervention and not a higher setting. And
the local answers: where the plan is written, who sets alarm limits, what happens when an
escalation is not answered, and what the legal framework is for observation imposed for someone's
own safety.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-nursing.md`](../../../for-agents/SOURCES-nursing.md). Specific to
this answer:

* The reader's **national guidance on recognising and responding to acute deterioration**, where
  the individualised monitoring plan requirement and the escalation structure live.
* The reader's institutional policy on physiological monitoring and alarm management, including
  default limits, who may change them, and the route when an alarm is not answered.
* The reader's national patient safety body's alerts on clinical alarms and alarm fatigue.
* The published literature on afferent and efferent limb failure in rapid-response systems, and
  the trials of continuous ward monitoring, whose results are mixed.
* The reader's institutional policy on enhanced, constant or one-to-one observation.
* The reader's own legal framework on capacity, consent and deprivation of liberty, and the local
  safeguarding route. This is law and differs profoundly between countries.
* A current textbook of clinical measurement, for the sampling and artefact arguments.

The Pokémon material is from the **pret/pokeemerald** decompilation of Pokémon Emerald:
`GetScaledHPFraction`, `GetHPBarLevel`, `CalcNewBarValue` and `UpdateStatusIconInHealthbox` in
`src/battle_interface.c`; `HandleLowHpMusicChange`, `HandleBattleLowHpMusicChange` and
`BattleStopLowHpSound` in `src/battle_gfx_sfx_util.c`; `TurnBasedEffects` and its case list in
`src/battle_util.c`; and the `BattleStopLowHpSound` call sites in `src/battle_main.c`. The
nine-sinks-in-five-stores count against the one-field status icon is m102's, checked against the
same two files.

## Scope and safety

This explains what intermittent and continuous observation each measure, and where the chain they
sit in actually fails, through a game's monitoring code, at the level of someone already training
in or qualified for clinical practice. It is not a monitoring policy, not an escalation protocol
and not guidance on enhanced observation. It states no observation interval, no alarm limit and no
monitoring threshold, because all of those are set by the reader's national guidance and local
policy, which are the authority. It is explicitly **not** a basis for any decision about
observation imposed for a person's own safety: that involves capacity, consent and restriction of
liberty and belongs to the reader's own legal framework and safeguarding route. Nothing here has
had clinical review, and nothing here is for use in an emergency or for a decision about any
person's care. If someone is unwell right now, the local emergency number is the correct response.

## Where this stands, October 2026

The mechanical material is fixed; the sampling argument is mathematics and does not date either.
The afferent-and-efferent-limb framing has been stable for two decades and the finding that the
back half is the usual failure point has been reproduced many times. What is genuinely unsettled
is whether continuous monitoring of general ward patients improves outcomes: wearable and
contactless continuous monitoring has moved quickly, the trial evidence is mixed, and the
plausible mechanism for the mixed result is the one this answer gives. Expect that literature to
look different in a few years, and expect alarm management to continue moving toward fewer,
better-targeted alarms. Everything procedural — intervals, default limits, who authorises what,
and the whole framework around observation for a person's own safety — is local and legal and
moves independently. The reader's national deterioration guidance, institutional policy and legal
framework are the authority throughout.
