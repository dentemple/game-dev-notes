---
title: Roguelike Core (Dungeon, Turn Loop, FOV, Combat, Items)
tags: [feature, roguelike, dungeon-generation, fov, turn-based, permadeath, combat, inventory, procedural, berlin-interpretation, bsp, cellular-automata, dijkstra-maps, shadowcasting]
source: https://www.roguebasin.com/index.php?title=Berlin_Interpretation (accessed 2026-11-18)
updated: 2026-11-18
---

# Roguelike Core (Dungeon, Turn Loop, FOV, Combat, Items)

## Goal & scope

The engine-agnostic core of a traditional roguelike — grid dungeon, turn loop, procedural generation,
field of view, bump combat, items, permadeath, save/load — distilled from canonical tutorials **and**
authoritative sources (RogueBasin, Kyzrati/Cogmind), mapped to Unreal. Does **not** cover meta-progression,
narrative, or asset work.

## Primary sources

- **Berlin Interpretation** — https://www.roguebasin.com/index.php?title=Berlin_Interpretation (accessed 2026-11-18)
- **RogueBasin BSP** — https://www.roguebasin.com/index.php?title=Basic_BSP_Dungeon_generation (accessed 2026-11-18)
- **RogueBasin Cellular Automata** — https://www.roguebasin.com/index.php?title=Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels (accessed 2026-11-18)
- **RogueBasin FOV comparison** — https://www.roguebasin.com/index.php?title=Comparative_study_of_field_of_view_algorithms_for_2D_grid_based_worlds (accessed 2026-11-18)
- **RogueBasin Dijkstra Maps** — https://www.roguebasin.com/index.php?title=The_Incredible_Power_of_Dijkstra_Maps (accessed 2026-11-18)
- **Kyzrati** — "How to Make a Roguelike": https://www.gridsagegames.com/blog/2018/10/how-to-make-a-roguelike/ (accessed 2026-11-18)
- **libtcod tutorial** (parts 2-5): https://libtcod.github.io/tutorials/python/2021/ (accessed 2026-11-18)
- **tutsplus roguelike**: https://code.tutsplus.com/how-to-make-your-first-roguelike--gamedev-13677t (accessed 2026-11-18)
- **rogueliketutorials 2019** (parts 8, 10): https://rogueliketutorials.com/tutorials/tcod/2019/ (accessed 2026-11-18)

## Genre definition — Berlin Interpretation

Nine **high-value** factors: random environment generation, permadeath, turn-based, grid-based,
non-modal, complexity, resource management, hack'n'slash, exploration/discovery. Six **low-value**
factors: single player character, monsters similar to players, tactical challenge, ASCII display,
dungeons, numbers. It is descriptive, not prescriptive: "Missing some points does not mean the game
is not a roguelike… It is not to place constraints on developers or games." Use it as a design
checklist, not a gate. (Berlin Interpretation)

## Key decisions / trade-offs

- **Core mechanic first (Kyzrati)**: "So what does a small roguelike really need? A core mechanic."
  "Go straight for the fun." — "only implement as many of the outer elements as necessary to bring
  out and test the core mechanic." Build a proto-game around one explainable mechanic. (Kyzrati)
- **Grid, not a physics world** — store the map as a tile array; do not spawn one Actor per tile.
- **One generic entity, not deep inheritance** — composition/optional fields is the norm.
- **Turn-based, not Tick-driven** — a turn/schedule manager.
- **Simple AI first** — random-walk → greedy → A* → Dijkstra/goal maps.

## Implementation notes (sourced unless labeled)

- **Dungeon generation** — pick per level/biome, don't assume one fits all:
  - *Rooms + corridors*: random rectangles, reject intersections, carve; L-shaped tunnels between
    centers; chain each room to the previous (one connected dungeon). (libtcod part-3)
  - *BSP*: recursively split until each leaf ≈ room size; one room per leaf; connect each leaf to its
    sister with a straight or Z-shaped corridor, then ascend the tree. (RogueBasin BSP)
  - *Cellular automata (caves)*: start ~40% wall; a tile becomes wall if ≥5 of its 8 neighbors are
    walls; ~4 smoothing passes (tweaked rule) then 3 plain. (RogueBasin Cellular Automata)
  - *Mazes* — a fourth family (from the IRDC "Dungeons I Have Known" taxonomy).
- **Field of view / fog of war** — keep `visible` (current) and `explored` (ever-seen, persists across
  save/load) separate. Default to symmetric shadowcasting. Trade-off (RogueBasin FOV comparison):
  BASIC/SHADOW don't allow corner peeking; permissive FOV (0–8) trades symmetry for permissiveness; "no
  permissiveness level gives perfect results." (libtcod part-4; RogueBasin FOV comparison)
- **Bump-to-attack** — one verb doubles as move+attack; Bump routes to Melee (blocked) or Move (empty).
  (libtcod part-5; tutsplus)
- **Items & inventory** — item = data + `use_function`; inventory = bounded list; heal clamps to max.
  (rogueliketutorials part-8)
- **Spatial lookup** — position-keyed map avoids scanning all entities each turn. (tutsplus)
- **Save/load** — serialize entities, map, message log, game state; save the player's index, not the
  object; use `USaveGame` + schema versioning (see ../game-architecture.md). (rogueliketutorials part-10)
- **Enemy AI escalation** — random walk (beyond range) → greedy axis approach (tutsplus) → A* pathfinding
  → **Dijkstra maps** (flood-fill step distances; agents "roll downhill"; flee by multiplying by ~-1.2;
  combine weighted maps for goal-driven AI). (RogueBasin Dijkstra Maps)

## Anti-patterns / gotchas

- One Actor per tile, or full physics/rendering per grid cell.
- Driving a turn-based loop from `Tick`.
- Deep entity class hierarchies (the canonical tutorial itself moved from components to a single class).
- Forgetting fog-of-war persistence (`explored` must survive save/load).
- Over-engineering enemy AI or procgen before the core mechanic is fun (Kyzrati's "go straight for the fun").
- Treating the Berlin Interpretation as a compliance test rather than a checklist.

## Verify-first

Re-verify UE-specific equivalents against dev.epicgames.com before coding: `USaveGame`/serialization,
Navigation/A* (or a custom grid A*), and any FOV/shadowcasting you implement in C++.
