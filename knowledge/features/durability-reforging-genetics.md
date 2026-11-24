---
title: Durability, Reforging & Item Genetics
tags: [feature, items, durability, reforging, crafting, genetics, inheritance, lineage, affixes, legacy, pokemon, gas, save]
source: https://dev.epicgames.com/documentation/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game?application_version=5.8 (accessed 2026-11-19)
updated: 2026-11-19
---

# Durability, Reforging & Item Genetics

## Goal & scope

A maintenance-and-inheritance item system: weapons/armor have two durability states, `Usable` and `Unusable`; an unusable item is reforged with a tool, a similar item, and a material; the reforge produces a child item that inherits stats, abilities, and effects from its parents and material. Covers the data model, inheritance rules, effect composition, economy, UI, and testing. Does **not** cover full Pokémon-scale genetics or permanent item destruction.

## Primary sources

- Epic — data-driven item definitions (`FItemData`, `UItemDefinition`, soft references):
  https://dev.epicgames.com/documentation/unreal-engine/coder-05-manage-item-and-data-in-an-unreal-engine-game?application_version=5.8 (accessed 2026-11-19)
- Smogon Gen 8 breeding guide (IVs, nature, ability, egg moves):
  https://www.smogon.com/ingame/guides/gen8_breeding (accessed 2026-11-19)
- D&D 3.5 *Weapons of Legacy* (legacy rituals, tiers, costs, penalties):
  https://www.dropbox.com/scl/fi/v0mpwauepcau6rv9ydmt2/D-D-3.5-Weapons-of-Legacy.pdf (accessed 2026-11-19; reported from the PDF/search summary)
- Nioh 2 Soul Match / Tempering (inheritable vs transferable effects, familiarity):
  https://nioh2.wiki.fextralife.com/Soul_Match (accessed 2026-11-19)
- Minecraft Anvil mechanics (combine, durability restore, enchantment merge, prior-work penalty):
  https://minecraft.wiki/w/Anvil_mechanics (accessed 2026-11-19)
- Path of Exile crafting (bases, mods, essences, fossils, recombinator):
  https://www.poewiki.net/wiki/Crafting (accessed 2026-11-19)
- Diablo II crafted items (magic item + gem + rune + jewel; fixed + random affixes):
  https://www.theamazonbasin.com/wiki/index.php?title=Crafted_item (accessed 2026-11-19)
- Monster Hunter weapon/armor progression (materials, trees, skills, decorations):
  https://jeu.video/en/guide/monster-hunter-rise-build-weapons-materials-progression (accessed 2026-11-19)
- Terraria reforging/prefixes:
  https://terraria.guide/guides/late-game/endgame-reforge-guide/ (accessed 2026-11-19)
- TotK weapon durability/fusion/repair:
  https://game8.co/games/Zelda-Tears-of-the-Kingdom/archives/393377 (accessed 2026-11-19)
- Durability design critique (BotW case study):
  https://dl.acm.org/doi/10.1145/3815598.3815601 (accessed 2026-11-19)
- UE deterministic random streams / seeding:
  https://benpyton.github.io/ProceduralDungeon/guides/Advanced-Features/Randomness (accessed 2026-11-19)

## Durability design

- **Two states:** `Usable` and `Unusable`. Unusable at zero durability; the item is not destroyed permanently.
- **Degradation triggers:** attacks, blocks, hits taken, special abilities; tune per item class.
- **Warnings:** UI durability bar/percentage, color change, audio/visual cue near zero.
- **Recovery:** reforge restores durability; optional field repair with a tool and material; no permanent loss.
- **Why two-state:** avoids the TotK failure mode where permanent break encourages hoarding and punitive replacement hunting. Durability should create maintenance choices, not inventory tax.
- **Costs:** scale by item tier/rarity; item-specific rather than universal; make the economy matter but avoid busywork.
- **Design test:** if the player would rather hoard the item than use it, the durability pressure is wrong.

### Lessons from other games

