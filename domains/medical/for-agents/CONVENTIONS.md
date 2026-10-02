# Analogy conventions — the medical domain's shared vocabulary

`BRIEF.md` step 5 sends you here. This file exists because of a defect report: for the first
forty-five questions it did not exist, and two writers found that out by looking for it. What
follows is extracted from the answers that *do* exist, not invented — every row names the pair
that established it, so you can go and read how it was used before you reuse it.

**The rule this file serves.** A specialty with one vocabulary is worth more than a specialty with
fifty metaphors. Reuse a mapping that fits even when you can think of a cleverer one, and when you
reuse it, say so in the text — *"this is the Super Fang problem from m006, applied to thyroid
replacement"* — so a reader moving between answers recognises the furniture. A new device is
justified when no established one carries the mechanism, not when an established one would merely
be less fun.

**The rule it does not serve.** Do not reuse a mapping that is only nearly right. A forced reuse is
worse than a new device, because it teaches the reader a false equivalence and the reader has no way
to know. If you break with a convention here, say so in your hand-back and say why.

---

## Part I — The house vocabulary, used across every specialty

These eleven are the load-bearing ones. If you are reaching for a device and one of these fits,
use it.

| Device | What it maps to | Established in | The exact mechanic, so you get it right |
| --- | --- | --- | --- |
| **The HP bar** | A single summary number read in place of the state it summarises | m001 nursing | 48 pixels wide in the third generation, and it never renders empty while any HP remains. The rounding is the point: the bar cannot show you the difference between 1 HP and 2 |
| **Super Fang** | A proportional effect, where the proportion and the absolute are different quantities | m006 pharmacology | Always removes half of *current* HP, so it never kills. Half of Blissey's bar and half of Shedinja's are the same fraction and nothing like the same number |
| **Shedinja** | The case where the usual reasoning collapses because a parameter is 1 | m001, m006, m028, m029 | Exactly 1 maximum HP and Wonder Guard. Every percentage-of-max-HP effect rounds to 1 against it. The most reused single species in the domain |
| **Leftovers** | A small continuous intervention that is invisible per-turn and decisive over time | m002, m005, m022, m026 | Restores maxHP/16 at end of turn. Same denominator as Sandstorm damage, which is why the pair cancel |
| **Type effectiveness as a zero** | An intervention that is not weak against this target but has no mechanism against it at all | m007 pharmacology, m031 emergency | Ground into Flygon is ×0, not ×0.5. No stacking, no repetition, no dose gets you past a zero. Use this and **not** "it is less effective" |
| **An Ability versus a move** | A standing property of the organism against a discrete act done to it | m009 pharmacology | An Ability stops when the holder leaves the field. Weather set by Drizzle persists after Kyogre is gone — that asymmetry is the whole device |
| **Priority before Speed** | A sort that happens in brackets, where no amount of improvement in the lower key crosses a bracket | m031, m032, m033 emergency | Priority is read first, always. Agility, Choice Scarf, paralysis, Trick Room — none of them move a move between brackets. This is the ABC/primary-survey mapping and it is settled; do not re-derive it |
| **Four move slots and one held item** | A fixed budget, where the marginal addition displaces rather than adds | m014 general practice, m038 nursing | Four moves, one item, and the games never ask whether the item is still needed. Polypharmacy and deprescribing both live here |
| **Poisoned versus Badly Poisoned under one PSN icon** | Two different trajectories with one identical readout, where on day one the dangerous one looks milder | m024 endocrinology, m054 dermatology | Poison is a flat maxHP/8. Toxic is maxHP/16 × an incrementing counter capped at 15. On turn one the Badly Poisoned Pokémon is taking **half** as much. Both set `STATUS1_PSN_ANY` and both draw the same graphic |
| **Seen versus Own in the Pokédex** | Documented-as-encountered against documented-as-confirmed | m037 nursing | Two separate flag arrays. The Pokédex is honest about which one it holds; clinical records frequently are not. The sepsis-suspicion mapping |
| **Stealth Rock / Spikes** | A hazard that belongs to the environment rather than to the patient, set by someone who has left | m036 nursing, m024 endocrinology, m051 dermatology | Spikes layer up to three times — **a third-generation change, not second**. Stealth Rock damage is type-based. Rapid Spin and Defog clear them, and the layering/clearing asymmetry is the infection-control device |

