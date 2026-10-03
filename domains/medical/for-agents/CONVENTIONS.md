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
| Why is the inverse care law a mechanism rather than a complaint, and what does treating it as a mechanism change? | The badge stat boost — **three cartridges, three different facts; my own correction to this row
was also wrong.** Emerald **does** have it, in `src/pokemon.c`: `CalculateBaseDamage` calls
`ShouldGetStatBadgeBoost` four times — `FLAG_BADGE01_GET` for Attack, `FLAG_BADGE05_GET` for
Defence, `FLAG_BADGE07_GET` for both Special stats — each `(110 * stat) / 100`, guarded off in
link, e-reader, recorded and Frontier battles and for the non-player side. With `FLAG_BADGE03_GET`
giving Speed ×110/100 in `GetWhoStrikesFirst`, that is **five** in-battle badge effects in
Emerald, not one. `ApplyBadgeStatBoosts` is `pokered`'s name for the Generation I routine, which
is where ×1.125 and `stat += stat>>3` come from. **And the parity in this row was backwards.** The
boosting flags are 01, 03, 05, 07 — the **odd** ones — while Emerald's obedience check in
`src/battle_util.c` reads `FLAG_BADGE02/04/06/08`, the even ones. The complementarity is real and
perfect; the row had it the wrong way round. The sequence of errors is worth keeping: the row was
written with Gen I's function name and multiplier, a writer correctly found that name absent from
`pokeemerald`, I "corrected" it by grepping `battle_main.c` for the Gen I name and `pokefirered`
for the real one and never opening `pokeemerald/src/pokemon.c`, and two further writers caught me.
**Two negatives are not a finding.** ×1.125 is **relative**, so it widens the absolute gap while
improving both; it is awarded for having already won; and it returns immediately in a link battle,
so the advantage is invisible in the only format where like is compared with like. The four badges
that boost are the even bits — exactly the four that m015's obedience check does *not* use | m050
|
| Why is a referral decision a threshold rather than a judgement, and what is a gatekeeper actually optimising? | The **Repel number**: `IsWildLevelAllowedByRepel` walks the party and stops at the first member with HP that is not an egg — **not the lead** — and falls through to FALSE with a wiped party, so the item cancels everything. Route 116's three thresholds, where 6→7 is free, 7→8 costs the same slot every time, and 8→9 makes the route read empty. The **mass outbreak**'s two-day counter as urgency distinct from probability, still subject to both filter flags | m081 |
| Why does a system that is easy to enter behave differently from one that is hard to enter, and who does each one filter out? | The encounter-**rate** pipeline — ×16, bike ×80/100, White and Black Flute, Cleanse Tag ×2/3, lead ability ×2 or ÷2, cap 2880, the 40 per cent new-metatile skip — as access, against the **table** as need: nine levers, not one of which touches a slot. The three rods as the route in restricting what is reachable rather than how often | m082 |
| Why does a preference-sensitive decision have no single right answer, and what does that demand of the consultation? | **`Thunder` in rain skips the accuracy check entirely** while sun overwrites `moveAcc` to 50 — so the same pair is a preference-sensitive trade in clear weather and effectiveness-sensitive in rain, and the *class* of the decision changes with the field. The chart is in the cartridge and nothing in the battle menu shows it: a decision aid is information moved forward, not new information | m083 |
| What is overdiagnosis, why can it never be seen in an individual, and what makes primary care generate it without any screening programme? | **`GetSetPokedexFlag` has no case that clears a bit**, and its three-copy integrity wipe returns 0 — labelling that outlives what it labelled. **Pokérus**'s `if (pokerus == 0) pokerus = 0x10;` forces a permanent marker, and `MonGainEVs` doubles on `CheckPartyHasHadPokerus`, the *ever-had* query. The Gen VI Fairy retyping as a definitional change with five instant downstream consequences | m084 |
| Why can an intervention prevent many cases across a population while offering almost no individual in it a benefit they could notice? | The bike's 80/100 as the population measure against abolishing the two rarest slots: ten-fold for nothing nameable, against 1.11 points per step for everyone. **Both 1 per cent slots are Geodude, and Geodude is not rare** — it holds 10 per cent of the table through two 4 per cent slots, so an intervention aimed at the tail removes a fifth of one species and leaves every Makuhita, Zubat and Abra untouched. Sandstorm's maxHP/16 as Leftovers with the sign reversed, set by one Sand Stream for everybody present | m085 |

