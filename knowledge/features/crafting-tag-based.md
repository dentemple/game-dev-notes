---
title: Tag-Based Ingredient Crafting
tags: [feature, crafting, items, ingredients, tags, categories, atelier, monster-hunter, left-4-dead, crock-pot, alchemy, opportunity-cost]
source: https://www.koeitecmoamerica.com/manual/duskdx/ayesha/en/3600.html (accessed 2026-11-20)
updated: 2026-11-20
---

# Tag-Based Ingredient Crafting

## Goal & scope

Crafting driven by ingredient *types and tags* rather than fixed recipes. Ingredients compete for multiple uses, strong enemies drop materials with several possible applications, and the output depends on what was mixed. Covers the ingredient/recipe data model, matching algorithm, discovery, enemy drops, UI, and balance. Extends the item/durability/genetics system in `durability-reforging-genetics.md`.

## Primary sources

- Atelier Ayesha synthesis manual (categories, CP, quality, effects, traits):
  https://www.koeitecmoamerica.com/manual/duskdx/ayesha/en/3600.html (accessed 2026-11-20)
- Atelier Lulua synthesis procedure (quality, traits, awakened effects):
  https://www.koeitecmoeurope.com/manual/lulua/en/7200.html (accessed 2026-11-20)
- Don't Starve Crock Pot (food groups/tags, values, priorities, fallback):
  https://dontstarve.fandom.com/wiki/Crock_Pot (accessed 2026-11-20; reported from wiki/search summary)
- Monster Hunter drop sources (carve, capture, part break, tail, investigations):
  https://eathealthy365.com/monster-hunter-drops-a-complete-guide-to-farming-parts/ (accessed 2026-11-20)
- Left 4 Dead 2 developer commentary (item-slot and consumable decisions):
  https://left4deadwiki.com/wiki/Developer_Commentary (accessed 2026-11-20; reported from search summary)

## Reference models

### Left 4 Dead 2 — opportunity cost, not recipes

L4D2 has no crafting bench; its lesson is **scarce slots and competing uses**. A survivor carries a large-slot item (medkit/defibrillator), a small-slot item (pills/adrenaline), and a throwable (molotov/pipe bomb/bile jar). Valve's commentary explains that each new item had to justify itself against the existing slot: the defibrillator had to be as valuable as a medkit in some situations, and adrenaline needed an extra effect beyond temporary health because pills already restored full speed.

Design takeaway: **an ingredient is only interesting if using it for A blocks using it for B.** Put ingredients into multiple recipes, or into crafting vs repair vs consumable vs upgrade, so the player feels the trade.

### Atelier — category requirements, quality, traits, effects

Atelier synthesis is the closest shipped model to tag-based crafting:

- Recipes may require a **category**, not an exact item: "If a category such as (Gunpowder) is specified, choose any item that falls under that category."
- "The effects and quality of the finished item will depend on the items you select."
- Synthesis previews an "Estimate" of quality and attribute values.
- Effects appear when attribute values cross thresholds ("graduations"); unknown effects show as "????".
- **CP** is the synthesis action budget; ingredient/item level consumes CP. Insufficient CP stops quality/attribute growth and can suppress effects.
- **Traits** enter a limited Stock Yard (up to five), combine in specific pairs, and grant bonuses during synthesis.
- Lulua adds **Awakened Effects** carried by materials, chosen when the material is used; higher quality increases power; traits can be carried to the result at a TP cost.
- Alchemy level gates recipes; higher levels unlock more recipes and stronger synthesis.

Implementation takeaway: model recipes as **requirements over ingredient tags/counts plus quality/trait/effect thresholds**, and make the output a function of the chosen ingredients, not a fixed lookup.

### Monster Hunter — enemy drops with multiple uses

Monster Hunter's materials come from several sources:

- Carving the body (typically three carves).
- Severing and carving a tail.
- Capture rewards, which replace body carves and can favor different rare materials.
- Part breaks, which add "Broken Part Reward" entries (fangs, claws, webbing, spikes).
- Quest rewards and Investigations, with gold boxes favoring rares.
- Palico/Palico equipment and shiny drops.

Rare materials (plates, gems, rubies, mantles) are used across weapon trees, armor, charms, decorations, and augmentation. The design takeaway: **a strong enemy should drop a material that is useful in more than one place**, and the *way* the player defeats it (kill/capture, part breaks, tail sever) should change which materials they get.

### Don't Starve Crock Pot — the concrete tag matcher

The Crock Pot is the clearest implementation of tag-based crafting with fallback:

- It ignores the specific item and reads hidden **food-group tags/values** (meat, fish, fruit, vegetable, egg, sweetener, dairy, fat, bug).
- Ingredients have values (e.g., 0.5 or 1.0 meat), and fillers add no recipe-changing value.
- Recipes have a **priority**; when multiple recipes match, the highest priority wins, with ties resolved randomly.
- Recipes have **exclusions** (e.g., Dragonpie forbids meat; Kabobs forbids Monster Meat).
- **Wet Goop** has negative priority: it is a valid fallback but never beats a real recipe.
- Special rules can override, such as "two or more Monster Foods → Monster Lasagna" unless twigs or a higher-priority recipe apply.

This is a working recipe-matching algorithm: **filter by exclusions, score by tag values, choose highest priority, fall back to a known filler.**

## Ingredient model

Each ingredient definition carries:

