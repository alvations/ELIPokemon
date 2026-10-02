---
id: "m055"
slug: leg-ulcers-and-vascular-assessment
style: pokemon
category: dermatology
difficulty: intermediate
question: "Why does the vascular assessment come before the dressing in a chronic leg ulcer, and what makes compression the treatment rather than the wound covering?"
tags: [leg-ulcer, compression, ankle-brachial-index, wound-bed, offloading]
---

# Surf is doubled against Charizard and gives Lapras a quarter of its HP back

**Surf** is one move with one base power. Throw it at a **Charizard** — Fire and Flying — and it
is super effective and lands for double. Throw the identical move at a **Lapras** and the code
does not compute damage at all: Lapras has **Water Absorb**, the absorbing branch fires instead,
and the routine sets a heal of **a quarter of maximum HP**. Same move, same user, same power. The
sign of the outcome flipped.

And here is the part that makes it the right analogy rather than a cute one: **you could not see
it coming**. An **Ability** is not drawn on the sprite. It is not on the summary screen for an
opponent. The code records an opponent's ability by calling `RecordAbilityBattle` **at the moment
the ability fires** — which is to say the game writes it down immediately after it is too late to
have used the information.

```
   ONE MOVE, OPPOSITE SIGNS, AND NOTHING ON THE SPRITE TO WARN YOU
   ==================================================================================

   THE MOVE         THE TARGET                 WHAT ACTUALLY HAPPENS
   ==============   ========================   ==================================
   a Water move     Charizard (Fire/Flying)    super effective, doubled
   a Water move     Lapras (Water Absorb)      HEALS a quarter of maximum HP
   a Water move     Quagsire (Water Absorb     heals -- and Quagsire's OTHER
                    as its second ability)     listed ability is Damp, so two
                                               Quagsire behave differently
   ==============   ========================   ==================================
   an Electric      Jolteon or Lanturn         heals a quarter of maximum HP
   move             (Volt Absorb)
   a Fire move      Vulpix, Ninetales,         no damage; raises the power of
                    Flareon (Flash Fire)       its own Fire moves instead
   a Ground move    Gengar (Levitate)          does not affect it at all
   a Water move     Paras or Parasect with     heals -- while a Fire move on the
                    Dry Skin, from Gen IV      same Pokemon lands at 1.25x
   ==================================================================================
   Dry Skin's in-game description is four words: "Heat hurts, Water restores."
   One ability. Two signs. Keyed entirely to what is being applied.
   ==================================================================================
```

Compression is that move. In venous ulceration it is the treatment — the only intervention that
opposes the mechanism. On a leg whose arterial inflow is already marginal, raising external
pressure reduces perfusion further and can convert a painful ulcer into tissue loss. Same bandage.
Opposite sign. Not visible on the wound.

That is the entire argument for the order of operations. The vascular assessment comes first
because it is the step that decides whether the definitive treatment is therapy or injury.

## Venous and arterial, side by side

```
   VENOUS AND ARTERIAL
   ==================================================================================

   FEATURE             VENOUS                       ARTERIAL
   =================   ==========================   ===========================
   mechanism           valve incompetence and       reduced arterial inflow;
                       calf pump failure, giving    perfusion pressure below
                       ambulatory venous            what the tissue needs
                       hypertension
   =================   ==========================   ===========================
   site                medial gaiter area,          toes, heel, lateral malleolus,
                       above the malleolus          over pressure points, distal
   =================   ==========================   ===========================
   edge and base       shallow, irregular edge,     deep, sharply demarcated,
                       granulating, exudative       "punched out", pale or
                                                    necrotic base, dry
   =================   ==========================   ===========================
   surrounding skin    oedema, haemosiderin         thin, shiny, hairless, cool,
                       staining, varicose eczema,   pallor on elevation, delayed
                       lipodermatosclerosis,        capillary refill
                       atrophie blanche
   =================   ==========================   ===========================
   pain                aching, worse on standing,   severe, worse on ELEVATION
                       better on elevation          and at night, better hanging
                                                    the leg down
   =================   ==========================   ===========================
   pulses              usually present              reduced or absent
   ==================================================================================
   The pain history separates them more often than the wound does. Relief on
   elevation points one way; relief on dependency points the other. Ask it first.
   Mixed disease is common, and for the purpose of deciding about compression it
   behaves as the arterial one.
```

