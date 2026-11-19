---
title: AI Director & Pacing System
tags: [feature, director, pacing, storyteller, difficulty, threat-budget]
source: https://teemo.dev/game-design/rimworld/systems/the-ai-storyteller/ (accessed 2026-11-18; from search summaries)
updated: 2026-11-18
---

# AI Director & Pacing System

> Source note — RimWorld Storyteller specifics are from search summaries (re-verify against the wiki).
> The *director pattern* is documented in ../simulation-agents.md.

## Goal & scope

A meta-system that schedules challenge and relief — the RimWorld Storyteller / Left 4 Dead Director
pattern. See ../simulation-agents.md (directors) and encounter-design.md (pacing beats).

## Primary sources (RESEARCH — re-verify)

- RimWorld Storyteller analysis (teemo.dev)
- Cross-refs: ../simulation-agents.md, encounter-design.md, ../4x-warfare.md (pressure)

## Key decisions / trade-offs

- **Threat budget** derived from player wealth/strength, not a script.
- **Rubber-band** (adaptation) raises/lowers pressure based on player performance.
- Distinct **personalities** (Cassandra's fixed cycle vs Randy's random) = pacing profiles.

## Implementation notes (RESEARCH)

- Cassandra ≈ 10.6-day on/off cycle; threat scaled by wealth + colonist count + recent events.
- A clamped "adaptation" counter adjusts difficulty.
- Emit events as **data** (a weighted schedule of incident types), not hardcoded branches.

## Anti-patterns / gotchas

- No rubber-band → difficulty snowballs or flatlines.
- A director with perfect information / rules the player can't perceive (feels arbitrary).

## Verify-first

Re-verify the RimWorld Storyteller mechanics against the wiki before mirroring.

## Related

../simulation-agents.md · encounter-design.md · ../4x-warfare.md · ../design-best-practices.md
