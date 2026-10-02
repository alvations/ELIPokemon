---
id: "m084"
slug: overdiagnosis-in-primary-care
style: pokemon
category: general-practice
difficulty: advanced
question: "What is overdiagnosis, why can it never be seen in an individual, and what makes primary care generate it without any screening programme?"
tags: [overdiagnosis, incidental-findings, labelling, cascade, diagnostic-thresholds]
---

# The SEEN counter measures how hard you looked, and Route 116 never changed

Put **Illuminate** in party slot one and the encounter rate doubles. That is the whole opening
argument, and the arithmetic is short.

```
   EVERY NUMBER BELOW IS REAL, READ OUT OF THE EMERALD WILD-ENCOUNTER ROUTINE AND
   THE POKEDEX FLAG ROUTINE.

   ROUTE 116, table rate 20.  20 × 16 = 320 against MAX_ENCOUNTER_RATE 2880.

                              rate    per step    encounters per 1 000 steps
     nothing in slot one       320      11.1 %              111
     Illuminate in slot one    640      22.2 %              222
     and with a White Flute    960      33.3 %              333

   AND THE TWELVE SLOTS, ACROSS ALL THREE ROWS:

     20% Poochyena L6   20% Whismur L6    10% Nincada L6    10% Abra  L7
     10% Nincada  L7    10% Taillow L6     5% Taillow L7     5% Taillow L8
      4% Poochyena L7    4% Poochyena L8   1% Skitty  L7     1% Skitty  L8

     Identical. Byte for byte. In all three rows.

   So the third row fills the Pokédex three times as fast as the first, and not one
   Pokémon has been added to Route 116. A Trainer comparing their own dex count this
   month against last month, having picked up an Illuminate lead in between, is
   measuring their lead slot. They will read it as a change in the route.
```

That is the entire shape of the problem. A count that rises with the intensity of looking,
reported as if it were a property of the place being looked at.

**Two answers already hold the ground this one is standing next to, and it defers to both.** m013
is where lead-time bias, length bias and overdiagnosis are worked through for a screening
programme. Oncology's m030 is where overdiagnosis is established as a real harm rather than a
technicality, where it is separated from a false positive, and where the population inference is
set out in full — and m030's own device, three rods in one pond that never changed, is the same
family as the rate levers above. Neither argument is re-derived here.

What is left is the version with no programme behind it, and the cartridge is precise about why
that is worse:

```
   REAL SAVE DATA. Emerald's game-stat array holds both halves of the fraction:

     GAME_STAT_STEPS           = index 5    the denominator
     GAME_STAT_WILD_BATTLES    = index 8    the numerator

   And the Pokédex screen, which is the screen anybody actually reads, shows the
   SEEN count and the OWN count with NEITHER of them beside it.

     a Trainer running rounds      could divide. Same route, same lead, counted
                                   steps, two totals — the rate is recoverable.

     a Trainer who just walks      cannot. The encounters arrived while they were
                                   doing something else, the step count is not on
                                   the screen they are reading, and the SEEN
                                   number rises monotonically whatever happens.
```

A count with no denominator next to it can only be read as news about the world. That is the
primary-care version of this problem and it is not the one a programme has.

## The record is append-only, and the only code that clears it does so for the wrong reason

The Pokédex keeps two separate bit arrays — `seen` and `owned`, one bit per national dex number —
and m037 established the pair for suspicion against confirmation. What matters here is what the
flag routine can and cannot do.

```
   REAL CODE. GetSetPokedexFlag has four cases. Two of them read, two of them write:

     FLAG_SET_SEEN     ORs the bit into pokedex.seen, AND into seen1, AND into seen2
     FLAG_SET_CAUGHT   ORs the bit into pokedex.owned

   THERE IS NO CASE THAT CLEARS A BIT. None. Release the Pokémon, trade it away,
   never see one again — the bit stays set for the rest of the save file.

   And the one path that DOES clear: the SEEN bit is stored in three places, and a
   READ compares all three. If they disagree, the routine clears all three and
   returns 0.

        three copies agree        ──►  reports 1
        three copies disagree     ──►  wipes them and reports 0
                                       └─ "never seen" and "the record
                                          contradicted itself" come back as
                                          the same answer, and the reader
                                          cannot tell which one happened
```

