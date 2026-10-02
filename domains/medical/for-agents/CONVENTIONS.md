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

**The rule it does not serve.** Do not reuse a mapping that is only nearly right. A forced reuse
is worse than a new device, because it teaches the reader a false equivalence and the reader has
no way to know. If you break with a convention here, say so in your hand-back and say why.

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

**The first column is the question, copied from `questions.tsv`, and it is generated rather than
written.** It used to be a label I wrote from the device, and that caused a real failure: a wave
brief offered a nursing writer eight topics of which three were already written, because whoever
assembled it read this table as a topic index. It was not one. m004 is *"What is a dressing
actually doing, and why is pressure damage a time-and-pressure problem rather than a cleanliness
problem?"* and this table used to render it as "Something that extends a state rather than causing
it — Damp Rock", which is true of the device and says nothing about the topic. Fourteen rows were
wrong the same way.

So: **this table is indexed by device, for reuse. It is not a coverage index.** To find out what a
specialty covers, run `python3 scripts/medical/coverage.py <specialty>` and read the questions.

### Nursing — m001–m005, m036–m040, m071–m075

| The question, from `questions.tsv` | Device | Pair |
| --- | --- | --- |
| Why does a composite score built from simple bedside observations detect deterioration earlier than any single observation? | The summary screen against the HP bar; Slaking's Truant as a property the bar cannot show | m001 |
| Why is clinical handover given in a structured format, and why are escalation criteria written as thresholds rather than left to judgement? | A traded Pokémon: full record, no history with *you*, and the obedience rules that follow | m002 |
| Why is safe medicines administration described as a system rather than a matter of individual carefulness, and where is that system weakest? | Antidote cures poison and nothing else. Full Heal and Full Restore as the wider-spectrum comparators | m003 |
| What is a dressing actually doing, and why is pressure damage a time-and-pressure problem rather than a cleanliness problem? | Damp Rock: eight turns instead of five. It makes no rain | m004 |
| What does a fluid balance chart actually measure, what does it miss, and how does it connect to the circulation? | Summing Leftovers ticks against reading the number | m005 |
| Why is hand hygiene a systems problem rather than a knowledge problem, and what has to be true around it for it to work? | Spikes are on the ground, not the Pokémon, and whoever laid them has gone. Rapid Spin as the removal, costed | m036 |
| Why is the response to suspected sepsis organised as a time-critical bundle, and what does that design trade away? | Seen against Own; Zoroark as the entry that is wrong in the way that matters | m037 |
| Why is every indwelling device a standing trade against infection risk, and why is duration the dominant term? | One held item, forever, and nothing ever asks if it is still needed. Knock Off and Trick as removal and exchange | m038 |
| What does a nutrition and swallowing assessment actually protect against, and what goes wrong when it is skipped? | **Stockpile / Swallow / Spit Up**: Swallow fails outright with nothing stockpiled. Heal Block as the route being unavailable | m039 |
| Why do multifactorial falls risks resist single-intervention fixes, and why can preventing falls cause harm? | Speed as one number with at least seven multipliers; Bind/Clamp/Fire Spin/Whirlpool as restraint that itself injures | m040 |
| Why is wound healing described as a sequence of overlapping phases, and what does it mean to say that a wound is stuck? | **Rollout**: base 30, timer 5, doubling per elapsed turn to 480 and again on the `STATUS2_DEFENSE_CURL` bit — and **no doubling on the first hit** — with `CancelMultiTurnMoves` returning the timer to **0** on a 10 per cent miss. **Encore** (3–6 turns, not 2–6) implemented as *every other move is unusable* inside `CheckMoveLimitations`, beside Disable, Taunt, Imprison and the Choice lock: five causes, one greyed-out readout | m071 |
| Why is bed rest an intervention with its own harms, and why is deconditioning quicker to produce than to reverse? | **`Ingrain` against `Aqua Ring`**: `HandleEndTurnIngrain` and `HandleEndTurnAquaRing` are the same function twice — same maxHP/16, same Heal Block guard, same `GetDrainedBigRootHp` — differing only in which volatile they read. And `Cmd_jumpifcantswitch` tests `STATUS3_ROOTED` in **one conditional** with the trapping states, where rooted is the only one with **no timer at all** | m072 |
| Why is the clinical record treated as an instrument other people act on, and what makes a pertinent negative worth writing down? | **`FlagGet` returns FALSE both for a failed lookup and for a genuine clear bit**, against `VarGet` returning the id — one storage class fails quietly into "no", which is why a blank cannot hold a pertinent negative. The **Move Deleter** (free, irreversible) against the **Move Reminder**, whose list is `gLevelUpLearnsets[species]`, so a TM or Egg Move once deleted is unrecoverable | m073 |
| Why is fatigue treated as a safety factor rather than a personal failing, and what makes the handover at the end of a night shift the most dangerous one? | **`STATUS1_ANY` names exactly six conditions and tiredness is not one.** **`Rest`** is a single assignment of a three-turn counter that clears four other statuses, and it fails under **Insomnia**, **Vital Spirit**, any **Uproar**, or full HP — the restorative blocked by the thing keeping you awake. **Early Bird** subtracts 2, which is a faster clock and not a smaller need. **`Helping Hand`**'s first condition is `BATTLE_TYPE_DOUBLE`: cover that fails on the format, not on the need | m074 |
| Why are isolation precautions keyed to the route of transmission rather than to the organism, and what follows from that? | **`FLAG_MAKES_CONTACT`** on 111 of 355 move entries, read by six abilities that ask nothing about the attacker, against **`sSoundMovesTable`** — ten moves and a sentinel, hand-maintained, failing silently for the eleventh audible move. A route encoded on the act against a route encoded as a list. **Reflect and Light Screen sit inside the two branches of `CalculateBaseDamage`**, split on `IS_TYPE_PHYSICAL`, so the wrong barrier is unreachable code and not weaker protection | m075 |

