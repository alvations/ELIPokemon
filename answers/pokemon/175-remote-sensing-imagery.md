---
id: "175"
slug: remote-sensing-imagery
style: pokemon
category: multimodal
difficulty: advanced
question: "What makes satellite and aerial imagery different from ordinary computer vision?"
tags: [remote-sensing, multispectral, geospatial, tiling, change-detection, dual-use]
---

# Reading the region from the back of a Charizard

Use **Fly** and the whole of Kanto is beneath you. It looks like looking at anything else, and it
breaks nearly every assumption from questions 117 to 128 — each one concretely, each one differently.

## Six things that are not like a photograph 🗺️

* **🌈 There is more here than your eye picks up.** A **Dowsing Machine** finds items that are
  invisible from above; the same is true of the view itself. Most of what tells you whether that
  grass is healthy, whether that ground is wet, what that roof is made of, lies **outside** what a
  Trainer can see. ⚠️ And here is the trap: use an eye built for ordinary photographs and it
  **quietly discards those channels**. Nothing errors. It still works. It just works **worse**,
  forever, and nobody finds out.
* **🧭 Nothing has a right way up.** A route runs north on one map and east on the next. Everything
  must be trained to be turned about.
* **📏 But you *know how big things are*.** The **Town Map** has a scale. You can say a step is a
  step, and therefore an object's size **in metres**. 📌 This is the exact **opposite** of question
  152's problem — the ruler is handed to you — and most pipelines throw it away by resizing the
  picture.
* **🔍 The view is vast and the thing is tiny.** A whole route, and one Trainer standing on it.
  Panels and overlap, as in question 121, and then reconciling whatever sat on a seam.
* **⚖️ Almost all of it is nothing.** The interesting thing occupies a sliver of the area, so
  counting how often you are right is meaningless (question 151).
* **📅 And it is not one look — it is the same place, over and over.** ⚠️ Which means **what you
  actually want is the *change*.**

## Change is the job, and almost all change is boring 🍂

```
   the route in spring  ──┐
                          ├─► line them up EXACTLY ─► compare ─► what changed
   the route in autumn  ──┘          ▲
                    ⚠️ out by ONE STEP and every edge in the region reports
                       a change. Lining them up dominates the whole error
                       budget — and it is a preparation problem, not a
                       clever-model problem.
```

📌 And then the deeper difficulty. **Deerling** is pink in spring and orange in autumn. The route
looks different because **the season turned**, not because anything happened.

Separating *change that means something* from *change that always happens* is the entire task, and
it needs either a baseline for each season or two looks taken at the same time of year.

## There is unlimited material and almost no labels 🏷️

Nobody has to pay for the view — the region can be flown over endlessly. What costs money is
somebody **walking the route to confirm what is actually there.**

So: learn the shape of the region from the enormous unlabelled pile first, then teach it from a
small verified set. This works better here than almost anywhere. ⚠️ With one caution: **a Pokédex
trained over Kanto does not transfer to Paldea.** Different terrain, different vegetation, different
everything.

## And this one requires a decision 🚨

A map of exactly where every rare Pokémon appears is **the same map** whether a researcher or
**Team Rocket** is holding it.

That is not an edge case — it is what this capability *is*. A survey that finds a **swarm** for a
conservation team finds it equally well for somebody who wants to clear the route out. And the
resolution now available means you are no longer looking at regions. You are looking at
**individuals**.

⚠️ **No technical control resolves this.** What exists is:

* 🎯 **Say who it is for**, out loud, and refuse the uses that target people for harm.
* 📜 **Honour the terms the imagery came with**, which often restrict exactly this.
* 🔢 **Report at a level that cannot pick out one household** — a route, not a doorway.
* 📢 **And be honest that publishing a capability publishes it to everybody**, including whoever you
  were hoping would not read it.
