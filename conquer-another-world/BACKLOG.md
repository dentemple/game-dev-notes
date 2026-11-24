# Conquer Another World — Backlog

Ordered for de-risking and priority: **prove the controls → prove the loop → prove the pipeline → scale content.** Decisions are checklist items and belong where they appear; gates are stop-and-assess points. Setup lives in `README.md`.

## How to use this backlog

- Work top to bottom. Do not start a phase before the previous gate passes.
- Phase order is priority order. Within a phase, work in the listed dependency order; the `Pillars` section is the tie-breaker.
- A **Decision** must be answered and recorded before the build items below it.
- A **Gate** is a go/no-go. If it fails, iterate or cut — do not build more content to rescue it.
- Every feature drags UI, animation, audio, save data, balance, and QA behind it. Add it only if it makes the game visibly better.
- A feature is not done until it compiles, has a test (automation or a written manual check), persists correctly if stateful, has readable UI/feedback, and stays inside the frame budget.
- Only build the traversal verbs and TotK-style abilities approved in Phase 0; the implementation items assume they survived that decision.
- Inline *Context:* notes define borrowed vocabulary or expand a terse line; they are commentary, not tasks.

## Pillars

The game is a **Roguelike Adventure RPG/Strategy**. Factions change the landscape; the player can engage with the dynamic world lightly or heavily. The run model is decided in Phase 0.

- **Dynamic faction frontier.** Goblin tribes encroach and add enemies; human settlements build infrastructure and add allies; the frontier between them is the conquest target.
- **Skyrim-like dynamic world.** Towns and caves change ownership, tier, population, and purpose as factions and the player act.
- **Engagement tiers.** Low engagement: the player's actions swing map control to the factions they help. High engagement: the player commands faction armies and build queues alongside the avatar.
- **Adventure combat.** Melee flavored by Shadow of Mordor/War; spellcasting flavored by Skyrim and Genshin Impact.
- **Squad density + Day 1 difficulty.** Squad combat provides battlefield density; the difficulty mechanism must scale for co-op, D&D-style NPC parties, and roguelike obstacles/help from the first playable.
- **Meaningful traversal and conquest.** TotK-inspired climbing, gliding, Recall, Ascend, Ultrahand, and Fuse exist to make exploration and conquest meaningful; they are not a vehicle- or contraption-building system.

**Tags:** `(architecture)`, `(landscape)`, `(world-streaming)`, `(movement)`, `(stamina)`, `(traversal-ability)`, `(animation)`, `(input)`, `(camera)`, `(physics)`, `(persistence)`, `(performance)`, `(testing)`, `(ui)`, `(world-state)`, `(world-map)`, `(local-map)`, `(tier-transition)`, `(squad)`, `(base-building)`, `(strategic-ai)`, `(economy)`, `(procgen)`, `(voronoi)`, `(validation)`, `(melee)`, `(ranged)`, `(combat)`, `(spellcasting)`, `(reaction)`, `(cc)`, `(rendering)`, `(vfx)`, `(style)`, `(items)`, `(crafting)`, `(genetics)`, `(durability)`, `(roguelike)`, `(run)`, `(meta-progression)`, `(faction-sim)`, `(frontier)`, `(infrastructure)`, `(dynamic-world)`, `(poi-state)`, `(engagement)`, `(party)`, `(co-op)`, `(difficulty)`, `(threat-budget)`, `(run-modifier)`, `(exploration)`, `(navigation)`, `(fast-travel)`, `(onboarding)`, `(audio)`, `(settings)`, `(accessibility)`, `(telemetry)`, `(ci)`, `(ui-framework)`.

**Implementation spike order:** climbing → gliding → single-object Ultrahand → layered world and streaming skeleton → Recall → delta-save → Ascend/Fuse. Animation and IK integration follows the movement work. The phase checklists place each spike where its surrounding systems are ready.

**Multi-scale spike order:** canonical world state → World Map turn and army movement → World Map → Landscape round-trip → Local Map orders → one squad → build plots → strategic AI.

**Procgen spike order:** reproducibility harness → headless World Map Voronoi generator → biome/terrain passes and validation → Local Map projection → heightmap/weightmap import → authored overrides → PCG scatter and baked borders.
  - *Context: Baked borders are generated region-edge meshes precomputed as static geometry so they render with Nanite and instancing.*

**Combat spike order:** greybox strike/counter/dodge/stun + token manager + hit streak → one special archetype → Might/Elf-shot/Focus loop → aim mode, charged shot, Shadow Strike → more archetypes and combat traits → hitstop/camera polish.

**Spellcasting spike order:** spell data model + one projectile/self-buff → primer/detonator + ICD → resource/ultimate loop → three elements/reaction matrix → CC diminishing returns/breakbar → delivery expansion → VFX/UI polish.

**Rendering spike order:** post-process style pass → style profiles/manager → distance blend and fog convergence → watercolor Niagara VFX → far-field HLOD/impostors → scalability and visual regression.
  - *Context: Fog convergence means matching the far-field style's color and contrast to atmospheric fog so the style boundary does not visibly pop.*

**Item-system spike order:** item definition/instance + durability → reforge validation → deterministic inheritance + preview → effect composition/conflicts → lineage/generation caps → UI/economy.

**Ingredient-crafting spike order:** tag ontology + ingredient definitions → pattern matcher with exclusions/priority/fallback → preview/commit → competing-output recipes → enemy multi-use drops → discovery journal → balance/audits.

**Roguelike/faction spike order:** run lifecycle + meta-progression → one goblin-vs-human frontier → dynamic town/cave state → engagement tiers → one NPC party → co-op/party threat budget → run modifiers/events → exploration/fast-travel rewards.

**Party/co-op spike order:** party data/roster → one NPC companion → party commands/AI → co-op party abstraction → threat-budget scaling → co-op combat/revive → co-op UI/network tests.

**Exploration/conquest spike order:** map discovery/fog → POI/reward tables → fast-travel network → faction opportunity/reward loop → conquest motivation UI → content scale.

## Terminology

Recurring acronyms and borrowed system terms. One-off terms are explained inline at first use.

| Term | Meaning |
|---|---|
| TotK | *The Legend of Zelda: Tears of the Kingdom*. Its abilities are Ascend, Recall, Ultrahand, and Fuse. |
| Ultrahand | The TotK ability to grab, move, and rotate physics objects. |
| Recall | The TotK ability to rewind an object's recorded movement. |
| GAS | Gameplay Ability System: UE's framework for abilities, attributes, costs, cooldowns, and gameplay tags. |
| CMC | Character Movement Component: UE's default character movement class; this project subclasses it. |
| EQS | Environment Query System: UE's spatial query and scoring system for AI decisions. |
| HLOD | Hierarchical Level of Detail: merged proxy geometry that replaces distant World Partition cells. |
| HISM | Hierarchical Instanced Static Mesh: GPU-instanced repeated meshes. |
| Mass | UE's Mass Entity framework for large, data-oriented crowds. |
| PCG | Procedural Content Generation: UE's rule-based framework for scattering and placing content. |
| RVT | Runtime Virtual Texture: a runtime-rendered texture that terrain and meshes sample for blending. |
| MPC | Material Parameter Collection: global named parameters shared by many materials. |
| TSR | Temporal Super Resolution: UE's temporal upscaler; its history and clamping affect ghosting and shimmer. |
| RDG | Render Dependency Graph: UE's API for authoring custom render passes; `ISceneViewExtension` hooks one into the frame. |
| StateTree | UE's hierarchical state-machine system, used as an alternative to Behavior Trees. |
| Game Features | UE's modular, mountable feature packages that can be enabled per project or build. |
| UMG | Unreal Motion Graphics: UE's widget-based UI framework. |
| PBR | Physically Based Rendering: shading driven by albedo, roughness, metalness, and normal maps. |
| Level Instance | A sublevel packed into one actor and streamed as a unit. |
| Data Layer | A World Partition layer that can be toggled or streamed independently. |
| Runtime hash | World Partition's spatial partition structure used at runtime to decide what streams. |
| After Tonemapping | The post-process stage after HDR-to-LDR conversion, where color and style filters run. |
| Blendables | Post-process materials stacked by priority in the post-process settings. |
| Mover | UE's newer experimental movement component; this project defaults to a custom CMC instead. |
| ICD | Internal cooldown: a short per-target lockout that stops a reaction or effect retriggering every frame. |
| CC / DR | Crowd control / diminishing returns: repeated stuns, roots, or fears last shorter each time. |
| Breakbar | A stagger meter: crowd control depletes it, then the elite is briefly vulnerable instead of stun-locked. |
| Primer / detonator | A combo model: one ability applies a status, another consumes it for a reaction. |
| Aura / trigger | The Genshin model: an elemental aura is applied, then a trigger hit consumes it for a reaction. |
| Token manager | A budget of simultaneous attack slots; enemies must claim a token before striking, which prevents swarming. |
| Freeflow | The Arkham/Shadow of Mordor crowd-combat model: few verbs, auto-targeted strikes, counters, and tokens. |
| Captain | An elite leader enemy with extra combat traits; not the Nemesis system's procedural rival hierarchy. |
| Alpha monster | A strong elite enemy whose rare drop has multiple crafting uses. |
| Hit Streak | The live counter of consecutive hits; a charged streak unlocks executions and wraith abilities. |
| Might | The execution resource built during combat; it resets on damage, a miss, or combat exit. |
| Elf-shot | Limited spectral ammunition for ranged abilities. |
| Focus | The slow-motion aim resource used while aiming. |
| Flurry | The rapid strike sequence that follows a successful stun. |
| Wraith abilities | Shadow of Mordor's spectral powers: Wraith Stun, Flash, Burn, and Combat Drain. |
| POI | Point of interest: a dungeon, camp, landmark, or resource node placed on the map. |
| DDC | Derived Data Cache: stored compiled shader and asset intermediates that keep rebuilds fast. |
| Cook | Converting editor assets into platform-ready runtime data before packaging. |
| Delta save | A save that stores only records changed since the last save, not the whole world. |
| Golden seed | A fixed generator seed whose output is stored as a baseline and diffed on every run. |
| Motion Matching / Motion Warping | Motion Matching chooses animation frames from a database by trajectory; Motion Warping adjusts a montage's root motion to hit a target. |

## Phase 0 — Define the game and lock irreversible choices

**Goal:** settle the decisions that are expensive to reverse before code or content exists.

- [ ] As the developer, I want a one-paragraph vision statement (fantasy, player role, tone) so every feature can be judged against it.
- [ ] As the developer, I want the genre and two to four pillar features named, so the backlog does not sprawl.
- [ ] As the developer, I want the core-loop hypothesis in one sentence (verb → reward → growth → harder challenge), so the prototype has a testable target.
- [ ] As the developer, I want a target session shape (length, platform, input) so scope and UI are sized correctly.
- [ ] As the developer, I want a written "not building" list, so scope creep has an answer.
- [ ] **(roguelike)** **Decision:** Run model — run-based vs. persistent world with runs; what resets on death/run end; what persists (meta-progression, unlocks, faction knowledge, map discovery).
- [ ] **(roguelike)** **Decision:** Run length, victory/defeat conditions, and new-run flow.
- [ ] **(faction-sim)** **Decision:** Dynamic faction simulation — goblin encroachment, human infrastructure, frontier control; which factions, how control changes, and how player actions influence it.
- [ ] **(dynamic-world)** **Decision:** Dynamic town/cave state — ownership, tier, population, purpose, upgrades, destruction, repopulation, quests, spawns; what changes and what persists.
- [ ] **(engagement)** **Decision:** Engagement tiers — how the player moves from light influence (swing map control) to full command (faction armies, build queues); what gates the transition.
- [ ] **(party)** **Decision:** NPC party model — party size, roles, recruitment, AI control, leveling, equipment, approval/banter, injury/permadeath; how parties interact with co-op.
- [ ] **(co-op)** **Decision:** Co-op scope — player count, online/local, host/client, drop-in/out, save authority, matchmaking; Day 1 architecture.
- [ ] **(difficulty)** **Decision:** Day 1 difficulty/threat-budget mechanism — scales with player count, NPC party size/composition, roguelike modifiers, faction state, and player power; not HP-only.
- [ ] **(run-modifier)** **Decision:** Roguelike obstacles/help — run modifiers (boons/curses), random events, faction interventions, dynamic encounters, risk/reward choices.
- [ ] **(exploration)** **Decision:** Exploration/conquest rewards — what makes exploration and conquest meaningful (POIs, lore, resources, recruits, fast travel, map discovery, territory, build queues).
- [ ] As the developer, I want falsifiable success criteria for the prototype and the slice (for example, "five fresh playtesters ask to keep playing"), so the gates are real.
- [ ] As the developer, I want visual references and an art-direction target, so the slice has something concrete to match.
- [ ] **Decision:** Single-player or multiplayer? Decide now. If multiplayer is even possible later, replication affects actor design, GAS placement, session management, and every test.
  - *Context: The pillar requires a Day 1 party-scaling difficulty mechanism that can support co-op; decide whether co-op is implemented now or only kept architecturally possible.*
