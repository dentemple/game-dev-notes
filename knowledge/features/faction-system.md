---
title: Faction & Reputation System
tags: [feature, faction, reputation, fame, infamy, diplomacy]
source: https://rpgcodex.net/article.php?id=7142 (accessed 2026-11-18)
updated: 2026-11-18
---

# Faction & Reputation System

## Goal & scope

Track the player's standing with factions and its consequences. See ../social-interaction.md (the
two-axis reputation model) and ../4x-warfare.md (war/diplomacy pressure).

## Primary sources

- rpgcodex — Avellone on Fallout: New Vegas:
  https://rpgcodex.net/article.php?id=7142 (accessed 2026-11-18)
- Cross-refs: ../social-interaction.md, ../4x-warfare.md

## Key decisions / trade-offs

- **Two-axis reputation** (Fame + Infamy per faction), not one global morality meter.
- Consequences (access, hostility, quests, endings) derive from reputation, not karma.
- Speech/diplomacy should be as rewarding as combat.

## Implementation notes (sourced unless labeled)

- Track Fame and Infamy **separately** so they don't cancel → nuanced labels ("Soft-Hearted Devil").
- Faction checks in dialogue: "checks for faction, and different reactions depending on rep."
- Gate quests/endings on faction standing (New Vegas's NCR / Legion / House / Yes Man) (RESEARCH).

## Anti-patterns / gotchas

- A single global good/evil karma meter.
- Reputation that never affects gameplay (pure flavor).
- Fame and Infamy cancelling each other out.

## Verify-first

Re-verify New Vegas's Fame/Infamy scales against the Fallout wiki.

## Related

../social-interaction.md · ../4x-warfare.md · ../features/quest-dialogue.md
