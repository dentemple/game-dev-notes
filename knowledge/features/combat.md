---
title: Action RPG Combat Mechanics
tags: [feature, combat, melee, hitbox, iframe, stagger, poise, hitstop, combo, gas, telegraph]
source: https://raw.githubusercontent.com/omer-metin/skills-for-antigravity/refs/heads/main/skills/combat-design/references/patterns.md (accessed 2026-11-18)
updated: 2026-11-18
---

# Action RPG Combat Mechanics

## Goal & scope

Real-time ARPG melee combat: hit detection, the attack lifecycle, dodging/i-frames, combos/cancels,
hitstop feel, stagger/poise, telegraphing, and the GAS implementation. Does **not** cover turn-based
combat or deep ranged/projectile systems.

## Primary sources

- **patterns.md** — combat-design frame-data reference:
  https://raw.githubusercontent.com/omer-metin/skills-for-antigravity/refs/heads/main/skills/combat-design/references/patterns.md (accessed 2026-11-18)
- **Neo Soft** — "Predicted Melee Combat in Unreal":
  https://neosoftentertainment.com.br/en/blog/predicted-melee-combat-unreal/ (accessed 2026-11-18)
- **Epic melee** — "Melee Abilities In ARPG" (GAS):
  https://dev.epicgames.com/documentation/unreal-engine/melee-abilities-in-arpg (RESEARCH — page body TOC-only, accessed 2026-11-18)
- **combat-design SKILL** — poise/telegraphing (RESEARCH):
  https://github.com/omer-metin/skills-for-antigravity/blob/main/skills/combat-design/SKILL.md (accessed 2026-11-18)
- **DiGRA 2026** — "Combat System Design for Action Games" (RESEARCH):
  https://gameindustrylibrary.com/documents/combat-system-design-for-action-games-key-concepts-and-styles (accessed 2026-11-18)

## Key decisions / trade-offs

- **Attack-centric detection, defender-centric damage** — hitboxes vs hurtboxes (patterns.md).
- **Commitment vs. cancellability**: Souls-style *animation priority* (long recovery = deliberate risk)
  vs. DMC-style *cancellable offense* (player dictates pace). Pick one and design enemies around it;
  Sekiro is the hybrid (basic attacks cancelable, others committed). (DiGRA 2026, RESEARCH)
- **Animation-driven hit windows**: an Anim Notify opens/closes the hitbox; gameplay code owns the rules.

## Implementation notes (sourced unless labeled)

- **Hitbox/hurtbox**: "Separate attack collision (hitboxes) from damage reception (hurtboxes)";
  hitbox "Only active during attack's active frames" and "20-40% larger than the weapon mesh."
  (patterns.md)
- **Attack lifecycle**: IDLE → STARTUP → ACTIVE → RECOVERY. Sample frames: light 5/3/10, heavy
  15/5/25, special 20/8/30. "Power = Startup + Active + Recovery." (patterns.md)
- **Multi-hit prevention**: a per-attack `hitEntities` set; skip already-hit owners; clear on end.
  (patterns.md)
- **Dodge / i-frames**: Dark Souls roll ~13/30, Bloodborne ~10/26, DMC5 ~8; a typical dodge is
  startup 2 / i-frames 12 / recovery 8 / cooldown 6; reward dodging *into* attacks with extra i-frames.
  (patterns.md)
- **Cancels**: per-attack windows (normal/special/jump/dodge); hierarchy Normal < Special < Super;
  cancels happen during Active or early Recovery. (patterns.md)
- **Hitstop**: light 3-5, medium 6-10, heavy 12-18, critical 20-30 frames; asymmetric (attacker
  ~70% of target); ramp with combo count. (patterns.md; see ../ue-game-feel.md)
- **Poise/stagger** (RESEARCH): three levels — no poise (every hit interrupts), partial (after N
  hits), full/hyper armor (attacks through hit-stun). Avoid stunlock → mashing degeneracy.
  (combat-design SKILL)
- **Telegraphing** (RESEARCH): reaction time ~200-300ms (12-18 frames); layer the tell (stance →
  wind-up → VFX → audio) and exaggerate it. (combat-design SKILL)

## UE / GAS implementation (RESEARCH — Epic melee)

- `GA_MeleeBase` uses `PlayMontageAndWaitForEvent`; the weapon emits a **Gameplay Event** (tag set by an
  **Anim Notify State** in the montage) on overlap; the ability routes it through `ApplyEffectContainer`
  (tag → Gameplay Effect map). See ../gameplay-ability-system.md. (Epic melee)
- **Measured gotchas**: inputs get dropped without a buffer; a non-sweeping trace misses
  fast swings; one-round-trip latency delays the swing. Fixes: an **input buffer**, **sweeping traces**
  (previous→current position + line-of-sight), and (multiplayer) **locally predicted attacks** with the
  server still deciding damage. (Neo Soft)

## Anti-patterns / gotchas

- Relying on overlap events alone (misses fast swings / low FPS) — use sweeping traces.
- No input buffer (dropped inputs feel unresponsive).
- Instant turn-and-hit enemies, or bosses with no readable launch cue.
- Full-hitstun enemies that let the player mash (stunlock degeneracy).
- Hardcoding combat in Blueprint event graphs instead of data-driven GAS abilities.

## Verify-first

Re-verify `GA_MeleeBase` / `PlayMontageAndWaitForEvent` and Anim Notify specifics against
dev.epicgames.com before coding.

## Related

combat-botw-genshin.md, combat-windwaker.md, combat-dnd5e.md, encounter-design.md,
enemy-tactics.md — reference-game mechanics and encounter/AI design that build on this foundation.
