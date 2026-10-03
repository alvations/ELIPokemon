---
id: "m148"
slug: controlled-drugs-and-the-legal-framework
style: pokemon
category: pharmacology
difficulty: intermediate
question: "Why is the legal framework around a controlled drug a separate structure from its pharmacology, and what does that structure actually do?"
tags: [controlled-drugs, regulation, custody, records, law]
---

# Mew and Latios both total 600. One is on the list and one is not, and the list is the whole reason.

Read the two rows out of `src/data/pokemon/species_info.h` and then read the array in
`src/frontier_util.c`.

```
   from species_info.h            HP  Atk  Def  Spe  SpA  SpD   total
   ────────────────────────────────────────────────────────────────────
   Mew                           100  100  100  100  100  100     600
   Celebi                        100  100  100  100  100  100     600
   Jirachi                       100  100  100  100  100  100     600
   Latios                         80   90   80  110  130  110     600
   Latias                         80   80   90  110  110  130     600

   from frontier_util.c
   ────────────────────────────────────────────────────────────────────
   const u16 gFrontierBannedSpecies[] =
   {
       SPECIES_MEW, SPECIES_MEWTWO, SPECIES_HO_OH, SPECIES_LUGIA, SPECIES_CELEBI,
       SPECIES_KYOGRE, SPECIES_GROUDON, SPECIES_RAYQUAZA, SPECIES_JIRACHI,
       SPECIES_DEOXYS, 0xFFFF
   };
```

Five species whose base stat totals are **exactly the same number**. Three of them cannot be
entered into the Battle Frontier and two of them can. Nothing in the stat block distinguishes the
banned from the permitted, because the stat block is not what the list was built from. The list
was built by somebody, for reasons about how the facility should feel, and then written down as
ten identifiers and a sentinel.

Say the list out loud, because the names are the point. **Mew**, **Mewtwo**, **Ho-Oh**, **Lugia**,
**Celebi**, **Kyogre**, **Groudon**, **Rayquaza**, **Jirachi** and **Deoxys** cannot be entered.
**Latias**, **Latios**, **Regirock**, **Regice** and **Registeel** can. Five legendaries walk in
through the front door and ten do not, and no property any of the fifteen possesses sorts them
that way: **Rayquaza** totals 680 and **Registeel** 580, which would give you a threshold, except
that **Mew** at 600 is banned and **Latios** at 600 is not. A threshold is a rule. This is a list.

That is a legal schedule, exactly. In this answer the Pokémon is the medicine and the Frontier's
entry desk is the legal framework. Nothing here stands in for a person.

`m045` used this same array as a formulary — a purchasing decision written into the cartridge. The
reuse is deliberate and the point here is a different one: not *which* things are on the list, but
that **the list is a separate structure from the engine**, maintained by hand, and that the engine
would run **Mew** perfectly happily if the desk let it through. The damage formula has never heard
of the Battle Frontier.

## The list is searched, not computed

```
   AppendIfValid, src/frontier_util.c

       for (i = 0; gFrontierBannedSpecies[i] != 0xFFFF
                && gFrontierBannedSpecies[i] != species; i++)
           ;
       if (gFrontierBannedSpecies[i] != 0xFFFF)
           return;
```

A linear walk to a sentinel. There is no rule, no threshold, no predicate on any property of the
species: there is a loop over an array of names. Add a line and the thing becomes ineligible;
delete a line and it becomes eligible; and no other file in the build changes, because nothing
else in the build depends on it.

Compare that with how the battle engine decides anything. Type effectiveness is a table lookup
driven by the Pokémon's own `types[2]`. Damage is an expression over base stats and stat stages.
Those are *derived*. Eligibility is *declared*. Two mechanisms, one cartridge, and the difference
between them is the difference between a pharmacological class and a schedule.

Two more properties of a declared list are sitting in those four lines. The terminator is `0xFFFF`
rather than a length, so **how long the schedule is, is itself data** — adding **Latios** to it
would be one comma and nothing else in the build would change, and nothing in the build could
notice. And the test immediately above it excludes an Egg and an empty slot before the list is
consulted at all, by a completely separate rule, which is the case of a thing that is not a
candidate for scheduling because it is not the kind of thing the schedule is about.