## Why the index exists, and why you look it up rather than find out the hard way

The honest way to learn an opponent's **Ability** is not to trigger it. It is to look it up before
you commit the turn — the **Pokédex**, the species table, the thing somebody else already wrote
down.

The **ankle-brachial pressure index** is that lookup. It is measured with a Doppler probe and a
sphygmomanometer, as the ratio of the highest ankle systolic pressure to the highest brachial
systolic pressure. Full compression is generally considered safe at an index of about 0.8 or
above; below that, compression is modified or withheld pending specialist assessment, and a
markedly low index means severe arterial disease needing urgent vascular referral. **The exact
thresholds, what happens at each, and who is permitted to apply compression are set by local
policy, and that policy is the authority rather than this answer.** [country-dependent]

Two caveats are routinely examined on. The index is **falsely elevated** where vessels are
calcified and incompressible — most importantly in diabetes and chronic kidney disease — so a
normal index does not exclude significant arterial disease in those groups, and a toe-brachial
index or other test may be needed. And the measurement is operator-dependent, so a number obtained
without training is not a reassurance — a **Bottle Cap** and **Hyper Training** will max out an
**Individual Value** that was never visible, and neither is any use to a trainer who has not
learned what IVs do. The instrument is the easy part.

```
   THE ORDER OF OPERATIONS, AND WHY IT IS THIS ORDER
   ==================================================================================

   1. IS THIS LIMB ACUTELY THREATENED?
      sudden pain, pallor, pulselessness, paraesthesia, paralysis, a cold leg,
      or spreading infection with systemic illness
      -> urgent referral. Nothing below happens first.
                 |
                 v
   2. VASCULAR ASSESSMENT
      history, pulses, ankle-brachial pressure index
      -> the step that decides whether step 4 is treatment or injury
                 |
                 v
   3. CLASSIFY THE CAUSE
      venous / arterial / mixed / neuropathic / pressure / inflammatory /
      malignant / other -- and reconsider if it does not fit
                 |
                 v
   4. TREAT THE CAUSE
      venous: compression.  arterial: revascularisation assessment.
      neuropathic: offloading.  pressure: redistribution.
      inflammatory: immunosuppression, and do NOT debride a pathergic ulcer.
                 |
                 v
   5. PREPARE AND DRESS THE WOUND BED
      debridement where appropriate, moisture balance, exudate management,
      edge and peri-wound skin care
                 |
                 v
   6. PREVENT RECURRENCE
      long-term hosiery, superficial venous intervention where indicated,
      footwear, skin care, exercise, and the follow-up to make it happen
   ==================================================================================
   Steps 5 and 6 are where most of the clinical time and most of the product
   spend go. Step 2 is where the outcome is decided.
```

## Leftovers against a Sandstorm is the cleanest arithmetic in this answer

**Leftovers** restores exactly a sixteenth of the holder's maximum **HP** at the end of every
turn. **Tyranitar**'s **Sand Stream** puts up a **Sandstorm** that costs exactly a sixteenth of
maximum HP at the end of every turn to anything that is not Rock, Ground or Steel. Both numbers
are in the code and both are `maxHP / 16`.

Put a Leftovers on a Pokémon standing in a Sandstorm and the bar does not move. Not a little — not
at all. Six turns later you are exactly where you started, you have spent your item slot, and the
storm is still permanent because an ability set it and the countdown code skips ability-set
weather.

That is a dressing on a venous ulcer. It is doing real work at the interface, and the net is zero
until something opposes the venous hypertension. Compression raises interstitial pressure, reduces
the transmural gradient, improves venous return and assists the calf muscle pump. It is the thing
that turns the weather off. And the finding that reorganises everybody's priorities is that there
is no strong evidence any one dressing type heals venous ulcers better than another **under
compression** — the bandage is the therapy and the dressing is the interface.

## What the wound bed work genuinely is

