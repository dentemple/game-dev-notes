---
title: Freeflow Combat (Arkham, Shadow of Mordor)
tags: [feature, combat, freeflow, arkham, shadow-of-mordor, nemesis, crowd-control, attack-token, hit-streak, might, traits]
source: https://episodiccontentmag.com/2016/03/11/batmanaa_chapter3/ (accessed 2026-11-19)
updated: 2026-11-19
---

# Freeflow Combat (Arkham, Shadow of Mordor)

## Goal & scope

Third-person crowd melee built on a small move set, enemy-type counterplay, a throttled attack crowd, protected versus interruptible finishers, a combo/resource economy, and persistent named rivals. Does **not** cover predator/stealth encounters, ranged-heavy combat, or vehicle combat.

## Primary sources

- Rocksteady interview (Sefton Hill, Paul Denning):
  https://episodiccontentmag.com/2016/03/11/batmanaa_chapter3/ (accessed 2026-11-19)
- Arkham freeflow design analysis:
  https://staging.gamedeveloper.com/design/batman-arkham-design-analysis-part-1- (accessed 2026-11-19)
- Arkham Knight enemy-type counters:
  https://www.ludo.guide/guide/batman-arkham-knight/gameplay-basics/basics/enemy-types (accessed 2026-11-19)
- Community ticketing/synced-animation breakdown (inference, not Rocksteady-confirmed):
  https://discussions.unity.com/t/how-does-the-batman-arkham-games-combat-system-work/509429 (accessed 2026-11-19)
- GDC 2026 "Punching Across the Room in Batman: Arkham Shadow" session page:
  https://gdcvault.com/play/1035681/Punching-Across-the-Room-in (accessed 2026-11-19)
- Michael de Plater on the Nemesis system:
  https://www.gamedeveloper.com/design/designing-i-shadow-of-mordor-i-s-nemesis-system (accessed 2026-11-19)
- GamesBeat on "anchors of gameplay":
  https://gamesbeat.com/shadow-of-mordors-nemesis-system-draws-from-burnout-football-and-an-architecture-book/ (accessed 2026-11-19)
- Shadow of War resource loop:
  https://staging.vulkk.com/2017/10/09/shadow-of-war-skill-tree-full-overview/ (accessed 2026-11-19)
- Shadow of War captain trait list (fan reference, representative):
  https://gameup24.wordpress.com/2017/10/14/shadow-of-war-all-180-possible-orc-traits-2/ (accessed 2026-11-19)
- Nemesis patent US 10,926,179 B2:
  https://patents.google.com/patent/US10926179B2/en (accessed 2026-11-19)
- Patent Section 101 analysis (not legal advice):
  https://www.legal500.com/intelligence/united-states/intellectual-property/will-101-be-a-nemesis-to-warner-brothers%27-patent (accessed 2026-11-19)

## Core loop

- **Four verbs carry the fight:** strike (builds combo), counter (grabs an attack mid-swing), dodge/evade (positioning and i-frames), and stun/vault (opens a specific enemy for damage).
- **Executions/finishers are gated by combo or a banked resource**, so the player has a spendable payoff inside the fight.
- **Simple execution, depth from the crowd.** Rocksteady's rule: if it is simple for Batman to do, it should be easy for the player to execute. "We spent a lot of time making it play great before it looked great."
- **Enemy composition supplies the difficulty:** special types demand specific answers and appear only one or two at a time.
- **Attack chaining uses synchronized animation pairs:** pick the next target, choose the closest-matching attack animation, align attacker and target, and disguise the translation/rotation fix-up as a jump or slide. Community-documented, not Rocksteady-confirmed.
- **Input buffering and readable counter prompts** are mandatory; without them the rhythm breaks.

## Crowd control: attack tokens

- Use a small ticket pool — 2–4; 2–3 is the right starting range for squad-scale fights.
- Only enemies holding a ticket may attack. Everyone else circles, repositions, and waits.
- Tickets redistribute when the holder dies, is incapacitated, or leaves range; add a timeout so a distant holder cannot stall the fight.
- Special enemy types are rationed: one or two per fight.
- Position waiting enemies with EQS around the player; give off-screen ticketed attackers a HUD indicator.
- The result is **throttled pressure**: the player is always threatened, never swarmed.

## Enemy archetypes and counters

Each archetype has one hard answer. Keep the vocabulary to roughly 4–6 types.

| Archetype | Behavior | Required answer |
|---|---|---|
| Shield | Blocks frontal attacks | Aerial/double-jump attack knocks the shield away |
| Stun baton | Punishes frontal attacks | Attack from behind via vault/evade, or a quickfire gadget |
| Knife/blade | Un-counterable yellow prompt | Dodge backward, punish the final swing |
| Medic | Revives downed enemies | Kill first; a gadget strips its charge |
| Ninja | Teleport-dodges and counters | Prioritize; use a special takedown |
| Brute | Immune to normal hits | Repeated stun, then attack; or environmental takedown |

This is the same structure as captain traits: **every challenge has a discoverable counter.**

## Combo and resources

