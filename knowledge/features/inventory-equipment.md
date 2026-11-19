---
title: Inventory & Equipment System
tags: [feature, inventory, equipment, items, lyra, gas, data-driven]
source: https://dev.epicgames.com/documentation/unreal-engine/lyra-inventory-and-equipment-in-unreal-engine (accessed 2026-11-18)
updated: 2026-11-18
---

# Inventory & Equipment System

## Goal & scope

Model the "what the player owns and wears" layer: items, inventory, and equipment. This is a *starting
point* — the design lives in ../rpg-design.md (itemization) and ../features/class-skill-leveling.md
(builds/durability).

## Primary sources

- Epic "Lyra Inventory and Equipment":
  https://dev.epicgames.com/documentation/unreal-engine/lyra-inventory-and-equipment-in-unreal-engine (accessed 2026-11-18)
- Cross-refs: ../rpg-design.md, ../gameplay-ability-system.md, data-driven-modding.md

## Key decisions / trade-offs

- **Inventory ≠ equipment**: inventory = "in your possession, may be stowed"; equipment = "held/worn/
  used." Different ownership (Controller vs Pawn) and lifetime.
- **Items as data definitions composed of fragments** (EquippableItem, SetStats, PickupIcon), not a
  class hierarchy.
- **Equipping grants Ability Sets** to the Ability System Component (the GAS hook).

## Implementation notes (Lyra)

- `InventoryItemDefinition` holds fragments; `InventoryItemInstance` = one item + stat-tag stacks;
  `EquipmentDefinition` grants abilities and spawns actors on equip; `EquipmentManagerComponent` manages
  weapons one-at-a-time.
- If you want durability, model it as a `UAttributeSet` value decremented per use (see
  ../features/combat-botw-genshin.md).

## Anti-patterns / gotchas

- Hardcoded item types instead of fragment-composed definitions.
- Storing mutable runtime state in the item *definition* (it's data; instances hold state).
- A deep item class hierarchy (composition wins).

## Verify-first

Re-verify Lyra's InventoryManagerComponent / EquipmentManagerComponent against dev.epicgames.com.

## Related

../rpg-design.md · ../gameplay-ability-system.md · ../features/class-skill-leveling.md · ../features/save-system.md
