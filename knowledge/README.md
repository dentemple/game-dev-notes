# Knowledge store

An on-demand, git-tracked knowledge base for the `unreal-engine-dev` agent. It
holds curated Unreal engineering notes plus design, narrative, and market
context for engineering decisions, so the agent loads only what it needs, when
it needs it — never the whole store into context.

## Who does what

- `agent-researcher` writes and maintains this store: it researches, distills,
  and adds topic files plus index rows.
- `unreal-engine-dev` reads it on demand: consult the index, then Read/Grep only
  the topic files relevant to the current task. It does not edit curated topics
  or index rows. It writes its own persistent notes under `agent-memory/` and
  research briefs under `research-requests/`; `agent-researcher` turns those
  requests into curated topics. Its memory writes are append-only.

## How to read (for unreal-engine-dev)

1. Read this file first — it is the cross-cutting map. Feature research has a
   second index at `features/README.md`; read it too when the task names a
   specific feature.
2. Use the routing table in the agent prompt
   (`../.claude/agents/unreal-engine-dev.md`, "Routing") for the common
   clusters. Grep the indexes first, then grep topic files only when the
   indexes are insufficient.
3. Read only the topic file(s) that match the current task; they are kept small
   on purpose. Never read multiple feature files "just in case" — one feature
   at a time unless the task explicitly spans features.
4. Treat every note as preliminary research. Each note cites a `source` URL and
   access date; `RESEARCH` and `ANALYSIS` sections are secondary or inferred.
   For anything load-bearing (an API signature, an engine flag), re-check
   against the cited source or primary docs (dev.epicgames.com /
   docs.unrealengine.com) rather than trusting the note alone.

## Feature research

Feature-specific research — how to build a *specific* feature (inventory,
save/load, dialogue, quests, combat, AI, …) — lives in `features/<feature-slug>.md`,
one self-contained file per feature. Read `features/README.md` for the convention
and the feature index. The agent prompt
(`../.claude/agents/unreal-engine-dev.md`, "Routing") carries the start-here
table for the common clusters (combat, AI, progression, modding, save,
performance, design, networking, input). This keeps feature work isolated: the
agent loads only the file for the feature it is working on, so unrelated feature
research never enters context.

## Handoff and memory

- `research-requests/` — `unreal-engine-dev` writes research briefs here.
  `agent-researcher` picks them up and writes the curated topic; see
  `research-requests/README.md` for the brief template and the accepted order.
- `agent-memory/` — `unreal-engine-dev`'s own persistent working memory. It is
  not a curated topic and is not in the index; see `agent-memory/README.md`.

## How to write (for contributors)

- One topic per file under `knowledge/`, with a kebab-case filename matching the
  slug in the index.
- Feature-specific research goes in `features/<feature-slug>.md` (see
  `features/README.md`); cross-cutting knowledge stays in the top-level topics.
- Keep each file short (aim under 300 lines); split a growing topic into two
  rather than appending indefinitely.
- Frontmatter on every topic file:

  ```yaml
  ---
  title: <short>
  tags: [<lowercase keywords for grep>]
  source: <URL> (accessed <YYYY-MM-DD>)
  updated: <YYYY-MM-DD>
  ---
  ```

- Every topic cites its `source` URL and access date. Use `RESEARCH` or
  `ANALYSIS` section labels for content that is secondary or inferred; do not
  present those sections as primary-sourced.
- Append only: add a new topic and its index row; never rewrite, delete, or
  reorder an existing topic. Report suspected errors to `agent-researcher`.
- After writing a topic, add its row to the index below.

## Index

