---
id: "m149"
slug: herbal-and-over-the-counter-products
style: pokemon
category: pharmacology
difficulty: intermediate
question: "Why is a claim that a product is natural not a pharmacological claim, and what makes the interaction problem with herbal and over-the-counter products harder than with prescribed medicines?"
tags: [herbal-medicines, self-medication, interactions, regulation, history-taking]
---

# The Lum Berry and the Full Heal are the same six bytes. There is no field in the table for where a thing came from.

```
   src/data/pokemon/item_effects.h

   const u8 gItemEffect_FullHeal[6] = {
       [3] = ITEM3_STATUS_ALL,
   };

   const u8 gItemEffect_LumBerry[6] = {
       [3] = ITEM3_STATUS_ALL,
   };
```

One is bought from a counter in a **Poké Mart** for 600. The other grows on a tree and is worth
20. They are the same array, the same length, the same byte set in the same position, and they sit
eleven lines apart in the same file. The structure has no field for provenance because provenance
is not a thing any routine needs to know.

And the table they are both in makes it formal: `gItemEffectTable` is indexed from `ITEM_POTION`
at one end and terminated by `[LAST_BERRY_INDEX - ITEM_POTION] = NULL` at the other. Manufactured
medicines and berries are entries in **one array**, consulted by one function. That is "natural is
not a pharmacological category", written as a data structure.

## The three matched pairs, and what the shop never mentions

The herbal items in the Advance games are not decoration. Each one is a near-exact clone of a
manufactured medicine, costs less, and carries extra bytes.

| | manufactured | bytes | herbal | bytes | price |
| --- | --- | --- | --- | --- | --- |
| restores 50 HP | **Super Potion** | `{[4] = ITEM4_HEAL_HP, [6] = 50}` | **Energy Powder** | the same two, **plus** `[5] = ITEM5_FRIENDSHIP_ALL` and `[7..9] = -5, -5, -10` | 700 against 500 |
| restores 200 HP | **Hyper Potion** | `{[4] = ITEM4_HEAL_HP, [6] = 200}` | **Energy Root** | the same two, **plus** the friendship flag and `[7..9] = -10, -10, -15` | 1200 against 800 |
| clears all status | **Full Heal** | `{[3] = ITEM3_STATUS_ALL}` | **Heal Powder** | the same one, **plus** the friendship flag and `[6..8] = -5, -5, -10` | 600 against 450 |

Three pairs. In every pair the intended effect is **byte-for-byte identical**, the herbal one is
cheaper, and the herbal one carries an effect the manufactured one does not. A fourth entry sits
in the same group with the same friendship bytes; it is in the family `m069` puts out of bounds
for this corpus, so it is named and not mapped.

Now read what the player is told. `src/data/text/item_descriptions.h`:

```
   sSuperPotionDesc   "Restores the HP of a POKéMON by 50 points."
   sEnergyPowderDesc  "A bitter powder that restores HP by 50 points."

   sHyperPotionDesc   "Restores the HP of a POKéMON by 200 points."
   sEnergyRootDesc    "A bitter root that restores HP by 200 points."

   sFullHealDesc      "Heals all the status problems of one POKéMON."
   sHealPowderDesc    "A bitter powder that heals all status problems."
```

The two descriptions in each pair say the same thing. The only difference is the word *bitter*,
which is a flavour note. **The friendship cost appears nowhere in any text the player can read.**
It is in the **Energy Powder**'s last three bytes, it fires through the friendship flag, and the
label is silent about it.

Put the three side by side once more, because the pattern is the whole argument. The **Energy
Powder** is a **Super Potion** for 200 less with three hidden bytes. The **Energy Root** is a
**Hyper Potion** for 400 less with three worse ones. The **Heal Powder** is a **Full Heal** for
150 less. Three purchases, three savings, three undeclared costs, and the costs scale with the
benefit: the **Energy Root**, which restores four times what the **Energy Powder** does, also
takes twice as much friendship. Whoever wrote that table was modelling a real relationship, and it
is the one nobody puts on a box.

That is the over-the-counter labelling problem with nothing left out: a product that works, costs
less than the licensed equivalent, is sold openly in the same shops, and has an effect in the data
that is not in the information supplied with it. The player who notices is the player who read the
source. Nobody playing the game notices, because the thing it costs you is slow, cumulative and
displayed nowhere.

## Six pairs, and one combination product on each side

