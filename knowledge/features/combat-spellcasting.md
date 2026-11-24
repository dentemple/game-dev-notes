---
title: Spellcasting & Spell Combat (Mass Effect, Wrath, Genshin, Skyrim, WoW, GW)
tags: [feature, combat, spellcasting, abilities, primer, detonator, elemental, reactions, cooldown, mana, ultimate, crowd-control]
source: https://staging.vulkk.com/2017/10/09/shadow-of-war-skill-tree-full-overview/ (accessed 2026-11-19)
updated: 2026-11-19
---

# Spellcasting & Spell Combat (Mass Effect, Wrath, Genshin, Skyrim, WoW, GW)

## Goal & scope

A data-driven spell/ability layer for a single-player third-person action game: casting types and delivery, resource models, cooldowns, primer/detonator reactions, elemental auras, crowd-control discipline, and ultimate states. Does **not** cover tab-target MMO rotations, party-swap gacha economies, or live-service content cadence.

## Primary sources

- Shadow of War Wrath/Might/Focus/Elf-shot (Vulkk):
  https://staging.vulkk.com/2017/10/09/shadow-of-war-skill-tree-full-overview/ (accessed 2026-11-19)
- Shadow of Mordor Wraith ability gates (Gosu Noob):
  https://www.gosunoob.com/shadow-of-mordor/ranger-wraith-abilities-list/ (accessed 2026-11-19)
- Official Shadow of Mordor manual (controls/readability):
  https://dlassets-ssl.xboxlive.com/public/content/ebe0c66c-a6fe-4e0d-88af-552ff19dbb1e/GameManual/29a5fd8e-4f27-4b6c-904e-5efd1f0a04cd/en-ZA/index.html (accessed 2026-11-19)
- Mass Effect power combos (TweakTown; primer/detonator):
  https://www.tweaktown.com/news/56417/closer-look-mass-effect-andromedas-power-combos/index.html (accessed 2026-11-19)
- Genshin design pillar (Wccftech):
  https://wccftech.com/talking-with-mihoyo-about-genshin-impact-and-how-its-more-than-some-clone/ (accessed 2026-11-19)
- WoW crowd-control diminishing returns (Maxroll):
  https://maxroll.gg/wow/resources/crowd-control-diminishing-returns (accessed 2026-11-19)
- Reported from blocked wikis (medium confidence; re-fetch before relying on exact values): Mass Effect fandom combo matrix; Genshin fandom/HoYoWiki reaction and gauge/ICD pages; UESP/Creation Kit MagicEffect and Magic Overview; Wowpedia cooldown/ability pages; GW2 wiki Combo; GW1 wiki Spell.

## Ability taxonomy

| Axis | Options |
|---|---|
| Delivery | Instant hit, projectile, beam/channel, cone, ground-target AoE, self-buff, target-buff, construct, summon, chain, homing |
| Casting | Fire-and-forget, concentration (hold), channel, constant effect (passive), charge |
| Throttle | Cooldown, mana/magicka, energy, banked meter, ammo, ultimate meter |
| Reaction role | Primer, detonator, both (rare), neutral |

## What each system contributes

### Mass Effect — primer/detonator

- Prime skills apply a lasting status; detonators consume it into a combo effect.
- The combo type appears to come from the primer. The exact four-type matrix and defense affinities are **reported** from the wiki, not confirmed by the fetched article.
- Primed targets should be visually marked.
- A power should not both prime and detonate the same combo.
- Implementation: `Primer.*` and `Detonator.*` gameplay tags; a detonator ability checks for a primer tag, removes it, and applies the reaction GameplayEffect.

### Shadow of Mordor/War — Wrath and Wraith

- Wrath builds per kill; at full, Elven Rage slows time, makes melee strikes lethal, and grants unlimited executions. Smaller abilities can also spend the same meter.
- Wraith abilities are gated by the charged Hit Streak (8 hits, 5 with Blade Master): Execution, Wraith Flash, Combat Drain, Wraith Burn, plus Wraith Stun and Brutalize.
- Resource loop: banked Might (resets on damage/miss/exit combat), Focus (chains/slow-mo aim), Elf-shot ammo (restored by counters/drain), Health via drain, Wrath per kill.
- Ultimate design: build from aggression, make it a temporary transform, and offer smaller spends so it is not a one-button nuke.

### Genshin Impact — elemental reactions and skill/burst

- Reported model: an aura plus a trigger causes a reaction; amplifying reactions multiply the triggering hit; transformative reactions deal flat level/EM damage; gauge units decay; an internal cooldown (roughly 2.5 s or 3 hits) limits re-application.
- Skill is cooldown-gated and generates particles; Burst is energy-gated by those particles. The particle/team-rotation economy is gacha/live-service-specific; copy the tag/reaction structure, not the rotation economy.
- Keep the reaction matrix small. Every element added multiplies reaction content, VFX, UI, and balance surface.

### Skyrim — the data model

- Reported Creation Kit decomposition: `MagicEffect` has an Effect Archetype, Casting Type (Fire and Forget / Concentration / Constant Effect), and Delivery (Self / Aimed / Target Actor / Target Location / Contact); a `Spell` composes effects and flags magnitude/area/duration; enchantments must match casting/delivery.
- Game layer: five schools, magicka cost and regeneration, dual casting.
- This maps to GAS: MagicEffect → GameplayEffect or data row; Casting Type → activation policy; Delivery → targeting/projection; Spell → GameplayAbility with cost/cooldown.

