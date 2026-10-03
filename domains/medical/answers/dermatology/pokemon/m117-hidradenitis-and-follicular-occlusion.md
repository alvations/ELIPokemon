---
id: "m117"
slug: hidradenitis-and-follicular-occlusion
style: pokemon
category: dermatology
difficulty: advanced
question: "Why is hidradenitis suppurativa misread as recurrent infection for years, and what does the follicular occlusion mechanism change about the plan?"
tags: [hidradenitis, follicular-occlusion, inflammation, misdiagnosis, sinus-tract]
---

# Thunder hits a Fly user, and almost everybody's reason for it is wrong

Ask why Thunder hits a Pokémon in mid-Fly and the answer comes back fast: because rain makes
Thunder always hit. The observation is correct. Thunder does hit a Fly user. The explanation is
wrong, and reading the code shows exactly where it goes wrong.

`AccuracyCalcHelper` runs its checks in a fixed order, and the second thing it does is this:

```
   AccuracyCalcHelper, as written
   ==================================================================================
   if (!(gHitMarker & HITMARKER_IGNORE_ON_AIR)
         && gStatuses3[gBattlerTarget] & STATUS3_ON_AIR)
   {
       gMoveResultFlags |= MOVE_RESULT_MISSED;
       JumpIfMoveFailed(7, move);
       return TRUE;                 <-- RETURNS. Nothing below runs.
   }
   ==================================================================
   The weather clauses are BELOW this. With the target on air and the
   override bit clear, the function has already returned a miss before
   any rain is consulted. The rain explanation describes a branch that
   was never reached.
   ==================================================================
   WHAT ACTUALLY DOES IT -- four scripts set the override, and they
   are not alike:

     BattleScript_EffectTwister    jumpifnostatus3 first, THEN the
                                   override, AND setbyte sDMG_MULTIPLIER, 2
     BattleScript_EffectGust       same shape: conditional, and doubles
     BattleScript_EffectThunder    orword gHitMarker, HITMARKER_IGNORE_ON_AIR
                                   -- UNCONDITIONAL, and NO doubling
     BattleScript_EffectSkyUppercut  unconditional, no doubling
   ==================================================================
```

Thunder hits a Fly user because one unconditional `orword` sits in its own script, with no weather
term anywhere near it. (And Thunder is the one that does **not** double its damage against an
airborne target, which Gust and Twister do — so the popular explanation does not merely misname
the cause, it predicts a damage bonus that is not there.)

That is the exact shape of the thing that keeps hidradenitis suppurativa misdiagnosed for years.
The observation is right. The inference is wrong. And the wrong inference makes further
predictions which also fail, and which nobody checks because the first prediction looked
confirmed.

## Markers used in this answer

The clinical claims here carry the same inline markers as the serious half. (**mechanism**) —
follows from the biology and is checkable by reasoning. (**definitional**) — a term's meaning.
(**consensus**) — standard across current textbooks and national guidance. (**country-dependent**)
— differs between countries or institutions, and yours is the authority. The Pokémon claims are
not marked this way; they are listed in the `## Sources` section with the file they were checked
against.

## The antibiotic worked, therefore it was an infection

Line up the clinical observations against the Thunder case and they are the same argument.

| Observation | The inference drawn | Why it is Thunder-in-rain |
| --- | --- | --- |
| Tender fluctuant lumps discharging pus | An abscess | Correct description of the sign; the sign does not name its cause. Pus is a neutrophil response and a ruptured follicle spilling keratin into the dermis produces one without any organism (**mechanism**) |
| Incision and drainage relieves it | Drainage treats the cause | It relieves pressure. It does not act on the occlusion or the tract, and recurrence at the same site is the prediction that fails (**consensus**) |
| Antibiotics help | An organism was driving it | The tetracyclines used in this disease have anti-inflammatory as well as antibacterial activity and are used partly for that reason, so improvement is not evidence of infection (**mechanism**, **consensus**) |
| It keeps coming back | Reinfection, or inadequate treatment | Or: the natural history of a follicular disease whose distribution is set by where terminal follicles sit in apposed skin (**mechanism**) |

The disciplined move is the one the disassembly forces: when a treatment works, ask which branch
actually ran. A response that is compatible with two mechanisms is not evidence for either, and a
response to an agent with two activities is evidence about neither until you know which one did
it. m086 makes the neighbouring point with Growl — a treatment aimed at the readout changes the
readout — and this is its sibling: a treatment with two mechanisms confirms neither.

## Six names, four types, one `EFFECT_TRAP`