The effect table pairs off further, and the pairing is exact.

| what it clears | manufactured | berry | the bytes, both of them |
| --- | --- | --- | --- |
| poison | **Antidote** | **Pecha Berry** | `{[3] = ITEM3_POISON}` |
| burn | **Burn Heal** | **Rawst Berry** | `{[3] = ITEM3_BURN}` |
| freeze | **Ice Heal** | **Aspear Berry** | `{[3] = ITEM3_FREEZE}` |
| sleep | **Awakening** | **Chesto Berry** | `{[3] = ITEM3_SLEEP}` |
| paralysis | **Paralyze Heal** | **Cheri Berry** | `{[3] = ITEM3_PARALYSIS}` |
| everything above | **Full Heal** | **Lum Berry** | `{[3] = ITEM3_STATUS_ALL}` |

Twelve items, six distinct effects, and in every row the two entries are the **same single byte in
the same position**. `m003` establishes the **Antidote** device for nursing — it cures poison and
nothing else — and this is that device with the column doubled: for each narrow product there is a
berry that is not merely similar but identical in the data, and for each column there is one
wide-spectrum entry, **Full Heal** on the manufactured side and the **Lum Berry** on the other.

That last row is the combination product, and it is where the duplication risk lives. Someone
holding a **Lum Berry** and carrying **Pecha Berries** is carrying the same effect twice under two
names, exactly as a person taking a prescribed analgesic and a branded cold remedy may be taking
one molecule twice. The game will happily let you use both. `m014`'s four-slots argument is the
other half: the second one occupies something.

And the **Persim Berry** is the entry worth noticing, because it breaks the symmetry. It is
`{[3] = ITEM3_CONFUSION}`, and `ITEM3_STATUS_ALL` is defined as the OR of all six conditions
including confusion, so the **Lum Berry** and the **Full Heal** both cover it. But there is **no
manufactured single-condition item for confusion** anywhere in the table. For that one effect the
narrow option exists only as a berry, and anyone who wants it without the rest has to reach for
the thing off the tree. That is the situation where the unlicensed product is not a worse
substitute for a licensed one but the only narrow option on the shelf, and it is a real and
awkward category rather than a rhetorical one.

## And a berry that declares its cost

The contrast matters, because it stops this being a story about berries being sneaky.

```
   src/data/items.h
   [ITEM_FIGY_BERRY] = {
       .name            = _("FIGY BERRY"),
       .price           = 20,
       .holdEffect      = HOLD_EFFECT_CONFUSE_SPICY,
       .holdEffectParam = 8,
       .description     = sFigyBerryDesc,
   }

   sFigyBerryDesc  "A hold item that restores HP but may confuse."
```

The Figy Berry restores maxHP/8 and may confuse — and the description **says so**. Whether it
confuses depends on the holder's own flavour preference, which is derived from the same
`personality` word `m077` works through: the same berry, the same effect bytes, and an adverse
effect that happens to some individuals and not others, declared on the label.

So the games contain both kinds of product: one whose extra effect is labelled and one whose extra
effect is not, with no pharmacological difference between those two situations at all. The
difference is entirely in the text file. That is the argument that what separates these product
classes is **regulatory, not pharmacological**, and it is sitting in two adjacent data files.

## Twelve berries with no manufactured counterpart at all

The pairing above is tidy because those berries have twins. Twelve do not, and they are the
interesting case.

```
   src/data/items.h, the hold-effect berries with no shop equivalent

   five keyed to a flavour, all with holdEffectParam = 8
   ─────────────────────────────────────────────────────────────────────
   Figy Berry      HOLD_EFFECT_CONFUSE_SPICY
   Wiki Berry      HOLD_EFFECT_CONFUSE_DRY
   Mago Berry      HOLD_EFFECT_CONFUSE_SWEET
   Aguav Berry     HOLD_EFFECT_CONFUSE_BITTER
   Iapapa Berry    HOLD_EFFECT_CONFUSE_SOUR

   seven that fire when the bar is low, all with holdEffectParam = 4
   ─────────────────────────────────────────────────────────────────────
   Liechi Berry    HOLD_EFFECT_ATTACK_UP
   Ganlon Berry    HOLD_EFFECT_DEFENSE_UP
   Salac Berry     HOLD_EFFECT_SPEED_UP
   Petaya Berry    HOLD_EFFECT_SP_ATTACK_UP
   Apicot Berry    HOLD_EFFECT_SP_DEFENSE_UP
   Lansat Berry    HOLD_EFFECT_CRITICAL_UP
   Starf Berry     HOLD_EFFECT_RANDOM_STAT_UP
```

