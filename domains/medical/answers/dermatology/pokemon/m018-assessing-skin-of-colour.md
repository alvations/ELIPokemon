---
id: "m018"
slug: assessing-skin-of-colour
style: pokemon
category: dermatology
difficulty: core
question: "Why do the standard descriptions of erythema, cyanosis and jaundice fail in darker skin, and what changes?"
tags: [skin-of-colour, erythema, pigmentation, examination, competence]
---

# Search the Pokédex for a red Gyarados and it returns nothing

The Gen III **Pokédex** will list the whole national dex by body colour. It is a real search over
a real field, and the field has ten values. **Gyarados** is stored as Blue. The **Gyarados**
waiting at the **Lake of Rage** is unmistakably red — its palette swaps four shades of blue for
four of red, and anybody who has seen it will tell you so. Ask the Pokédex for Red and it will not
come back. Not because the search is broken. Because the search was keyed to one palette, and
nobody ever told it there was another.

That is the whole shape of the problem. Most of the descriptive vocabulary a student is handed for
skin is keyed to colour, and it was calibrated on lightly pigmented skin. *Erythematous* means
reddened. *Cyanosis* means blue. *Jaundice* means yellow. In darker skin those descriptors are
unreliable and sometimes simply wrong, and a clinician taught only the colour-keyed version will
under-recognise inflammation, detect cyanosis late, misjudge severity, and reassure where a more
experienced colleague would not. The failure is in the vocabulary. It is a competence issue and it
should be named as one.

## What this analogy carries, and what it does not

**Shiny** is a one-in-several-thousand flourish with no consequences, and a trainer who never
meets one has lost nothing. Skin tone is neither rare nor a flourish, and nobody is a variant of a
default. The analogy carries exactly one thing and nothing else: **a description keyed to colour
fails on an appearance it was not calibrated for, and the fault is in the description.** The
rarity, the novelty and the collector's interest have no counterpart here and should be dropped at
the door.

## Why the failure is systematic — the mechanism

Two different pieces of machinery produce the two answers, which is why they can disagree
reliably. The body colour is a field written once into the species table. The palette is picked at
draw time: the game exclusive-ors the halves of the **Original Trainer**'s **ID No.** against the
halves of the personality value, and if the result is small enough it reaches into the shiny
palette table instead of the ordinary one. That is the entire consequence. Not one stat, not one
type, not one **Ability**, not one line of the learnset.

```
   WHEN THE LOOKUP IS KEYED TO COLOUR, THE LOOKUP IS WHAT FAILS
   ===================================================================================

   THE QUESTION ASKED        WHAT IS ACTUALLY CHECKED      WHAT CARRIES IT INSTEAD
   =======================   ===========================   ===========================
   list every Red Pokemon    a fixed body-colour field     the palette the sprite was
                             on the species table; for     drawn from, chosen at draw
                             Gyarados it says Blue and     time and completely
                             no shiny changes it           independent of that field
   =======================   ===========================   ===========================
   is this one unusual?      nothing on the sprite; the    the Pokedex number printed
                             difference can be enormous    in a different colour, and
                             or almost nothing            the portrait background
                                                          palette swapped -- a readout
                                                          that does not ask your eye
   =======================   ===========================   ===========================
   Gyarados: blue 180 205    the four body blues become    an unmissable difference
   255 / 131 164 230 / 98    four reds -- 255 189 172,     that proves nothing about
   131 164 / 65 65 106       255 115 115, 213 74 115,      how well the eye does in
                             123 41 65                     general
   =======================   ===========================   ===========================
   Pikachu: yellow           becomes 246 205 32, a         exactly why a dedicated
   255 238 0                 slightly duller, oranger      indicator exists; several
                             yellow, and the black         palette slots are
                             outline is byte-identical     byte-identical between the
                                                          two files
   =======================   ===========================   ===========================
   Umbreon: five body        every one of the five is      only the rings and the eye
   greys, 49 41 41 up to     byte-identical between the    move -- gold 139 98 0 up to
   180 164 164               normal and the shiny file     255 238 139 becomes blue
                                                          32 74 148 up to 148 230 255
   =======================   ===========================   ===========================
```

