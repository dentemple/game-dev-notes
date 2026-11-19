---
title: Factory & Automation Design (Core Loop, Pollution, Blueprints)
tags: [feature, factory, automation, core-loop, pollution, blueprint, design]
source: https://teemo.dev/game-design/factorio/systems/core-loop-mine-automate/ (accessed 2026-11-18; from search summaries)
updated: 2026-11-18
---

# Factory & Automation Design (Core Loop, Pollution, Blueprints)

> Source note — the core-loop/pollution/blueprint specifics are from consistent search summaries, not a
> fetched primary. Re-verify before treating the numbers as load-bearing.

## Goal & scope

The *design* side of Factorio: the automation loop, the pollution→biter pressure valve, and the blueprint
system. Companion to the engineering feature files (determinism, performance, modding).

## Primary sources

- Game Design Lab "Factorio core loop" + community/teardown summaries (accessed 2026-11-18)
- Factorio Wiki "Blueprint" (accessed 2026-11-18)

## Key decisions / trade-offs

- **The core loop is self-pressurizing**: growing the factory generates pollution, which provokes biters,
  which forces better defenses — "grow the factory to research better defenses to survive the attacks
  caused by growing the factory."
- **The "automation ratchet"** is the compulsion driver: every manual task is a candidate for automation.

## Implementation notes (RESEARCH)

- **Core loop**: mine → smelt/assemble → science packs → research → pollution → biter attacks → defend →
  expand → launch rocket.
- **Pollution** (the pressure valve): machines emit pollution into 32x32 chunks; above ~15 units a chunk
  diffuses ~2% to neighbors; terrain absorbs it; an **evolution factor** (time + pollution + spawners
  killed) scales biter strength.
- **Blueprints**: copy a built area into a blueprint/book, share it as an **exchange string**, and let
  **construction robots** build the pasted ghosts; advanced: parameterized blueprints and force-build modes.

## Anti-patterns / gotchas

- A factory game with no external pressure (pollution/enemies) can feel aimless — the loop needs a
  problem to solve.
- Copy-paste without blueprint sharing loses the community/content flywheel.
- Ignoring the UPS ceiling on huge factories (design and performance are coupled — see
  performance-data-oriented.md).

## Verify-first

Re-verify the pollution numbers and blueprint specifics against the Factorio Wiki before using them as
reference values.