### Pharmacology — m006–m010

| The question, from `questions.tsv` | Device | Pair |
| --- | --- | --- |
| What do absorption, distribution, metabolism and excretion each contribute, and why are clearance, volume of distribution and half-life the three numbers that actually predict a drug's behaviour? | Super Fang's half, across Blissey and Shedinja | m006 |
| Distinguish agonist, partial agonist, antagonist and inverse agonist, and explain why a competitive antagonist shifts a dose-response curve while a non-competitive one flattens it. | Earthquake into Flygon is zero | m007 |
| What is the therapeutic index, and what does a narrow one change about how a drug is monitored, substituted and assessed for interactions? | Take Down pays 4:1 recoil, Double-Edge 3:1 — and the printed ratio is not the margin | m008 |
| Compare enzyme induction and enzyme inhibition mechanistically, and explain why protein-binding displacement usually matters less than it sounds. | Drizzle keeps raining after Kyogre has gone | m009 |
| How are adverse drug reactions classified, why do dose-dependent and idiosyncratic reactions need different responses, and why do spontaneous reporting schemes exist despite their known biases? | Hyper Beam always recharges; Rough Skin only ever happens to someone else | m010 |
| Which drugs are monitored by plasma concentration rather than by effect, what has to be true before a concentration can be interpreted, and what does a trough actually tell you? | The Blissey/Shedinja bar as volume of distribution; the five conditions under which a concentration is worth measuring at all | m041 |
| Why do renal and hepatic impairment change prescribing in different ways, and why is there a usable number for one of them and not for the other? | **Light Screen as first-pass extraction**, with three exact bypasses: a critical hit (the screen applies only when the crit multiplier is 1), a physical move (Reflect covers that route), and Brick Break | m042 |
| What makes a regimen hard to take, why does the timing of a side effect matter more than its severity, and why is calling someone non-compliant a statement about the prescription? | Snorlax learning Rest and Snore at the same level | m043 |
| Why does the same drug behave differently by route, and what does a modified-release preparation actually modify? | **Accuracy = bioavailability**, with power × accuracy as the delivered dose; **Lock-On / Mind Reader = the intravenous route**, where F = 1 is a property of the route and not an improvement to the move; the partial-trapping family as modified release; Future Sight as delayed release, because damage is computed at the moment of use | m044 |
| What is antimicrobial stewardship optimising, and why does the way resistance spreads make it a collective-action problem rather than an individual prescribing decision? | **Sketch as horizontal gene transfer, Egg Moves as vertical**; `gFrontierBannedSpecies` plus the duplicate checks as a formulary written into the cartridge; Rapid Spin clearing exactly one thing per use, in a fixed order, as the review point | m045 |

### General practice — m011–m015, m046–m050, m081–m085

