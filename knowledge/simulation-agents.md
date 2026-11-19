---
title: Simulation Agents (Needs, Utility AI, Directors)
tags: [behavior, agent, simulation, utility-ai, needs, director, ai, rimworld, rct, cities-skylines]
source: https://mathiasmdesign.com/journal/74-the-pathfinder (accessed 2026-11-18)
updated: 2026-11-18
---

# Simulation Agents (Needs, Utility AI, Directors)

## Goal & scope

How individual *agent* behavior drives simulation games, from three canonical examples — RollerCoaster
Tycoon (guests), Cities: Skylines (citizens/vehicles), RimWorld (colonists). Companion to
emergent-behavior.md (flocking/emergence) — that covers *group* behavior from neighbor rules; this covers
*individual* agents with needs and utility-driven decisions.

## Primary sources

- **RCT pathfinding** — https://mathiasmdesign.com/journal/74-the-pathfinder (accessed 2026-11-18)
- **RimWorld Mood** — https://rimworldwiki.com/wiki/Mood (accessed 2026-11-18)
- **Cities: Skylines Traffic AI** — https://colossalorder.fi/news/development-diary-2-traffic-ai/ (accessed 2026-11-18)

## The three approaches

### RollerCoaster Tycoon — bounded local behavior

Guests "walk randomly" and "pick a direction at junctions with near-zero intelligence" — **no global
pathfinding**. Real pathfinding only engages for a specific goal (the park exit), and even then "it has a
hard limit: five junctions," after which "the pathfinder gives up and returns a failure." The famous "I
can't find the park exit" thought is "a performance budget," not flavor (map → 7 junctions, mechanics → 8).

**Lesson**: *design out the expensive problem* — bounded search + no peep collision + wander-as-default is
how RCT simulated thousands of guests on 1999 hardware. (RCT's author was both programmer and designer.)

### Cities: Skylines — weighted agent pathfinding

"The core of pathfinding calculations is the four aspects: **Time, Comfort, Money, and Behavior**," with
age groups weighting them differently — "For teens the most important factor is Money," adults value Time,
seniors prefer Comfort. This is **utility scoring**: a decision = weighted sum of factors, per-agent.
Skylines II dropped the hard agent cap and leans on multicore; Skylines I capped at ~65,536 simulated
citizens (RESEARCH), so the *apparent* population always exceeded the *simulated* one.

### RimWorld — needs-driven pawns + a director

Colonists are **needs-driven agents**: mood is a **derived value** — base mood (difficulty-scaled) plus the
net of positive/negative **thoughts**; the visible bar drifts toward that "mood target." Mental-break
thresholds are explicit (5% extreme / 20% major / 35% minor), and every mood swing is **inspectable** via
the thought list. On top of needs, a **job AI** resolves a player-set work-priority matrix (1-4, fixed
left-to-right order; emergencies bypass it) into one-at-a-time tasks (RESEARCH). Above the pawns, the
**AI Storyteller** is a pacing **director** (Cassandra's 10.6-day cycle, a wealth-scaled threat budget, and
a hidden "adaptation" rubber-band) that generates "tellable moments" (RESEARCH).

## Common patterns (ANALYSIS)

1. **Needs/drives** — each agent tracks a handful of decaying needs; behavior chases the worst one.
2. **Utility scoring** — a decision is a weighted sum of factors (Skylines' Time/Comfort/Money/Behavior;
   RimWorld's work priorities) rather than a scripted sequence.
3. **A director/pacing layer** — a separate system schedules pressure and events (RimWorld's Storyteller),
   so the agent sim stays legible and the *narrative* stays tuned.
4. **Bounded, perf-informed simulation** — search-depth limits, agent caps, wander-as-default: constrain the
   simulation to what the hardware (and the design) can afford.

## Anti-patterns / gotchas

- Simulating every agent "honestly" when you only need the *appearance* of a crowd (RCT/Skylines bounded).
- Hidden randomness in agent decisions — RimWorld's mood is legible *because* it's an inspectable function
  of thoughts; hidden dice feel unfair.
- A director with no rubber-band — difficulty that doesn't adapt either snowballs or flatlines.
- Global pathfinding for every agent every frame (O(n) pathfinds) — use bounded search / flow fields / grids.

## Verify-first

Re-verify Skylines I's agent cap and RimWorld's exact need/break numbers against their wikis before quoting
them; the *patterns* (needs, utility scoring, director, bounded sim) are robust regardless of exact numbers.
