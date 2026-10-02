---
id: "m090"
slug: urticaria-and-angioedema
style: pokemon
category: dermatology
difficulty: intermediate
question: "Why is a weal that comes and goes a different problem from a swelling that does not, and what follows from that for treatment?"
tags: [urticaria, angioedema, histamine, bradykinin, anaphylaxis]
---

# Refresh does not cure a frozen Pokémon less well, it prints "But it failed!"

The battle script for **Refresh** is five instructions long and the fourth of them is named for
exactly what it does: `cureifburnedparalyzedorpoisoned`, with a branch to
`BattleScript_ButItFailed` if none of those three applies. Refresh is Normal-type, power 0,
accuracy 100, 20 PP, targets the user, and against a sleeping or frozen Pokémon it is not a weak
option. It is **not an option**. The coverage list is written into the command's own name.

That is an antihistamine against bradykinin-mediated angioedema, and it is the single most
important thing in this answer. There is no histamine step in that pathway, so there is nothing
for the drug to bind. More of it does not help. This is m007's rule, and it is worth stating in
its strongest form: **a zero is not a small number.** `Cmd_typecalc` writes `TYPE_MUL_NO_EFFECT`
when an Earthquake meets a **Flygon** — whose only listed ability, in both slots, is **Levitate**
— and no accuracy, no power, no repetition and no dose gets past it.

## Markers used in this answer

The clinical claims here carry the same inline markers as the serious half. **mechanism** —
follows from biology and is checkable by reasoning. (**definitional**) — a term's meaning.
(**consensus**) — standard across current textbooks and national guidance. (**country-dependent**)
— differs between countries or institutions, and yours is the authority. The Pokémon claims are
not marked this way; they are listed in the `## Sources` section with the file they were checked
against.

## Two lesions, and the one that moves is the one that is behaving normally

```
   WEAL AND ANGIOEDEMA
   ==================================================================================

   FEATURE             WEAL (URTICARIA)             ANGIOEDEMA
   =================   ==========================   ===========================
   compartment         superficial dermal oedema    deeper -- lower dermis,
                                                    subcutis, submucosa
   =================   ==========================   ===========================
   what it feels       ITCHY, sometimes burning     tense, often PAINFUL or
   like                                             tingling; usually NOT itchy
   =================   ==========================   ===========================
   duration of ONE     minutes to hours; by         hours to days -- commonly
   lesion              definition resolving         one to three days, and it
                       within about a day, leaving  may be longer
                       normal skin
   =================   ==========================   ===========================
   does it move        yes -- migratory, and that   no -- it swells and subsides
                       is part of the definition    in place
   =================   ==========================   ===========================
   sites               anywhere                     lips, periorbital, tongue,
                                                    pharynx and larynx, hands,
                                                    feet, genitals, bowel wall
   ==================================================================================
   THE OBSERVATIONS THAT MEAN IT IS SOMETHING ELSE
   ==================================================================================
   one lesion lasting more than about a day; pain rather than itch; bruising or
   staining as it fades; fever, joint pain or feeling unwell; raised inflammatory
   markers. Those point AWAY from ordinary urticaria -- towards urticarial
   vasculitis or an autoinflammatory syndrome, and towards a biopsy.
```

## Rain lasts five turns. If it is still raining, something else set it

`Cmd_setrain` gives rain a counter, and `DoFieldEndTurnEffects` decrements it every turn and ends
the weather at zero. Five turns. That is the whole of what **Rain Dance** buys.

Unless an ability set it. When **Kyogre**'s **Drizzle** puts the rain up, the code sets the
permanent bit alongside the temporary one, and the end-of-turn branch reads `if (!(gBattleWeather
& B_WEATHER_RAIN_PERMANENT))` before it touches the counter. **The countdown is skipped
entirely.** Rain that has not stopped after five turns was not set by Rain Dance.

A weal is the five-turn timer. It appears, it migrates, and by definition it is gone inside about
a day leaving normal skin. **A lesion that is still in the same place tomorrow is not a weal**,
and that single observation redirects the entire assessment — which is the diagnostic value of a
timer you know the length of.