- **TotK:** weapons break permanently; fusion extends durability; Rock Octoroks repair one item per Blood Moon. The system drives exploration but is widely criticized as punitive. Your two-state + reforge model is more forgiving.
- **WoW / 7 Days:** repair as a gold/material sink is meaningful only if the economy is not trivialized; avoid universal repair kits and forced gear rotation.
- **Nioh 2:** familiarity gates inheritance; inheritable effects are repeatable, transferable effects are one-time; conflict pools prevent stacking. Copy the familiarity/conflict-pool discipline.
- **Minecraft:** combining two items restores durability and merges enchantments, but the prior-work penalty escalates; incompatible enchantment groups are blocked. Copy the prior-work penalty and conflict groups.
- **Monster Hunter:** materials drive weapon-tree progression; armor skills/decorations are slot-budgeted. Copy the material-tier gating and slot budgets, not the grind.
- **D&D Weapons of Legacy:** rituals unlock tiers of abilities but impose personal costs; the costs were widely disliked. Use resource maintenance, not permanent character penalties.

## Reforging

### Inputs

1. **Tool** — a required tool tag/tier. Tool quality can influence inheritance odds or success, but do not require a consumable tool for every reforge.
2. **Base item** — the unusable item being reforged; supplies the item family, base ability/effect pool, and one parent record.
3. **Similar item** — consumed; supplies transferable abilities/effects and a second parent record. "Similar" should be defined by tags: same family, compatible tier, compatible material class.
4. **Material** — consumed; supplies stat bias, element/status, mutation chance, and appearance/durability traits.

### Recipe validation

- Tool tag/tier matches.
- Base item is `Unusable` (or allow reforging usable items at a higher cost).
- Similar item passes family/tier/material compatibility.
- Material is allowed for the family.
- Costs are paid.
- Output slot/lineage cap is not exceeded.
- Optional: station requirement, quest unlock, NPC service.

### Output

- New item instance with a new stable ID.
- Durability restored (or max durability changed by material).
- Inherited traits/effects resolved from parents and material.
- Generation incremented; lineage record points to both parents and the material.
- Deterministic RNG seed stored with the instance.

## Genetics and lineage model

Use a simplified genotype/phenotype model:

- **Genotype:** hidden trait slots and inheritance weights stored on the item instance.
- **Phenotype:** the expressed stats, abilities, effects, appearance, and durability the player sees.
- **Parents:** base item and similar item each contribute a trait pool; the material contributes its own pool and a mutation catalyst.
- **Inheritance channels:**
  - Base item → family, base ability, one or two innate effects.
  - Similar item → transferable abilities/effects ("egg moves"), one-time or repeatable depending on rarity.
  - Material → stat bias, element/status, durability, appearance, mutation chance.
  - Tool → control/odds (e.g., guarantees a stat channel or preserves the base ability).
- **Probabilities:** define per channel, e.g., 50/50 for a contested trait, 60–80% for ability inheritance, 5-of-6 stat channels with a control tool, small mutation chance for a new effect.
- **Dominance:** mark traits as dominant/recessive; expressed phenotype picks the dominant trait unless a control item forces the other.
- **Mutation:** a small chance to create a new trait/effect from a material-specific pool; cap mutations per generation.
- **Generation cap:** limit reforge depth or apply diminishing returns so two items cannot be reforged forever to stack effects.

### Pokémon breeding mapping

- IVs → material-quality/stat-potential channels; inherit 3 by default, 5 with a "Destiny Knot"-style control tool.
- Nature → base item's inherent stat bias; an "Everstone"-style tool preserves it.
- Ability → item's granted ability; rare "hidden" abilities have a lower inheritance chance.
- Egg moves → transferable effects from the similar item.
- Held item → material catalyst.
- Masuda-style rare odds → rare material combinations increase mutation/rare-effect chance.
- Breeding limits → reforge/generation caps.

### D&D legacy mapping

- Least/Lesser/Greater rituals → reforge tiers requiring better tools/materials and unlocking effect slots.
- Personal costs → maintenance costs (durability, materials), not permanent character penalties.
- Reforgable from remnants → two-state durability instead of permanent destruction.
- Legacy abilities → inherited/upgraded effects that grow with reforge count.

## Effect composition and power budget

