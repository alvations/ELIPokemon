---
id: "001"
slug: attention-mechanisms
style: pokemon
category: transformers
difficulty: core
question: "Can you explain the concept of attention mechanisms in transformer models?"
tags: [attention, self-attention, transformers, qkv, softmax]
---

# Attention, but it's a Double Battle

An attention mechanism is a Trainer choosing which enemy Pokémon to target based on the whole
field, instead of blindly hitting whatever is closest.

Older models (RNNs, LSTMs) fought like the Victory Road gauntlet: Pokémon #1, then #2, then
#3, strictly in order, and by the time you reached the Champion you had forgotten what your
strategy was. A transformer walks into the stadium and sees **the entire opposing team at
once**, then works out exactly where to point.

## The core idea: reading the field ⚔️

You are in a Double Battle. Your active Pokémon is **Pikachu**. Across the field stand
**Gyarados** (Water/Flying) and **Golem** (Rock/Ground).

Pikachu does not treat them as equals. Its attention lights up:

* **90% on Gyarados** — Electric hits Water/Flying for 4× damage.
* **10% on Golem** — Ground immunity means Electric does literally nothing.

Now put a **Grass** move in Pikachu's mouth instead. The spotlight *inverts on its own*:
Grass hits Golem's Rock/Ground for 4×, while Gyarados's Flying half resists it back down to
neutral. Same two Pokémon, same field — opposite answer. Nothing about Pikachu changed. The
*question* changed, and the attention followed.

## Query, Key, Value: the Pokédex lookup 🎒

```
                    ┌──────────────────────────────────────┐
                    │        YOUR SIDE: Pikachu ⚡         │
                    │   Query: "I want to Thunderbolt.     │
                    │           Who does that hurt?"       │
                    └───────────────┬──────────────────────┘
                                    │
              ┌─────────────────────┴─────────────────────┐
              ▼                                           ▼
   ┌────────────────────────┐              ┌────────────────────────┐
   │ 🌊 GYARADOS            │              │ 🪨 GOLEM               │
   │ Key:   "Water/Flying"  │              │ Key:   "Rock/Ground"   │
   │ Match: SUPER EFFECTIVE │              │ Match: NO EFFECT       │
   │ Score: 4×              │              │ Score: 0×              │
   └───────────┬────────────┘              └───────────┬────────────┘
               │                                       │
               ▼          ── type chart ──             ▼
          weight 0.90                             weight 0.10
               │                                       │
   ┌───────────▼────────────┐              ┌───────────▼────────────┐
   │ Value: 331 HP, about   │              │ Value: shrugs, sets    │
   │ to faint, no Sturdy    │              │ up Stealth Rock        │
   └───────────┬────────────┘              └───────────┬────────────┘
               └───────────────┬───────────────────────┘
                               ▼
                    TURN OUTCOME = 0.90 × Gyarados' Value
                                 + 0.10 × Golem's Value
                    → Thunderbolt goes into Gyarados. 💥
```

* 🔍 **Query (Q)** — what your active Pokémon *wants*. *"I'm holding an Electric move. Who is
  weak to this?"*
* 🏷️ **Key (K)** — what each Pokémon on the field *advertises*: its typing, the label on its
  Pokédex entry. *"I am Water/Flying."*
* 📦 **Value (V)** — what you actually *get* if you commit to that target: its real HP, its
  ability, whether it faints.

## The battle calculation

1. **Type matchup (Q × K).** Compare Thunderbolt against every typing on the field. Raw
   effectiveness scores come out.
2. **Effectiveness multiplier (softmax).** The type chart normalises those scores into one
   plan for the turn — 4× becomes "almost all my focus", 0× becomes "ignore". The percentages
   always add up to one full turn, because you only *get* one turn.
3. **The attack (× V).** You unleash the full Value of the move into the target you picked
   and leave the immune one alone.

The **√d_k** scaling is the level cap. Without it, a level 100 Pokémon's numbers dwarf
everything and every calculation collapses to "always hit that one" — you stop reading the
field and just spam. Dividing keeps the matchups on a sane scale so subtler advantages still
register.

The **causal mask** is the rule that you cannot target a Pokémon that hasn't been sent out
yet. Turn 4 sees turns 1–4. It does not get to peek at the ace in the back.

## Multi-head attention: the coaching box 👥

At a real tournament you don't just read typings. Multi-head attention is having several
coaches in your ear at the same time, each watching a different thing:

* 🧪 **Head 1 — the Type Expert:** *"Gyarados is Water/Flying, 4× damage, go."*
* 🛡️ **Head 2 — the Ability Scout:** *"Careful, Golem might have Sturdy — it survives on 1 HP."*
* 🌧️ **Head 3 — the Weather Tracker:** *"Rain is up. Thunder never misses this turn."*
* 🎽 **Head 4 — the Item Watcher:** *"That Gyarados is holding a Focus Sash."*

Each coach independently ranks the field. You listen to all of them **at once**, combine
their advice, and make one decision. That is why one head is not enough: the Type Expert
alone would walk you straight into a Sturdy Golem.

## Why the old way lost

An RNN Trainer had to remember the entire battle in their head, one turn at a time, and
inevitably forgot that the enemy set up Stealth Rock nine turns ago. Attention lets any turn
look directly at any other turn, one hop, no forgetting.

The cost: with a full team on a huge field, you compare *everyone* to *everyone*. Six
Pokémon is easy. A stadium of a thousand is where the battle timer runs out — which is why
so much of the field's engineering is about scouting smarter instead of scouting everything.
