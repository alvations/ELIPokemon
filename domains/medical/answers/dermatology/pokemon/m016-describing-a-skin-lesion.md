---
id: "m016"
slug: describing-a-skin-lesion
style: pokemon
category: dermatology
difficulty: core
question: "How should a skin lesion be described, and why does the primary morphology constrain the differential more than any other single step?"
tags: [morphology, examination, description, documentation, dermatology]
---

# Spinda's spots are not how you know it is a Spinda

The **Pokédex** is a descriptive instrument before it is a diagnostic one. It does not open on a
verdict; it opens on fields, and the fields are a fixed vocabulary you fill in. The field that
closes most of the list is the one that says what kind of thing this is at all. Everything else —
where it lives, what it weighs, which **Route 1** patch of **Tall Grass** it came out of — refines
a partition you have already committed to. Call a **Haunter** a **Gengar** and you have not slowed
down by a turn; you are now reasoning about a Pokémon that is already fully evolved and will never
need a trade.

## The vocabulary, which is definitional rather than contested

The Gen III **Pokédex** ships with a closed descriptive vocabulary and a search built on it. It
will list the whole national dex by body colour, and the list of colours has exactly ten entries:
Red, Blue, Yellow, Green, Black, Brown, Purple, Gray, White and Pink. That is not a judgement
call. It is a field stored on every species, definitional in the way that *macule* is
definitional, and its only purpose is to cut the search space.

A single comparison can decide an entire branch. **Tyrogue** has three evolutions and the game
picks between them with one check:

```
   THE ONE COMPARISON THAT PARTITIONS EVERYTHING ELSE
   Tyrogue, at level 20.  One comparison, three completely different Pokemon.

   compare Attack with Defense
   |
   +-- Attack  >  Defense -----------------------------> HITMONLEE
   |                                                     the legs: Mega Kick, Rolling Kick
   +-- Attack  <  Defense -----------------------------> HITMONCHAN
   |                                                     the fists: Fire Punch, Ice Punch,
   |                                                     Thunder Punch
   +-- Attack  == Defense -----------------------------> HITMONTOP
                                                         neither, and it fights on its head

   Nothing else about Tyrogue changes the answer.  Not its Nature, not its
   nickname, not the Poke Ball it came in, not where it was caught.
```

Get that one comparison wrong in your notes and you have written down a Pokémon that cannot learn
the moves you are planning around. The size conventions in the medical vocabulary vary slightly
between atlases, which matters about as much as the fact that **Hyper Potion** heals a different
amount in different generations: record the number beside the word and the variation stops
mattering.

## Why the field you fill in is really a statement about depth

```
   WHAT THE FIELD COMMITS YOU TO

   WHERE IT SITS      THE FIELD               WHAT MUST THEREFORE BE TRUE
   ===============    ====================    =========================================
   on the surface     body colour             fixed per species, set once in the
                                              species table and never recalculated
                      the sprite              drawn from a palette table, which is a
                                              separate thing from the species data
   ===============    ====================    =========================================
   underneath         types                   Gourgeist is Ghost and Grass in all four
                                              of its sizes -- the single field that
                                              most constrains what will work on it
                      base stats              Gourgeist Small has 55 HP and 99 Speed;
                                              Super Size has 85 and 54, and Defense
                                              sits at 122 in both of them
   ===============    ====================    =========================================
   a named size       Small / Average /       Pumpkaboo and Gourgeist each come in four
                      Large / Super Size      named sizes, and the size is part of the
                                              identification, not decoration
```

**Pumpkaboo** and **Gourgeist** make the point cleanly: the size category has a name, the name is
part of what the thing is, and changing it changes what the thing does. That is exactly the work
*papule* against *plaque* is doing. Different compartment, different creature.

## Secondary change is a record of the battle, not of the species

A Pokémon that is **Badly Poisoned**, down to a tenth of its **HP**, with its Attack lowered two
stages and **Leftovers** ticking, is carrying a great deal of information — about the last nine
turns. None of it says what it is. **Smokescreen** landed, something used **Swords Dance**,
somebody switched. Leading with any of that is the commonest way a battle log becomes useless,
because the same crust of status and stat stages is produced by a dozen unrelated openings.

## The record worth writing down

The summary screen fills its fields in a fixed order on purpose: species and Pokédex number,
nickname, level, **Original Trainer** and **ID No.**, **Nature**, **Ability**, **Held Item**, and
where and at what level it was met. The order forces the identification first and leaves
everything downstream re-readable by the next trainer.

