---
id: "m061"
slug: how-a-cancer-spreads
style: pokemon
category: oncology
difficulty: intermediate
question: "How does a cancer spread, and why is the pattern of spread organ-specific rather than random?"
tags: [metastasis, routes-of-spread, organotropism, lymphatics, cascade]
---

# Kanto is a graph, not a map — and arriving somewhere is not the same as living there

**Diglett's Cave** has exactly two warps in it. Read the object file in the Red decompilation and
that is the whole of the map: one exit to the Route 2 entrance building, one exit to the Route 11
entrance building. Nothing else. So **Viridian City** and **Vermilion City**, which sit at
opposite corners of Kanto and are nowhere near each other, are two hops apart — and the reason is
not distance. It is that somebody dug a tunnel.

That is the first half of how a cancer spreads, and it is the half people get right. The second
half is the one the games state even better. Take an **Eevee** and level it up, and what you get
depends on **where you were standing**. In the Emerald expansion's data the entry is explicit: one
evolution is gated on being in **Petalburg Woods**, another on being in the ice room of **Shoal
Cave**. Same Eevee, same level-up, two different outcomes, and the only thing that differs is the
map.

Routes decide what arrives. The map it arrives on decides what happens next. Both are needed and
neither is enough.

As elsewhere in this specialty: **the objects of study are maps, warps, drainage and evolution
conditions.** No Pokémon in this answer stands in for a person with cancer, and the analogy is
dropped entirely at the end, where the subject changes.

Clinical claims carry the same marks as the rigorous half: **mechanism**, **definitional**,
**consensus**, **country-dependent**.

## The channels, drawn as what they are

```
   THE WORLD IS A SET OF EDGES, NOT A DISTANCE FUNCTION

      Route 2  ──┐                                    ┌── Route 11
                 │        Diglett's Cave               │
      Viridian ──┴────────── 2 warps ──────────────────┴── Vermilion
                                                          
      far apart on the map.  ONE EDGE apart in the graph.
      You cannot read the second fact off the first.

   ─────────────────────────────────────────────────────────────────────────────────

   AND A CLINICAL SITE'S EDGES ARE ITS DRAINAGE:

      gut, and the other portal-drained viscera  ──►  portal vein  ──►  LIVER
                                                                        first bed

      almost everywhere else  ──►  systemic veins  ──►  right heart  ──►  LUNG
                                                                        first bed

      past the first bed the outflow is ARTERIAL  ──►  anywhere at all

      each site's lymphatics  ──►  ITS OWN node field, in order
                                   — which is the whole basis of
                                     sentinel node mapping

   ─────────────────────────────────────────────────────────────────────────────────

   AND SOME CHANNELS NEED NO VESSEL.  Compare the target fields in
   Emerald's own move data:

      MOVE_TARGET_SELECTED      one declared target.  Surgery and
                                radiotherapy are this shape.
      MOVE_TARGET_BOTH          Surf, 95 power — both opponents, because
                                the water is shared.  Transcoelomic spread
                                across a serous cavity is this shape: no
                                channel, just a cavity everything in it
                                is exposed to.
      MOVE_TARGET_FOES_AND_ALLY Earthquake, 100 power — and it hits your
                                OWN side too, because being grounded is
                                the only test it makes.
```

## Reading the edges, not the distances

The mechanical half of the clinical argument is the Diglett's Cave argument and nothing more
(**mechanism**). A cell leaving a tumour travels in whatever vessel leaves that site, and stops at
the first filter that vessel reaches. Portal-drained viscera reach the liver first. Everything
else reaches the lung first. Past that bed the outflow is arterial and the destination list opens
up — which is exactly why the liver and the lung are so often involved first and why involvement
beyond them tends to follow rather than lead.

Two features of the games' geography make the same point sharper than a diagram of veins does.

* **An edge can make two distant places adjacent, and nothing on the surface shows it.** Diglett's
  Cave is the clean case: two warps, one tunnel, and a pair of cities that look unrelated on the
  **Town Map** become neighbours. The standard mechanical account of spread to the axial skeleton
  turns on exactly this — the valveless venous plexuses around the vertebral column are an edge
  that bypasses the usual sequence (**consensus** on the anatomy, **mechanism** for what follows).
* **Fly's destination list is enumerated, not open.** You can Fly to the towns on the list and
  nowhere else, and the list is a property of the world rather than of the Pokémon doing the
  flying. A site's regional node field is the same kind of object: a defined, ordered set of
  destinations belonging to that site's anatomy (**definitional**), which is why it can be mapped,
  sampled or treated as a field at all.

## Where the edges stop explaining it, and Eevee says why