| Slug | Title | Tags | Updated |
|------|-------|------|---------|
| ue5-overview | Unreal Engine 5 Overview | ue5, version, cpp20, resources, docs | 2026-11-18 |
| cpp-programming | C++ Programming Fundamentals | cpp, uclass, uproperty, ufunction, reflection, modules, gc, naming | 2026-11-18 |
| delegates | Delegates | delegate, multicast, dynamic, broadcast, blueprintassignable | 2026-11-18 |
| replication | Property Replication | replication, networking, replicated, dorplifetime, onrep, server | 2026-11-18 |
| gameplay-ability-system | Gameplay Ability System (GAS) | gas, abilities, asc, attributes, gameplayeffects, gameplaytags, lyra | 2026-11-18 |
| automation-testing | Automation Testing | automation, fatomationtestbase, latent, command, runtests | 2026-11-18 |
| enhanced-input | Enhanced Input | input, enhancedinput, inputaction, mappingcontext, triggers, modifiers | 2026-11-18 |
| agentic-ai | Agentic AI (Unreal MCP & AI Agents) | ai, mcp, agent, llm, claude-code, codex, cursor, toolset, assistant | 2026-11-18 |
| game-design-fundamentals | Game Design Fundamentals (Fun, Feel, Loops) | design, mda, fun, game-feel, juice, core-loop, retention, aesthetics | 2026-11-18 |
| narrative-storytelling | Narrative & Storytelling (Games as a Story Medium) | narrative, story, storytelling, environmental, ludonarrative, jenkins, rpg-maker, cinematics, dialogue | 2026-11-18 |
| social-interaction | Social Interaction (Dialogue, Morality, Reputation) | social, dialogue, morality, reputation, choice, consequence, mass-effect, fallout, relationship, faction | 2026-11-18 |
| emergent-behavior | Emergent Behavior (Boids, Steering, Swarms) | behavior, flocking, boids, emergence, steering, swarm, stigmergy, crowd, ai, simulation | 2026-11-18 |
| simulation-agents | Simulation Agents (Needs, Utility AI, Directors) | behavior, agent, simulation, utility-ai, needs, director, ai, rimworld, rct, cities-skylines | 2026-11-18 |
| procedural-generation | Procedural Generation (Voronoi, WFC, Cellular Automata) | procedural, generation, voronoi, delaunay, wfc, cellular-automata, terrain, biome, mapgen, ecosystem | 2026-11-18 |
| epidemiology-behavior | Epidemiology & Population Models (SIR, Lotka-Volterra, Corrupted Blood) | behavior, epidemiology, sir, seir, pathogen, population, lotka-volterra, agent-based, cellular-automata, corrupted-blood, simulation | 2026-11-18 |
| rpg-design | RPG Design (Systems, Progression, Itemization) | rpg, stats, leveling, progression, itemization, loot, damage, balance, gas, attributes | 2026-11-18 |
| 4x-warfare | 4X Military & Warfare Design (Total War, Civ 6, Humankind) | 4x, warfare, military, strategy, combat, morale, units, war-weariness, diplomacy, terrain | 2026-11-18 |
| product-lifecycle | Product Development Lifecycle | pdlc, lifecycle, prototype, vertical-slice, mvp, alpha, beta, scope, milestone | 2026-11-18 |
| solo-project-management | Solo Project Management & Shipping | solo, project-management, scope, milestone, backlog, shipping, burnout, runway | 2026-11-18 |
| feature-prioritization | Feature Prioritization & Build vs Buy | prioritization, kano, rice, ice, moscow, build-vs-buy, tech-debt, roadmap | 2026-11-18 |
| market-and-consumer | Market & Consumer Expectations | market, steam, wishlist, revenue, quality-bar, survivorship-bias, first-impression | 2026-11-18 |
| ue-project-architecture | UE Project Structure & Source Control | structure, folder, naming, git, lfs, source-control, conventions | 2026-11-18 |
| ue-performance | UE Performance & Profiling | performance, profiling, frame-budget, stat-unit, gpu, cpu, insights, optimization | 2026-11-18 |
| ue-game-feel | UE Game Feel (Coyote Time, Buffering, Hitstop) | game-feel, coyote-time, jump-buffering, hitstop, screen-shake, enhanced-input, juice | 2026-11-18 |
| paper-parchment-style | Paper & Parchment Visual Style (UE) | art, rendering, paper, parchment, post-process, materials, decals, nanite, substrate, ui, manuscript | 2026-11-19 |
| multi-style-rendering | Multi-Style Rendering (Realistic Near, Impressionist Far, Watercolor VFX) | rendering, art, impressionism, kuwahara, watercolor, vfx, post-process, sceneviewextension, tsr, style-profile | 2026-11-19 |
| engineering-best-practices | Engineering Best Practices (Patterns & Anti-Patterns) | best-practices, patterns, kiss, yagni, tick, cast, blueprint, cpp, anti-pattern | 2026-11-18 |
| game-architecture | Game Architecture (Actors, Components, Subsystems, Save) | architecture, actor, component, subsystem, event-dispatcher, interface, casting, save, versioning | 2026-11-18 |
| modding-support | Modding Support (Mod-First Architecture) | modding, mod-first, ugc, modio, steam-workshop, pak, game-features, data-driven, gameplaytags, plugin | 2026-11-18 |
| design-best-practices | Design Best Practices (Onboarding, Playtesting, Difficulty) | design, onboarding, ftue, tutorial, playtesting, iteration, difficulty | 2026-11-18 |
| shipping-and-polish | Shipping & Polish (Launch Checklist) | shipping, launch, localization, store-page, wishlist, certification, polish | 2026-11-18 |

Add one row per topic; keep it grep-friendly (stable slugs, lowercase tags).