| The question, from `questions.tsv` | Device | Pair |
| --- | --- | --- |
| Why does an identical finding mean something different in general practice than in a hospital clinic, and how does prevalence change what it is worth? | The same rustle on a different floor. Mt. Moon's encounter table against the route's | m011 |
| What is safety-netting actually for, and what separates a safety-net that works from reassurance that only sounds like one? | You do not clear Mt. Moon of Clefairy by meeting ten Zubat | m012 |
| Why is a screening programme not simply more testing, and what do lead-time bias, length bias and overdiagnosis each do to its apparent benefit? | Sweeping the grass on purpose is a different act from meeting something in it | m013 |
| Why is the number of medicines a risk factor in its own right, and what makes a decision to stop different in kind from a decision to start? | Four slots, one item, and the fourth addition is the one that loses | m014 |
| What does continuity of care actually buy, and why is it a clinical intervention rather than a courtesy? | A Pokémon someone else raised does not obey, and that is in the code — badge-gated, by level | m015 |
| Why does a structured review at a fixed interval outperform reactive consulting for a condition that produces no symptoms, and what makes a review a clinical act rather than an administrative one? | **Generation I Stat Experience** as a cached record: five hidden counters nobody displays, refreshed by exactly four events, and because Medium Fast is *n*³ the interval between refreshes lengthens exactly as the hidden burden grows | m046 |
| Why do single-disease guidelines stop composing once a person has four conditions, and what has to replace them? | Stealth Rock as a product of two documented terms, where Skarmory, Scizor and Snorlax all land on maxHP/8 by different routes — a composed answer that looks ordinary is not evidence that anything is ordinary. **Utility Umbrella** as protecting one condition from the other condition's treatment | m047 |
| Why does the opening question shape the diagnosis, and what does a hypothesis formed in the first minute actually cost? | `SweetScentWildEncounter` passes **flags = 0** where an ordinary step passes `WILD_CHECK_REPEL \| WILD_CHECK_KEEN_EYE`: the open question bypasses every filter you had running. Premature closure is the Choice lock, `gCurrentMove = *choicedMove` | m048 |
| Why do the individual and the population optimum genuinely differ when an antibiotic is considered under diagnostic uncertainty? | The Safari Zone as a shared counter: 30 balls against 58.8 expected encounters, where no individual throw can be named as the wasteful one | m049 |
| Why is the inverse care law a mechanism rather than a complaint, and what does treating it as a mechanism change? | `ApplyBadgeStatBoosts`: ×1.125 is **relative**, so it widens the absolute gap while improving both; it is awarded for having already won; and it returns immediately in a link battle, so the advantage is invisible in the only format where like is compared with like. The four badges that boost are the even bits — exactly the four that m015's obedience check does *not* use | m050 |
| Why is a referral decision a threshold rather than a judgement, and what is a gatekeeper actually optimising? | The **Repel number**: `IsWildLevelAllowedByRepel` walks the party and stops at the first member with HP that is not an egg — **not the lead** — and falls through to FALSE with a wiped party, so the item cancels everything. Route 116's three thresholds, where 6→7 is free, 7→8 costs the same slot every time, and 8→9 makes the route read empty. The **mass outbreak**'s two-day counter as urgency distinct from probability, still subject to both filter flags | m081 |
| Why does a system that is easy to enter behave differently from one that is hard to enter, and who does each one filter out? | The encounter-**rate** pipeline — ×16, bike ×80/100, White and Black Flute, Cleanse Tag ×2/3, lead ability ×2 or ÷2, cap 2880, the 40 per cent new-metatile skip — as access, against the **table** as need: nine levers, not one of which touches a slot. The three rods as the route in restricting what is reachable rather than how often | m082 |
| Why does a preference-sensitive decision have no single right answer, and what does that demand of the consultation? | **`Thunder` in rain skips the accuracy check entirely** while sun overwrites `moveAcc` to 50 — so the same pair is a preference-sensitive trade in clear weather and effectiveness-sensitive in rain, and the *class* of the decision changes with the field. The chart is in the cartridge and nothing in the battle menu shows it: a decision aid is information moved forward, not new information | m083 |
| What is overdiagnosis, why can it never be seen in an individual, and what makes primary care generate it without any screening programme? | **`GetSetPokedexFlag` has no case that clears a bit**, and its three-copy integrity wipe returns 0 — labelling that outlives what it labelled. **Pokérus**'s `if (pokerus == 0) pokerus = 0x10;` forces a permanent marker, and `MonGainEVs` doubles on `CheckPartyHasHadPokerus`, the *ever-had* query. The Gen VI Fairy retyping as a definitional change with five instant downstream consequences | m084 |
| Why can an intervention prevent many cases across a population while offering almost no individual in it a benefit they could notice? | The bike's 80/100 as the population measure against abolishing the two rarest slots: ten-fold for nothing nameable, against 1.11 points per step for everyone. **Both 1 per cent slots are Geodude, and Geodude is not rare** — it holds 10 per cent of the table through two 4 per cent slots, so an intervention aimed at the tail removes a fifth of one species and leaves every Makuhita, Zubat and Abra untouched. Sandstorm's maxHP/16 as Leftovers with the sign reversed, set by one Sand Stream for everybody present | m085 |