## Each Sandstorm tick is a complete transient event, and the disease is the setter

**Tyranitar**'s **Sand Stream** is its only listed ability, and it sets a Sandstorm with the
permanent bit up. `Cmd_weatherdamage` then costs each exposed battler **maximum HP divided by
sixteen** at the end of every turn, with a floor of 1. Every tick is a fresh, complete, transient
event. Not one of them is the problem.

That is chronic urticaria, and it is why hunting for what caused *today's* weal is usually the
wrong question:

```
   THE MISCONCEPTION THAT COSTS THE MOST TIME
   ==================================================================================
   "Chronic urticaria means we have to find the allergy."
   ==================================================================================
   In chronic spontaneous urticaria an external allergen is usually NOT the cause.
   A large share of it involves autoantibodies directed at the IgE receptor or at
   IgE itself, activating mast cells with no allergen present at all -- the setter
   is standing on the field. Extensive allergy testing without a history pointing
   to an allergen has a poor yield and generates false leads that restrict diets
   for no benefit. The recommended investigation is minimal: history and
   examination do most of it, with a small number of basic tests and more only
   where the history asks. What tests, and how many, is set by your national
   guidance.
   ==================================================================================
   AND THE DEVICE THAT REPLACES IT: m004's DAMP ROCK
   ==================================================================================
   A Damp Rock -- a FOURTH-generation item, so pin the generation when you use it --
   makes rain last eight turns instead of five. It makes no rain. Heat, alcohol,
   non-steroidal anti-inflammatory drugs, tight clothing, stress, exercise and
   intercurrent infection all make existing urticaria worse. Removing them improves
   the disease and does not cure it, because none of them set it going.
   AGGRAVATING FACTORS ARE NOT CAUSES.
```

The weal itself is mast cell activation in the dermis: histamine and other mediators dilate
vessels, increase permeability so fluid enters the interstitium, and stimulate sensory nerves —
redness, swelling and itch, which is why all three arrive together. The shallow compartment is why
it itches and why it goes: a small volume of fluid in a thin space is reabsorbed quickly.
(**mechanism**)

Three routes reach that same activation. An allergen cross-linking IgE, which is mostly **acute**
urticaria with a clear exposure. Direct activation by some drugs, including opioids and
radiocontrast media. And non-steroidal anti-inflammatory drugs by a different route again, through
altered arachidonic acid metabolism — which is why they aggravate chronic urticaria in a
substantial proportion of the people who have it without being its cause.

## Will-O-Wisp is the inducible urticaria, and its script is the differential

**Will-O-Wisp** has accuracy 75, power 0, 15 PP, and a `secondaryEffectChance` of **zero** —
because the burn is not a secondary effect. Its script calls `setmoveeffect MOVE_EFFECT_BURN`
followed by `seteffectprimary`. Compare **Flamethrower**: power 95, accuracy 100, and a
`secondaryEffectChance` of 10. One move burns as its purpose; the other burns sometimes.

The inducible urticarias are Will-O-Wisp. Stroking the skin produces linear weals in symptomatic
dermographism; cold contact, sustained pressure with a delay, sunlight, heat, vibration, water and
a rise in core temperature each define their own form. Apply the stimulus and the lesion appears,
reliably, which is why **the provocation test is the diagnosis** — the one part of urticaria that
a bedside test settles. Chronic spontaneous urticaria is the opposite: there is no move to name.

And the script around that one line is the most useful list in this answer, because it is eight
ordered reasons for the same move to produce nothing:

