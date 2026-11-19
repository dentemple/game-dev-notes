---
title: Deterministic Simulation & Lockstep Multiplayer
tags: [feature, determinism, lockstep, multiplayer, desync, fixed-point, simulation]
source: https://wiki.factorio.com/Desynchronization (accessed 2026-11-18)
updated: 2026-11-18
---

# Deterministic Simulation & Lockstep Multiplayer

## Goal & scope

How Factorio runs a fully deterministic simulation and syncs multiplayer by inputs only — the model for
any game that wants cheap, scalable networking plus replay/desync debugging.

## Primary sources

- **Factorio Wiki "Desynchronization"** — https://wiki.factorio.com/Desynchronization (accessed 2026-11-18)
- **Factorio Friday Facts** (determinism, multithreading) (RESEARCH) — https://www.factorio.com/blog/post/fff-415 (accessed 2026-11-18)

## Key decisions / trade-offs

- **Deterministic lockstep**: send only inputs, not state — bandwidth stays tiny and scales with factory
  size, at the cost of *every* machine running the identical simulation and being limited by the slowest.

## Implementation notes (sourced unless labeled)

- "Factorio multiplayer code uses deterministic lockstep to synchronize clients… sending only the user
  inputs… rather than networking the state of the objects." Every client simulates **every tick identically**.
  (Factorio Wiki Desynchronization)
- A **desync** is *any* tiny divergence — "If any computer does something ever-so-slightly different, a
  desynchronization (desync) occurs." (Factorio Wiki Desynchronization)
- Desync causes are **bugs, mod/scenario bugs, or faulty hardware** — "Networking-, latency or performance
  problems do not cause desyncs." (Latency causes input lag/rubber-banding, not desyncs.)
  (Factorio Wiki Desynchronization)
- Use **fixed-point / integer math** for anything that must be deterministic across machines; avoid
  platform-float differences, unordered container iteration, and any RNG not derived from the tick. (RESEARCH)
- Deterministic **multithreading** is hard: a 2.0 desync required *four* coinciding conditions (mods +
  chunk-generation + forced generation + differing CPU core counts). Parallelism that touches shared
  state risks divergence. (FFF #415, RESEARCH)

## Anti-patterns / gotchas

- Floating-point math in shared simulation state (non-portable across CPUs).
- Unordered iteration or wall-clock time in the sim.
- Assuming latency causes desyncs (it doesn't) — chase determinism bugs, not network tuning.

## Verify-first

Re-verify fixed-point/determinism specifics against Factorio's FFF posts and your own engine before
committing to a lockstep architecture; UE's default is non-deterministic, so this is a deliberate,
project-wide decision.
