---
title: Performance & Data-Oriented Design (UPS Optimization)
tags: [feature, performance, ups, data-oriented, soa, cache, belt, optimization]
source: https://www.factorio.com/blog/post/fff-176 (accessed 2026-11-18)
updated: 2026-11-18
---

# Performance & Data-Oriented Design (UPS Optimization)

## Goal & scope

Factorio's discipline for running huge simulations at a fixed **60 UPS** — data-oriented layout,
cache-friendly updates, and the canonical "change the representation, not the algorithm" wins.

## Primary sources

- **FFF #176** (belt optimization) — https://www.factorio.com/blog/post/fff-176 (accessed 2026-11-18)
- **FFF #215** (cache/prefetch/multithreading) (RESEARCH) — https://www.factorio.com/blog/post/fff-215 (accessed 2026-11-18)
- **FFF #415** (deterministic multithreading) (RESEARCH) — https://www.factorio.com/blog/post/fff-415 (accessed 2026-11-18)

## Key decisions / trade-offs

- **Fixed 60 UPS simulation**, decoupled from render FPS — a hard performance target that drives design.
- **Data-oriented design over OOP**: struct-of-arrays, cache locality, compact per-entity data.

## Implementation notes (sourced unless labeled)

- **The belt optimization (the canonical lesson)**: merge adjacent belts into one **transport line**
  ("treating sequences of adjacent belts as one single piece"), store **relative item gaps** instead of
  absolute coordinates ("We no longer store absolute coordinates of items, instead we store the distance
  between items"), and update only the line *ends* ("incrementing/decrementing two integers instead of
  incrementing the position of all 200 items"). Result: "x50-100 on items movement… actual gains around
  x5-x10." **The insight: a better data representation beats a faster algorithm.** (FFF #176)
- **Struct-of-arrays** and compact entity structs for cache locality; chunks (32x32) allocated with
  **Morton encoding** so spatial proximity = memory proximity. (FFF #215, RESEARCH)
- **Software prefetching** into entity update loops gained ~9-13%; optimal range ~-128..+384 bytes.
  (FFF #215, RESEARCH)
- **Parallel update was *slower*** — threads invalidating each other's cache pages (false sharing).
  Determinism also forbids naive parallelism. (FFF #215, RESEARCH)
- **Fluid rewrite (2.0)**: pipes → "fluid segments", ~10-100x. (FFF #415, RESEARCH)

## Anti-patterns / gotchas

- Per-item objects/entities for high-count systems (belts, items) — merge into lines/segments.
- Storing absolute coordinates when relative gaps suffice.
- Assuming multithreading will help a cache-bound, deterministic update loop (it often hurts).

## Verify-first

Re-verify UPS/SoA patterns against FFF posts and profile your own hot paths; the belt trick generalizes
to any "many items on a shared path" system.
