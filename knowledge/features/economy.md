---
title: Economy & Trading
tags: [feature, economy, currency, sources, sinks, inflation, pricing]
source: https://raw.githubusercontent.com/omer-metin/skills-for-antigravity/refs/heads/main/skills/game-monetization/references/patterns.md (accessed 2026-11-18; from search summaries)
updated: 2026-11-18
---

# Economy & Trading

> Source note — economy specifics are from search summaries (re-verify against a fetched primary). The
> *itemization* layer is documented in ../rpg-design.md.

## Goal & scope

A game economy: currency, prices, sources and sinks, and inflation control. See ../rpg-design.md
(itemization) and ../features/factory-automation.md (production chains).

## Primary sources (RESEARCH — re-verify)

- "Game Monetization & Economy Design" patterns; "Economy Playbook" (search summaries)
- Cross-refs: ../rpg-design.md, factory-automation.md, ../market-and-consumer.md

## Key decisions / trade-offs

- **Every source needs a sink** (faucet/drain balance) — otherwise inflation.
- Keep reward scaling **linear-ish**, not exponential.
- **Anchor pricing**; avoid hidden currency conversion that leaves useless "leftover" currency.

## Implementation notes (RESEARCH)

- Track net currency flow per currency; alert on inflation thresholds.
- Sinks: repairs, consumables, taxes, prestige resets, item degradation.
- Simulate before shipping: load sources/sinks/prices, simulate player segments, detect runaway loops and
  unrecoverable poverty.

## Anti-patterns / gotchas

- Sources > Sinks (inflation devalues everything).
- Exponential reward scaling.
- Hidden conversion that produces "leftover" currency.

## Verify-first

Re-verify the economy patterns against a fetched primary before load-bearing use.

## Related

../rpg-design.md · ../features/factory-automation.md · ../market-and-consumer.md
