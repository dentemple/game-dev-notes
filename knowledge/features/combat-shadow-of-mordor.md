---
title: Shadow of Mordor Combat (Melee & Ranged)
tags: [feature, combat, shadow-of-mordor, shadow-of-war, melee, ranged, hit-streak, might, elf-shot, focus, execution, wraith]
source: https://dlassets-ssl.xboxlive.com/public/content/ebe0c66c-a6fe-4e0d-88af-552ff19dbb1e/GameManual/29a5fd8e-4f27-4b6c-904e-5efd1f0a04cd/en-ZA/index.html (accessed 2026-11-19)
updated: 2026-11-19
---

# Shadow of Mordor Combat (Melee & Ranged)

## Goal & scope

The player-character combat layer of *Middle-earth: Shadow of Mordor*, with *Shadow of War* additions where they change how combat is executed: melee move set, crowd targeting, hit-streak and Might economy, Wraith abilities, enemy archetypes and counters, bow/aim mode, Focus slow-motion, and Elf-shot. Does **not** cover the Nemesis hierarchy, rival memory, promotions, fortresses, or sieges.

## Primary sources

- Official game manual (controls and prompt rules):
  https://dlassets-ssl.xboxlive.com/public/content/ebe0c66c-a6fe-4e0d-88af-552ff19dbb1e/GameManual/29a5fd8e-4f27-4b6c-904e-5efd1f0a04cd/en-ZA/index.html (accessed 2026-11-19)
- Ranger/Wraith ability list with gates and thresholds:
  https://www.gosunoob.com/shadow-of-mordor/ranger-wraith-abilities-list/ (accessed 2026-11-19)
- Enemy archetypes and counters:
  https://www.gamepressure.com/shadowofmordor/enemy-types/z169aa (accessed 2026-11-19)
- Shadow of War resource loop (Might/Focus/Elf-shot/Wrath):
  https://staging.vulkk.com/2017/10/09/shadow-of-war-skill-tree-full-overview/ (accessed 2026-11-19)
- Ranged combat and Focus slow-motion:
  https://www.gamepressure.com/middle-earth-shadow-of-war/ranged-combat/zaa2eb (accessed 2026-11-19)
- Execution behavior:
  https://www.ludo.guide/guide/shadow-of-mordor/characters-builds/talions-abilities-and-upgrades/combat-abilities (accessed 2026-11-19)
- Captain combat traits and the daze rule:
  https://gameup24.wordpress.com/2017/10/14/shadow-of-war-all-180-possible-orc-traits-2/ (accessed 2026-11-19)

## Melee move set

| Input / move | Purpose | Rule |
|---|---|---|
| Attack | Builds the Hit Streak | Chain hits; the combo builder |
| Counter | Answers an incoming attack | Press on the prompt; press twice when multiple enemies attack at once |
| Stun → Flurry | Safe combo building | Stun, then repeated attacks build the streak |
| Dodge | Escapes un-counterable attacks | A red icon means dodge; that attack cannot be countered |
| Execution | Crowd thinning / finisher | Ground execution on downed enemies; charged-streak execution otherwise |
| Drain | Sustain | Restores Elf-shot and terrifies nearby enemies |
| Brutalize | Stealth-to-combat bridge | Stealth finisher that builds the Hit Streak and terrifies |
| Ranged mode | Bow / ranged abilities | Hold to aim; hold to charge a stronger shot |

The move set is deliberately small; depth comes from enemy composition and the streak/resource gates.

## Resource economy

- **Hit Streak** — the live risk meter. Every 8 consecutive hits charges it (5 with Blade Master). Taking damage or missing resets it. A charged streak unlocks Execution, Wraith Flash, Wraith Burn, Combat Drain, and Fire Arrow.
- **Might** — the banked meter. Builds from damage taken, kills, and counters; "fully resets after you take damage, miss an attack, or exit combat"; full Might buys Execution/Elven Light/Mighty Shot/Consume.
- **Focus** — consumed by slow-motion aiming and chain abilities.
- **Elf-shot** — the ammo resource. Restored by well-timed counters (1 per counter) and by Drain; spent by Shadow Strike and ranged abilities.
- **Health** — recovered by Drain/dominate.
- **Wrath** — builds per kill into an ultimate state (Elven Rage).

The shape: one live meter, one banked meter, one positional ammo resource, one drain resource. The player is rewarded for engaging, not for waiting.

## Crowd control and targeting

- Use an attack-token manager: only 2–3 enemies may attack at once; everyone else circles, repositions, and waits. Redistribute tokens on death/incapacitation/range exit, with a timeout.
- The **double counter** exists because simultaneous attacks are a designed occurrence; allow a timed double-press to answer two attackers.
- Vault Stun and Flurry are spacing/combo tools; Brutalize and Wraith Flash are “get off me” tools that also feed the streak.
- Target selection: nearest plus input-direction scoring; avoid repeating the same target when there is no directional input.
- Use Motion Warping or synced attack animations to align strikes and executions; keep the CMC authoritative and use root motion only inside finishers.
- Off-screen attackers get indicators driven by the token holder.

## Enemy archetypes

