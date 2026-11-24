---
title: Stardew Valley Co-op (Case Study)
tags: [feature, co-op, stardew-valley, host, farmhand, save, shared-world, per-player, peer-to-peer, lidgren]
source: https://stardewvalleywiki.com/Multiplayer (accessed 2026-11-24)
updated: 2026-11-24
---

# Stardew Valley Co-op (Case Study)

## Case study: Stardew Valley

Stardew Valley is the closest shipped analogue to a shared-world co-op RPG with per-player
characters, and it is a useful warning about retrofitting co-op late.

**Session model.** Optional co-op for 1–8 players on PC (1.6), 1–4 on consoles (Switch 2
supports up to 8 online), with split-screen up to four on PC/consoles (two on Switch 1).
The host creates the world and owns the save; farmhands join it. The host must be online
and the farm open; farm ownership cannot be transferred without modding. No cross-platform
play except among PC versions. (Stardew Valley Wiki, "Multiplayer",
https://stardewvalleywiki.com/Multiplayer, accessed 2026-11-24)

**Netcode and authority.** ConcernedApe describes it as peer-to-peer with no central
server: "Stardew uses peer to peer multiplayer, there is no central server, so someone's
phone would have to host the game." (ConcernedApe, 25 Sep 2022, via
https://devtrackers.gg/stardewvalley/p/bd037d66-tweets-by-concernedape-on-27-sep, accessed
2026-11-24) Tom Coxon (Chucklefish) wrote the multiplayer layer; retrofitting it touched
"almost every source file" and rewrote "15,000 lines of code." (Times-Standard, 21 Jan 2018,
https://www.times-standard.com/2018/01/21/well-played-farming-with-friends-in-stardew-valley/,
accessed 2026-11-24)

The transport is Lidgren.Network over UDP (default port 24642), using ReliableOrdered
delivery and compression above 1 KB. (Decompiled IPv6 mod diff,
https://github.com/sunsst/Stardew-Valley-IPv6/commit/d6241cb9f541a973e03b37af743ffbc7208c3eda,
accessed 2026-11-24) Above that, the game uses its own `NetField` trees and delta
serialization. The host owns `GameLocation` roots, `NetWorldState`, and `FarmerTeam`; each
player owns a `NetFarmerRoot`. Clients send farmer deltas to the host, which relays them;
the dedicated-server reverse-engineering notes report that the host does **not** validate
farmer deltas from clients, while team actions use a request/authorize pattern. Joining
sends a full snapshot of the host farmer, team, and world state; farmer deltas broadcast
every 3 ticks. (JunimoServer developer docs,
https://docs.junimoserver.com/developers/advanced/client-manipulation-techniques.html,
accessed 2026-11-24)

**Save model.** Farmhands live inside the host's save (`SaveGame.farmhands`); the XML save
includes inventory, mail, modData, and quests. On disconnect, farmhand state is cloned into
world state and transient state is reset; on load it is copied back into the farmhand's
root. The same reverse-engineering notes report no inventory validation during save/load.
Offline farmhands' inventory is stored in their cabin's chest/dresser, and the host can
manage it. (JunimoServer docs, accessed 2026-11-24; Stardew Valley Wiki, accessed 2026-11-24)

**Shared vs. individual state.**

| Shared | Individual |
|---|---|
| Farmland, buildings, festivals | Energy, Skills/XP, inventory, tools |
| Mine progress, museum collection | NPC relationships, mailbox, spouse porch |
| Bundle/Joja completion, beach bridge | Recipes, Stardrops, most quest progress |
| Money (optional), daily-luck average for calculations | Daily luck roll, combat/foraging/farming XP to the actor |

Quest difficulty is based on the highest-level player. NPCs can be married by only one
player at a time; players can marry each other with a Wedding Ring. (Stardew Valley Wiki,
"Multiplayer", accessed 2026-11-24)

**Economy and time.** Money is shared or separate, switchable through the Town Ledger in
the Mayor's Manor (switching splits existing money evenly). Profit margin (25/50/75/100%)
is chosen at world creation and reduces most sell prices and some seed prices to offset
extra players; it cannot be changed later without save editing. Time does not pause in
menus, dialogue, shops, or cutscenes; it pauses at festivals, day-end profession selection,
the host's `/pause`, and 2 a.m. cutscene/menu states. Split-screen pauses if all players are
in a menu/cutscene. (Stardew Valley Wiki, "Multiplayer", accessed 2026-11-24)

**Combat scaling.** No reliable source was found that Stardew scales enemy health, damage,
or spawn rate with player count; the documented co-op difficulty lever is profit margin,
and quest difficulty uses the highest-level player. Treat claims that Stardew scales
monsters per player as unverified. (Stardew Valley Wiki, accessed 2026-11-24; search result
contamination traced to a different game's developer post.)

**Lessons for this project.**

- One cabin per player is a tangible slot; the host can add or remove slots, and offline
  inventory is preserved. A player camp/house or party slot can serve the same role.
- Host-owned world + per-player character state is the clean split; Stardew embeds farmhand
  records in the host save rather than using separate character files.
- Shared world progress (mines, museum, bundles) plus individual skills/inventory/relationships
  avoids duplicating progress while preserving personal progression.
- Profit margin is an economy-level co-op balance knob; a party-size economy multiplier is
  cheaper than retuning every price and drop.
- Collaborative sleep/festival decisions are simple but can create friction; a host-decides
  or vote rule is a design choice.
- Host dependence is the price of peer-to-peer: no host migration, no offline farmhands, and
  no farmhand access without the host.
- Retrofitting co-op cost 15,000 rewritten lines; building it from the start (as this
  project plans) is materially cheaper.

## Related

`co-op.md` · `save-system.md` · `../replication.md`
