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

### General practice — m011–m015

| Medical concept | Device | Pair |
| --- | --- | --- |
| Pre-test probability | The same rustle on a different floor. Mt. Moon's encounter table against the route's | m011 |
| Prevalence and the limits of a sample | You do not clear Mt. Moon of Clefairy by meeting ten Zubat | m012 |
| Screening against case-finding | Sweeping the grass on purpose is a different act from meeting something in it | m013 |
| Polypharmacy | Four slots, one item, and the fourth addition is the one that loses | m014 |
| Continuity, and shared care | A Pokémon someone else raised does not obey, and that is in the code — badge-gated, by level | m015 |

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

### Oncology — m026–m030

| Medical concept | Device | Pair |
| --- | --- | --- |
| Classification that changed, and what the old one conflated | For three generations the damage category was computed from the type | m026 |
| Treatment toxicity written into the treatment | Read the move's own data and the cost is already in it | m027 |
| Exemptions that go by category rather than by name | The exemption list is types, not names — and the counter says when | m028 |
| What a response measurement cannot show | The bar is 48 pixels and never renders empty while anything is left | m029 |
| Sampling, and the thing the sample did not change | Three rods, one pond, and the pond never changed | m030 |

### Emergency — m031–m035

| Medical concept | Device | Pair |
| --- | --- | --- |
| The primary survey's ordering | Priority is read before Speed, and nothing done to Speed ever changes that | m031 |
| Why protocols exist | Red and Blue decided turn order with two if-statements; Emerald wrote it in a table | m032 |
| What triage optimises | Trick Room inverts the sort key and leaves the brackets alone | m033 |
| Compensation, and the reserve the monitor is not showing | PP is the budget, the bar is not showing it, and the bar is all the game shows | m034 |
| First aid for the untrained | Focus Energy *said* it raised the critical-hit rate; in Red and Blue it quartered it | m035 |

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