**It cannot be done by looking.** A wild **Pikachu** in Hoenn may be carrying an **Oran Berry**,
and it may be carrying a **Light Ball**, and the screen says neither. **Knock Off** is how you
find out. A **Nature** and an **Ability** are not on the sprite either. This is the structural
reason that assessing a Pokémon from a screenshot is harder than it looks: the fields that decide
the battle are not the ones that are drawn.

**And do not smuggle the verdict into the description.** Writing down *a sweeper* instead of
**Salamence** records a conclusion and destroys the evidence, because nobody downstream can now
disagree with it.

## Spinda, which is the whole lesson in one species

**Spinda** has four spots on its front sprite. Their positions are generated from its personality
value — a single 32-bit number, four bits for each coordinate of each spot, so each spot lands
anywhere from eight pixels left of its base position to seven pixels right. No two Spinda you meet
are patterned alike, and the **Pokédex** has to store the personality of the first Spinda you saw
purely so it can redraw the same one consistently.

Now the part that matters. Not one bit of that touches a stat, a type, an **Ability** or a
learnset. The variation is real, it is visible, it is the first thing anyone notices, and it is
not the identification. Every **Spinda** is a Spinda. A description that leads with the spots has
led with the one feature that varies between individuals while the answer does not.

## Where the metaphor stops

This section carries no Pokémon, because the mechanism is over and the consequence is not
something to be cute about.

A description is written about a person who has usually been asked to undress in a cold room in
front of a stranger, and who may have been self-conscious about that skin for years. Thoroughness
and kindness are not competing here: say what you are looking at and why, expose one region at a
time, offer a chaperone, and accept a refusal. A rushed examination that skipped the scalp because
asking felt awkward is not a kinder examination. It is a worse one.

The record has a human consequence too. The next person to read it may be deciding whether this
patient is seen today or in six weeks. A description that wrote down a conclusion instead of the
findings has quietly taken that decision away from them.

And this needs saying without softening: nothing in this vocabulary allows anyone to settle a
worry about their own skin. Recognising your own lesion in a definition is not an assessment and
is not reassurance. A new, changing, bleeding or non-healing lesion needs to be looked at by a
person who is trained to look at it.

## What a Gym Leader is listening for

Why a pustule is not evidence of infection — which in this register is why a flinch is not
evidence of **Fake Out**. How you would separate a patch from a plaque on a real arm, when no
screen will print it. What a wheal rules out by being gone within a day. And how you would write
the record when the next reader is deciding whether somebody needs to be seen today.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md).
Specific to this answer:

* For the morphology vocabulary and the size conventions: any standard dermatology atlas or
  textbook of clinical dermatology. These terms are definitional and a current edition of a
  recognised atlas is the right authority; the terms do not come from a guideline.
* For the structure of a dermatological examination record: the clinical examination guidance
  issued by your national dermatology professional body.
* For anything concerning urgency or referral: your region's suspected-skin-cancer referral
  guideline, issued by the national body that sets referral thresholds where you practise.

The Pokémon claims are a separate matter and were checked against source. Spinda's spot
generation, the Pokédex body-colour search, the Tyrogue branch and the wild Pikachu held items are
from the pret decompilation of Pokémon Emerald. The Pumpkaboo and Gourgeist size data is from the
Gen VIII species tables in the pokeemerald-expansion project, because the pret decompilations
cover the first three generations only.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

This answer explains the vocabulary used to describe lesions. It deliberately pairs no morphology
with a diagnosis, and it cannot be used to work out what a lesion on a real person is. **Nothing
here can be used to reassure anyone about their own mole, patch or lump.** Urgent assessment
pathways for suspected skin cancer exist because the relevant features are not reliably
self-assessable, and a Pokémon analogy is not an assessment of anything. Anyone with a new,
changing, bleeding or non-healing skin lesion needs to be seen in person.

Local guidance is the authority on everything procedural here, and it differs by country and by
institution.

## Where this stands, October 2026

The morphology vocabulary has been stable for decades, which is why it is the safest ground in the
specialty — rather more stable than **Hyper Potion**, which has been rebalanced since **Kanto**.
The 1 cm against 0.5 cm cut-off still varies between textbooks. Record the millimetres beside the
word and the variation stops mattering, and that is the practice to carry forward from October
2026.
