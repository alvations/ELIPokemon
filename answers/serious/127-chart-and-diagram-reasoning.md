---
id: "127"
slug: chart-and-diagram-reasoning
style: serious
category: multimodal
difficulty: intermediate
question: "Why do models struggle to read charts and diagrams?"
tags: [chartqa, plots, visual-reasoning, program-of-thought, synthetic-data, grounding]
---

# Charts and diagrams

A chart is not a picture of a thing. It is an **encoding**: numbers mapped onto position, length,
angle, area and colour, with a legend and axes as the decoding key. Reading one requires
recovering the numbers and then reasoning over them — two different failures waiting to happen.

## Why it is harder than object recognition

```
   OBJECT RECOGNITION            CHART READING
   ──────────────────            ─────────────
   "is there a bird?"            "what was Q3 revenue?"
                                    │
   one look, one label              ├─ find the Q3 bar               (localisation)
                                    ├─ measure its height in pixels  (precise geometry)
                                    ├─ read the y-axis ticks         (small text, OCR)
                                    ├─ interpolate between ticks     (continuous estimate)
                                    ├─ apply the axis units/scale    (log? thousands? %)
                                    └─ then answer                   (arithmetic)

   any single step wrong ⇒ confidently wrong number, no signal that anything failed
```

The specific weaknesses, roughly in order of how often they bite:

* **Continuous estimation.** Models are poor at reading a value that falls between gridlines. They
  snap to tick values, or hallucinate a round number.
* **Small text.** Axis labels, legends and data labels are exactly the fine print that
  downsampling destroys (question 121). Chart QA is a resolution problem wearing a reasoning
  costume.
* **Legend binding.** Matching a colour in the legend to a series in the plot is a
  colour-and-position association that fails with similar hues or many series.
* **Non-obvious axes.** Log scales, truncated axes not starting at zero, dual y-axes, reversed
  axes. Models read them as linear and full-range far too often.
* **Arithmetic on read values.** "How much more than" compounds a reading error with a
  calculation error.
* **Chart types with poor perceptual encodings.** Pie charts (angle), bubble charts (area),
  stacked bars (only the bottom series shares a baseline) are hard for humans too — the model's
  difficulty here is partly the chart's fault.

## What actually helps

**Program-of-thought decoding.** Instead of answering directly, have the model emit the extracted
data table and then a short program or explicit calculation over it:

```
   image ─► "extract the series as a table"  ─►  | quarter | revenue |
                                                 | Q1      | 4.2     |
                                                 | Q3      | 6.8     |
        ─► "compute the answer from the table" ─► 6.8 - 4.2 = 2.6
```

This separates *perception* from *arithmetic*, which is the single most effective change. It also
makes the failure visible: you can look at the extracted table and see that Q3 was misread,
instead of receiving a wrong number with no working.

**Synthetic training data.** Charts are one of the few domains where you can generate perfect
supervision at scale: render plots from known data with a plotting library, and you have exact
ground truth for values, axes, legends and derived questions. Vary chart type, style, fonts,
colour palettes, rotation and clutter, or the model overfits to one library's default aesthetic.
This is how modern chart ability was largely obtained.

**Resolution and OCR.** Feed the chart at high enough resolution to read the axis labels
(question 121). Much apparent reasoning failure disappears.

## Diagrams are a different problem

Flowcharts, circuits, architecture diagrams and molecular structures encode **topology**, not
magnitude: what connects to what, in which direction. The failure modes are edge-following (which
arrow leads where, especially crossing lines), node identity when labels are far from their
shapes, and containment (is this box inside that one?). Chart training data does not help here;
structured diagram data and explicit graph-extraction targets do.

## Evaluation

ChartQA and similar suites use **relaxed accuracy** — a numeric answer within 5% of ground truth
counts as correct — because exact match on a value read off a plot is unreasonable. Report the
tolerance you used; results are not comparable without it. And separate **extraction accuracy**
from **reasoning accuracy**, or you cannot tell which half to fix.

## What an interviewer digs into next

* Why does program-of-thought help so much here specifically?
* How would you generate synthetic chart data without overfitting to one style?
* Why is relaxed accuracy used, and what does it hide?
* Why don't chart skills transfer to circuit diagrams?