- [ ] **Decision:** Target platform(s) and input devices (PC keyboard/mouse, gamepad, Steam Deck, console). This fixes input, UI framework, performance budget, and packaging.
- [ ] **Decision:** Combat model — real-time action, turn-based, or hybrid/real-time-with-pause — before any combat prototype.
- [ ] **Decision:** C++/Blueprint split, defaulting to a C++ foundation with Blueprint classes on top. Name which systems must be C++ (GAS, save, subsystems, performance-critical code).
- [ ] **Decision:** Engine version lock (UE 5.8.x stable) and upgrade policy. Do not drift onto a preview mid-project.
- [ ] **Decision:** AI-assisted development rules for Claude Code/DeepSeek: what may be generated, what must be hand-reviewed, and the rule that nothing is committed without a clean build and passing tests.
- [ ] **Decision:** Modding support — yes or no. If yes, data-driven architecture and plugin/pak boundaries become early requirements; if no, record it and stop revisiting it.
- [ ] **Decision:** Localization — will the game ship in more than one language? If yes, all user-facing text uses `FText` from day one; translation can wait until content lock.
- [ ] **(architecture)** **Decision:** Movement architecture — custom `UCharacterMovementComponent`, GAS-driven movement, physics-driven movement, or Mover. Default to a custom CMC on UE 5.8; record why.
- [ ] **(landscape)** **Decision:** Terrain approach — Landscape-only, mesh-only, or hybrid. Default to Landscape for the ground plane plus Nanite meshes for cliffs, caves, and sky islands.
- [ ] **(world-streaming)** **Decision:** Map size and streaming budget. Set a hard map cap, target cell size, and loading range before any terrain is built.
- [ ] **(movement)** **Decision:** Which traversal verbs ship in v1 — climb, glide, swim, sprint, slide, mount, zipline — and which are cut.
- [ ] **(traversal-ability)** **Decision:** Which TotK-style abilities are in scope — Ascend, Recall, Ultrahand, Fuse. Start with one; cut the rest unless they serve the core loop.
  - *Context: Ultrahand and Fuse are exploration/interaction tools, not a vehicle- or contraption-building system.*
- [ ] **(persistence)** **Decision:** What dynamic world state must persist — moved objects, built structures, altered terrain, quest flags — and whether delta saves are sufficient.
- [ ] **(performance)** **Decision:** Target frame budget, streaming budget, and memory budget for the target hardware, including mobile quality tiers if mobile is a target.
- [ ] **(animation)** **Decision:** Locomotion stack — Motion Matching versus blend spaces — and where Motion Warping is allowed for discrete traversal moves.
- [ ] **(input)** **Decision:** Input contexts and remapping strategy for ground, air, climbing, swimming, and UI states.
- [ ] **(world-state)** **Decision:** Canonical world-state model — which entities (hexes, regions, settlements, armies, squads, units, buildings, monster spawns) get stable IDs, what each record owns, and what is derived.
- [ ] **(tier-transition)** **Decision:** Tier architecture — separate maps per tier, one World Partition world, or a Humankind-style overlay for the Local Map. Pick the combination that keeps state handoff simple.
  - *Context: Humankind draws its strategic map as an abstract overlay above the same terrain; the Local Map could do the same instead of using a separate level.*
- [ ] **(world-map)** **Decision:** Hex-grid size and tile data — ground type, movement cost, region, owner — plus the army movement and turn model.
- [ ] **(local-map)** **Decision:** Local Map representation — orthographic overlay on the Landscape versus a separate simplified level reading the same records.
- [ ] **(squad)** **Decision:** Squad granularity — member count, whether members are actors or lightweight instances, and what persists (squad record, casualties, experience, equipment).
- [ ] **(base-building)** **Decision:** Predefined build plots versus free placement; plot size and grid; which buildings are constructible and what they require.
- [ ] **(tier-transition)** **Decision:** Strategic time model — turn-based, real-time with pause, or hybrid — and whether strategic time pauses while the player is in the Landscape.
- [ ] **(strategic-ai)** **Decision:** Strategic AI scope — scripted factions, utility AI, or Behavior Trees — and how armies and towns decide.
- [ ] **(performance)** **Decision:** Battle scale — maximum squads and members on screen, and whether Mass or HISM is used for background crowds only.
  - *Context: Squad density must scale for co-op and NPC parties; the threat-budget system owns that scaling.*
- [ ] **(economy)** **Decision:** Resource flow — where army and construction costs come from, and how towns or captured points feed them.
- [ ] **(procgen)** **Decision:** What is procedural versus authored — regions, biomes, terrain, POIs, encounters, buildings. Default to generating the spatial skeleton and hand-authoring the interesting content.
- [ ] **(voronoi)** **Decision:** Voronoi scope — region, territory, and biome boundaries plus POI spacing only; not heightmaps, erosion, rivers, or caves.
- [ ] **(procgen)** **Decision:** Offline/baked generation versus runtime generation. Default to offline generation with runtime scene selection and cheap scatter.
- [ ] **(procgen)** **Decision:** Generator contract — seed, generator version, parameter blob, override list, and how seeds and versions are stored and migrated.
- [ ] **(world-map)** **Decision:** Hex/Voronoi mapping rule — center containment versus nearest seed — and how region IDs, ownership, and adjacency are derived from cells.
  - *Context: Center containment assigns a hex to the region containing its center; nearest seed assigns it to the closest Voronoi point.*
- [ ] **(procgen)** **Decision:** Generation stack and licenses — delaunator, FastNoise2, Clipper2, PCGEx versus custom code; language and build targets.
  - *Context: delaunator = Delaunay triangulation; FastNoise2 = noise generation; Clipper2 = polygon clipping; PCGEx = extended PCG nodes for UE.*
- [ ] **(procgen)** **Decision:** Validation gates — connectivity, biome distribution, resource fairness, POI spacing and buildability, and road/river connectivity.
- [ ] **(procgen)** **Decision:** Override policy — how authored POIs and buildings merge with generated records and survive regeneration.
- [ ] **(procgen)** **Decision:** World size, region count, and generation time and memory budgets.
- [ ] **(melee)** **Decision:** Melee model — freeflow (small verb set plus crowd control) versus a heavier action-combat model. Default to freeflow.
- [ ] **(ranged)** **Decision:** Ranged model — aim-mode slow motion, charge shots, ammo economy, and hitscan versus projectile for arrows.
- [ ] **(combat)** **Decision:** Resource economy — live hit streak, banked Might, ammo, Focus, and Health; which abilities each resource gates.
  - *Context: Hit Streak is the consecutive-hit counter; Might is the execution resource built during combat; Focus is the slow-motion aim resource; ammo is Elf-shot, the limited spectral arrows.*
- [ ] **(combat)** **Decision:** Crowd throttle — attack-token count and how many special enemy types appear at once.
- [ ] **(combat)** **Decision:** Prompt model — counter prompt versus red dodge-only icon, and whether double-counter is supported.
  - *Context: A counter prompt marks an attack that can be parried; a red dodge-only icon marks an attack that cannot be countered and must be dodged. A double-counter chains counters against two attackers striking at nearly the same time.*
- [ ] **(combat)** **Decision:** Protected versus interruptible finishers; every move must be tagged one or the other.
- [ ] **(combat)** **Decision:** Enemy archetype set and the one required answer for each (archer, defender, hunter, berserker, captain).
  - *Context: Captain here means an elite leader enemy with extra combat traits, not the Nemesis system's procedural rival hierarchy.*
- [ ] **(combat)** **Decision:** Ability list and gates — execution, Wraith Stun/Flash/Burn, Combat Drain, Shadow Strike, Mighty Shot, and upgrades.
  - *Context: Wraith abilities are Shadow of Mordor's spectral powers; Shadow Strike is a teleport strike and Mighty Shot a charged arrow.*
- [ ] **(combat)** **Decision:** Difficulty model — composition, timing windows, token count, and counter-demands, not HP scaling.
- [ ] **(ranged)** **Decision:** Aim camera, time-dilation policy, and Focus drain duration.
- [ ] **(spellcasting)** **Decision:** Spellcasting model — data-driven spell definitions combining delivery, casting type, resource, and effects; choose which systems to borrow from Skyrim, Mass Effect, and Genshin.
- [ ] **(spellcasting)** **Decision:** Element set and reaction-matrix size. Default to three elements and roughly ten spells.
- [ ] **(spellcasting)** **Decision:** Per-tier resource model — cooldown for basics, banked meter for power moves, ammo for ranged, ultimate for the transform.
  - *Context: A transform ultimate replaces the player's moveset and stats for a short window rather than firing one burst.*
- [ ] **(spellcasting)** **Decision:** Casting taxonomy — fire-and-forget, concentration/channel, charge, and constant effect.
  - *Context: A constant effect is an always-on passive spell, as in Skyrim, rather than a cast or channel.*
- [ ] **(spellcasting)** **Decision:** Delivery taxonomy — instant, projectile, beam, cone, ground AoE, self/target buff, construct, summon, chain.
- [ ] **(reaction)** **Decision:** Reaction model — primer/detonator tags, aura/trigger with ICD, or ground fields; default primer/detonator with a small ICD.
- [ ] **(cc)** **Decision:** Crowd-control model — diminishing-returns categories, reset timer, PvE/PvP differences, and which elites use breakbars.
- [ ] **(spellcasting)** **Decision:** Ultimate state — build source, duration, transform versus nuke, cancel rules, and whether smaller abilities spend the same meter.
  - *Context: A nuke ultimate deals one large burst; a transform ultimate temporarily changes the player's state. The per-tier resource model above currently assumes the transform option.*
- [ ] **(spellcasting)** **Decision:** Ability count and cut list — maximum spells, elements, upgrades, and which systems are explicitly not built.
- [ ] **(style)** **Decision:** Visual style domains — realistic near field, impressionist far field, watercolor VFX — and their precedence.
- [ ] **(rendering)** **Decision:** Implementation route — a single post-process material versus custom RDG/SceneViewExtension passes. Start with post-process.
- [ ] **(style)** **Decision:** Distance threshold and blend curve for realistic→impressionist, plus region-versus-distance precedence.
- [ ] **(vfx)** **Decision:** Watercolor VFX approach — authored textures plus a simple shader versus animated simulation. Default to authored.
- [ ] **(rendering)** **Decision:** Temporal-stability policy — TSR settings, world-space noise, and ghosting tolerance.
- [ ] **(rendering)** **Decision:** Performance budget for full-screen style passes and VFX overdraw, plus quality-tier toggles.
- [ ] **(style)** **Decision:** Style assignment channels — stencil, post-process volumes, Data Layers, Runtime Virtual Textures, Material Parameter Collections.
  - *Context: Stencil means a Custom Depth/Stencil value written per object and read by post-process materials for per-object styling.*
- [ ] **(style)** **Decision:** Style count and cut list — how many domains, which regions use them, and what is explicitly not stylized.
- [ ] **(vfx)** **Decision:** Readability rules — near-field PBR/outline priority and VFX opacity limits in combat.
- [ ] **(durability)** **Decision:** Durability model — two-state `Usable`/`Unusable`, degradation triggers, reforge recovery, and whether repeated reforge lowers max durability.
- [ ] **(items)** **Decision:** Which item families and equipment slots are durable; weapons, armor, tools, and accessories may need different rules.
- [ ] **(crafting)** **Decision:** Reforge inputs — tool requirement, what counts as a "similar item," material categories, and whether a station or NPC is required.
- [ ] **(genetics)** **Decision:** Inheritance model — genotype/phenotype, inheritance channels, dominance, mutation, and generation caps.
  - *Context: Genotype is the hidden inherited data; phenotype is the stats and effects actually shown on the item.*
- [ ] **(items)** **Decision:** Effect composition — slots, stack caps, conflict groups, and the item power budget.
- [ ] **(crafting)** **Decision:** Economy — material/item sinks, reforge costs, repair costs, and durability cadence.
  - *Context: Durability cadence is how often gear degrades and breaks relative to playtime.*
- [ ] **(items)** **Decision:** Reforge UI — preview odds, inherited effects, conflict warnings, comparison, and confirmation.
- [ ] **(genetics)** **Decision:** Lineage persistence — parent records, generation depth, save size, and pruning policy.
- [ ] **(items)** **Decision:** V1 content scale — item families, materials, traits, and effects; write the cut list.
- [ ] **(crafting)** **Decision:** Failure model — deterministic success with inheritance odds versus chance of failure/backfire; default to no failure.
- [ ] **(crafting)** **Decision:** Ingredient tag ontology — hierarchy, category values, exclusions, and how many tags/categories the game supports.
- [ ] **(crafting)** **Decision:** Pattern requirements — tag counts/values, quality, traits, optional catalysts, priority, and fallback behavior.
- [ ] **(crafting)** **Decision:** Opportunity-cost policy — every ingredient must have at least two credible uses, and the UI must surface competing uses.
- [ ] **(crafting)** **Decision:** Enemy drop channels — carve/capture/part-break/defeat-method — and how strong enemies supply multi-use materials.
  - *Context: Borrowed from Monster Hunter: carve the body, capture instead of kill, break a body part, and receive different drop pools.*
- [ ] **(crafting)** **Decision:** Discovery model — known patterns versus experimentation, journal, unknown effects, and recipe unlocks.
- [ ] **(crafting)** **Decision:** Fallback result — a legible “nothing matched” output versus outright failure; default to an intentional filler.
- [ ] **(items)** **Decision:** Ingredient content scale — categories, ingredients, patterns, traits, and effects for v1; write the cut list.
- [ ] **(economy)** **Decision:** Ingredient scarcity, drop rates, and competing sinks — crafting versus repair versus consumables versus upgrades.
- [ ] **(ui)** **Decision:** Crafting preview — tags/values, predicted pattern, estimated quality/effects, unknown effects, competing uses, and comparison.
- [ ] As the developer, I want these decisions recorded in a short `DECISIONS.md`, so future-me does not silently reverse them.

