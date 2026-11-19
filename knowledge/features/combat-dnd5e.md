---
title: Combat Mechanics — D&D 5e & Baldur's Gate 3 Translation
tags: [feature, combat, dnd, 5e, advantage, disadvantage, action-economy, conditions, bounded-accuracy, bg3]
source: https://bg3.wiki/w/index.php?title=High_ground_rules (accessed 2026-11-18)
updated: 2026-11-18
---

# Combat Mechanics — D&D 5e & Baldur's Gate 3 Translation

## Goal & scope

The D&D 5e combat mechanics worth borrowing for an ARPG, and how Baldur's Gate 3 translated them
(positioning, advantage, surfaces). Companion to combat.md (the frame-data foundation).

## Primary sources

- **bg3.wiki High ground** — https://bg3.wiki/w/index.php?title=High_ground_rules (accessed 2026-11-18)
- **5e SRD combat** (RESEARCH — page not extractable this session) — https://www.5esrd.com/gamemastering/combat/ (accessed 2026-11-18)
- **5e advantage discussion** (RESEARCH) — https://www.dndbeyond.com/forums/dungeons-dragons-discussion/rules-game-mechanics/3016-shooting-in-the-dark (accessed 2026-11-18)
- **Bounded accuracy** (RESEARCH) — https://forum.rpg.net/index.php?threads/tweaking-core-mechanics-of-5e.884996/ (accessed 2026-11-18)
- **Larian forums** (RESEARCH) — https://forums.larian.com/ubbthreads.php?Number=756211&ubb=showflat (accessed 2026-11-18)

## Key decisions / trade-offs

- **Bounded numbers + situational modifiers** (advantage/disadvantage, high ground) beat stat inflation —
  keeps low-level threats relevant and modifiers legible.
- **Positioning as a core mechanic** (height, cover, surfaces) — BG3's most transferable idea.

## Implementation notes (sourced unless labeled)

- **Advantage/disadvantage** (RESEARCH): roll two d20s, take higher/lower (~+4/+5 equivalent; crit 5% →
  9.75%). In a real-time ARPG this maps to a **crit/effect modifier** for "advantageous" states, not a
  second die roll. (5e SRD / dndbeyond)
- **Action economy** (RESEARCH): Action + move + Bonus Action + Reaction; simplified and legible. In
  real-time it maps to **cooldowns + energy/stamina + interrupt windows** (see combat.md cancels).
  (5e SRD)
- **Bounded accuracy** (RESEARCH): proficiency scales +2→+6; numbers stay flat so weak enemies stay
  threatening. → resist power-creep; use situational modifiers instead of big stat growth. (rpg.net)
- **Conditions** (RESEARCH): 15 statuses (blinded, prone, stunned, poisoned, …) that mostly *route into*
  advantage/disadvantage. → a **GameplayTag status system** (see ../gameplay-ability-system.md), each
  status modifying hit/effect, not a bespoke rule per status. (5e SRD)
- **BG3 high/low ground**: "+2 High Ground bonus" at 2.5 m above, "-2 Low Ground penalty" below;
  applies to all attack rolls; ranged range extends downward; Sharpshooter removes the penalty. → a
  cheap, legible **verticality modifier** on attack rolls. (bg3.wiki High ground)
- **BG3 environmental surfaces** (RESEARCH): grease/fire/electrified water, "barrelmancy" — encounters
  as *arenas* with interactable hazards. → a **surface/status-on-tile** system (fire spreads, water
  conducts) — see combat-botw-genshin.md for the elemental/reaction analogue. (Larian forums)

## Anti-patterns / gotchas

- Stat inflation instead of bounded modifiers (bounded accuracy is the point).
- One bespoke rule per condition instead of a unified status/tag system.
- "Openly exploitable" systems (BG3's height/surfaces) if you don't want cheese — decide the exploit
  ceiling deliberately. (Larian forums)

## Verify-first

Re-verify the 5e rules against the SRD and BG3 specifics against bg3.wiki before coding; in UE, model
statuses as GameplayTags + Gameplay Effects rather than hardcoded branches.
