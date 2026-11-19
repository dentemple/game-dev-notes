---
title: Modding Support (Mod-First Architecture)
tags: [modding, mod-first, ugc, modio, steam-workshop, pak, game-features, data-driven, gameplaytags, plugin]
source: https://www.strayspark.studio/blog/modding-support-ue5-mod-io-ugc (accessed 2026-11-18)
updated: 2026-11-18
---

# Modding Support (Mod-First Architecture)

## The defining constraint (RESEARCH — Epic forums)

In a packaged/shipping Unreal game you **cannot load arbitrary C++/DLL mods**: shipping builds use
monolithic linking, and loading untrusted native code is a security risk (and iOS forbids shipping
dylibs). So "mod-first" in UE realistically means **content-only mods — Blueprints, data assets, and
PAK content** — plus optionally a game-provided scripting layer. Architect for that from day one.

## Mod content & distribution

- Mods are additional **PAK files** mounted alongside the base game. "When multiple PAK files contain
  assets at the same path, UE5 uses a priority system"; mods add or override content by matching asset
  paths.
- Distribution: **mod.io** (leading cross-platform UGC, official UE plugin), **Steam Workshop**
  (Steamworks), direct PAK, or a custom CDN. The mod.io plugin offers C++/Blueprint, background
  downloads + delta updates, and SSO auth; it supports the 3 most recent UE versions.
Source: https://www.strayspark.studio/blog/modding-support-ue5-mod-io-ugc (accessed 2026-11-18).

## Runtime PAK loading

1. Mount via `FPakPlatformFile` (or `IPluginManager::MountExplicitlyLoadedPlugin` for plugin-cooked content).
2. Mount to the exact virtual path the assets were cooked under (e.g. `/Game/Mods/MyMod/`) — "a mismatch
   between cook path and mount point makes every reference fail to resolve."
3. Call `AssetRegistry.ScanPathsSynchronous` on the mounted path, or lookups/async loads return nothing.
4. Mods must be cooked with the **same engine version and target platform** as the game.
Source: https://bugnet.io/blog/how-to-fix-unreal-mod-pak-not-mounting-at-runtime (accessed 2026-11-18).

## Mod-first architecture (sourced unless labeled)

- **Epic's Game Features + Modular Gameplay plugins** are the first-party primitive: "Build standalone
  features that you can quickly activate or deactivate." Each feature has a `GameFeatureData` asset and
  built-in actions — **Add Components** (inject components into actors), Add Data Registry, Add World
  Partition Content, Add Cheats. Lifecycle is driven by `UGameFeaturesSubsystem`.
Source: https://dev.epicgames.com/documentation/unreal-engine/game-features-and-modular-gameplay-in-unreal-engine (accessed 2026-11-18).
- **Data-driven design** (RESEARCH): logic reads data, not specific content. `DataTable` for many rows of
  identical shape; `DataAsset` for a few rich configs; **GameplayTags over hard enums** (extensible, no
  recompile); `SoftObjectPtr` for lazy-loading mod icons/meshes.
- **Plugin hygiene** (RESEARCH): use an interface module to break cross-domain coupling; avoid
  parent↔child plugin dependency cycles.

## Lower the barrier for modders

- "Provide a standalone mod packaging tool" — a small executable that cooks a folder of mod assets into a
  PAK, so "the modder never sees a command line."
- Support **raw image formats (PNG/TGA)** for texture-only mods (skips the cooking step).
- "In-game mod creation tools" — a level editor / character customizer that cooks and packages internally.
Source: https://www.strayspark.studio/blog/modding-support-ue5-mod-io-ugc (accessed 2026-11-18).

## Anti-patterns / gotchas

- Planning for C++ code mods in shipping (needs `TargetLinkType.Modular` + a custom loader + accepting
  untrusted native code).
- Hard-coded content references instead of data-driven lookup — kills the ability to add/override content.
- Mount-point/cook-path mismatch, or skipping the AssetRegistry scan (the #1 "pak won't mount" cause).
- Ignoring engine-version/platform compatibility — a mod cooked on a different version won't load.

## Verify-first

Re-verify the Game Features plugin and PAK-mounting APIs against dev.epicgames.com before coding; confirm
the mod.io plugin's current UE version support at docs.mod.io.