- **Effect definitions:** stat modifiers, granted abilities, procs, elemental/status effects, conditional effects.
- **Tags:** material, family, trait, element, effect category.
- **Stacking:** define stack rules per effect; cap stacks; conflict groups (like Minecraft's incompatible enchantments).
- **Slots:** base slots + inherited slots; material can add a slot; tool can preserve/transfer a slot.
- **Power budget:** each item has a tier/level and an effect-point budget; inherited effects consume points; reforging cannot exceed the budget.
- **Anti-degeneracy:** prior-work/generation penalty, duplicate-trait suppression, conflict groups, and a hard cap on effect count.

## Comparable systems

- **Path of Exile:** base item + explicit mod pools; essences force a mod; fossils weight/block mods; recombinator transfers mods with probability and exclusive-mod rules. Copy the base-plus-mod-pool model and explicit transfer odds.
- **Nioh 2:** soul matching transfers effects; familiarity gates transfer; inheritable vs transferable distinction; tempering rerolls free effects within conflict pools. Copy the familiarity gate and one-time vs repeatable inheritance.
- **Diablo II:** crafted item = magic item + gem + rune + jewel; item level and affix level determine the affix pool; fixed + random affixes. Copy the input-driven affix pool and item-level gating.
- **Minecraft:** combining two items restores durability and merges enchantments; prior-work penalty; incompatible enchantment groups. Copy the penalty and conflict groups.
- **Monster Hunter:** weapon trees consume materials; armor skills/decorations are slot-budgeted. Copy material tiers and slot budgets.
- **Terraria:** reforging rerolls a prefix for cost. Use only if you want a random reroll sink; it is not an inheritance system.

## UE 5.8 implementation

- **Static definitions:** `UItemDefinition` (`UDataAsset`) for meshes, materials, animations, and shared data; `FItemData` (`FTableRowBase`) for lightweight DataTable rows; soft `TSoftObjectPtr` references because DataTables cannot hold hard UObject references.
- **Runtime instances:** `FItemInstance` struct with stable ID, definition ID, durability state/current/max, trait/effect arrays, parent IDs, generation, and RNG seed.
- **Trait/effect definitions:** DataAssets or DataTable rows; gameplay tags for family/material/element/effect category.
- **Reforge recipes:** data-driven definitions with tool tag, similar-item tags, material tags, costs, and inheritance rules.
- **GAS:** granted abilities as GameplayAbilities; stat/status effects as GameplayEffects; tags for stacking/conflicts; attributes for durability if needed.
- **Deterministic RNG:** a dedicated `FRandomStream` per reforge, seeded from base ID, similar-item ID, material ID, recipe ID, and a salt; never use one global stream. Store the seed with the output.
- **Preview:** compute the output in a dry-run mode without consuming inputs; show odds, inherited effects, conflicts, and durability.
- **Persistence:** save item instances and lineage records with schema versioning; prune lineage beyond a cap; save stable IDs, not actor pointers.
- **UI:** reforge screen with base/similar/material/tool slots, predicted outcome, inheritance odds, conflict warnings, cost, and confirmation.
- **Tests:** durability transitions, recipe rejection, inheritance probability over many seeds, effect caps/conflict groups, save/load lineage, anti-duplication, economy simulation.

## Implementation order

1. Item definition/instance + two-state durability + save/load.
2. Reforge recipe validation: tool + similar item + material.
3. Deterministic inheritance channels + dry-run preview.
4. Effect composition, stack caps, and conflict groups.
5. Lineage/generation records + mutation + anti-degeneracy.
6. Reforge UI and tooltips.
7. Economy/balance and content expansion.

**Minimal slice:** one sword family, two similar swords, three materials, one tool. Break a sword, reforge it with a similar sword + material, inherit one ability and one stat bias, preview the odds, restore durability, save/load, and assert the lineage and effects are identical.

## Anti-patterns

- Permanent break with no recovery path; two-state + reforge is the fix.
- Durability as inventory tax rather than a maintenance choice.
- Universal repair kits that erase item identity.
- Inheritance with hidden odds and no preview.
- Infinite reforge loops that stack every effect; use generation caps, prior-work penalties, and conflict groups.
- Too many materials/traits before the loop is proven; combinatorial explosion.
- Saving actor pointers or display names instead of stable IDs.
- Global RNG for inheritance; seed drift across sessions.
- Confusing "similar item" rules; define them with tags and show them in the UI.
- Copying D&D legacy personal penalties; use resource maintenance instead.

## Verify-first

- Re-verify Epic item data, GAS, and save APIs against dev.epicgames.com.
- Re-verify deterministic RNG behavior and seed persistence for the installed engine version.
- Re-verify Pokémon/D&D/PoE/Nioh/Minecraft mechanics against current sources before copying exact probabilities; several wiki pages were blocked during research.
- Playtest the durability cadence and reforge costs before content scale.

## Related

`inventory-equipment.md` · `progression.md` · `class-skill-leveling.md` · `save-system.md` · `../rpg-design.md` · `../data-driven-modding.md`