- **Tags/categories:** hierarchical gameplay tags (e.g., `Ingredient.Cloth.Rag`, `Material.Metal.Scrap`, `Source.Monster.Alpha`).
- **Values:** tag-specific potency (e.g., `Cloth=1`, `Metal=2`, `Heat=1`).
- **Quality:** numeric grade that influences output quality.
- **Traits:** transferable properties (sharp, fireproof, lightweight, life-drain).
- **Element/effect values:** thresholds that unlock output effects.
- **Source/rarity:** where it drops, how rare it is, and whether it is part-specific.
- **Competing uses:** recipes, repair, fuel, consumables, upgrades; the UI should surface these.

## Recipe/pattern model

A pattern should describe requirements, not a fixed ingredient list:

```
Pattern {
  id,
  required_tags: [{ tag, min_count, min_value }],
  excluded_tags: [],
  quality_range,
  required_traits: [],
  optional_catalysts: [],
  priority,
  output_rules: {
    base_item,
    trait_pool,
    effect_thresholds,
    quality_formula,
    fallback_output
  },
  discovery: { known_by_default, unlock_tag, alchemy_level }
}
```

Matching:

1. Reject ingredients that violate exclusions.
2. Check required tag counts/values and quality thresholds.
3. Score all matching patterns by priority and specificity.
4. Choose the highest-priority valid pattern; deterministic tie-break (e.g., pattern ID/seed).
5. If none match, use the fallback output (Wet Goop analog), but make the fallback intentional and legible.
6. Apply quality, trait inheritance, effect thresholds, and lineage.

## Impactful decisions

- **Every ingredient should have at least two credible uses.** If rags only make bandages, there is no decision. If rags make bandages, torches, or silencers, there is.
- **Make the alternative uses visible.** Show "also used for: bandage, torch, quiet takedown" in the ingredient tooltip.
- **Use scarcity to create tension.** Limited drops and competing recipes make choice meaningful.
- **Enemy materials should be multi-use.** A monster part can be a weapon component, an armor ingredient, a consumable catalyst, or a repair material.
- **Defeat method should matter.** Carve/capture/part break changes drop pools; this rewards planning and gives strong enemies multiple "loot conversations."
- **Avoid a single dominant recipe.** If one output is always best, the decision collapses. Use situational effects, caps, and costs.
- **Use quality/traits as the second decision axis.** Even when the recipe is obvious, choosing which ingredient quality/trait to spend is a decision.

## UE 5.8 implementation

- **Tags:** use `FGameplayTag`/`FGameplayTagContainer` for ingredient categories, traits, effects, and recipe requirements; `FGameplayTagQuery` for all/any/none requirements.
- **Definitions:** `UIngredientDefinition` (DataAsset) for static data; DataTable rows for lightweight numeric tables; soft references for meshes/icons.
- **Instances:** `FIngredientInstance` with definition ID, quantity, quality, trait rolls, source, and stable ID.
- **Patterns:** `UCraftingPatternDefinition` DataAssets or DataTable rows with tag requirements, exclusions, priority, output rules, and discovery gates.
- **Crafting service:** validate → match → score → preview → commit; cache candidate patterns; do not consume inputs on preview.
- **Deterministic RNG:** per-craft `FRandomStream` seeded from ingredient IDs, pattern ID, and a salt; store the seed.
- **Output:** feed into the item genetics system (`durability-reforging-genetics.md`): base item, inherited traits/effects, quality, lineage, durability.
- **UI:** ingredient slots with tag/value display, predicted match/pattern, estimated quality/effects, competing-use warnings, unknown-effect "????", discovery journal, comparison.
- **Testing:** tag coverage, pattern reachability, no dead ingredients, dominance simulation, deterministic preview/commit, save/load.

## Implementation order

1. Tag ontology + ingredient definitions with at least two uses each.
2. Pattern matcher with requirements, exclusions, priority, and fallback.
3. Preview/estimate and commit transaction.
4. One family with competing outputs (e.g., rag + alcohol → bandage vs fire bomb).
5. One strong enemy with part/condition-based drops feeding multiple patterns.
6. Trait/quality inheritance into the item genetics system.
7. Discovery journal, UI polish, content and balance.

**Minimal slice:** rags can become a bandage or a fire bomb; scrap metal can become an anti-human blade or an anti-monster blade; one alpha monster drops a core used in either a weapon or a ward; the preview shows the competing uses and the resulting traits; save/load preserves the crafted item and lineage.

## Anti-patterns

- Fixed recipes disguised as tags; if the player must look up the exact combination, it is not tag-based.
- Tag soup: too many overlapping categories with no clear hierarchy.
- Hidden priority/failure rules; show why a pattern matched or failed.
- One dominant output; the alternative is never worth choosing.
- Ingredients with a single use; no opportunity cost.
- Rare enemy drops with no bad-luck protection and no alternative acquisition path.
- Fallback junk that feels like punishment rather than a readable "nothing matched" result.
- Combinatorial explosion before the matcher and UI are proven.
- Ignoring save/versioning for ingredient instances and crafted lineage.

## Verify-first

- Re-verify Atelier category/CP/quality/trait rules against the current title's manual before copying numbers.
- Re-verify Don't Starve Crock Pot priority/exclusion rules against the wiki; the fetched page was blocked and details came from a search summary.
- Re-verify Monster Hunter drop-source rules for the specific title; carve/capture behavior differs across entries.
- Re-verify UE gameplay-tag query, DataAsset, and crafting/save APIs against dev.epicgames.com.

## Related

`durability-reforging-genetics.md` · `inventory-equipment.md` · `progression.md` · `economy.md` · `../rpg-design.md` · `../data-driven-modding.md`
