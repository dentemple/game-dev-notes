---
title: 4X Military & Warfare Design (Total War, Civ 6, Humankind)
tags: [4x, warfare, military, strategy, combat, morale, units, war-weariness, diplomacy, terrain]
source: https://civilization.fandom.com/wiki/War_weariness_(Civ6) (accessed 2026-11-18; 402 — content from search summaries)
updated: 2026-11-18
---

# 4X Military & Warfare Design (Total War, Civ 6, Humankind)

> Source note — the primary pages (Rock Paper Shotgun, the Civ wiki, the Humankind encyclopedia) were
> blocked/402 this session; the content below is from consistent search summaries. Re-verify before
> load-bearing use.

## The 4X military layer

4X = **eXplore, eXpand, eXploit, eXterminate** (coined by Alan Emrich, 1993). The military layer
("exterminate") is tied to tech progression and diplomacy; combat ranges from *abstract* (strength
comparison) to *tactical* (positional), turn-based or real-time.

## Three combat-resolution models (RESEARCH)

- **Total War** — turn-based campaign map + **real-time tactical battles**. Unit counters (the classic
  triangle: spears > cavalry > swords > spears, with ranged/war-machines/heroes as wildcards) plus
  **morale/rout**, formations (depth, wedge, phalanx), and flanking/terrain/fatigue. Medieval 3's stated
  direction: favor **situational/contextual counters** (terrain, exhaustion, disorganization, crowding)
  over hard rock-paper-scissors, citing Starcraft as the balancing paradigm.
- **Civilization 6** — **one-unit-per-tile**, abstract resolution. Melee (attack by moving, can capture
  cities) vs ranged (attack at range, weak in melee, can't capture). Combat strength is an **absolute
  difference** (~30 gap one-shots, ~20 is negligible); flanking/support give +2 per adjacent friendly.
  Aggression is gated by **war weariness** (an amenity/happiness penalty) and **warmonger penalties**
  (capturing/razing cities, surprise wars), reducible via **casus belli**.
- **Humankind** — armies **unstack into units for a mini turn-based battle on the world map** (3 rounds
  per campaign turn; reinforce by moving adjacent armies into the battle). War is gated by **war
  support** and requires a **casus belli** — surprise attacks carry heavy penalties.

## Transferable systems (for a solo UE game) (RESEARCH)

- **Data-driven units** — a DataTable/DataAsset per unit (stats, type, counters, cost) — see
  modding-support.md.
- **Prefer abstract over tactical resolution** — a Civ-style strength + modifier formula is tractable
  solo; a Total War-scale real-time battle engine is specialist scope (and Humankind's world-map battle
  is the middle path).
- **Morale/rout** (Total War) — a per-unit state machine (steady → wavering → routing) driven by
  flanking, terrain, exhaustion, and casualties.
- **Terrain modifiers** — a grid with terrain flags feeding combat bonuses.
- **War weariness + warmonger** (Civ) — a pressure valve: war accrues penalties that sour diplomacy and
  hurt happiness, preventing endless, consequence-free war.
- **War support + casus belli** (Humankind) — war requires a justification; surprise war costs you.

## Anti-patterns / gotchas (RESEARCH)

- Building a Total War-scale real-time battle engine for a solo project.
- Hard RPS "color matching" counters that remove tactical nuance (Medieval 3 explicitly avoids this).
- No war-cost system → endless consequence-free war (Civ and Humankind both gate aggression).

## Verify-first

Re-verify the specific mechanics (Civ combat-strength formula, Humankind battle rules, war-weariness
numbers) against a fetchable primary before coding.
