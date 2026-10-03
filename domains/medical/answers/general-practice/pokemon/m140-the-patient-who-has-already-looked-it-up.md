---
id: "m140"
slug: the-patient-who-has-already-looked-it-up
style: pokemon
category: general-practice
difficulty: intermediate
question: "When someone arrives having already researched their symptoms, what has actually changed about the information in the room, and why has the asymmetry reversed in only one direction?"
tags: [information-asymmetry, health-information, consultation, prior-probability, trust]
---

# Anybody can read all 336 bytes of the type chart, and nobody can read the number that makes an individual

Generation III splits its knowledge into two kinds and treats them completely differently, and the
split is exactly the one this question is about.

The **general** is in data tables. The type chart, every learnset, every base stat, every
encounter table, every item's effect: all of it is static data, all of it has been read out of the
cartridge by other people, and a Trainer who has read a guide holds it as exactly and as
completely as the engine does. The **particular** is a thirty-two-bit number generated when an
individual is created, from which half a dozen of its properties are derived, and which **no
screen in the game displays**. m083 noticed the first half of this in one sentence — the chart is
in the cartridge and nothing in the battle menu shows it — and this answer is what happens when
you take that sentence seriously and then go looking for the other half.

## The general: one hundred and ten rows, and everything else is ordinary by omission

```
   const u8 gTypeEffectiveness[336] in src/battle_main.c. Three bytes per entry:
   attacking type, defending type, multiplier. 336 / 3 = 112 entries.

   108  real match-ups
     1  TYPE_FORESIGHT, TYPE_FORESIGHT, TYPE_MUL_NO_EFFECT   <- a SEPARATOR, not a rule
     2  real match-ups AFTER the separator:
            NORMAL   -> GHOST   x0
            FIGHTING -> GHOST   x0
        (the two that Foresight and Odor Sleuth are allowed to walk past)
     1  TYPE_ENDTABLE, TYPE_ENDTABLE, TYPE_MUL_NO_EFFECT     <- the sentinel
   ────
   110  rules in total, and by multiplier:

          TYPE_MUL_NOT_EFFECTIVE  (05, x0.5) .... 57
          TYPE_MUL_SUPER_EFFECTIVE(20, x2.0) .... 46
          TYPE_MUL_NO_EFFECT      (00, x0.0) ....  7

   AND NOW THE DENOMINATOR. Generation III defines 18 type constants, so there are
   18 x 18 = 324 ordered pairs. 110 of them are written down.

        THE OTHER 214 ARE x1 BECAUSE THEY ARE ABSENT.

   There is no row anywhere that says "WATER against NORMAL is ordinary". The engine
   walks the list, finds no entry, and leaves the multiplier at 10. So in the single
   most-read reference table in the whole cartridge, "checked and ordinary" and
   "nobody ever entered this" are THE SAME STATE, and no query can separate them.
   That is nursing m073's collapse - a storage class that fails quietly into "no" -
   in the one place every reader goes first.
```

And the published vocabulary contains an entry that behaves like nothing else in it.
`gTypeNames[TYPE_MYSTERY]` is the string `???`. **No species in the game has that type.** Exactly
one move does — **Curse** — and `CalculateBaseDamage` handles it with a hard-coded special case,
`if (type == TYPE_MYSTERY) damage = 0;`, carrying a source comment that says what it is for. A
category in the published taxonomy with one member, no holders, and its own line in the damage
routine.

## What the chart is, and what it still is not

Everything above is *general*. It is true of a species against a species, it is identical in every
cartridge of the generation, and a Trainer who has read it holds it perfectly.

Four things it does not contain, and they are the four that decide the battle in front of you.

* **Which species is actually there.** The chart is a function of two types. Reading it correctly
  about the wrong creature produces a confident wrong answer, and m007's device is the limiting
  case: **Earthquake** into **Flygon** is ×0, not ×0.5 — no stacking, no repetition and no amount
  of power gets past a zero. A Trainer who has memorised the chart and misidentified the target
  has done everything right and arrived at nothing.