## Phase 1 — Foundations and technical spikes

**Goal:** make the project buildable, versioned, observable, and prove the core terrain, streaming, movement, and save pipelines before content exists.

- [ ] **Decision:** Source-control hosting and backup strategy, including LFS quota and a second copy of the repository.
- [ ] **Decision:** Project/plugin structure and which marketplace or first-party plugins are allowed.
- [ ] **Decision:** Testing strategy — what gets automation coverage versus a written manual playtest checklist.
- [ ] As the developer, I want every setup step in `README.md` completed: engine, C++ toolchain, Git + LFS, Claude Code with DeepSeek, and Unreal MCP.
- [ ] As a developer, I want the C++ project created and launching into Play-In-Editor, so the toolchain is proven before code is written.
- [ ] As a developer, I want source control with a clean first commit, `.gitignore`, `.gitattributes`, and LFS rules for `*.uasset`, `*.umap`, `*.ubulk`, and `*.uexp`.
- [ ] As a developer, I want asset/class naming conventions and folder rules written down and enforced by review.
- [ ] As a developer, I want a shared or local derived-data cache configured, so rebuilds stay fast.
- [ ] As a developer, I want a clean `Development Editor` build in Visual Studio/Rider with zero warnings that matter.
- [ ] As a developer, I want one automation smoke test that runs on editor/game startup, so the test harness itself is proven.
- [ ] As a developer, I want logging, crash reporting, and a debug HUD, so problems are visible from the first playable.
- [ ] As a developer, I want a written performance budget (CPU/GPU frame ms, memory, load time) for the target hardware.
- [ ] As a developer, I want a repeatable build → cook → package → run script tested once on a trivial map, so shipping is never a late surprise.
- [ ] **(telemetry)** As the developer, I want a crash reporter with symbol upload, an in-game bug report, and a basic analytics pipeline.
- [ ] **(ci)** As the developer, I want CI builds, nightly packaged smoke tests, and determinism gates for procgen and combat.
- [ ] **(performance)** As the developer, I want a Steam Deck performance floor and PSO/shader-stutter tests, so launch quality is measured.
- [ ] **(audio)** As the developer, I want an audio subsystem with sound classes, submixes, attenuation, concurrency, and dynamic music.
- [ ] **(settings)** As the developer, I want graphics/audio/input/language settings with scalability tiers and device profiles.
- [ ] **(accessibility)** As the developer, I want an accessibility framework (assist/difficulty, remap, subtitles, colorblind, motion reduction, hold/toggle).
- [ ] **(ui-framework)** As the developer, I want a UI framework with widget stacks, gamepad focus, modals, tooltips, safe zones, scaling, and localization hooks.
- [ ] **(validation)** As the developer, I want an asset/data validation commandlet for missing references, bad sizes, missing LODs, and uncompressed assets.
- [ ] **(balance)** As the developer, I want a headless balance/economy simulation harness for combat TTK, drops, progression, and crafting.
- [ ] **(tools)** As the developer, I want a developer console with cheats, spawn/teleport, time scale, save/load, and stat editing.
- [ ] **(platform)** As the developer, I want a platform abstraction for achievements, cloud saves, rich presence, Steam Deck, and suspend/resume.
- [ ] **(localization)** As the developer, I want an FText/string-table/font pipeline with pseudo-localization and text-expansion checks.
- [ ] As a developer, I want a daily commit/backup habit and a tagged milestone, so progress is durable.
- [ ] **(architecture)** As the developer, I want a custom `UCharacterMovementComponent` subclass installed with `SetDefaultSubobjectClass` in the character constructor, so traversal modes have a stable home.
- [ ] **(movement)** As the developer, I want a `MOVE_Custom` mode enum and a `PhysCustom()` dispatch scaffold, so climbing and gliding can be added without rewriting the CMC.
- [ ] **(landscape)** As the developer, I want a test Landscape at the target resolution with a height-range check, so I know the terrain budget before sculpting.
  - *Context: The height-range check confirms the terrain's minimum and maximum heights fit the intended playable vertical scale.*
- [ ] **(landscape)** As the developer, I want a hybrid terrain test — Landscape ground plus a Nanite cliff/cave mesh fitted into a visibility hole — so I can validate the pipeline.
  - *Context: A visibility hole is a section cut out of the Landscape with the Landscape Visibility tool so a mesh cave can occupy it.*
- [ ] **(world-streaming)** As the developer, I want a World Partition test map with cell size and loading range configured, plus `stat streaming` and the runtime-hash debug overlays, so streaming problems appear before content.
  - *Context: World Partition uses a runtime spatial hash; its debug overlays show active cells and streaming sources.*
- [ ] **(performance)** As the developer, I want a packaged-build baseline for `stat unit`, `stat gpu`, `stat streaming`, and `stat memory`, so optimization is measured, not guessed.
- [ ] **(input)** As the developer, I want Enhanced Input actions and a default mapping context for ground movement, so traversal contexts can be layered on later.
- [ ] **(animation)** As the developer, I want a placeholder locomotion animation blueprint with a traversal-state hook, so climbing and gliding can drive animation without rework.
- [ ] **(persistence)** As the developer, I want a versioned save schema with a delta-save path for dynamic objects, so the world can remember changes.
- [ ] **(persistence)** As the developer, I want atomic save writes, checksums, backup rotation, and corruption recovery, not only a backup slot.
- [ ] **(testing)** As the developer, I want an automation smoke test that boots the map and round-trips a save, so traversal and persistence regressions are caught.
- [ ] **(world-state)** As the developer, I want a `UGameInstanceSubsystem` that owns canonical world state and survives level transitions, with stable IDs for every persistent entity.
- [ ] **(roguelike)** As the developer, I want a run-state subsystem (run ID, seed, lifecycle, victory/defeat, death/retry, meta-progression) that survives level transitions.
- [ ] **(faction-sim)** As the developer, I want faction-state records (territory control, influence, infrastructure, armies, goals) with a deterministic tick.
- [ ] **(dynamic-world)** As the developer, I want dynamic POI-state records for towns and caves (ownership, tier, population, purpose, upgrades, destruction, repopulation, quests, spawns).
- [ ] **(engagement)** As the developer, I want engagement-tier state (influence score, command unlocks, army/build-queue access) in the canonical store.
- [ ] **(party)** As the developer, I want an NPC party roster and definitions (roles, stats, AI, equipment, leveling, recruitment, approval).
- [ ] **(co-op)** As the developer, I want a party/co-op abstraction (player count, composition, authority, save) that gameplay reads instead of assuming one player.
- [ ] **(difficulty)** As the developer, I want a threat-budget service that computes encounter budgets from party size/composition, roguelike modifiers, faction state, and player power.
- [ ] **(run-modifier)** As the developer, I want run modifier and event definitions (boons, curses, faction interventions, random events, risk/reward).
- [ ] **(exploration)** As the developer, I want discovery and reward data (POIs, secrets, lore, resources, recruits, fast-travel points, map fog).
- [ ] **(navigation)** As the developer, I want map/compass/waypoint/fast-travel data and UI hooks.
- [ ] **(telemetry)** As the developer, I want run/faction/party/co-op telemetry events, so balance is data-driven.
- [ ] **(persistence)** As the developer, I want run, faction, POI, engagement, party, and co-op state saved and versioned.
- [ ] **(world-state)** As the developer, I want a versioned `USaveGame` delta round-trip for armies, squads, buildings, and hex state, so the strategic layer survives save/load.
- [ ] **(world-map)** As the developer, I want a minimal hex-grid data model with ground type, movement cost, region, and owner, so strategic pathfinding has one source of truth.
- [ ] **(tier-transition)** As the developer, I want a stub World Map → Landscape → World Map transition using hard level loads and the canonical store, so the handoff is proven before content.
- [ ] **(testing)** As the developer, I want an automation test that creates an army, enters the Landscape, returns, saves, loads, and asserts no state drift.
- [ ] **(procgen)** As the developer, I want a deterministic RNG and a generator contract of seed, version, parameters, and overrides, so the same inputs always produce the same world.
- [ ] **(procgen)** As the developer, I want an offline generator CLI/library scaffold that runs headless, so generation is testable outside UE.
- [ ] **(voronoi)** As the developer, I want a minimal Delaunay/Voronoi proof — points to cells to adjacency, with border handling — so the core algorithm is proven.
- [ ] **(validation)** As the developer, I want a validation pass skeleton for connectivity, biome bounds, and POI spacing, so broken maps fail early.
- [ ] **(procgen)** As the developer, I want golden-seed snapshot tests and a multi-seed validation runner, so generator changes are caught as diffs.
- [ ] **(world-state)** As the developer, I want the seed, generator version, parameters, and overrides stored in the canonical save, so worlds can be regenerated.
- [ ] **(rendering)** As the developer, I want a packaged-build GPU-ms baseline before any style pass, so every style cost is measured against a known budget.
- [ ] **(style)** As the developer, I want a style profile data asset and a style manager scaffold, so near/far/VFX styles are data-driven from the start.
- [ ] **(rendering)** As the developer, I want one After-Tonemapping post-process material with a distance mask, so the style stack is proven on a greybox.
- [ ] **(vfx)** As the developer, I want one watercolor-textured Niagara effect with a simple shader, rim light, and edge darkening.
- [ ] **(style)** As the developer, I want a test scene with a clear near/far boundary for seam and temporal-stability checks.
- [ ] **(items)** As the developer, I want a data-driven item definition/instance model with stable IDs, so items survive saves, reforges, and tier transitions.
- [ ] **(durability)** As the developer, I want two-state durability (`Usable`/`Unusable`) with save/load, so the break/reforge boundary is testable.
- [ ] **(crafting)** As the developer, I want reforge recipe definitions for tool, similar-item, and material inputs, so the recipe system is data-driven.
- [ ] **(genetics)** As the developer, I want a deterministic per-item/per-reforge random stream with a stored seed, so inheritance is reproducible.
- [ ] **(items)** As the developer, I want trait/effect definitions with tags, stack rules, and conflict groups, so inheritance has a stable vocabulary.
- [ ] **(testing)** As the developer, I want durability-transition and item-save/load tests before the reforge service is built.
- [ ] **(crafting)** As the developer, I want ingredient definitions and instances with tags, values, quality, traits, source, and stable IDs.
- [ ] **(crafting)** As the developer, I want a pattern-definition schema with required tags, exclusions, quality thresholds, priority, and fallback output.
- [ ] **(crafting)** As the developer, I want a matcher skeleton with deterministic tie-breaking and a dry-run preview.
- [ ] **(crafting)** As the developer, I want a preview/commit transaction that never consumes ingredients on a rejected or unconfirmed craft.
- [ ] **(economy)** As the developer, I want an ingredient source/drop-table skeleton, so scarcity can be tuned later.
- [ ] **(testing)** As the developer, I want tag-coverage and matcher unit tests, including exclusions, priority, and fallback.

## Phase 2 — First playable: the 3 C's

**Goal:** make character, camera, and control feel right before anything else is built on them.

- [ ] **Decision:** Camera perspective (first-person, third-person, top-down, isometric) and movement set (walk/run/jump/climb/dash/glide).
- [ ] **Decision:** Animation approach for now and for the slice (in-house, marketplace, or outsourced).
- [ ] **Decision:** Gamepad-first or keyboard/mouse-first, and which prompts the UI shows by default.
- [ ] As a player, I want movement that responds immediately and predictably, so the character feels good to control.
- [ ] As a player, I want a camera that frames the action and never fights my input.
- [ ] As a developer, I want Enhanced Input actions and mapping contexts for every core verb, with remappable bindings.
- [ ] As a player, I want contextual interaction prompts, so I know what I can interact with.
- [ ] As a developer, I want placeholder idle/run/jump animations wired to movement, so timing and readability can be judged.
- [ ] As a developer, I want a graybox test level sized to the intended movement speed, so traversal is testable.
- [ ] As a developer, I want a debug view of input state, camera mode, and movement speed.
- [ ] As a player, I want a short controls tutorial or prompt card, so a new tester is not blocked by controls.
- [ ] **(onboarding)** As a new player, I want to learn the roguelike/faction/party/co-op loop through contextual play, not a text wall, so the first run is understandable.
- [ ] As a developer, I want five fresh-player control tests with notes on confusion and discomfort.
- [ ] **(movement)** As the player, I want a capsule trace to detect climbable walls and reject non-climbable surfaces by SurfaceType or Physical Material, so climbing is readable and controlled.
- [ ] **(movement)** As the player, I want averaged surface normals and a smoothed climb rotation (`MakeFromX(-Normal)` plus `QInterpTo`), so corners and curved walls do not jitter.
- [ ] **(movement)** As the player, I want the capsule snapped to the climb surface while moving, so I can climb curved and overhanging geometry without falling off.
- [ ] **(movement)** As the player, I want climb input projected onto the surface plane, so climbing follows slopes and overhangs instead of world-up.
- [ ] **(movement)** As the player, I want a ledge mantle using traced Motion Warping targets and `ConstrainAnimRootMotionVelocity`, so pull-ups land cleanly.
- [ ] **(movement)** As the player, I want a gliding mode built from `GravityScale`, `AirControl`, `FallingLateralFriction`, and a manual vertical-velocity clamp, so gliding has a controllable dive/rise tradeoff.
- [ ] **(stamina)** As the player, I want one shared stamina pool drained by climbing, gliding, sprinting, and swimming, with readable regeneration, so traversal has a consistent cost.
- [ ] **(exploration)** As the player, I want traversal to lead to meaningful discoveries, resources, recruits, and conquest opportunities, so movement is not just traversal.
- [ ] **(animation)** As the player, I want motion-warped vaults and hops plus Control Rig foot and hand IK, so traversal moves match the terrain.
- [ ] **(input)** As the player, I want jump buffering and coyote time as separate tunables, so traversal feels forgiving without changing the movement math.
- [ ] **(camera)** As the player, I want camera collision and lag tuned for climbing and gliding, so the camera does not clip or fight the motion.
- [ ] **(performance)** As the developer, I want traversal tested in a packaged build, so editor-only performance does not hide problems.
- [ ] **(world-state)** As the developer, I want the player character's persistent state — position, health, stamina, inventory — written to the canonical store on tier exit, so it survives transitions.
- [ ] **(tier-transition)** As the player, I want a loading screen and a clean pawn/camera handoff between tiers, so transitions are clear and state-safe.
- [ ] **Gate:** A new player can use every v1 traversal verb without fighting the controls. Iterate until yes.