## The same object, with a second identifier under the second regime

`include/constants/battle_frontier.h` holds a second, parallel numbering for items.

```
   BATTLE_FRONTIER_ITEM_NONE            0
   BATTLE_FRONTIER_ITEM_KINGS_ROCK      1
   BATTLE_FRONTIER_ITEM_SITRUS_BERRY    2
   BATTLE_FRONTIER_ITEM_ORAN_BERRY      3
   ...
   BATTLE_FRONTIER_ITEM_SOUL_DEW       15
   BATTLE_FRONTIER_ITEM_CHOICE_BAND    16
   ...
   BATTLE_FRONTIER_ITEM_GANLON_BERRY   62
```

Sixty-two entries, hand-maintained, in a numbering that is **not** the `ITEM_*` numbering the rest
of the game uses. A **Leftovers** is `ITEM_LEFTOVERS` to the battle engine and index 25 to the
facility — one object, two identifiers, two registries, and a facility roster that stores the
frontier index and has to translate.

Read the names rather than the indices and the list stops looking technical. The permitted
sixty-two are the **King's Rock**, the **Sitrus Berry**, the **Oran Berry**, the **Chesto Berry**,
a **Hard Stone**, a **Focus Band**, the **Soul Dew**, a **Choice Band**, **Leftovers**, a **Quick
Claw**, a **Lum Berry**, a **Shell Bell**, a **Scope Lens**, a **Mental Herb**, a **White Herb**,
**Bright Powder**, a **Macho Brace**, the **Light Ball**, a **Thick Club**, a **Lucky Punch**,
**Metal Powder**, a **Deep Sea Tooth**, a **Deep Sea Scale**, **Silver Powder**, a **Sharp Beak**,
a **Spell Tag**, a **Twisted Spoon**, a **Black Belt**, **Black Glasses**, **Never-Melt Ice**, a
**Silk Scarf**, **Soft Sand**, a **Magnet**, **Mystic Water**, **Miracle Seed**, **Charcoal**, a
**Poison Barb**, a **Dragon Fang**, a **Dragon Scale**, a **Metal Coat**, **Lax Incense**, **Sea
Incense**, **Berry Juice**, and the rest of the berries, up to the **Ganlon Berry** at 62.

Five of those are the sharp ones, and the condition is in `CalculateBaseDamage` and in the
critical- hit calculation, species by species. The **Light Ball** does nothing unless a
**Pikachu** holds it. The **Thick Club** does nothing unless the holder is a **Cubone** or a
**Marowak**. **Metal Powder** does nothing unless the holder is a **Ditto** and is the one being
hit. The **Lucky Punch** does nothing unless it is a **Chansey**, and the **Stick** nothing unless
it is a **Farfetch'd**. Five permitted items, six species between them, and inert on everything
else in the game.

A permitted list containing five entries that are inert for all but six species is not a list of
things that work. It is a list of things you are *allowed*, and those are different documents —
which is the relationship between a formulary and a pharmacopoeia, and the reason reading one as
the other goes wrong in both directions.

A medicine under a controlled-drugs framework carries a second identifier in exactly this way: its
pharmacological identity, and its position in a schedule, in two documents, maintained by two
different processes, requiring translation at every point where they meet. And note which
direction this list runs: `gFrontierBannedSpecies` is an exclusion list of ten, while the item
list is an **inclusion** list of sixty-two — everything not on it is unavailable. Two lists in one
header, one denying and one permitting, which is the difference between a prohibited-substances
schedule and a permitted-formulary and the reason you have to know which kind you are reading.

One more detail, because it is funny and it is also the point: the **Soul Dew** is index 15 on the
permitted list. The item that makes a **Latios** formidable is explicitly allowed, while three
species with the identical base stat total are explicitly forbidden. Nobody derived that. Somebody
decided it.

