---
title: Narrative & Storytelling (Games as a Story Medium)
tags: [narrative, story, storytelling, environmental, ludonarrative, jenkins, rpg-maker, cinematics, dialogue]
source: https://web.mit.edu/~21fms/People/henry3/games&narrative.html (accessed 2026-11-18)
updated: 2026-11-18
---

# Narrative & Storytelling (Games as a Story Medium)

## Goal & scope

How games tell stories differently from other media, and how two tool ecosystems (RPG Maker, Unreal)
produced narrative-first indie hits. Companion to features/quest-dialogue.md (dialogue systems) and
features/encounter-design.md (pacing beats).

## Primary sources

- **Jenkins, "Game Design as Narrative Architecture" (2004)** — https://web.mit.edu/~21fms/People/henry3/games&narrative.html (accessed 2026-11-18)
- **Hocking, "Ludonarrative Dissonance in BioShock" (2007)** (RESEARCH — original post dead) (accessed 2026-11-18)
- **RPG Maker / UE narrative case studies** (RESEARCH) (accessed 2026-11-18)

## The theory — four modes of environmental storytelling

Jenkins: think of designers "less as storytellers than as **narrative architects**." Four spatial modes:
- **Evocative** — "spatial stories can evoke pre-existing narrative associations" (familiar genres/tropes).
- **Enacted** — "a staging ground where narrative events are enacted" (play/witness beats).
- **Embedded** — "embed narrative information within their mise-en-scene"; "the game world becomes a kind
  of information space, a memory palace" (clues, artifacts, environmental detail the player pieces together).
- **Emergent** — "not pre-structured or pre-programmed, taking shape through the game play."

The practical upshot: **story can live in the environment and in systems, not just cutscenes.**

## Ludonarrative dissonance (RESEARCH)

Hocking's 2007 term: a **mismatch between what the game's mechanics reward and what its story says**
(BioShock's systems reward self-interested choice while its narrative praises altruism/free will; linear
funneling undercuts the theme of agency). The lesson: **make mechanics and message agree**, or the
dissonance will read as a design flaw (or, deliberately, as the point).

## Two ecosystems, one lesson (RESEARCH)

- **RPG Maker** → *story-first, mechanics-minimal*: To the Moon (no combat), OMORI (custom art hiding the
  engine), OneShot (meta/fourth-wall), LISA (agonizing permanent choices). The tool's low-fi ceiling
  *forced* the story to carry the game; custom assets were the differentiator ("when you can't impress
  with graphics, impress with story").
- **Unreal Engine** → *environmental/cinematic*: The Vanishing of Ethan Carter (photogrammetry +
  environmental clues, no combat), Hellblade: Senua's Sacrifice (emotional, performance-driven), Observer
  (atmospheric world-building). UE's Blueprints, **Sequencer** cinematics, and **MetaHuman** are the levers.

Both succeed on the same principle: **embedded narrative + show-don't-tell** — let the world and the data
tell the story, and keep mechanics serving the theme.

## Implementation for a solo UE dev (ANALYSIS)

1. **Dialogue/quests as data** — a DataTable-driven dialogue/quest system (see features/quest-dialogue.md),
   gated by flags, so narrative content is authorable and moddable.
2. **Environmental storytelling** — place "memory palace" clues in the level (notes, objects, lighting,
   audio) rather than explaining via text (Jenkins' embedded mode).
3. **Cinematics via Sequencer** — use UE's Sequencer for key beats; keep them few and earned.
4. **Pacing via the 5-room structure** — Entrance → Puzzle/RP → Setback → Climax → Reward (see
   features/encounter-design.md) is a *narrative* beat structure as much as an encounter one.
5. **Respect player agency** — emergent narrative (player-authored moments) is a story too; don't over-script.

## Anti-patterns / gotchas

- Cutscene-heavy exposition when the environment could show it (violates show-don't-tell).
- Mechanics that contradict the story (ludonarrative dissonance).
- "Walking simulator" with no player agency or payoff — story needs *some* interaction/stakes.
- Default/RTP assets (RPG Maker lesson: a unique visual identity is the differentiator).

## Verify-first

Re-verify Jenkins' four modes against the paper above and Hocking's term against a current secondary
source (the 2007 post is dead); the *patterns* (embedded narrative, show-don't-tell, agency) are robust
regardless.
