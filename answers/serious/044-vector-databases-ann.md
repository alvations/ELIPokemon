---
id: "044"
slug: vector-databases-ann
style: serious
category: rag
difficulty: intermediate
question: "How do vector databases work? Explain HNSW and IVF."
tags: [ann, hnsw, ivf, pq, vector-database, recall]
---

# Vector databases and ANN search

Exact nearest-neighbour search over `N` vectors is `O(N·d)` per query — at 100M vectors and 768
dimensions that is tens of GB of arithmetic per query. Vector databases give up exactness for speed:
**approximate** nearest neighbour search returns *most* of the true top-k, orders of magnitude
faster. The governing tradeoff is **recall vs latency vs memory**, and every index is a point on
that surface.

## HNSW

Hierarchical Navigable Small World ([Malkov & Yashunin, 2016](https://arxiv.org/abs/1603.09320))
builds a multi-layer proximity graph. Upper layers are sparse and give long-range jumps; lower
layers are dense and give local refinement. Search is greedy descent.

```
   Layer 2   ●───────────────────●──────────────●        sparse: big hops
              ╲                 ╱                        (entry point)
   Layer 1   ●──●──────●───────●────●─────●──●          medium
              ╲  ╲    ╱       ╱    ╱                     
   Layer 0   ●─●─●─●─●─●─●─●─●─●─●─●─●─●─●─●─●          every vector, dense

   query: start at the top entry point, greedily move to the neighbour
   closest to the query, drop a layer when no neighbour improves, repeat.
   O(log N) hops.
```

Parameters: `M` (neighbours per node — memory and recall), `ef_construction` (build-time search
width — build time and index quality), `ef_search` (query-time candidate list — the runtime
recall/latency dial; this is the one you tune in production).

Strengths: the best recall-per-latency of any mainstream index, and it supports incremental
insertion. Weaknesses: high memory (the graph itself is often larger than the vectors), slow builds,
and deletions require tombstoning plus periodic rebuilds.

## IVF

Inverted File Index: `k`-means the vectors into `nlist` cells, store each vector in its cell's
posting list, and at query time search only the `nprobe` nearest cells.

```
   ┌─────────┬─────────┬─────────┐    query lands here ──┐
   │ cell 1  │ cell 2  │ cell 3  │                       ▼
   │  ● ● ●  │  ● ● ●  │  ● ● ●  │              ┌─────────────┐
   ├─────────┼─────────┼─────────┤              │   cell 5    │
   │ cell 4  │ cell 5  │ cell 6  │              │ search this │  nprobe = 1
   │  ● ● ●  │  ●●✕●●  │  ● ● ●  │              └─────────────┘
   ├─────────┼─────────┼─────────┤
   │ cell 7  │ cell 8  │ cell 9  │              nprobe = 3 would also
   │  ● ● ●  │  ● ● ●  │  ● ● ●  │              search cells 2 and 8
   └─────────┴─────────┴─────────┘
```

`nprobe` is the recall/latency dial. The classic failure is the **boundary problem**: a true
neighbour just across a cell border is missed unless `nprobe` is raised. Cheaper to build and far
lighter on memory than HNSW, so it scales to billions.

## Compression: product quantization

PQ splits each vector into `m` sub-vectors and replaces each with the index of the nearest centroid
in a small learned codebook. A 768-d float32 vector (3 KB) becomes 96 bytes — a 32× reduction — and
distances are computed by table lookup. Lossy, so production systems use **IVF-PQ for the coarse
pass and rerank the top candidates with full-precision vectors**. That two-stage pattern is how
billion-scale search is actually done.

## Choosing

| Scale | Index |
| --- | --- |
| < 10k vectors | brute force. Genuinely. NumPy is fast enough and exact. |
| 10k – 10M | HNSW |
| 10M – 1B | IVF-PQ, or HNSW with quantization |
| > 1B | IVF-PQ with sharding, disk-based (DiskANN) |

## The operational issues people forget

* **Metadata filtering.** "Documents from this tenant, after this date" interacts badly with ANN:
  pre-filtering breaks the graph's connectivity, post-filtering can return nothing. Native filtered
  search is a genuine differentiator between vector databases.
* **Updates and deletes.** HNSW deletion is tombstoning; index quality degrades until a rebuild.
* **Recall is not observable in production.** You cannot see what you failed to retrieve. Measure it
  offline against exact search on a sample — otherwise you will not notice degradation.

## What an interviewer digs into next

* Why does HNSW's layered structure give logarithmic search?
* What is IVF's boundary problem and how do you mitigate it?
* Why rerank PQ results with full-precision vectors?
* How would you implement per-tenant filtering without destroying recall?