Wound bed preparation is usually taught as four elements — tissue, infection and inflammation,
moisture balance, and the wound edge — and the framework is worth knowing under whichever name
your service uses. The elements are real: devitalised tissue impedes healing and is debrided where
that is safe and appropriate; exudate is managed without maceration or desiccation; and the
peri-wound skin needs protecting, because the eczema and excoriation around a leg ulcer is a large
part of the symptom burden.

Infection needs the same discipline the sibling answer in this set applies to colonisation in
eczema. Every chronic wound is colonised, colonisation is not infection, routine swabbing of a
wound that is not clinically infected does not help, and a positive swab from such a wound invites
antibiotics nobody needed. What matters is clinical change — increasing pain, spreading erythema,
cellulitis, malodour, rapid deterioration, systemic features. Systemic antibiotics are for
spreading infection; topical antibiotics on chronic wounds are avoided on resistance and
sensitisation grounds in most guidance. Agents and durations are **country-dependent**.

## Offloading is Heavy-Duty Boots, and the diabetic foot is where pain stops helping

**Heavy-Duty Boots** have a six-word job: *protects from the effects of traps set on the field*.
With them, **Spikes** are not an event. Without them, every single entry costs, and it costs again
on the next entry, and **Rapid Spin** clearing the hazard afterwards is a different and later kind
of fix from never taking it.

In diabetic neuropathy the protective sensation is gone, so the ulcer is painless, the person
keeps walking on it, and the mechanical cause is reapplied with every step. Offloading is the
structural twin of compression — it removes the cause rather than dressing the effect. The
diabetic foot is managed urgently by a multidisciplinary foot service, with assessment for
osteomyelitis and for ischaemia, on referral timescales that are **country-dependent** and short.

## Illusion, and the wound that is not what it is presenting as

**Zoroark**'s **Illusion** makes it enter the field looking like another Pokémon from its
trainer's party. Type effectiveness is even displayed against the Pokémon it is pretending to be.
The implementation ends the disguise on one condition: the battler is actually damaged. Looking
harder never breaks an Illusion. Only a real interaction does.

A non-healing wound may be a malignancy — a basal cell or squamous cell carcinoma, or a melanoma —
or a squamous cell carcinoma may arise in a long-standing ulcer. An atypical appearance, a rolled
or everted edge, exuberant granulation, or simple failure to progress despite correct treatment of
the cause, is a reason to biopsy rather than to inspect again.

And the inversion worth memorising: **pyoderma gangrenosum** shows pathergy, so surgical trauma
makes it worse and debriding it is actively harmful. A rapidly enlarging ulcer with an undermined
violaceous border, often alongside inflammatory bowel disease or inflammatory arthritis, is
treated with immunosuppression. It is the second ability on the species table — the same move, the
opposite sign, and the only defence is having looked first.

## Where the metaphor stops

This section carries no Pokémon, because the mechanism is over and the consequences are not
something to be cute about.

Leg ulcer pain is substantial, continuous, and consistently under-recognised. It is worst at
dressing changes, which happen on a schedule set by the service, and people describe dreading them
for days. Asking about pain at dressing change specifically, and planning analgesia around it, is
part of the treatment and not a courtesy.

Chronic ulceration is isolating in ways that never reach a wound chart. Exudate and odour stop
people leaving the house, and they know it. Bandages do not fit shoes. Many people with venous
disease cannot easily wash, cannot reach their own legs, and have had the condition for years with
a realistic expectation that it will come back. Compression hosiery is uncomfortable, is hard to
put on with arthritic hands, and is the single thing most likely to be abandoned — which makes the
conversation about how it will actually be managed at home more important than the choice of
product.

This condition disproportionately affects older people living alone, which means the practical
details — who applies this, how often, how they get to the clinic — are clinical facts rather than
social background. A perfect plan nobody can carry out heals nothing.

Without softening: nothing in this answer is for any reader's own use, and no threshold or
treatment in it should be applied to anyone's leg. Compression is applied by trained staff after
an assessment, and the reason that is said plainly here is that the harm from getting it wrong is
real. Anyone with a wound that is not healing, a painful or cold leg, or redness spreading from a
wound needs to be seen in person. A suddenly painful, pale, cold, numb or weak leg is an emergency
— call your local emergency number.

## What a Gym Leader is listening for

