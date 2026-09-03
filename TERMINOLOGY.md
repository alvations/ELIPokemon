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
  stable vocabulary across all 54 questions — the wild grass is *always* pretraining,
  a held item is *always* a LoRA adapter — and once you have that mapping, the answers
  read as a single consistent system rather than 54 separate jokes.
* Checking an answer's honesty? Cross-reference the mapping table against
  `answers/serious/` for the same id. Both answers describe the same reality; that is
  the whole premise.

Question ids are cited as bare numbers (`007`, `041`) and correspond to the filenames
in both `answers/serious/` and `answers/pokemon/`.

---

## Core concepts

**Pokémon.** A creature you catch, raise and battle with. Each one has a species (its
kind), a level, six numeric stats, one or two elemental **types**, up to four **moves**,
one **ability**, and optionally one **held item**. In the dataset a Pokémon is usually
the model itself, or one token in a sequence, depending on the question.

**Trainer.** The human who owns and directs the Pokémon. Trainers do not act on the
field; they issue orders and their Pokémon carry them out. This split matters enormously
in `054`, where it becomes the model-versus-harness boundary.

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
extremes an attention distribution needs (`001`), the cliff a pass/fail benchmark hides
(`015`), and the arithmetic a chain of thought has to actually perform (`049`).

**Party.** The six Pokémon a Trainer carries, in a fixed order. Slot 1 is sent out
first. The order is strategy, not decoration.

**PC box.** Storage at a Pokémon Center holding everything not in your party —
thousands of Pokémon, unordered, and requiring a trip to reach. The dataset uses it two
ways: as an unordered set with no notion of position (`002`), and as large, slow,
far-away memory as opposed to the six fast slots on your belt (`010`).

**HP (hit points).** A Pokémon's health. At zero it **faints** and can no longer battle.

**Fainting.** Being knocked out. A **KO** is causing this. "Did the Gyarados faint?" is
the dataset's stock example of a fact you can simply check rather than have graded
(`023`, `038`).

**Moves.** The four attacks or effects a Pokémon knows. Four is a hard cap: to learn a
fifth, one must be forgotten, and the game asks you which. `006` builds residual
connections out of the fact that you are *allowed to say no*; `026` builds catastrophic
forgetting out of a hypothetical version where the game never asks.

**PP (power points).** Each move has a limited number of uses per trip, refilled at a
Pokémon Center. Appears once, in `001`, as the resource that runs out when you try to
compare everyone on the field to everyone else.

**Ability.** A passive trait, one per Pokémon, that changes the rules for it
specifically — see the abilities table below. Abilities are the reason a coach whose
only skill is the type chart gets ambushed (`001`, `003`).

**Held item.** One object a Pokémon carries into battle, granting a persistent effect.
Small, swappable, and it does not change the Pokémon. This is the dataset's single most
reused mapping: a held item is a LoRA adapter (`026`, `027`, `028`, `029`).

**Level.** 1 to 100. Higher levels mean higher stats. Levels are gained by battling, or
bought outright with Rare Candy — the tradeoff `014` is built on.

**EVs (effort values).** Hidden training points a Pokémon accumulates by battling, which
raise specific stats. "EV-trained" means deliberately conditioned rather than merely
levelled (`005`, `047`).

**Evolution.** A permanent transformation into a different, usually stronger species,
triggered by level, item or condition. It is discrete: nothing, nothing, nothing, then a
different creature. `015` uses it as the image of a genuine phase transition, and then
spends the rest of the answer arguing that most claimed emergence is a badly chosen
metric rather than a real evolution.

**Rare Candy.** An item granting one level instantly, with none of the experience that
normally comes with it. Pure scale, no substance. `014` makes it parameters, and battles
the training tokens.

**Nickname.** A Pokémon can be renamed to anything. `012` uses a Charizard nicknamed
"Big Steve" to show why a vocabulary of whole names cannot work.

---

## Battling

**Turn.** Both sides choose an action, then both resolve. Battles in the dataset run
anywhere from 6 turns (`038`) to a hypothetical 400 (`013`).

**Single vs Double Battle.** In a Single Battle one Pokémon per side is out. In a
**Double Battle** two per side are out simultaneously, so a move must choose a target
among several. `001` opens with a Double Battle precisely because attention needs more
than one candidate to attend to.