### World of Warcraft — cooldown/CC/aura discipline

- Reported GCD: 1.5 s for most abilities, 1.0 s for energy classes; instant abilities trigger it; haste reduces it to a 1.0 s minimum.
- CC diminishing returns: categories include stuns, disorients, incapacitates, silences, disarms (PvP), and roots; displacements use separate anti-spam limits; reset about 16 s after the last application expires; PvP immunity after two applications; in PvE only stuns are affected, with a shrinking duration floor.
- Auras/buffs/debuffs carry stacks, durations, and dispel types; procs alter rotations; interrupts apply lockout and pushback.
- Do not import the addon/aura-tracking burden or GCD rotation-lock into a single-player action game.

### Guild Wars 2 — fields, finishers, stacks, breakbars

- Reported combo model: finishers (blast/leap/projectile/whirl) interact with fields (fire/water/light/smoke/etc.) to produce fixed effects; a field has a combatant cap; finisher stats scale the effect.
- Boons and conditions stack by intensity or duration.
- Breakbars replace binary stuns on bosses/elites: hard CC damages the bar instantly, soft CC drains it, and breaking opens an exposed damage window.
- This is the best model for positional spell interactions and for boss CC that is not a stun-lock.

### Guild Wars 1 — cost/interrupt discipline

- Reported: energy is paid at cast start and not refunded on failure; spells have recharge and an aftercast delay; maintained enchantments cost continuous upkeep; exhaustion stacks a penalty; interrupts cancel casting.
- Aftercast delay is a useful separate tuning knob from cooldown.

## Unified spell-definition model

Use data rows rather than a class per spell:

```
{
  id,
  element,
  delivery,            // instant | projectile | beam | cone | ground_aoe | self | target | construct | summon | chain
  casting,             // fire_and_forget | concentration | channel | constant | charge
  resource_cost,       // which resource + amount
  cooldown,
  charge_time,
  primer_tags[],       // statuses this spell applies
  detonator_tags[],    // statuses this spell consumes
  status_effects[],    // effects applied on hit
  reaction_table_id,   // which reaction matrix to consult
  icd                  // internal cooldown for element application
}
```

A spell is a `UGameplayAbility` that owns cost/cooldown and fires one or more `UGameplayEffect`s. The reaction table is `(element × status) → reaction effect`; a detonator reads the primer tag, removes it, and applies the reaction. CC is a separate table of categories and diminishing-return state per target.

## UE 5.8 implementation

- **GAS:** spells as GameplayAbilities; effects as GameplayEffects; element/status/primer/detonator/CC as GameplayTags; costs/cooldowns as attributes and cooldown effects.
- **Targeting:** soft-lock plus input-direction for target spells; ground decal for ground AoE; line trace for instant/beam; projectile actor for travelling spells; line-of-sight check before target effects.
- **Casting:** montage-driven cast/channel; ability task for channel ticks; cancel windows; charge time as a curve; dual-cast/concentration as an activation policy.
- **Reactions:** detonator ability queries the target's tags, applies the reaction effect, removes the primer, and respects the per-ability ICD.
- **CC:** a `UCCStateComponent` on each target tracks category → application count → duration multiplier → immunity; bosses use a breakbar instead of a binary stun.
- **Resources:** one banked combat meter (Might), one ammo resource (Elf-shot), and one ultimate meter (Wrath); Focus can be a fourth if slow-mo/chains need it.
- **UI:** ability bar with cooldown/charges, element aura tint on primed targets, ultimate meter, cast/channel bar.
- **Testing:** cost/cooldown correctness, ICD respected, reaction table coverage, CC DR state, ultimate build/spend, save/load of ability state.

## Implementation order

1. Spell data model + one instant projectile + one self-buff, with cost/cooldown in GAS.
2. One primer + one detonator of the same element, with the reaction table and ICD.
3. Resource loop: banked Might + ammo + ultimate meter.
4. Three elements and a small reaction matrix (e.g., fire/ice/shock).
5. CC diminishing-returns table + one boss breakbar.
6. Delivery expansion: ground-target, beam/channel, chain; elemental terrain interactions.
7. VFX/SFX/animation polish and cancel windows.

## Anti-patterns

- Ability bloat: many weak spells instead of a few upgradeable ones.
- Uninteractive CC chains; always use a DR table or breakbar.
- Resource starvation; ammo must be refillable by fighting, not waiting.
- One-button ultimate; let the same meter buy smaller options.
- Damage-type rock-paper-scissors that becomes memorization; keep two or three elements.
- Importing WoW's addon/aura-tracking UI burden into a single-player game.
- Copying Genshin's party-swap/energy-particle rotation economy into a solo character game.
- Copying GW2's full field×finisher or 25-stack boon matrix without the content budget.
- Treating reporting from blocked wikis as verified; re-fetch exact formulas before balancing.

## Verify-first

- Re-fetch the blocked wikis (Mass Effect fandom, Genshin fandom/HoYoWiki, UESP/Creation Kit, Wowpedia, GW2/GW1 wikis) before relying on exact matrices, ICD values, or cooldown formulas.
- Re-verify GAS ability/effect/tag APIs, targeting, and cooldown handling against dev.epicgames.com.
- Tune cast times, cooldowns, costs, ICD, and DR in a greybox; the numbers above are starting points, not specifications.

## Related

`combat.md` · `combat-freeflow.md` · `combat-shadow-of-mordor.md` · `gameplay-ability-system.md` · `enemy-ai.md` · `encounter-design.md` · `../game-architecture.md`