## Phase 3 — Core-loop prototype (disposable)

**Goal:** prove the fun with throwaway code and placeholder content, then decide whether to continue.

- [ ] As a developer, I want the loop statement written down and a graybox arena that exercises it end to end.
- [ ] As a player, I want one combat verb that feels good, with readable wind-up, impact, and recovery.
- [ ] As a player, I want an enemy that can die and can kill me, so the loop has stakes.
- [ ] As a player, I want a reward (loot, XP, access, or story) that makes the loop turn.
- [ ] As a player, I want a failure and retry state, so failure teaches something.
- [ ] As a developer, I want a minimal HUD (health, resource, objective) to test readability.
- [ ] As a developer, I want temporary hitstop, camera shake, flashes, and placeholder SFX to test game feel.
- [ ] **(roguelike)** As the player, I want one complete run start-to-end — seed, run start, faction front, dynamic town/cave, death/retry, meta-progression stub — so the roguelike loop is testable.
- [ ] **(faction-sim)** As the player, I want one goblin-vs-human frontier where goblin encroachment and human infrastructure change the landscape, and my actions swing control.
- [ ] **(faction-sim)** As the player, I want my actions to change faction standing and map control, so low-engagement play has visible consequences.
- [ ] **(faction-sim)** As the player, I want one faction quest/event that changes standing or control, so the RPG and strategy layers connect.
- [ ] **(faction-sim)** As the player, I want goblin camps/tunnels and human roads/outposts to appear and change on the landscape, so the faction frontier is visible.
- [ ] **(dynamic-world)** As the player, I want one town and one cave to change state (captured, upgraded, destroyed, repopulated), so the world feels dynamic.
- [ ] **(engagement)** As the player, I want to switch between light influence (swing map control) and full command (army/build queue), so engagement depth is a choice.
- [ ] **(party)** As the player, I want one NPC party of 2–3 companions with roles, AI, recruitment, equipment, and leveling, so D&D-style parties are testable.
- [ ] **(co-op)** As the developer, I want one co-op scaling test (two players or simulated) with threat-budget scaling, so co-op is not bolted on later.
- [ ] **(difficulty)** As the developer, I want a threat-budget test where party size/composition, a roguelike modifier, and faction state change the encounter budget.
- [ ] **(run-modifier)** As the player, I want one run modifier/obstacle/help (boon, curse, event, or faction intervention), so runs vary.
- [ ] **(exploration)** As the player, I want one meaningful exploration loop: map discovery → POI → reward → fast travel/conquest motivation.
- [ ] **(squad)** As the player, I want one squad battle with density + party/co-op scaling, so squad combat is proven with the difficulty mechanism.
- [ ] **(telemetry)** As the developer, I want run outcome, faction control, and party-size telemetry from the prototype.
- [ ] **(melee)** As the player, I want a greybox melee loop — attack, counter, dodge, stun/flurry, and execution — with the Hit Streak charging at 8 consecutive hits.
  - *Context: Flurry is the rapid strike sequence that follows a successful stun.*
- [ ] **(combat)** As the developer, I want an attack-token manager limiting the crowd to 2–3 simultaneous attackers, so the player is pressured but never swarmed.
- [ ] **(melee)** As the player, I want a counter prompt and a red dodge-only icon, plus a double-counter for simultaneous attackers, so un-counterable attacks are readable.
- [ ] **(combat)** As the player, I want one basic enemy and one special archetype with a required answer, so counterplay is testable.
  - *Context: A required answer is the one counter an archetype demands, such as vaulting a shield or dodging a berserker.*
- [ ] **(ranged)** As the player, I want an aim mode with Focus slow-motion, a charged shot, and limited Elf-shot, so ranged combat has a cost and a feel.
- [ ] **(combat)** As the developer, I want the resource loop wired — live Hit Streak, banked Might, Elf-shot, Focus, and Health-via-drain — so aggression is rewarded.
  - *Context: Health-via-drain means Combat Drain restores health, making aggression also a recovery path.*
- [ ] **(combat)** As the player, I want executions protected from interruption and ground executions punishable, so finishers carry risk.
- [ ] **(testing)** As the developer, I want combat automation for token cap, streak reset, and ranged hit registration, so the greybox does not regress.
- [ ] **(spellcasting)** As the player, I want one instant projectile spell and one self-buff, each with a visible cost and cooldown, so the spell foundation is testable.
- [ ] **(reaction)** As the player, I want one primer spell and one detonator spell of the same element, with a reaction table and an internal cooldown, so combo magic works end to end.
- [ ] **(spellcasting)** As the player, I want one ultimate meter that builds from aggression and activates a temporary empowered state.
- [ ] **(style)** As the developer, I want one distance-masked post-process style pass on the far field, so the realistic-to-impressionist idea is visible in the prototype.
- [ ] **(rendering)** As the developer, I want a cheap single-pass Kuwahara or bilateral approximation before attempting a multi-pass RDG filter.
  - *Context: Kuwahara and bilateral filters are edge-preserving blurs that flatten color into painterly patches without blurring silhouettes.*
- [ ] **(style)** As the developer, I want the style manager to resolve near-field and far-field precedence, so style assignment is not hard-coded per camera.
- [ ] **(vfx)** As the player, I want one watercolor impact effect in combat, so the VFX style is judged in motion.
- [ ] **(testing)** As the developer, I want a camera-pan test for seams and temporal shimmer at the style boundary.
- [ ] **(rendering)** As the developer, I want the style pass and watercolor VFX measured against the GPU-ms budget.
- [ ] **(testing)** As the developer, I want spell automation for cost/cooldown correctness, ICD, and reaction triggers.
- [ ] **(items)** As the player, I want one durable item family — a sword — that becomes `Unusable` at zero durability without being destroyed.
- [ ] **(crafting)** As the player, I want one reforge recipe using a tool, a similar sword, and a material, so the recovery loop is playable.
- [ ] **(genetics)** As the player, I want the reforged sword to inherit one ability and one stat bias from its parents/material, with a preview before committing.
- [ ] **(testing)** As the developer, I want a deterministic reforge test and a lineage save/load test.
- [ ] **(economy)** As the developer, I want the reforge to consume the similar item and material, so the loop has real sinks.
- [ ] **(crafting)** As the player, I want rags to become either a bandage or a fire bomb, so the first ingredient has a real competing use.
- [ ] **(crafting)** As the player, I want scrap metal to become either an anti-human blade or an anti-monster blade, so material choice changes combat.
- [ ] **(crafting)** As the player, I want one alpha-monster core with at least two uses, so a strong enemy opens a crafting decision.
- [ ] **(crafting)** As the player, I want the matcher, exclusion rules, priority, fallback, and preview working end to end.
- [ ] **(testing)** As the developer, I want deterministic craft and save/load tests for ingredient instances and crafted outputs.
- [ ] **(economy)** As the developer, I want scarcity tuned so the competing uses are felt rather than theoretical.
- [ ] **(voronoi)** As the developer, I want to generate World Map points, Delaunay/Voronoi cells, hex assignments, and region adjacency, so the strategic map has a coherent structure.
  - *Context: Hex assignment maps each generated Voronoi cell or point onto a hex tile so the strategic grid and region map agree.*
- [ ] **(procgen)** As the developer, I want elevation, moisture, biome, and river passes assigned to cells, so the map has terrain logic.
- [ ] **(validation)** As the developer, I want connectivity, biome, and resource-fairness validation on the generated map, so every seed is playable.
- [ ] **(local-map)** As the player, I want the Local Map to project one generated region's records, so the two scales agree.
- [ ] **(landscape)** As the developer, I want to export and import one region's heightmap and weightmaps and verify it matches the World Map, so the three tiers align.
  - *Context: Weightmaps are per-layer Landscape blend masks that tell the terrain material where each texture applies.*
- [ ] **(procgen)** As the developer, I want one hand-authored override POI or build plot to survive regeneration, so authored content is preserved.
- [ ] **(procgen)** As the developer, I want a PCG scatter proof for one generated region, so the presentation pipeline works.
- [ ] **(procgen)** As the developer, I want byte-identical regeneration from the same seed and version, so determinism is proven.
- [ ] **(world-map)** As the player, I want to select an army on the World Map and move it along hexes using movement points, so the strategic loop functions.
- [ ] **(world-map)** As the developer, I want turn resolution that consumes army orders and updates positions and ownership, so the strategic layer owns state.
- [ ] **(local-map)** As the player, I want a Local Map overlay with fog of war and order widgets, so I can issue squad and construction orders.
- [ ] **(local-map)** As the developer, I want per-squad and per-settlement order queues in the canonical store, consumed by the Landscape or an off-screen resolver.
- [ ] **(squad)** As the player, I want one squad with member actors and a Behavior Tree, so I can command and fight it in the Landscape.
- [ ] **(squad)** As the player, I want formation slots and marquee selection, so squad movement and commands are readable.
- [ ] **(squad)** As the developer, I want EQS cover scoring and a cover-quality enum, so squad members use cover.
- [ ] **(base-building)** As the player, I want to place a building on a predefined plot and see a construction schedule, so Local Map orders change the Landscape.
- [ ] **(base-building)** As the developer, I want construction state, a scaffold-to-finished swap, and destruction persisted by building ID, so built and removed objects stay consistent.
- [ ] **(tier-transition)** As the developer, I want one three-tier round-trip test — World Map → Local Map order → Landscape → back — with state assertions.
- [ ] **(performance)** As the developer, I want off-screen tiers abstracted to records, so the game does not simulate all three at once.
- [ ] **(traversal-ability)** As the player, I want a single-object Ultrahand grab using `UPhysicsHandleComponent::GrabComponentAtLocationWithRotation` and `SetTargetLocationAndRotation`, so I can move and rotate physics props.
- [ ] **(physics)** As the developer, I want a small physics prop set with tuned mass and damping and a rotation-offset hold, so grabbed objects do not snap or fight their constraints.
  - *Context: A rotation-offset hold keeps a grabbed object at a fixed angle relative to the grab point, preventing snap or spin.*
- [ ] **(world-streaming)** As the developer, I want a layered graybox — surface Landscape, sky-island Level Instances on a Runtime Data Layer, and a mesh cave layer — so I can test layer switching and streaming.
- [ ] **(landscape)** As the developer, I want the graybox to use the hybrid terrain pipeline, so cliffs and caves are meshes and the ground is a Landscape.
- [ ] **(traversal-ability)** As the player, I want a Recall prototype that records transforms at 20–30 Hz and rewinds with `ETeleportType::TeleportPhysics`, so I can test rewind on a few objects.
- [ ] **(persistence)** As the developer, I want a delta-save prototype for moved and built objects, so I can measure save size and load time before content scale.
- [ ] **(testing)** As the developer, I want one traversal route that exercises the v1 traversal verbs together, so the verbs are tested as a system.
- [ ] As a developer, I want a repeatable five-to-ten-minute playtest session with reset, spawn, timer, and a feedback form.
- [ ] As a developer, I want three to five fresh playtests and notes on where players got bored, confused, or delighted.
- [ ] As a developer, I want a prototype postmortem: what was fun, what was not, and what to keep or kill.
- [ ] **Gate:** Core-loop go/no-go. If it is not fun, iterate or pivot; do not build content or production architecture to rescue it.
- [ ] **Decision:** Keep, pivot, or kill the core loop based on playtests.
- [ ] **Decision:** Which prototype code, if any, survives. Default to rewriting; prototypes are disposable.
- [ ] **Decision:** MVP definition for the vertical slice — the smallest set of systems and content that represents the final game.

## Phase 4 — Architecture skeleton

**Goal:** stand up the permanent skeleton the slice will use, without gold-plating.