| Archetype | Behavior | Required answer |
|---|---|---|
| Archer | Ranged pressure from vantage points | Close distance, shoot, or stealth |
| Defender | Shield blocks frontal attacks | Vault over and attack from behind |
| Hunter | Pike reach; punishes counters | Rely on dodging |
| Berserker | Counters standard attacks | Stun first, then attack |
| Captain | Stronger, with combat strengths and weaknesses | Learn the weakness; do not fight several at once |

Captain combat traits are categorical: immunities, hates/enrages, weaknesses, and mortal weaknesses. **Immunities are temporarily forgotten while the enemy is dazed.** Combat Master and Vault Breaker block executions/vaults (reported). Difficulty comes from counterplay, not HP.

## Ranged combat

- **Aim mode** activates slow motion until the Focus bar depletes. Focus is the ranged stamina and is shared with chain abilities.
- **Elf-shot** is limited; restock from world pickups, counters, and Drain. Every shot and ranged ability spends it.
- **Hold to charge** for a stronger shot.
- **Shadow Strike** — aim at a target and attack to teleport-kill; a counter variant teleports and stuns; spends Elf-shot. In UE, validate the target with a line trace, then play the teleport/attack.
- **Mighty Shot** — spends full Might for an explosive arrow; fire/freeze/poison variants are reported.
- **Chain of Shadows** — each additional target consumes Focus.
- **Freeze Pin** — shoot the foot to pin (reported).
- **Quick Throw** — a dagger throw that stuns.
- Projectile vs hitscan, headshot multipliers, and damage falloff are engine choices; no reliable published numbers were found.

## Ability classification and mode switching

- Melee: attack chain, counter, stun/flurry, vault stun, execution, ground execution, Wraith Flash, Wraith Burn, Combat Drain, Brutalize.
- Ranged: normal/charged bow shots, Shadow Strike, Mighty Shot, Fire/Poison arrows, Freeze Pin, Quick Throw.
- Hybrid: entering aim mode switches to ranged; Shadow Strike bridges ranged back into melee; stealth is a third posture.

## UE 5.8 implementation

- **Abilities:** GAS, or a component plus a tag enum. Each move is an ability with a cost/tag: Counter is a tagged parry-window ability; Execution is gated on the charged-streak tag; Combat Drain applies heal + Elf-shot restore; Shadow Strike validates a ranged target, teleports, and pays Elf-shot.
- **Damage:** one pipeline reading attacker/defender gameplay tags. `Status.Dazed` suppresses `Trait.Immunity.*`; i-frames are a status tag during dodge.
- **Melee hit detection:** sweeping traces or hitboxes fired from the montage's attack window; multi-hit prevention per attack; short hitstop on counters/executions.
- **Ranged:** line trace for target validity and Shadow Strike; projectile for arrows; an aim camera with time dilation; reticle and aim assist; Elf-shot/Focus as attributes with costs.
- **Enemy AI:** Behavior Trees for decisions, EQS for spacing, StateTree for combat states, and a C++ token manager. Archers need a ranged branch that keeps distance and checks line of sight.
- **Input:** Enhanced Input with buffering; double-counter as a timed double-press; aim-in/aim-out must preserve the combo and camera.
- **Testing:** combo/counter state machine, streak reset on damage, token cap, ranged hit registration, ability costs/cooldowns, and melee↔ranged transitions.

## Tuning notes

Sourced: Hit Streak charge at 8 (5 with Blade Master); Might resets on damage/miss/exit combat; counters restore 1 Elf-shot; double-counter for simultaneous attacks; specials keyed to the charged streak.

Estimates, not published: counter window ~0.3–0.5 s; hitstop ~40–80 ms on counters/executions; 2–3 attack tokens for squad-scale fights; Focus supports ~2–4 s of slow motion. Tune in a greybox.

## Implementation order

1. Greybox melee: attack, counter, dodge, stun/flurry, Hit Streak (charge at 8), execution, token manager, counter/red-dodge prompts.
2. One special enemy per counter type (berserker-stun, defender-vault).
3. Resource loop: Might + Elf-shot + Health-via-drain + Focus.
4. Ranged mode: aim slow-mo, reticle, charge shot, Elf-shot costs, Shadow Strike.
5. Captain combat traits and daze-suppresses-immunity.
6. Hitstop, hit reactions, camera polish, then difficulty by composition.

## Anti-patterns

- Over-generous counter windows that reduce combat to mashing.
- More simultaneous attackers than tokens; off-screen attacks with no indicator.
- Forgetting the red dodge-only channel; un-counterable attacks are what create depth.
- Making defenders/berserkers HP sponges instead of “vault/stun first.”
- Root motion fighting the CMC outside finishers.
- Ammo starvation: Elf-shot must always be refillable by fighting (counters/drain).
- Aim-in/aim-out dropping the combo or breaking the camera.
- Difficulty by HP inflation instead of enemy mix, timing windows, and counter-demands.

## Verify-first

- Re-verify UE GAS, Enhanced Input, Motion Warping, Behavior Tree, EQS, and StateTree APIs against dev.epicgames.com before coding.
- Tune counter windows, hitstop, token count, and Focus duration in a greybox; the estimates above are starting points.
- Re-verify ability costs (Shadow Strike’s Elf-shot cost) against a current source before balancing.

## Related

`combat.md` · `combat-freeflow.md` · `enemy-ai.md` · `enemy-tactics.md` · `encounter-design.md` · `../ue-game-feel.md`