Now the part a flow argument cannot reach, and the games have a better device for it than medicine
does.

In the expansion's species data, **Eevee** carries two evolutions whose condition is a place. One
is `IF_IN_MAP` set to **Petalburg Woods**, giving **Leafeon**. The other is `IF_IN_MAP` set to the
low-tide ice room of **Shoal Cave**, giving **Glaceon**. **Magneton** carries the same shape with
`IF_IN_MAPSEC` set to **New Mauville**, giving **Magnezone** — the expansion's Hoenn stand-in for
the fourth generation's special magnetic field. The condition type has its own name in the data's
enumeration. *Where you are* is a first-class input, recorded beside gender, friendship and held
item as one more thing the outcome can depend on.

That is the **seed-and-soil** argument (**mechanism**). A cell that arrives somewhere has to
adhere, leave the vessel, survive in a foreign tissue and then start dividing, and whether it can
is a property of the tissue it landed in — adhesion molecules, chemokine receptor and ligand
pairing, the local stromal and immune context, the behaviour of the resident cells. The specifics
are an active research programme rather than a settled list, which is why no particular molecule
is asserted here.

And the clinical evidence that the second argument is needed is a mismatch, not a theory
(**consensus**):

* **Skeletal muscle takes a large share of cardiac output and is an uncommon site. The spleen is
  likewise uncommon.** Pure flow predicts otherwise.
* **Several cancers deposit overwhelmingly in an organ that is not first downstream of them.** The
  preference of uveal melanoma for the liver is the usual teaching example; the preference of
  breast and prostate cancer for bone is the commonest.

Same Eevee, different map, different outcome. Nothing about the Eevee changed.

## Why it is rare per cell: the shake check, and all of them have to pass

The best fact in this answer is in the catch routine, and it is exact.

Read `Cmd_handleballthrow` in Emerald. If the computed odds exceed 254 the capture succeeds
outright. Otherwise the code rescales the odds and then runs a loop: up to **three** independent
checks, each a fresh `Random()` against that value, and the capture only lands if **every one of
them passes**. Fail the second and the **Poké Ball** opens with two shakes. The individual check
can be quite likely and the product of three of them is a good deal less likely, and that gap is
the entire reason a **Great Ball** is not a **Master Ball**.

The metastatic cascade is that loop with more iterations (**mechanism**). Breach the basement
membrane and the local stroma. Enter a vessel. Survive the circulation — shear, loss of adhesion,
immune surveillance. Arrest somewhere. Leave the vessel. Survive in a tissue that is not the one
you came from. Then start dividing again. Each step discards most of what reached it, so the joint
probability is a product of small numbers and is minute.

Two consequences come free, and both are commonly got wrong:

* **Cells in the circulation are far commoner than metastases**, because they have only passed the
  early checks. Detecting them is therefore not the same as detecting metastatic disease, and that
  is the central difficulty in reading any circulating-cell or circulating-DNA assay
  (**consensus**).
* **Dormancy and late recurrence are predictions of the model, not exceptions to it.** The last
  check — resuming proliferation in a new tissue — can be delayed, in some diseases by many years.
  That is why follow-up in those diseases is long, and why an interval without disease is not
  evidence that the loop was never completed.

## What the pattern is actually used for

* **Staging investigation is directed rather than exhaustive**, chosen from the known pattern for
  that primary site rather than by looking everywhere (**consensus**, **country-dependent** in
  protocol).
* **The node field is treated as the anatomical object it is** — sampled, mapped or irradiated as
  a field, by site-specific rules.
* **A cancer of unknown primary is worked up from its pattern of spread**, because the pattern
  carries information about where it started (**consensus**).
* **A limited-volume metastatic pattern is managed differently from a widespread one in several
  diseases**, and whether that is offered where you are is strongly **country-dependent**.

And one honest limit, which the games supply themselves. **Diglett's Cave does not explain why
anyone dug it.** The two warps are in the file because they are in the file; no principle about
Kanto's geography generates them. A graph tells you what is reachable and says nothing about why
the edges are where they are, and a drainage argument is in exactly that position: it predicts the
destinations well and explains none of the biology that decides which arrivals survive.

## Where the metaphor stops

Everything above is anatomy, graphs and probability, and a world with a readable map file is a
good place to look at those. What follows is about people, so it is said plainly and without the
analogy.

A report describing spread beyond the primary site is, for the person it is about, among the
hardest things they will ever be told, and it changes the shape of everything that comes after.
Nothing in a mechanistic account speaks to that, and nothing in a game comes anywhere near it.
Being able to say which organ a particular cancer tends to reach is a different skill from being
any use to someone who has just learned that it reached theirs, and the second is harder and
matters more.