### Dermatology — m016–m020, m051–m055, m086–m090

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
| Why do skin infections and infestations that look alike need different treatments, and what is the skin scraping or swab actually for? | **Silcoon and Cascoon**: identical in every base stat, ability, typing and effort yield, differing in body colour and **one point of experience yield, 71 against 72** — and the fork is `(personality >> 16) % 10 <= 4`, fixed at creation. Two things that look the same, told apart only by a measurement nobody takes by eye | m086 |
| Why are the nail plate and the hair shaft records of events that happened months earlier, and what does that change about the history? | **The six growth-rate curves** as records of elapsed time, with `Erratic` and `Fluctuating` changing shape mid-range; and a **Rare Candy** *writing* `gExperienceTables[growthRate][level + 1]` rather than adding to it, so the readout moves and the record of how it got there is destroyed | m087 |
| Why is photoageing a function of cumulative ultraviolet dose, and why is the number printed on a sunscreen not the protection a person gets? | **Effort values**: `hpEV / 4` in `CalculateMonStats`, capped at 510 total and 255 per stat — with the cap named in the answer as the point where the analogy breaks, because ultraviolet dose does not cap. The honest limit is stated inside the scored body rather than quarantined in the plain-prose section | m088 |
| Why does the level at which the skin splits determine almost everything that follows in a blistering disease? | **The third generation keeps "protected" in five separate structures** — `status1`, `status2`, `gStatuses3`, the side statuses with their timers, and the field weather — and which one a state lives in decides what reads it, what clears it, and what survives a switch. Sampling from inside the blister is `gBattleMons[i].status2` returning zero while the answer sits in `gSideStatuses[side]`: **a confident zero from the wrong structure is worse than no result** | m089 |
| Why is a weal that comes and goes a different problem from a swelling that does not, and what follows from that for treatment? | **`Cmd_setsafeguard` fails rather than refreshing its own timer**, and Safeguard's check sits in the script while Shield Dust's sits behind `!primary` — so one blocks Will-O-Wisp and the other does not, and the only difference is where the check is written | m090 |

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

### Oncology — m026–m030, m061–m065, m096–m100

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
| Why does a targeted therapy that is working stop working, and what does the mechanism of escape tell you about what to do next? | **`Color Change`'s preconditions**, of which `TARGET_TURN_DAMAGED` is load-bearing: the type change fires only when the hit did damage, and `SET_BATTLER_TYPE` overwrites both slots. The capacity is in Kecleon's species table before the battle. **`Castform`'s `CastformDataTypeChange`** is the reversible counterpart, and the answer says plainly that no mechanic models an irreversible lineage change | m096 |
| In what sense is a single tumour biopsy a sample of a population under selection, and what follows for how a biomarker result is interpreted? | **`gSpeciesInfo[species]` against the `Personality Value`** — what every member shares by ancestry against what this one has. And **`TryGenerateWildMon`'s ordering**: the slot and level are drawn, *then* the filters delete the draw, so the filter changes no individual and reshapes the composition, and Keen Eye's `!(Random() % 2)` makes it partial, enriching rather than purifying | m097 |
| What is a cancer multidisciplinary meeting actually for, and what failure modes is it designed to prevent? | **`gTrainers[].aiFlags` as a committee**: scores initialised to one hundred, `CheckMoveLimitations` striking options off before any script runs, bit position as the agenda, `Random() % numOfBestMoves` on a tie — and 640 of 855 entries run one member. **`Helping Hand`** is the contribution with no value outside the forum: priority five, power zero, and it fails without a present partner | m098 |
| Why does a crude ordinal performance status scale predict tolerance of systemic therapy better than more precise measurements, and where does it mislead? | **`Cmd_hiddenpowercalc`** reading twelve of thirty IV bits, with all-thirty-one collapsing to one answer and `(40*0)/63 + 30` as the floor — a crude index computed from precise inputs. And **`F_DYNAMIC_TYPE_IGNORE_PHYSICALITY`**: the same reading honoured for one purpose and overridden for another, with the override commented in the source | m099 |
| Why are a biomarker test and the drug it selects for treated as one object rather than two, and what goes wrong when they are separated? | **Species-gated hold effects** — six consecutive lines of `CalculateBaseDamage` where the identity test and the effect are one `if` — as a companion diagnostic, against **`sHoldEffectToType`**'s seventeen rows, where Charcoal's parameter raises the stat only for a matching type: a weight, not a gate. Plus **`GetGenderFromSpeciesAndPersonality`**, where one byte reads male for Treecko and female for Kecleon, and for Chansey and Beldum the comparison is never performed at all | m100 |

