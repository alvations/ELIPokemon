---
id: "120"
slug: contrastive-image-text-pretraining
style: pokemon
category: multimodal
difficulty: intermediate
question: "How does contrastive image-text pretraining like CLIP actually work?"
tags: [clip, infonce, contrastive, temperature, siglip, zero-shot]
---

# Who's that Pokémon?

A silhouette. A shape with no colour and no detail, and four seconds to name it.

Nobody ever taught you that game by handing you a labelled photograph of every species. You
learned it by being shown **a shape and a set of possible answers**, over and over, until the
shapes and the names lived in the same part of your head.

That is the entire training method. Two separate skills — *seeing shapes* and *reading Pokédex
entries* — drilled until they agree on where things are.

## The lineup 🎴

Put a row of silhouettes on one wall and a row of Pokédex entries on the other, shuffled. Every
silhouette has exactly one entry that belongs to it. Match them.

```
                 entry A     entry B     entry C     entry D
   silhouette 1 [  ✓   ]       ·           ·           ·
   silhouette 2    ·        [  ✓   ]       ·           ·
   silhouette 3    ·           ·        [  ✓   ]       ·
   silhouette 4    ·           ·           ·        [  ✓   ]

   pull each ✓ together.  push every · apart.
   and do it BOTH WAYS — shape→entry, and entry→shape.
```

📌 **The wrong answers are the lesson.** Nobody had to write them; they are just the other
Pokémon already on the wall. Put four species up and the game is trivial. Put up **four hundred**
and every round is a real test — the wall *is* the difficulty, and it costs nothing to make it
bigger.

Grading both directions matters too. Drill only shape→entry and you get a Trainer who can name
any silhouette and cannot, given a Pokédex entry, pick out the Pokémon it describes.

## Do not let the quizmaster just get stricter 🎚️

There is a dial for how harshly near-misses are punished. Turn it up and the scores look better
immediately — the quizmaster is simply being more decisive, not the student being more right.

⚠️ Left free, the dial runs to the ceiling and stays there, because *sharpening* is the cheapest
way to look correct. It gets capped for the same reason a Trainer cannot use **Swords Dance** more
than three times before hitting +6: past the cap, more confidence is not more skill.

## The wall does not have to be one wall 🧾

There is a second way to run the drill: instead of *"which of these four hundred entries goes with
this shape"*, ask **"does this entry go with this shape — yes or no?"** — one pair at a time,
independently.

Same skill, no lineup required. You no longer need four hundred candidates present simultaneously
to make the round hard, which matters enormously when the wall is spread across a dozen different
Gyms and they all have to agree before anyone can be graded.

## Then it names things it was never drilled on 🔮

Here is the payoff. Once shapes and words live in the same place, **naming becomes matching.**

```
   candidates ─► "a Pokémon known as {name}, seen in the wild" ─► the reading skill ─► 📖📖📖
   the shape  ─────────────────────────────────────────────────► the seeing skill  ─► 👁️
   answer = whichever entry the shape lands nearest
```

And note the phrasing, because it is not decoration. **A bare name works noticeably worse than a
sentence.** The drill was done on Pokédex *entries* — "It is said to melt any material", "Its wings
can carry it close to an altitude of 4,600 feet" — full sentences, every one of them. Hand the
reading skill a lone word like `Golbat` and you have handed it something it has never seen in its
life. Wrap the name in a sentence shaped like an entry and it lands where it belongs.

## Where the silhouette game breaks 🚨

* **🔀 Word order does nothing.** *"Charizard standing behind Blastoise"* and *"Blastoise standing
  behind Charizard"* read as very nearly the same thing. The drill never once required knowing
  which was in front — both entries contained both names, and matching worked fine either way. So
  it never learned. The same hole eats **counting**: a cave of Zubat is "Zubat", whether there are
  three or thirty.
* **🦋 It knows the family, not the member.** "A butterfly Pokémon" — easy. *Which* Vivillon
  pattern, out of all the regional wing designs? It never had to care, because the entries almost
  never said.
* **🎭 Impostors are genuinely hard, and that is correct.** **Ditto** mid-Transform, **Zoroark**
  under Illusion, **Mimikyu** in its Pikachu rag: three silhouettes that are *supposed* to match
  the wrong entry. These are the most valuable rounds on the wall, and the ones a shape-only
  reading will always get wrong — the tell is never in the outline.
* **📚 Studying with the answers visible.** If the quiz shapes were already on your practice wall,
  your score is memory, not skill. Check what was on the wall before believing any number.

## And everything downstream inherits all of it 🧬

This drilled eye usually becomes the **frozen lens** bolted onto a talking Pokédex (question 117).
So the holes travel. Build on an eye that never learned front-from-behind, and no amount of
eloquence in the voice will fix it — you will get beautifully worded sentences that put Zapdos on
the wrong side of the sky, forever.
