---
title: RPG Design (Systems, Progression, Itemization)
tags: [rpg, stats, leveling, progression, itemization, loot, damage, balance, gas, attributes]
source: https://www.gamedeveloper.com/design/defining-loot-tables-in-arpg-game-design (accessed 2026-11-18)
updated: 2026-11-18
---

# RPG Design (Systems, Progression, Itemization)

## Genre & core loop

An RPG owns "the numbers that make a character grow: stats, levels, damage, items and quests." The
loop is **explore → encounter (fight/talk/solve) → earn (XP/loot/story) → grow (level/gear/unlock) →
harder content**. Must-have systems: stats + leveling, inventory + equipment, combat, quests, dialogue,
save/load, economy/progression gating, and character/UI.
Source: gamedev-skills RPG playbook (accessed 2026-11-18).

## Stats & progression

- **Derived stats are recomputed, never stored**: "Base attributes are the only stored truth; derived
  stats are recomputed." Apply gear/buffs as a reversible modifier layer to avoid value drift.
- **Damage formula**: `dmg * K / (K + def)` — "each defense point adds the same effective HP (1/K of
  HP), so defense never makes anyone immune." (This is the ratio-mitigation default; pick deliberately
  vs. subtractive mitigation.)
- **XP curve**: "early levels fast, late ones long."
Source: gamedev-skills RPG playbook (accessed 2026-11-18).

## Progression curves & balance (RESEARCH — Schreiber & Romero, primary 403)

Curve types: **identity, linear, exponential, logarithmic, triangular** (and custom-crafted). Establish
an **anchor** baseline value and scale it with the chosen curve. Spreadsheet the damage/XP/cost tables
before coding.
Source: *Game Balance* (Schreiber & Romero) (accessed 2026-11-18).

## Itemization & loot

- **Two tables**: one for base items, one for affixes/modifiers.
- Generation is **five ordered decisions**: drop? → rarity → type → affixes → numerical rolls.
- Rarity via weighted roll (e.g. 41-60 regular, 61-80 magic, 81-93 rare, 94-100 legendary); affixes
  filtered by rarity/type; item-level scales affix values.
- **Smart loot** biases drops toward the player's class/needs; "a good loot table is about controlled
  randomization" — random enough to surprise, deterministic enough to plan.
Source: https://www.gamedeveloper.com/design/defining-loot-tables-in-arpg-game-design (accessed 2026-11-18).

## UE mapping (Epic Lyra)

Lyra is the reference architecture: **inventory items** (owned by the Controller via
`InventoryManagerComponent`) vs **equipment items** (owned by the Pawn via
`EquipmentManagerComponent`). Item definitions are composed of **fragments** (e.g. `SetStats`,
`EquippableItem`); **equipping grants Ability Sets** to the ASC. For a solo UE RPG: GAS + a custom
`UAttributeSet` (see gameplay-ability-system.md) + data-driven item definitions (see modding-support.md).
Source: https://dev.epicgames.com/documentation/unreal-engine/lyra-inventory-and-equipment-in-unreal-engine (accessed 2026-11-18).

## Enemy AI (RESEARCH — community consensus)

Use a **finite state machine** (patrol → investigate → attack → flee, with windup/recover/stagger); boss
encounters add **phases** keyed to health thresholds. **Telegraph** attacks (wind-up/glow/ground marker)
before they land for fairness.
Source: Unity "How enemies decide what to do" + community (accessed 2026-11-18).

## Scope discipline (RESEARCH — practitioner)

RPGs are the canonical never-ship genre. "Shipping rewards restraint more than ambition." Lock a minimum
viable feature set early; every added system ripples into UI, balance, save data, and QA. Celeste,
Vampire Survivors, and Undertale are the counter-examples: small, focused, shipped.

## Verify-first

Re-verify GAS/Lyra API specifics against dev.epicgames.com before coding; spread out the damage/XP/rarity
tables before implementing.
