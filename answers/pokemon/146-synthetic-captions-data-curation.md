---
id: "146"
slug: synthetic-captions-data-curation
style: pokemon
category: multimodal
difficulty: advanced
question: "Why do multimodal models train on synthetic captions instead of web alt-text?"
tags: [synthetic-data, recaptioning, alt-text, filtering, model-collapse, curation]
---

# What Trainers actually write under their photographs

Go through a shoebox of other people's **Pokémon Snap** photographs and read what is written on the
back.

*"Route 4."* *"IMG_204."* *"cool!!"* *"taken with my new camera."* Half of them say nothing at all.
One of them names the photographer rather than the Pokémon. And even the *good* ones say
**"Gyarados"** when the shot also contains three **Magikarp**, a **Poliwag**, and the **Old Rod**
that caught them.

That is the original supply of training material, and it is dreadful.

## So write better ones 📝

Send a describer round the whole shoebox and have it write a proper entry for every photograph:

```
   what was on the back:  "Route 4, nice one"

   what the describer writes:
       "A Sandshrew curled defensively at the mouth of a cave, three Zubat
        overhead, dusk light, a Poké Ball dropped in the sand to its left."
```

📌 Now every phrase corresponds to **something actually in the photograph**. The Pokédex can finally
learn which attribute belongs to which Pokémon, how many there were, and what was to the left of
what — precisely the things it could never learn from *"cool!!"*, and precisely the things that were
missing in questions 120 and 128.

## Do not throw the shoebox away 📦

⚠️ Train on **nothing but** the describer's entries and you have built a Pokédex that understands
**one describer**. Its phrasing, its habits, its blind spots. Then a real Trainer walks up and says
*"cool bug thing"* and it has never heard anybody talk like that in its life.

So keep a slice of the originals in the mix. Most recipes lean heavily on the rewritten ones and
deliberately hold back a fraction of the scrappy real ones — the exact proportion is worth testing
on your own shoebox, but **keeping some is not optional.**

Same for **length**. Feed it only sixty-word descriptions and it will handle a three-word request
badly. Mix long and short deliberately.

## And here is how it poisons itself ☠️

**The describer hallucinates, and the hallucination becomes the truth.**

Recall question 122: shown a **Charmeleon**, a describer with a well-practised voice writes about
the wings. Charmeleon has no wings — **Charizard** does, and that is the whole point of the last
evolution. And now that sentence is not a mistake in an answer somebody reads once — **it is a
training label**, and the next Pokédex learns it as fact. It will write the same thing about every
**Quilava**, every **Monferno**, every mid-stage Fire type it ever sees.

⚠️ The nasty part is that it is not random noise. Noise averages out. **The describer gets it wrong
the same way every single time**, so the same false claim is stamped across a million photographs
and reinforced rather than cancelled.

What actually helps:

* **👀 Read two hundred of them yourself.** Dull, and it catches more than any automatic check.
* **🧑‍⚖️ Have a *different* describer mark the work.** Asking the one that wrote the entries whether
  the entries are right is asking a Pokémon to referee its own battle.
* **✂️ Prefer short and factual over long and lyrical** where accuracy matters. Invention grows with
  length here exactly as it does everywhere else.
* **🏷️ Write down *which* describer produced each entry**, so you can find them all and redo them
  when you get a better one.

## The rest of the sorting 🗂️

Rewriting captions is one stage. Around it: throw out the near-identical photographs, or the same
shot filed six times gets six votes. Screen for what must never be in the pile at all, first,
before anything else. Handle faces and personal details. Check what you are allowed to use. And
make sure the photographs you plan to **test** with are not sitting in the training pile — which,
for pictures, means matching them by how they *look*, not by filename.

## Is this the archive eating itself? 🐍

There is a real worry that training on generated material degrades a model as each generation
learns from the last.

📌 **This is not that.** The **photographs are real.** Every one is a genuine **Sandshrew**, a
genuine **Lapras**, a genuine **Snorlax** asleep across a road, that somebody genuinely
photographed. What is generated is the *writing underneath* — produced by a
strong describer **looking at that real photograph**. Nothing is being invented out of nothing;
knowledge is being copied from a stronger reader into a weaker one.

The risk here is **inheriting the describer's errors and habits**, which is real, serious, and a
completely different problem from the archive eating itself. Be clear which one you are worried
about, because the fixes are not the same.
