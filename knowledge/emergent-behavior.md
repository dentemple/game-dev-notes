---
title: Emergent Behavior (Boids, Steering, Swarms)
tags: [behavior, flocking, boids, emergence, steering, swarm, stigmergy, crowd, ai, simulation]
source: https://www.red3d.com/cwr/boids/ (accessed 2026-11-18)
updated: 2026-11-18
---

# Emergent Behavior (Boids, Steering, Swarms)

## Goal & scope

How to capture complex *group* behavior with **concise algorithms** — the academic foundation (Reynolds'
boids, the Vicsek model, swarm intelligence) plus game applications (Total War unit cohesion, UE flocking).

## Primary sources

- **Reynolds, "Flocks, Herds, and Schools" (SIGGRAPH 1987)** — https://www.red3d.com/cwr/boids/ (accessed 2026-11-18)
- **Reynolds, "Steering Behaviors for Autonomous Characters" (GDC 1999)** — https://www.red3d.com/cwr/steer/gdc99/ (accessed 2026-11-18)
- **Vicsek et al., PRL 75, 1226 (1995)** (RESEARCH) — https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.75.1226 (accessed 2026-11-18)
- **Swarm intelligence / stigmergy** (RESEARCH) — Bonabeau–Dorigo–Theraulaz; ACO (Dorigo 1991) (accessed 2026-11-18)
- **UE flocking** (RESEARCH) — UCrowdFollowingComponent / dtCrowd / Niagara boids (accessed 2026-11-18)

## The core idea

Flocking is "a particularly evocative example of emergence": **complex global behavior can arise from the
interaction of simple local rules**, with no central control. That is the entire trick — *each agent runs
a tiny local rule set; the group behavior is an emergent property.*

## Boids — the three rules

Each boid steers by three local forces:
1. **Separation** — "steer to avoid crowding local flockmates."
2. **Alignment** — "steer towards the average heading of local flockmates."
3. **Cohesion** — "steer to move toward the average position of local flockmates."

Perception is strictly local: a boid "reacts only to flockmates within a certain small neighborhood"
(distance + angle); "flockmates outside this local neighborhood are ignored."

## Steering behaviors — the building blocks

Individual behaviors that each return a steering force vector:
**Seek / Flee / Arrive / Pursuit / Evasion / Wander / Obstacle avoidance / Path following** (plus
leader-following, flow-field following). The canonical force model:
`desired_velocity = normalize(target - position) * max_speed`; `steering = desired_velocity - velocity`;
then `acceleration = steering / mass` and `velocity = clamp(velocity + acceleration, max_speed)`.

**Combining behaviors** is where it gets subtle: weighted **summation** is simplest but "component
behaviors may cancel each other out"; **prioritized dithering** (pick the first non-zero priority behavior)
is more robust; discrete behavior *switching* belongs at an action-selection layer above steering.

## Emergence theory (RESEARCH)

- **Vicsek model** (1995): constant-speed self-propelled particles that align to the average neighbor
  direction + noise. It exhibits a **noise-driven order→disorder phase transition** — the *minimum*
  model that still shows flocking, and the reason tuning (noise, neighbor range) matters. **Metric**
  (fixed radius) vs **topological** (k-nearest) neighbor choice changes the phase behavior.
- **Swarm intelligence / stigmergy**: ants coordinate *indirectly* by depositing pheromone (environment as
  shared memory); positive feedback (reinforce good paths) + negative feedback (evaporation) converges to
  shortest paths (ACO). The lesson: you can get group intelligence with **local rules + a shared field**
  instead of direct communication.

## Game application (RESEARCH)

- **Total War** moves units with a **flocking/neighbor-based algorithm + a spatial grid** for neighbor
  lookup (each entity queries only its tile + neighbors, avoiding O(n²)). Formation-keeping rules
  ("Formation Attack" = cohesive; mobs blob) sit on top; targeting the *center* of an enemy unit produces
  the well-known blobbing.
- **Unreal Engine**: **Niagara** GPU boids (Neighbor Grid 3D; cohesion/alignment/separation + obstacle
  avoidance) for 10k+ particles; **UCrowdFollowingComponent / dtCrowd** (DetourCrowd) for CPU crowd
  steering; **Mass Entity** for tens of thousands of navigation-driven agents. A spatial hash / neighbor
  grid is the standard O(n·k) neighbor query.

## The concise-algorithm playbook (ANALYSIS)

To capture complex group behavior cheaply:
1. **Pick 2-4 local rules** (separation/alignment/cohesion; or seek/arrive/wander).
2. **Make perception local** (a radius/angle, or k-nearest), and use a **spatial grid** for O(n·k) queries.
3. **Combine forces** with weighted sum (tune weights) or priority dithering.
4. **Lay a shared field** (pheromone/flow field) when you need coordination *between* agents without direct
   messaging.

## Anti-patterns / gotchas

- Summing many behaviors blindly (they cancel; tune weights or use priority).
- O(n²) "check everyone" neighbor loops — use a spatial grid/hash.
- Assuming more rules = more realistic (three rules already flock; more rules add tuning fragility).
- Global/per-agent randomness that breaks determinism (see features/deterministic-simulation.md).
- Treating "flocking" as the whole answer when you need *directed* motion — pair it with seek/path following.

## Verify-first

Re-verify the steering-force formulas against Reynolds' pages and UE's crowd APIs against dev.epicgames.com
before coding; start with the three boids rules and add obstacles/arrival only as needed.