A label that cannot be removed, and a contradiction resolved to a clean zero that looks exactly
like an absence. Both halves of that transfer directly, and neither needs a metaphor to explain.

## A definition moved, and five rules changed with it, and nothing happened to anybody

**Clefairy** was a Normal-type for three generations. From the sixth it is a Fairy-type — in the
expansion's species data that is a compile-time switch, `P_UPDATED_TYPES >= GEN_6`, and the
creature on either side of it is otherwise the same entry. Read the chart against the new typing
and five matchups changed at once:

| attacking type | against Clefairy as Normal | against Clefairy as Fairy |
| --- | --- | --- |
| **Dragon** | ×1 | **×0** — no mechanism at all |
| **Poison** | ×1 | ×2 |
| **Steel** | ×1 | ×2 |
| **Fighting** | ×2 | ×0.5 |
| **Bug**, **Dark** | ×1 | ×0.5 |

**Jigglypuff** went from Normal to Normal/Fairy in the same generation, and **Magnemite** gained
Steel back in the second. No Clefairy anywhere was altered. The classification was, and every
downstream rule followed it instantly. That is what a widened diagnostic criterion does: the
population is the same on both sides of the change and the consequences are not.

## The finding whose record outlives the finding

**Pokérus** is the incidental finding, written out in one byte. The mapping here is to the
*record* and not to anybody's illness, which is the only reason it belongs in this answer at all.

* It is rolled in the routine that returns from a battle to the overworld, and it needs a 16-bit
  draw to come out at exactly one of three values. **Three chances in 65 536**, per non-link
  battle. Nobody goes looking for it; it turns up.
* The byte holds a strain in the high nibble and days remaining in the low one. When the days run
  out the low nibble is cleared — and then the routine checks whether the whole byte has reached
  zero, and if it has, it **writes 0x10 back in**. The game refuses to leave the record empty. A
  permanent marker, created by an explicit line of code, at the moment the condition ends.
* And the marker keeps acting. The routine that awards Effort Values asks the *ever-had* question,
  not the *currently has* question, and doubles the yield on it. Long after the thing is over, the
  record is what the rest of the system reads and responds to.

Nothing in that paragraph is about a Pokémon being unwell. All of it is about a flag that gets
set, cannot be unset, and changes how every later routine behaves — which is what a label does,
and the resemblance is not an accident of the analogy.

## And the cascade, which is one irreversible step dressed as a small one

```
   REAL LEARNSETS, READ OUT OF THE EMERALD LEVEL-UP DATA.

   VULPIX learns, by level:          NINETALES learns, by level:
     1  Ember                          1  Ember
     5  Tail Whip                      1  Quick Attack
     9  Roar                           1  Confuse Ray
    13  Quick Attack                   1  Safeguard
    17  Will-O-Wisp                   45  Fire Spin
    21  Confuse Ray                   ─────────────────────────
    25  Imprison                      and that is the entire list
    29  Flamethrower
    33  Safeguard
    37  Grudge
    41  Fire Spin

   Use a Fire Stone at level 20 and Imprison, Flamethrower and Grudge are not
   delayed. They are off the level-up route permanently, because Ninetales' list
   does not contain them and evolution does not run backwards.

   What remains is the expensive route: TM35 is Flamethrower, and a Generation III
   TM is consumed by the one Pokémon that uses it.
```

One act, taken for a good reason, at a moment that felt minor, closing a cheap route and leaving
only a costly single-use one. That is the structure of a cascade, and the Trainer who used the
stone was not making a mistake — they were making a decision whose cost arrives in a different
part of the game.

## Where the metaphor stops

A person told they have a condition is changed by being told. They may take a medicine for
decades, be declined insurance, attend appointments, undergo procedures with real complications,
and describe themselves as a patient, for something that was never going to affect them. Each of
those harms is real, and none of them is visible *as a consequence of the diagnosis*, because the
version of that person who was never told does not exist to be compared with.

The mirror harm has to be stated just as plainly, because it is worse when it happens. Somebody
whose diagnosis was missed or made late carries a consequence that is concrete, attributable and
sometimes severe, and no amount of reasoning about overdiagnosis makes that acceptable. The honest
position is that both errors are real, that only one of them generates feedback, and that the
invisible one therefore has to be counted deliberately rather than felt.