The follicular occlusion family is four separately named diseases in four sites running one
mechanism, and the game has an exact model of that: a set of moves with distinct names, distinct
types and distinct flavour, all compiling to one effect constant and one shared counter.

```
   EVERY EFFECT_TRAP MOVE IN THE THIRD GENERATION
   ==================================================================================
   MOVE          POWER   TYPE      ACC   PP   CONTACT?
   ===========   =====   =======   ===   ==   ========
   Bind             15   Normal     75   20   yes
   Wrap             15   Normal     85   20   yes
   Fire Spin        15   Fire       70   15   no
   Clamp            35   Water      75   10   yes
   Whirlpool        15   Water      70   15   no
   Sand Tomb        15   Ground     70   15   no
   ==================================================================
   ONE effect constant. ONE counter:

       status2 |= STATUS2_WRAPPED_TURN((Random() & 3) + 3)   // 3-6 turns

   ONE per-turn cost:   maxHP / 16, floored at 1
                        -- the same denominator as Leftovers and Sandstorm

   AND the ONLY thing that differs downstream is the MESSAGE. A
   separate hand-maintained table, gTrappingMoves, is walked purely
   to choose which move name to print, and the loop breaks at
   NUM_TRAPPING_MOVES - 1, falling through to the last entry for
   anything not listed.
   ==================================================================
   Fire Spin sounds like burning. Whirlpool sounds like drowning.
   Sand Tomb sounds like burial. They are the same mechanic with
   different names printed, and the names are the only difference
   a player can see.
   ==================================================================
```

The species that carry them are as unalike as the names. **Charmander** learns Fire Spin at level
49; **Shellder** learns Clamp at level 41; **Trapinch** learns Sand Tomb at level 25, and
**Dugtrio** learns the same move at 26. A Fire-type lizard, a bivalve and a desert ant-trap, three
unrelated level-up learnsets, one effect constant. Nothing a player can observe about the three
suggests they are the same act, and they are the same act.

That is the follicular occlusion family. (**consensus**)

| Condition | Site | The shared mechanic |
| --- | --- | --- |
| **Hidradenitis suppurativa** | Axillae, groin, perineum, gluteal, inframammary | Occlusion → rupture → foreign-body response → tunnel |
| **Acne conglobata** | Face, trunk, back | The same, in sebaceous-rich skin |
| **Dissecting cellulitis of the scalp** | Scalp | The same, in scalp follicles, with scarring hair loss |
| **Pilonidal sinus** | Natal cleft | The same, with hair as the foreign material |

Four names that advertise four different problems, running one sequence. The names are the message
string. And as with the trapping moves, co-occurrence in individuals and in families is the
observation that revealed the shared constant underneath. (**consensus**)

The per-unit-time cost is worth one line of its own. Trapping bills `maxHP / 16` every turn while
the counter runs — a small number that is invisible on any single turn and decisive across the
episode. It is the Leftovers argument with the sign reversed, and it is the right shape for a
disease whose damage is almost entirely cumulative.

## The occlusion is the move, and the gland is standing next to it

Two of the mechanics above deserve pinning to the anatomy, because this is the point the name gets
wrong.

The lesion is the **terminal hair follicle**. It plugs, distends, and ruptures into the dermis,
spilling keratin and hair shaft fragments into a compartment that will mount a brisk foreign-body
and neutrophilic response to the host's own material. (**mechanism**) The apocrine glands are in
that skin. They are not the lesion. "Hidradenitis" means inflammation of sweat glands and points
at the wrong structure; "suppurativa" means pus-forming and points at a real sign with a false
implication. (**definitional**)

Which makes the name itself a `gTrappingMoves` lookup: a label chosen for printing, carrying no
information about which branch ran. "Acne inversa" is also in use and is also imperfect, and the
argument between them is an argument about which structure the label should name.

## `STATUS3_ROOTED` has no timer, and that is the tunnel

Here is the single most useful mechanical fact in this answer, and it decides the treatment plan.

Count the clocks in `DisableStruct`. There are eight named ones — `disableTimer`, `encoreTimer`,
`perishSongTimer`, `rolloutTimer`, `chargeTimer`, `tauntTimer`, `rechargeTimer`, and the
`protectUses` / `stockpileCounter` / `furyCutterCounter` group — and there is **no
`rootedTimer`**. The string does not appear in the struct, or in `battle_util.c` at all.
`Cmd_trysetroots` is three lines:

```
   static void Cmd_trysetroots(void)
   {
       if (gStatuses3[gBattlerAttacker] & STATUS3_ROOTED)
           gBattlescriptCurrInstr = T1_READ_PTR(gBattlescriptCurrInstr + 1);   // fails
       else
       {
           gStatuses3[gBattlerAttacker] |= STATUS3_ROOTED;                     // sets the bit
           gBattlescriptCurrInstr += 5;
       }
   }
```