**Pikachu** and **Umbreon** are the rows that matter. A shiny **Gyarados** is the easy case, and
anybody can be trained on the easy case and come away confident. A shiny **Pikachu** differs by
one step of saturation in one palette slot. A shiny **Umbreon** has a body byte-for-byte the same
colour as every other **Umbreon** and differs only in the rings — which is to say the difference
is real, it is diagnostic, and it is confined to a region you have to know to look at. Scanning
the whole sprite for a general impression of colour finds nothing at all. The games do not leave
it to your eye: the summary screen prints the dex number in a different colour and swaps the
palette behind the portrait, because an appearance judgement is a poor channel for a fact that
matters.

The clinical equivalent of that dedicated indicator is: contour, texture, warmth, induration,
scale, swelling, the sites where the epidermis is thinnest — palms, soles, conjunctivae, the mouth
and the hard palate — and above all the patient's own account. Erythema, cyanosis and pallor are
haemoglobin changes and jaundice is bilirubin, all of them below the epidermis, while melanin sits
above and attenuates the channel they travel on. The signal is still there. The channel is not
reliable. Use another one.

And it is not only the eye that was calibrated narrowly. The Pokédex AREA screen is built by
walking the wild-encounter tables, which works for every species in the game bar one: **Feebas**
turns up on a handful of tiles in a single route, the general method gets it wrong, and the code
carries a hard-coded table for **Feebas** alone to patch over it. A tool whose general method
needs a special case bolted on is a familiar object. Pulse oximetry is known to overestimate
arterial oxygen saturation more often in people with darker skin, and device regulators have
issued safety communications about it. An instrument built on light passing through skin inherited
the same assumption that the body-colour field did.

## The mark that stays after the thing has gone

A Pokémon that catches **Pokérus** is infectious for a few days and then clears, and is not
contagious afterwards. Two things outlast the infection. The summary screen keeps a permanent
mark, drawn specifically for a Pokémon that no longer has Pokérus and has had it. And the doubled
**Effort Values** keep coming — the code asks whether the Pokémon has *ever* had Pokérus, not
whether it has it now, so a cured Pokémon goes on earning twice the **EVs** from every battle for
the rest of its life. The active phase ended. The consequence did not, and the mark is how you
know to expect it.

Post-inflammatory pigment change works the same way and is some of the best information available:

* **It is a map of resolved disease.** The distribution of hyperpigmentation or hypopigmentation
  records where the eruption was and roughly how severe it got, after every other sign has gone. A
  patient who presents between flares is not presenting with nothing.
* **It changes what counts as a response.** The inflammation clearing is not the end of the
  episode, and a record saying the rash has resolved while the pigment change is still spreading
  over the shins is an incomplete record.
* **It is very often the reason the person came.** This part is not an analogy and is handled
  plainly below.

Both directions happen, for a reason: activated melanocytes leave hyperpigmentation, damaged or
suppressed ones leave hypopigmentation, and both are more frequent, more marked and more
persistent in darker skin. Three findings travel with this in the standard texts: keloid and
hypertrophic scarring are more common, so the threshold for anything that leaves a wound is
different; inflammatory eruptions are more often papular and follicular; and lichenification and
scale are often far more conspicuous than any colour change.

## What changes in the examination itself

**The reference is this individual, not a reference image.** You do not establish that a Pokémon
is shiny by remembering what the species looks like in a book; you compare against what that
Pokémon's own data says it should be. Compare affected skin with the person's own unaffected skin,
on the same limb, in the same light.

**Ask the Original Trainer.** They raised it, they have been looking at it for weeks, and in an
assessment that turns on spotting a deviation from a baseline you do not hold, they hold the
baseline. This is the most reliable instrument in the room, not a courtesy.

**Record what was actually seen.** Writing *erythematous* by default on skin where nothing red was
visible is writing Blue into the record for the **Gyarados** in front of you, and the next reader
will reason from it.

**Look at the pages the main screen skips** — the whole surface, scalp, mucosae, nails, palms and
soles. A **Held Item** was never drawn on any sprite either, and **Knock Off** is how a trainer
finds out: some of this has to be touched rather than looked at.

