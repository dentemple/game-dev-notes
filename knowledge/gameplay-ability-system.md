---
title: Gameplay Ability System (GAS)
tags: [gas, abilities, asc, attributes, gameplayeffects, gameplaytags, lyra]
source: https://dev.epicgames.com/documentation/unreal-engine/gameplay-ability-system-for-unreal-engine (accessed 2026-11-18)
updated: 2026-11-18
---

# Gameplay Ability System (GAS)

## Core concepts (primary)

- **Ability System Component (ASC):** "The Ability System Component includes all the base
  functionality that an Actor Component implements." Every GAS-interacting actor needs one.
- **Gameplay Abilities:** "Create active or passive Gameplay Abilities, for Actors that
  coordinate with your project's gameplay mechanics" (subclass `UGameplayAbility`, C++ or BP).
- **Attributes / Attribute Sets:** "Use Attributes and Attribute Sets that store, calculate,
  and modify your gameplay-related values" (`UAttributeSet` + `FGameplayAttributeData`).
- **Gameplay Effects:** "Change Attributes with Gameplay Effects that provide a method to
  directly modify attribute values" (instant / duration / infinite, stacking rules).
- **Gameplay Tags:** hierarchical tags (e.g. `State.Stunned`) gate activation/blocking/cancel
  (not on the overview page; verify at the GAS docs topic directory).
- Source: https://dev.epicgames.com/documentation/unreal-engine/gameplay-ability-system-for-unreal-engine (accessed 2026-11-18).

## Setup (community-authoritative — tranek GASDocumentation; re-verify plugin name against Epic)

- Enable the **GameplayAbilities** plugin (Edit → Plugins; ships at
  `Engine/Plugins/Runtime/GameplayAbilities`, production-ready).
- Add `"GameplayAbilities", "GameplayTags", "GameplayTasks"` to `.Build.cs`
  (tranek uses `PrivateDependencyModuleNames`; some community docs prefer Public when GAS types
  appear in public headers — surface, don't assume).
- For UE **4.24–5.2** only: call `UAbilitySystemGlobals::Get().InitGlobalData()`; **5.3+** calls
  it automatically.
- Source: https://github.com/tranek/GASDocumentation (README, accessed 2026-11-18).

## Reference sample

- **Lyra** is Epic's official sample implementing GAS + Enhanced Input + modular gameplay:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine

## Note

GAS is a C++ framework (not enabled by default in a new project) exposed to Blueprint. The
canonical community reference is tranek's GASDocumentation; Epic's own docs are the primary
truth for API signatures.