**Switching.** Swapping the active Pokémon for one from your party. Costs your action
for the turn. Switch loops — in, out, in, out — are the dataset's picture of an agent
that never terminates (`053`) and of exposure-bias drift (`017`).

**Weather.** A field condition lasting several turns, usually set by an ability or a
move. **Rain** boosts Water moves and makes some abilities live; **sun** boosts Fire.
Weather teams are built entirely around it: `016` and `051` both use "Politoed sets
rain, Swift Swim Kingdra sweeps" as an example of a plan you have to have been following
to predict the next move.

**Entry hazards.** Effects laid on the opponent's side that damage Pokémon as they
switch in. **Stealth Rock** is the famous one: floating stones that hurt anything
entering, scaled by its Rock weakness — so a 4×-weak Charizard loses half its HP just by
appearing. In `001` it is the thing an RNN forgot nine turns ago; in `007` it is a fact
the Pokédex knows about Charizard.

**Setup moves.** Moves that boost your own stats instead of attacking — **Swords Dance**
sharply raises Attack. Setup is only worth it when you can afford the turn. `019` uses
"Swords Dance six times against a Magikarp" as its picture of reward hacking: locally
adored by the judge, catastrophic in the match.

**Protect.** A move that blocks everything aimed at you for one turn. Cannot be relied
on repeatedly.

**Substitute.** A move that spends some of your own HP to put up a decoy that absorbs
attacks.

**Trick Room.** A move that inverts the speed order for five turns, so the slowest
Pokémon moves first. Whole teams are built around it — the Bronzong-and-Rhyperior team
in `051` is a textbook one. Recognising a Trick Room team from its roster is the example
`004` uses for what an encoder-only model is good at.

**Win condition.** The specific route by which a team plans to win. Identifying the
opponent's win condition is the multi-hop reasoning task in `013` and the strategic
inference in `016`.

**Metagame.** The prevailing set of popular teams and counters at a given moment. It
drifts, which is why `020` warns that a two-year-old collection of preference cards
trains you for last season.

**Flat Rules / Level 50.** A common competitive format that sets every Pokémon to Level
50 regardless of its actual level, so matches are decided by team and play rather than
by grinding. `005` makes this layer normalization, and the analogy is exact: the
rescaling looks only at the one Pokémon in front of it, and it destroys the advantage of
one runaway number.

**Regulation G.** A named ruleset for one season of official competitive play. Appears
once, in `047`, as an example of a query that is too specific to retrieve against.

**Tier (S / A / F).** Community shorthand ranking teams or Pokémon from best (S) to
useless (F). `051` uses tier letters as the label set for a few-shot classification task.

---

## The world and progression

**Gym.** A themed challenge building, usually specialising in one type. Beat it and you
get a badge. Gyms are stops on a fixed circuit, which is why `005` and `006` use "a Gym"
to mean one layer of a deep network and "the League" to mean the stack.

**Gym Leader.** The specialist who runs a Gym. Each is a genuine expert in exactly one
type and nothing else, which is what makes them the experts in `011`'s Mixture-of-Experts.

**Badge.** The token you get for beating a Gym. Eight badges qualify you for the Elite
Four. In `037` and `039` the eight badges are public benchmarks — standardised,
comparable, and thoroughly leaked.

**Gym Circuit.** The dataset's collective name for the eight badges taken as an exam
(`037`, `039`).

**Elite Four.** Four consecutive high-level Trainers you must beat back to back, with no
healing between them, after collecting all eight badges.

**Champion.** The final opponent, above the Elite Four, and the strongest Trainer in the
region. Throughout the dataset "Champion" means the large, expensive, strong model, in
contrast to the **rookie** (`031`, `033`) — and "the Champion's feedback reaching your
starter" is backpropagation through a deep stack (`005`, `006`).

**Victory Road.** The long, linear, one-way gauntlet leading to the Elite Four. `001`
uses it for strictly sequential processing: Pokémon 1, then 2, then 3, and by the end you
have forgotten why.

**Route.** Numbered stretches of land between towns. **Route 1** is the very first, home
to the weakest wild Pokémon. `006` puts "the Route 1 tutor who taught your Charmander to
Scratch" at the far end of the gradient path.

**Pewter City.** The town with the first Gym, Brock's (`016`, `039`).

**Kanto, Johto, Hoenn, Sinnoh, Unova, Kalos.** The regions of successive games. `044`
uses them purely as named spatial partitions of a map — the clusters of an IVF index.

