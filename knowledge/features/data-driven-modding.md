---
title: Data-Driven Architecture & Modding
tags: [feature, data-driven, modding, lua, prototype, content, scripting]
source: https://wiki.factorio.com/Modding (accessed 2026-11-18)
updated: 2026-11-18
---

# Data-Driven Architecture & Modding

## Goal & scope

Factorio's model for making **all content data-defined and moddable** — a Lua prototype layer plus a
runtime modding API. (Complements ../modding-support.md, which covers UE's PAK/plugin modding.)

## Primary sources

- **Factorio Wiki Modding** — https://wiki.factorio.com/Modding (accessed 2026-11-18)
- **Factorio Lua API** (RESEARCH) — http://lua-api.hornwitser.no/1.1.104/index.html (accessed 2026-11-18)

## Key decisions / trade-offs

- **Content is data**: every item/recipe/entity is a *prototype* (a data table), not code — so adding or
  modding content never touches the engine.
- **A full scripting API** (Lua 5.2.1) is exposed to mods, with events and class wrappers around the
  deterministic sim.

## Implementation notes (sourced unless labeled)

- "You need to use the Lua programming language (version 5.2.1) to create any mods in Factorio."
  (Factorio Wiki Modding)
- "The game's mod system injects your code into the startup and to the data construction stage of the
  game." (Factorio Wiki Modding)
- **Three-stage data lifecycle** (RESEARCH): `settings` (mod config) → `prototype`/`data` (define
  prototypes as Lua tables via `data.extend()`) → `runtime` (event handlers via `script.on_event()` on the
  live game world). (Factorio Lua API)
- Prototypes use **inheritance** (base → derived), which is how mods add variants cheaply. (RESEARCH)

## Anti-patterns / gotchas

- Hardcoding item/recipe/entity definitions in engine code (un-moddable).
- Exposing a scripting API that isn't deterministic (mods must be able to run deterministically for
  lockstep — see deterministic-simulation.md).
- No versioning/migration for the data schema (see ../game-architecture.md save versioning).

## Verify-first

Re-verify the three-stage data lifecycle against the Factorio Lua API docs before mirroring it; in UE,
the analogue is DataTables/DataAssets + GameplayTags + a scripting layer (see ../modding-support.md).
