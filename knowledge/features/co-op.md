---
title: Co-op Play (Topology, State, Scaling)
tags: [feature, co-op, multiplayer, networking, replication, save, session, party, difficulty, host, dedicated-server, drop-in]
source: https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-dedicated-servers-in-unreal-engine (accessed 2026-11-24)
updated: 2026-11-24
---

# Co-op Play

## Goal & scope

How shipped co-op games solve network topology, authority, session/save state, shared
vs. per-player progression, player-count difficulty scaling, time control, combat
authority, NPC companions, multi-tier persistence, and co-op UX. Fits a solo UE5
action-RPG/strategy hybrid with dynamic factions, NPC parties, roguelike runs, squad
combat, and a three-tier world. Does **not** cover competitive matchmaking, anti-cheat
services, or live-service content cadence.

## Primary sources

- Epic, "Setting Up Dedicated Servers in Unreal Engine" — listen vs. dedicated,
  client-server authority, host advantage:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-dedicated-servers-in-unreal-engine (accessed 2026-11-24)
- StraySpark, "UE5 Multiplayer 2026: Replication & EOS" — server-authoritative UE5,
  CMC prediction, no lag compensation out of the box, listen-for-co-op guidance:
  https://www.strayspark.studio/blog/ue5-multiplayer-2026-replication-eos (accessed 2026-11-24)
- Valve, "The AI Systems of Left 4 Dead" (AIIDE 2009 paper mirror) — AI Director
  intensity and pacing:
  https://archive.org/stream/valve-publications/2009/ai_systems_of_l4d_mike_booth_djvu.txt (accessed 2026-11-24)
- Terraria wiki, Character and Multiplayer — separate character/world files,
  host-owned world save, server kick/ban:
  https://terraria.wiki.gg/wiki/Character and https://terraria.wiki.gg/wiki/Multiplayer (accessed 2026-11-24)
- BG3 wiki, Multiplayer — four players, host-owned save, companion assignment,
  absent-player storage:
  https://bg3.wiki/wiki/Multiplayer (accessed 2026-11-24)
- Remnant 2 wiki, Multiplayer — per-player enemy health/damage scaling:
  https://remnant2.wiki.gg/index.php?title=Multiplayer (accessed 2026-11-24)
- Deep Rock Galactic wiki, Multiplayer — peer-to-peer host, no dedicated servers,
  late-join drop pod:
  https://deeprockgalactic.wiki.gg/wiki/Multiplayer (accessed 2026-11-24)
- Monster Hunter World wiki, Multiplayer — monster HP tiers by player count:
  https://monsterhunterworld.wiki.fextralife.com/Multiplayer (accessed 2026-11-24)
- Don't Starve Together server docs — cluster/shard model, one server process per level:
  https://docs.linuxgsm.com/game-servers/dont-starve-together (accessed 2026-11-24)
- Steam, Wolcen launch announcement — database failure, restore/merge, character/progress loss:
  https://store.steampowered.com/news/posts/?feed=steam_community_announcements&appids=424370&enddate=1582732521 (accessed 2026-11-24)

## Models

| Model | Sync | Save ownership | Drop-in | Main cost/risk |
|---|---|---|---|---|
| Listen server (host = authority) | Server-authoritative + CMC client prediction | Host device: world; per-player character saves | Host-required; optional join-in-progress | Cheapest; host advantage; host quit ends session |
| Dedicated server | Server-authoritative | Server files; world outlives players | Easy | Ops, backend, anti-cheat cost |
| P2P + relay (EOS) | Host peer | Host device | Host-required | NAT handled; higher latency; host quit |
| Deterministic lockstep (strategic/RTS) | Identical simulations, commands only | Shared | Replay-style | Runs at slowest player; desync tail |
| Turn-based co-op | Turn ownership, no prediction | Host/server | Session-based | Slower pacing; easiest state sync |