It sets a bit, and nothing anywhere decrements it. (m072 noticed this from the other side: rooted
is the only trapping state with no clock at all.) Compare the trapping counter three sections up,
which is explicitly `(Random() & 3) + 3` and is decremented every end of turn until it runs out.

**Two states, two stores, two completely different problems.**

| The state | Where it lives | What ends it |
| --- | --- | --- |
| **The inflammatory episode** — tender nodule, pus, flare | A timed store. It has a counter and the counter runs down | Time, and anything that suppresses the process. Medical treatment acts here (**mechanism**) |
| **The sinus tract** — epithelialised tunnel, bridged scar | An untimed bit. Set once; nothing decrements it | Nothing in the ordinary path. It is anatomy, and only an intervention on the anatomy touches it (**mechanism**, **consensus**) |

So medical and surgical treatment in this disease are **not alternatives and not a sequence of
last resorts**. They are addressed at different objects: one at a counter that is running, one at
a bit that is set. (**consensus**) A service that offers only one of them produces a predictable
pattern of failure, and that pattern is diagnostic of the gap rather than of the disease.

Three consequences, at the level of principle; no agent, dose, strength or regimen appears
anywhere in this answer.

* **Draining an acute nodule** relieves the episode and is not definitive; repeated drainage at
  one site contributes to the scarring. (**consensus**)
* **Modifiable factors are treatment, not advice.** Smoking is the most consistently associated
  modifiable factor and friction in apposed skin is why the distribution is what it is; offering
  cessation and weight management as referral pathways rather than as remarks is the difference
  between an intervention and a comment. (**consensus**)
* **Systemic immunomodulatory therapy including biologic agents** has changed what is achievable
  in moderate and severe disease. Which agents are licensed, funded and reachable, and where in a
  pathway, is firmly (**country-dependent**).

And one more untimed bit, which is the thing that gets missed: **squamous cell carcinoma can arise
in long-standing disease**, particularly at gluteal and perineal sites, so a non-healing, changing
or indurated area within chronically affected skin is a new question and needs biopsy rather than
another course of treatment. (**consensus**) A chronic diagnosis does not retire the question of
what a new lesion is.

## Where the metaphor stops

No Pokémon anywhere in this answer stands in for a person. A trapping counter and a rooted bit are
facts about a data structure; nothing in the game stands for anyone's pain, their scars or their
course, and nothing above should be read as doing so. This is the section where the analogy is put
down, and in this answer it matters more than in most.

**This is a painful disease, and the pain is a primary symptom rather than a complication.** It is
frequently reported as the worst feature. Analgesic needs in severe disease are substantial and
are a specialist matter; nothing in this answer speaks to them and no analgesic is named.

**Discharge and malodour are common, intrusive, and a major driver of avoidance.** Dressings may
be needed continuously. Involvement of the groin, perineum and genital skin affects sitting,
walking, working and sexual relationships, and it is routinely not asked about — which means it is
routinely not addressed.

**Depression and anxiety are substantially over-represented.** So is the experience of having been
told, repeatedly and over years, that the problem is hygiene. It is not, and saying so explicitly
is part of the consultation rather than a courtesy. Scarring from this disease is permanent and
sits in places nobody can conceal in a changing room, a clinical examination or an intimate
relationship.

None of that is adjacent to the mechanism. It is the reason the mechanism is worth getting right,
because years of being treated for recurrent infection is years of exactly this. The burden also
cannot be inferred from the extent of skin involved — it is reported as high at every level of
severity — so an assessment that reads severity off the surface area has not assessed the thing
that matters most. The specialist services and the patient organisations for this condition hold
expertise about living with it that no mechanism answer contains, and pointing someone toward them
is a clinical act.

Nothing here is for any reader's own use and no treatment named or implied is a recommendation.
Anyone with recurrent painful lumps in these sites needs assessment in person and sooner rather
than later, because the tunnelling and scarring steps are the irreversible ones. Spreading redness
with fever, rapidly increasing pain, or feeling systemically unwell needs urgent assessment — call
your local urgent care route or emergency number.

## What a Gym Leader is listening for

Which structure is primarily involved, and why both halves of the name point elsewhere. The four
steps in order, and which one has no clock. Why a response to an antibiotic is not evidence of
infection, and what else the wrong inference predicts that turns out to be false. What a sterile
aspirate does and does not say. The three elements of the clinical diagnosis, and why there is no
confirmatory test. Why bridged scars and double-ended comedones are near-specific. The four
members of the follicular occlusion family and the one mechanic they share. Why medical and
surgical treatment are aimed at different objects. And the complication in long-standing disease
that makes a new lesion a new question.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md),
and they are the authority for everything procedural or quantitative here. Specific to this
answer:

