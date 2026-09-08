---
id: "192"
slug: multimodal-monitoring
style: pokemon
category: multimodal
difficulty: advanced
question: "How do you monitor a multimodal system in production?"
tags: [monitoring, drift, silent-failure, canaries, alerting, incident-response]
---

# Nothing is on fire, and it has been wrong since Tuesday

Testing tells you how the Pokédex behaves on a set **you** chose. The field tells you how it behaves
on the world, and **the world changes without sending word.**

📌 And here is what makes this different from watching an ordinary service: **the failures are
silent.** Nothing errors. Nothing is slow. Fluent, confident, wrong entries flow out at full speed,
and every dashboard is green.

It is **Toxic**, not a knockout. On the turn it lands it takes a sixteenth and shows nothing; by
the time anybody notices, it is taking a quarter. The Pokédex is not broken. It has been quietly
telling Trainers that **Charmeleon** has wings since Tuesday.

## Four things drift 🌊

```
   1. 📥 WHAT COMES IN     a new camera. A new app version. A partner who used to
                           send photographs and now sends scanned pages.

   2. 🌍 THE WORLD ITSELF  the Celadon Department Store gets refurbished and every
                           directory board looks different from Tuesday onward.
                           Route 3 is rerouted. The Town Map is reprinted.

   3. 🔄 THE POKÉDEX       somebody updates the hosted model underneath you
                           (question 187's change-control problem, arriving uninvited)

   4. ⚙️ THE PLUMBING      a resize step changes. A library starts honouring the
                           rotation tag that another part still ignores.
```

⚠️ **Number four causes more real incidents than the model ever does**, and it is completely
invisible to anything watching the model.

## What to actually watch 👀

**📥 On the way in** — this is your early warning:

* how big the pictures are, what shape they are, how large the files are;
* how many are documents, how many are photographs, how many are screenshots;
* **how far the incoming pictures sit from the ones you trained on** — cheap to compute and
  remarkably sensitive;
* pictures that fail to open, and pictures arriving sideways.

**📤 On the way out:**

* **how long the answers are.** ⚠️ Suddenly shorter usually means it is refusing; suddenly longer
  usually means it has started hedging (question 167);
* **how often it refuses** — tracked in **both** directions (question 139);
* whether the citations still point at anything real;
* and whether it has started repeating itself (question 136).

**🚶 And what Trainers do**, which is what actually tracks harm:

* asking again, rewording, walking closer, **giving up and reaching for the Town Map instead**
  (question 189);
* how often somebody escalates to a person;
* and the cost per question — ⚠️ **a cost drift is very often the first visible sign that routing
  changed underneath you.**

## Send the same Pokémon out every hour 🐤

📌 **This is the highest-value control on the page, and most teams do not have it.**

Keep a small fixed set of pictures whose correct answers you already know — a **Charizard** that is
definitely a Charizard, a **TM26** label, six **Voltorb** to count, **Zapdos** on the left and
**Moltres** on the right — and run them through **the live system, hourly.**

When a provider quietly swaps the model, when a resize step changes, when somebody ships a config
with the wrong resolution — **you find out in an hour instead of next quarter.**

Put in the set:

* 🔤 one that needs the **Poké Mart** price board read;
* 🔢 one that needs the **Zubat** in **Mt. Moon** counted;
* 🧭 one that needs **Blissey** told from **Chansey**, and left told from right;
* 📜 **one with no picture at all**, to catch question 148's quiet regression;
* 🚨 and one that **should** be refused, to check the refusals still work.

## Alarm on the right thing 🔔

⚠️ **Alarm on rates and distributions, never on single answers.** One bad entry is weather. **A
five-point shift in the refusal rate is an incident.** Set the thresholds from what you have
actually observed varying, not from a guess.

📌 And decide **before** it fires what you will do: roll back to a pinned version, fall back to a
cheap deterministic path, or degrade gracefully to *"I cannot answer this"*.

⚠️ A monitoring setup with no agreed response is **an expensive way to feel informed** — a **Poké
Flute** you never actually play while the **Snorlax** sits in the road.
