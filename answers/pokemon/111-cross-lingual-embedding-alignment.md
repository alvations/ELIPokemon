---
id: "111"
slug: cross-lingual-embedding-alignment
style: pokemon
category: multilingual
difficulty: intermediate
question: "How do embedding spaces for different languages get aligned?"
tags: [muse, procrustes, csls, isomorphism, bilingual-lexicon, hubness]
---

# Two regions drew the same map and labelled it differently

Kanto's professors laid out every Pokémon they know by how alike they are. Sinnoh's professors
did the same, separately, never comparing notes.

Both maps have the same **shape**. On each one, the little Fire starter sits next to the middle
Fire starter, which sits next to the big one. The pseudo-legendary Dragons cluster in a corner.
The Water birds are down near the coast. Neither professor arranged it — the arrangement fell
out of what the Pokémon are.

What differs is the **orientation**. Kanto's map has Charmander in the north-east. Sinnoh's has
Chimchar in the south-west. Nobody agreed on which way is up.

## Rotating one onto the other 🧭

You do not redraw anything. You **spin** Sinnoh's map until it lands on Kanto's.

To do it you need a handful of pairs you already know match:

```
   known anchors:   Charmander ── Chimchar      (little Fire starter)
                    Charizard  ── Infernape     (final Fire starter)
                    Gyarados   ── Gyarados      (identical, both regions)
                    Dratini    ── Gible         (the slow-burn Dragon)

              rotate ─────────────────────────────►

   and now:         Bulbasaur  ── Turtwig        ✅ falls out for free
                    Squirtle   ── Piplup         ✅ never told it this
```

Four anchors, one spin, and the rest of the map answers itself. **Spin only** — never stretch,
never squash. Stretching lets you force the anchors to line up while wrecking everything
between them, and the whole value is in the parts you did not label.

Then go round again: take the matches you are most confident about, add them to the anchor
list, re-spin. Four anchors becomes forty, forty becomes four hundred.

## Two ways it goes wrong 💥

**🟣 Ditto is everybody's nearest neighbour.**

Ask "which Sinnoh Pokémon is closest to Charmander?" and you get Ditto. Ask about Snorlax — Ditto.
Ask about Wailord — Ditto. Ditto Transforms into anything, so it sits plausibly near everything,
and a naive lookup returns it forever.

The fix is not a better map. It is a **crowding penalty**: any Pokémon that shows up as
everyone's neighbour has its closeness discounted. That single correction buys more than any
amount of extra spinning.

**📐 Some pairs of regions were never the same shape.**

Kanto and Johto rotate onto each other beautifully — the same species, the same ecology, half
the same routes. Kanto and Alola do not. Alola's Vulpix is Ice. Alola has Ultra Beasts and no
one else does. Its map has regions with nothing to correspond to, so there is no rotation that
works, and forcing one produces confident nonsense.

The distant regions are exactly the ones you most wanted to reach. And the honest fix is
unglamorous: **go and hand-label five hundred pairs.** A small list of pairs you actually
checked beats every clever spin on the pairs where clever spinning fails.

## Where this ended up 🏁

Mostly, professors stopped drawing separate maps. If Kanto and Sinnoh survey the world together
from the start, there is one map and nothing to rotate.

The spinning still matters in three places: regions so small nobody surveyed them; slotting a
newly discovered species onto a map already drawn; and as the clearest possible statement of
what "one shared map" was ever really promising — **the same shape, roughly, where the regions
happen to overlap.**