## Eligibility is a chain of bare returns

The full entry check is five independent conditions in one function, and every one of them exits
the same way.

```
   AppendIfValid(species, heldItem, hp, lvlMode, monLevel, speciesArray, itemsArray, count)

     if (species == SPECIES_EGG || species == SPECIES_NONE)   return;   ← 1
     if (on gFrontierBannedSpecies)                           return;   ← 2
     if (lvlMode == FRONTIER_LVL_50
         && monLevel > FRONTIER_MAX_LEVEL_50)                 return;   ← 3
     if (this species already counted)                        return;   ← 4
     if (heldItem != 0 && this item already counted)           return;   ← 5

     speciesArray[*count] = species;
     itemsArray[*count]   = heldItem;
     (*count)++;
```

Five tests, five bare `return`s, **no return value and no reason code**. The caller learns only
that the count did not go up. `CheckPartyIneligibility` then reports, through
`gSpecialVar_0x8004`, a single boolean: there are not enough eligible Pokémon. Which of the five
rules excluded which member is nowhere in the data.

Everything about a conjunctive legal control is in that function. The conditions are independent —
they test a species list, a level, and two kinds of duplication, and none of them has anything to
do with any other. They are **conjunctive** — failing one is not partial compliance, it is
exclusion. And the failure is **silent**, which is the part a reader should hold onto: a
transaction that is not lawful does not come back with an explanation of which requirement it
missed. `m073`'s point about `FlagGet` returning FALSE for both a failed lookup and a genuine
clear bit is the same storage problem; here it is five problems sharing one exit.

## The rule lives at the door, not in the engine

This is the structural claim, and the code makes it unusually literally.

Nothing in `src/battle_main.c`, `src/battle_util.c` or `src/battle_script_commands.c` knows that
two **Alakazam** on one team are disallowed, or that two of them may not both hold a **Choice
Band**. The battle engine would run them. It would run six **Mew**, each holding **Leftovers**, at
level 100, in the Level 50 division. The duplicate-species check and the duplicate-item check are
in `frontier_util.c`, beside the banned list and the level cap, in the function that builds the
entry list — and the level cap is enforced the same way, by `return`, at the desk, rather than by
the battle engine refusing to load a level 73 **Slaking** into the battle structure.

So the control is placed where the thing **changes hands**, not where it acts. That is why a
controlled-drugs framework is made of prescribing eligibility, prescription particulars, supply
licensing, custody and records, and contains nothing at all about receptors: the receptor is not a
place where a quantity can be counted and attributed, and the counter at the door is.

## The register is three copies and a rule for when they disagree

```
   GetSetPokedexFlag(nationalDexNo, caseID), src/pokedex.c

   case FLAG_GET_SEEN:
       if (gSaveBlock2Ptr->pokedex.seen[index] & mask)
       {
           if (  (pokedex.seen[index] & mask) == (gSaveBlock1Ptr->seen1[index] & mask)
              && (pokedex.seen[index] & mask) == (gSaveBlock1Ptr->seen2[index] & mask))
                   retVal = 1;                       ← all three agree: the entry stands
           else
           {
                   pokedex.seen[index] &= ~mask;
                   seen1[index]        &= ~mask;
                   seen2[index]        &= ~mask;
                   retVal = 0;                       ← they disagree: ALL THREE are cleared
           }
       }

   case FLAG_SET_SEEN:
       pokedex.seen[index] |= mask;
       seen1[index]        |= mask;
       seen2[index]        |= mask;                  ← writing touches all three at once
```

Three independent copies of the same bit, in two different save blocks. A read is only honoured if
all three agree. A write goes to all three in one instruction. And a disagreement is not repaired
or flagged — the entry is voided and the function returns "no".