## Part II — Established per-specialty mappings

Reuse within your own specialty first. Reading the two pairs `BRIEF.md` step 4 asks for will show
you how these sound in place.

### Nursing — m001–m005, m036–m040

| Medical concept | Device | Pair |
| --- | --- | --- |
| Observations as a set, not a single number | The summary screen against the HP bar; Slaking's Truant as a property the bar cannot show | m001 |
| Handover, and the record that arrives without its history | A traded Pokémon: full record, no history with *you*, and the obedience rules that follow | m002 |
| An intervention that does exactly one thing | Antidote cures poison and nothing else. Full Heal and Full Restore as the wider-spectrum comparators | m003 |
| Something that extends a state rather than causing it | Damp Rock: eight turns instead of five. It makes no rain | m004 |
| Cumulative small effects, and why you read the total | Summing Leftovers ticks against reading the number | m005 |
| Infection prevention as a systems problem | Spikes are on the ground, not the Pokémon, and whoever laid them has gone. Rapid Spin as the removal, costed | m036 |
| Suspicion versus confirmation under time pressure | Seen against Own; Zoroark as the entry that is wrong in the way that matters | m037 |
| Indwelling devices, with duration as the dominant term | One held item, forever, and nothing ever asks if it is still needed. Knock Off and Trick as removal and exchange | m038 |
| Nutrition and swallowing | **Stockpile / Swallow / Spit Up**: Swallow fails outright with nothing stockpiled. Heal Block as the route being unavailable | m039 |
| Multifactorial risk, and iatrogenic harm from prevention | Speed as one number with at least seven multipliers; Bind/Clamp/Fire Spin/Whirlpool as restraint that itself injures | m040 |

### Pharmacology — m006–m010

| Medical concept | Device | Pair |
| --- | --- | --- |
| Half-life against absolute concentration | Super Fang's half, across Blissey and Shedinja | m006 |
| No mechanism versus insufficient dose | Earthquake into Flygon is zero | m007 |
| Therapeutic index | Take Down pays 4:1 recoil, Double-Edge 3:1 — and the printed ratio is not the margin | m008 |
| Pharmacodynamics outliving pharmacokinetics | Drizzle keeps raining after Kyogre has gone | m009 |
| Predictable adverse effect against idiosyncratic one | Hyper Beam always recharges; Rough Skin only ever happens to someone else | m010 |
| Therapeutic drug monitoring | The Blissey/Shedinja bar as volume of distribution; the five conditions under which a concentration is worth measuring at all | m041 |
| Renal and hepatic impairment | **Light Screen as first-pass extraction**, with three exact bypasses: a critical hit (the screen applies only when the crit multiplier is 1), a physical move (Reflect covers that route), and Brick Break | m042 |
| Adherence and regimen design | Snorlax learning Rest and Snore at the same level | m043 |
| Formulation and route | **Accuracy = bioavailability**, with power × accuracy as the delivered dose; **Lock-On / Mind Reader = the intravenous route**, where F = 1 is a property of the route and not an improvement to the move; the partial-trapping family as modified release; Future Sight as delayed release, because damage is computed at the moment of use | m044 |
| Antimicrobial stewardship | **Sketch as horizontal gene transfer, Egg Moves as vertical**; `gFrontierBannedSpecies` plus the duplicate checks as a formulary written into the cartridge; Rapid Spin clearing exactly one thing per use, in a fixed order, as the review point | m045 |

### General practice — m011–m015

