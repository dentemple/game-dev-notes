---
title: Feature Prioritization & Build vs Buy
tags: [prioritization, kano, rice, ice, moscow, build-vs-buy, tech-debt, roadmap]
source: https://salivity.github.io/game-development/article/how-to-balance-tech-debt-and-features-in-game-dev (accessed 2026-11-18)
updated: 2026-11-18
---

# Feature Prioritization & Build vs Buy

> Source note — the primary game-industry sources for this topic returned HTTP 403 this session,
> so the specifics below are practitioner consensus from search results, not a fetched primary.
> Re-verify against a primary source before making load-bearing roadmap decisions.

## Frameworks (practitioner consensus)

- **Pre-launch**, RICE/ICE are weak — they need reach/impact data that does not exist yet. Prefer:
  - **Kano model** — classify must-haves vs. performance vs. delighters.
  - **Value-vs-effort (ROI) matrix** — plot value against cost.
  - **Eisenhower matrix** — weekly urgent/important triage.
  - **MoSCoW** — Must / Should / Could / Won't; the explicit "Won't" is the scope guard.

## Tech debt (practitioner consensus)

- Debt vs. features is a false binary — allocate a **portfolio** (~15-25% of capacity) to debt reduction.
- Use feature-adjacent refactoring (Boy Scout rule); keep debt in the same backlog, ranked by player-facing impact.

## Build vs buy (practitioner consensus)

- In-house builds look free due to an "accounting illusion" (payroll-absorbed costs). Reserve internal engineering for **game-specific differentiators**; buy commodity systems (auth, matchmaking, leaderboards, economy tooling).
- Evaluate with a 5-part TCO: build cost, maintenance, evolution, knowledge retention, opportunity cost.

## Verify-first

Re-verify these frameworks against a fetched primary source before relying on them; the practical solo rule that stands regardless: every feature is a cost center — ask "does this make the game visibly better?" before adding it.