That is a running register with a reconciliation rule, and it behaves like one in the way that
matters: **the record, not the thing, is the authority.** You met the **Zigzagoon**. You stood in
the grass and it was there and the battle happened. The engine does not care; the three bytes
disagree, so the entry is gone, and the **Pokédex** will tell you to your face that you have never
seen one. `m084` uses this function to make the
point that no case clears a bit deliberately — the labelling outlives the thing labelled — and
that holds here too: `FLAG_SET_SEEN` and `FLAG_SET_CAUGHT` only ever OR the mask in. A register
you can add to and cannot amend, held in triplicate, voided on discrepancy. Every one of those
four properties is a controlled-drugs register property, and none of them is a property of any
Pokémon.

## Custody: what you get back is what the record says you held

```
   RestoreHeldItems(void), src/frontier_util.c

   for each of the selected party slots:
       item = GetMonData(&gSaveBlock1Ptr->playerParty[selectedPartyMons[i] - 1],
                         MON_DATA_HELD_ITEM, NULL);
       SetMonData(&gPlayerParty[i], MON_DATA_HELD_ITEM, &item);
                   ─────────────
       the item is restored from the STORED record, not from the thing that
       walked into the building.
```

The Battle Factory takes your Pokémon off you entirely and hands you rentals; the Pike has its own
`BATTLE_PIKE_FUNC_SAVE_HELD_ITEMS` and `BATTLE_PIKE_FUNC_RESET_HELD_ITEMS`; and at the end of a
challenge `FRONTIER_UTIL_FUNC_RESTORE_HELD_ITEMS` puts the held items back **by reading
`gSaveBlock1Ptr->playerParty`**, the record, and writing it onto the working party. Custody,
return, and a record that is the authority for what was in custody. The thing that comes back is
the thing the register says went in.

## Where the metaphor stops

The analogy above is about structures: lists, identifiers, entry checks and registers. This topic
also touches dependence and misuse, and the following is said plainly because no Pokémon mechanic
should be near it.

**Everything above describes a framework, not anyone's behaviour.** The mechanistic account of
tolerance, physical dependence and addiction — three different things that are routinely spoken of
as one — is `m076`'s subject, because it is pharmacology. Nothing in this pair describes how
diversion or misuse is carried out, deliberately, and nothing here is a basis for forming a view
about any individual.

**A controlled drugs register is a record about real people's medicines.** An entry names a
patient, a quantity and a time, and a discrepancy in it is investigated as a legal matter as well
as a clinical one. The right response to finding one is to report it immediately by the local
route. `m147` is the systems half of that: most discrepancies are process failures, and treating
every one as a suspicion both misses the common cause and suppresses the reporting that would find
the rare one.

**Needing one of these medicines is not a suspicious status.** A reasonable, sometimes long-term,
clinical need for a controlled drug is common. The framework exists to make supply accountable,
not to make the people who need it accountable, and the well-documented pattern of under-treatment
in places where the paperwork is heaviest is a direct consequence of confusing those two things.
The international obligation has two halves — prevent diversion, and ensure availability for
medical purposes — and it is the second half that is unmet in much of the world.

Nothing here indicates what anyone should take, start or stop, and none of it is legal advice.
Anyone worried about their own or someone else's use of a medicine should talk to a prescriber, a
pharmacist or a local service, who can do things a revision answer cannot.

## What a Gym Leader is listening for

* Mew, Celebi, Jirachi, Latios and Latias all total 600. Which three cannot enter, and what does
  that tell you about what the list was built from?
* Is eligibility derived or declared? Point at the line that settles it.
* Why does `SPECIES_DEOXYS` appearing once, with no forme, matter?
* `gFrontierBannedSpecies` and `BATTLE_FRONTIER_ITEM_*` run in opposite directions. Name both
  directions and say which kind of document each one is.
* `AppendIfValid` has five tests and one exit. Which three properties of a legal control does that
  demonstrate?
* Where is the duplicate-species rule implemented, and where is it *not*? Why does that location
  matter?
* `GetSetPokedexFlag` holds a bit three times. What happens when the three disagree, and what kind
  of record does that make it?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and all of them jurisdiction-specific except the first:

* **The three international drug control conventions** — the single convention on narcotic drugs,
  the convention on psychotropic substances, and the convention against illicit traffic in
  narcotic drugs and psychotropic substances — with the annual reports of the international
  narcotics control board and the recommendations of the world health organization's expert
  committee on drug dependence.