| Medical concept | Device | Pair |
| --- | --- | --- |
| Pre-test probability | The same rustle on a different floor. Mt. Moon's encounter table against the route's | m011 |
| Prevalence and the limits of a sample | You do not clear Mt. Moon of Clefairy by meeting ten Zubat | m012 |
| Screening against case-finding | Sweeping the grass on purpose is a different act from meeting something in it | m013 |
| Polypharmacy | Four slots, one item, and the fourth addition is the one that loses | m014 |
| Continuity, and shared care | A Pokémon someone else raised does not obey, and that is in the code — badge-gated, by level | m015 |
| Chronic disease review | **Generation I Stat Experience** as a cached record: five hidden counters nobody displays, refreshed by exactly four events, and because Medium Fast is *n*³ the interval between refreshes lengthens exactly as the hidden burden grows | m046 |
| Multimorbidity and guidelines | Stealth Rock as a product of two documented terms, where Skarmory, Scizor and Snorlax all land on maxHP/8 by different routes — a composed answer that looks ordinary is not evidence that anything is ordinary. **Utility Umbrella** as protecting one condition from the other condition's treatment | m047 |
| The consultation, and premature closure | `SweetScentWildEncounter` passes **flags = 0** where an ordinary step passes `WILD_CHECK_REPEL \| WILD_CHECK_KEEN_EYE`: the open question bypasses every filter you had running. Premature closure is the Choice lock, `gCurrentMove = *choicedMove` | m048 |
| Antibiotics under uncertainty | The Safari Zone as a shared counter: 30 balls against 58.8 expected encounters, where no individual throw can be named as the wasteful one | m049 |
| Health inequality as mechanism | `ApplyBadgeStatBoosts`: ×1.125 is **relative**, so it widens the absolute gap while improving both; it is awarded for having already won; and it returns immediately in a link battle, so the advantage is invisible in the only format where like is compared with like. The four badges that boost are the even bits — exactly the four that m015's obedience check does *not* use | m050 |

### Dermatology — m016–m020, m051–m055

| Medical concept | Device | Pair |
| --- | --- | --- |
| Morphology that varies between individuals with the same diagnosis | Spinda's per-individual spots, derived from its personality value | m016 |
| Distribution as diagnostic information | Vivillon's wing pattern as a map of where it came from | m017 |
| Appearance separable from pathology | Search the Pokédex for a red Gyarados and it returns nothing: colour is not a field you can query | m018 |
| Potency classification, and why a figure without its system is unusable | The Potion ladder; Milcery's evolution on a duration nobody writes down | m019 |
| A property no amount of looking at the surface reveals | Nature as a word for something invisible on the sprite | m020 |
| The barrier, and emollient quantity as the intervention | **Substitute** costs maxHP/4 and *fails if current HP is at or below that quarter* — a barrier built from the substance it protects. **Haze** clears every stat stage and restores not one point of substituteHP | m051 |
| Systemic disease presenting on the skin | Kyogre's Drizzle as one upstream setter with six verified downstream readouts; Air Lock / Cloud Nine as the biologic, because the weather macro is written as the *absence* of those abilities | m052 |
| Mechanism dictating treatment order | Kanto's badge-gated field moves as a dependency graph, not a difficulty curve: the boulder needs Strength, not Hyper Beam's 150 base power | m053 |
| Pattern recognition, and the few emergencies | Poisoned against Badly Poisoned under one PSN graphic | m054 |
| Assessment before intervention | Surf doubled on Charizard and healing Lapras a quarter: one act, two signs, invisible on the sprite. The game records an opponent's Ability only when it fires | m055 |

### Endocrinology — m021–m025

| Medical concept | Device | Pair |
| --- | --- | --- |
| The same lab value from two different causes | The field says RAIN; in one battle there is no Kyogre, in the other a Golduck | m021 |
| Basal and bolus | Leftovers every turn against a Sitrus Berry at the threshold — the real thing is both, and neither is a move | m022 |
| A cumulative marker against a point measurement | Return's base power is the whole history; the HP bar is now | m023 |
| Complications that accrue against those that wait | Badly Poisoned counting turns; Stealth Rock waiting at the door | m024 |
| Negative feedback and suppression | Solar Power fires only in harsh sunlight, and one turn of rain switches it off completely | m025 |
| The axis hormones, as a layer distinct from the metabolic ones | **The terrain layer**, deliberately kept separate from weather (which stays the glucose-control hormones): Grassy for thyroid hormone, Psychic for cortisol, Misty for calcium, Electric's five-turn timer for the reproductive cycle. The payoff is that terrain affects **grounded battlers only**, so Levitate / Flying / Air Balloon is a tissue without the receptor and Gravity / Iron Ball / Ingrain is what forces it to respond | m056–m060 |
| An amplified reporter that reads inversely | **`Flail`'s six-band power table** — 48ths with cut-offs at 1/4/9/16/32 giving 200/150/100/80/40/20. The *flat top third* is what makes "a suppressed reporter cannot grade severity" work | m056 |
| Exogenous replacement suppressing the axis | **`TryChangeBattleTerrain` returns false when its own terrain is already up and does not refresh the timer** — including the lapse on the original clock when the outside supply stops. One mechanic, three answers | m057–m059 |
| A suppression test | `Intimidate` against `Clear Body`; `Hyper Cutter` as the stat-specific block | m058 |
| Pulsatility | The `Protect` consecutive-use counter: 1, 1/2, 1/4, 1/8 in Gen III, and **it resets to zero whenever the last resulting move was not one of the family** | m060 |