**Tall grass / wild encounters.** Walking through grass triggers battles with wild,
untrained, unowned Pokémon. Nobody supervises this and nobody grades it. In this dataset
the wild grass is **always** pretraining (`018`, `019`, `025`, `029`, `036`, `040`).

**Pokédex.** The in-game encyclopedia listing every species, its types, and its
behaviour. The dataset's most heavily reused prop — see
[One term, several jobs](#one-term-several-jobs), because it does three different jobs.

**Pokémon Center.** A free clinic in every town that fully heals your party, and where
the PC boxes live. In `043` "how do I heal my Pokémon?" versus "where can I restore HP?"
is the canonical pair of queries with zero words in common and identical meaning.

**Poké Ball.** The device used to catch and carry a Pokémon. `002` numbers them, then
spins them, to build up absolute versus rotary positional encoding. A **Master Ball** is
the unique, never-fails, single-use version — `054`'s example of an irreversible action a
tool harness must guard.

**Fly.** A move that transports you instantly between towns you have already visited —
a sparse network of long-range shortcuts layered over the map you otherwise have to walk.
`044` maps it directly onto HNSW.

**TM (Technical Machine).** A consumable disc that teaches a move, identified by number
(`TM24`, `TM25`). The dataset uses TM identifiers as its running example of an **exact
code**: strings where semantic similarity is actively wrong, because `TM24` and `TM25`
are neighbours on the map and unrelated in fact (`043`, `045`, `047`).

**Potion / Super Potion / Antidote / Full Heal.** Healing items. A Potion restores HP; an
Antidote or Full Heal cures status conditions instead. `054` uses the distinction to show
that a tool description must say *when not to* use the tool.

**Daycare.** In the games, a facility that raises Pokémon for you. In `037` and `039` it
is a deliberately mundane job — *"you got all eight badges; you run a daycare"* — standing
for your actual production use case, which no public benchmark measures.

---

## Species named in the dataset

Only species that actually appear in `answers/pokemon/` are listed. The last column is
the point: why this particular creature and not another.

| Species | Type(s) | What it is | Why the dataset uses it |
| --- | --- | --- | --- |
| **Pikachu** | Electric | The mascot; a small Electric mouse, the default protagonist's Pokémon | The stand-in for "your model" whenever an answer needs a concrete actor. Its Thunderbolt against Water types is the dataset's canonical 4× matchup (`001`, `049`) |
| **Raichu** | Electric | Pikachu's evolution | Appears only in `043`, as an obviously-near-neighbour of Pikachu on the embedding map |
| **Gyarados** | Water/Flying | A huge sea serpent; Magikarp's evolution | The dataset's universal attention target: Water/Flying is **4× weak to Electric**, the single most extreme non-zero multiplier on the chart. Used in 18 questions |
| **Magikarp** | Water | Famously useless — a flopping fish whose only move is Splash — until it evolves into Gyarados at level 20 | The emergence and phase-transition example (`015`). Also the floor of usefulness generally: "six Magikarp" is an F-tier team (`051`), and you cannot distil a Champion into one (`031`) |
| **Golem** | Rock/Ground | A boulder with limbs | Ground types are **immune to Electric**. Golem is the dataset's 0× case — the thing attention must learn to give no weight at all (`001`, `003`, `008`) |
| **Ferrothorn** | Grass/Steel | A spiked, extremely defensive seed | Resists Water, resists Electric, and is 4× weak to Fire. The dataset's "the field changed, so the spotlight moved" example, and its stock awkward matchup (`001`, `013`, `017`, `053`) |
| **Charmander** | Fire | The Fire starter; a small lizard | The beginning of a chain: the thing at the bottom of the network that gradients have to reach (`005`, `006`) |
| **Charmeleon** | Fire | Charmander's middle evolution | The level-up in `006` where the "forget a move?" prompt appears |
| **Charizard** | Fire/Flying | Charmander's final evolution; a dragon-shaped fan favourite | Two properties do the work: it is a **fully evolved** endpoint (`007`), and Fire/Flying is 4× weak to Rock, so Stealth Rock halves it on entry |
| **Squirtle** / **Wartortle** / **Blastoise** | Water | The Water starter line | `043` uses Squirtle and Wartortle as an adjacent pair on the embedding map. `054` uses Blastoise as a Pokémon you *do not own* — the hallucinated tool argument |
| **Venusaur** | Grass/Poison | The Grass starter's final form; has a sun-boosted speed ability | Half of the Sun team in `051` |
| **Torkoal** | Fire | A tortoise whose ability automatically summons harsh sunlight | The other half of the Sun team in `051` — it is *why* the team is a Sun team |
| **Politoed** | Water | A frog whose ability automatically summons rain | The enabler of a Rain team (`016`, `051`) |
| **Kingdra** | Water/Dragon | A seahorse that can carry **Swift Swim**, doubling its Speed in rain | The payoff of a Rain team. "Politoed leads, Kingdra sweeps" is a *plan*, which is exactly why `016` uses it for the kind of prediction that requires strategy rather than recall |
| **Bronzong** | Steel/Psychic | A slow bell-shaped Pokémon that reliably sets Trick Room | Half of the Trick Room team in `051` |
| **Rhyperior** | Ground/Rock | Very slow, very heavy, very strong | The other half: slow attackers are what Trick Room exists to enable |
| **Tapu Fini** | Water/Fairy | A legendary guardian; a common competitive pick | `047`'s example of a query so specific ("what EV spread does Assault Vest Tapu Fini run in Regulation G?") that no document matches it word for word |
| **Milotic** | Water | An elegant serpentine Water type | `047`'s resolution of the pronoun "the other one" — the concrete referent a follow-up question needs |
| **Chansey** | Normal | Enormous HP, almost no Defence; a dedicated wall | `016`'s example of a Pokémon deliberately kept alive at 4 HP for a reason you had to have been watching to know |
| **Skarmory** | Steel/Flying | An armoured bird; another classic defensive wall | `017`'s misidentification: the Trainer decides turn 3 that a Ferrothorn is a Skarmory and then plays ten flawless turns against a Pokémon that does not exist |
| **Snorlax** | Normal | Famously huge and heavy; a giant sleeping bear | Two jobs: an unusual thing to run into in the wild (`018`), and the **outlier** — the one entry on the page whose value is 9,000 when everything else is 40–90 (`030`) |
| **Ditto** | Normal | A blob that transforms into whatever it faces; has no real identity of its own | `043`, where it sits alone on the embedding map "being weird" |
| **Eevee** | Normal | A small mammal famous for evolving into many different specialists | `037`, as the mundane real-world case ("a distressed Eevee") that no Gym badge tells you anything about |
| **Flareon** | Fire | One of Eevee's evolutions | `040` and `041`'s recall target — a species obscure enough that asking the model to remember a specific detail about it is unreliable, and handing it the page is not. Also the canary string `XQ7-FLAREON-9982` in `039` |
| **Growlithe** / **Arcanine** | Fire | A puppy and the large dog it evolves into | `007`'s minimum pair: a Pokédex too thin cannot tell them apart |
| **Rattata** | Normal | The weakest, most common early-route wild Pokémon | Low-quality training data. "1,000 real Gym battles beat 10,000 fights against wild Rattata" (`014`); also `035`'s trivial opponent nobody should plan forty turns against |
| **Zubat** | Poison/Flying | The bat that appears constantly and unwantedly in every cave | Sheer undifferentiated volume, alongside Rattata, in `018`'s wild grass |
| **Onix** | Rock/Ground | A rock snake; Brock's ace, and the first real wall a new player hits | The benchmark itself. "Can it beat Brock's Onix?" is `015`'s pass/fail cliff and `039`'s memorised exam |
| **Bidoof** | Normal | A weak, ubiquitous early-game beaver, affectionately regarded as a joke | The bottom of the range in `005`'s Flat Rules — a Level 12 Bidoof next to a Level 100 Garchomp, rescaled to the same footing |
| **Garchomp** | Dragon/Ground | A pseudo-legendary; genuinely top-tier | The top of that same range |
| **Mew** | Psychic | A mythical Pokémon, and the subject of the most famous fan urban legend in the series ("Mew is under the truck") | `043`'s obvious non-answer — the easy negative that teaches an embedding model nothing |

---

## People and groups named in the dataset

| Name | Who | Where and why |
| --- | --- | --- |
| **Brock** | Gym Leader of Pewter City; **Rock** type; his ace is Onix | The first Gym, so "beating Brock" is the entry-level benchmark everyone has taken and everyone has memorised (`015`, `037`, `039`). Also a Leader on the MoE roster (`011`) |
| **Misty** | Gym Leader of Cerulean City; **Water** type | `011`'s overworked expert: the receptionist sends everyone to Misty, she gets better, so more go to her, until she is fighting Dragons badly and the other 63 Leaders have forgotten how to battle. The dataset's picture of router collapse |
| **Wallace** | A **Water** specialist — Gym Leader of Sootopolis City, and Champion in one game | `011`'s second Water expert, so a challenger can be routed to two of them (top-2 gating) |
| **Blaine** | Gym Leader of Cinnabar Island; **Fire** type | On the `011` roster; also the answer's example of the expert specialisation you *hoped* for and did not get |
| **Surge** (Lt. Surge) | Gym Leader of Vermilion City; **Electric** type | On the `011` roster |
| **Agatha** | A member of the Elite Four; **Ghost** type | On the `011` roster |
| **Lance** | A member of the Elite Four, later Champion; **Dragon** type | On the `011` roster |
| **The Elite Four** | The four Trainers between the badges and the Champion | The gauntlet after the grind (`001`, `014`) |
| **The League** | The whole institution — Gyms, badges, Elite Four, Champion | Used for the model as a whole: "a hundred-Gym League" is a hundred-layer network (`005`, `006`), and a League of sixty-four Gyms is an MoE (`011`) |

---

## Moves, items and abilities named in the dataset

**Moves.** Most appear once or twice, as concrete filler where a real move name lands
better than a placeholder.

| Move | What it does | Where |
| --- | --- | --- |
| Thunderbolt | Strong reliable Electric attack | The dataset's default action, in 20+ answers |
| Thunder | Stronger, less accurate Electric attack; never misses in rain | `001`, `031` — the near-miss that shows a distilled ranking is richer than a label |
| Splash | Does nothing whatsoever; Magikarp's signature | The null action (`012`, `031`, `034`, `035`) |
| Ember / Flamethrower | Weak and strong Fire attacks | `006`'s early and late moveset entries; `026`'s forgotten Fire move |
| Growl / Leer / Smokescreen / Tackle / Scratch / Bite / Slash / Dragon Rage | Assorted early-game moves | `006`'s movesets, kept and rerolled |
| Surf / Waterfall / Aqua Tail / Rain Dance | Water moves | `026`'s Water-camp curriculum |
| Rock Slide | Rock attack | `026`'s achievable specialist gain |
| Power Whip | Strong Grass attack; a Ferrothorn staple | `016` |
| Volt Switch | Attack and switch out in one action | `034` |
| Quick Attack | Weak but always moves first | `053`, finishing off a Focus Sash |
| Earthquake | Powerful Ground attack that hits everything | `029`, `052` — the thing standing orders tell you not to switch into |
| Roost | Recovers HP; a Flying-type staple | `007`, as a Pokédex inference |
| Protect / Substitute / Swords Dance / Trick Room / Stealth Rock / Fly | See [Battling](#battling) and [The world](#the-world-and-progression) | |

**Held items.**

| Item | Effect | Where and why |
| --- | --- | --- |
| **Focus Sash** | Lets the holder survive one otherwise-fatal hit at 1 HP, then is consumed | The hidden fact the type-chart-only coach misses (`001`, `003`, `009`, `053`) |
| **Leftovers** | Restores a little HP every turn | A stock detail in the battle notebook (`008`, `042`) |
| **Damp Rock** | Extends rain by three turns; carried by rain teams | `027`'s LoRA adapter — a tiny object that specialises a Champion for wet weather without touching it |
| **Charcoal** / **Magnet** / **Mystic Water** | Each boosts moves of one type | `011` and `027`, as the swappable specialisation |
| **Assault Vest** | Boosts Special Defence but forbids status moves | `047`, inside the too-specific query |

**Abilities.**

| Ability | Effect | Where and why |
| --- | --- | --- |
| **Sturdy** | The holder survives a would-be one-hit KO at 1 HP | The dataset's canonical *second* thing to check. A coach who reads only the type chart walks straight into it (`001`, `003`, `009`) |
| **Swift Swim** | Doubles Speed in rain | The payoff half of a rain plan (`016`, `051`) |
| **Flash Fire** / **Guts** | Flareon's regular and hidden abilities | `040`, in the question the Trainer is asked to answer from memory |
| **Hidden Ability** | A rarer alternative ability some Pokémon can have | `040` — chosen because it is exactly the kind of detail that is stored fuzzily |

---

## Not actually Pokémon

Four proper nouns in the dataset look like species and are not.

| Term | What it really is | Where |
| --- | --- | --- |
| **Chinchilla** | The 2022 DeepMind compute-optimal scaling result. The Pokémon answer keeps the paper's name and treats it as a well-battled Level 70 Pokémon | `014` |
| **Gopher** | The larger, under-trained DeepMind model Chinchilla outperformed; here, a "candy-stuffed Lv280" | `014` |
| **SolidGoldMagikarp** | A real undertrained token from GPT-2/GPT-3's vocabulary that caused bizarre model behaviour. The dataset's "cursed tile" | `012` |
| **Big Steve** | A nicknamed Charizard, invented for the answer | `012` |
| **TM-4471**, `XQ7-FLAREON-9982` | Invented identifiers used as exact-match and canary strings | `039`, `045`, `047` |

---

## Recurring analogy conventions

This is the section that makes the dataset legible. These mappings are stable across
all 54 questions: once an answer establishes that a held item is an adapter, every later
answer means the same thing by it.

### Architecture

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| Query / Key / Value as "what I want", "what each Pokémon advertises", "what I get if I commit" | attention's Q, K, V | `001` |
| The type chart normalising raw effectiveness into one turn's plan | softmax over attention scores | `001` |
| The level cap on the calculation | the `1/√d_k` scaling factor | `001` |
| "You cannot target a Pokémon that hasn't been sent out yet" | the causal mask | `001`, `004` |
| **The coaching box** — several coaches watching one field, each paid to notice a different thing | multi-head attention; the head coach is `W_O` | `001`, `003`, `009` |
| The bench-warmer coach who has nothing to say | heads that mostly attend to nothing; the value of an attention sink | `003`, `008` |
| A **PC box** vs a **party** | an unordered set vs an ordered sequence | `002` |
| A numbered Poké Ball / a spinning Poké Ball | absolute vs rotary (RoPE) positional encoding | `002` |
| Fast-spinning and slow-spinning grooves on the ball | high- and low-frequency RoPE dimensions | `002` |
| The Judge / the Battler / the Interpreter | encoder-only / decoder-only / encoder-decoder | `004` |
| **Flat Rules, everyone set to Level 50** | layer normalization (and RMSNorm as "skip half the paperwork") | `005` |
| **A Gym** as one stop on the circuit | one transformer layer; the League is the stack | `005`, `006` |
| The scaler at the Gym *door* vs the Gym *exit* | pre-norm vs post-norm | `005` |
| **"Keep your moves"** — declining the level-up prompt | residual connections | `006` |
| The notice board every Gym pins to and nobody tears down | the residual stream | `006`, `007` |
| **The Pokédex** — each Pokémon looking itself up alone | the feed-forward block; where factual knowledge lives | `007` |
| The gated Pokédex ("is this relevant?" plus "how much?") | SwiGLU | `007` |
| **The battle notebook** — write each Pokémon down once, append as new ones appear | the KV cache | `008`, `009`, `013` |
| Coaches sharing one notebook | MQA (all share one) and GQA (grouped) | `009` |
| Six slots on your **belt** vs the **PC box** across town | on-chip SRAM vs off-chip HBM | `010` |
| The giant poster you never write | the materialised attention matrix | `010` |
| A running tally rescaled when a bigger score appears | the online-softmax rescaling trick | `010` |
| **The Gym Leader roster and the receptionist** | Mixture-of-Experts; the receptionist is the router | `011`, `032` |
| A fairness quota; a daily cap per Gym; turned-away challengers | load-balancing loss; expert capacity; dropped tokens | `011` |
| **Scoreboard tiles** you spell names out of | tokens and the vocabulary | `012` |
| A cursed tile with nothing behind it | an undertrained token | `012` |

### Training, scaling and alignment

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| **The wild grass** — months of unsupervised, ungraded encounters | pretraining | `018`, `019`, `025`, `029`, `036`, `040` |
| **Obedience school** — one week, a clipboard of worked examples | supervised fine-tuning / instruction tuning | `018`, `019`, `020`, `025`, `040` |
| **The coach** — showing pairs and saying which is better | RLHF | `016`, `017`, `018`, `019` |
| **Comparison cards** ("in this position, turn B beat turn A") | human preference pairs | `019`, `020`, `021`, `024` |
| **The judge** — a copy of your Pokémon retrained to score instead of battle | the reward model | `019`, `020`, `021`, `022`, `038` |
| **The photocopy** kept from obedience school | the frozen reference model; the KL penalty is "how weird was that, compared to the photocopy" | `019`, `020`, `022` |
| **Swords Dance six times against a Magikarp** | reward hacking / over-optimisation | `019`, `021` |
| The fourth Pokémon in the gym, predicting how the match is going | the value / critic model | `019`, `022` |
| The clip: no single match may move a habit more than a set amount | PPO's clipped objective | `022` |
| **Run the same battle eight times and average** | GRPO's group baseline | `022`, `023` |
| **The scoreboard** — "did the Gyarados actually faint?" | a verifiable, ungameable reward | `018`, `021`, `023`, `025`, `038` |
| A referee with a bug you can win through | reward hacking against a verifier | `023` |
| **The League rulebook**, cited by article number | a constitution (Constitutional AI) | `024` |
| **Rare Candy vs actual battles** | parameters vs training tokens | `014` |
| **Magikarp → Gyarados at level 20** | emergence; and a pass/fail benchmark manufacturing a cliff out of smooth progress | `015` |
| Studying **Champion replays**, rewound to the Champion's position each turn | teacher forcing, and the exposure bias it leaves | `017` |
| **The four-move limit**, in a version where the game never asks | catastrophic forgetting | `026` |
| **Specialist camp** | full fine-tuning | `026`, `027`, `029`, `041` |
| **A held item** | a LoRA adapter — frozen base, tiny trainable object, swappable, initialised to no effect | `026`, `027`, `028`, `029` |
| Fusing the item into the Pokémon | merging adapter weights back into the base | `027`, `028` |
| **Shorthand** — writing every stat more coarsely | quantization | `028`, `030`, `044` |
| **The Snorlax on the page** — one entry at 9,000 when the rest are 40–90 | outliers, and why per-tensor scaling fails | `030` |
| **The Champion teaching the rookie** its full ranking, not just its pick | knowledge distillation on soft targets | `031`, `029` |
| Snipping lines / two-of-every-four / tearing out pages | unstructured, 2:4 semi-structured, and structured pruning | `032` |
| The lottery ticket hidden in a fat Pokédex | the lottery ticket hypothesis | `032` |
| **The rookie guesses, the Champion checks in one flip** | speculative decoding | `033` |

### Decoding and evaluation

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| How boldly the Pokémon plays | sampling temperature; top-k, top-p and min-p as which options it will consider | `034` |
| Carrying three game plans forward and pruning | beam search | `035` |
| **How surprised the Trainer is, every turn** | perplexity — and the observation that coaching makes it *worse* | `036` |
| **The Gym Circuit / eight badges** | public benchmarks: standardised, comparable, saturated and leaked | `037`, `039` |
| **Your daycare** | your actual production task, which no badge measures | `037`, `039` |
| **The tapes / the training footage** | the pretraining corpus | `016`, `017`, `036`, `039`, `040` |
| A **Champion in the referee's chair** | LLM-as-a-judge, with position, length, self-preference and style biases | `038` |
| Planting a nonsense code word in the exam paper | a canary string for contamination detection | `039` |
| Comparing scores on pre-cutoff and post-cutoff battles | the cleanest contamination signal there is | `039` |
| Inventing Flareon's ability, confidently | hallucination — five distinct failures under one name | `040` |

### Retrieval

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| **Handing the Trainer the Pokédex mid-battle** | RAG — converting a memory question into a reading question | `040`, `041` |
| **Scouting reports** | your document corpus | `029`, `041`, `042`, `045`, `046`, `047`, `048`, `052` |
| **Cutting the reports into cards** | chunking. "File by the small card, hand over the big one" is small-to-big retrieval | `042` |
| Writing the section heading on every card | heading-augmented / contextual chunking | `042` |
| Reading the whole report first, *then* cutting | contextual chunking with a full-document view | `042` |
| **The map**, where similar things stand near each other | embedding space | `043`, `044`, `045`, `047` |
| Pushing against things that are *almost* right | hard negative mining | `043`, `046` |
| **The Fly network**, layered from cities to footpaths | HNSW | `044` |
| **Regions** (Kanto, Johto, Hoenn…) each with a centre | IVF partitioning, and the border problem is the recall loss | `044` |
| Shorthand coordinates, then full coordinates for the survivors | product quantization plus exact rerank | `044` |
| **The Literalist** | keyword / BM25 search — perfect on codes, helpless with paraphrase | `045` |
| **The Cartographer** | dense vector search — good at meaning, bad at exactness | `045` |
| Combining by rank rather than by score | reciprocal rank fusion | `045` |
| **The filing clerk** — writes one index card per report, months in advance | a bi-encoder | `045`, `046` |
| **The coach** — reads the question and one report side by side | a cross-encoder reranker | `045`, `046`, `048` |
| One card per *line* of the report | late-interaction retrieval (ColBERT-style) | `046` |
| **Writing a fake answer and searching with that** | HyDE | `047` |
| "What about the other one?" rewritten to "What about Milotic?" | query rewriting and coreference resolution | `047` |
| **Scout vs Trainer** | retriever vs generator, measured separately | `048` |
| "Was the right report even in the fifty?" | retrieval recall as a hard ceiling on the whole system | `045`, `048` |

### Prompting, reasoning and agents

| Pokémon term | Stands for | Questions |
| --- | --- | --- |
| **Talking through the damage calc out loud** | chain-of-thought | `016`, `049` |
| "One moment of thought per thing you say" | fixed compute per token; each generated token buys another forward pass | `016`, `049` |
| A narrated chain that never mentions the real reason | unfaithful reasoning — a thinking tool, not a confession | `049` |
| **Six calcs and a vote** | self-consistency | `050` |
| **Three examples, then a tier letter** | few-shot in-context learning; the wrong-labels experiment shows the examples select a task rather than teach one | `051` |
| "That happened before — what followed it?" | induction heads, and the visible kink where the ability appears | `003`, `015`, `051` |
| **The bag** — everything the Trainer carries into the stadium | the context window | `052`, `053`, `054` |
| Sending a scout off with their own empty bag | subagents / context isolation | `052` |
| Pre-packing the unchanging pages at the top | prefix caching | `008`, `052` |
| **Think, act, look, repeat** | ReAct | `053` |
| 0.95 per turn compounding to 13% over forty turns | why long agent trajectories fail | `053` |
| **"The Trainer shouts, you throw the ball"** | tool calling: the model emits a request, the harness executes it. Every safety property lives in the harness | `054` |
| Only letting them say words that could still form a valid command | constrained decoding / grammar-guided sampling | `054` |
| A note planted in what you report back | prompt injection through tool output | `054` |

---

## One term, several jobs

A few props are reused for different technical objects in different questions. The
answers are consistent within themselves; this table is here so you do not carry the
wrong reading across.

| Prop | Meaning A | Meaning B | Meaning C |
| --- | --- | --- | --- |
| **The Pokédex** | the feed-forward block, where knowledge is stored (`007`) | the model weights being rounded, pruned or flipped through (`030`, `032`, `033`) | the retrieved documents handed over at battle time (`040`, `041`) |
| **The coach** | RLHF — the person who grades pairs (`018`, `019`) | one attention head in the coaching box (`001`, `003`) | the cross-encoder reranker that reads question and report together (`045`, `046`) |
| **The notebook** | the KV cache (`008`, `009`, `013`) | the Judge's notes that the Battler glances at — cross-attention (`004`) | |
| **The photocopy** | the frozen reference model in RLHF (`019`, `020`, `022`) | a cached copy of the shared prompt prefix (`008`) | |
| **The scoreboard** | a verifiable reward (`018`, `023`) | the vocabulary you spell names out of (`012`) | a pass/fail benchmark that manufactures cliffs (`015`) |
| **Camp** | full fine-tuning (`026`–`029`, `041`) | a short refresher after merging KV heads — uptraining (`009`) | |
| **Shorthand** | weight quantization (`028`, `030`) | compressed KV representations (`009`) | coarse vector codes for search (`044`) |
| **The rookie** | the small draft model in speculative decoding (`033`) | the small student in distillation (`031`) | a weak model generally, which chain-of-thought can make worse (`030`, `049`) |
| **The judge** | the learned reward model (`019`–`022`) | an LLM grading outputs at eval time (`038`) | |

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