- [ ] **Decision:** GAS versus a custom action system, made after the prototype proves the combat feel. Weigh ability depth, buffs/debuffs, replication, C++ tolerance, and iteration speed.
- [ ] **Decision:** Attribute/stat model — stored base attributes, recomputed derived stats, and the damage-mitigation formula.
- [ ] **Decision:** Save model — slots, autosave triggers, world state versus player state, and migration policy.
- [ ] **Decision:** Inventory ownership and item composition — Controller inventory plus Pawn equipment, with items built from data fragments rather than a deep class hierarchy.
- [ ] **Decision:** Progression model — XP/levels, skill-use, or a hybrid; keep numbers bounded.
- [ ] **Decision:** Data-driven boundaries — what is authored in data versus code, and the ID/naming conventions.
- [ ] **Decision:** Modding/plugin boundaries, if mod support is in scope.
- [ ] As a developer, I want the responsibilities of GameMode, GameState, PlayerController, PlayerState, and GameInstance documented and implemented.
- [ ] As a developer, I want subsystems for cross-cutting services (save, audio, quests, economy) with the correct lifetimes.
- [ ] As a developer, I want event dispatchers and interfaces for one-to-many signals; no routine `Get All Actors of Class`.
- [ ] As a developer, I want data-driven definitions (DataAssets/DataTables) for items, enemies, abilities, and quests, with soft references where required.
- [ ] As a developer, I want save schema v1 with `SchemaVersion`, stable IDs, async saves, a backup slot, and a tested migration path.
- [ ] As a developer, I want modular boundaries (Game Features/plugins) before the system count grows, if the design needs them.
- [ ] As a developer, I want automation tests for boot, save/load round-trip, and damage/stat math.
- [ ] As a developer, I want default map, game mode, input, rendering baseline, and packaging settings configured once and versioned.
- [ ] **(architecture)** As the developer, I want the CMC/GAS boundary finalized — CMC owns movement integration, GAS owns activation, costs, and cooldowns — so traversal abilities do not duplicate movement logic.
- [ ] **(combat)** As the developer, I want every combat move implemented as a GAS ability or a component ability with attributes, costs, cooldowns, and gameplay tags.
- [ ] **(melee)** As the developer, I want one damage pipeline with sweeping melee traces, montage-driven hit windows, multi-hit prevention, and directional hit reactions.
- [ ] **(ranged)** As the developer, I want aim-mode camera and time dilation, line-trace target validation, projectile arrows, and a reticle/aim-assist layer.
- [ ] **(combat)** As the developer, I want enemy combat AI on Behavior Trees, EQS spacing, and StateTree states, with the token manager feeding attack permissions.
- [ ] **(combat)** As the developer, I want enemy archetypes and combat traits authored as data, with one required counter per archetype and daze-suppresses-immunity.
  - *Context: Daze is a stun-like state; while dazed, a captain's immunities are temporarily disabled.*
- [ ] **(combat)** As the developer, I want melee, ranged, and stealth postures to switch cleanly without dropping the combo or breaking the camera.
- [ ] **(testing)** As the developer, I want a combat automation harness for ability costs, cooldowns, token logic, and melee/ranged transitions.
- [ ] **(spellcasting)** As the developer, I want a data-driven `SpellDef` schema covering delivery, casting type, resource cost, cooldown, primer/detonator tags, effects, and ICD.
- [ ] **(spellcasting)** As the developer, I want each spell implemented as a GAS ability that fires one or more GameplayEffects and owns its cost/cooldown.
- [ ] **(reaction)** As the developer, I want a reaction table keyed by element and status, with tag checks, primer removal, and a per-ability ICD.
- [ ] **(spellcasting)** As the developer, I want delivery handlers for instant, projectile, beam/channel, cone, ground AoE, self/target buff, construct, summon, and chain.
- [ ] **(cc)** As the developer, I want a per-target crowd-control component tracking category, application count, duration scaling, immunity, and breakbar state.
- [ ] **(spellcasting)** As the developer, I want ability-bar hooks for cooldowns, charges, cast/channel bars, aura tints, and the ultimate meter.
- [ ] **(testing)** As the developer, I want spell-system automation for reaction coverage, CC diminishing returns, ultimate build/spend, and save/load.
- [ ] **(style)** As the developer, I want a style-profile schema per domain: post-process materials, priority, blend radius, MPC parameters, stencil ranges, distance thresholds, and quality toggles.
- [ ] **(rendering)** As the developer, I want the post-process stack configured with Blendables, priority ordering, unbound/bound volumes, and the After-Tonemapping location.
- [ ] **(rendering)** As the developer, I want style assignment through per-object stencil, per-region volumes/Data Layers/RVT, per-distance masks, and Material Parameter Collections.
- [ ] **(rendering)** As the developer, I want an optional `ISceneViewExtension`/RDG custom-pass scaffold for a multi-pass painterly filter, isolated behind a quality toggle.
- [ ] **(rendering)** As the developer, I want temporal-stability rules enforced: motion vectors where needed, world-space noise, and TSR settings verified with the visualize modes.
- [ ] **(vfx)** As the developer, I want a Niagara style library and shared watercolor material functions, with flow-map/UV-drift and edge-darkening controls.
- [ ] **(testing)** As the developer, I want visual-regression, style-coverage, temporal-stability, and GPU-budget tests for the rendering stack.
- [ ] **(items)** As the developer, I want a full item schema: definition, runtime instance, traits, effects, durability, parents, generation, and seed.
- [ ] **(crafting)** As the developer, I want a transactional reforge service — validate, compute, preview, commit — so a failed preview never consumes inputs.
- [ ] **(genetics)** As the developer, I want inheritance channels with explicit probabilities, dominance, mutation, and generation caps.
- [ ] **(items)** As the developer, I want effect composition with slots, power budgets, stack caps, and conflict groups.
- [ ] **(crafting)** As the developer, I want preview data that the UI can render: odds, inherited effects, conflicts, costs, and durability.
- [ ] **(persistence)** As the developer, I want lineage records with stable parent IDs, schema versioning, and a pruning policy.
- [ ] **(testing)** As the developer, I want inheritance-probability, anti-exploit, and reforge-transaction tests.
- [ ] **(crafting)** As the developer, I want the full ingredient/pattern schema: tags, values, quality, traits, exclusions, priorities, and output rules.
- [ ] **(crafting)** As the developer, I want the matcher pipeline — filter exclusions, validate requirements, score, choose priority, fallback — as one tested service.
- [ ] **(items)** As the developer, I want crafted outputs to feed the existing item-genetics/durability system, not a second item model.
- [ ] **(crafting)** As the developer, I want discovery gates and journal hooks for unknown patterns and unknown effects.
- [ ] **(ui)** As the developer, I want preview data for tags/values, predicted pattern, quality/effects, competing uses, and conflict warnings.
- [ ] **(persistence)** As the developer, I want ingredient instances, discovered patterns, and crafted lineage saved and versioned.
- [ ] **(testing)** As the developer, I want tag-coverage, pattern-reachability, dominance, and deterministic-transaction tests.
- [ ] **(movement)** As the developer, I want custom movement modes for each approved traversal verb, with `GetMaxSpeed()` and `GetMaxAcceleration()` overrides, so speeds and accelerations are mode-specific.
- [ ] **(world-streaming)** As the developer, I want World Partition cell size, loading range, HLOD layers, and Data Layers configured for the target map, so streaming stays stable at glide speed.
- [ ] **(landscape)** As the developer, I want the Landscape material routed through Runtime Virtual Texturing, with Nanite cliffs and caves, PCG scatter, water, and sky atmosphere wired in a test cell, so the visual pipeline is proven.
- [ ] **(animation)** As the developer, I want Motion Matching or blend-space locomotion plus Motion Warping hooks, so ground and traversal animation share one stack.
- [ ] **(stamina)** As the developer, I want stamina costs and regeneration curves per movement mode stored as tunable data, so climb, glide, and sprint budgets are easy to change.
- [ ] **(persistence)** As the developer, I want save versioning, migrations, backup slots, and off-thread autosave, so dynamic world state survives patches.
- [ ] **(traversal-ability)** As the developer, I want Ascend implemented as an upward trace plus a swept teleport, so vertical traversal is reliable.
  - *Context: Ascend is the TotK ability that lifts the player through a ceiling to the surface above.*
- [ ] **(traversal-ability)** As the developer, I want Fuse implemented as attachment plus data composition, so combined objects carry their stats.
  - *Context: Fuse is the TotK ability that merges two objects into one, combining their properties.*
- [ ] **(performance)** As the developer, I want a repeatable streaming and frame-time benchmark, so regressions are caught before they compound.
- [ ] **(world-state)** As the developer, I want canonical records for hexes, regions, settlements, armies, squads, units, buildings, and monster spawns, with schema versioning and migrations.
- [ ] **(procgen)** As the developer, I want a full generator contract with stable IDs, versioned parameters, override merge, and delta saves.
- [ ] **(procgen)** As the developer, I want generated region-border and cell meshes baked to static meshes, so Nanite, Lumen, and instancing work.
- [ ] **(procgen)** As the developer, I want the offline bake → import → Data Layer/Level Instance pipeline documented and repeatable.
- [ ] **(validation)** As the developer, I want multi-seed validation and golden-seed snapshots in CI, so generator changes cannot silently break worlds.
- [ ] **(performance)** As the developer, I want generation time, memory, and cook-time budgets measured, so the pipeline stays viable.
- [ ] **(voronoi)** **Decision:** Whether weighted or constrained Voronoi is needed for territory catchments; default to plain Voronoi until it is proven insufficient.
  - *Context: A catchment is the territory a settlement controls or draws resources from; weighted Voronoi lets each seed's influence vary; constrained Voronoi fixes borders to terrain.*
- [ ] **(world-map)** As the developer, I want A* over the hex graph with per-ground-type costs and per-turn movement points.
- [ ] **(world-map)** As the developer, I want fog-of-war state and region ownership stored on the canonical records, not in map-specific actors.
- [ ] **(local-map)** As the developer, I want the Local Map to render from the same records as the Landscape, with no separate simulation.
- [ ] **(tier-transition)** As the developer, I want the tier transition contract documented: which IDs are passed, what is written back, and what resets.
- [ ] **(squad)** As the developer, I want squad and army persistence boundaries fixed: army owns squads, squad owns members, members own health and equipment.
- [ ] **(base-building)** As the developer, I want the navmesh strategy fixed: predefined plots, `NavModifierVolume`, Dynamic Modifiers Only, and “Can Ever Affect Navigation” rules.
- [ ] **(strategic-ai)** As the developer, I want strategic AI to use Behavior Trees and EQS at lower fidelity, so it shares tooling with tactical AI.
- [ ] **(roguelike)** As the developer, I want the full run lifecycle and meta-progression (start/end, death/retry, unlocks, persistent knowledge) saved and versioned.
- [ ] **(faction-sim)** As the developer, I want the full faction simulation: goals, encroachment, infrastructure, frontier control, armies, relations, deterministic tick, and save.
- [ ] **(faction-sim)** As the developer, I want faction infrastructure (camps, tunnels, roads, outposts, farms) spawned, upgraded, and destroyed by the simulation and persisted.
- [ ] **(faction-sim)** As the developer, I want faction standing/reputation, alliances, and consequences integrated with the simulation, dialogue, and quests.
- [ ] **(faction-sim)** As the developer, I want faction quests and events (aid, sabotage, defend, capture, raid, construction) integrated with the simulation, rewards, and dialogue.
- [ ] **(dynamic-world)** As the developer, I want full dynamic POI state for towns and caves: ownership, tier, population, purpose, upgrades, destruction, repopulation, quests, spawns, and save.
- [ ] **(engagement)** As the developer, I want the full engagement-tier system: influence actions, command unlocks, army/build-queue access, and UI hooks.
- [ ] **(party)** As the developer, I want the full NPC party system: roster, roles, AI, equipment, leveling, recruitment, approval/banter, injury/permadeath, and save.
- [ ] **(co-op)** As the developer, I want the full co-op architecture (replication/authority, lobby/drop-in, save, UI, network tests) if co-op is implemented.
- [ ] **(difficulty)** As the developer, I want the full threat-budget/difficulty service: party size/composition, roguelike modifiers, faction state, player power, and encounter composition, with no HP-only scaling.
- [ ] **(run-modifier)** As the developer, I want the full run modifier/event system: boons, curses, faction interventions, random events, risk/reward, and save.
- [ ] **(exploration)** As the developer, I want the full exploration/discovery/navigation/fast-travel system: POIs, secrets, lore, resources, recruits, map fog, compass/minimap/waypoints, fast travel.
- [ ] **(telemetry)** As the developer, I want full telemetry for runs, faction control, party composition, and co-op outcomes.
- [ ] **(testing)** As the developer, I want round-trip tests for run, faction, POI, party, and co-op state.
- [ ] **(testing)** As the developer, I want round-trip automation tests for save/load, tier transitions, and construction persistence.

## Phase 5 — Combat and abilities (real implementation)

**Goal:** replace the prototype combat with the chosen production stack and prove it is legible and satisfying.