```
   BattleScript_EffectWillOWisp, IN ORDER, AND WHAT EACH CHECK MEANS
   ==================================================================================

   THE CHECK IN THE SCRIPT                 WHY THE SAME MOVE DOES NOTHING
   =====================================   ==========================================
   jumpifstatus2 SUBSTITUTE                there is a barrier in the way
   =====================================   ==========================================
   jumpifstatus BURN (already burned)      the state is already present
   =====================================   ==========================================
   jumpiftype TYPE_FIRE                    constitutionally not susceptible
   =====================================   ==========================================
   jumpifability WATER_VEIL                a standing property blocks this one
                                           specific thing
   =====================================   ==========================================
   jumpifstatus STATUS1_ANY                a DIFFERENT state occupies the slot --
                                           one condition at a time
   =====================================   ==========================================
   accuracycheck                           it simply missed: 75, not 100
   =====================================   ==========================================
   jumpifsideaffecting SAFEGUARD           a side-level protection, checked HERE, in
                                           the move's own script
   ==================================================================================
   And the one that is NOT in the list: SHIELD DUST. The Shield Dust clause in
   SetMoveEffect requires the effect to be non-primary, and Will-O-Wisp's burn is
   primary. Shield Dust therefore does not stop it, while Safeguard does -- because
   somebody wrote the Safeguard check into this script and could not write a
   Shield Dust one. Two protections, one blocks this move and one does not, and the
   difference is only where the check lives. Which is exactly the shape of
   "an antihistamine covers the histamine route and nothing else".
```

Two of those checks are worth naming in full, because they are different kinds of defence and the
clinical differential for a swelling has both. A **Substitute** is a barrier in the way — a
physical obstacle, costing its holder maximum HP divided by four to build. **Water Veil** is a
standing property of the species that blocks this one specific state and nothing else, which is
what a pathway-specific protection looks like. A swelling that an antihistamine does not touch is
not a Substitute problem; it is a Water Veil problem, and the question is which state you are
actually trying to cause.

## The swelling that does not move: two pathways, one of them a zero

```
   THE DISCRIMINATION, IN THE ORDER IT IS USEFUL
   ==================================================================================

   ASK                                   MAST-CELL      BRADYKININ
   ===================================   ============   ===========================
   are there weals as well?              usually yes    NO -- the single most
                                                        useful question there is
   ===================================   ============   ===========================
   is it itchy?                          often          no
   ===================================   ============   ===========================
   how fast?                             minutes to     hours
                                         an hour or
                                         two
   ===================================   ============   ===========================
   how long?                             hours          often one to three days or
                                                        more
   ===================================   ============   ===========================
   abdominal attacks?                    no             yes, and they are often
                                                        investigated for years as
                                                        something else
   ===================================   ============   ===========================
   family history?                       no             often, in the hereditary
                                                        forms
   ===================================   ============   ===========================
   on an ACE inhibitor?                  irrelevant     ASK -- and ask how long for,
                                                        because the delay to the
                                                        first attack can be years
   ===================================   ============   ===========================
   does an antihistamine help?           yes            NO. Earthquake into Flygon.
                                                        Mechanism, not dose
   ==================================================================================
```

Bradykinin-mediated angioedema is a different pathway, not a worse version of the same one. Excess
bradykinin increases vascular permeability, and the picture follows the mechanism: no weals, no
itch, slower onset over hours, longer duration, frequent abdominal attacks from bowel wall
involvement, sometimes a preceding tingling or a non-itchy marbled rash, and often a family
history. The causes are angiotensin-converting-enzyme inhibitors — which reduce bradykinin
breakdown, and where the first attack may come months or years after starting, which is the
commonest reason the link is missed — and hereditary or acquired deficiency of C1 inhibitor.

Antihistamines, corticosteroids and adrenaline do not act on that pathway. (**consensus**) The
specific treatments are different in kind: C1 inhibitor replacement, a bradykinin receptor
antagonist and a plasma kallikrein inhibitor are the classes involved, and which agents are
available, licensed and funded is firmly (**country-dependent**). No agent or dose is named here.
What matters at this level is that the airway risk is real, the treatment is pathway-specific, and
people with the hereditary form are managed by a specialist service with an individual plan that
is the authority in an attack.

## Treatment, at the level of principle

