---
title: Class, Skill & Leveling Design (D&D 5e, Skyrim, WoW, Battlefield)
tags: [feature, class, skill, leveling, talent-tree, perk, progression, xp]
source: https://www.engadget.com/2014-04-13-wow-archivist-wows-talent-system-has-come-full-circle.html (accessed 2026-11-18)
updated: 2026-11-18
---

# Class, Skill & Leveling Design (D&D 5e, Skyrim, WoW, Battlefield)

## Goal & scope

Four models of class/skill/leveling, distilled into transferable choices for an ARPG. Companion to
../rpg-design.md (stats/itemization) and combat-dnd5e.md (bounded numbers).

## Primary sources

- Engadget "WoW Archivist" — talent-tree evolution (accessed 2026-11-18)
- D&D 5e SRD — classes/proficiency (accessed 2026-11-18; search summary)
- UESP "Skyrim:Leveling" (accessed 2026-11-18; 403 — search summary)

## Key decisions / trade-offs

- **XP-driven vs. skill-driven leveling**: D&D/WoW award XP for activities (controlled pace); Skyrim
  awards skill XP "by doing" (emergent, but grindable). Pick one, or blend.
- **Class identity vs. flexibility**: fixed classes (D&D, WoW, Battlefield) vs. classless (Skyrim).
- **Talent/perk trees = horizontal choice within a vertical level** — but guard the "illusion of choice".

## Implementation notes (sourced unless labeled)

- **D&D 5e** (RESEARCH): proficiency bonus +2→+6 by level; Ability Score Improvements at 4/8/12/16/19;
  subclass at level 2-3. → a bounded progression curve + periodic "feat/ASI" choice points.
- **Skyrim** (RESEARCH): "learn by doing" — 18 skills (Magic/Combat/Stealth); character XP = skill
  levels gained; XP-to-level ≈ (level+3) × 25; classes removed; ~250 perks; Legendary-skill reset. →
  skill-use-based XP, one perk point per level.
- **WoW Vanilla/TBC**: three trees, 51 points; "Hybrid builds were not ideal from a min/max
  perspective, but they were popular" — "TBC was the golden age of such builds."
- **WoW Wrath**: 71 points/11 tiers + Dual Specialization ("one of WoW's biggest
  gamechangers") — spec-switching replaced hybrid builds.
- **The lesson**: the old trees were "an illusion of choice while cookie cutter specs
  dominated" — "most points went to 'cookie cutter' talents that added raw damage." → **every node must
  be a real choice; avoid mandatory filler.**
- **Battlefield** (RESEARCH): 1942's five classes → BF2's seven → 2142's four (Assault/Engineer/
  Support/Recon) with dual unlock trees. → **few, high-contrast classes with distinct kits beat many
  overlapping ones** (BF2's seven classes overlapped; 2142's four is the consensus best).

## UE mapping

- Classes/skills/perks as **DataTables/DataAssets** (see data-driven-modding.md); abilities via **GAS**
  (see ../gameplay-ability-system.md); roles/kit via **GameplayTags**.
- Progression curves per ../rpg-design.md; bounded numbers per combat-dnd5e.md.

## Anti-patterns / gotchas

- Cookie-cutter/mandatory talent nodes (the "illusion of choice").
- Too many overlapping classes (Battlefield's 7-class problem).
- Skill-grinding without a cap (Skyrim's crafting power-leveling).
- Level scaling that erases the sense of progression (Skyrim's controversy).

## Verify-first

Re-verify the 5e proficiency/ASI table against the SRD and Skyrim's formulas against UESP before using
them as reference numbers.