### Dermatology — m016–m020, m051–m055

| The question, from `questions.tsv` | Device | Pair |
| --- | --- | --- |
| How should a skin lesion be described, and why does the primary morphology constrain the differential more than any other single step? | Spinda's per-individual spots, derived from its personality value | m016 |
| Why do the distribution of a rash and the configuration of its lesions carry as much diagnostic weight as the individual lesions? | Vivillon's wing pattern as a map of where it came from | m017 |
| Why do the standard descriptions of erythema, cyanosis and jaundice fail in darker skin, and what changes? | Search the Pokédex for a red Gyarados and it returns nothing: colour is not a field you can query | m018 |
| Why is under-application the commonest reason a topical treatment appears not to work, and what do potency, vehicle and quantity each contribute? | The Potion ladder; Milcery's evolution on a duration nobody writes down | m019 |
| What does dermoscopy add over the naked eye, and why is it pattern recognition over a structured vocabulary rather than magnification? | Nature as a word for something invisible on the sprite | m020 |
| Why is atopic eczema best understood as a barrier disease, and why is the quantity of emollient the intervention rather than an adjunct? | **Substitute** costs maxHP/4 and *fails if current HP is at or below that quarter* — a barrier built from the substance it protects. **Haze** clears every stat stage and restores not one point of substituteHP | m051 |
| Why is psoriasis described as a systemic inflammatory disease that presents on the skin, and what follows from that for assessment? | Kyogre's Drizzle as one upstream setter with six verified downstream readouts; Air Lock / Cloud Nine as the biologic, because the weather macro is written as the *absence* of those abilities | m052 |
| What are the mechanisms of acne, and why does the order in which treatments are added follow from them? | Kanto's badge-gated field moves as a dependency graph, not a difficulty curve: the boulder needs Strength, not Hyper Beam's 150 base power | m053 |
| How are drug eruptions recognised as patterns, and which few of them are emergencies? | Poisoned against Badly Poisoned under one PSN graphic | m054 |
| Why does the vascular assessment come before the dressing in a chronic leg ulcer, and what makes compression the treatment rather than the wound covering? | Surf doubled on Charizard and healing Lapras a quarter: one act, two signs, invisible on the sprite. The game records an opponent's Ability only when it fires | m055 |

### Endocrinology — m021–m025

| The question, from `questions.tsv` | Device | Pair |
| --- | --- | --- |
| Type 1 and type 2 diabetes are diagnosed by the same measurement. Why are they different diseases? | The field says RAIN; in one battle there is no Kyogre, in the other a Golduck | m021 |
| Why is replacing insulin with injections intrinsically hard, and what do basal and bolus each do? | Leftovers every turn against a Sitrus Berry at the threshold — the real thing is both, and neither is a move | m022 |
| What does glycated haemoglobin measure that a spot glucose cannot, and where does it mislead? | Return's base power is the whole history; the HP bar is now | m023 |
| Why do the microvascular and macrovascular complications of diabetes differ in mechanism and time course? | Badly Poisoned counting turns; Stealth Rock waiting at the door | m024 |
| Why do diabetic ketoacidosis and the hyperosmolar hyperglycaemic state present so differently? | Solar Power fires only in harsh sunlight, and one turn of rain switches it off completely | m025 |
| The axis hormones, as a layer distinct from the metabolic ones | **The terrain layer**, deliberately kept separate from weather (which stays the glucose-control hormones): Grassy for thyroid hormone, Psychic for cortisol, Misty for calcium, Electric's five-turn timer for the reproductive cycle. The payoff is that terrain affects **grounded battlers only**, so Levitate / Flying / Air Balloon is a tissue without the receptor and Gravity / Iron Ball / Ingrain is what forces it to respond | m056–m060 |
| Why does the three-level thyroid feedback loop make its tests counterintuitive, and what is the pituitary's output actually reporting? | **`Flail`'s six-band power table** — 48ths with cut-offs at 1/4/9/16/32 giving 200/150/100/80/40/20. The *flat top third* is what makes "a suppressed reporter cannot grade severity" work | m056 |
| Exogenous replacement suppressing the axis | **`TryChangeBattleTerrain` returns false when its own terrain is already up and does not refresh the timer** — including the lapse on the original clock when the outside supply stops. One mechanic, three answers | m057–m059 |
| Why do the tests for cortisol excess have the shape they do, and why is imaging the wrong first step? | `Intimidate` against `Clear Body`; `Hyper Cutter` as the stat-specific block | m058 |
| Every other endocrine axis holds a set point. Why is the reproductive axis a cyclical controller instead, and what does that change about reading its tests? | The `Protect` consecutive-use counter: 1, 1/2, 1/4, 1/8 in Gen III, and **it resets to zero whenever the last resulting move was not one of the family** | m060 |