And this belongs here too. A person who has been given a label is not making a mistake by taking
it seriously. They were told something true, by someone they were right to trust. If the label
later proves to have been unnecessary, that is a property of the system that produced it and not a
failing of the person who believed it.

## What a Gym Leader is listening for

Whether the Trainer can say what doubled — the rate, not the route — and resist the conclusion the
dex count invites, and name the two game stats that would have let them divide. Then the flag
routine: that there is no clearing case, and what the three-copy wipe does to the difference
between *never* and *contradicted*. Then the retyping, and
the observation that no Clefairy changed. Then the Pokérus byte, and specifically the line that
writes 0x10 back in, because that line is the whole labelling argument in one instruction. Then
the Fire Stone, and which route it closed. Then the counterweight, offered unprompted. Then the
hard one: what a Trainer could measure that would tell them a count is tracking their own
looking.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The diagnostic criteria currently in force for any condition the reader has in mind, together
  with the previous version, because the comparison between the two is where a definitional change
  becomes visible *[country-dependent]*.
* The published literature on overdiagnosis and on incidence-mortality divergence, in the
  epidemiology and public-health journals, for the population evidence the argument rests on.
* Any systematic review of incidental findings on cross-sectional imaging, for the frequency of
  findings and of the cascades that follow them.
* The reader's national guidance on the management of specific incidental findings, where it
  exists, which is the only authority on what to do with one *[country-dependent]*.
* The literature on diagnostic labelling and its effects on symptom reporting, absence from work
  and self-rated health, for the harms that are caused by the label rather than by the condition.

The Pokémon figures are a separate matter and are not covered by the line above. Illuminate
doubling the encounter rate and the White Flute adding half, the rate being multiplied by 16 and
compared against a maximum encounter rate of 2 880, the Route 116 table with its levels and its
rate of 20, the Pokédex keeping separate seen and owned bit arrays with the seen bit held in three
places, the flag routine having no case that clears a bit and its read wiping all three copies and
returning zero when they disagree, Clefairy becoming a Fairy-type from the sixth generation and
Jigglypuff becoming Normal/Fairy with Magnemite gaining Steel in the second, the five chart
entries that changed with Clefairy's typing, the game-stat array holding a step counter at index 5
and a wild-battle counter at index 8, the Pokérus roll sitting in the return-from-battle
routine and requiring a 16-bit draw to land on one of three values, the byte's strain and
day-counter nibbles, the line that writes 0x10 back when the byte would reach zero, the Effort
Value routine reading the ever-had test and doubling on it, Vulpix's and Ninetales' level-up
learnsets, and TM35 being Flamethrower, were all read directly from the pret and rh-hideout
decompilation projects, which this environment can reach. The single-use nature of a Generation
III TM is a property of those games stated here from general knowledge of them rather than read
out of a specific routine.

## Scope and safety

This is revision material about how a diagnostic system behaves, written for someone already
training in or qualified for the field. It is not a clinical reference, not a decision aid, and
nothing here is a reason for any individual to doubt, stop or change anything about their own
care — that belongs with the clinician who knows them. No condition, threshold, incidence figure
or overdiagnosis estimate is named here on purpose: the estimates are specific to the condition
and the setting, several are strongly contested, and all are revised. The encounter rates, flag
routines and learnsets above are real and stand in for a mechanism; none of them is a clinical
quantity and no clinical figure should be read out of them. Anyone who has been given a diagnosis
and has questions about it should take those questions to their own clinician rather than to this
page. If someone is unwell right now, the relevant action is to contact local urgent care or the
local emergency number, not to read this.

## Where this stands, October 2026

The definition and the reasoning are mainstream and stable, and so is the claim that individual
cases cannot be identified. What is actively contested, condition by condition, is the
*magnitude*: the proportion of diagnoses that are overdiagnoses is estimated differently by
different groups using different methods, and those arguments are live rather than settled. The
diagnostic thresholds themselves move, which is one of the mechanisms described above, so any
specific criterion read here would date quickly. Guidance on incidental findings is being written
in several systems and did not exist a decade ago. The Emerald figures are stable because the
games are finished, and the Fairy-type change is pinned to the sixth generation because the
typing before it was different. Take criteria and estimates from current local guidance and the
current literature rather than from here, as of October 2026.