### Emergency — m031–m035, m066–m070, m101–m105

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
| Why is the workup for chest pain ordered by danger rather than by likelihood, when a dozen unrelated mechanisms produce the same complaint? | **`BattleScript_ButItFailed`**: 95 jumps from 55 distinct labels into one five-instruction label, one bit, and `MOVE_RESULT_NO_EFFECT` as a composite that erases three unrelated causes — five miss strings against one failure string. One presenting complaint, a dozen mechanisms, and a readout that cannot tell them apart | m101 |
| Why does the differential for breathlessness split by system rather than by severity, and what do the first few observations actually buy? | **Nine end-of-turn HP sinks held in five stores**, with one purpose-built jump instruction per store, while `UpdateStatusIconInHealthbox` reads `MON_DATA_STATUS` only and draws five graphics — so four of the nine are invisible on screen. Leftovers and Sandstorm share maxHP/16 and cancel | m102 |
| Why is immobilising a fracture treatment in its own right rather than packaging for transport? | **Prevention as refusal at the point of entry**: Safeguard (effect bytes ≤ 7, secondary only, no cover against an ability-sourced status) and Shield Dust (≤ 9, never the damage), ten hand-written check sites, and `BattleScript_SafeguardProtected` as the **only** evidence it ever worked | m103 |
| Why is imaging a test with a harm of its own, and what is a clinical decision rule actually for? | **`EFFECT_RECOIL` billing a fraction of damage dealt against `EFFECT_RECOIL_IF_MISS` billing on a miss**, with `MOVE_RESULT_DOESNT_AFFECT_FOE` as the one free failure — and **`Rock Head` waiving the cost of success and not the cost of failure**, which is the whole argument about a test that has its own harm | m104 |
| Why is a presentation that looks social rather than medical still a clinical problem, and why is dismissing it a diagnostic error? | **Spikes in `gSideStatuses` with no screen indicator at all**, while `STRINGID_PKMNHURTBYSPIKES` names the entrant on every entry. m036's device doing a second job: the cause is stored where nothing displays it and the effect is attributed to whoever walked in | m105 |

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
- **Paediatric skin was re-offered with the explicit no-child-mapping instruction, and declined
  again.** The writer worked three candidate devices and rejected all three: a flat Sitrus Berry
  30 against different maximum HP is the surface-to-volume point but makes small-body-equals-child
  explicit; `Substitute`'s `maxHP/4` is a *fixed fraction*, so it cannot carry "thinner relative
  to what it protects" at all; and height and weight from `gSpeciesInfo` would need an invented
  derived ratio dressed up as a code reading. Its objection is the one to keep: **removing the
  vehicle is not supplying one.** Do not re-commission any of these four on the same terms — they
  need a device, not a prohibition.
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
- **Burns.** Every mapping either put the injury on a creature, or made the in-game `Burn` status
  stand for a thermal burn — which both puts a Pokémon in the patient's place and makes the
  condition itself the joke. And depth assessment rests substantially on sensation, which is pain
  assessment, which is set aside. The nearest clean device (a move's `target` field against its
  `power`) does not carry the second half of the clinical point, that depth declares late.
  Declined.