* For the diagnostic criteria, the staging and severity instruments, and the treatment pathway:
  the specialist guidance of your national dermatology body, and the relevant European or
  international consensus document where your service follows one. The staging definitions and
  score cut-offs are there and are deliberately not reproduced above.
* For systemic agents including biologics — licensed indication, funding, pre-treatment screening,
  monitoring and infection precautions: your national formulary and your national or regional
  funding policy.
* For surgical options including deroofing and wide excision: your local dermatological surgery or
  plastic surgery service's protocol.
* For smoking cessation and weight management referral pathways: your national guidance and your
  local service specification.
* For the pathology and the follicular occlusion mechanism: a current standard textbook of
  dermatology.
* For the perineal manifestations of Crohn's disease, which is the most important mimic: your
  national gastroenterology guidance.
* For patient information and lived-experience support: your national patient organisation for
  this condition.

The Pokémon claims were checked separately against source. `AccuracyCalcHelper` testing
`HITMARKER_IGNORE_ON_AIR` together with `STATUS3_ON_AIR` and returning before any weather clause
is reached; the four scripts that set that marker being `BattleScript_EffectTwister`,
`BattleScript_EffectGust`, `BattleScript_EffectThunder` and `BattleScript_EffectSkyUppercut`, with
the first two guarded by `jumpifnostatus3` and also setting `sDMG_MULTIPLIER` to 2 while Thunder's
is unconditional and sets no multiplier; the six `EFFECT_TRAP` moves being Bind, Wrap, Fire Spin,
Clamp, Whirlpool and Sand Tomb with the powers, types, accuracies, PP and contact flags tabulated
above; `STATUS2_WRAPPED_TURN((Random() & 3) + 3)` giving three to six turns with the comment in
the source; the per-turn trapping damage being `maxHP / 16` floored at 1; `gTrappingMoves` being
walked only to select the message string, with the loop breaking at `NUM_TRAPPING_MOVES - 1`;
`Cmd_trysetroots` setting `STATUS3_ROOTED` with no timer and failing rather than refreshing if the
bit is already set; Charmander learning Fire Spin at level 49, Shellder learning Clamp at level
41, Trapinch learning Sand Tomb at level 25 and Dugtrio learning it at 26, all read from the
level-up learnset table; and `DisableStruct` containing `disableTimer`, `encoreTimer`,
`perishSongTimer`, `rolloutTimer`, `chargeTimer`, `tauntTimer` and `rechargeTimer` but no field
for Ingrain — all from the pret decompilation of Pokémon Emerald. Sandstorm and Leftovers sharing
the `maxHP / 16` denominator is from the same source and is m055's observation.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No agent, dose, regimen, severity score, stage definition or analgesic is named in this answer,
and none of it addresses any reader's own treatment.** The omission of the staging systems and
severity instruments is deliberate: they are defined in the documents named above and a cut-off
quoted here without the document would be worse than none. Pain management in this condition is a
specialist matter and nothing here speaks to it.

Anyone with recurrent painful lumps in the axillae, groin, perineum, buttocks or under the breasts
needs to be assessed in person, and sooner rather than later because the scarring and tunnelling
are irreversible. A non-healing or changing area within long-standing disease needs assessment and
usually biopsy. Spreading redness with fever, rapidly worsening pain, or feeling systemically
unwell is an emergency — call your local emergency number or use your local urgent care route.

Local guidance and the policy where you practise are the authority on all of this, and they differ
by country and by institution.

## Where this stands, October 2026

The mechanism is settled and is the part worth memorising: occlusion, rupture, foreign-body
response, tunnelling. The clinical triad is settled and remains the diagnosis. The
reclassification away from infection and toward chronic follicular inflammation is settled in
specialist practice and lags elsewhere, which is where the diagnostic delay accumulates.

What moves is treatment. Biologic therapy targeting tumour necrosis factor changed what was
achievable in moderate-to-severe disease, and agents aimed at other cytokine pathways have reached
licensing in several jurisdictions more recently; which are available and funded where you
practise is firmly (**country-dependent**) and is the fastest-changing thing here. Surgical
practice has moved toward tissue-sparing deroofing with wide excision reserved rather than
routine, and the comparative evidence is still developing. The nomenclature is unsettled: "acne
inversa" has advocates and the argument is about which structure the name should point at.
Severity instruments have proliferated and harmonising them is ongoing. Current as of October
2026.