- [ ] As a player, I want a basic attack with readable wind-up, hit, recovery, and cancel windows.
- [ ] As a player, I want to take damage, die, respawn, and understand why.
- [ ] As a player, I want at least one ability with a resource cost, cooldown, and visible effect.
- [ ] As a player, I want buffs and debuffs that visibly change a fight.
- [ ] As a developer, I want hit detection/traces, damage types, resistances, and a damage log for debugging.
- [ ] As a developer, I want a training dummy and training room for tuning.
- [ ] As a developer, I want animation montages, notifies, hitstop, and impact feedback wired to the real system.
- [ ] As a developer, I want a balance spreadsheet for HP, damage, cooldowns, and scaling before tuning in-engine.
- [ ] As a developer, I want automation tests for the damage formula and ability activation/cooldown rules.
- [ ] As a player, I want at least two viable combat approaches, so the system has a decision in it.
- [ ] **(movement)** As the player, I want combat to respect traversal state — no climbing during an attack, no gliding while staggered — so modes do not conflict.
- [ ] **(animation)** As the developer, I want montage and state transitions between combat and traversal, so root motion and the CMC do not fight.
- [ ] **(physics)** As the developer, I want knockback and grabbed-object interactions tested against combat, so Chaos does not destabilize the character.
- [ ] **(squad)** As the player, I want squad combat with morale, suppression, cover, and reinforcement, so battles use the tactical systems.
- [ ] **(squad)** As the developer, I want squad casualties written back to the army record, so strategic strength reflects battle losses.
- [ ] **(party)** As the player, I want party roles and synergies in combat (tank/DPS/support/controller, combo abilities, friendly fire, revive), so NPC parties are more than extra bodies.
- [ ] **(co-op)** As the player, I want co-op combat (player revive, shared aggro, difficulty scaling, loot/XP), so co-op is a real mode.
- [ ] **(squad)** As the player, I want faction battles and squad density with allied NPC parties and enemy squads, so battles feel large and legible.
- [ ] **(boss)** As the player, I want boss/elite encounters with phases, telegraphs, arena gates, checkpoints, and rewards, so runs have climaxes.
- [ ] **(stealth)** As the player, I want stealth/detection (vision, noise, alert states, takedowns, cover, distractions), so the SoM/War fantasy includes stealth.
- [ ] **(input)** As the player, I want lock-on/target switching that works in solo, party, and co-op combat.
- [ ] **(base-building)** As the developer, I want destructible cover and buildings to update navigation and canonical state, so combat and construction interact correctly.
- [ ] **(melee)** As the player, I want the full melee move set — attack chain, counter, double counter, dodge, stun/flurry, vault stun, execution, ground execution, drain, and brutalize.
  - *Context: Brutalize is a slow, high-damage finisher that leaves the player exposed.*
- [ ] **(melee)** As the developer, I want the Hit Streak to charge at 8 consecutive hits (5 with the Blade Master upgrade), Might to reset on damage or miss, and counters to restore 1 Elf-shot.
  - *Context: Blade Master is an upgrade that lowers the Hit Streak threshold from 8 hits to 5. Might is the execution resource built during combat; it resets on damage, a miss, or combat exit. The Hit Streak is the separate live counter.*
- [ ] **(melee)** As the player, I want Wraith Stun, Wraith Flash, Wraith Burn, Combat Drain, and Execution gated by the charged Hit Streak, so the meter has spendable payoffs.
  - *Context: In Shadow of Mordor, a charged Hit Streak unlocks Execution and the Wraith abilities; Might is a separate resource for some finishers.*
- [ ] **(ranged)** As the player, I want aim mode with Focus slow-motion, hold-to-charge shots, and limited Elf-shot, so ranged combat is a resource decision.
- [ ] **(ranged)** As the player, I want Shadow Strike, Mighty Shot, Chain of Shadows, Freeze Pin, and Quick Throw, with each ability's cost and target rule visible.
  - *Context: Shadow Strike teleports to a target; Mighty Shot is a charged arrow; Chain of Shadows hits several targets; Freeze Pin immobilizes; Quick Throw is a fast ranged attack.*
- [ ] **(combat)** As the player, I want enemy archetypes that each demand a specific answer — archer, defender, hunter, berserker — mixed one or two at a time.
- [ ] **(combat)** As the player, I want captain combat traits with discoverable counters and the rule that daze temporarily suppresses immunities.
- [ ] **(combat)** As the developer, I want difficulty set by enemy composition, timing windows, and token count, not HP scaling.
- [ ] **(animation)** As the developer, I want Motion Warping for strike/execution alignment, directional hit reactions, and hitstop tuned on counters and finishers.
- [ ] **(input)** As the player, I want input buffering, a timed double-counter, and a clean aim-mode toggle that does not drop the combo.
- [ ] **(testing)** As the developer, I want combat-feel playtests, token-cap tests, and melee/ranged mode-transition tests before content scale.
- [ ] **(spellcasting)** As the player, I want fire-and-forget, concentration/channel, and charge spells to behave differently, with interrupts and cancel windows.
- [ ] **(spellcasting)** As the player, I want instant, projectile, beam, cone, ground-AoE, self/target buff, construct, summon, and chain deliveries, each with line-of-sight and targeting rules.
- [ ] **(spellcasting)** As the developer, I want every spell's cost, cooldown, charge time, and resource tier defined in data, not hard-coded in Blueprint graphs.
- [ ] **(spellcasting)** As the player, I want visible elemental statuses and aura tints on affected targets, so reactions are readable before they trigger.
- [ ] **(reaction)** As the player, I want a three-element reaction matrix — prime, detonate, freeze/shatter, burn, shock — with combo type determined by the primer.
  - *Context: Prime applies an element; detonate consumes it. Freeze/shatter, burn, and shock are the reaction outcomes; the mapping of three elements to these outcomes is still unnamed.*
- [ ] **(cc)** As the player, I want crowd-control diminishing returns per category and a breakbar on elites/bosses instead of infinite stun-locks.
- [ ] **(spellcasting)** As the player, I want an ultimate state that transforms combat for a short window — slow time, empowered spells, or unlimited finishers — built from kills.
- [ ] **(spellcasting)** As the developer, I want roughly ten upgradeable spells rather than a large roster of weak ones, with upgrades modifying behavior instead of adding new buttons.
- [ ] **(animation)** As the developer, I want cast, channel, and charge animations with cancel windows and Motion Warping for spell-driven strikes/teleports.
- [ ] **(testing)** As the developer, I want spell tests for reaction coverage, ICD, CC diminishing returns, ultimate build/spend, and mode transitions.
- [ ] **(vfx)** As the player, I want watercolor-styled impact, magic, and ambient VFX with readable silhouettes and bounded opacity in combat.
- [ ] **(style)** As the player, I want the near-field combat layer to stay PBR-clear while the far field is painterly, so style never hides threat state.
- [ ] **(rendering)** As the developer, I want spell/combat VFX interactions with the style stack tested — distortion, bloom, overdraw, and screen-space effects.
- [ ] **(testing)** As the developer, I want combat-readability and temporal-stability tests with the full style and VFX stack active.
- [ ] **(durability)** As the player, I want combat actions to degrade equipment, with warnings before `Unusable`, so durability is felt but never surprising.
- [ ] **(items)** As the player, I want inherited abilities and effects to apply through GAS in combat, so reforged items change how fights play.
- [ ] **(economy)** As the developer, I want repair and reforge costs tuned against combat income, so maintenance is a real but not punishing sink.
- [ ] **(testing)** As the developer, I want combat durability and inherited-effect tests, including `Unusable` behavior.
- [ ] **(crafting)** As the player, I want crafted consumables and weapons usable in combat, with the bandage-vs-fire-bomb choice felt in a fight.
- [ ] **(crafting)** As the player, I want combat outcomes — part breaks, capture/defeat method, elite kills — to change which ingredient drops appear.
- [ ] **(economy)** As the developer, I want combat income tuned against ingredient scarcity, so crafting choices have weight.
- [ ] **(testing)** As the developer, I want combat crafting/drop tests, including competing-use and drop-channel coverage.
- [ ] **Gate:** Melee, ranged, and spell combat are legible and satisfying with placeholder art and the style stack active, and the chosen stack does not fight the design.

## Phase 6 — Slice-critical supporting systems

**Goal:** build only what the slice actually needs; defer everything else.

- [ ] **Decision:** CommonUI versus plain UMG, based on platform and menu complexity.
- [ ] **Decision:** Slice scope — which systems get a real version now, which get a placeholder, and which are deferred. Write the fake list down.
  - *Context: The fake list names systems intentionally stubbed or faked for the slice, so placeholders are not mistaken for finished work.*
- [ ] **Decision:** Whether inventory, progression, and quests are slice-critical or post-slice, based on whether they define the core experience.
- [ ] As a player, I want a HUD that shows what I need without clutter.
- [ ] As a player, I want a pause menu, settings (audio/graphics/input), and clear quit/restart behavior.
- [ ] As a player, I want a checkpoint or autosave and to resume exactly where I left off.
- [ ] As a player, I want to pick up, inspect, equip, and drop an item, if inventory is slice-critical.
- [ ] As a player, I want to gain a level or unlock and see the effect, if progression is slice-critical.
- [ ] As a player, I want to talk to one NPC and accept and complete one quest, if quests are slice-critical.
- [ ] As a developer, I want data-driven UI binding, so HUD changes do not require hard-coded casts.
- [ ] As a developer, I want all user-facing strings in `FText`, so localization does not require a rewrite.
- [ ] As a player, I want remappable input, subtitles, text scaling, and color-safe prompts from the start.
- [ ] **(ui)** As the player, I want a stamina wheel or bar that shows climb and glide costs, so traversal limits are legible.
- [ ] **(persistence)** As the player, I want a checkpoint or autosave that captures position, traversal state, and dynamic objects, so reloads are seamless.
- [ ] **(input)** As the player, I want context prompts for climbing, gliding, grabbing, and rewind, so the traversal verbs are discoverable.
- [ ] **(animation)** As the player, I want traversal animation transitions that match stamina and speed, so the character looks controlled.
- [ ] **(camera)** As the player, I want traversal-specific camera behavior for climbing, gliding, and riding, so each mode reads clearly.
- [ ] **(ui)** As the player, I want a combat HUD showing Hit Streak, Might, Elf-shot, Focus, and the active execution prompt, so the resource loop is legible.
- [ ] **(ui)** As the player, I want a reticle and aim UI, plus counter and red-dodge indicators on enemies, so melee and ranged prompts are unambiguous.
- [ ] **(input)** As the player, I want remappable melee/ranged controls and aim sensitivity, so the combat scheme fits the input device.
- [ ] **(persistence)** As the player, I want health, ammo, and ability unlocks to persist, while the transient Hit Streak resets on load.
- [ ] **(animation)** As the player, I want combat animation transitions that match the current weapon, posture, and movement state.
- [ ] **(ui)** As the player, I want an ability bar with cooldowns/charges, a cast/channel bar, an ultimate meter, and aura tints on primed targets.
- [ ] **(input)** As the player, I want spell-slot bindings and clean aim/ground-target controls for delivery types.
- [ ] **(persistence)** As the player, I want spell unlocks and loadouts to persist, while cooldowns and active cast state reset on load.
- [ ] **(spellcasting)** As the developer, I want a spell training dummy with resistances, immunities, and status hooks for tuning reactions and CC.
- [ ] **(ui)** As the player, I want HUD and menu styling consistent with the paper/watercolor treatment while staying readable over combat.
- [ ] **(style)** As the developer, I want a style-readability check for HUD, prompts, and damage feedback over the painterly far field and watercolor VFX.
- [ ] **(ui)** As the player, I want a reforge screen with base, similar-item, material, and tool slots, plus a preview of odds, inherited effects, conflicts, costs, and durability.
- [ ] **(ui)** As the player, I want item tooltips showing durability, lineage, inherited effects, and conflict warnings.
- [ ] **(persistence)** As the player, I want item instances and lineage records to save/load and migrate across versions.
- [ ] **(items)** As the player, I want reforge stations or tools placed in the world, so the recovery loop has a physical home.
- [ ] **(ui)** As the player, I want a crafting screen with ingredient slots, tag/value display, predicted pattern, estimated effects, competing uses, and “????” unknowns.
- [ ] **(ui)** As the player, I want ingredient tooltips and a discovery journal showing every known use and where the ingredient drops.
- [ ] **(persistence)** As the player, I want ingredient instances and discovered patterns saved and migrated.
- [ ] **(crafting)** As the player, I want crafting stations placed in the world, so crafting has a physical home.
- [ ] **(ui)** As the player, I want World Map, Local Map, and squad command UI to share one selection and order model, so commands behave identically in every tier.
- [ ] **(ui)** As the player, I want construction and order queues visible in the Local Map, so I can see what is in progress.
- [ ] **(tier-transition)** As the player, I want clear transition feedback and a reliable way to return to the strategic layer.
- [ ] **(persistence)** As the player, I want save/load to preserve armies, squads, buildings, and fog of war, not just the current character.
- [ ] **(party)** As the player, I want a party UI (roster, roles, equipment, leveling, commands, approval/banter).
- [ ] **(co-op)** As the player, I want co-op UI (lobby/invite, player list, revive, shared objectives, ping).
- [ ] **(faction-sim)** As the player, I want a faction map UI (control, influence, infrastructure, frontier, armies, relations).
- [ ] **(engagement)** As the player, I want an engagement-tier UI (influence actions vs. command mode, army/build-queue access).
- [ ] **(run-modifier)** As the player, I want a run modifier/event UI (boons, curses, risk/reward, faction interventions).
- [ ] **(dynamic-world)** As the player, I want a dynamic POI UI (town/cave state, upgrades, quests, ownership).
- [ ] **(exploration)** As the player, I want map/compass/minimap/waypoints/fast travel UI.
- [ ] **(onboarding)** As a new player, I want onboarding for the roguelike/faction/party/co-op loop.
- [ ] **(settings)** As the player, I want audio/settings/accessibility menus for the new systems.

## Phase 7 — Enemy AI and encounters

**Goal:** one enemy archetype that is fair, readable, and cheap enough to run.