* **Whether an individual property overrides it.** **Wonder Guard** on **Shedinja** replaces the
  chart's answer wholesale for that one creature. The chart is not wrong; it is simply not the
  last word, and the last word is a property of the individual.
* **How often anything appears.** The chart has no prevalence term. m011 took the per-route tables
  for that, and they are a different file.
* **Which cartridge the statement was true in.** This is the big one, and it has its own section.

## Published, correct, and true of a different cartridge

This domain maintains a list of mechanical claims that competent writers got wrong from memory,
every one of them checked against the decompilation. The striking thing about the list is how few
of the entries are *false*. Most are true somewhere.

```
   THE STATEMENT                              WHERE IT IS TRUE      WHAT EMERALD HAS
   ─────────────────────────────────────────  ───────────────────   ───────────────────────────
   Politoed has Drizzle                       Generation V on       Water Absorb and Damp;
                                                                    in Gen III only Kyogre
                                                                    has Drizzle
   Sandstorm raises ROCK-types' Sp. Defence   Generation IV on      Cmd_weatherdamage exempts
                                                                    Rock, Ground and Steel from
                                                                    maxHP/16 and has no boost
                                                                    clause at all
   Spikes can be layered three times          Generation III on     three - but Gen II has one,
                                                                    so the sentence dates the
                                                                    cartridge rather than the
                                                                    mechanic
   Struggle's recoil is a fixed fraction      ambiguous as written  a fraction of damage dealt
                                                                    in Gen II-III, a fraction
                                                                    of max HP from Gen IV
   ─────────────────────────────────────────────────────────────────────────────────────────────
   NONE OF THESE SENTENCES CARRIES THE POPULATION IT WAS DERIVED IN. They are correct,
   they are widely published, and they are silent about the one thing a reader needs
   to know in order to use them. m111 is the full argument: what fails to transport
   is not the rule, it is the setting the rule was fitted in.
```

The general knowledge is public. The *provenance* of the general knowledge is not, and it is the
provenance that decides whether a true statement applies here.

## The particular: one thirty-two-bit number, derived from six ways, displayed nowhere

```
   THE PERSONALITY VALUE. One u32, assigned at creation, from which:

     nature ........ personality % NUM_NATURES            (25)
     ability slot .. personality & 1
     gender ........ gSpeciesInfo[species].genderRatio > (personality & 0xFF)
                     ? MON_FEMALE : MON_MALE
     Unown's letter  four 2-bit fields pulled from bytes 0, 1, 2 and 3, ORed
                     together and taken % NUM_UNOWN_FORMS (28)
     shininess ..... GET_SHINY_VALUE(otId, personality) < SHINY_ODDS, where
                     SHINY_ODDS is 8 - out of 65 536
     Spinda's spots  derived from the same value, which m016 took for
                     per-individual morphology

   NOT ONE OF THOSE SIX IS SHOWN AS A NUMBER ANYWHERE IN THE GAME, and neither are
   the six individual values or the six effort values.

   AND THE PARTICULAR IS NOT ADDRESSABLE. The engine cannot write a nature, a
   gender or a letter. CreateMonWithGenderNatureLetter does this:

       do { personality = Random32(); actualLetter = GET_UNOWN_LETTER(personality); }
       while (nature != GetNatureFromPersonality(personality)
           || gender != GetGenderFromSpeciesAndPersonality(species, personality)
           || actualLetter != unownLetter - 1);

   To obtain a particular individual the engine throws the whole individual away
   and draws another one. There is no setter. There is no field to edit. The
   particular can only be OBSERVED, and observing it means working backwards from
   what the creature does.
```

## The Pokédex page is handed the individual and uses it to draw the picture

The clearest single demonstration is in the Pokédex's own interface.

`struct PokedexEntry` is thirty-two bytes: a twelve-character category name, a height in
decimetres, a weight in hectograms, a pointer to the description paragraph, and four numbers used
for scaling the sprite against the Trainer's. One entry per species. `GetPokedexHeightWeight`
takes a **dex number** — not a Pokémon — so two individuals of the same species print the same
height and the same weight, always.