Epic's guidance: a listen server is "often acceptable for casual multiplayer and
cooperative gaming"; headless dedicated servers are "ideal for large-scale or competitive
games." The host plays in the true state, so listen-server co-op has host advantage.
(https://dev.epicgames.com/documentation/en-us/unreal-engine/setting-up-dedicated-servers-in-unreal-engine, accessed 2026-11-24)

## What shipped games do

| Game | Model | Shared vs. per-player | Scaling / notable rule |
|---|---|---|---|
| Deep Rock Galactic | Peer-to-peer, player-hosted; no dedicated servers | Shared mission; per-player class/gear | Late join via drop pod; joining disabled near mission start; host quit can collapse the operation |
| Vermintide 2 | Host-based co-op (community-confirmed) | Shared mission; per-player gear | Four players; AI director pacing; no host migration |
| Risk of Rain 2 | Host-based co-op (community-confirmed) | Shared run; per-player items/builds | Difficulty rises with player count and time; no host migration |
| Remnant 2 | Host world | Shared world; per-player loot | Enemy health/damage rises per additional player; world scales mainly by host power |
| Monster Hunter World | Session/quest host | Shared quest; per-player rewards | Monster HP ~150% for 2, ~220–260% for 3+; reverts when group shrinks (Iceborne) |
| Baldur's Gate 3 | Host-owned campaign | Shared quest/world; per-player characters/companions | Up to four; save creator must host; host is sole saver/loader; absent characters stored and auto-return |
| Divinity: Original Sin 2 | Host/session | Shared campaign; per-player characters | Up to four; turn-based combat; Competitive Questing |
| Terraria | Host & Play or server | Shared world; per-player character/inventory | Characters and worlds are separate files; characters carry inventory across worlds |
| Don't Starve Together | Cluster with master + slave shards | Shared world; per-player characters | Each level is its own server process; caves/surface shards |
| Warframe | Per-mission P2P host elected by connection quality | Shared mission; per-player loadout | Host migration transfers mission state; DE cites infrastructure cost for dedicated mission servers |
| Left 4 Dead 2 | Dedicated/listen servers | Shared campaign; per-player health/inventory | AI Director paces from the max intensity of all survivors; 75% of mobs spawn behind |
| Crusader Kings III | Server-authoritative grand strategy | Shared world; per-player realm | Real-time with pause; cross-platform desync fixes still shipping in 2026 |

## State ownership and save

The cleanest split for a persistent-world co-op game is **world state on the host/server,
character state per player**. Terraria stores characters and worlds as separate files;
characters are not locked to worlds and carry their inventory into any world. In Host &
Play the world "is saved to and runs entirely from" the host's device, and a server can
save the map and kick/ban players without any particular player staying connected.
(https://terraria.wiki.gg/wiki/Character, https://terraria.wiki.gg/wiki/Multiplayer, accessed 2026-11-24)

Baldur's Gate 3 concentrates campaign ownership on the host: the creator of a multiplayer
save must host later sessions, and the host is the sole player responsible for saving and
loading, though any player can trigger autosaves. The host also assigns characters and
companions to players; absent players' characters can be stored and auto-return on rejoin.
(https://bg3.wiki/wiki/Multiplayer, accessed 2026-11-24)

Implication: decide early which state is **world-owned** (factions, territory, towns,
caves, armies, build queues, discovered map, run seed) and which is **player-owned**
(inventory, equipment, XP, character build, personal quest flags). Ambiguous ownership
is where co-op save bugs live.

## Difficulty scaling by player count

Three shipped patterns:

1. **Director pacing** — Left 4 Dead's AI Director computes each survivor's intensity and
   drives the team from the maximum, pacing Build Up → Sustain Peak (3–5 s) → Peak Fade →
   Relax (30–45 s), with 75% of mobs spawning behind the team.
   (https://archive.org/stream/valve-publications/2009/ai_systems_of_l4d_mike_booth_djvu.txt, accessed 2026-11-24)
2. **Per-player stat multipliers** — Remnant 2 grants all enemies bonus health and damage
   per additional player (2p: 110% damage, 125% standard, 150% elite, 185% boss; 3p:
   120%, 150%, 200%, 270%); world scaling is keyed mainly to the host's power level.
   (https://remnant2.wiki.gg/index.php?title=Multiplayer, accessed 2026-11-24)
3. **Tiered HP scaling** — Monster Hunter World raises monster HP to ~150% for two players
   and ~220–260% for three or more, applied when a second player joins and reduced when
   the group drops back to one (Iceborne).
   (https://monsterhunterworld.wiki.fextralife.com/Multiplayer, accessed 2026-11-24)

For an action game, stat multipliers alone produce HP sponges. Prefer a **threat budget**
that scales composition, attack tokens, reinforcements, elite count, and rewards, with
stat scaling as a secondary knob.

## Time control

Turn-based co-op (Baldur's Gate 3, Divinity: Original Sin 2, Solasta) avoids prediction
and desync entirely: players own turns, and the game can pause between them. Real-time
action co-op (Deep Rock, Vermintide, Left 4 Dead) requires a single authority for combat
and AI, and cannot freely pause for one player. Deterministic lockstep appeals for a
shared strategy simulation but "the game progresses as slowly as the player with the
highest latency," and a mature grand-strategy game can still be fixing desyncs years
later (Crusader Kings III, April 2026 cross-platform desync fix).
(https://en.wikipedia.org/wiki/Lockstep_protocol, https://changelog.gg/games/crusader-kings-iii-1158310/updates/2026-04-23-update-1-19-0-4-32dc, accessed 2026-11-24)

Implication: keep combat real-time; make the strategic layer **server-authoritative or
turn-resolved**, not lockstep. If the strategy layer pauses, decide who can pause:
host-only, vote, or no pause during co-op.

## Combat authority

UE5 is server-authoritative; the Character Movement Component has built-in client
prediction and server correction. UE5 does **not** provide lag compensation out of the
box, so hitscan/rewind must be implemented deliberately. (https://www.strayspark.studio/blog/ue5-multiplayer-2026-replication-eos, accessed 2026-11-24)

For this project: the host/server owns health, damage, ability activation, cooldowns, AI
tokens, and hit validation. Clients predict movement and presentation, not combat
outcomes. Ranged/aim abilities need server-side line traces and, if desired, a rewind
buffer. Friendly fire, revive/downed states, and aggro sharing are design rules layered on
that authority, not client-side effects.

## NPC companions and party state

Baldur's Gate 3 is the clearest shipped model: the host assigns characters and companions
to players; absent players' characters can be stored and auto-return on rejoin. That solves
the "human player leaves, companion takes over" problem without duplicating party state.
(https://bg3.wiki/wiki/Multiplayer, accessed 2026-11-24)

Implication: make party membership **session-owned** (who controls which character) and
party data **world/character-owned** (stats, equipment, approval). NPC companions can fill
empty player slots, but the host must own their AI and commands during co-op.

## Multi-tier worlds and persistence

Don't Starve Together runs each level (surface, caves) as its own server process: a cluster
contains shards, each shard is a map/level run as an individual game server instance, with
a master shard and connected slave shards.
(https://docs.linuxgsm.com/game-servers/dont-starve-together, accessed 2026-11-24)

That is the closest shipped analogy to a Landscape / Local Map / World Map split: either
run each tier as a separate server/simulation process, or keep one authoritative server
that owns all tiers and streams the active view to each client. The second is simpler for
a solo team; the first isolates crashes and load.

## Failure modes

- **Shared backend drops under load** — Wolcen's launch database failure forced a
  restore/merge that wiped characters, stashes, and endgame progression.
  (https://store.steampowered.com/news/posts/?feed=steam_community_announcements&appids=424370&enddate=1582732521, accessed 2026-11-24)
- **Promising co-op late** — No Man's Sky's pre-launch "not really a multiplayer game"
  framing still produced a launch controversy when players expected to meet.
  (https://gamerant.com/no-mans-sky-no-multiplayer-explanation-826/, accessed 2026-11-24)
- **Host departure** — Deep Rock Galactic's host leaving can terminate the operation and
  lose collected mission progress; the cheap mitigation is host-side autosave and short
  runs. (https://roguecorewiki.com/article/preventing-host-dependent-mission-collapse-on-hoxxes-iv/, accessed 2026-11-24)
- **Desync in shared strategy** — Crusader Kings III still fixed a cross-platform desync
  in 2026; a shared strategic simulation needs one authority or rigorous determinism.
  (https://changelog.gg/games/crusader-kings-iii-1158310/updates/2026-04-23-update-1-19-0-4-32dc, accessed 2026-11-24)

## Case study

See `stardew-valley-co-op.md` for the shared-world/per-player-character model and the retrofit warning.

## Recommendation for this project (ANALYSIS)

For a solo UE5 action-RPG/strategy hybrid with dynamic factions, NPC parties, and
roguelike runs:

1. **Start with a host-authoritative listen server**, 1–4 players, server-authoritative
   combat and AI, CMC client prediction for movement. Epic explicitly calls listen servers
   acceptable for co-op; DRG, Vermintide, and Risk of Rain 2 shipped successful co-op
   without dedicated servers.
2. **Host owns one shared world save; each player owns a character save.** Put factions,
   territory, towns, caves, armies, build queues, run seed, and discovered map in the world
   save; put inventory, equipment, XP, and character build in the character save. This is
   the Terraria split and the BG3 host-save model.
3. **Defer host migration.** It is expensive to do well; DRG/Vermintide/RoR2/BG3 shipped
   without it. Mitigate with host autosave, short runs, and a clear "host left" flow.
4. **Decide drop-in deliberately.** DRG supports late join via drop pod; BG3 requires the
   save creator to host. A host-required lobby is cheaper; join-in-progress is a
   separate feature, not a free side effect.
5. **Keep combat real-time; make the strategic layer server-authoritative or turn-resolved.**
   Do not use deterministic lockstep for the whole game unless the entire simulation is
   bit-deterministic. A single authoritative host is the cheaper path for a solo team.
6. **Scale difficulty with a threat budget, not only HP.** Use player count, NPC party
   size/composition, run modifiers, and faction state to drive enemy composition, tokens,
   reinforcements, and rewards. Remnant 2 and MHW show per-player stat scaling; L4D shows
   director pacing.
7. **Treat party membership as session state.** Host assigns characters/companions;
   absent players' characters can be stored and auto-return. NPC companions can fill
   empty slots; the host owns their AI.
8. **Run each tier as a server-side simulation, not a client-side one.** Either one
   authoritative server owns all tiers or each tier is a separate shard/process; clients
   only render the active tier. Don't let two clients simulate the same faction state.

## Two-player spike

Host + client over LAN against a listen server:

1. CMC client prediction for movement.
2. One replicated damage event with server-authoritative health.
3. Host-owned world save + separate per-player character save that round-trips.
4. One difficulty multiplier keyed to player count that applies on join and reverts on leave.
5. One faction tick that runs only on the host and replicates a summary to the client.
6. One player in the Landscape and one on the World Map at the same time.

Success criteria: movement is responsive, combat state stays authoritative, save/load
survives a host restart, party-size scaling adjusts on join/leave, and the client sees the
host's faction state without simulating it.

## Verify-first

- Re-check Epic's dedicated-server/listen-server guidance and CMC prediction against the
  installed UE 5.8 docs before coding.
- Re-check BG3/Terraria/Remnant 2/MHW behavior against current patches; community wikis
  are patch-sensitive.
- Decide drop-in, host migration, and pause policy explicitly; the evidence supports
  "host-owned, no migration" but not a universal rule.
- Profile the two-player spike on target hardware before committing to 4 players.

## Related

`../replication.md` · `deterministic-simulation.md` · `save-system.md` · `../game-architecture.md` · `../ue-performance.md`