- [ ] **Decision:** AI architecture — Behavior Tree, State Tree, finite state machine, or utility AI — matched to the number of enemies and decision complexity.
- [ ] **Decision:** Encounter design pattern — hand-placed encounters, a director, or both.
- [ ] As a player, I want enemies that perceive me, pursue, attack, and retreat believably.
- [ ] As a developer, I want one enemy archetype fully implemented before starting a second.
- [ ] As a developer, I want an AI Controller with a Behavior Tree or State Tree and a Blackboard, plus sight and hearing perception.
- [ ] As a developer, I want navigation, patrol/investigate/attack/flee states, and a fair telegraph for every attack.
- [ ] As a developer, I want basic spawn/encounter management, plus a director if the game needs pacing.
- [ ] As a developer, I want AI debug visualization and a decision-tick performance budget.
- [ ] As a developer, I want automation or smoke coverage for spawning and the basic state transitions.
- [ ] As a player, I want at least one encounter that teaches a mechanic without a text tutorial.
- [ ] **(landscape)** As the developer, I want navigation data to cover the hybrid terrain, so enemies can path across Landscape ground and mesh cliffs.
- [ ] **(performance)** As the developer, I want AI decision ticks and streaming tested with enemies active, so the open world stays inside the frame budget.
- [ ] **(strategic-ai)** As the player, I want enemy armies and towns to move, recruit, and contest territory on the World Map.
- [ ] **(squad)** As the player, I want enemy squads to use cover, suppression, and retreat, so battles are not target practice.
- [ ] **(performance)** As the developer, I want strategic AI tick budgets and off-screen resolution tested, so the World Map does not consume the tactical frame.
- [ ] **(faction-sim)** As the developer, I want faction strategic AI (goblin encroachment, human infrastructure, frontier battles, army goals, relations).
- [ ] **(dynamic-world)** As the developer, I want dynamic POI AI (town/cave state transitions, defenders, repopulation, quests).
- [ ] **(party)** As the developer, I want NPC party AI (follow, combat roles, revive, loot, banter, player commands).
- [ ] **(co-op)** As the developer, I want co-op enemy scaling and aggro.
- [ ] **(run-modifier)** As the developer, I want a run modifier/event director that places obstacles/help and risk/reward choices.
- [ ] **(difficulty)** As the developer, I want a difficulty director that feeds the threat budget from party size/composition, modifiers, and faction state.
- [ ] **(combat)** As the player, I want archers to seek vantage and line of sight, defenders to shield, hunters to punish counters, and berserkers to counter standard attacks.
  - *Context: A hunter enemy dodges and punishes reckless counters by striking during recovery.*
- [ ] **(combat)** As the developer, I want archetype behavior and counter rules to be data-driven and integrated with the token manager.
- [ ] **(spellcasting)** As the player, I want enemy casters to use the same ability system, with telegraphed casts, interrupts, and elemental affinities.
- [ ] **(cc)** As the player, I want enemy crowd control to respect diminishing returns or breakbars, so fights do not become stun-lock chains.
- [ ] **(crafting)** As the player, I want strong enemies to drop materials through multiple channels — part breaks, defeat method, rare drops — each feeding different patterns.
- [ ] **(testing)** As the developer, I want drop-table coverage tests ensuring every strong enemy's materials have multiple uses.
- [ ] **Gate:** A fresh player can fight the enemy and understand its intent.

## Phase 8 — Vertical slice

**Goal:** one narrow segment at near-shipping quality that proves the content and build pipeline.

- [ ] **Decision:** Art style and asset pipeline locked (in-house, marketplace, or outsourced; shader and material budget).
- [ ] **Decision:** Animation pipeline and outsourcing plan.
- [ ] **Decision:** Audio direction and pipeline (placeholder versus final; middleware if any).
- [ ] **Decision:** Release platform/store and certification requirements.
- [ ] As a developer, I want a written slice definition: start state, five to fifteen minutes of play, end state, and the exact systems and content included.
  - *Context: The slice may use a shortened run; define the representative run segment and its start/end state, not the full campaign.*
- [ ] As a developer, I want the fake list written down (main menu, story text, settings, icons, audio, localization) and visible to playtesters.
- [ ] As a player, I want the slice to include real controls, real character and enemy art, a real HUD and pause menu, a working save/checkpoint, and an installable build.
- [ ] As a developer, I want one complete content pipeline pass: model → material → animation → VFX → audio → data → level → build.
- [ ] As a developer, I want a performance capture on target hardware, fixing only budget-breaking issues.
- [ ] As a developer, I want a clean-machine cook/package and a packaged-build playthrough.
- [ ] As a developer, I want an external playtest with strangers, using structured feedback.
- [ ] **(landscape)** As the developer, I want the slice's terrain built through the hybrid Landscape plus Nanite-mesh pipeline at final quality.
- [ ] **(world-streaming)** As the developer, I want the slice to stream cleanly during climbing and gliding, with no hitches at cell borders.
- [ ] **(movement)** As the player, I want every shipped traversal verb playable end-to-end in the slice.
- [ ] **(traversal-ability)** As the player, I want the chosen TotK-style ability to work against the slice's real geometry, not only the prototype props.
- [ ] **(persistence)** As the developer, I want save/load of dynamic objects verified in the slice.
- [ ] **(performance)** As the developer, I want packaged-build traversal profiling on target hardware.
- [ ] **(procgen)** As the developer, I want the slice to use one generated region with multiple biomes and POIs, so generation is represented in the vertical slice.
- [ ] **(validation)** As the developer, I want the slice seed to pass connectivity, POI, and buildability validation.
- [ ] **(procgen)** As the developer, I want one authored override in the slice to prove regeneration preserves it.
- [ ] **(world-map)** As the player, I want the slice to include two hexes, one army, and one town, so the strategic loop is visible.
- [ ] **(local-map)** As the player, I want to issue a build order and a squad move from the Local Map in the slice.
- [ ] **(landscape)** As the player, I want to drop into the slice Landscape, see the construction scaffold and squad, fight one monster spawn, and return.
- [ ] **(tier-transition)** As the developer, I want the slice round-trip to preserve state and load within the transition budget.
- [ ] **(testing)** As the developer, I want the slice's World Map → Local Map → Landscape → World Map round-trip in automation.
- [ ] **(roguelike)** As the player, I want the slice to include one complete run: seed, faction front, dynamic town/cave, NPC party, co-op scaling, run modifier, exploration/fast-travel reward, squad battle, and boss/elite climax.
- [ ] **(faction-sim)** As the player, I want the slice to include one goblin-vs-human frontier with encroachment/infrastructure and player influence.
- [ ] **(dynamic-world)** As the player, I want the slice to include one town and one cave that change state.
- [ ] **(engagement)** As the player, I want the slice to include the low/high engagement switch.
- [ ] **(party)** As the player, I want the slice to include one NPC party with roles, AI, and leveling.
- [ ] **(co-op)** As the player, I want the slice to include a two-player co-op test with threat-budget scaling.
- [ ] **(run-modifier)** As the player, I want the slice to include one run modifier/obstacle/help.
- [ ] **(exploration)** As the player, I want the slice to include one exploration/fast-travel reward loop.
- [ ] **(difficulty)** As the developer, I want the slice to validate threat-budget scaling across solo, NPC party, and co-op.
- [ ] **(onboarding)** As a new player, I want the slice to onboard the roguelike/faction/party/co-op loop.
- [ ] **(melee)** As the player, I want the slice's melee loop to include attack, counter, dodge, stun/flurry, execution, and the charged Hit Streak.
- [ ] **(ranged)** As the player, I want the slice's ranged loop to include aim slow-motion, a charged shot, Elf-shot costs, and Shadow Strike.
- [ ] **(combat)** As the player, I want a slice enemy mix that requires each counter — at least a berserker, a defender, and an archer.
- [ ] **(testing)** As the developer, I want slice combat automation for token cap, streak reset, ranged hit registration, and mode transitions.
- [ ] **(spellcasting)** As the player, I want the slice to include one projectile spell, one primer/detonator pair, and one ultimate activation.
- [ ] **(reaction)** As the player, I want a slice reaction to fire on a real enemy with the correct element and visual feedback.
- [ ] **(testing)** As the developer, I want slice spell automation for cost/cooldown, ICD, reaction triggers, and ultimate state.
- [ ] **(style)** As the player, I want the slice to show the realistic near field, the impressionist far field, and watercolor VFX together.
- [ ] **(testing)** As the developer, I want slice visual-regression, temporal-stability, and GPU-budget checks for the style stack.
- [ ] **(items)** As the player, I want the slice to include one item family, a durability break, a reforge with inheritance, and save/load.
- [ ] **(testing)** As the developer, I want slice durability/reforge automation covering determinism, lineage, and costs.
- [ ] **(crafting)** As the player, I want the slice to include one competing-output ingredient, one alpha-monster multi-use drop, and a previewed craft.
- [ ] **(testing)** As the developer, I want slice crafting automation for tag matching, priority, fallback, and save/load.
- [ ] **Gate:** Vertical-slice review — does this represent the final game, and is the pipeline repeatable? Re-scope before production.
- [ ] **Decision:** Production content volume (zones, quests, enemies, items, playtime) and the cut list.
- [ ] **Decision:** Which prototype or slice systems to replace now, before content scale makes the debt expensive.

## Phase 9 — Production systems and content breadth

**Goal:** deepen the systems the game needs and build the content pipeline, in dependency order.

- [ ] **Decision:** Production mix — confirm the handcrafted/procedural split chosen in Phase 0 and set the PCG content budget; if procedural is core, prototype a tiny version in Phase 3.
- [ ] **Decision:** Quest and dialogue authoring approach — custom DataTable plus manager, an engine plugin, or a marketplace tool.
- [ ] **Decision:** Faction/economy depth — how faction simulation, infrastructure, and the economy feed the core loop.
- [ ] **Decision:** Content pipeline ownership — what is made in-house, what is outsourced, and what is bought.
- [ ] **Decision:** Localization timing and the final language list.
- [ ] As a player, I want a full inventory and equipment loop with meaningful choices, if in scope.
- [ ] As a developer, I want itemization data: base items, affixes, rarity, loot tables, and smart-loot rules.
- [ ] As a player, I want progression with an XP curve, perks or talents, respec, and bounded numbers, if in scope.
- [ ] As a player, I want quests with available/active/complete/turned-in/failed states, objectives as data, and saved progress.
- [ ] As a player, I want dialogue with data-driven lines, flags, conditions, and choices that have consequences.
- [ ] As a player, I want factions, reputation, and consequences, if in scope.
- [ ] As a player, I want an economy with sources, sinks, prices, and inflation controls, if in scope.
- [ ] As a player, I want paced encounters and a director or equivalent pacing system, if in scope.
- [ ] As a player, I want a handcrafted or procedurally generated world that supports the core loop.
- [ ] As a developer, I want content-authoring tools and validation for missing IDs, broken references, and bad data.
- [ ] As a developer, I want automation coverage to grow with each new system, so regressions are caught early.
- [ ] As a developer, I want a regular external playtest cadence through production, not only at milestones.
- [ ] **(landscape)** As the developer, I want the full world's terrain built from modular kits and PCG through the hybrid pipeline.
- [ ] **(world-streaming)** As the developer, I want cell, HLOD, and Data Layer budgets validated at full map scale.
- [ ] **(traversal-ability)** As the developer, I want remaining TotK-style abilities implemented only where they serve the core loop.
- [ ] **(persistence)** As the developer, I want dynamic world state saved as deltas at content scale.
- [ ] **(performance)** As the developer, I want streaming, memory, and cook-time checks at every content milestone.
- [ ] **(movement)** As the player, I want traversal to remain readable and useful across every biome and layer.
- [ ] **(procgen)** As the player, I want all World Map regions generated with biomes, rivers, towns, resources, and factions.
- [ ] **(voronoi)** As the player, I want settlement catchments and territory boundaries derived from Voronoi cells.
- [ ] **(procgen)** As the player, I want Local Map projections for every region from the same records.
- [ ] **(procgen)** As the player, I want Landscape heightmaps and weightmaps for every region, with erosion and river carving.
- [ ] **(procgen)** As the player, I want POI and encounter placement rules with authored overrides.
- [ ] **(validation)** As the developer, I want fairness, connectivity, and buildability validation across all regions and seeds.
- [ ] **(world-map)** As the player, I want multiple regions, towns, armies, and fog-of-war states on the World Map.
- [ ] **(squad)** As the player, I want multiple squad types, abilities, and equipment loadouts.
- [ ] **(base-building)** As the player, I want a building roster with upgrades and prerequisites.
- [ ] **(strategic-ai)** As the player, I want factions that recruit, expand, defend, and fight over territory.
- [ ] **(faction-sim)** As the player, I want multiple faction types, infrastructure tiers, frontier states, and faction relations.
- [ ] **(dynamic-world)** As the player, I want more town and cave archetypes with different state transitions, upgrades, and quests.
- [ ] **(party)** As the player, I want more companions, roles, party compositions, and banter.
- [ ] **(run-modifier)** As the player, I want more run modifiers, events, obstacles, and help across the content.
- [ ] **(exploration)** As the player, I want more POIs, secrets, lore, and fast-travel rewards across the world.
- [ ] **(co-op)** As the developer, I want co-op content and balance tuned for the same encounters as solo/party play.
- [ ] **(economy)** As the player, I want resources from towns and captured points to fund armies and construction.
- [ ] **(local-map)** As the player, I want the full Local Map order and construction workflow, with off-screen resolution.
- [ ] **(tier-transition)** As the player, I want every tier transition to feel deliberate and preserve all relevant state.
- [ ] **(combat)** As the player, I want additional enemy archetypes and captain combat traits across the content, each with a discoverable counter.
- [ ] **(melee)** As the player, I want melee ability upgrades and weapon progression that change how the core verbs are used.
- [ ] **(ranged)** As the player, I want ranged ability upgrades and elemental arrow options, with clear costs and tradeoffs.
- [ ] **(combat)** As the player, I want difficulty modes and New Game+ built from composition, timing, and token changes, not HP inflation.
- [ ] **(combat)** As the player, I want encounter compositions that mix archetypes and force different counter sequences.
- [ ] **(spellcasting)** As the player, I want the full spell roster — roughly ten upgradeable spells across three elements — with clear roles and costs.
- [ ] **(reaction)** As the player, I want the full reaction matrix implemented and surfaced through intel and aura feedback.
  - *Context: Intel is a codex or bestiary that records discovered reactions; aura feedback shows the element on the target.*