### Oncology — m026–m030

| The question, from `questions.tsv` | Device | Pair |
| --- | --- | --- |
| Staging and grading are two different axes. What does each describe, why are both needed, and in what sense is a staging system a communication protocol rather than a biological description? | For three generations the damage category was computed from the type | m026 |
| Cytotoxic chemotherapy, targeted therapy, endocrine therapy and immunotherapy work by different mechanisms. What are those mechanisms, and how does each one's toxicity profile follow from it rather than being arbitrary? | Read the move's own data and the cost is already in it | m027 |
| Why do cytotoxic agents damage the particular tissues they damage, why is the timing of that damage predictable rather than surprising, and why do immunotherapy toxicities look like autoimmunity? | The exemption list is types, not names — and the counter says when | m028 |
| Why is deciding whether a cancer treatment is working harder than it sounds, what does a structured response criterion actually buy, and why is a better scan not the same thing as a longer life? | The bar is 48 pixels and never renders empty while anything is left | m029 |
| Why is finding more cancer not automatically better? Explain lead-time bias, length bias and overdiagnosis, and why overdiagnosis is a real harm rather than a technicality. | Three rods, one pond, and the pond never changed | m030 |
| How does a cancer spread, and why is the pattern of spread organ-specific rather than random? | The `MIMIC_FORBIDDEN_END` sentinel sitting mid-list in `sMovesForbiddenToCopy`, so Mimic and Metronome read different prefixes of one exclusion list | m061 |
| What does ionising radiation actually do to a cell, and why is a course of radiotherapy divided into many small fractions instead of being given all at once? | The multi-hit class — `Random() & 3` redrawn, giving 2 and 3 at three-eighths each and 4 and 5 at one-eighth — with Rock Blast, Bullet Seed, Fury Swipes and Icicle Spear | m062 |
| What does a surgical margin actually mean, and in what sense is a clear margin a probability statement rather than a guarantee? | `GetScaledHPFraction(hp, maxHP, 48)` — the Flail table uses literally the same 48 as the health bar | m063 |
| What is a tumour marker actually measuring, and why are almost none of them useful as screening tests even where they are useful for monitoring? | **Three separate routines in one game refusing to report zero**: the bar's forced 1, Super Fang's floor, and `Cmd_scaledamagebyhealthratio`'s. Flail and Water Spout as opposite functions of one quantity | m064 |
| What does randomisation buy in an oncology trial that no amount of analysis of a registry can buy, and where is a registry the better instrument? | The allocated object is a **move**, the confounder is the player's choice of when to use it, and the registry is the battle log — so nothing stands in for a person | m065 |

### Emergency — m031–m035