- **Disposition.** The natural mapping is party-against-box, which is the boxed-Pokémon-as-queued-
  patients shape above. Every alternative is m070's handover device doing a second job it does not
  fit.
- **The structured assessment of someone who will not respond.** The patient would have to be an
  asleep or fainted Pokémon, and the device — an ordered chain where each step gates the next — is
  already m031, m032 and m067. It would be the fourth re-derivation of one idea in one specialty.
- **Complexity against severity.** Every mapping needs a Pokémon to *be* the complex patient. Same
  shape as frailty, and m047 already holds the composition argument.
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

| `Encore` lasts 2–6 turns | **3–6.** `Cmd_trysetencore` sets `encoreTimer = (Random() & 3) + 3` |
| `Encore` refuses two moves | **Three** — Struggle, Encore and Mirror Move — plus no-PP-in-slot and already-encored |
| `Rollout` doubles from its first hit | **It does not.** `for (i = 1; i < (5 - rolloutTimer); i++)` gives 30/60/120/240/480, doubled again by the `STATUS2_DEFENSE_CURL` bit |
| `Rest` fails only at full HP | **Four ways.** `jumpifcantmakeasleep` sits in front of `trysetrest` and checks `UproarWakeUpCheck`, Insomnia and Vital Spirit. Its counter is an *assignment* of three turns, which clears poison, burn, freeze and paralysis in the same instruction |
| Five abilities are gated on the contact flag in Gen III | **Six.** Cute Charm is the one people miss, beside Rough Skin, Poison Point, Static, Flame Body and Effect Spore |
| There is a powder flag in the Advance data | **There is not.** Spore, Sleep Powder and Stun Spore share only Grass type and Magic Coat affinity. Powder immunity and Safety Goggles are later additions |
| `Thunder` hits a Fly user because rain makes it always hit | **No.** `AccuracyCalcHelper` returns a miss on `STATUS3_ON_AIR` *before* the rain clause is reached. It works because `BattleScript_EffectThunder` sets `HITMARKER_IGNORE_ON_AIR` itself, unconditionally, with no damage doubling — unlike Gust and Twister |
| `PERCENT_FEMALE(50)` is 128 | **127.** The macro is `min(254, ((percent * 255) / 100))`, so 12.5 per cent is 31, not 32 |
| `Rock Head` waives Hi Jump Kick's crash damage | **It does not.** `ABILITY_ROCK_HEAD` appears only in `BattleScript_MoveEffectRecoil`; the crash branch has no such jump. Rock Head waives the cost of success, not the cost of failure |
| `Shield Dust` blocks `Will-O-Wisp` | **It does not.** The Shield Dust clause requires `!primary`, and Will-O-Wisp applies the burn via `seteffectprimary`. Safeguard *does* block it, because that script checks the side status itself — two protections, one works, and the only difference is where the check is written |
| `Safeguard` blocks any status | **Not an ability-sourced one.** The check carries `!(gHitMarker & HITMARKER_STATUS_ABILITY_EFFECT)`, so Effect Spore, Poison Point and Flame Body get through |
| `Mist` and `Clear Body` block every stat reduction | **Both exempt a `certain` reduction and Curse by name** |
| A Rare Candy adds experience | **It writes** `gExperienceTables[growthRate][level + 1]` into the experience field, discarding surplus progress |
| `Rapid Spin` clears the hazards | **Exactly one thing per use**, in a fixed order: trapping, then Leech Seed, then Spikes |
| The Repel threshold reads your lead | **The first party member with HP that is not an egg** — and it falls through to cancelling every encounter when there is none. `IsAbilityAllowingEncounter`, in the same file, *does* read slot 0 only |
| Gen III land encounters use ten slots at x/256 | **That is Generation I.** Gen III uses **twelve** slots at 20/20/10/10/10/10/5/5/4/4/1/1 per cent, in `src/data/wild_encounters.json`. Do not carry one across |
| Tauros learns Double-Edge | **Not by level-up.** Onix 57, Golem 62, Chansey 57, Marowak 61 all do |
| `Quick Claw` rolls `Random() % 100` | `gRandomTurnNumber < (0xFFFF * param)/100`, and it sets Speed to `UINT_MAX` — so it beats any Speed and no priority bracket |
| Most moves use `EFFECT_HIT` | **24 of 355.** The shared *script* pipeline is the real story: 41 effect scripts reaching one label through 45 jumps |
| The Safari Zone counter is 500 | **502 in Generation I**, 500 in Emerald. The gate worker says 500 and the auto-walk in spends two |

