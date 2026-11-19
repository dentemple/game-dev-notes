---
title: Game Architecture (Actors, Components, Subsystems, Save)
tags: [architecture, actor, component, subsystem, event-dispatcher, interface, casting, save, versioning]
source: https://adventuresincausality.com/unreal/unreal-blueprint-architecture/ (accessed 2026-11-18)
updated: 2026-11-18
---

# Game Architecture (Actors, Components, Subsystems, Save)

## Class / lifetime selection (primary)

- "Use an Actor for an independently placed, spawned, replicated, or transformed entity."
- "Use an Actor Component for a reusable capability owned by an Actor."
- "Use a GameInstance Subsystem for one service spanning maps in one game instance."
- "Use a LocalPlayer Subsystem for per-local-player services and split-screen isolation."
- "Use a World Subsystem for one service per World."
- "Use a Data Asset for authored definitions; keep mutable runtime state elsewhere."
- "Use a Blueprint Function Library only for stateless operations."
Source: https://adventuresincausality.com/unreal/unreal-blueprint-architecture/ (accessed 2026-11-18).

## Event dispatchers (primary)

- "Use an Event Dispatcher when one known publisher notifies zero or more listeners."
- "Treat Event Dispatchers as publisher-owned signals, not global message buses."
- "Never bind a delegate repeatedly without a matching unbind or one-time guard."
- "Do not replace clear one-to-one calls with global messaging."
Source: https://adventuresincausality.com/unreal/unreal-blueprint-architecture/ (accessed 2026-11-18).

## Interfaces vs casting (primary)

- "Use a Blueprint Interface when the caller has a target but should not depend on its concrete class."
- "Treat Interfaces as contracts, not object discovery; a target reference is still needed."
Source: https://adventuresincausality.com/unreal/unreal-blueprint-architecture/ (accessed 2026-11-18).

## Hard rules (primary)

- "Avoid gameplay logic in Level Blueprints unless it truly belongs to that level."
- "Never use Get All Actors of Class as routine dependency injection."
- "Never store mutable session state in a Data Asset or class default object."
Source: https://adventuresincausality.com/unreal/unreal-blueprint-architecture/ (accessed 2026-11-18).

## Save systems (primary)

- "Every save file starts with a version number" (e.g. `uint32 SchemaVersion`).
- Migrate forward, never reset: "run migrations to bring the data up to current" via an ordered, idempotent chain.
- "Always write to a temp file first, then rename to the real slot" (atomic/crash-safe); test migration chains, not isolated migrations.
Source: https://www.strayspark.studio/blog/ue5-save-system-versioning-2026 (accessed 2026-11-18).

## Note for solo dev

Choose the class with the right lifetime for each job; use subsystems for services, dispatchers for one-to-many signals, and interfaces over concrete casts. Version your save schema from day one.