No **Potion** raises Attack. No **Full Heal** sharpens a critical-hit rate. There is nothing on
any shelf in Hoenn that does what a **Salac Berry** does, and the seven of them are the only items
in the game whose effect is a stat change triggered by a condition. `m044` already uses the
Berries as the withheld-until-a-condition device and this extends it one step: these are products
whose *effect class* has no licensed counterpart at all.

That is the honest version of the supplement argument, and it cuts both ways. Some of what people
buy outside the prescription system does something the licensed range does not offer, which is a
real reason to use it and a real reason the content and the dose matter more rather than less. And
the **Starf Berry** is the one to end on: `HOLD_EFFECT_RANDOM_STAT_UP` raises **a stat chosen at
random**. An effect that is genuinely real, genuinely useful, and not the same effect twice
running — which is the hardest kind of product to evaluate and the easiest kind to believe in.

## The Enigma Berry: a licensed product whose contents are not in the cartridge

This is the best single mechanic in the games for an unregulated supplement, and it is better than
anything a writer could invent.

```
   src/data/items.h
   [ITEM_ENIGMA_BERRY] = {
       .name         = _("ENIGMA BERRY"),
       .price        = 20,
       .description  = sEnigmaBerryDesc,
       .pocket       = POCKET_BERRIES,
       .battleUsage  = ITEM_B_USE_MEDICINE,
   }
                       ← and that is the whole entry. There is NO .holdEffect
                         and NO .holdEffectParam. The fields are absent.

   sEnigmaBerryDesc  "{POKEBLOCK} ingredient. Plant in loamy soil to grow a mystery."

   so every site that needs to know what it does has to branch:

   src/battle_util.c, four separate places, including inside
   CheckMoveLimitations itself:

       if (gBattleMons[battler].item == ITEM_ENIGMA_BERRY)
           holdEffect = gEnigmaBerries[battler].holdEffect;
       else
           holdEffect = GetItemHoldEffect(gBattleMons[battler].item);
```

An item that is in the shop list, in the berry pocket, usable in battle, priced at 20 — and whose
pharmacology **is not in the game's data at all**. It lives in `gEnigmaBerries[battler]`, a
per-battler structure populated from outside the cartridge, and the battle engine cannot evaluate
it without first asking somewhere else what this particular one happens to be.

Every property of a poorly regulated product is in that. It is freely available. It has a label
that says nothing about what it does. Its actual content is per-instance rather than per-product —
two of them need not be the same thing. And the system has to special-case it in four places,
because the general mechanism for "what does this item do" does not work on it.

And then the detail that finishes the argument: a berry occupies the single held-item slot. That
is `m014`'s four-moves-and-one-item budget and `m038`'s point that nothing ever asks whether the
item is still needed. Holding an Enigma Berry means not holding **Leftovers**, not holding a
**Choice Band**, not holding a **Lum Berry**. The product you took displaced the product you knew.

## The same name, twice, with different contents

```
   Generation III, from src/data/items.h and item_effects.h
       Oran Berry     holdEffect = HOLD_EFFECT_RESTORE_HP,  param = 10   (a FLAT 10)
       Sitrus Berry   holdEffect = HOLD_EFFECT_RESTORE_HP,  param = 30   (a FLAT 30)
       and the descriptions agree: "restores 10 HP", "restores 30 HP"

   Generation IV onward
       Sitrus Berry   restores a FRACTION of maximum HP
```

One name, two products. A **Sitrus Berry** in the Advance games is a flat 30 and a **Sitrus
Berry** later is a proportion, and `m006`'s **Super Fang** argument is exactly why those are not
the same item. Put the two extremes of the Pokédex against it.

```
   a FLAT 30 against a PROPORTION of maximum HP, on two real base-HP figures

   Blissey   baseHP 255   ──►  the flat 30 is a sliver of the bar
   Shedinja  baseHP   1   ──►  the flat 30 is the whole bar, several times over
   Oran Berry's flat 10 does the same thing one third as loudly.

   Same printed name. Same pocket. Same price of 20. Two different medicines,
   and which one you are holding depends on which cartridge you are holding.
```

