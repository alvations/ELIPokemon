---
id: "009"
slug: mqa-and-gqa
style: pokemon
category: inference
difficulty: intermediate
question: "Explain Multi-Query Attention and Grouped-Query Attention."
tags: [mqa, gqa, kv-cache, inference, llama]
---

# One scouting report, eight coaches

Your coaching box has eight coaches. Each one watches the field for a different thing — types,
abilities, weather, items. Good.

But right now, **each coach keeps their own private notebook** on every Pokémon that's appeared.
Eight coaches × forty Pokémon = eight thick notebooks of largely the same information. The
Type Expert wrote "Gyarados: Water/Flying, holding Sash." The Weather Tracker wrote "Gyarados:
Water/Flying, holding Sash." So did everyone else.

That's a lot of desk for one fact.

```
  🗂️ EIGHT NOTEBOOKS (MHA)      📔 TWO SHARED (GQA)         📄 ONE SHARED (MQA)

  🧪📓 🛡️📓 🌧️📓 🎽📓          🧪🛡️🌧️🎽 ─┐    📊🧠😴🎯─┐    🧪🛡️🌧️🎽📊🧠😴🎯
  📊📓 🧠📓 😴📓 🎯📓                     │              │           │
                                        📓             📓          📓
  Everyone writes                  four coaches   four coaches   all eight share
  everything, separately            share one      share one      the one notebook

  desk: 8 units                    desk: 2 units               desk: 1 unit
  quality: perfect                 quality: basically perfect  quality: noticeably worse
```

## The key insight 🔑

The coaches' **opinions** must stay separate — that's the entire value of having eight of them.
The Ability Scout and the Weather Tracker must be allowed to reach different conclusions.

But the **raw facts** they're each writing down? Almost identical. Gyarados is Water/Flying no
matter who's looking.

So: keep eight independent opinions, share the notebook they're written from. Eight coaches,
one filing cabinet.

## Sharing too hard 📄

**One notebook for all eight (MQA)** is the aggressive version. Desk space plummets, and you
can now run thirty battles at once instead of four.

But something is lost. Each coach used to record facts in the format *they* found useful — the
Ability Scout jotting a note about Sturdy that the Type Expert would never have bothered with.
Force everyone into one shared format and the notes drift toward the generic. The coaches still
disagree, but they're now disagreeing about a blander summary. Play matters.

## The compromise that won 🤝

**Two or four shared notebooks (GQA).** Coaches team up in small groups; each group keeps one
notebook in a format that suits them.

Nearly all the desk savings. Nearly none of the quality loss. This is what basically every
serious modern team runs.

And there's a lovely retrofit: if you already trained a squad with eight separate notebooks,
you don't start over. **Merge** them in groups — average the four Type-ish notebooks into one —
and run a short refresher camp, about 5% of the original training. The coaches adjust in a week.

## Which one do you want? 🎯

* 🏆 **Eight notebooks** — one high-stakes exhibition match, quality above all, desk space is
  free. Rare.
* ✅ **Grouped** — you're running a tournament circuit and need throughput without dropping
  games. The default answer.
* 🚀 **One notebook** — you're running *hundreds* of casual battles simultaneously and a slightly
  worse call now and then is fine.

There's also a clever variant where instead of sharing notebooks, each coach writes in
**shorthand** and expands it back out when they need it. Tiny desk footprint, a bit of extra
thinking per turn, and if you design the shorthand well it can beat grouping outright.

One last thing worth knowing: none of this helps you **read the team sheet** at the start. Eight
notebooks or one, you're scouting the same roster. This trick is entirely about the long grind
of turn-by-turn play.
