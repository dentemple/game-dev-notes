---
title: Enemy Tactics & AI Archetypes (Monsters Know What They're Doing)
tags: [feature, enemy, combat, ai, tactics, monster, archetype, self-preservation, retreat, morale]
source: https://www.themonstersknow.com/why-these-tactics/ (accessed 2026-11-18)
updated: 2026-11-18
---

# Enemy Tactics & AI Archetypes (Monsters Know What They're Doing)

## Goal & scope

Keith Ammann's framework for making enemies behave *intelligently* — self-preservation, stat-driven
archetypes, and exploiting their own abilities — mapped to enemy AI for an ARPG.

## Primary sources

- **Ammann** — "Why These Tactics?" (themonstersknow.com):
  https://www.themonstersknow.com/why-these-tactics/ (accessed 2026-11-18)
- **Enemy-AI FSM** — state-machine patterns (see combat.md)

## Key decisions / trade-offs

- **Monsters act to survive and win, not to be farmed** — self-preservation and ability-use make combat
  legible and non-monotone.
- **Derive behavior from stats/abilities** — an enemy's role follows from its numbers, not hand-waved AI.

## Implementation notes (sourced unless labeled)

- **Self-preservation** (Ammann): "Every creature wants, first and foremost, to survive." When reduced to
  ~40% HP or less, most will **flee** (exceptions: fanatics, or those who believe flight = being hunted).
  → an enemy AI with a **retreat/rout threshold**, not "fight to the death."
- **Stats dictate the archetype** (Ammann): "Physical abilities influence fighting styles." High
  STR/CON + low DEX = "brutes that will welcome a close-quarters slugfest"; the inverse → skirmishers.
  → derive AI role from an enemy's stat profile (brute / skirmisher / artillery / controller).
- **Intelligence/Wisdom tiers** (Ammann): a creature of low Intelligence "operates purely from instinct";
  higher tiers allow planning, coordination, and targeting weaknesses.
  → a "smarts" parameter that gates coordinated/targeted behavior.
- **Exploit advantage features** (Ammann): "A creature with a feature that gives it an advantage… will
  always prefer to use that feature"; it seeks "the best possible result from whatever movement, actions,
  bonus actions and reactions are available."
  → a utility/scoring layer that prefers the enemy's most effective ability (see combat.md for FSM).

## Anti-patterns / gotchas

- Enemies that fight to the death with no retreat/rout state (Ammann's core correction).
- One AI behavior for all enemies instead of stat/role-derived behavior.
- Enemies that ignore their strongest ability in favor of a generic attack.

## Verify-first

Re-verify the exact 40% retreat threshold and archetype mapping against Ammann's book/blog before
hard-coding; the percentages are a starting point, not a spec.