* **Your national controlled drugs legislation and its regulations**, which define the schedules,
  the prescription requirements, the records and the offences. The schedule numbers in it match no
  other country's.
* **Your national formulary's section on controlled drugs and dependence.**
* **Your institution's controlled drugs standard operating procedure and accountable officer
  arrangements**, for custody, the register, witnessing, destruction and how to report a
  discrepancy. Where it is stricter than national law, it governs.
* **Your professional regulator's guidance on prescribing controlled drugs.**
* **The world health organization's guidance on ensuring balance in national policies on
  controlled substances**, for the availability half of the obligation.

The Pokémon figures are a different matter and were read directly from the public decompilation of
the Game Boy Advance games rather than recalled: `gFrontierBannedSpecies` with its ten entries and
`0xFFFF` sentinel in `src/frontier_util.c`; the base stat rows for Mew, Mewtwo, Ho-Oh, Lugia,
Celebi, Kyogre, Groudon, Rayquaza, Jirachi, Deoxys, Latios, Latias, Regirock, Regice and Registeel
from `src/data/pokemon/species_info.h`, with every total recomputed here rather than recalled; the
species-specific hold effects, namely Light Ball for Pikachu, Metal Powder for a Ditto being hit
and Thick Club for Cubone or Marowak in `CalculateBaseDamage` in `src/pokemon.c`, and Lucky Punch
for Chansey and the Stick for Farfetch'd in the critical-hit calculation in
`src/battle_script_commands.c`; `AppendIfValid`'s five conditions in source order, and
`CheckPartyIneligibility` returning a single boolean through `gSpecialVar_0x8004`; the
`BATTLE_FRONTIER_ITEM_*` block in `include/constants/battle_frontier.h`, 62 entries, with the
indices quoted for King's Rock, Sitrus Berry, Oran Berry, Soul Dew, Choice Band, Leftovers and
Ganlon Berry; `FRONTIER_MAX_LEVEL_50`; `GetSetPokedexFlag`'s three-copy comparison and its
clear-all-three branch in `src/pokedex.c`, which is `m084`'s device; and `RestoreHeldItems`
reading `gSaveBlock1Ptr->playerParty` in `src/frontier_util.c`, with the Pike's save and reset
held-item function ids from `include/constants/battle_pike.h`. The claim that no file in the
battle engine enforces the duplicate-species rule is from grepping the battle sources for the
check and finding it only in `frontier_util.c`.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, not legal advice, and
it has had no clinical, pharmacist or legal review. **The only honest numbers in this pair are the
Pokémon ones.** Neither half names a drug, a schedule, a quantity, a validity period or a penalty,
deliberately: all of those are jurisdiction-specific, and an invented or misremembered one would
be a legal error as well as a clinical one. This pair describes a structure, not anyone's
behaviour, and contains nothing about how misuse or diversion is carried out. The mechanistic
material on tolerance, dependence and withdrawal is in `m076`. Nothing here indicates what anyone
should take, start or stop; anyone concerned about their own or another person's use of a medicine
should speak to a prescriber, a pharmacist or a local service.

## Where this stands, October 2026

The structural argument — a declared legal class against a derived pharmacological one, controls
placed where a quantity changes hands, a register that is the authority — is definitional and
stable, and the game mechanics quoted are fixed in released software, pinned to the Game Boy
Advance games, where the Battle Frontier bans ten species and permits sixty-two hold items. Later
generations changed both lists and the competitive formats that replaced them use different ones
again, which is itself the point. On the clinical side almost every specific is moving. **National
schedules change**, in both directions, sometimes on policy grounds with no new pharmacology.
**Prescription and record requirements** are being modernised, including electronic prescribing
and electronic registers for controlled drugs, which changes what the register physically is
without changing what it is for. **The international framework is under active debate**,
particularly on availability for medical use. Check your national legislation, your formulary and
your institution's current procedure.