Urticaria is divided by duration, conventionally at six weeks, into acute and chronic, and chronic
into spontaneous and inducible. (**definitional**) The mainstay is a non-sedating
H1-antihistamine, with national guidance describing up-titration beyond the standard licensed
amount under specialist advice where the response is inadequate — the multiples, the licensing
position and who may do it are (**country-dependent**) and live in your guidance and formulary,
not here. The older sedating antihistamines are generally avoided for maintenance because of their
effects on sleep architecture, cognition and driving. Long-term systemic corticosteroids are not a
treatment for chronic urticaria, though a short course has a place in a severe flare in some
guidance. Beyond that are specialist escalations including an anti-IgE monoclonal antibody, with
availability differing by country.

For the bradykinin pathway the principle inverts: identify the pathway, stop the responsible drug
where there is one, and use a pathway-specific treatment through a service holding that person's
plan. Escalating the thing that was always a zero is the error the whole answer exists to prevent.

## Where the metaphor stops

No Pokémon in this section.

**Anaphylaxis is the emergency and it is defined by what is happening beyond the skin.** Urticaria
with any of airway compromise, difficulty breathing, wheeze, stridor, hoarseness, tongue or throat
swelling, a sense of the throat closing, collapse, or low blood pressure is anaphylaxis until
proven otherwise, and the response is immediate adrenaline given by someone trained to give it,
emergency services, and nothing that delays either. Intramuscular adrenaline is the first-line
treatment for anaphylaxis in every mainstream guideline, and antihistamines are not a substitute
for it. The doses and the devices are in your resuscitation council's guidance and your formulary
and they are not in this answer. Skin signs can be absent in anaphylaxis, which is why their
absence does not exclude it.

**Laryngeal angioedema is an airway emergency whichever pathway caused it**, and in the
bradykinin-mediated forms the drugs that work for anaphylaxis will not reverse it, so the airway
has to be secured and a pathway-specific treatment given. People with hereditary C1 inhibitor
deficiency are usually given written plans and medication to carry, and that plan is the authority
in an attack.

**And the chronic disease is not trivial.** Chronic urticaria is itchy day and night, disrupts
sleep, is visible, and is frequently dismissed as a rash. People commonly arrive having eliminated
most of their diet on the basis of a test result that never meant what they were told it meant,
and part of the consultation is undoing that. Angioedema of the face does not look like a minor
problem to the person who has it, or to anyone who sees them. None of that is written here to be
affecting; it is written because it changes what the consultation has to contain.

Without softening: nothing here is for any reader's own use and no treatment named here is a
recommendation. Anyone with swelling of the lips, tongue, mouth or throat, any difficulty
breathing or swallowing, a hoarse voice with swelling, or a feeling that the throat is closing,
needs emergency help immediately — call your local emergency number. Anyone with recurrent
swelling without weals, or with unexplained recurrent abdominal pain and swellings, needs
assessment for the bradykinin-mediated causes rather than more antihistamine.

## What a Gym Leader is listening for