**Use daylight**, and keep the lighting consistent if photographing, because inconsistent lighting
destroys the only comparison that was working.

## Why the teaching fails, structurally

Nobody decided to exclude the red **Gyarados**. One field, one value per species, assigned once,
and every tool built on top of it inherited the assumption silently. That is the exact shape of
the curriculum problem: image libraries under-represent darker skin, so the pattern library a
trainee builds is skewed before they meet a patient; the written descriptors are colour-keyed; and
assessment has historically rewarded the colour-keyed version, so the gap is reproduced each year
rather than closed. Treating it as a caveat to add at the end of a teaching session is part of how
it persists.

## Where the metaphor stops

This section carries no Pokémon, because the mechanism is over and the consequence is not
something to be cute about.

Visible skin disease is socially and psychologically costly in a way that is easy to understate
from the other side of a desk. Facial pigment change is not trivial. Hair loss is not trivial.
People change how they dress, where they go and who they see, and they are frequently told the
problem is cosmetic by a clinician who did not ask.

And the consequence of this particular failure of description is not an embarrassing missed sign.
A larger proportion of the melanomas diagnosed in people with darker skin arise on the palms,
soles and nail units, those sites are examined less often, and later-stage presentation of
melanoma in people with darker skin is documented. Later-stage presentation means worse outcomes.
That is why this answer is written as a competence issue and not as an interesting variation, and
it is why there is no joke in this section.

## What a Gym Leader is listening for

Why the failure is systematic rather than occasional, in one sentence of mechanism. Where you
would look to assess a non-blanching rash. Why post-inflammatory hyperpigmentation is a finding
and not a residue. And what you would say to a patient whose rash has cleared and whose pigment
change has not.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md).
Specific to this answer:

* For the clinical appearance of common inflammatory conditions in darker skin: a dedicated
  textbook or atlas of dermatology in skin of colour, which exists precisely because general
  atlases do not cover it, plus the skin-of-colour teaching resources published by your national
  dermatology professional body.
* For pulse oximeter accuracy: the safety communications issued by your national medicines and
  medical devices regulator on pulse oximeter performance.
* For the sites and urgency of suspected skin cancer, including acral and nail-unit disease: your
  region's suspected-skin-cancer referral guideline, issued by the national body that sets
  referral thresholds where you practise.
* For the mechanism of cutaneous optics and melanin: a textbook of skin physiology or
  photobiology.

The Pokémon claims were checked separately, against the pret decompilation of Pokémon Emerald: the
Pokédex body-colour search and the species field it compares against, Gyarados being stored as
Blue, the shiny calculation from the trainer ID and the personality value, the shiny palette table
being its only consequence, the summary-screen indicator, the Pokérus cured mark and its permanent
doubling of Effort Value gain, the Feebas special case in the AREA screen, and the three pairs of
palette files quoted here by value.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

This answer explains why colour-keyed descriptors fail and what to use instead. It names no
diagnosis for any appearance. **Nothing in it can be used to assess or reassure anyone about their
own mole, pigmented band, patch or lump, and that includes everything written above about acral
and nail sites.** Those sites are named so that a clinician examines them, not so that a reader
can examine themselves — the whole argument of this answer is that the assessment is unreliable
without training, which applies with more force to someone looking at their own skin.
Urgent-assessment pathways exist for that reason. Anyone with a new, changing, bleeding or
non-healing skin lesion, or a new pigmented line in a nail, needs to be seen in person.

A rash with fever, or a rash that does not blanch, needs urgent assessment regardless of skin
tone, and the difficulty of assessing blanching in darker skin is a reason to lower the threshold
for seeking help, not to raise it.

Local guidance is the authority on referral and escalation, and it differs by country and by
institution.

## Where this stands, October 2026

This is the part of dermatology teaching that has moved most in the last decade and is still
moving. Dedicated skin-of-colour atlases, image libraries and curriculum reviews have multiplied
and the direction of travel is clear. What has not changed everywhere is the older teaching
material still in circulation and the colour-keyed phrases embedded in it, which is why this
answer is written to be used alongside material that has not caught up. Current as of October
2026.
