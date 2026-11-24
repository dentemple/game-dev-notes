# Feature research (on-demand)

Per-feature development research for the `unreal-engine-dev` agent. One file per
feature; the agent loads only the file for the feature it is actively working on
— never the whole directory.

## Why this exists

Cross-cutting knowledge (engine, design theory, architecture, process) lives in
the parent `knowledge/` topics. When `agent-researcher` researches *how to build
a specific feature* (inventory, save/load, dialogue, quests, combat, AI, …), that
research lands here as a single self-contained file so it can be pulled on
demand and unrelated features never enter context.

## How the agent reads it

1. Start at the cross-cutting index, `../README.md` — it points here. Read the
   feature index below when the task names a specific feature.
2. Use the routing table in the agent prompt
   (`../../.claude/agents/unreal-engine-dev.md`, "Routing") for the common
   clusters.
3. Grep the index by keyword, then Read **only** the matching `<feature>.md`.
4. Never load multiple feature files "just in case"; read one feature at a time.

## Convention (for agent-researcher)

- One feature per file: `features/<feature-slug>.md` (kebab-case, e.g. `save-system.md`).
- Frontmatter on every feature file:

  ```yaml
  ---
  title: <Feature Name>
  tags: [feature, <feature keywords>]
  source: <URL> (accessed <YYYY-MM-DD>)
  updated: <YYYY-MM-DD>
  ---
  ```

- Keep each file short (< 300 lines) and self-contained: cite sources with URL
  + access date; label sections `RESEARCH` or `ANALYSIS` where the content is
  secondary or inferred.
- Do **not** duplicate cross-cutting content inside a feature file — reference
  the parent topic instead (e.g. "see ../replication.md").
- After writing a feature file, add its row to the index below.
- `unreal-engine-dev` does not write here: it writes research briefs under
  `../research-requests/` and its own notes under `../agent-memory/`.

## Feature topic template

```markdown
---
title: <Feature Name>
tags: [feature, <keywords>]
source: <URL> (accessed <YYYY-MM-DD>)
updated: <YYYY-MM-DD>
---

# <Feature Name>

## Goal & scope
<one line: what the feature does, and what it does NOT include>

## Primary sources
<fetched primary URLs + access dates>

## Key decisions / trade-offs
<the load-bearing choices and why>

## Implementation notes (sourced unless labeled)
<concrete, actionable notes, each with a source label>

## Anti-patterns / gotchas
<what not to do>

## Verify-first
<what to re-check against primary docs before coding>
```

## Index