And `DisplayCaughtMonDexPage` has this signature: `u8 DisplayCaughtMonDexPage(u16 dexNum, u32
otId, u32 personality)`. The page for the thing you just caught is given that individual's trainer
id and personality value, and everything printed on it belongs to the species. The particular is
passed in so the picture can be drawn correctly, and no number on the page is about the creature
you are holding.

The **Area** screen is the same shape in miniature: it will tell you that a species occurs on a
map, which is true and public, and it will not tell you which rod reaches it — the gap m112 found
when it took the three rods as the channel that decides what is in the sample space at all.

## Where the reversal actually sits

```
                   │ GENERAL                        │ PARTICULAR
   ────────────────┼────────────────────────────────┼─────────────────────────────────
   in the cartridge│ 336 bytes of chart, the whole  │ one u32 per individual, plus
                   │ learnset tables, every base    │ 6 IVs and 6 EVs
                   │ stat, every encounter table    │
   ────────────────┼────────────────────────────────┼─────────────────────────────────
   shown to the    │ NOTHING. The battle menu does  │ NOTHING as a number. Nature is
   player          │ not display the chart (m083)   │ a word on a summary screen;
                   │                                │ the rest is invisible (m020)
   ────────────────┼────────────────────────────────┼─────────────────────────────────
   available to a  │ ALL OF IT, exactly, from a     │ none of it directly - only by
   reader outside  │ guide or a disassembly         │ inference from what the
   the game        │                                │ individual actually does
   ─────────────────────────────────────────────────────────────────────────────────────

   THE LEFT COLUMN REVERSED COMPLETELY. A Trainer with a guide holds the general
   better than the interface does. THE RIGHT COLUMN DID NOT MOVE AT ALL, and it is
   the column that decides what happens next.
```

## Where the metaphor stops

People look things up because they are frightened and because waiting is hard. That is the whole
of it and it needs no other explanation. Reading at three in the morning about something that
might be happening to you is not a failure of discipline; it is what anybody does.

Being dismissed for having read about it is corrosive out of all proportion to the consultation it
happens in. It is reported most by people whose symptoms are hard to see, whose conditions
fluctuate, who are young, who are women, and who have been doubted before — and the effect is not
only that one question goes unanswered. It changes whether they come back, what they say when they
do, and whether they believe the reassurance when it is finally the right answer. Being
disbelieved while unwell is its own injury and it is distributed unequally.

There is also a genuine skill question that this pair's tidy two-by-two does not capture. For a
rare condition, a person who has it can hold more depth in it than any generalist will, and the
documented pattern in rare-disease diagnosis includes a great many cases where the person or their
family named the answer first. Holding that open at the same time as holding a prior is the actual
clinical work, and neither half of it is optional.

And the honest half from the other side. A consultation that arrives with a conclusion already
formed takes longer than the time available, and the clinician is sometimes being asked to
disprove something that cannot be disproved — which is not a reasonable request and cannot be met
by agreeing to it. Saying plainly that a test cannot answer the question, and then staying in the
room, is difficult under time pressure. Naming that difficulty is more useful than implying the
skilled version of this consultation is easy.

## What a Gym Leader is listening for

