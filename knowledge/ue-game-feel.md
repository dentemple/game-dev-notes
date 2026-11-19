---
title: UE Game Feel (Coyote Time, Buffering, Hitstop)
tags: [game-feel, coyote-time, jump-buffering, hitstop, screen-shake, enhanced-input, juice]
source: https://adventuresincausality.com/unreal/unreal-enhanced-input/buffering/ (accessed 2026-11-18)
updated: 2026-11-18
---

# UE Game Feel (Coyote Time, Buffering, Hitstop)

## Model (primary)

- Input buffering and coyote time share one shape: a semantic action + timestamp + expiry, consumed exactly once when legal.
- "early press before landing → input buffer"; "late press just after leaving edge → coyote time."
- "They solve opposite timing errors and should have separate tuning variables/telemetry."
Source: https://adventuresincausality.com/unreal/unreal-enhanced-input/buffering/ (accessed 2026-11-18).

## Community timing ranges (RESEARCH — tune per game)

- Coyote time ~100-150ms after leaving ground.
- Jump buffering ~100-200ms before landing.
- Hitstop ~50-120ms on impact (light ~3-5 frames, heavy ~8-13 frames).
- Screen shake: decaying; use a trauma model (amplitude = trauma²); throttle to avoid nausea.
Source: community consensus (UEFN central, GameCodex, GamesByAI) (accessed 2026-11-18).

## Note for solo dev

These are feel-layer tunables on top of correct movement math. Implement via Enhanced Input events plus a grounded-timestamp check; keep buffering and coyote variables separate; validate server-side in multiplayer.