- **Combo/hit streak is the in-fight scalar:** builds on hits, resets on damage or a miss, gates special moves, and scales damage/score.
- **Banked Might** (Shadow of War model): survives the combo, builds from damage taken, kills, and counters, and is spent on executions; it resets on taking damage, missing, or leaving combat. Easier to balance than gating every special behind a live streak.
- **Ammo** (Elf-shot equivalent): limited ranged/teleport resource, refilled by a specific action such as counters or drain.
- **Health** as the risk resource: restored by a specific action such as drain/dominate.
- **One ultimate meter** (Wrath equivalent), built per kill.
- Keep each ability to one resource cost and one clear effect. Gate upgrades as modifiers, not new abilities.

## Protection rules

Tag every combat move **Protected** or **Interruptible**:

- Protected finishers/executions: other enemies hold their attacks during the animation.
- Unsafe moves (for example ground takedowns): the nearest enemy attacks and cancels them, breaking the combo.
- The crowd AI must respect the tag. This single rule creates rhythm, risk/reward, and difficulty without stat inflation.

## Captain traits and rival memory

Captain traits fall into five buckets:

- Strengths
- Immunities
- Hates/enrages
- Weaknesses
- Mortal weaknesses

Key rule: **immunities are temporarily forgotten while the enemy is dazed.** Each immunity has a daze/counter; each mortal weakness is a discoverable instant-kill door. Difficulty comes from counterplay, not HP inflation.

A rival is a composition of:

- Stable ID, name, appearance seed
- Class/archetype and faction/tribe
- 3–6 traits
- Relationship record (killed by, killed, avenged, rival)
- One “last interaction” memory slot
- Promotion/demotion state and location
- A visible consequence (scar, title, promotion)

Monolith's scope guidance: use sparse **“anchors of gameplay”** — a few peak moments the player latches onto — rather than authoring every beat. Personality comes from remembered interactions, not from deeper procedural backstories.

## Nemesis patent caution

US 10,926,179 B2 (Warner Bros., filed 2016, priority 2015, granted 2021) is titled “Nemesis characters, nemesis forts, social vendettas and followers in computer games.” The specification describes detecting a predefined avatar–NPC interaction, changing character parameters of a second NPC based on that detection, and outputting an indication of the change. The exact granted claim scope should be reviewed by counsel; this note is not legal advice.

A legal analysis notes the claims never faced a Section 101 rejection during prosecution, but validity remains untested in court. Treat this as legal uncertainty, not permission. Keeping memory on the same NPC the player fought (a grudge, scar, or rematch) is farther from the described cross-NPC parameter-change combination than a fully auto-promoting hierarchy tied to vendettas and forts. Consult an attorney before shipping a full Nemesis-like loop.

## UE 5.8 implementation

- **Abilities:** GAS or a component + gameplay-tag enum. Model Might/ammo/Health/ultimate as attributes; costs and cooldowns as GameplayEffects; parry windows, i-frames, and status effects as GameplayTags. Keep one damage entry point that reads attacker/defender tags.
- **Crowd AI:** Behavior Trees for decisions, EQS for spacing/approach positions, StateTree for per-enemy combat states, and a C++ ticket manager that writes attack tokens as Blackboard keys. Mass Entity is for decorative crowds only, not fought enemies.
- **Animation:** Motion Matching for locomotion; Motion Warping to align strikes and finishers; montage hit reactions selected by direction/strength; root motion only inside protected windows. Keep the CMC authoritative.
- **Input:** Enhanced Input with input buffering and counter/attack indicators; reject inputs faster than the intended rhythm if anti-mashing matters.
- **Traits:** a data table of `FTraitDef { GameplayTag, category, counter-tag }`; a `Status.Dazed` tag suppresses `Trait.Immunity.*` in the damage pipeline.
- **Rivals:** stable IDs in the canonical `UGameInstanceSubsystem` state; delta-saved with schema versioning; no actor-owned persistent state.
- **Testing:** token logic (never more than N simultaneous attacks), combo/counter state transitions, no damage during protected frames, every archetype’s counter is reachable, and rival round-trip save/load.

## Anti-patterns

- Letting every enemy attack at once.
- Over-generous counter windows that turn the fight into mashing.
- Too many special enemy types in one encounter.
- Ambiguous protected/unsafe moves; the player cannot learn the rule.
- Token starvation from a distant or stuck token holder.
- Difficulty by HP inflation; it breaks the counterplay model.
- Procedural rivals with names and stats but no memory; they feel impersonal (the AC Odyssey mercenary critique).
- Full auto-promoting cross-NPC vendetta systems without legal review.
- Root motion fighting the CMC outside protected windows.

## Verify-first

- Re-verify the patent’s granted claim scope with counsel before designing a full Nemesis loop.
- Re-verify GAS, Behavior Tree, StateTree, EQS, Motion Warping, and Mass APIs against dev.epicgames.com before coding.
- Tune ticket count, combo thresholds, counter windows, and hitstop in a greybox; reported numbers are starting points, not specifications.
- Confirm every archetype and trait has a reachable counter before adding it to the content pool.

## Related

`combat.md` · `enemy-ai.md` · `enemy-tactics.md` · `encounter-design.md` · `../game-architecture.md` · `save-system.md`
