# TERMINOLOGY

A glossary for reading the Pokémon answers in `answers/pokemon/`.

## Who this is for

You know the machine learning. You do not know Pokémon, or you played one game
twenty years ago and remember that there was a mouse.

That is a real problem for this dataset, because the Pokémon answers deliberately
never break the metaphor to explain themselves. A line like *"eight coaches sharing
one notebook"* is doing precise technical work — it is grouped-query attention — and
you cannot check whether the analogy is honest if you do not know what a notebook is
doing in a Pokémon battle in the first place.

This file exists so you can. It is not a Pokémon encyclopedia. **Every term below
actually appears in `answers/pokemon/`**, and the entries say which question uses it
and what it is standing in for. Terms that never appear are not here, however famous
they are.

## How to use it

* Reading one answer? Skim [Core concepts](#core-concepts) and
  [Battling](#battling) once, then look up species as you hit them.
* Reading the whole set? The section that actually unlocks the dataset is
  [Recurring analogy conventions](#recurring-analogy-conventions). The answers reuse a
  stable vocabulary across every question in the set — the wild grass is *always*
  pretraining, a held item is *always* a LoRA adapter — and once you have that mapping,
  the answers read as a single consistent system rather than a pile of separate jokes.
* Checking an answer's honesty? Cross-reference the mapping table against
  `answers/serious/` for the same id. Both answers describe the same reality; that is
  the whole premise.

Every question id in this file is a **link**: [`007`](answers/pokemon/007-transformer-feed-forward-block.md) opens
`answers/pokemon/007-transformer-feed-forward-block.md`, because this glossary exists to
help you read the Pokémon answers. The serious counterpart is always the same filename
under `answers/serious/` — swap the directory in the URL.

---

## Core concepts

**Pokémon.** A creature you catch, raise and battle with. Each one has a species (its
kind), a level, six numeric stats, one or two elemental **types**, up to four **moves**,
one **ability**, and optionally one **held item**. In the dataset a Pokémon is usually
the model itself, or one token in a sequence, depending on the question.

**Trainer.** The human who owns and directs the Pokémon. Trainers do not act on the
field; they issue orders and their Pokémon carry them out. This split matters enormously
in [`054`](answers/pokemon/054-tool-calling.md), where it becomes the model-versus-harness boundary.

**Type.** Every Pokémon and every attacking move has an elemental type — Fire, Water,
Grass, Electric, Rock, Ground, Steel, Flying, Dragon, Ghost, Fairy, Bug, Fighting,
Normal, Psychic, Poison, Ice, Dark. A Pokémon may have two types at once, written
`Water/Flying`. Both of its types apply when it is being attacked.

**Type chart / type effectiveness.** A fixed lookup table saying how much damage each
attacking type does to each defending type. The multipliers are:

| Result | Multiplier | Example from the dataset |
| --- | --- | --- |
| Super effective | 2× | Electric into Water |
| Doubly super effective | 4× | Electric into Water/Flying (Gyarados) — both types are weak |
| Neutral | 1× | most matchups |
| Not very effective | 0.5× | Electric into Grass (Ferrothorn) |
| Doubly resisted | 0.25× | both types resist |
| No effect / immunity | 0× | Electric into Ground (Golem) — literally nothing happens |

The 4× and 0× cases are load-bearing throughout the dataset, because they are the two
extremes an attention distribution needs ([`001`](answers/pokemon/001-attention-mechanisms.md)), the cliff a pass/fail benchmark hides
([`015`](answers/pokemon/015-emergent-abilities.md)), and the arithmetic a chain of thought has to actually perform ([`049`](answers/pokemon/049-chain-of-thought.md)).

**Party.** The six Pokémon a Trainer carries, in a fixed order. Slot 1 is sent out
first. The order is strategy, not decoration.

**PC box.** Storage at a Pokémon Center holding everything not in your party —
thousands of Pokémon, unordered, and requiring a trip to reach. The dataset uses it two
ways: as an unordered set with no notion of position ([`002`](answers/pokemon/002-positional-encodings-rope.md)), and as large, slow,
far-away memory as opposed to the six fast slots on your belt ([`010`](answers/pokemon/010-flash-attention.md)).

**HP (hit points).** A Pokémon's health. At zero it **faints** and can no longer battle.

**Fainting.** Being knocked out. A **KO** is causing this. "Did the Gyarados faint?" is
the dataset's stock example of a fact you can simply check rather than have graded
([`023`](answers/pokemon/023-grpo-reasoning.md), [`038`](answers/pokemon/038-llm-as-a-judge.md)).

**Moves.** The four attacks or effects a Pokémon knows. Four is a hard cap: to learn a
fifth, one must be forgotten, and the game asks you which. [`006`](answers/pokemon/006-residual-connections.md) builds residual
connections out of the fact that you are *allowed to say no*; [`026`](answers/pokemon/026-catastrophic-forgetting.md) builds catastrophic
forgetting out of a hypothetical version where the game never asks.

**PP (power points).** Each move has a limited number of uses per trip, refilled at a
Pokémon Center. Appears once, in [`001`](answers/pokemon/001-attention-mechanisms.md), as the resource that runs out when you try to
compare everyone on the field to everyone else.

**Ability.** A passive trait, one per Pokémon, that changes the rules for it
specifically — see the abilities table below. Abilities are the reason a coach whose
only skill is the type chart gets ambushed ([`001`](answers/pokemon/001-attention-mechanisms.md), [`003`](answers/pokemon/003-multi-head-attention.md)).

**Held item.** One object a Pokémon carries into battle, granting a persistent effect.
Small, swappable, and it does not change the Pokémon. This is the dataset's single most
reused mapping: a held item is a LoRA adapter ([`026`](answers/pokemon/026-catastrophic-forgetting.md), [`027`](answers/pokemon/027-lora.md), [`028`](answers/pokemon/028-qlora.md), [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md)).

**Level.** 1 to 100. Higher levels mean higher stats. Levels are gained by battling, or
bought outright with Rare Candy — the tradeoff [`014`](answers/pokemon/014-scaling-laws.md) is built on.

**EVs (effort values).** Hidden training points a Pokémon accumulates by battling, which
raise specific stats. "EV-trained" means deliberately conditioned rather than merely
levelled ([`005`](answers/pokemon/005-layer-normalization.md), [`047`](answers/pokemon/047-query-rewriting-hyde.md)).

**Evolution.** A permanent transformation into a different, usually stronger species,
triggered by level, item or condition. It is discrete: nothing, nothing, nothing, then a
different creature. [`015`](answers/pokemon/015-emergent-abilities.md) uses it as the image of a genuine phase transition, and then
spends the rest of the answer arguing that most claimed emergence is a badly chosen
metric rather than a real evolution.

**Rare Candy.** An item granting one level instantly, with none of the experience that
normally comes with it. Pure scale, no substance. [`014`](answers/pokemon/014-scaling-laws.md) makes it parameters, and battles
the training tokens.

**Releasing a Pokémon.** Permanently letting one go. It is irreversible and there is no
undo, which is why [`055`](answers/pokemon/055-model-context-protocol.md) and [`059`](answers/pokemon/059-prompt-injection.md) use it as the archetypal action a tool or an agent must
never be allowed to take unsupervised.

**Nickname.** A Pokémon can be renamed to anything. [`012`](answers/pokemon/012-tokenization-bpe.md) uses a Charizard nicknamed
"Big Steve" to show why a vocabulary of whole names cannot work.

---

## Battling

**Turn.** Both sides choose an action, then both resolve. Battles in the dataset run
anywhere from 6 turns ([`038`](answers/pokemon/038-llm-as-a-judge.md)) to a hypothetical 400 ([`013`](answers/pokemon/013-context-length-limits.md)).

**Single vs Double Battle.** In a Single Battle one Pokémon per side is out. In a
**Double Battle** two per side are out simultaneously, so a move must choose a target
among several. [`001`](answers/pokemon/001-attention-mechanisms.md) opens with a Double Battle precisely because attention needs more
than one candidate to attend to.

**Switching.** Swapping the active Pokémon for one from your party. Costs your action
for the turn. Switch loops — in, out, in, out — are the dataset's picture of an agent
that never terminates ([`053`](answers/pokemon/053-react-agents.md)) and of exposure-bias drift ([`017`](answers/pokemon/017-teacher-forcing-exposure-bias.md)).

**Weather.** A field condition lasting several turns, usually set by an ability or a
move. **Rain** boosts Water moves and makes some abilities live; **sun** boosts Fire.
Weather teams are built entirely around it: [`016`](answers/pokemon/016-next-token-prediction.md) and [`051`](answers/pokemon/051-in-context-learning.md) both use "Politoed sets
rain, Swift Swim Kingdra sweeps" as an example of a plan you have to have been following
to predict the next move.

**Entry hazards.** Effects laid on the opponent's side that damage Pokémon as they
switch in. **Stealth Rock** is the famous one: floating stones that hurt anything
entering, scaled by its Rock weakness — so a 4×-weak Charizard loses half its HP just by
appearing. In [`001`](answers/pokemon/001-attention-mechanisms.md) it is the thing an RNN forgot nine turns ago; in [`007`](answers/pokemon/007-transformer-feed-forward-block.md) it is a fact
the Pokédex knows about Charizard.

**Setup moves.** Moves that boost your own stats instead of attacking — **Swords Dance**
sharply raises Attack. Setup is only worth it when you can afford the turn. [`019`](answers/pokemon/019-rlhf-end-to-end.md) uses
"Swords Dance six times against a Magikarp" as its picture of reward hacking: locally
adored by the judge, catastrophic in the match.

**Protect.** A move that blocks everything aimed at you for one turn. Cannot be relied
on repeatedly.

**Substitute.** A move that spends some of your own HP to put up a decoy that absorbs
attacks.

**Trick Room.** A move that inverts the speed order for five turns, so the slowest
Pokémon moves first. Whole teams are built around it — the Bronzong-and-Rhyperior team
in [`051`](answers/pokemon/051-in-context-learning.md) is a textbook one. Recognising a Trick Room team from its roster is the example
[`004`](answers/pokemon/004-encoder-decoder-vs-decoder-only.md) uses for what an encoder-only model is good at.

**Win condition.** The specific route by which a team plans to win. Identifying the
opponent's win condition is the multi-hop reasoning task in [`013`](answers/pokemon/013-context-length-limits.md) and the strategic
inference in [`016`](answers/pokemon/016-next-token-prediction.md).

**Metagame.** The prevailing set of popular teams and counters at a given moment. It
drifts, which is why [`020`](answers/pokemon/020-dpo-vs-ppo.md) warns that a two-year-old collection of preference cards
trains you for last season.

**Flat Rules / Level 50.** A common competitive format that sets every Pokémon to Level
50 regardless of its actual level, so matches are decided by team and play rather than
by grinding. [`005`](answers/pokemon/005-layer-normalization.md) makes this layer normalization, and the analogy is exact: the
rescaling looks only at the one Pokémon in front of it, and it destroys the advantage of
one runaway number.

**Banned move / banlist.** Competitive formats forbid certain moves and Pokémon outright.
[`060`](answers/pokemon/060-jailbreaks.md) uses "never use a banned move" as the trained rule a jailbreak is trying to talk the
Pokémon past — and notes that a banned move is far easier to recognise *after* the fact
than a sneaky request is beforehand.

**Team sheet.** The declared list of your six Pokémon, their items and their moves, shown
to the opponent before a competitive match. [`004`](answers/pokemon/004-encoder-decoder-vs-decoder-only.md) uses it for what an encoder sees all at
once; [`056`](answers/pokemon/056-multi-agent-systems.md) and [`059`](answers/pokemon/059-prompt-injection.md) use it as the shared state two agents must not both write to, and as
the secret an injected instruction wants to exfiltrate.

**Regulation G.** A named ruleset for one season of official competitive play. Appears
once, in [`047`](answers/pokemon/047-query-rewriting-hyde.md), as an example of a query that is too specific to retrieve against.

**Tier (S / A / F).** Community shorthand ranking teams or Pokémon from best (S) to
useless (F). [`051`](answers/pokemon/051-in-context-learning.md) uses tier letters as the label set for a few-shot classification task.

---

## The world and progression

**Gym.** A themed challenge building, usually specialising in one type. Beat it and you
get a badge. Gyms are stops on a fixed circuit, which is why [`005`](answers/pokemon/005-layer-normalization.md) and [`006`](answers/pokemon/006-residual-connections.md) use "a Gym"
to mean one layer of a deep network and "the League" to mean the stack.

**Gym Leader.** The specialist who runs a Gym. Each is a genuine expert in exactly one
type and nothing else, which is what makes them the experts in [`011`](answers/pokemon/011-mixture-of-experts.md)'s Mixture-of-Experts.

**Badge.** The token you get for beating a Gym. Eight badges qualify you for the Elite
Four. In [`037`](answers/pokemon/037-evaluating-llms.md) and [`039`](answers/pokemon/039-benchmark-contamination.md) the eight badges are public benchmarks — standardised,
comparable, and thoroughly leaked.

**Gym Circuit.** The dataset's collective name for the eight badges taken as an exam
([`037`](answers/pokemon/037-evaluating-llms.md), [`039`](answers/pokemon/039-benchmark-contamination.md)).

**Elite Four.** Four consecutive high-level Trainers you must beat back to back, with no
healing between them, after collecting all eight badges.

**Champion.** The final opponent, above the Elite Four, and the strongest Trainer in the
region. Throughout the dataset "Champion" means the large, expensive, strong model, in
contrast to the **rookie** ([`031`](answers/pokemon/031-knowledge-distillation.md), [`033`](answers/pokemon/033-speculative-decoding.md)) — and "the Champion's feedback reaching your
starter" is backpropagation through a deep stack ([`005`](answers/pokemon/005-layer-normalization.md), [`006`](answers/pokemon/006-residual-connections.md)).

**Victory Road.** The long, linear, one-way gauntlet leading to the Elite Four. [`001`](answers/pokemon/001-attention-mechanisms.md)
uses it for strictly sequential processing: Pokémon 1, then 2, then 3, and by the end you
have forgotten why.

**Route.** Numbered stretches of land between towns. **Route 1** is the very first, home
to the weakest wild Pokémon. [`006`](answers/pokemon/006-residual-connections.md) puts "the Route 1 tutor who taught your Charmander to
Scratch" at the far end of the gradient path.

**Pewter City.** The town with the first Gym, Brock's ([`016`](answers/pokemon/016-next-token-prediction.md), [`039`](answers/pokemon/039-benchmark-contamination.md)).

**Kanto, Johto, Hoenn, Sinnoh, Unova, Kalos.** The regions of successive games. [`044`](answers/pokemon/044-vector-databases-ann.md)
uses them purely as named spatial partitions of a map — the clusters of an IVF index.

**Tall grass / wild encounters.** Walking through grass triggers battles with wild,
untrained, unowned Pokémon. Nobody supervises this and nobody grades it. In this dataset
the wild grass is **always** pretraining ([`018`](answers/pokemon/018-pretraining-sft-rlhf.md), [`019`](answers/pokemon/019-rlhf-end-to-end.md), [`025`](answers/pokemon/025-instruction-tuning.md), [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md), [`036`](answers/pokemon/036-perplexity.md), [`040`](answers/pokemon/040-hallucination.md)).

**Pokédex.** The in-game encyclopedia listing every species, its types, and its
behaviour. The dataset's most heavily reused prop — see
[One term, several jobs](#one-term-several-jobs), because it does three different jobs.

**Pokémon Center.** A free clinic in every town that fully heals your party, and where
the PC boxes live. In [`043`](answers/pokemon/043-embeddings.md) "how do I heal my Pokémon?" versus "where can I restore HP?"
is the canonical pair of queries with zero words in common and identical meaning.

**Poké Ball.** The device used to catch and carry a Pokémon. [`002`](answers/pokemon/002-positional-encodings-rope.md) numbers them, then
spins them, to build up absolute versus rotary positional encoding. [`055`](answers/pokemon/055-model-context-protocol.md) makes the ball
itself the standard: one design that works with every species, maintained by the species
rather than by each Trainer — the Model Context Protocol. A **Master Ball** is
the unique, never-fails, single-use version — [`054`](answers/pokemon/054-tool-calling.md)'s example of an irreversible action a
tool harness must guard.

**Fly.** A move that transports you instantly between towns you have already visited —
a sparse network of long-range shortcuts layered over the map you otherwise have to walk.
[`044`](answers/pokemon/044-vector-databases-ann.md) maps it directly onto HNSW.

**TM (Technical Machine).** A consumable disc that teaches a move, identified by number
(`TM24`, `TM25`). The dataset uses TM identifiers as its running example of an **exact
code**: strings where semantic similarity is actively wrong, because `TM24` and `TM25`
are neighbours on the map and unrelated in fact ([`043`](answers/pokemon/043-embeddings.md), [`045`](answers/pokemon/045-hybrid-search-reranking.md), [`047`](answers/pokemon/047-query-rewriting-hyde.md)).

**Potion / Super Potion / Antidote / Full Heal.** Healing items. A Potion restores HP; an
Antidote or Full Heal cures status conditions instead. [`054`](answers/pokemon/054-tool-calling.md) uses the distinction to show
that a tool description must say *when not to* use the tool.

**Daycare.** In the games, a facility that raises Pokémon for you. In [`037`](answers/pokemon/037-evaluating-llms.md) and [`039`](answers/pokemon/039-benchmark-contamination.md) it
is a deliberately mundane job — *"you got all eight badges; you run a daycare"* — standing
for your actual production use case, which no public benchmark measures.

---

## Species named in the dataset

Only species that actually appear in `answers/pokemon/` are listed. The last column is
the point: why this particular creature and not another.

| Species | Type(s) | What it is | Why the dataset uses it |
| --- | --- | --- | --- |
| **Pikachu** | Electric | The mascot; a small Electric mouse, the default protagonist's Pokémon | The stand-in for "your model" whenever an answer needs a concrete actor. Its Thunderbolt against Water types is the dataset's canonical 4× matchup ([`001`](answers/pokemon/001-attention-mechanisms.md), [`049`](answers/pokemon/049-chain-of-thought.md)) |
| **Raichu** | Electric | Pikachu's evolution | Appears only in [`043`](answers/pokemon/043-embeddings.md), as an obviously-near-neighbour of Pikachu on the embedding map |
| **Gyarados** | Water/Flying | A huge sea serpent; Magikarp's evolution | The dataset's universal attention target: Water/Flying is **4× weak to Electric**, the single most extreme non-zero multiplier on the chart. Used in 18 questions |
| **Magikarp** | Water | Famously useless — a flopping fish whose only move is Splash — until it evolves into Gyarados at level 20 | The emergence and phase-transition example ([`015`](answers/pokemon/015-emergent-abilities.md)). Also the floor of usefulness generally: "six Magikarp" is an F-tier team ([`051`](answers/pokemon/051-in-context-learning.md)), and you cannot distil a Champion into one ([`031`](answers/pokemon/031-knowledge-distillation.md)) |
| **Golem** | Rock/Ground | A boulder with limbs | Ground types are **immune to Electric**. Golem is the dataset's 0× case — the thing attention must learn to give no weight at all ([`001`](answers/pokemon/001-attention-mechanisms.md), [`003`](answers/pokemon/003-multi-head-attention.md), [`008`](answers/pokemon/008-kv-cache.md)) |
| **Ferrothorn** | Grass/Steel | A spiked, extremely defensive seed | Resists Water, resists Electric, and is 4× weak to Fire. The dataset's "the field changed, so the spotlight moved" example, and its stock awkward matchup ([`001`](answers/pokemon/001-attention-mechanisms.md), [`013`](answers/pokemon/013-context-length-limits.md), [`017`](answers/pokemon/017-teacher-forcing-exposure-bias.md), [`053`](answers/pokemon/053-react-agents.md)) |
| **Charmander** | Fire | The Fire starter; a small lizard | The beginning of a chain: the thing at the bottom of the network that gradients have to reach ([`005`](answers/pokemon/005-layer-normalization.md), [`006`](answers/pokemon/006-residual-connections.md)) |
| **Charmeleon** | Fire | Charmander's middle evolution | The level-up in [`006`](answers/pokemon/006-residual-connections.md) where the "forget a move?" prompt appears |
| **Charizard** | Fire/Flying | Charmander's final evolution; a dragon-shaped fan favourite | Two properties do the work: it is a **fully evolved** endpoint ([`007`](answers/pokemon/007-transformer-feed-forward-block.md)), and Fire/Flying is 4× weak to Rock, so Stealth Rock halves it on entry |
| **Squirtle** / **Wartortle** / **Blastoise** | Water | The Water starter line | [`043`](answers/pokemon/043-embeddings.md) uses Squirtle and Wartortle as an adjacent pair on the embedding map. [`054`](answers/pokemon/054-tool-calling.md) uses Blastoise as a Pokémon you *do not own* — the hallucinated tool argument |
| **Venusaur** | Grass/Poison | The Grass starter's final form; has a sun-boosted speed ability | Half of the Sun team in [`051`](answers/pokemon/051-in-context-learning.md) |
| **Torkoal** | Fire | A tortoise whose ability automatically summons harsh sunlight | The other half of the Sun team in [`051`](answers/pokemon/051-in-context-learning.md) — it is *why* the team is a Sun team |
| **Politoed** | Water | A frog whose ability automatically summons rain | The enabler of a Rain team ([`016`](answers/pokemon/016-next-token-prediction.md), [`051`](answers/pokemon/051-in-context-learning.md)) |
| **Kingdra** | Water/Dragon | A seahorse that can carry **Swift Swim**, doubling its Speed in rain | The payoff of a Rain team. "Politoed leads, Kingdra sweeps" is a *plan*, which is exactly why [`016`](answers/pokemon/016-next-token-prediction.md) uses it for the kind of prediction that requires strategy rather than recall |
| **Bronzong** | Steel/Psychic | A slow bell-shaped Pokémon that reliably sets Trick Room | Half of the Trick Room team in [`051`](answers/pokemon/051-in-context-learning.md) |
| **Rhyperior** | Ground/Rock | Very slow, very heavy, very strong | The other half: slow attackers are what Trick Room exists to enable |
| **Tapu Fini** | Water/Fairy | A legendary guardian; a common competitive pick | [`047`](answers/pokemon/047-query-rewriting-hyde.md)'s example of a query so specific ("what EV spread does Assault Vest Tapu Fini run in Regulation G?") that no document matches it word for word |
| **Milotic** | Water | An elegant serpentine Water type | [`047`](answers/pokemon/047-query-rewriting-hyde.md)'s resolution of the pronoun "the other one" — the concrete referent a follow-up question needs |
| **Chansey** | Normal | Enormous HP, almost no Defence; a dedicated wall | [`016`](answers/pokemon/016-next-token-prediction.md)'s example of a Pokémon deliberately kept alive at 4 HP for a reason you had to have been watching to know |
| **Skarmory** | Steel/Flying | An armoured bird; another classic defensive wall | [`017`](answers/pokemon/017-teacher-forcing-exposure-bias.md)'s misidentification: the Trainer decides turn 3 that a Ferrothorn is a Skarmory and then plays ten flawless turns against a Pokémon that does not exist |
| **Snorlax** | Normal | Famously huge and heavy; a giant sleeping bear | Two jobs: an unusual thing to run into in the wild ([`018`](answers/pokemon/018-pretraining-sft-rlhf.md)), and the **outlier** — the one entry on the page whose value is 9,000 when everything else is 40–90 ([`030`](answers/pokemon/030-quantization.md)) |
| **Ditto** | Normal | A blob that transforms into whatever it faces; has no real identity of its own | [`043`](answers/pokemon/043-embeddings.md), where it sits alone on the embedding map "being weird" |
| **Alakazam** | Psychic | Enormous Special Attack, paper-thin defences — the archetypal glass cannon | [`086`](answers/pokemon/086-pca.md), as the far end of the "physical bruiser ↔ special sweeper" axis that PCA discovers |
| **Starmie** | Water/Psychic | A fast, fragile Water-type; Misty's signature Pokémon in the anime | [`099`](answers/pokemon/099-ml-system-design.md), as the lead whose meaning inverts when the metagame shifts |
| **Arceus** | Normal | Framed in-universe as the creator of the Pokémon world; the highest total stats in the games | [`086`](answers/pokemon/086-pca.md), as the top of the stat-total range against Magikarp's floor |
| **Eevee** | Normal | A small mammal famous for evolving into many different specialists | [`037`](answers/pokemon/037-evaluating-llms.md), as the mundane real-world case ("a distressed Eevee") that no Gym badge tells you anything about |
| **Flareon** | Fire | One of Eevee's evolutions | [`040`](answers/pokemon/040-hallucination.md) and [`041`](answers/pokemon/041-rag-vs-finetuning.md)'s recall target — a species obscure enough that asking the model to remember a specific detail about it is unreliable, and handing it the page is not. Also the canary string `XQ7-FLAREON-9982` in [`039`](answers/pokemon/039-benchmark-contamination.md) |
| **Growlithe** / **Arcanine** | Fire | A puppy and the large dog it evolves into | [`007`](answers/pokemon/007-transformer-feed-forward-block.md)'s minimum pair: a Pokédex too thin cannot tell them apart |
| **Rattata** | Normal | The weakest, most common early-route wild Pokémon | Low-quality training data. "1,000 real Gym battles beat 10,000 fights against wild Rattata" ([`014`](answers/pokemon/014-scaling-laws.md)); also [`035`](answers/pokemon/035-beam-search.md)'s trivial opponent nobody should plan forty turns against |
| **Zubat** | Poison/Flying | The bat that appears constantly and unwantedly in every cave | Sheer undifferentiated volume, alongside Rattata, in [`018`](answers/pokemon/018-pretraining-sft-rlhf.md)'s wild grass |
| **Onix** | Rock/Ground | A rock snake; Brock's ace, and the first real wall a new player hits | The benchmark itself. "Can it beat Brock's Onix?" is [`015`](answers/pokemon/015-emergent-abilities.md)'s pass/fail cliff and [`039`](answers/pokemon/039-benchmark-contamination.md)'s memorised exam |
| **Bidoof** | Normal | A weak, ubiquitous early-game beaver, affectionately regarded as a joke | The bottom of the range in [`005`](answers/pokemon/005-layer-normalization.md)'s Flat Rules — a Level 12 Bidoof next to a Level 100 Garchomp, rescaled to the same footing |
| **Garchomp** | Dragon/Ground | A pseudo-legendary; genuinely top-tier | The top of that same range |
| **Mew** | Psychic | A mythical Pokémon, and the subject of the most famous fan urban legend in the series ("Mew is under the truck") | [`043`](answers/pokemon/043-embeddings.md)'s obvious non-answer — the easy negative that teaches an embedding model nothing |

---

## People and groups named in the dataset

| Name | Who | Where and why |
| --- | --- | --- |
| **Brock** | Gym Leader of Pewter City; **Rock** type; his ace is Onix | The first Gym, so "beating Brock" is the entry-level benchmark everyone has taken and everyone has memorised ([`015`](answers/pokemon/015-emergent-abilities.md), [`037`](answers/pokemon/037-evaluating-llms.md), [`039`](answers/pokemon/039-benchmark-contamination.md)). Also a Leader on the MoE roster ([`011`](answers/pokemon/011-mixture-of-experts.md)) |
| **Misty** | Gym Leader of Cerulean City; **Water** type | [`011`](answers/pokemon/011-mixture-of-experts.md)'s overworked expert: the receptionist sends everyone to Misty, she gets better, so more go to her, until she is fighting Dragons badly and the other 63 Leaders have forgotten how to battle. The dataset's picture of router collapse |
| **Wallace** | A **Water** specialist — Gym Leader of Sootopolis City, and Champion in one game | [`011`](answers/pokemon/011-mixture-of-experts.md)'s second Water expert, so a challenger can be routed to two of them (top-2 gating) |
| **Blaine** | Gym Leader of Cinnabar Island; **Fire** type | On the [`011`](answers/pokemon/011-mixture-of-experts.md) roster; also the answer's example of the expert specialisation you *hoped* for and did not get |
| **Surge** (Lt. Surge) | Gym Leader of Vermilion City; **Electric** type | On the [`011`](answers/pokemon/011-mixture-of-experts.md) roster |
| **Agatha** | A member of the Elite Four; **Ghost** type | On the [`011`](answers/pokemon/011-mixture-of-experts.md) roster |
| **Lance** | A member of the Elite Four, later Champion; **Dragon** type | On the [`011`](answers/pokemon/011-mixture-of-experts.md) roster |
| **The Elite Four** | The four Trainers between the badges and the Champion | The gauntlet after the grind ([`001`](answers/pokemon/001-attention-mechanisms.md), [`014`](answers/pokemon/014-scaling-laws.md)) |
| **The League** | The whole institution — Gyms, badges, Elite Four, Champion | Used for the model as a whole: "a hundred-Gym League" is a hundred-layer network ([`005`](answers/pokemon/005-layer-normalization.md), [`006`](answers/pokemon/006-residual-connections.md)), and a League of sixty-four Gyms is an MoE ([`011`](answers/pokemon/011-mixture-of-experts.md)) |

---

## Moves, items and abilities named in the dataset

**Moves.** Most appear once or twice, as concrete filler where a real move name lands
better than a placeholder.

| Move | What it does | Where |
| --- | --- | --- |
| Thunderbolt | Strong reliable Electric attack | The dataset's default action, in 20+ answers |
| Thunder | Stronger, less accurate Electric attack; never misses in rain | [`001`](answers/pokemon/001-attention-mechanisms.md), [`031`](answers/pokemon/031-knowledge-distillation.md) — the near-miss that shows a distilled ranking is richer than a label |
| Splash | Does nothing whatsoever; Magikarp's signature | The null action ([`012`](answers/pokemon/012-tokenization-bpe.md), [`031`](answers/pokemon/031-knowledge-distillation.md), [`034`](answers/pokemon/034-sampling-temperature-top-p.md), [`035`](answers/pokemon/035-beam-search.md)) |
| Ember / Flamethrower | Weak and strong Fire attacks | [`006`](answers/pokemon/006-residual-connections.md)'s early and late moveset entries; [`026`](answers/pokemon/026-catastrophic-forgetting.md)'s forgotten Fire move |
| Growl / Leer / Smokescreen / Tackle / Scratch / Bite / Slash / Dragon Rage | Assorted early-game moves | [`006`](answers/pokemon/006-residual-connections.md)'s movesets, kept and rerolled |
| Surf / Waterfall / Aqua Tail / Rain Dance | Water moves | [`026`](answers/pokemon/026-catastrophic-forgetting.md)'s Water-camp curriculum |
| Rock Slide | Rock attack | [`026`](answers/pokemon/026-catastrophic-forgetting.md)'s achievable specialist gain |
| Power Whip | Strong Grass attack; a Ferrothorn staple | [`016`](answers/pokemon/016-next-token-prediction.md) |
| Volt Switch | Attack and switch out in one action | [`034`](answers/pokemon/034-sampling-temperature-top-p.md) |
| Quick Attack | Weak but always moves first | [`053`](answers/pokemon/053-react-agents.md), finishing off a Focus Sash |
| Earthquake | Powerful Ground attack that hits everything | [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md), [`052`](answers/pokemon/052-context-engineering.md) — the thing standing orders tell you not to switch into |
| Dragon Dance | Setup move raising Attack and Speed together | [`058`](answers/pokemon/058-reasoning-models.md), as what the opponent gets for free if your attack leaves them at 1 HP |
| Explosion | Deals huge damage and knocks out the user | [`061`](answers/pokemon/061-guardrails-moderation.md), as the question whose intent is unknowable from its words alone — a curious child, a competitive player and a bad actor all ask it identically |
| Roost | Recovers HP; a Flying-type staple | [`007`](answers/pokemon/007-transformer-feed-forward-block.md), as a Pokédex inference |
| Protect / Substitute / Swords Dance / Trick Room / Stealth Rock / Fly | See [Battling](#battling) and [The world](#the-world-and-progression) | |

**Held items.**

| Item | Effect | Where and why |
| --- | --- | --- |
| **Focus Sash** | Lets the holder survive one otherwise-fatal hit at 1 HP, then is consumed | The hidden fact the type-chart-only coach misses ([`001`](answers/pokemon/001-attention-mechanisms.md), [`003`](answers/pokemon/003-multi-head-attention.md), [`009`](answers/pokemon/009-mqa-and-gqa.md), [`053`](answers/pokemon/053-react-agents.md)) |
| **Leftovers** | Restores a little HP every turn | A stock detail in the battle notebook ([`008`](answers/pokemon/008-kv-cache.md), [`042`](answers/pokemon/042-chunking-strategies.md)) |
| **Damp Rock** | Extends rain by three turns; carried by rain teams | [`027`](answers/pokemon/027-lora.md)'s LoRA adapter — a tiny object that specialises a Champion for wet weather without touching it |
| **Charcoal** / **Magnet** / **Mystic Water** | Each boosts moves of one type | [`011`](answers/pokemon/011-mixture-of-experts.md) and [`027`](answers/pokemon/027-lora.md), as the swappable specialisation |
| **Assault Vest** | Boosts Special Defence but forbids status moves | [`047`](answers/pokemon/047-query-rewriting-hyde.md), inside the too-specific query |

**Abilities.**

| Ability | Effect | Where and why |
| --- | --- | --- |
| **Sturdy** | The holder survives a would-be one-hit KO at 1 HP | The dataset's canonical *second* thing to check. A coach who reads only the type chart walks straight into it ([`001`](answers/pokemon/001-attention-mechanisms.md), [`003`](answers/pokemon/003-multi-head-attention.md), [`009`](answers/pokemon/009-mqa-and-gqa.md)) |
| **Swift Swim** | Doubles Speed in rain | The payoff half of a rain plan ([`016`](answers/pokemon/016-next-token-prediction.md), [`051`](answers/pokemon/051-in-context-learning.md)) |
| **Flash Fire** / **Guts** | Flareon's regular and hidden abilities | [`040`](answers/pokemon/040-hallucination.md), in the question the Trainer is asked to answer from memory |
| **Hidden Ability** | A rarer alternative ability some Pokémon can have | [`040`](answers/pokemon/040-hallucination.md) — chosen because it is exactly the kind of detail that is stored fuzzily |

---

## Not actually Pokémon

Four proper nouns in the dataset look like species and are not.

| Term | What it really is | Where |
| --- | --- | --- |
| **Chinchilla** | The 2022 DeepMind compute-optimal scaling result. The Pokémon answer keeps the paper's name and treats it as a well-battled Level 70 Pokémon | [`014`](answers/pokemon/014-scaling-laws.md) |
| **Gopher** | The larger, under-trained DeepMind model Chinchilla outperformed; here, a "candy-stuffed Lv280" | [`014`](answers/pokemon/014-scaling-laws.md) |
| **SolidGoldMagikarp** | A real undertrained token from GPT-2/GPT-3's vocabulary that caused bizarre model behaviour. The dataset's "cursed tile" | [`012`](answers/pokemon/012-tokenization-bpe.md) |
| **Big Steve** | A nicknamed Charizard, invented for the answer | [`012`](answers/pokemon/012-tokenization-bpe.md) |
| **TM-4471**, `XQ7-FLAREON-9982` | Invented identifiers used as exact-match and canary strings | [`039`](answers/pokemon/039-benchmark-contamination.md), [`045`](answers/pokemon/045-hybrid-search-reranking.md), [`047`](answers/pokemon/047-query-rewriting-hyde.md) |

---

## Recurring analogy conventions

This is the section that makes the dataset legible. These mappings are stable across the
whole set: once an answer establishes that a held item is an adapter, every later answer
means the same thing by it.

### Architecture

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| Query / Key / Value as "what I want", "what each Pokémon advertises", "what I get if I commit" | attention's Q, K, V | [`001`](answers/pokemon/001-attention-mechanisms.md) |
| The type chart normalising raw effectiveness into one turn's plan | softmax over attention scores | [`001`](answers/pokemon/001-attention-mechanisms.md) |
| The level cap on the calculation | the `1/√d_k` scaling factor | [`001`](answers/pokemon/001-attention-mechanisms.md) |
| "You cannot target a Pokémon that hasn't been sent out yet" | the causal mask | [`001`](answers/pokemon/001-attention-mechanisms.md), [`004`](answers/pokemon/004-encoder-decoder-vs-decoder-only.md) |
| **The coaching box** — several coaches watching one field, each paid to notice a different thing | multi-head attention; the head coach is `W_O` | [`001`](answers/pokemon/001-attention-mechanisms.md), [`003`](answers/pokemon/003-multi-head-attention.md), [`009`](answers/pokemon/009-mqa-and-gqa.md) |
| The bench-warmer coach who has nothing to say | heads that mostly attend to nothing; the value of an attention sink | [`003`](answers/pokemon/003-multi-head-attention.md), [`008`](answers/pokemon/008-kv-cache.md) |
| A **PC box** vs a **party** | an unordered set vs an ordered sequence | [`002`](answers/pokemon/002-positional-encodings-rope.md) |
| A numbered Poké Ball / a spinning Poké Ball | absolute vs rotary (RoPE) positional encoding | [`002`](answers/pokemon/002-positional-encodings-rope.md) |
| Fast-spinning and slow-spinning grooves on the ball | high- and low-frequency RoPE dimensions | [`002`](answers/pokemon/002-positional-encodings-rope.md) |
| The Judge / the Battler / the Interpreter | encoder-only / decoder-only / encoder-decoder | [`004`](answers/pokemon/004-encoder-decoder-vs-decoder-only.md) |
| **Flat Rules, everyone set to Level 50** | layer normalization (and RMSNorm as "skip half the paperwork") | [`005`](answers/pokemon/005-layer-normalization.md) |
| **A Gym** as one stop on the circuit | one transformer layer; the League is the stack | [`005`](answers/pokemon/005-layer-normalization.md), [`006`](answers/pokemon/006-residual-connections.md) |
| The scaler at the Gym *door* vs the Gym *exit* | pre-norm vs post-norm | [`005`](answers/pokemon/005-layer-normalization.md) |
| **"Keep your moves"** — declining the level-up prompt | residual connections | [`006`](answers/pokemon/006-residual-connections.md) |
| The notice board every Gym pins to and nobody tears down | the residual stream | [`006`](answers/pokemon/006-residual-connections.md), [`007`](answers/pokemon/007-transformer-feed-forward-block.md) |
| **The Pokédex** — each Pokémon looking itself up alone | the feed-forward block; where factual knowledge lives | [`007`](answers/pokemon/007-transformer-feed-forward-block.md) |
| The gated Pokédex ("is this relevant?" plus "how much?") | SwiGLU | [`007`](answers/pokemon/007-transformer-feed-forward-block.md) |
| **The battle notebook** — write each Pokémon down once, append as new ones appear | the KV cache | [`008`](answers/pokemon/008-kv-cache.md), [`009`](answers/pokemon/009-mqa-and-gqa.md), [`013`](answers/pokemon/013-context-length-limits.md) |
| Coaches sharing one notebook | MQA (all share one) and GQA (grouped) | [`009`](answers/pokemon/009-mqa-and-gqa.md) |
| Six slots on your **belt** vs the **PC box** across town | on-chip SRAM vs off-chip HBM | [`010`](answers/pokemon/010-flash-attention.md) |
| The giant poster you never write | the materialised attention matrix | [`010`](answers/pokemon/010-flash-attention.md) |
| A running tally rescaled when a bigger score appears | the online-softmax rescaling trick | [`010`](answers/pokemon/010-flash-attention.md) |
| **The Gym Leader roster and the receptionist** | Mixture-of-Experts; the receptionist is the router | [`011`](answers/pokemon/011-mixture-of-experts.md), [`032`](answers/pokemon/032-pruning-and-sparsity.md) |
| A fairness quota; a daily cap per Gym; turned-away challengers | load-balancing loss; expert capacity; dropped tokens | [`011`](answers/pokemon/011-mixture-of-experts.md) |
| **Scoreboard tiles** you spell names out of | tokens and the vocabulary | [`012`](answers/pokemon/012-tokenization-bpe.md) |
| A cursed tile with nothing behind it | an undertrained token | [`012`](answers/pokemon/012-tokenization-bpe.md) |

### Training, scaling and alignment

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| **The wild grass** — months of unsupervised, ungraded encounters | pretraining | [`018`](answers/pokemon/018-pretraining-sft-rlhf.md), [`019`](answers/pokemon/019-rlhf-end-to-end.md), [`025`](answers/pokemon/025-instruction-tuning.md), [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md), [`036`](answers/pokemon/036-perplexity.md), [`040`](answers/pokemon/040-hallucination.md) |
| **Obedience school** — one week, a clipboard of worked examples | supervised fine-tuning / instruction tuning | [`018`](answers/pokemon/018-pretraining-sft-rlhf.md), [`019`](answers/pokemon/019-rlhf-end-to-end.md), [`020`](answers/pokemon/020-dpo-vs-ppo.md), [`025`](answers/pokemon/025-instruction-tuning.md), [`040`](answers/pokemon/040-hallucination.md) |
| **The coach** — showing pairs and saying which is better | RLHF | [`016`](answers/pokemon/016-next-token-prediction.md), [`017`](answers/pokemon/017-teacher-forcing-exposure-bias.md), [`018`](answers/pokemon/018-pretraining-sft-rlhf.md), [`019`](answers/pokemon/019-rlhf-end-to-end.md) |
| **Comparison cards** ("in this position, turn B beat turn A") | human preference pairs | [`019`](answers/pokemon/019-rlhf-end-to-end.md), [`020`](answers/pokemon/020-dpo-vs-ppo.md), [`021`](answers/pokemon/021-reward-models.md), [`024`](answers/pokemon/024-constitutional-ai-rlaif.md) |
| **The judge** — a copy of your Pokémon retrained to score instead of battle | the reward model | [`019`](answers/pokemon/019-rlhf-end-to-end.md), [`020`](answers/pokemon/020-dpo-vs-ppo.md), [`021`](answers/pokemon/021-reward-models.md), [`022`](answers/pokemon/022-ppo-for-llms.md), [`038`](answers/pokemon/038-llm-as-a-judge.md) |
| **The photocopy** kept from obedience school | the frozen reference model; the KL penalty is "how weird was that, compared to the photocopy" | [`019`](answers/pokemon/019-rlhf-end-to-end.md), [`020`](answers/pokemon/020-dpo-vs-ppo.md), [`022`](answers/pokemon/022-ppo-for-llms.md) |
| **Swords Dance six times against a Magikarp** | reward hacking / over-optimisation | [`019`](answers/pokemon/019-rlhf-end-to-end.md), [`021`](answers/pokemon/021-reward-models.md) |
| The fourth Pokémon in the gym, predicting how the match is going | the value / critic model | [`019`](answers/pokemon/019-rlhf-end-to-end.md), [`022`](answers/pokemon/022-ppo-for-llms.md) |
| The clip: no single match may move a habit more than a set amount | PPO's clipped objective | [`022`](answers/pokemon/022-ppo-for-llms.md) |
| **Run the same battle eight times and average** | GRPO's group baseline | [`022`](answers/pokemon/022-ppo-for-llms.md), [`023`](answers/pokemon/023-grpo-reasoning.md) |
| **The scoreboard** — "did the Gyarados actually faint?" | a verifiable, ungameable reward | [`018`](answers/pokemon/018-pretraining-sft-rlhf.md), [`021`](answers/pokemon/021-reward-models.md), [`023`](answers/pokemon/023-grpo-reasoning.md), [`025`](answers/pokemon/025-instruction-tuning.md), [`038`](answers/pokemon/038-llm-as-a-judge.md) |
| A referee with a bug you can win through | reward hacking against a verifier | [`023`](answers/pokemon/023-grpo-reasoning.md) |
| **The League rulebook**, cited by article number | a constitution (Constitutional AI) | [`024`](answers/pokemon/024-constitutional-ai-rlaif.md) |
| **Rare Candy vs actual battles** | parameters vs training tokens | [`014`](answers/pokemon/014-scaling-laws.md) |
| **Magikarp → Gyarados at level 20** | emergence; and a pass/fail benchmark manufacturing a cliff out of smooth progress | [`015`](answers/pokemon/015-emergent-abilities.md) |
| Studying **Champion replays**, rewound to the Champion's position each turn | teacher forcing, and the exposure bias it leaves | [`017`](answers/pokemon/017-teacher-forcing-exposure-bias.md) |
| **The four-move limit**, in a version where the game never asks | catastrophic forgetting | [`026`](answers/pokemon/026-catastrophic-forgetting.md) |
| **Specialist camp** | full fine-tuning | [`026`](answers/pokemon/026-catastrophic-forgetting.md), [`027`](answers/pokemon/027-lora.md), [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md), [`041`](answers/pokemon/041-rag-vs-finetuning.md) |
| **A held item** | a LoRA adapter — frozen base, tiny trainable object, swappable, initialised to no effect | [`026`](answers/pokemon/026-catastrophic-forgetting.md), [`027`](answers/pokemon/027-lora.md), [`028`](answers/pokemon/028-qlora.md), [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md) |
| Fusing the item into the Pokémon | merging adapter weights back into the base | [`027`](answers/pokemon/027-lora.md), [`028`](answers/pokemon/028-qlora.md) |
| **Shorthand** — writing every stat more coarsely | quantization | [`028`](answers/pokemon/028-qlora.md), [`030`](answers/pokemon/030-quantization.md), [`044`](answers/pokemon/044-vector-databases-ann.md) |
| **The Snorlax on the page** — one entry at 9,000 when the rest are 40–90 | outliers, and why per-tensor scaling fails | [`030`](answers/pokemon/030-quantization.md) |
| **The Champion teaching the rookie** its full ranking, not just its pick | knowledge distillation on soft targets | [`031`](answers/pokemon/031-knowledge-distillation.md), [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md) |
| Snipping lines / two-of-every-four / tearing out pages | unstructured, 2:4 semi-structured, and structured pruning | [`032`](answers/pokemon/032-pruning-and-sparsity.md) |
| The lottery ticket hidden in a fat Pokédex | the lottery ticket hypothesis | [`032`](answers/pokemon/032-pruning-and-sparsity.md) |
| **The rookie guesses, the Champion checks in one flip** | speculative decoding | [`033`](answers/pokemon/033-speculative-decoding.md) |

### Decoding and evaluation

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| How boldly the Pokémon plays | sampling temperature; top-k, top-p and min-p as which options it will consider | [`034`](answers/pokemon/034-sampling-temperature-top-p.md) |
| Carrying three game plans forward and pruning | beam search | [`035`](answers/pokemon/035-beam-search.md) |
| **How surprised the Trainer is, every turn** | perplexity — and the observation that coaching makes it *worse* | [`036`](answers/pokemon/036-perplexity.md) |
| **The Gym Circuit / eight badges** | public benchmarks: standardised, comparable, saturated and leaked | [`037`](answers/pokemon/037-evaluating-llms.md), [`039`](answers/pokemon/039-benchmark-contamination.md) |
| **Your daycare** | your actual production task, which no badge measures | [`037`](answers/pokemon/037-evaluating-llms.md), [`039`](answers/pokemon/039-benchmark-contamination.md) |
| **The tapes / the training footage** | the pretraining corpus | [`016`](answers/pokemon/016-next-token-prediction.md), [`017`](answers/pokemon/017-teacher-forcing-exposure-bias.md), [`036`](answers/pokemon/036-perplexity.md), [`039`](answers/pokemon/039-benchmark-contamination.md), [`040`](answers/pokemon/040-hallucination.md) |
| A **Champion in the referee's chair** | LLM-as-a-judge, with position, length, self-preference and style biases | [`038`](answers/pokemon/038-llm-as-a-judge.md) |
| Planting a nonsense code word in the exam paper | a canary string for contamination detection | [`039`](answers/pokemon/039-benchmark-contamination.md) |
| Comparing scores on pre-cutoff and post-cutoff battles | the cleanest contamination signal there is | [`039`](answers/pokemon/039-benchmark-contamination.md) |
| Inventing Flareon's ability, confidently | hallucination — five distinct failures under one name | [`040`](answers/pokemon/040-hallucination.md) |

### Retrieval

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| **Handing the Trainer the Pokédex mid-battle** | RAG — converting a memory question into a reading question | [`040`](answers/pokemon/040-hallucination.md), [`041`](answers/pokemon/041-rag-vs-finetuning.md) |
| **Scouting reports** | your document corpus | [`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md), [`041`](answers/pokemon/041-rag-vs-finetuning.md), [`042`](answers/pokemon/042-chunking-strategies.md), [`045`](answers/pokemon/045-hybrid-search-reranking.md), [`046`](answers/pokemon/046-cross-encoder-vs-bi-encoder.md), [`047`](answers/pokemon/047-query-rewriting-hyde.md), [`048`](answers/pokemon/048-evaluating-rag.md), [`052`](answers/pokemon/052-context-engineering.md) |
| **Cutting the reports into cards** | chunking. "File by the small card, hand over the big one" is small-to-big retrieval | [`042`](answers/pokemon/042-chunking-strategies.md) |
| Writing the section heading on every card | heading-augmented / contextual chunking | [`042`](answers/pokemon/042-chunking-strategies.md) |
| Reading the whole report first, *then* cutting | contextual chunking with a full-document view | [`042`](answers/pokemon/042-chunking-strategies.md) |
| **The map**, where similar things stand near each other | embedding space | [`043`](answers/pokemon/043-embeddings.md), [`044`](answers/pokemon/044-vector-databases-ann.md), [`045`](answers/pokemon/045-hybrid-search-reranking.md), [`047`](answers/pokemon/047-query-rewriting-hyde.md) |
| Pushing against things that are *almost* right | hard negative mining | [`043`](answers/pokemon/043-embeddings.md), [`046`](answers/pokemon/046-cross-encoder-vs-bi-encoder.md) |
| **The Fly network**, layered from cities to footpaths | HNSW | [`044`](answers/pokemon/044-vector-databases-ann.md) |
| **Regions** (Kanto, Johto, Hoenn…) each with a centre | IVF partitioning, and the border problem is the recall loss | [`044`](answers/pokemon/044-vector-databases-ann.md) |
| Shorthand coordinates, then full coordinates for the survivors | product quantization plus exact rerank | [`044`](answers/pokemon/044-vector-databases-ann.md) |
| **The Literalist** | keyword / BM25 search — perfect on codes, helpless with paraphrase | [`045`](answers/pokemon/045-hybrid-search-reranking.md) |
| **The Cartographer** | dense vector search — good at meaning, bad at exactness | [`045`](answers/pokemon/045-hybrid-search-reranking.md) |
| Combining by rank rather than by score | reciprocal rank fusion | [`045`](answers/pokemon/045-hybrid-search-reranking.md) |
| **The filing clerk** — writes one index card per report, months in advance | a bi-encoder | [`045`](answers/pokemon/045-hybrid-search-reranking.md), [`046`](answers/pokemon/046-cross-encoder-vs-bi-encoder.md) |
| **The coach** — reads the question and one report side by side | a cross-encoder reranker | [`045`](answers/pokemon/045-hybrid-search-reranking.md), [`046`](answers/pokemon/046-cross-encoder-vs-bi-encoder.md), [`048`](answers/pokemon/048-evaluating-rag.md) |
| One card per *line* of the report | late-interaction retrieval (ColBERT-style) | [`046`](answers/pokemon/046-cross-encoder-vs-bi-encoder.md) |
| **Writing a fake answer and searching with that** | HyDE | [`047`](answers/pokemon/047-query-rewriting-hyde.md) |
| "What about the other one?" rewritten to "What about Milotic?" | query rewriting and coreference resolution | [`047`](answers/pokemon/047-query-rewriting-hyde.md) |
| **Scout vs Trainer** | retriever vs generator, measured separately | [`048`](answers/pokemon/048-evaluating-rag.md) |
| "Was the right report even in the fifty?" | retrieval recall as a hard ceiling on the whole system | [`045`](answers/pokemon/045-hybrid-search-reranking.md), [`048`](answers/pokemon/048-evaluating-rag.md) |

### Prompting, reasoning and agents

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| **Talking through the damage calc out loud** | chain-of-thought | [`016`](answers/pokemon/016-next-token-prediction.md), [`049`](answers/pokemon/049-chain-of-thought.md) |
| "One moment of thought per thing you say" | fixed compute per token; each generated token buys another forward pass | [`016`](answers/pokemon/016-next-token-prediction.md), [`049`](answers/pokemon/049-chain-of-thought.md) |
| A narrated chain that never mentions the real reason | unfaithful reasoning — a thinking tool, not a confession | [`049`](answers/pokemon/049-chain-of-thought.md) |
| **Six calcs and a vote** | self-consistency | [`050`](answers/pokemon/050-self-consistency.md) |
| **Three examples, then a tier letter** | few-shot in-context learning; the wrong-labels experiment shows the examples select a task rather than teach one | [`051`](answers/pokemon/051-in-context-learning.md) |
| "That happened before — what followed it?" | induction heads, and the visible kink where the ability appears | [`003`](answers/pokemon/003-multi-head-attention.md), [`015`](answers/pokemon/015-emergent-abilities.md), [`051`](answers/pokemon/051-in-context-learning.md) |
| **The bag** — everything the Trainer carries into the stadium | the context window | [`052`](answers/pokemon/052-context-engineering.md), [`053`](answers/pokemon/053-react-agents.md), [`054`](answers/pokemon/054-tool-calling.md) |
| Sending a scout off with their own empty bag | subagents / context isolation | [`052`](answers/pokemon/052-context-engineering.md) |
| Pre-packing the unchanging pages at the top | prefix caching | [`008`](answers/pokemon/008-kv-cache.md), [`052`](answers/pokemon/052-context-engineering.md) |
| **Think, act, look, repeat** | ReAct | [`053`](answers/pokemon/053-react-agents.md) |
| 0.95 per turn compounding to 13% over forty turns | why long agent trajectories fail | [`053`](answers/pokemon/053-react-agents.md) |
| **"The Trainer shouts, you throw the ball"** | tool calling: the model emits a request, the harness executes it. Every safety property lives in the harness | [`054`](answers/pokemon/054-tool-calling.md) |
| Only letting them say words that could still form a valid command | constrained decoding / grammar-guided sampling | [`054`](answers/pokemon/054-tool-calling.md) |
| A note planted in what you report back | prompt injection through tool output | [`054`](answers/pokemon/054-tool-calling.md) |
| **A standard-issue Poké Ball** that works with every species | the Model Context Protocol — one interface instead of N×M bespoke integrations | [`055`](answers/pokemon/055-model-context-protocol.md) |
| Moves (the Trainer picks) / Pokédex pages (you hand over) / battle strategies (the player invokes) | MCP tools vs resources vs prompts — the split is about *who decides* | [`055`](answers/pokemon/055-model-context-protocol.md) |
| A ball that borrows your Trainer to think for it | MCP sampling: the server asks the client's model, so servers need no credentials of their own | [`055`](answers/pokemon/055-model-context-protocol.md) |
| **Sending a scout with their own bag** who returns one sentence | subagents, adopted for context isolation rather than modularity | [`052`](answers/pokemon/052-context-engineering.md), [`056`](answers/pokemon/056-multi-agent-systems.md) |
| A lead and scouts / a relay / a maker and a critic | orchestrator-worker, pipeline, and generator-critic multi-agent shapes | [`056`](answers/pokemon/056-multi-agent-systems.md) |
| "Only one Trainer writes" | avoiding concurrent writes to shared state | [`056`](answers/pokemon/056-multi-agent-systems.md) |
| **Taking longer per turn** rather than training harder before the season | test-time compute as a dial separate from training compute | [`057`](answers/pokemon/057-test-time-compute.md) |
| The easy turn / the hard-but-reachable turn / the impossible turn | where extra inference compute pays and where it is wasted | [`057`](answers/pokemon/057-test-time-compute.md) |
| **A Trainer who pauses before moving** | a reasoning model, and the fact that deliberation emerged from scoreboard training rather than being scripted | [`023`](answers/pokemon/023-grpo-reasoning.md), [`057`](answers/pokemon/057-test-time-compute.md), [`058`](answers/pokemon/058-reasoning-models.md) |
| Showing a rookie a Champion's full deliberations | distilling reasoning traces — "can't discover it, can imitate it" | [`058`](answers/pokemon/058-reasoning-models.md) |
| **A stranger in the crowd shouting orders at your Pokémon** | prompt injection; the Pokémon hears one undifferentiated stream of words | [`059`](answers/pokemon/059-prompt-injection.md) |
| The three ingredients: secrets, untrusted input, a way to send something out | the lethal trifecta — remove any one and data cannot leave | [`059`](answers/pokemon/059-prompt-injection.md) |
| One Pokémon that holds the secrets and never reads outside material | privilege separation between a trusted and a quarantined agent | [`059`](answers/pokemon/059-prompt-injection.md) |
| **Talking your own Pokémon into a banned move** | jailbreaking, as distinct from injection: you are the attacker, not a third party | [`060`](answers/pokemon/060-jailbreaks.md) |
| Rules taught in an afternoon versus abilities built over months | why the safety-trained region is much smaller than the capability region | [`060`](answers/pokemon/060-jailbreaks.md) |
| Screening what the Pokémon *did* rather than what it was *asked* | output filtering, and why it usually beats input filtering | [`060`](answers/pokemon/060-jailbreaks.md) |
| **Referees standing around the arena**, one at each stage | layered guardrails: format checks, an input classifier, the model's own training, an output classifier, and mechanical validation | [`061`](answers/pokemon/061-guardrails-moderation.md) |
| The junior ref at the door vs the head ref watching the move | input moderation vs output moderation — judging a request is ambiguous, judging a move is not | [`061`](answers/pokemon/061-guardrails-moderation.md) |
| "Let it redo the turn more carefully" instead of blocking | regenerating under stricter instructions as a middle response between allow and refuse | [`061`](answers/pokemon/061-guardrails-moderation.md) |
| Zero incidents and a 15% false-refusal rate | over-refusal: the failure that never shows up on a dashboard because the user just leaves | [`061`](answers/pokemon/061-guardrails-moderation.md), [`062`](answers/pokemon/062-red-teaming.md) |
| A refusal that names the exact rule it broke | leaking a map of your defences to the next attacker | [`061`](answers/pokemon/061-guardrails-moderation.md) |
| **Hiring someone to beat your own Pokémon** | red teaming, as opposed to measuring the average case | [`062`](answers/pokemon/062-red-teaming.md) |
| The curious kid / the determined opponent / the note-planter / the automated operation | threat modelling by adversary class | [`062`](answers/pokemon/062-red-teaming.md) |
| "Fix the class, not the phrasing" | generalising from one found attack instead of patching a string | [`062`](answers/pokemon/062-red-teaming.md) |
| Testing the whole stadium, not just the Pokémon | the attack surface is the system — documents, tool permissions and guardrails included | [`062`](answers/pokemon/062-red-teaming.md) |

### Fundamentals, optimisation and systems

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| **"Is that 90% honest?"** | calibration — whether stated confidence matches observed accuracy | [`063`](answers/pokemon/063-model-calibration.md) |
| Coaching that makes a Trainer *less* honest about uncertainty | RLHF degrading calibration by rewarding decisive answers | [`019`](answers/pokemon/019-rlhf-end-to-end.md), [`063`](answers/pokemon/063-model-calibration.md) |
| Asking three times and seeing whether they agree | self-consistency agreement as an uncertainty estimate | [`050`](answers/pokemon/050-self-consistency.md), [`063`](answers/pokemon/063-model-calibration.md) |
| Naming a *set* of moves that contains the right one 95% of the time | conformal prediction | [`063`](answers/pokemon/063-model-calibration.md) |
| **The One-Trick Trainer** ("always lead with Onix") | high bias — consistently wrong, and retraining does not help | [`064`](answers/pokemon/064-bias-variance-tradeoff.md), [`065`](answers/pokemon/065-overfitting.md) |
| **The Superstitious Trainer** (red hats, Tuesdays) | high variance — memorising the training sample | [`064`](answers/pokemon/064-bias-variance-tradeoff.md), [`065`](answers/pokemon/065-overfitting.md), [`066`](answers/pokemon/066-l1-vs-l2-regularization.md) |
| The Pokémon with *exactly* enough memory to memorise and no more | the interpolation threshold, where double descent peaks | [`064`](answers/pokemon/064-bias-variance-tradeoff.md) |
| **The scrambled-tape test** | fitting random labels, to prove the model has memorisation capacity | [`065`](answers/pokemon/065-overfitting.md) |
| A feature from the future (`revive_used`) | target leakage | [`065`](answers/pokemon/065-overfitting.md), [`068`](answers/pokemon/068-cross-validation.md), [`098`](answers/pokemon/098-training-serving-skew.md) |
| **Releasing weak Pokémon vs a pay cut for everyone** | L1 (sparse, exact zeros) vs L2 (dense, shrunk) regularisation | [`066`](answers/pokemon/066-l1-vs-l2-regularization.md) |
| Charging upkeep separately from the feedback channel | decoupled weight decay — the AdamW correction | [`066`](answers/pokemon/066-l1-vs-l2-regularization.md), [`072`](answers/pokemon/072-gradient-descent-optimizers.md) |
| **Benching half the team at random each practice** | dropout, and counting the survivors double is inverted scaling | [`067`](answers/pokemon/067-dropout.md) |
| Forgetting to switch to tournament mode | forgetting `model.eval()` — silent degradation, no error | [`067`](answers/pokemon/067-dropout.md), [`075`](answers/pokemon/075-batch-norm-vs-layer-norm.md) |
| **Testing against five different Gyms in rotation** | k-fold cross-validation; the fold-to-fold spread is the point | [`068`](answers/pokemon/068-cross-validation.md) |
| Testing on the future / splitting by opponent / preparing before splitting | temporal, group and preprocessing leakage | [`065`](answers/pokemon/065-overfitting.md), [`068`](answers/pokemon/068-cross-validation.md), [`098`](answers/pokemon/098-training-serving-skew.md) |
| **Hunting shinies with a detector** | precision (are your Ultra Balls landing?) and recall (did any get away?) | [`069`](answers/pokemon/069-precision-recall-f1.md), [`070`](answers/pokemon/070-roc-auc-vs-pr-auc.md), [`071`](answers/pokemon/071-class-imbalance.md) |
| "You only have ten Ultra Balls" | precision@k, when downstream capacity is fixed | [`069`](answers/pokemon/069-precision-recall-f1.md) |
| The scorecard that divides by a million ordinary Pokémon | ROC-AUC hiding false positives under a huge true-negative count | [`070`](answers/pokemon/070-roc-auc-vs-pr-auc.md) |
| **"Nothing is ever shiny"** scoring 99.98% | why accuracy is meaningless on rare positives | [`069`](answers/pokemon/069-precision-recall-f1.md), [`070`](answers/pokemon/070-roc-auc-vs-pr-auc.md), [`071`](answers/pokemon/071-class-imbalance.md) |
| Turning the detector's dial down before touching the footage | threshold tuning before resampling | [`071`](answers/pokemon/071-class-imbalance.md) |
| Inventing halfway-shinies | SMOTE, and why "halfway between two positives" may not be a positive | [`071`](answers/pokemon/071-class-imbalance.md) |
| **Adjusting after every twenty matches** | mini-batch gradient descent | [`072`](answers/pokemon/072-gradient-descent-optimizers.md), [`081`](answers/pokemon/081-batch-size-and-lr.md) |
| Remembering the trend so contradictory advice cancels | momentum | [`072`](answers/pokemon/072-gradient-descent-optimizers.md) |
| Weighting the adjustment by how noisy that stat's feedback is | adaptive optimisers (Adam's second moment) | [`072`](answers/pokemon/072-gradient-descent-optimizers.md), [`076`](answers/pokemon/076-learning-rate-schedules.md) |
| Scaling up early estimates when you have no history | Adam's bias correction | [`072`](answers/pokemon/072-gradient-descent-optimizers.md) |
| **Walking back through the season once** | backpropagation as reverse-mode autodiff | [`073`](answers/pokemon/073-backpropagation.md), [`078`](answers/pokemon/078-gradient-checkpointing.md) |
| "Thousands of things to fix, one outcome to explain" | why reverse mode rather than forward mode | [`073`](answers/pokemon/073-backpropagation.md) |
| A Pokémon that never improves however much you train it | a detached graph — gradients silently not flowing | [`073`](answers/pokemon/073-backpropagation.md) |
| **The Champion's advice fading to silence by Route 1** | vanishing gradients | [`005`](answers/pokemon/005-layer-normalization.md), [`006`](answers/pokemon/006-residual-connections.md), [`074`](answers/pokemon/074-vanishing-exploding-gradients.md) |
| The message amplifying into "BURN EVERYTHING" | exploding gradients | [`074`](answers/pokemon/074-vanishing-exploding-gradients.md) |
| Turning the whole message down proportionally | gradient clipping by global norm, preserving direction | [`074`](answers/pokemon/074-vanishing-exploding-gradients.md) |
| **"Compare to the room" vs "compare to your own six stats"** | BatchNorm vs LayerNorm | [`005`](answers/pokemon/005-layer-normalization.md), [`075`](answers/pokemon/075-batch-norm-vs-layer-norm.md) |
| **Easing into training over the first fortnight** | learning-rate warmup — mostly because the optimiser's noise estimates have not calibrated | [`072`](answers/pokemon/072-gradient-descent-optimizers.md), [`076`](answers/pokemon/076-learning-rate-schedules.md) |
| Flat intensity, then a sharp taper at the end | WSD scheduling, and why cosine forces you to fix the run length in advance | [`076`](answers/pokemon/076-learning-rate-schedules.md) |
| **The precise-but-narrow format vs the rough-but-unlimited one** | FP16 vs BF16 — range matters more than precision for training | [`077`](answers/pokemon/077-mixed-precision-training.md) |
| Multiplying every correction by a thousand before writing it down | FP16 loss scaling, and the thrown-away steps when it overflows | [`077`](answers/pokemon/077-mixed-precision-training.md) |
| Keeping the official stat records precise while the work is rough | FP32 master weights under mixed precision | [`077`](answers/pokemon/077-mixed-precision-training.md) |
| **Filming only every third Gym and replaying the gaps** | gradient checkpointing / activation recomputation | [`010`](answers/pokemon/010-flash-attention.md), [`078`](answers/pokemon/078-gradient-checkpointing.md) |
| Recording the dice rolls so the replay is identical | saving RNG state so recomputation reproduces the forward pass | [`078`](answers/pokemon/078-gradient-checkpointing.md) |
| **Same team different opponents / splitting a Pokémon / splitting the journey / splitting the roster** | data, tensor, pipeline and expert parallelism | [`011`](answers/pokemon/011-mixture-of-experts.md), [`079`](answers/pokemon/079-parallelism-strategies.md) |
| Gyms sitting idle while the first one works | the pipeline bubble, closed by micro-batching | [`079`](answers/pokemon/079-parallelism-strategies.md) |
| **Eight gyms each keeping a full copy of the paperwork** | replicated optimizer state under plain data parallelism | [`080`](answers/pokemon/080-zero-and-fsdp.md) |
| Splitting the history / the feedback / the stats themselves | ZeRO stages 1, 2 and 3 (FSDP) | [`080`](answers/pokemon/080-zero-and-fsdp.md) |
| Phoning ahead for the next Pokémon's stats | prefetching to overlap all-gather with compute | [`080`](answers/pokemon/080-zero-and-fsdp.md) |
| **"Watch more matches, adjust harder"** | the batch-size / learning-rate scaling relationship | [`076`](answers/pokemon/076-learning-rate-schedules.md), [`081`](answers/pokemon/081-batch-size-and-lr.md) |
| Ten sessions of ten, one adjustment at the end | gradient accumulation — and forgetting to divide by ten is the classic bug | [`081`](answers/pokemon/081-batch-size-and-lr.md) |
| **The Bouncer / the Soft Bouncer / the Dimmer** | ReLU, GELU and gated (SwiGLU) activations | [`082`](answers/pokemon/082-activation-functions.md) |
| A Pokémon permanently switched off | dying ReLU units | [`074`](answers/pokemon/074-vanishing-exploding-gradients.md), [`082`](answers/pokemon/082-activation-functions.md) |
| Two knobs — "what's my reaction" and "how much does this matter" | the multiplicative gate, an operation a pointwise activation cannot express | [`007`](answers/pokemon/007-transformer-feed-forward-block.md), [`082`](answers/pokemon/082-activation-functions.md) |
| **Subtracting the best score before converting** | the max-subtraction trick that makes softmax numerically stable | [`010`](answers/pokemon/010-flash-attention.md), [`083`](answers/pokemon/083-softmax-and-logsumexp.md) |
| Handing over percentages when raw scores were expected | double-softmax — the silent, common bug | [`083`](answers/pokemon/083-softmax-and-logsumexp.md), [`084`](answers/pokemon/084-cross-entropy-loss.md) |
| **"You said it was impossible, and it happened"** | cross-entropy's unbounded penalty for confident errors | [`084`](answers/pokemon/084-cross-entropy-loss.md) |
| Grading how much confidence went on what actually happened | negative log-likelihood, and its equivalence to KL and to maximum likelihood | [`036`](answers/pokemon/036-perplexity.md), [`084`](answers/pokemon/084-cross-entropy-loss.md) |
| **"Thunderbolt — 90%, and leave room for everything else"** | label smoothing | [`085`](answers/pokemon/085-label-smoothing.md) |
| A softened teacher being a worse teacher | label smoothing erasing the dark knowledge distillation depends on | [`031`](answers/pokemon/031-knowledge-distillation.md), [`085`](answers/pokemon/085-label-smoothing.md) |

### Classical ML, generative models and production

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| **"Physical bruiser ↔ special sweeper"** as a single axis | a principal component | [`086`](answers/pokemon/086-pca.md) |
| The axis that varies most vs the tiny Speed gap that decides the match | PCA keeping variance rather than discriminative signal, because it never saw the labels | [`086`](answers/pokemon/086-pca.md) |
| **The ribbon of real Pokémon inside an enormous empty space** | the manifold hypothesis — why embeddings and vector search work despite the curse | [`044`](answers/pokemon/044-vector-databases-ann.md), [`087`](answers/pokemon/087-curse-of-dimensionality.md) |
| Everyone being the same distance from everyone else | distance concentration in high dimensions | [`087`](answers/pokemon/087-curse-of-dimensionality.md) |
| **A flowchart / a committee that votes / a relay that fixes mistakes** | decision trees, random forests, gradient boosting | [`088`](answers/pokemon/088-trees-forests-boosting.md), [`089`](answers/pokemon/089-bagging-vs-boosting.md) |
| Blinding each scout to different stats | random feature selection, to decorrelate the ensemble | [`088`](answers/pokemon/088-trees-forests-boosting.md), [`089`](answers/pokemon/089-bagging-vs-boosting.md) |
| Wild-and-detailed members vs simple-and-reliable ones | deep trees for bagging, shallow ones for boosting | [`088`](answers/pokemon/088-trees-forests-boosting.md), [`089`](answers/pokemon/089-bagging-vs-boosting.md) |
| A chain contorting itself around one mislabelled match | boosting's sensitivity to label noise | [`089`](answers/pokemon/089-bagging-vs-boosting.md) |
| **"Your Champion already knows how to battle"** | transfer learning; the basics transfer, the specifics are replaced | [`090`](answers/pokemon/090-transfer-learning.md) |
| Attaching a clueless new specialist that shouts wild corrections | a randomly initialised head damaging a pretrained backbone | [`090`](answers/pokemon/090-transfer-learning.md) |
| "Frozen" that is still quietly recalibrating | frozen weights with BatchNorm statistics still updating | [`075`](answers/pokemon/075-batch-norm-vs-layer-norm.md), [`090`](answers/pokemon/090-transfer-learning.md) |
| **"The footage grades itself"** | self-supervised learning | [`016`](answers/pokemon/016-next-token-prediction.md), [`091`](answers/pokemon/091-self-supervised-learning.md) |
| "Is this clip upside down?" | a pretext task with a shortcut, and why the good ones have none | [`091`](answers/pokemon/091-self-supervised-learning.md) |
| Deciding which of a million hours is worth watching | data curation replacing labelling as the bottleneck | [`014`](answers/pokemon/014-scaling-laws.md), [`091`](answers/pokemon/091-self-supervised-learning.md) |
| **Two photos of the same Pokémon, pulled together** | contrastive learning and the InfoNCE objective | [`043`](answers/pokemon/043-embeddings.md), [`092`](answers/pokemon/092-contrastive-learning.md) |
| Tinting one photo blue | augmentation designed to block a shortcut (colour-histogram matching) | [`092`](answers/pokemon/092-contrastive-learning.md) |
| Putting every Pokémon in the same spot on the map | representational collapse | [`092`](answers/pokemon/092-contrastive-learning.md) |
| Writing "a photo of a Flareon" and finding the nearest image | CLIP-style zero-shot classification from a shared embedding space | [`092`](answers/pokemon/092-contrastive-learning.md), [`094`](answers/pokemon/094-multimodal-models.md) |
| **Developing a photo out of static** | diffusion; training is "spot the static", sampling is repeated removal | [`093`](answers/pokemon/093-diffusion-models.md) |
| The "how literally?" dial | classifier-free guidance | [`093`](answers/pokemon/093-diffusion-models.md) |
| Developing a compressed sketch rather than every pixel | latent diffusion | [`093`](answers/pokemon/093-diffusion-models.md) |
| "What is halfway between Pikachu and Charizard?" | why diffusion suits continuous data and struggles with discrete text | [`093`](answers/pokemon/093-diffusion-models.md) |
| **The spotter who describes the field in the Trainer's own format** | a vision encoder plus a projector | [`094`](answers/pokemon/094-multimodal-models.md) |
| Answering without really looking at the photo | modality imbalance — text-only hallucination in a VLM | [`040`](answers/pokemon/040-hallucination.md), [`094`](answers/pokemon/094-multimodal-models.md) |
| **"The metagame moved and nobody told your Trainer"** | drift; four kinds needing four responses | [`095`](answers/pokemon/095-data-drift.md) |
| The same lead meaning something different this season | concept drift — the only kind that necessarily degrades accuracy | [`095`](answers/pokemon/095-data-drift.md) |
| Somebody changing how the scoreboard reports HP | upstream pipeline breakage, which is most drift alerts | [`095`](answers/pokemon/095-data-drift.md), [`098`](answers/pokemon/098-training-serving-skew.md) |
| Watching what your Trainer *says* before results arrive | prediction drift as the earliest label-free signal | [`095`](answers/pokemon/095-data-drift.md) |
| **"Does the new Trainer actually win more?"** | online A/B testing versus offline metrics | [`096`](answers/pokemon/096-ab-testing-ml.md) |
| Deal-breakers that must not get worse | guardrail metrics — latency, cost, complaint rate | [`096`](answers/pokemon/096-ab-testing-ml.md), [`097`](answers/pokemon/097-serving-cost-latency.md) |
| Checking every morning and stopping when ahead | peeking, and the false-positive rate it inflates | [`096`](answers/pokemon/096-ab-testing-ml.md) |
| A 50.4/49.6 split | sample ratio mismatch — check it before anything else | [`096`](answers/pokemon/096-ab-testing-ml.md) |
| **Reading the team sheet vs playing the turns** | prefill (compute-bound) vs decode (bandwidth-bound) | [`008`](answers/pokemon/008-kv-cache.md), [`097`](answers/pokemon/097-serving-cost-latency.md) |
| Stopping the Trainer monologuing | shortening output, the most ignored cost lever | [`097`](answers/pokemon/097-serving-cost-latency.md) |
| Not sending the Champion to every match | model routing by difficulty | [`057`](answers/pokemon/057-test-time-compute.md), [`097`](answers/pokemon/097-serving-cost-latency.md) |
| Seating a new challenger the moment a table frees up | continuous / in-flight batching | [`097`](answers/pokemon/097-serving-cost-latency.md) |
| Matches per hour *at an acceptable speed* | goodput, rather than raw throughput | [`097`](answers/pokemon/097-serving-cost-latency.md) |
| **The practice scoreboard reading differently from the live one** | training-serving skew | [`098`](answers/pokemon/098-training-serving-skew.md) |
| A January match scored with September's career totals | time-travel skew, and why it produces excellent offline metrics | [`065`](answers/pokemon/065-overfitting.md), [`098`](answers/pokemon/098-training-serving-skew.md) |
| Writing down exactly what the live board showed, then training on that | logging serving features — skew becomes structurally impossible | [`098`](answers/pokemon/098-training-serving-skew.md) |
| **Rough sweep, careful ranking, final polish** | the retrieval → ranking → re-ranking funnel of a recommender | [`046`](answers/pokemon/046-cross-encoder-vs-bi-encoder.md), [`099`](answers/pokemon/099-ml-system-design.md) |
| Trainers and Pokémon placed on the same map | two-tower retrieval, and why it cannot notice "they already have three Fire types" | [`043`](answers/pokemon/043-embeddings.md), [`099`](answers/pokemon/099-ml-system-design.md) |
| The Pokémon shown first getting caught most | position bias | [`099`](answers/pokemon/099-ml-system-design.md) |
| Recommending only what you are confident about | the exploration problem and the feedback loop that narrows the catalogue | [`095`](answers/pokemon/095-data-drift.md), [`099`](answers/pokemon/099-ml-system-design.md) |
| **Five incompatible meanings of "fair"** | the fairness impossibility results — demographic parity, equalised odds, calibration | [`100`](answers/pokemon/100-fairness-bias-privacy.md) |
| Deleting "region" but keeping hometown and academy | fairness through unawareness failing, and losing the ability to audit | [`100`](answers/pokemon/100-fairness-bias-privacy.md) |
| Removing duplicate footage | deduplication, which reduces memorisation *and* improves quality | [`012`](answers/pokemon/012-tokenization-bpe.md), [`100`](answers/pokemon/100-fairness-bias-privacy.md) |
| Noise that drowns out the two hundred Alola records | differential privacy hurting under-represented groups most | [`100`](answers/pokemon/100-fairness-bias-privacy.md) |
| "Kanto 94%, Johto 92%, Alola 61%" | disaggregated evaluation — the single highest-value fairness practice | [`037`](answers/pokemon/037-evaluating-llms.md), [`100`](answers/pokemon/100-fairness-bias-privacy.md) |

---

## One term, several jobs

A few props are reused for different technical objects in different questions. The
answers are consistent within themselves; this table is here so you do not carry the
wrong reading across.

| Prop | Meaning A | Meaning B | Meaning C |
| --- | --- | --- | --- |
| **The Pokédex** | the feed-forward block, where knowledge is stored ([`007`](answers/pokemon/007-transformer-feed-forward-block.md)) | the model weights being rounded, pruned or flipped through ([`030`](answers/pokemon/030-quantization.md), [`032`](answers/pokemon/032-pruning-and-sparsity.md), [`033`](answers/pokemon/033-speculative-decoding.md)) | the retrieved documents handed over at battle time ([`040`](answers/pokemon/040-hallucination.md), [`041`](answers/pokemon/041-rag-vs-finetuning.md)) |
| **The coach** | RLHF — the person who grades pairs ([`018`](answers/pokemon/018-pretraining-sft-rlhf.md), [`019`](answers/pokemon/019-rlhf-end-to-end.md)) | one attention head in the coaching box ([`001`](answers/pokemon/001-attention-mechanisms.md), [`003`](answers/pokemon/003-multi-head-attention.md)) | the cross-encoder reranker that reads question and report together ([`045`](answers/pokemon/045-hybrid-search-reranking.md), [`046`](answers/pokemon/046-cross-encoder-vs-bi-encoder.md)) |
| **The notebook** | the KV cache ([`008`](answers/pokemon/008-kv-cache.md), [`009`](answers/pokemon/009-mqa-and-gqa.md), [`013`](answers/pokemon/013-context-length-limits.md)) | the Judge's notes that the Battler glances at — cross-attention ([`004`](answers/pokemon/004-encoder-decoder-vs-decoder-only.md)) | |
| **The photocopy** | the frozen reference model in RLHF ([`019`](answers/pokemon/019-rlhf-end-to-end.md), [`020`](answers/pokemon/020-dpo-vs-ppo.md), [`022`](answers/pokemon/022-ppo-for-llms.md)) | a cached copy of the shared prompt prefix ([`008`](answers/pokemon/008-kv-cache.md)) | |
| **The scoreboard** | a verifiable reward ([`018`](answers/pokemon/018-pretraining-sft-rlhf.md), [`023`](answers/pokemon/023-grpo-reasoning.md)) | the vocabulary you spell names out of ([`012`](answers/pokemon/012-tokenization-bpe.md)) | a pass/fail benchmark that manufactures cliffs ([`015`](answers/pokemon/015-emergent-abilities.md)) |
| **Camp** | full fine-tuning ([`026`](answers/pokemon/026-catastrophic-forgetting.md)–[`029`](answers/pokemon/029-finetuning-vs-peft-vs-prompting.md), [`041`](answers/pokemon/041-rag-vs-finetuning.md)) | a short refresher after merging KV heads — uptraining ([`009`](answers/pokemon/009-mqa-and-gqa.md)) | |
| **Shorthand** | weight quantization ([`028`](answers/pokemon/028-qlora.md), [`030`](answers/pokemon/030-quantization.md)) | compressed KV representations ([`009`](answers/pokemon/009-mqa-and-gqa.md)) | coarse vector codes for search ([`044`](answers/pokemon/044-vector-databases-ann.md)) |
| **The rookie** | the small draft model in speculative decoding ([`033`](answers/pokemon/033-speculative-decoding.md)) | the small student in distillation ([`031`](answers/pokemon/031-knowledge-distillation.md)) | a weak model generally, which chain-of-thought can make worse ([`030`](answers/pokemon/030-quantization.md), [`049`](answers/pokemon/049-chain-of-thought.md)) |
| **The judge** | the learned reward model ([`019`](answers/pokemon/019-rlhf-end-to-end.md)–[`022`](answers/pokemon/022-ppo-for-llms.md)) | an LLM grading outputs at eval time ([`038`](answers/pokemon/038-llm-as-a-judge.md)) | |
| **The referee** | the automatic checker a verifiable reward runs against, buggy and exploitable ([`023`](answers/pokemon/023-grpo-reasoning.md), [`058`](answers/pokemon/058-reasoning-models.md)) | a safety classifier trained on synthetic jailbreak attempts ([`060`](answers/pokemon/060-jailbreaks.md)) | |

---

## A note on accuracy

The Pokémon answers are held to the same standard as the serious ones: an analogy that
misstates a game mechanic is a bug, not a stylistic choice. Where an entry above
describes a mechanic more loosely than the games do — type effectiveness has more edge
cases than the table shows, and abilities interact in ways no single line captures — that
is deliberate simplification for readers who need enough to follow the argument. If you
find an answer relying on a mechanic that does not work the way it claims, that is worth
an issue.

---

Pokémon is a trademark of Nintendo / Creatures Inc. / GAME FREAK inc. This project is an
unaffiliated educational work and uses the names nominatively for teaching purposes.