### Oncology — m026–m030

| Medical concept | Device | Pair |
| --- | --- | --- |
| Classification that changed, and what the old one conflated | For three generations the damage category was computed from the type | m026 |
| Treatment toxicity written into the treatment | Read the move's own data and the cost is already in it | m027 |
| Exemptions that go by category rather than by name | The exemption list is types, not names — and the counter says when | m028 |
| What a response measurement cannot show | The bar is 48 pixels and never renders empty while anything is left | m029 |
| Sampling, and the thing the sample did not change | Three rods, one pond, and the pond never changed | m030 |
| Spread, and organotropism | The `MIMIC_FORBIDDEN_END` sentinel sitting mid-list in `sMovesForbiddenToCopy`, so Mimic and Metronome read different prefixes of one exclusion list | m061 |
| Fractionation | The multi-hit class — `Random() & 3` redrawn, giving 2 and 3 at three-eighths each and 4 and 5 at one-eighth — with Rock Blast, Bullet Seed, Fury Swipes and Icicle Spear | m062 |
| A surgical margin | `GetScaledHPFraction(hp, maxHP, 48)` — the Flail table uses literally the same 48 as the health bar | m063 |
| Tumour markers, and a lower limit of detection | **Three separate routines in one game refusing to report zero**: the bar's forced 1, Super Fang's floor, and `Cmd_scaledamagebyhealthratio`'s. Flail and Water Spout as opposite functions of one quantity | m064 |
| Randomisation against registries | The allocated object is a **move**, the confounder is the player's choice of when to use it, and the registry is the battle log — so nothing stands in for a person | m065 |

### Emergency — m031–m035

| Medical concept | Device | Pair |
| --- | --- | --- |
| The primary survey's ordering | Priority is read before Speed, and nothing done to Speed ever changes that | m031 |
| Why protocols exist | Red and Blue decided turn order with two if-statements; Emerald wrote it in a table | m032 |
| What triage optimises | Trick Room inverts the sort key and leaves the brackets alone | m033 |
| Compensation, and the reserve the monitor is not showing | PP is the budget, the bar is not showing it, and the bar is all the game shows | m034 |
| First aid for the untrained | Focus Energy *said* it raised the critical-hit rate; in Red and Blue it quartered it | m035 |
| Shock categories by mechanism | The seven-factor Speed pipeline in `GetWhoStrikesFirst`, where the only observable is who acts first and each broken factor has a non-interchangeable counter. Ninjask at 160 quartered still beats Shuckle at 5; Jolteon at 130 with two drops loses to it | m066 |
| What speech proves about the airway | `attackcanceler` and the fourteen-case `AtkCanceler_UnableToUseMove` chain, with the `effect == 0` short-circuit as the source of the asymmetry and per-turn re-rolls as the reason a pass cannot be extrapolated | m067 |
| Mechanism of injury as a prior | `Cmd_trysetfutureattack` storing the whole consequence at the moment of use; the four semi-invulnerable `sDMG_MULTIPLIER` doublings as state at the instant of transfer; and the explicit `setbyte sDMG_MULTIPLIER, 1` on the no-bonus branch as anchoring implemented in code | m068 |
| Supportive care, and the antidote exception | Forty-one effect scripts reaching one shared pipeline through forty-five jumps, with five labelled entry points, against single-purpose items that are six bytes with one bit | m069 |
| Handover, and what crosses the boundary | `SwitchInClearSetData`: what is deleted against what survives (`status1`, HP, PP); Baton Pass's hand-written whitelist, which does **not** include the history; `DEFAULT_STAT_STAGE` as both the never-set and the cleared value — the pertinent-negative problem; and `truantSwitchInHack` as what a field list looks like after someone discovers a loss | m070 |

## Part III — Devices that are not available, and why

Not a style preference. These come out of `../SAFETY.md`, which you have read twice.