- [ ] **(spellcasting)** As the player, I want enemy casters, elemental resistances, and immunities that force spell choice.
- [ ] **(cc)** As the player, I want elite and boss breakbars tuned across the content, with diminishing returns on regular enemies.
- [ ] **(style)** As the player, I want regional and biome-specific far-field treatments that stay coherent with the near-field style.
- [ ] **(rendering)** As the developer, I want far-field HLOD and impostors tuned so the painterly filter has the right input geometry.
- [ ] **(vfx)** As the player, I want the full watercolor VFX library — impacts, abilities, ambience, weather — with consistent materials.
- [ ] **(testing)** As the developer, I want style-coverage checks so every tagged object and region resolves to a style profile.
- [ ] **(items)** As the player, I want additional item families, materials, traits, and effects that create meaningfully different reforge outcomes.
- [ ] **(crafting)** As the player, I want reforge tiers, tools, and stations that unlock stronger inheritance and legacy progression.
- [ ] **(genetics)** As the player, I want mutation, rare traits, and deeper lineage to produce surprising but bounded results.
- [ ] **(economy)** As the developer, I want material, item, durability, and reforge costs balanced across the content.
- [ ] **(crafting)** As the player, I want more ingredient families, patterns, drop tables, and discovery content across the world.
- [ ] **(items)** As the player, I want trait and quality variety that makes ingredient choice matter beyond the recipe.
- [ ] **(economy)** As the developer, I want drop rates and scarcity balanced against competing uses and player progression.
- [ ] **(testing)** As the developer, I want dead-ingredient and dominance audits across the full crafting content.
  - *Context: A dead ingredient has no viable use; a dominant recipe makes alternatives pointless. The audit finds both.*
- [ ] **Gate:** Alpha — feature-complete. No new systems after this point; only content, balance, and fixes.

## Phase 10 — Content scale

**Goal:** produce enough content to fill the target playtime without padding or repetition.

- [ ] As a player, I want enough zones, encounters, and rewards for the target playtime.
- [ ] As a developer, I want all levels built to the slice's quality bar.
- [ ] As a player, I want enemy variety and encounter compositions that test different skills.
- [ ] As a player, I want item, loot, and progression content that supports build variety.
- [ ] As a player, I want quests, dialogue, and narrative content that pay off the premise.
- [ ] As a player, I want audio, music, VFX, and animation at final quality.
- [ ] As a player, I want difficulty options and accessibility settings that fit the game.
- [ ] As a developer, I want localization completed and integrated, if in scope.
- [ ] As a developer, I want performance and memory checks at every content milestone, not only at the end.
- [ ] As a developer, I want external playtests to catch comprehension and fun problems, not just bugs.
- [ ] **(landscape)** As the developer, I want PCG scatter baked and hand-tuned rather than generated at runtime.
- [ ] **(world-streaming)** As the developer, I want HLOD and loading ranges tuned for final map density and glide speed.
- [ ] **(performance)** As the developer, I want memory and streaming profiles across the full map, not spot checks.
- [ ] **(movement)** As the player, I want traversal stamina, speeds, and camera tuned per biome and layer.
- [ ] **(procgen)** As the developer, I want many-seed generation and biome variety tested, so the generator holds up beyond the golden seeds.
- [ ] **(validation)** As the developer, I want large-scale validation and golden-seed regression runs, so content-scale generation stays correct.
- [ ] **(procgen)** As the developer, I want PCG scatter baked and border meshes optimized, so generated worlds render within budget.
- [ ] **(performance)** As the developer, I want generation, cook, memory, and load budgets measured at full scale.
- [ ] **(world-map)** As the developer, I want full map and region content with strategic balance across starts, distances, and chokepoints.
- [ ] **(faction-sim)** As the developer, I want many-faction and many-seed simulation/balance, so the frontier holds up beyond one scenario.
- [ ] **(roguelike)** As the developer, I want many-run and meta-progression balance, so runs stay varied without runaway power.
- [ ] **(party)** As the developer, I want party-composition and co-op scaling validated across the full enemy/encounter set.
- [ ] **(dynamic-world)** As the developer, I want dynamic POI variety and state-transition validation at content scale.
- [ ] **(exploration)** As the developer, I want exploration reward distribution validated, so discovery stays meaningful.
- [ ] **(squad)** As the developer, I want squad variety and battle compositions that test different tactical answers.
- [ ] **(base-building)** As the developer, I want building variety and construction balance across the full tech and economy curve.
- [ ] **(strategic-ai)** As the developer, I want AI difficulty and behavior tuned across regions and game phases.
- [ ] **(economy)** As the developer, I want the economy balanced so armies and construction compete for the same resources.
- [ ] **(performance)** As the developer, I want large battles and many World Map armies tested together within budget.
- [ ] **(combat)** As the developer, I want encounter compositions and difficulty tuned across the full enemy and ability set.
- [ ] **(performance)** As the developer, I want large crowd combat — maximum tokens, archetypes, and hit effects — profiled in a packaged build.
- [ ] **(melee)** As the developer, I want melee and ranged damage, cost, and cooldown balance validated across the full enemy mix.
- [ ] **(spellcasting)** As the developer, I want spell damage, cost, cooldown, and upgrade balance validated across the full enemy mix.
- [ ] **(performance)** As the developer, I want spell VFX, projectiles, beams, and AoE effects profiled in packaged-build combat.
- [ ] **(testing)** As the developer, I want reaction-matrix coverage tested against every enemy type and immunity.
- [ ] **(performance)** As the developer, I want style-stack quality tiers validated, including half-res/async far-field filtering and disabled-style fallbacks.
- [ ] **(vfx)** As the developer, I want watercolor VFX overdraw measured in the densest combat scenes.
- [ ] **(style)** As the developer, I want style consistency validated across biomes, regions, and lighting conditions.
- [ ] **(items)** As the developer, I want item-family, material, and trait combinations balanced against combinatorial explosion.
- [ ] **(performance)** As the developer, I want item/lineage save size and load time measured, with pruning if needed.
- [ ] **(testing)** As the developer, I want mass-reforge simulations across many seeds and input combinations.
- [ ] **(crafting)** As the developer, I want tag coverage and combinatorial balance validated at full ingredient/pattern scale.
- [ ] **(testing)** As the developer, I want mass crafting simulations across ingredient sets, priorities, and fallbacks.
- [ ] **(performance)** As the developer, I want matcher performance measured with the full pattern and ingredient set loaded.
- [ ] **Gate:** Beta — content-complete. Only polish, balance, and bug fixes after this point.

## Phase 11 — Polish, optimization, and shipping

**Goal:** make the build stable, fast, understandable, and ready to sell.

- [ ] **Decision:** Launch date and marketing beat.
- [ ] As a player, I want the game to run smoothly on the target hardware.
- [ ] As a developer, I want CPU, GPU, and load-time profiles with fixes prioritized by player impact.
- [ ] As a developer, I want crash, save-corruption, and migration bugs fixed before cosmetic issues.
- [ ] As a player, I want a final balance pass informed by playtest data, not vibes alone.
- [ ] As a player, I want complete accessibility and input-remapping coverage.
- [ ] As a developer, I want localization QA, including font coverage and text overflow.
- [ ] As a developer, I want a store page, screenshots, trailer, and wishlist campaign ready before launch.
- [ ] As a developer, I want a Shipping build configuration, a clean cook/package, and clean-machine install tests.
- [ ] As a developer, I want console certification and submission complete, if applicable.
- [ ] As a developer, I want a release candidate, a day-one patch plan, and a rollback plan.
- [ ] **(performance)** As the developer, I want a final open-world performance pass using packaged builds and Unreal Insights.
- [ ] **(persistence)** As the developer, I want save migration and corruption recovery tested across versions.
- [ ] **(movement)** As the player, I want traversal tuning finalized and regression-tested across all modes.
- [ ] **(landscape)** As the developer, I want terrain, LOD, and HLOD artifacts fixed to shipping quality.
- [ ] **(procgen)** As the developer, I want seed and generator-version migration with archived generated worlds, so old saves do not break when the generator changes.
- [ ] **(validation)** As the developer, I want a final validation pass with no unreachable POIs, disconnected regions, or unbuildable plots.
- [ ] **(performance)** As the developer, I want final generation and cook-time checks in packaged builds.
- [ ] **(procgen)** As the developer, I want the generator and override pipeline documented for post-launch maintenance.
- [ ] **(tier-transition)** As the developer, I want transition times, loading screens, and failure recovery polished.
- [ ] **(world-state)** As the developer, I want strategic save migration tested across versions, including armies, squads, buildings, and fog of war.
- [ ] **(performance)** As the developer, I want three-tier performance verified in packaged builds, including strategic-to-tactical transitions.
- [ ] **(ui)** As the player, I want World Map, Local Map, and squad command UI polished and accessible.
- [ ] **(world-map)** As the developer, I want strategic balance finalized across factions, armies, and territory.
- [ ] **(roguelike)** As the developer, I want final run/meta-progression balance and regression tests.
- [ ] **(faction-sim)** As the developer, I want final faction/frontier/infrastructure balance and regression tests.
- [ ] **(party)** As the developer, I want final party/co-op balance and regression tests.
- [ ] **(squad)** As the developer, I want tactical balance finalized across squad types, abilities, and counters.
- [ ] **(combat)** As the developer, I want final melee and ranged balance across all archetypes, traits, and difficulty settings.
- [ ] **(melee)** As the player, I want hit feedback, camera, and hitstop polished on counters, executions, and finishers.
- [ ] **(ranged)** As the player, I want aim feel, reticle behavior, and charge-shot feedback polished.
- [ ] **(testing)** As the developer, I want a final combat regression pass for token logic, streak resets, ability costs, and mode transitions.
- [ ] **(spellcasting)** As the developer, I want final spell balance and ability-bar UI polish across all elements and upgrades.
- [ ] **(animation)** As the player, I want spell VFX, SFX, and cast/channel animations polished for impact and readability.
- [ ] **(testing)** As the developer, I want a final spell regression pass for cost/cooldown, ICD, reactions, CC diminishing returns, and ultimate states.
- [ ] **(style)** As the developer, I want final style tuning and visual-regression approval across all three domains.
- [ ] **(rendering)** As the developer, I want a final performance pass for the full style stack in packaged builds.
- [ ] **(vfx)** As the developer, I want final watercolor VFX polish for impact, readability, and overdraw.
- [ ] **(items)** As the developer, I want final item balance and reforge UI polish across all families and materials.
- [ ] **(crafting)** As the developer, I want final durability cadence and reforge economy tuned from playtest data.
- [ ] **(testing)** As the developer, I want a final item regression pass for durability, inheritance, anti-exploit, and save migration.
- [ ] **(crafting)** As the developer, I want final crafting balance and UI polish, including competing-use tooltips and discovery journal clarity.
- [ ] **(testing)** As the developer, I want a final dead-ingredient/dominance audit and a crafting regression pass.
- [ ] **Decision:** Post-launch support scope — patches, mod support, or additional content.
- [ ] **Gate:** Launch readiness — stable build, save migration verified, store assets approved, support plan in place.

## Phase 12 — Post-launch

**Goal:** support the players who showed up and protect the game's reputation.

- [ ] As a player, I want crashes and progression blockers fixed quickly.
- [ ] As a developer, I want telemetry and crash reports reviewed and patches prioritized by player impact.
- [ ] As a player, I want promised mod support or content delivered on a realistic schedule.
- [ ] As a developer, I want a clear end-of-support statement instead of silent abandonment.

## Recurring practices (every phase)

- [ ] As a developer, I want a weekly fifteen-minute review that re-aims the current milestone and checks motivation runway.
  - *Context: Motivation runway is how much sustained solo effort remains feasible before burnout forces a break.*
- [ ] As a developer, I want every milestone to be demoable by a stranger, so progress is falsifiable.
- [ ] As a developer, I want to cut scope — not quality, not the date — when a milestone slips.
- [ ] As a developer, I want the backlog to stay the single source of truth; most ideas die here.
- [ ] As a developer, I want a test added with every system that has state, math, or persistence.
- [ ] As a developer, I want load-bearing engine APIs re-verified against Epic docs before coding, not trusted from notes alone.
- [ ] As a developer, I want playtests at every phase, not only at the end.
- [ ] As a developer, I want prototype and slice shortcuts declared in writing, so temporary code does not become permanent by accident.
