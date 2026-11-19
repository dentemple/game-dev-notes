---
title: Combat Reference — Wind Waker (Parry & Telegraphing)
tags: [feature, combat, windwaker, parry, counter, telegraph, lock-on, disarm, sword]
source: https://zeldawiki.wiki/wiki/Parry_Attack (accessed 2026-11-18; 403 — content from search summaries)
updated: 2026-11-18
---

# Combat Reference — Wind Waker (Parry & Telegraphing)

> Source note — the canonical wiki pages (zeldawiki.wiki, zeldadungeon.net) returned HTTP 403 this
> session; the specifics below are from consistent search summaries. Re-verify against a fetchable
> mirror before treating them as load-bearing.

## Goal & scope

Wind Waker's signature combat ideas, as a third reference alongside BotW/Genshin (see
combat-botw-genshin.md): the A-button parry/counter with layered telegraphing, lock-on targeting, the
Orca sword techniques, and weapon disarm/pickup. Companion to combat.md.

## Key decisions / trade-offs

- **One-button counter + strong telegraph = readable combat.** The parry is the model for a counter that
  is *readable* (HUD flash + glint + sound) without being a pure QTE.
- **Disarm/pickup** turns enemy gear into options — environment-as-arsenal, not a stat drop.

## Implementation notes (RESEARCH)

- **Parry Attack**: lock on → keep the shield *down* → wait for the A-button icon to flash (plus a sword
  glint and sound cue) → press A for an automatic dodge + counter.
- **Counter varies by attack type**: vertical strike → roll behind + jump-slash; horizontal → leap over +
  slash the head; special → leap up + downward stab.
- **Telegraphing**: the A-flash + chime/rumble is the canonical "readable tell" — a prompt, not a guess.
- **Sword techniques (Orca training)**: Horizontal Slash, Vertical Slash (while targeting), Thrust (target +
  forward), Spin Attack (hold/rotate B), Parry (A on telegraph), Jump Attack (A while targeting).
- **Disarm/pickup**: force an enemy to drop its weapon, pick it up and use it temporarily; disarmed enemies
  rearm or resort to punches/kicks. Weapon types: Boko Stick (flammable), Machete, Moblin Spear, Darknut
  Sword (two-handed), Stalfos Club.
- **Design caution**: praised as fluid/readable, criticized as *too lenient* (low damage, forgiving
  telegraphs, B-mashing often suffices) — telegraph clearly, but keep the counter window meaningful.

## UE mapping

- **Parry/counter** → lock-on + an enemy "wind-up" telegraph (GameplayTag `Status.Telegraphing`), then a
  tight A-press window that cancels into a dodge/counter ability (see combat.md for i-frame/cancel data).
  Surface the tell as a HUD prompt + audio cue + glint.
- **Disarm/pickup** → an interactable weapon pickup (the equipment/quick-bar pattern, see ../rpg-design.md),
  with enemies dropping their weapon object on disarm.
- **Slow-motion on the parry** → time dilation (see combat-botw-genshin.md).

## Anti-patterns / gotchas

- Reducing the counter to a pure QTE — Wind Waker's works because it is *contextual* (vertical vs
  horizontal), not just "press A on prompt."
- Forgiving telegraphs that make combat mashable.
- Hardcoding enemy telegraphs instead of a shared `Telegraphing` state/tag.

## Verify-first

Re-verify parry/disarm specifics against a fetchable Zelda Wiki mirror, and lock-on + time-dilation
against dev.epicgames.com before coding.