Why compression heals a venous ulcer when a dressing does not — the **Leftovers** against the
**Sandstorm**, both at a sixteenth. What the ankle-brachial pressure index is a ratio of, and in
whom it is falsely reassuring. Which single question in the pain history separates venous from
arterial most reliably. Why a positive wound swab is usually not an indication to treat. What
would make you biopsy a leg ulcer. Why debridement is contraindicated in pyoderma gangrenosum. And
what offloading and compression have in common conceptually.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in the dermatology sources file in the
writers' directory for this domain, and they are the authority for everything procedural or
quantitative here. Specific to this answer:

* For the ankle-brachial pressure index — how it is measured, the threshold values, what is done
  at each, and who is competent to apply compression: your institution's leg ulcer and compression
  policy, and the leg ulcer or chronic wound guideline issued by the national body that sets
  guidance where you practise. The thresholds differ between policies.
* For compression systems, hosiery classes and the strength of evidence behind each: the wound
  care formulary or appliance list in use where you practise, and your national guideline. Hosiery
  class numbers are not interchangeable between countries.
* For the diabetic foot — risk stratification, referral timescales and the composition of the
  multidisciplinary foot service: your national diabetic foot guideline.
* For antimicrobial choice and duration in wound infection: your national antimicrobial guidance
  and your local microbiology policy.
* For pyoderma gangrenosum and the inflammatory ulcers: a current standard textbook of dermatology
  and the specialist guidance of your national dermatology body.
* For when to biopsy a non-healing wound: your region's suspected-skin-cancer referral guideline.

The Pokémon claims were checked separately against source. Water Absorb, Volt Absorb and Dry Skin
each setting a heal of a quarter of maximum HP through the same absorbing routine; Lapras and
Vaporeon carrying Water Absorb, Quagsire carrying it as a second ability behind Damp, Jolteon and
Lanturn carrying Volt Absorb, Vulpix, Ninetales and Flareon carrying Flash Fire, Gengar carrying
Levitate and Levitate making Ground moves not affect the target; Charizard being Fire and Flying
with Blaze; Leftovers restoring a sixteenth of maximum HP at end of turn; Sandstorm costing a
sixteenth while sparing Rock, Ground and Steel types; Tyranitar's Sand Stream being its only
ability and ability-set weather being skipped by the countdown code; and the game recording an
opponent's ability only at the moment that ability fires are all from the pret decompilation of
Pokémon Emerald. Dry Skin's description and its 1.25 multiplier against Fire, Heavy-Duty Boots and
its description, and Illusion ending when the battler is damaged are from the
pokeemerald-expansion project, because those are fourth-generation, fifth-generation and
eighth-generation content and the pret decompilations stop at the third. The Bottle Cap and Hyper
Training are seventh-generation features and are named here from general knowledge of the series
rather than from a file that was opened.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No threshold, index value, dressing, compression system or referral timescale named here is an
instruction, and none of it addresses any reader's own treatment.** The index value quoted appears
only to explain why a threshold exists at all; the operative figure is the one in your local
policy, and applying compression is a trained activity governed by that policy. Compression
applied to a leg with inadequate arterial inflow can cause tissue loss, which is why this answer
is ordered as it is.

Anyone with a wound that is not healing, a leg that is painful, cold or discoloured, or redness
spreading from a wound needs to be assessed in person. A suddenly painful, pale, cold, numb or
weak leg is an emergency — call your local emergency number.

Local guidance and the policy where you practise are the authority on all of this, and they differ
by country and by institution.

## Where this stands, October 2026

The physiology and the order of operations here are settled, and they are the part worth
memorising. What moves is the detail: compression systems and hosiery classifications differ
between countries and are revised, the evidence comparing two-layer and four-layer systems and
compression wraps has continued to accumulate, and the position on early superficial venous
intervention to reduce recurrence has strengthened rather than stayed still. Adjunctive therapies
for hard-to-heal wounds — skin substitutes, topical oxygen, negative pressure in selected wounds —
remain an area where the evidence is uneven and the funding decisions are national. The index
itself, and its falsely elevated values in calcified vessels, are not in dispute — more stable, as
it happens, than **Dry Skin**, which did not exist before the fourth generation. Current as of
October 2026.
