---
id: "104"
slug: language-sampling-pretraining
style: pokemon
category: multilingual
difficulty: intermediate
question: "How do you sample languages when pretraining on an imbalanced multilingual corpus?"
tags: [sampling, temperature, unimax, data-mixture, pretraining]
---

# Who gets the Exp. Share?

Six on the team. One journey's worth of experience to hand out. How you split it decides who
this team actually is.

**Hand it out by what shows up in the grass** and your Charizard eats everything. Route 1 is
Rattata and Pidgey; the Safari Zone is a hundred Nidoran; your Charizard sweeps all of it and
takes the experience for all of it. Meanwhile the Larvitar you caught in Mt. Silver has fought
twice, ever.

```
   🌿 BY WHAT'S IN THE GRASS        ⚖️ SOFTENED              👥 STRICTLY EQUAL

   Charizard  ████████████         Charizard  █████        Charizard  ██
   Pidgeot    ██                   Pidgeot    ███          Pidgeot    ██
   Larvitar   ▏                    Larvitar   ██           Larvitar   ██
   Ninetales  ▏                    Ninetales  ██           Ninetales  ██

   Larvitar never leaves           everyone gets a          Larvitar has three
   the PC box.                     turn.                    routes and grinds them
                                                            four hundred times.
```

## Both ends are a trap 🪤

Straight by-the-grass and half your team never battles. Strictly equal is worse than it looks:
Larvitar only has **three routes** available to it, so equal shares mean walking those same
three patches four hundred times.

And that is not training. That is **memorising Route 10**. Your Larvitar becomes flawless at
the exact Geodude that stands on the exact tile — and clueless the moment anything else appears.
It looks brilliant on the only test you have, because the test is the tile it memorised.

## The usual compromise 🎚️

One dial. All the way one way, the grass decides. All the way the other, everyone splits it
evenly. Most Trainers park it somewhere in between and stop thinking about it — and that is
genuinely most of the value, so it is a reasonable place to stop.

## The better question ♻️

The dial hides the thing you actually care about. It answers *"how big a share does Larvitar
get?"* when the question that bites is *"how many times am I walking Larvitar through Route 10?"*

So set **that** instead:

> Split it as evenly as you can — **but nobody walks the same route more than four times.**

Once Larvitar has done its three routes four times each, it is finished; its share goes to
whoever still has fresh ground to cover. That single change beats fiddling with the dial,
because four passes over new grass is worth roughly what one pass is, and the fortieth pass
over the same grass is worth **nothing at all**. Worse than nothing — the Geodude on that tile
is now in your team's test set as well as its training.

## Two things that quietly ruin it 😖

**🧹 Cleaning hurts the rare ones most.** Sensible rule: throw out any battle log that looks
malformed. But the tidy, well-formatted logs all come from the big Kanto stadiums. Village
matches on Route 10 were written up in a notebook by one person, so the filter deletes those
first — and Larvitar's three routes become one. **Filter, then split, then go and check the
tail survived.**

**🔁 Copying multiplies the rubbish, not just the training.** If a third of Larvitar's three
routes are mislabelled — a Graveler recorded as a Golem, a Ninetales entered as Vulpix —
walking them forty times does not average the errors out. It teaches them forty times as hard.

📌 Both ends of the dial are a way of losing a Pokémon. One leaves Larvitar in the box; the
other marches it around one field until it has learned the field instead of the game.