A **Blissey** barely notices the **Sitrus Berry** and a **Shedinja** is restored outright by it,
and that gap is produced entirely by the choice between a flat figure and a proportion — the
choice that a later generation made differently while keeping the name. `m041` makes the same
point about reading a bar instead of a quantity.

So the label, the name, the price and the pocket are all stable, and the thing in the packet is
not. That is batch-to-batch and product-to-product variability in content, and it is the reason an
interaction demonstrated with one preparation does not transfer its size to another. `m044` is the
formulation half of this: the same drug by a different route or in a different preparation is a
different exposure, and the name on the front does not record it.

One more, from the same table, because it shows the data can carry a benefit as well as a cost:
the effort-value berries — **Pomeg Berry**, **Kelpsy Berry**, **Qualot Berry**, **Hondew Berry**,
**Grepa Berry**, **Tamato Berry** — all share a macro that writes `[7..9] = 10, 5, 2`, a
friendship *gain*, while lowering a stat's effort value. A product with a documented benefit and a
documented cost, both in the bytes, and the player choosing which one they came for. That is a
fair label, and it is in the same file as the ones that are not.

## Where the metaphor stops

Everything above is about data structures and labels. Four things about these products are about
people, and they are said here without analogy.

**People take them for reasons that make sense.** Relief that conventional care did not provide, a
preference for something that feels less interventional, cost, availability, and family or
cultural practice. And the reasonable inference that something sold freely on a shelf must be low
risk. None of that is ignorance, and a consultation whose purpose is to win that argument stops
collecting the information it needed.

**The belief that natural means safe is a labelling artefact.** When a product carries no stated
dose, no stated active content and no warning, the packaging is making an implicit claim.
Correcting the belief is worth doing. Blaming someone for holding it is not, and the Energy Powder
table above is a fair picture of why they hold it: the thing genuinely works and the cost
genuinely is not written down.

**Non-disclosure is usually a question nobody asked.** A large share of people using these
products have not mentioned it to anyone in their clinical team, and the commonest reason given is
that they were not asked and did not think it counted as a medicine. That is a fixable system
problem in the sense `m147` means it, and the fix is to ask by category — prescribed, bought,
borrowed, herbal, vitamins, supplements, topicals, teas — rather than to ask about "medicines".

**Regulation of these products is genuinely uneven, and the unevenness falls unevenly.** Where
traditional and herbal preparations are a major part of how care is actually delivered, the
quality assurance available is often weakest, and adulteration and contamination of unregulated
preparations are documented problems, including undeclared pharmaceutical ingredients and heavy
metals. That is a statement about supply chains and regulatory capacity, not about traditional
medicine, and the remedy is regulation and quality assurance rather than disapproval.

Nothing in this pair indicates what anyone should take, start or stop, including any herbal or
over-the-counter product. A question about a specific combination belongs with a pharmacist or a
prescriber, who can open the formulary.

## What a Gym Leader is listening for

* Write out the **Full Heal**'s effect bytes and the **Lum Berry**'s. What is the difference, and
  what does that tell you about the table?
* Give the three matched manufactured-and-herbal pairs, the effect they share, and the bytes only
  one of them carries.
* Read `sSuperPotionDesc` against `sEnergyPowderDesc`. What is the only difference, and what is
  missing from both?
* The **Figy Berry** declares its adverse effect and the **Energy Root** does not. Is that a
  pharmacological difference? Say what kind of difference it is.
* What two fields are absent from the **Enigma Berry**'s entry, and where does the engine go
  instead?
* Why is a flat 30 and a proportion of maximum HP not the same product, and which species makes
  the difference most obvious?
