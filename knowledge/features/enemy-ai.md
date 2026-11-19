---
title: Enemy AI (Behavior Trees, EQS, Utility)
tags: [feature, enemy, ai, behavior-tree, eqs, utility, statetree, fsm]
source: https://dev.epicgames.com/community/learning/talks-and-demos/yj7j/designing-and-implementing-your-game-s-ai-architecture-in-unreal-engine-unreal-fest-2024 (accessed 2026-11-18; from search summaries)
updated: 2026-11-18
---

# Enemy AI (Behavior Trees, EQS, Utility)

> Source note — UE-specific AI specifics are from search summaries (re-verify against Epic docs). The
> *design* layer is already documented in enemy-tactics.md.

## Goal & scope

Implementing enemy decision-making in UE. This is the *implementation*; the *roles/archetypes* are in
enemy-tactics.md, the frame-data in combat.md, and *movement* in ../emergent-behavior.md.

## Primary sources (RESEARCH — re-verify)

- Unreal Fest 2024 "Designing and Implementing Your Game's AI Architecture" (search summary)
- Cross-refs: enemy-tactics.md, combat.md (FSM), ../emergent-behavior.md (steering), ../simulation-agents.md (utility)

## Key decisions / trade-offs

- **FSM** for 2–6 states; **Behavior Tree + Blackboard + EQS** for hierarchical humanoid enemies;
  **State Tree** (UE 5.7+, Epic's newer default); **Utility AI** for many competing actions.
- **Layered**: perceive (Blackboard) → decide (BT) → path → steer → animate.
- **Perception budget**: tick decision logic at ~5–10 Hz; cap fully-thinking agents near the player.

## Implementation notes (RESEARCH)

- Blackboard = NPC memory (sensors write, behaviors read).
- EQS = spatial queries (cover, flanking, retreat points) → results feed back into the Blackboard.
- Common shipping mix: FSM top-level (Idle/Combat/Dead) + BT/Utility inside Combat.
- Map Ammann's stat→archetype (enemy-tactics.md) to BT/Utility parameters.

## Anti-patterns / gotchas

- Perfect-information AI (reads player position directly = "psychic").
- Giant Blackboards becoming "global variable soup."
- Expensive per-frame decorators.

## Verify-first

Re-verify BT / EQS / StateTree APIs against dev.epicgames.com before coding.

## Related

enemy-tactics.md · combat.md · ../emergent-behavior.md · ../simulation-agents.md