Whether the Trainer gets the arithmetic of the chart right: 336 bytes, 112 entries, one separator
and one sentinel, 110 rules, and 214 of the 324 ordered pairs ordinary **by omission** rather than
by statement. Then the collapse that follows — that absent and ordinary are one state — with m073
named. Then `TYPE_MYSTERY`, its `???` display name, its single move and its hard-coded zero. Then
the four things the chart does not contain, with **Flygon** against **Earthquake** as the
misidentification case and **Wonder Guard** as the individual override. Then provenance: at least
two statements that are true in a later generation and false in Emerald, with Politoed's actual
abilities named. Then the personality value: six derivations from one u32, none displayed, and
`CreateMonWithGenderNatureLetter` re-rolling the whole individual because there is no setter. Then
`GetPokedexHeightWeight` taking a dex number while `DisplayCaughtMonDexPage` takes the personality
— the page handed the particular and using it only to draw. Then the hard one: what a Trainer
would have to *do* to the creature in front of them to recover any of the right-hand column, and
why that is a different kind of work from reading.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-general-practice.md`](../../../for-agents/SOURCES-general-practice.md).
Specific to this answer:

* The patient information material issued by the reader's own national health service or national
  body, which is the material a reader is most likely to have found.
* The reader's professional regulator's guidance on communication, consent and shared decision
  making (**country-dependent**).
* The published literature on online health information seeking and its effects on consultations,
  read for the consistent findings and for the contested ones.
* The published literature on diagnostic delay in rare diseases, for the documented pattern of the
  person or the family identifying the diagnosis first.
* Any evaluation of symptom checkers or of generated clinical answers in the reader's own system,
  read for performance on real presentations rather than on vignettes.

The Pokémon facts are a separate matter and are not covered by the line above.
`gTypeEffectiveness[336]` with its 112 three-byte entries, the `TYPE_FORESIGHT` separator at entry
109 and the two post-separator immunity rows, the `TYPE_ENDTABLE` sentinel, and the counts of 57
halves, 46 doubles and 7 zeroes; the 18 type constants and therefore 324 ordered pairs;
`gTypeNames[TYPE_MYSTERY]` being `???`, no species carrying that type, `MOVE_CURSE` being the only
move that does, and the `if (type == TYPE_MYSTERY) damage = 0;` line in `CalculateBaseDamage`;
Politoed's abilities being Water Absorb and Damp in Emerald; `Cmd_weatherdamage` exempting Rock,
Ground and Steel from maxHP/16 with no Special Defence clause; the personality-value derivations —
`personality % NUM_NATURES`, `personality & 1`, the gender-ratio comparison against `personality &
0xFF`, `GET_UNOWN_LETTER`'s four 2-bit fields taken modulo 28, and `GET_SHINY_VALUE` against
`SHINY_ODDS` of 8; `CreateMonWithGenderNatureLetter`'s re-roll loop; and `struct PokedexEntry`'s
32 bytes with `GetPokedexHeightWeight` taking a dex number while `DisplayCaughtMonDexPage` takes
an OT id and a personality value, were all read directly from the pret decompilation projects,
which this environment can reach. These are Emerald's, except where a later generation is named as
the place a statement is true.

## Scope and safety

This is revision material about the structure of a consultation, written for someone already
training in or qualified for the field. It is not a clinical reference and not a decision aid.
**It is not advice about how any individual should use health information about themselves**, and
nothing here says whether any particular source, website, application or symptom checker is
reliable — that is a question about specific tools, it changes, and it is not answerable from
here. No test, threshold, condition or probability is named in this pair on purpose. The byte
counts, modulo arithmetic and shiny odds above are real and stand in for a mechanism; none of them
is a clinical quantity and no clinical figure should be read out of them. If you are a patient
reading this: looking things up is reasonable, and the one thing worth bringing to a consultation
is what you are most worried about. If someone is unwell right now, the relevant action is to
contact local urgent care or the local emergency number, not to read this.

## Where this stands, October 2026

The structural claim — that the general became public while the particular did not, so the
reversal is one-dimensional — is mechanism and will not move. So are the properties of what gets
found, the treatment of a search as a history item, and the unequal distribution. What is moving
quickly is the technology: generated answers, consumer devices producing continuous physiological
data, direct-to-consumer testing and patient access to their own records all change what arrives
in the room, and each of them acts on the *right-hand* column as well as the left. That is the
development most likely to date this pair, because it attacks the half of the asymmetry that has
so far held. The Emerald code is stable because the games are finished. Take any claim about a
specific tool's performance from a current evaluation rather than from here, as of October 2026.