How long one weal lasts, and what it means if a lesion is still there the next day — the five-turn
timer, and what it tells you when the rain has not stopped. Why the itch, the redness and the
swelling arrive together. Why extensive allergy testing in chronic spontaneous urticaria is
unhelpful. The difference between an aggravating factor and a cause, which is the Damp Rock point
and it makes no rain. Where the six-week line falls. Why the inducible urticarias are the ones a
bedside test settles — the effect is in the move's own data. The single most useful question
separating the two angioedema pathways. Why an antihistamine fails against bradykinin-mediated
angioedema, phrased as mechanism and not as dose. Why the first attack on an ACE inhibitor can be
years after starting it. And what makes a presentation anaphylaxis rather than urticaria.

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-dermatology.md`](../../../for-agents/SOURCES-dermatology.md),
and they are the authority for everything procedural or quantitative here. Specific to this
answer:

* For the classification of urticaria, the recommended investigation, the treatment ladder and any
  up-titration of antihistamine: the urticaria guidance used where you practise — an international
  consensus guideline exists and is widely adopted, and national bodies issue their own versions
  that differ in the detail. Yours is the authority.
* For anaphylaxis — recognition, the drug, the route, the doses, the devices and the follow-up:
  your national resuscitation council's guidance and your national formulary. This answer
  deliberately contains no dose.
* For hereditary and acquired C1 inhibitor deficiency — diagnosis, the specific treatments,
  prophylaxis and the individual action plan: your national immunology or specialist angioedema
  service, which is where these patients are managed and where the plan lives.
* For any medicine named or implied, including the antihistamines, the anti-IgE monoclonal
  antibody and the angioedema-specific agents: your national formulary.
* For drug-induced angioedema and drug causes of urticaria: your national formulary's adverse
  effect entries, and this domain's m054 for the drug eruption reasoning.
* For urticarial vasculitis and the autoinflammatory syndromes: a current standard textbook of
  dermatology, and your national rheumatology or immunology pathway.

The Pokémon claims were checked separately against source. Refresh being Normal-type with power 0,
accuracy 100, 20 PP and a user target, and its battle script calling
`cureifburnedparalyzedorpoisoned` with a branch to `BattleScript_ButItFailed`; `Cmd_typecalc`
writing `TYPE_MUL_NO_EFFECT` for a Ground move against a Levitate holder, and Flygon listing
Levitate in both ability slots; rain from Rain Dance running on a counter that
`DoFieldEndTurnEffects` decrements, with the end-of-turn branch testing `!(gBattleWeather &
B_WEATHER_RAIN_PERMANENT)` so that ability-set weather skips the countdown entirely; Kyogre's
Drizzle setting the permanent bit alongside the temporary one; Tyranitar's Sand Stream being its
only listed ability; `Cmd_weatherdamage` costing maximum HP divided by sixteen with a floor of 1;
Will-O-Wisp having accuracy 75, power 0, 15 PP and a `secondaryEffectChance` of 0, with its script
applying the burn through `setmoveeffect MOVE_EFFECT_BURN` and `seteffectprimary` after checking
Substitute, an existing burn, Fire typing, Water Veil, any other status, accuracy and Safeguard in
that order; Flamethrower having power 95, accuracy 100 and a `secondaryEffectChance` of 10; and
the Shield Dust clause in `SetMoveEffect` applying only to non-primary effects, so that it does
not block a primary burn; Water Veil preventing a burn, which is what that script's
`jumpifability` branch exists for; and Substitute costing maximum HP divided by four — all from
the pret decompilation of Pokémon Emerald. The Damp Rock is a fourth-generation item and is named
here as such; it is not in the third-generation code and the eight-turn figure is its established
use in this domain's m004 rather than something read out of the Emerald source.

## Scope and safety

Revision material for someone already training in or qualified for the field. Not a clinical
reference, not a decision aid, and not reviewed by a clinician. It is not for use in making a
decision about anyone's care, including your own.

**No dose, agent, device, up-titration multiple or treatment schedule appears in this answer, and
none of it addresses any reader's own treatment.** The absence of the adrenaline dose is
deliberate: anaphylaxis treatment is set by your resuscitation council and your formulary, the
figures differ by age and by device, and a number quoted here without its document would be
dangerous rather than helpful.

Swelling of the lips, tongue, mouth or throat, difficulty breathing or swallowing, a hoarse voice
with swelling, stridor, collapse, or a feeling that the throat is closing, is a medical emergency
— call your local emergency number. Someone with a prescribed adrenaline auto-injector and an
individual action plan should follow that plan, which was written for them and which overrides
anything general.

Local guidance and the policy where you practise are the authority on all of this, and they differ
by country and by institution.

## Where this stands, October 2026

The mechanisms and the discrimination between the two angioedema pathways are settled and are the
part worth memorising. What moves is the treatment ladder. The internationally adopted urticaria
guideline has been revised several times, and the position on up-titration, on the sequencing of
specialist agents and on the role of short corticosteroid courses has changed between revisions,
so the edition matters. Several newer agents acting on mast cell signalling have been in
late-stage development for chronic spontaneous urticaria and the licensed landscape is likely to
look different within a few years. In hereditary angioedema the options have expanded
substantially over the last decade, including long-term prophylaxis by different routes, and
access varies sharply by country. The understanding of chronic spontaneous urticaria as
substantially autoimmune has strengthened rather than reversed. Refresh has covered the same three
conditions, and failed outright against the other two, throughout the third generation. Current as
of October 2026.
