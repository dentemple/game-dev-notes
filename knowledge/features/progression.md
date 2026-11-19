---
title: Progression & Leveling Runtime
tags: [feature, progression, xp, leveling, perk, skill, gas]
source: https://www.engadget.com/2014-04-13-wow-archivist-wows-talent-system-has-come-full-circle.html (accessed 2026-11-18)
updated: 2026-11-18
---

# Progression & Leveling Runtime

## Goal & scope

Implement XP, levels, skills, and perk/talent choices. See ../features/class-skill-leveling.md (the four
design models) and ../rpg-design.md (curves/damage).

## Primary sources

- Engadget "WoW Archivist":
  https://www.engadget.com/2014-04-13-wow-archivist-wows-talent-system-has-come-full-circle.html (accessed 2026-11-18)
- Cross-refs: class-skill-leveling.md, ../rpg-design.md, ../gameplay-ability-system.md

## Key decisions / trade-offs

- **XP-driven vs skill-driven** leveling (pick one, or blend).
- **Bounded numbers** (proficiency-like scaling) over stat inflation.
- **No mandatory filler nodes** (avoid the "illusion of choice").

## Implementation notes

- XP curve: "early levels fast, late ones long" (quadratic-ish) — see ../rpg-design.md.
- Perks/talents as **data** (DataTable) → GAS abilities / attribute modifiers.
- Derived stats recomputed; base attributes are the stored truth (../rpg-design.md).

## Anti-patterns / gotchas

- Cookie-cutter / mandatory talent nodes.
- Stat inflation (unbounded numbers).
- Skill-grinding without a cap.

## Verify-first

Re-verify XP/perk specifics against the 5e SRD / Skyrim UESP before using reference numbers.

## Related

../features/class-skill-leveling.md · ../rpg-design.md · ../gameplay-ability-system.md
