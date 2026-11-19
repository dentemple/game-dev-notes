---
title: Procedural World Generation (UE PCG)
tags: [feature, world-gen, pcg, procedural, biome, landscape, voronoi]
source: https://dev.epicgames.com/documentation/unreal-engine/procedural-content-generation--framework-in-unreal-engine (accessed 2026-11-18; PCG specifics RESEARCH)
updated: 2026-11-18
---

# Procedural World Generation (UE PCG)

## Goal & scope

Generate **bounded** worlds/landscapes/biomes in UE. See ../procedural-generation.md (Voronoi/WFC/CA) and
../features/roguelike-core.md (bounded dungeon maps).

## Primary sources

- Epic "Procedural Content Generation Framework" (RESEARCH — search summary):
  https://dev.epicgames.com/documentation/unreal-engine/procedural-content-generation--framework-in-unreal-engine (accessed 2026-11-18)
- Cross-refs: ../procedural-generation.md, roguelike-core.md

## Key decisions / trade-offs

- **PCG framework** (UE 5.3+) for landscape/foliage/biome scattering; **Voronoi** for region/biome layout
  (../procedural-generation.md).
- **Bounded** maps: fixed cells + a connectivity pass, not infinite (see ../procedural-generation.md).

## Implementation notes (RESEARCH)

- PCG graph shape: Surface Sampler → Transform Points → Static Mesh Spawner (+ Difference for exclusions).
- Biomes via layered PCG graphs / heightmap + slope sampling.
- Runtime PCG is possible but costlier; prefer bake-for-shipping.

## Anti-patterns / gotchas

- Infinite/no-connectivity maps when you need bounded Civ-style.
- Uniform-random Voronoi points (use Poisson/Lloyd relaxation).

## Verify-first

Re-verify PCG node APIs against dev.epicgames.com; Voronoi/WFC via ../procedural-generation.md.

## Related

../procedural-generation.md · ../features/roguelike-core.md · ../ue-performance.md
