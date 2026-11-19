---
title: Save/Load & Persistence
tags: [feature, save, load, serialization, usavegame, versioning, migration]
source: https://www.strayspark.studio/blog/ue5-save-system-versioning-2026 (accessed 2026-11-18)
updated: 2026-11-18
---

# Save/Load & Persistence

## Goal & scope

Persist game state (character, inventory, quests, world flags) across sessions, with versioning so
patches don't break old saves. See ../game-architecture.md (save versioning) and
../features/deterministic-simulation.md (determinism).

## Primary sources

- StraySpark "UE5 Save System Versioning":
  https://www.strayspark.studio/blog/ue5-save-system-versioning-2026 (accessed 2026-11-18)
- Cross-refs: ../game-architecture.md, roguelike-core.md

## Key decisions / trade-offs

- **USaveGame** object plus an explicit **schema version field** ("every save file starts with a version
  number").
- **Migrate forward, never reset** — ordered, idempotent migrations.
- **Async I/O** (`AsyncSaveGameToSlot`) to avoid game-thread hitches.
- **Stable IDs**, not array indexes.

## Implementation notes

- Header: `SchemaVersion` + `GameBuildVersion` + timestamp.
- Migrations: `v1→v2→…`, additive only (defaults for new fields), never reverse.
- Keep a backup slot; validate on load and fall back to the backup on corruption.
- Unreal serializes by UPROPERTY name/type — don't rename or retarget existing properties (they silently
  reset). Adding/removing fields is safe.

## Anti-patterns / gotchas

- Resetting a failed load to defaults (wipes progress) — migrate instead.
- Saving derived/absolute state instead of stable IDs.
- Renaming UPROPERTY fields across versions.

## Verify-first

Re-verify `USaveGame` and `AsyncSaveGameToSlot` against dev.epicgames.com.

## Related

../game-architecture.md · ../features/deterministic-simulation.md · ../features/inventory-equipment.md