- **A Pokémon standing in for a confused, frightened, dying or hurting person.** Forbidden outright.
  Two wave-two topics — delirium/dementia/depression, and pain in someone who cannot self-report —
  were declined in full for this reason rather than written around, and declining was the right call.
  If the only mapping you can find requires it, decline the topic and say so.
- **Fainting, KO, or Revive as death, resuscitation or bereavement.** The game's fainting is
  reversible by design and the mapping is obscene. Prognosis, dying, bereavement, mental-health
  crisis, self-harm, safeguarding, capacity, consent and coercion are all set-aside; handle them in
  the plain-prose section or not at all.
- **A Trainer standing in for a clinician making a decision about a person.** Trainer-as-prescriber
  works for a decision about a *drug* or a *protocol*; it stops working the moment the Pokémon is
  the patient.
- **Catching as diagnosis or admission.** Specifically avoided: catching is acquisitive and
  non-consensual, and the mapping reads badly however carefully it is framed. Poké Ball mechanics
  are used in m011–m013 for *probability* only, never for the act.
- **Frailty via Shedinja, and the shape it shares with others.** Shedinja — 1 HP, Wonder Guard,
  ended by one point of anything — is the obvious mapping for frailty and it requires a creature to
  be the patient whose resilience is the subject. A writer reached for it, saw the problem, and wrote
  health inequality instead, noting that *"the next writer will reach for Shedinja too"*. They were
  right. Shedinja is available for a **type-override** point with no person attached (m047 uses it
  that way); it is not available as a frail patient. The same shape blocked paediatric differences (a
  low-level Pokémon as the patient), analgesia, and crowding and flow (boxed Pokémon as queued
  patients). All four remain unwritten and should be commissioned with an explicit instruction about
  what may stand in for the patient, or not at all.
- **A Pokémon half with no Pokémon in it.** Raised by a writer declining supportive and palliative
  care, and the argument is worth keeping: that territory is almost entirely what `SAFETY.md` fences
  off, so there is no mechanism left to carry an analogy, and the result would not be a low-scoring
  pair but a *degenerate record* for a dataset whose premise is two registers of the same content.
  The corpus floor for taste-constrained answers is around 45, not zero. If an answer would land near
  zero because the whole subject is set aside, the subject is set aside — do not write it and do not
  soften the taste rule to make it scoreable.
- **Revive and Max Revive, for anything.** They sit in the same `item_effects.h` table as everything
  else, and nothing in Pokémon may stand in for resuscitating a person. m069 says so in its own text.
- **Breeding mechanics for the reproductive axis.** Day Care, egg groups and Destiny Knot are the
  obvious mapping and would have scored well. m060 keeps the analogy entirely on the *controller* —
  rhythms, thresholds, sign reversals — and says so out loud, which makes the omission legible.
- **Any mechanic whose humour depends on the condition.** The Pokémon half is a teaching register,
  not a comic one. Check your jokes against the question "would I say this in front of someone who
  has it".

## Part IV — Mechanical facts that have been got wrong, so check before reusing

Every one of these was written from memory by a competent writer and caught against
`pret/pokered`, `pret/pokeemerald` or `rh-hideout/pokeemerald-expansion`. Verify in the
disassembly; do not trust this list either.

| Claim | The correction |
| --- | --- |
| Spikes layering is a second-generation feature | **Third generation.** Gen II has one layer |
| Held items begin in the first generation | **Second.** Gen I has no held items |
| Politoed has Drizzle in Gen III | **Kyogre alone.** Politoed gained it in Gen V |
| Quagsire has Cloud Nine | **Psyduck and Golduck only.** Quagsire has Damp and Water Absorb |
| Parasect has Dry Skin in Gen III | **Effect Spore only.** Dry Skin is its second ability from Gen IV |
| Sandstorm boosts Rock-types' Special Defence | **Not in Gen III.** A fourth-generation change; `Cmd_weatherdamage` has no such boost |
| Sticky Barb damages any holder | **Magic Guard is exempt** |
| Struggle's recoil is a fixed fraction | Differs by generation: fraction of damage dealt in Gen II–III, fraction of max HP from Gen IV. Quote no fraction |
| The OHKO clause is in the game | **A Smogon community ruleset**, not game code. If your argument depends on it, say in the body that it is a written community rule |

And the general rule behind the table: **state the generation, or do not state the number.** An
unqualified mechanical figure is the single most common defect in drafts, and the one a reader is
least able to catch.
