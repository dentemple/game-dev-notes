---
title: Procedural Generation (Voronoi, WFC, Cellular Automata)
tags: [procedural, generation, voronoi, delaunay, wfc, cellular-automata, terrain, biome, mapgen, ecosystem]
source: https://www.redblobgames.com/maps/polygon-map-generation/ (accessed 2026-11-18)
updated: 2026-11-18
---

# Procedural Generation (Voronoi, WFC, Cellular Automata)

## Goal & scope

How to generate **bounded** maps and evolving ecosystems with concise algorithms — Voronoi/Delaunay for
regions/biomes, Wave Function Collapse for constrained tile fills, and cellular automata for systems that
evolve over time. Companion to features/roguelike-core.md (dungeon algorithms) and emergent-behavior.md
(CA as emergence).

## Primary sources

- **Red Blob Games — Polygonal Map Generation** — https://www.redblobgames.com/maps/polygon-map-generation/ (accessed 2026-11-18)
- **Gumin — Wave Function Collapse** — https://github.com/mxgmn/WaveFunctionCollapse (accessed 2026-11-18)
- **CA / ecosystem models** (RESEARCH) — forest-fire CA, reaction-diffusion automata (accessed 2026-11-18)

## Voronoi / Delaunay map pipeline

The canonical recipe (Red Blob):
1. **Sample points** — Poisson-disc sampling or **Lloyd relaxation**, *not* uniform random ("I didn't use
   uniformly random points, because they aren't evenly distributed").
2. **Delaunay triangulate** the points.
3. **Voronoi / centroid polygons** — "calculate the centroids of the triangles… construct polygonal
   regions."
4. **Assign attributes** — elevation = breadth-first search from the coastline (no noise); rivers =
   a subset of the **watershed/drainage map** (each corner points to its lowest neighbor); moisture =
   distance from water; biomes = **Whittaker diagram** (temperature × rainfall).

This is how you get **Civ-style bounded continents**: a fixed set of cells, partitioned into organic
regions, then colored into biomes. Point spacing matters — "poisson disk, lloyd relaxation, or precomputed
blue noise" is what makes cells look natural rather than "pointy."

## Wave Function Collapse

WFC is **constraint solving**: "bitmap & tilemap generation from a single example… locally similar to the
input." Each cell starts as a superposition of all tiles; the solver picks the **lowest-entropy** cell
(minimum remaining values), collapses it, and propagates adjacency constraints (AC-4) — "WFC translates a
texture synthesis problem into a constraint satisfaction problem." It's "perfect for level generation in
games" but constrains only *nearby* tiles, so it **rarely produces large-scale structure** (rooms/corridors)
on its own (RESEARCH) — used in Caves of Qud, Bad North, Townscaper.

## Cellular automata as evolving systems (RESEARCH)

- **Forest-fire model**: three states (unburnt / burning / burnt), Moore neighborhood; fuel, wind, and
  topography shape spread — a minimal CA that produces realistic fire fronts.
- **Reaction-diffusion automata** (Greenberg–Hastings / Gray-Scott): two chemicals react and diffuse,
  producing spots/stripes/labyrinths — the standard tool for organic patterns.
- **Ecosystem evolution**: CA with fire + vegetation states show forest↔grassland **bistability** and
  perimeter "erosion," linking local rules to percolation/reaction-diffusion theory.
- These are the *time* axis — CA is how you let terrain/ecosystems **evolve**, not just be stamped once.

## Bounded roguelike maps (RESEARCH)

The standard bounded-map toolbox (combine, don't rely on one): **rooms+tunnels, BSP, maze, drunkard's walk,
DLA, cellular automata (caves), Voronoi hive, WFC**. For organic room layouts, **Delaunay triangulation +
Prim's minimum spanning tree** connects scattered rooms into a guaranteed-connected graph. The practical
rule (Wolverson's survey): **layer generators** — e.g. Voronoi for layout, CA/WFC for local detail.

## The concise playbook (ANALYSIS)

1. **Bounded layout** → Voronoi/Delaunay (regions, biomes) or BSP/rooms (dungeons).
2. **Guarantee connectivity** → a spanning tree (Prim) over the region/room graph.
3. **Local detail** → WFC (constrained tile patterns) or CA (caves/erosion).
4. **Time evolution** → a CA or reaction-diffusion pass that runs per-tick.

## Anti-patterns / gotchas

- Uniform random points for Voronoi (uneven, ugly cells) — relax/sample for blue noise.
- Relying on WFC alone for a connected roguelike map (it has no global structure).
- Unconnected generated maps — always run a connectivity pass (flood fill + spanning tree).
- Treating CA as fully predictable — it's emergent; tune by playtest, not by formula.

## Verify-first

Re-verify the Red Blob pipeline and WFC's AC-4/lowest-entropy details against the sources above; in UE,
Voronoi/Delaunay and WFC have no built-in node — implement in C++ or use a marketplace/plugin library.