* What does holding any berry cost, and which two answers already in this specialty make that
  point?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-pharmacology.md`](../../../for-agents/SOURCES-pharmacology.md).
Specific to this answer, and to its technical twin:

* **Your national formulary's interactions section and its guidance on herbal medicines.** This is
  the authority for any specific interaction and the only place one should be looked up. Nothing
  in either half of this pair substitutes for it.
* **Your national medicines regulator's registration scheme for herbal and traditional products**,
  for what the authorisation on a given pack actually certifies where you are — which differs
  enormously between a fully licensed product, a traditional-use registration and an unregulated
  food supplement.
* **The approved product information for any over-the-counter pack in question**, for its full
  composition. That document settles the duplication question, and reading it is the whole
  intervention.
* **The world health organization's strategy and guidance on traditional and complementary
  medicine**, for the regulatory landscape and the quality-assurance material.
* **A current clinical pharmacology textbook chapter on drug interactions**, for the mechanisms,
  and `m009` for how this specialty classifies them.
* **The primary literature**, for any figure about how often these products are used, how often
  they are disclosed, or the size of a specific interaction. Neither half of this pair states one.

The Pokémon figures are a different matter and were read directly from the public decompilation of
the Game Boy Advance games rather than recalled: `gItemEffect_FullHeal`, `gItemEffect_LumBerry`,
`gItemEffect_Potion`, `gItemEffect_SuperPotion`, `gItemEffect_HyperPotion`,
`gItemEffect_EnergyPowder`, `gItemEffect_EnergyRoot`, `gItemEffect_HealPowder`,
`gItemEffect_OranBerry` and `gItemEffect_SitrusBerry` in `src/data/pokemon/item_effects.h`, with
their byte indices and values exactly as quoted, and the `ITEM5_FRIENDSHIP_ALL` flag from
`include/constants/item_effects.h`; the `gItemEffectTable` bounds from `ITEM_POTION` to
`[LAST_BERRY_INDEX - ITEM_POTION] = NULL`; the prices and hold-effect fields for Potion, Super
Potion, Hyper Potion, Max Potion, Full Heal, Energy Powder, Energy Root, Heal Powder, Oran Berry,
Sitrus Berry, Lum Berry, Figy Berry and Enigma Berry from `src/data/items.h`, including the Enigma
Berry entry's **absent** `holdEffect` and `holdEffectParam`; the description strings quoted
verbatim from `src/data/text/item_descriptions.h`; the four `ITEM_ENIGMA_BERRY` branches reading
`gEnigmaBerries[battler]` in `src/battle_util.c`, one of them inside `CheckMoveLimitations`; and
the `EV_BERRY_FRIENDSHIP_CHANGE` macro writing `10, 5, 2` for the six effort-value berries; the
six matched status pairs, Antidote with Pecha Berry, Burn Heal with Rawst Berry, Ice Heal with
Aspear Berry, Awakening with Chesto Berry, Paralyze Heal with Cheri Berry and Full Heal with Lum
Berry, each pair byte-identical in `item_effects.h`, with `ITEM3_STATUS_ALL` defined in
`include/constants/item_effects.h` as the OR of all six conditions including confusion, and the
Persim Berry the only single-condition entry with no manufactured counterpart; the twelve
hold-effect berries with no shop equivalent, five `HOLD_EFFECT_CONFUSE_*` at `holdEffectParam` 8
and seven stat-raising ones at 4, from `src/data/items.h`; and Blissey's base HP of 255 and
Shedinja's of 1 from `src/data/pokemon/species_info.h`. The Generation IV change to the Sitrus
Berry is a cross-generation fact and is **not** from this decompilation; it is stated as a
generation difference and should be checked against that generation's own data. Shedinja's single
maximum HP and the flat-against-proportional argument are `m006`'s.

## Scope and safety

This is revision material for a pharmacy undergraduate, a prescriber revising, or anyone already
training in the field. It is not a clinical reference, not a decision aid, and has had no clinical
or pharmacist review. **The only honest numbers in this pair are the Pokémon ones.** Neither half
gives doses, interaction magnitudes, maximum durations or a list of products to avoid: the size of
a given interaction depends on the preparation, and the authority is the formulary and the product
information. The two interaction examples in the technical half are textbook illustrations of
induction and inhibition, not a complete list and not an instruction. Nothing here indicates
whether anyone should take, start or stop any medicine, supplement or herbal product, including
the reader's own.

## Where this stands, October 2026

The mechanism — provenance is not a pharmacological property, and the real differences between
these product classes are regulatory and behavioural — does not date, and the game mechanics
quoted are fixed in released software, pinned to the Game Boy Advance games, where the Sitrus
Berry is a flat 30 and the herbal items carry explicit friendship deltas. The regulatory picture
dates quickly. **How herbal and traditional products are regulated** differs by country and is
being revised in several, with registration schemes introduced, tightened and in places withdrawn.
**Which medicines are available over the counter** changes in both directions. **Supplement
regulation** is the weakest-controlled part of the market in most jurisdictions and is an active
policy question. And the interaction evidence base for individual preparations is still being
built, so an absence of documented interactions for a product is not evidence that there are none.
Check your formulary and your national regulator.