| Gen III `Stockpile` raises Defence and Special Defence | **It does not.** `Cmd_stockpile` increments a counter and sets a message, nothing more. The stat boosts are a Gen IV addition |
| `Wish` heals half the *wisher's* maximum HP | **In Gen III, half the recipient's**: `gBattleMoveDamage = gBattleMons[gBattlerTarget].maxHP / 2`, and `wishMonId` is used only to print a name. The wisher's-max-HP version is Gen V onward |
| `Sitrus Berry` restores a fraction | **Flat 30 in Gen III** (`holdEffectParam = 30`); Oran is 10. The percentage Sitrus is Gen IV. Auto-eat fires at `hp <= maxHP / 2 && !moveTurn` |
| `Rock Head` waives recoil | **Three costs and it waives one.** Not the crash damage of a missed Hi Jump Kick, and not Struggle's recoil either — `BattleScript_MoveEffectRecoil` jumps to `BattleScript_DoRecoil` on Struggle *before* the ability check. It waives the cost of success, not the cost of failure, and not the cost of having no option |
| Fishing is three tables, one per rod | **One ten-entry table with three disjoint index groups** — `old_rod [0,1]`, `good_rod [2,3,4]`, `super_rod [5..9]` — drawn against a single shared denominator in `ChooseWildMonIndex_Fishing` |
| Fishing runs the encounter filters | **Neither.** `GenerateFishingWildMon` takes no flags argument, so no Repel and no Keen Eye, and `FishingWildEncounter` runs no rate test and no new-metatile roll. The same shape as Sweet Scent's `flags = 0`, except Sweet Scent's zero is deliberate and this one is a parameter nobody threaded through |
| `IsAbilityAllowingEncounter` only reads slot 0 | It also requires `playerMonLevel > 5`, so it is unreachable with a lead at level 5 or below; it cancels only at or below the lead's level minus five; and it fires on `!(Random() % 2)`, so it is partial |
| `CheckMoveLimitations` has five causes | **Five named mechanics, eight ORed conditions**: empty slot, zero PP, Disable, Torment, Taunt, Imprison, Encore, Choice lock — read from six stores, one of them (`gStatuses3`, via `GetImprisonedMovesCount`) on the other side of the field |
| A per-route species share can be recalled | **It cannot.** Two were wrong by four points from arithmetic-by-memory in one block — Poochyena is 28 per cent of Route 116 and 30 per cent of Route 102. Recompute from `src/data/wild_encounters.json` every time; this is the adjacent failure to the generation rule below and just as silent |