| Slug | Feature | Tags | Updated |
|------|---------|------|---------|
| roguelike-core | Roguelike Core (Dungeon, Turn Loop, FOV, Combat, Items) | feature, roguelike, dungeon-generation, fov, turn-based, permadeath, combat, inventory, procedural, berlin-interpretation, bsp, cellular-automata, dijkstra-maps, shadowcasting | 2026-11-18 |
| quest-dialogue | Quest & Dialogue System | feature, quest, dialogue, state-machine, branching, flags, narrative, datatable | 2026-11-18 |
| combat | Action RPG Combat Mechanics | feature, combat, melee, hitbox, iframe, stagger, poise, hitstop, combo, gas, telegraph | 2026-11-18 |
| combat-botw-genshin | Combat Reference — Breath of the Wild & Genshin Impact | feature, combat, botw, genshin, elemental-reactions, flurry-rush, parry, durability, stamina, slow-motion | 2026-11-18 |
| combat-windwaker | Combat Reference — Wind Waker (Parry & Telegraphing) | feature, combat, windwaker, parry, counter, telegraph, lock-on, disarm, sword | 2026-11-18 |
| combat-dnd5e | Combat Mechanics — D&D 5e & Baldur's Gate 3 Translation | feature, combat, dnd, 5e, advantage, disadvantage, action-economy, conditions, bounded-accuracy, bg3 | 2026-11-18 |
| combat-freeflow | Freeflow Combat (Arkham, Shadow of Mordor) | feature, combat, freeflow, arkham, shadow-of-mordor, nemesis, crowd-control, attack-token, hit-streak, might, traits | 2026-11-19 |
| combat-shadow-of-mordor | Shadow of Mordor Combat (Melee & Ranged) | feature, combat, shadow-of-mordor, shadow-of-war, melee, ranged, hit-streak, might, elf-shot, focus, execution, wraith | 2026-11-19 |
| combat-spellcasting | Spellcasting & Spell Combat (Mass Effect, Wrath, Genshin, Skyrim, WoW, GW) | feature, combat, spellcasting, abilities, primer, detonator, elemental, reactions, cooldown, mana, ultimate, crowd-control | 2026-11-19 |
| encounter-design | Encounter Design (5 Room Dungeon & Pacing) | feature, encounter, combat, design, 5-room-dungeon, pacing, terrain, action-economy, telegraph | 2026-11-18 |
| enemy-tactics | Enemy Tactics & AI Archetypes (Monsters Know What They're Doing) | feature, enemy, combat, ai, tactics, monster, archetype, self-preservation, retreat, morale | 2026-11-18 |
| class-skill-leveling | Class, Skill & Leveling Design (D&D 5e, Skyrim, WoW, Battlefield) | feature, class, skill, leveling, talent-tree, perk, progression, xp | 2026-11-18 |
| deterministic-simulation | Deterministic Simulation & Lockstep Multiplayer | feature, determinism, lockstep, multiplayer, desync, fixed-point, simulation | 2026-11-18 |
| co-op | Co-op Play (Topology, State, Scaling) | feature, co-op, multiplayer, networking, replication, save, session, party, difficulty, host, dedicated-server, drop-in | 2026-11-24 |
| stardew-valley-co-op | Stardew Valley Co-op (Case Study) | feature, co-op, stardew-valley, host, farmhand, save, shared-world, per-player, peer-to-peer, lidgren | 2026-11-24 |
| performance-data-oriented | Performance & Data-Oriented Design (UPS Optimization) | feature, performance, ups, data-oriented, soa, cache, belt, optimization | 2026-11-18 |
| data-driven-modding | Data-Driven Architecture & Modding | feature, data-driven, modding, lua, prototype, content, scripting | 2026-11-18 |
| factory-automation | Factory & Automation Design (Core Loop, Pollution, Blueprints) | feature, factory, automation, core-loop, pollution, blueprint, design | 2026-11-18 |
| inventory-equipment | Inventory & Equipment System | feature, inventory, equipment, items, lyra, gas, data-driven | 2026-11-18 |
| durability-reforging-genetics | Durability, Reforging & Item Genetics | feature, items, durability, reforging, crafting, genetics, inheritance, lineage, affixes, legacy, pokemon, gas, save | 2026-11-19 |
| crafting-tag-based | Tag-Based Ingredient Crafting | feature, crafting, items, ingredients, tags, categories, atelier, monster-hunter, left-4-dead, crock-pot, alchemy, opportunity-cost | 2026-11-20 |
| save-system | Save/Load & Persistence | feature, save, load, serialization, usavegame, versioning, migration | 2026-11-18 |
| enemy-ai | Enemy AI (Behavior Trees, EQS, Utility) | feature, enemy, ai, behavior-tree, eqs, utility, statetree, fsm | 2026-11-18 |
| director | AI Director & Pacing System | feature, director, pacing, storyteller, difficulty, threat-budget | 2026-11-18 |
| faction-system | Faction & Reputation System | feature, faction, reputation, fame, infamy, diplomacy | 2026-11-18 |
| economy | Economy & Trading | feature, economy, currency, sources, sinks, inflation, pricing | 2026-11-18 |
| progression | Progression & Leveling Runtime | feature, progression, xp, leveling, perk, skill, gas | 2026-11-18 |
| world-gen | Procedural World Generation (UE PCG) | feature, world-gen, pcg, procedural, biome, landscape, voronoi | 2026-11-18 |

Add one row per feature; stable kebab-case slug, lowercase tags.
