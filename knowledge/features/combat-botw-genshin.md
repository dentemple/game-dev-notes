---
title: Combat Reference — Breath of the Wild & Genshin Impact
tags: [feature, combat, botw, genshin, elemental-reactions, flurry-rush, parry, durability, stamina, slow-motion]
source: https://gamesbeat.com/the-legend-of-zelda-breath-of-the-wild-makes-chemistry-just-as-important-as-physics/ (accessed 2026-11-18)
updated: 2026-11-18
---

# Combat Reference — Breath of the Wild & Genshin Impact

## Goal & scope

The signature mechanics of two reference games (the project's stated combat inspirations), extracted and
mapped to Unreal. Companion to `combat.md` (which holds the frame-data foundation: i-frames, hitstop,
cancels). Does **not** cover full open-world systems or gacha meta-progression.

## Primary sources

- GamesBeat — "Breath of the Wild makes chemistry just as important as physics" (accessed 2026-11-18)
- India Today Gaming — "Genshin Impact Elemental Reactions Guide" (accessed 2026-11-18)
- Search summaries: IGN / ZeldaDungeon (Flurry Rush), Wikipedia / Google Play (Genshin combat)

## Key decisions / trade-offs

- **Adopt the elemental reaction matrix, not the character-swap** — Genshin's quick-swap team synergy is
  gacha-specific; the transferable core is a data-driven element × element reaction table.
- **Adopt the chemistry engine's three simple rules, not a physics simulation** — the emergence is cheap.
- **Durability and stamina are deliberate friction** — copy only if you want the tension/scavenging loop;
  both are divisive.

## Implementation notes (sourced unless labeled)

### Breath of the Wild

- **Flurry Rush** (RESEARCH): perfect dodge (side-hop vs vertical, backflip vs horizontal) → slow-motion →
  rapid counter (7 hits 1-handed, 4 two-handed, 7-10 spears); does not drain stamina.
- **Perfect Guard / Parry** (RESEARCH): shield bash just before impact → deflect + slow time (even deflects
  Guardian lasers).
- **Stamina** (RESEARCH): gates charged/spin attacks, climbing, sprinting, airborne bow slow-mo; normal
  attacks and Flurry Rush are free.
- **Weapon durability** (RESEARCH): all weapons break; thrown weapons = guaranteed crit + break; the Master
  Sword "recharges" instead of breaking.
- **Chemistry engine**: physics = movement, chemistry = state changes, governed by three rules —
  "Elements can change the state of materials." / "Elements are able to change each other's states." /
  "Materials can not influence each other's states." Tracked elements: fire, water, ice, wind, electricity.
  Emergent play: throw a metal sword in a storm to draw lightning; fire spreads on grass and creates updrafts.
  (The director: "this kind of chemistry isn't real chemistry.")

### Genshin Impact

- **Amplifying reactions**: Vaporize (Hydro+Pyro) — "double damage when Hydro comes first, but
  when Pyro is first, it only does 1.5 times"; Melt (Cryo+Pyro) "works the same way" (trigger-order-dependent).
- **Transformative reactions**: Overloaded (AoE + knockback), Superconduct (-physical defense),
  Electro-Charged (multi-hit, auras coexist), Frozen (immobilize), Swirl (spreads the element), Bloom →
  Hyperbloom/Burgeon (Dendro cores), Quicken → Aggravate/Spread, Crystallize (Geo shields).
- **Amplifying vs transformative** (RESEARCH): amplifying multiplies the triggering hit; transformative deals
  separate damage scaling off level + Elemental Mastery (ignoring crit/ATK).
- **Skills & energy** (RESEARCH): Elemental Skill (cooldown) + Elemental Burst (energy, charged by
  particles/defeats).

## UE mapping

- **Elemental reactions** → a DataTable reaction matrix: `(Element A × Element B) → reaction + Gameplay
  Effect`. Tag elements (`Element.Fire`) and statuses (`Status.Frozen`) with GameplayTags; apply reactions
  via GAS Gameplay Effects (see ../gameplay-ability-system.md and ../modding-support.md).
- **Flurry Rush / parry** → detect a perfect dodge/parry inside a tight window (see combat.md i-frame/cancel
  data), then trigger slow-motion + a counter ability.
- **Slow-motion** → UE time dilation (`SetGlobalTimeDilation` / per-actor `CustomTimeDilation`); note it is
  global and complicates multiplayer.
- **Stamina / durability** → simple attributes in a `UAttributeSet`, decremented per action/hit and breaking
  at 0 (ties to ../rpg-design.md itemization).

## Anti-patterns / gotchas

- Copying Genshin's party-of-4 quick-swap into a solo single-character game (doesn't transfer).
- Copying durability without the scavenging loop it exists to drive.
- Over-building the chemistry engine — the power is three simple rules, not a real simulation.
- Global time dilation in multiplayer (slow-motion desyncs clients).

## Verify-first

Re-verify UE time-dilation and GAS Gameplay Effect APIs against dev.epicgames.com before coding the
slow-motion and reaction systems.