| `Shield Dust` and `Safeguard` differ in "where the check is written" | **One shared check plus a hand-maintained list of ten.** Both clauses in `Cmd_setadditionaleffects` carry `!primary` and both are excused by `HITMARKER_STATUS_ABILITY_EFFECT`; they differ only in an effect-byte ceiling, 9 against 7. Safeguard catches a *primary* status because the check is written **again, by hand, inside ten individual move scripts** — Sleep, Toxic, Confuse, Poison, Paralyze, Swagger's and Flatter's confusion branches, Will-O-Wisp, Yawn and Teeter Dance. Shield Dust has **zero** script sites |
| The Safari Zone's entry walk spends two steps | **Neither the number nor the ordering carries across.** Generation I writes 502 into the counter *before* a three-press auto-walk, with the event flag set after the call, so the walk is live. Emerald runs its seven-command entry movement *first* and `EnterSafariMode` then sets the counter to 500 and the flag — and `SafariZoneTakeStep` returns early without the flag, so **Emerald's walk in is free and the full 500 is spendable** |
| `Spikes` costs a sixteenth | **maxHP/8, /6, /4 by layer** — `(5 - spikesAmount) * 2` — floor 1. Gen III exempts on exactly two conditions, Flying type and Levitate; there is no Air Balloon, Iron Ball or Gravity in the check |
| `Sitrus Berry` is a percentage | Flat **30** in Gen III, and the item's own description says so. The percentage is Gen IV |
| `Surf` hits your partner | **It does not.** Surf is `MOVE_TARGET_BOTH`; Earthquake, Explosion and Self-Destruct are `MOVE_TARGET_FOES_AND_ALLY`. Two writers had this the wrong way round and one answer's whole H1 depended on it |
| `Reflect` halves damage | **Two thirds in a double battle** — `damage = 2 * (damage / 3)` when two defenders are alive, a plain halving otherwise, and only when `gCritMultiplier == 1` |
| `Protect` only decays | It also **fails outright if the user acts last in the turn**: `if (gCurrentTurnActionNumber == (gBattlersCount - 1)) notLastTurn = FALSE;` |
| `CreateShedinja` needs a spare Poké Ball | **Not in Emerald.** The test is the evolution method plus `gPlayerPartyCount < PARTY_SIZE` and nothing else. The ball is a later generation |
| `Low Kick` reads an individual's weight | **The published species figure**, `gPokedexEntries[dexNum].weight`, identical for every individual. `.height` sits beside it and is never read. Magikarp at exactly 100 falls in the 40 band, because the comparison is strict |
| A move's damage is halved for hitting several targets | **Keyed to the field, not the body count.** The halving applies only to `MOVE_TARGET_BOTH` with two defenders alive, so Earthquake hits three battlers undivided while Rock Slide and Gen III Surf are halved |

And the general rule behind the table: **state the generation, or do not state the number.** An
unqualified mechanical figure is the single most common defect in drafts, and the one a reader is
least able to catch.


## Part V — writing against the metric, and when that is correct

Three patterns recur in hand-backs and all three are the right call. They are here so a writer can
make them without first inventing the argument.

**Write the absence of a mapping rather than inventing one — at section scale, not only at answer
scale.** One writer did this three times in five answers: *"here the game has nothing, and saying
so is more useful than inventing something"* for pre-analytic degradation (a held item is in the
slot or it is not; there is no degraded-item state); that nothing in Pokémon models an observer
disagreeing with a subject, which is the largest gap between a computed index and an assigned one;
and that no mechanic models an irreversible lineage change. Each cost density. Each is better than
the forced mapping.

**Put the analogy's honest limit where the device is used, not in the unscored section.** A writer
kept *"effort values cap at 510 total and 255 per stat — ultraviolet dose does **not** cap; the
analogy breaks here"* inside the scored body, on the grounds that a limit stated where the device
is used is read by someone using the device and one quarantined at the end is not. It cost a
little density and was right.

**The mandated plain-prose sections are free, and a writer who thinks otherwise writes them short
for no reason.** Measured across one wave: those sections run **28 to 36 per cent** of a Pokémon
half's text, all of it excluded from scoring, and the answer carrying the fullest one still scored
87.0. There is no tension between the metric and writing them properly. Write them at length.

**And one thing to know about the correspondence requirement.** It is a quality instrument, not a
formatting one. A writer whose first drafts did not correspond found that in three of five cases
the reason was that the Pokémon device had surfaced content the serious half had folded away — so
restoring correspondence meant adding load-bearing clinical content to the rigorous half, not
padding. Enforcing it found three real gaps.
