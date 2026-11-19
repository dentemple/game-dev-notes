---
title: Game Design Fundamentals (Fun, Feel, Loops)
tags: [design, mda, fun, game-feel, juice, core-loop, retention, aesthetics]
source: https://www.jesperjuul.net/ludologist/2004/06/29/mechanics-dynamics-aesthetics-the-whole-thing/ (accessed 2026-11-18)
updated: 2026-11-18
---

# Game Design Fundamentals (Fun, Feel, Loops)

## MDA (primary, canonical)

Mechanics → Dynamics → Aesthetics (Hunicke, LeBlanc, Zubek 2004):

- "Mechanics describes the particular components of the game, at the level of data representation and algorithms."
- "Dynamics describes the run-time behavior of the mechanics acting on player inputs and each others' outputs over time."
- "Aesthetics describes the desirable emotional responses evoked in the player, when she interacts with the game system."

The designer works mechanics → dynamics → aesthetics; the player experiences it in reverse. Tune from the player's side.
Source: https://www.jesperjuul.net/ludologist/2004/06/29/mechanics-dynamics-aesthetics-the-whole-thing/ (accessed 2026-11-18).

## Why games are fun (primary theory)

Koster's *Theory of Fun*: fun ≈ learning. "Dopamine is really interesting because it specifically enhances learning and memory." Players enjoy mastering new patterns; once a pattern is mastered, the fun is in pushing its edges, not merely repeating it.
Source: https://www.gamedeveloper.com/design/raph-koster-s-theory-of-fun-ten-years-on (accessed 2026-11-18).

## Game feel / juice (practitioner, canonical)

Juice is the feedback layer — "Developers also call the feedback part juice." The 12 techniques (Jonasson & Purho, "Juice It or Lose It", GDC Europe 2012):

1. Coyote time, 2. Jump buffering, 3. A softer jump peak, 4. Hit stop, 5. Screen shake that decays,
6. Knockback and recoil, 7. Particles and flashes, 8. Easing, 9. Squash and stretch, 10. A camera
that leads, 11. A sound for every action, 12. Feedback in the numbers.

Dose matters: don't "drown the game in effects"; an effect you don't miss probably wasn't doing much.
Source: https://gamesbyai.win/guides/game-feel-with-ai/ (accessed 2026-11-18).

## Core loops (practitioner)

Core loop = the match/level/run; metagame = everything between. Retention loops nest on cadences:

- Session: "play, earn, spend, play again … closes cleanly in a few minutes."
- Daily: a limited resource recovers on a timer.
- Weekly: events/leaderboards.
- Seasonal: resets and reopens the chase.

"The failure mode is uniformity" — distinct rewards on distinct cadences.
Source: https://heroiclabs.com/blog/metagame-design-guide/ (accessed 2026-11-18).

## Note for solo dev

These are design lenses, not code. For a premium single-player game, the session loop and a clear progression arc matter most; live-service cadences (daily/weekly) are optional, not required.