| The question, from `questions.tsv` | Device | Pair |
| --- | --- | --- |
| Why is the primary survey ordered airway, breathing, circulation, and what is that ordering actually sorting on? | Priority is read before Speed, and nothing done to Speed ever changes that | m031 |
| Why are time-critical decisions written down as protocols instead of left to individual clinical judgement? | Red and Blue decided turn order with two if-statements; Emerald wrote it in a table | m032 |
| What is a triage system optimising, and why is the sickest patient not first in a mass-casualty setting? | Trick Room inverts the sort key and leaves the brackets alone | m033 |
| Why is a patient holding normal observations by compensating closer to collapse than one with abnormal but stable numbers? | PP is the budget, the bar is not showing it, and the bar is all the game shows | m034 |
| Why is first-aid guidance for untrained bystanders different in kind from clinical guidance, rather than just simpler? | Focus Energy *said* it raised the critical-hit rate; in Red and Blue it quartered it | m035 |
| Why are the categories of shock defined by mechanism rather than by blood pressure, and how can the pressure be normal while perfusion is not? | The seven-factor Speed pipeline in `GetWhoStrikesFirst`, where the only observable is who acts first and each broken factor has a non-interchangeable counter. Ninjask at 160 quartered still beats Shuckle at 5; Jolteon at 130 with two drops loses to it | m066 |
| Why does whether someone can talk carry so much information about the airway, and what exactly does a normal voice rule out and fail to rule out? | `attackcanceler` and the fourteen-case `AtkCanceler_UnableToUseMove` chain, with the `effect == 0` short-circuit as the source of the asymmetry and per-turn re-rolls as the reason a pass cannot be extrapolated | m067 |
| Why does the mechanism of injury change what is looked for in trauma, when the examination itself is the same either way? | `Cmd_trysetfutureattack` storing the whole consequence at the moment of use; the four semi-invulnerable `sDMG_MULTIPLIER` doublings as state at the instant of transfer; and the explicit `setbyte sDMG_MULTIPLIER, 1` on the no-bonus branch as anchoring implemented in code | m068 |
| Why is the management of most poisonings supportive rather than antidotal, and what has to be true before a specific antidote is worth reaching for? | Forty-one effect scripts reaching one shared pipeline through forty-five jumps, with five labelled entry points, against single-purpose items that are six bytes with one bit | m069 |
| Why is the handover from pre-hospital to hospital the point at which information loss costs most, and what is it that actually gets lost? | `SwitchInClearSetData`: what is deleted against what survives (`status1`, HP, PP); Baton Pass's hand-written whitelist, which does **not** include the history; `DEFAULT_STAT_STAGE` as both the never-set and the cleared value — the pertinent-negative problem; and `truantSwitchInHack` as what a field list looks like after someone discovers a loss | m070 |

## Part III — Devices that are not available, and why

Not a style preference. These come out of `../SAFETY.md`, which you have read twice.

- **A Pokémon standing in for a confused, frightened, dying or hurting person.** Forbidden
  outright. Two wave-two topics — delirium/dementia/depression, and pain in someone who cannot
  self-report — were declined in full for this reason rather than written around, and declining
  was the right call. If the only mapping you can find requires it, decline the topic and say so.
- **Fainting, KO, or Revive as death, resuscitation or bereavement.** The game's fainting is
  reversible by design and the mapping is obscene. Prognosis, dying, bereavement, mental-health
  crisis, self-harm, safeguarding, capacity, consent and coercion are all set-aside; handle them
  in the plain-prose section or not at all.
- **A Trainer standing in for a clinician making a decision about a person.**
  Trainer-as-prescriber works for a decision about a *drug* or a *protocol*; it stops working the
  moment the Pokémon is the patient.
- **Catching as diagnosis or admission.** Specifically avoided: catching is acquisitive and
  non-consensual, and the mapping reads badly however carefully it is framed. Poké Ball mechanics
  are used in m011–m013 for *probability* only, never for the act.
- **Frailty via Shedinja, and the shape it shares with others.** Shedinja — 1 HP, Wonder Guard,
  ended by one point of anything — is the obvious mapping for frailty and it requires a creature
  to be the patient whose resilience is the subject. A writer reached for it, saw the problem, and
  wrote health inequality instead, noting that *"the next writer will reach for Shedinja too"*.
  They were right. Shedinja is available for a **type-override** point with no person attached
  (m047 uses it that way); it is not available as a frail patient. The same shape blocked
  paediatric differences (a low-level Pokémon as the patient), analgesia, and crowding and flow
  (boxed Pokémon as queued patients). All four remain unwritten and should be commissioned with an
  explicit instruction about what may stand in for the patient, or not at all.
- **A Pokémon half with no Pokémon in it.** Raised by a writer declining supportive and palliative
  care, and the argument is worth keeping: that territory is almost entirely what `SAFETY.md`
  fences off, so there is no mechanism left to carry an analogy, and the result would not be a
  low-scoring pair but a *degenerate record* for a dataset whose premise is two registers of the
  same content. The corpus floor for taste-constrained answers is around 45, not zero. If an
  answer would land near zero because the whole subject is set aside, the subject is set aside —
  do not write it and do not soften the taste rule to make it scoreable.
- **Revive and Max Revive, for anything.** They sit in the same `item_effects.h` table as
  everything else, and nothing in Pokémon may stand in for resuscitating a person. m069 says so in
  its own text.
- **Breeding mechanics for the reproductive axis.** Day Care, egg groups and Destiny Knot are the
  obvious mapping and would have scored well. m060 keeps the analogy entirely on the *controller*
  — rhythms, thresholds, sign reversals — and says so out loud, which makes the omission legible.
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