A pattern of spread also does not settle what happens to any individual. The distribution of sites
is a population regularity; one person's course depends on their disease, their treatment, what is
available where they live, everything else going on in their body, and what they choose. No figure
of any kind appears in either half of this answer, and that is deliberate rather than an omission.

## What a Gym Leader is listening for

* Diglett's Cave has two warps. Say what that has to do with the liver and colorectal cancer, in
  one sentence, without using the word *near*.
* Why is the lung the first bed for a limb sarcoma and the liver for a colonic primary?
* Skeletal muscle has a large blood supply and few metastases. What does that do to a purely
  mechanical explanation, and what has to be added?
* Eevee's two place-gated evolutions are the seed-and-soil argument. What exactly is being carried
  across, and what is not?
* The catch loop runs three checks and needs all three. Why does that make metastasis rare per
  cell and common per cancer at the same time?
* Why are circulating tumour cells much commoner than metastases, and what does that do to an
  assay that finds them?

## Sources

**None of the sources below was retrieved.** They were unreachable from the environment this was
written in, so every claim here rests on general professional knowledge and is attributed, not
quoted. Open the document before relying on anything in this answer.

The standing documents for this specialty are listed in
[`../../../for-agents/SOURCES-oncology.md`](../../../for-agents/SOURCES-oncology.md). Specific to
this answer:

* A current standard textbook of pathology or of surgical anatomy, for the venous and lymphatic
  drainage of each site and for the nodal fields that follow from it.
* A current standard textbook of cancer biology, for the metastatic cascade and the seed-and-soil
  account, including the adhesion and chemokine mechanisms named here.
* The tumour–node–metastasis classification published by the Union for International Cancer
  Control, and the parallel staging manual of the American Joint Committee on Cancer, for how each
  site's regional node field is defined and what counts as distant.
* Your national or regional cancer network's staging investigation protocols, for what is imaged
  for which primary site where you work.
* The primary literature, for circulating tumour cells, circulating tumour DNA and the management
  of limited-volume metastatic disease, all of which are moving.

The Pokémon side is in the opposite position and is sourced file by file in the closing note.

## Scope and safety

This is revision material about routes and patterns of spread, dressed in a game so that the
difference between a channel and a destination stays concrete. It has had no clinical review. It
is not a staging protocol, it is not a diagnostic aid, and it describes no individual's situation.
No threshold, interval, proportion or survival figure appears here and none should be inferred.
Which investigations are done for which primary site differs by country, region and institution
and is revised; the protocol in force where you work is the authority, and this is not. Anyone
affected by cancer — their own diagnosis or someone else's — should be talking to the clinical
team looking after that person, who have the imaging, the pathology and the history, none of which
are here. The analogy carries two ideas and no others: that reachability is decided by edges
rather than by distance, and that arriving is not the same as surviving. No part of it stands in
for a person, and none of it says anything about what happens to anybody.

## Where this stands, October 2026

The Pokémon facts are read from the projects' own files. Diglett's Cave's two warps — one to the
Route 2 entrance, one to the Route 11 entrance — are the entire warp list in its map object file
in the Red decompilation. Surf's target field in Emerald's move data is `MOVE_TARGET_BOTH` at 95
base power, and Earthquake's is `MOVE_TARGET_FOES_AND_ALLY` at 100; Surf's targeting widened in a
later generation, so the value quoted is Emerald's. Eevee's place-gated evolutions, with the
conditions `IF_IN_MAP` for Petalburg Woods and for Shoal Cave's low-tide ice room, and Magneton's
`IF_IN_MAPSEC` for New Mauville, are read from the Emerald expansion's species data, where those
condition types are enumerated by name; the expansion is a fan project reimplementing fourth- and
later-generation mechanics on the Emerald map, and the fourth generation's own locations are
different places with the same logic. The three-shake loop, the early success above odds of 254
and the rescaling between them are in `Cmd_handleballthrow` in Emerald's battle script commands.
Fly's destination list is described from working knowledge of the games rather than from code
opened here.

The clinical structure — a short list of routes, destinations predicted by drainage, a target
tissue that decides what survives, and a lossy multi-step cascade — is long-standing and will not
move. The anatomy will not move at all. What moves is the molecular detail of organotropism, which
is unsettled and is deliberately not pinned to a named molecule here, and the clinical periphery:
what circulating tumour DNA is used for, how limited-volume metastatic disease is defined and
treated, and which staging investigations are protocolised for which site. Those last are
**country-dependent**, under revision, and belong to the current local protocol rather than to a
revision note like this one.
