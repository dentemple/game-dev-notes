---
title: Multi-Style Rendering (Realistic Near, Impressionist Far, Watercolor VFX)
tags: [rendering, art, impressionism, kuwahara, watercolor, vfx, post-process, sceneviewextension, tsr, style-profile]
source: https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-materials-in-unreal-engine (accessed 2026-11-19)
updated: 2026-11-19
---

# Multi-Style Rendering (Realistic Near, Impressionist Far, Watercolor VFX)

## Goal & scope

Architecture for using several visual treatments in one UE 5.8 game: a realistic PBR/Nanite/Lumen near field, an impressionist/painterly far field, and watercolor-styled special effects. The focus is the style system — assignment, blending, precedence, performance, and temporal stability — not a single shader.

## Primary sources

- Epic — Post Process Materials:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-materials-in-unreal-engine (accessed 2026-11-19)
- Epic — ISceneViewExtension API:
  https://dev.epicgames.com/documentation/unreal-engine/API/Runtime/Engine/ISceneViewExtension?application_version=5.7 (accessed 2026-11-19)
- Epic — Temporal Super Resolution:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/temporal-super-resolution-in-unreal-engine (accessed 2026-11-19)
- Epic — Exponential Height Fog:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/exponential-height-fog-in-unreal-engine (accessed 2026-11-19)
- Dordogne art-direction Q&A (watercolor pipeline):
  https://www.gamedeveloper.com/design/q-a-hand-painting-the-watercolor-world-of-i-dordogne-i- (accessed 2026-11-19)
- Kyprianidis et al. — anisotropic Kuwahara (reported; PDF):
  https://www.kyprianidis.com/p/npar2009/jkyprian-npar2009.pdf (accessed 2026-11-19)
- Ghost of Tsushima Advances 2021 talk (reported; PDF):
  https://www.realtimerendering.com/advances/s2021/jpatry_advances2021.pdf (accessed 2026-11-19)
- Epic — Nanite / Lumen / RVT and stat commands (reused receipts):
  https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine · https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine · https://dev.epicgames.com/documentation/en-us/unreal-engine/runtimevirtual-texturing-quick-start-in-unreal-engine · https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine (accessed 2026-11-19)

## Three style domains

1. **Realistic near field.** Stock PBR + Nanite + Lumen. No screen-space style below the near threshold; this is the readability and combat-legibility layer.
2. **Impressionist far field.** A distance-masked painterly filter — anisotropic Kuwahara or a cheaper bilateral/mean-shift — plus a stroke-texture overlay, atmospheric perspective, and HLOD/impostors. Flatten the far field; do not simulate brush physics.
3. **Watercolor VFX.** Authored watercolor textures on Niagara sprites/meshes, a simple shader, edge darkening, white rim light, subtle glow/edge blending, paper grain, and optional slow UV/flow drift. Do not build an animated watercolor simulation for gameplay VFX.

## Technique notes

### Impressionist far field

- Kuwahara: structure tensor → local orientation/anisotropy → elliptical filter sectors → weighted average favoring low-variance sectors. Produces a painterly, feature-preserving flattening.
- Cheaper alternatives: bilateral or mean-shift filtering, or a single-pass approximation. Start cheap; profile.
- Add a stroke-texture overlay and atmospheric perspective; let fog carry color convergence into the sky.
- Use HLOD/impostors for geometry that is far enough that the filter does most of the work.

### Watercolor VFX

- Dordogne's art director: animated watercolor shaders usually look fake, and the eye is uncomfortable with watercolor movement. The shipped approach was painted lighting/shadows, watercolor-textured assets, a very simple shader, and a white rim light with glow edge blending.
- For gameplay effects: authored watercolor textures, edge darkening, paper grain, a subtle flow-map/UV drift, and restrained screen-space distortion. Keep motion slow and readable.
- Prefer additive/unlit materials and bounded sprite counts to control sorting and overdraw in combat.

## UE 5.8 architecture

### Post-process backbone

- Post-process materials read `SceneTexture` color/GBuffer/custom depth/stencil and are assigned through Post Process Volume **Blendables** with priority ordering.
- Prefer the **After Tonemapping** blendable location for performance (LDR).
- Use unbound volumes for global styles, bound volumes with Blend Radius for region styles; volume priority resolves overlap.
- Put global style scalars/vectors (style blend, brush density, grain strength) in a Material Parameter Collection.

### Custom passes

- `ISceneViewExtension::SubscribeToPostProcessingPass` is the engine hook; `EPostProcessingPass` immediately precedes a PPM blend location.
- `GetPriority` orders extensions; `IsActiveThisFrame` gates per frame.
- The `FSceneViewExtensions::NewExtension<T>()` + `FRDGBuilder` callback pattern is the standard plugin route for a multi-pass compute filter without engine edits.

### Per-object, per-region, per-distance assignment

- **Per-object:** Custom Depth Stencil values for selective post-process masks.
- **Per-region:** bound post-process volumes, Data Layers, Runtime Virtual Textures for blended style layers.
- **Per-distance:** SceneDepth/camera-distance masks in materials and post-process; Exponential Height Fog for atmospheric color convergence (Inscattering Color Cubemap can match distant fogged elements to the sky).
- **Global:** Material Parameter Collection and style profile parameters.

### Temporal stability

- TSR reprojects with motion vectors; its flicker heuristic deliberately trades ghosting for stability.
- Any stylized effect must be temporally stable or write correct motion vectors.
- Use world-space-stable noise for grain/brush textures, not screen-space random noise.
- Tune `r.TSR.Velocity.WeightClampingSampleCount` (default 4.0) and verify with `r.TSR.Visualize` (0 = accumulated samples, 7 = flicker-heuristic mask) and the motion/reprojection visualizers.

## Style system

Model styles as data, not code sprawl:

- **Style profile data asset** per domain: post-process materials + priority, blend radius, MPC parameter set, stencil ranges, distance thresholds, quality-tier toggles.
- **Style manager** (GameInstanceSubsystem or WorldSubsystem) owns active profiles and resolves precedence: per-region > per-distance > global.
- **Assignment:** gameplay tags on actors/regions map to stencil values and MPC overrides; the post-process stack reads the masks.
- **Conflict rule:** no two full-screen styles may write the same channel at the same blendable location. Order by blendable location and priority; use one distance mask as the single source of truth for realistic→impressionist.
- **Content pipeline:** shared material functions, a style atlas (brush strokes, grain, watercolor washes, LUTs), and HLOD/impostor baking.
- **Testing:** golden-screenshot regression per style domain, GPU ms budgets, camera-pan temporal-stability diffs, style-coverage checks, quality-tier sweeps.

## Blend contract

One smooth scalar drives the realistic→impressionist transition:

- Per-pixel camera-distance mask or per-region style weight.
- Cross-fade between the unmodified scene and the painterly output inside the same post-process material.
- Smooth the mask; do not use a hard depth cut.
- Let fog carry color convergence so the boundary does not read as a line.

## Build order

1. Post-process style pass: cheap Kuwahara/bilateral masked by distance, plus stroke overlay, grain, LUT, vignette.
2. One style profile data asset + style manager with near/far precedence.
3. Per-object stencil and per-region volume assignment.
4. Watercolor-textured Niagara impact effect with a simple shader and edge darkening.
5. HLOD/impostor far-field geometry and fog convergence.
6. Custom RDG multi-pass Kuwahara only if the single-pass approximation is insufficient.

## Performance and scalability

- Full-screen filters are bandwidth-heavy: half-res and/or async compute the far-field pass; gate it behind a quality setting.
- Bound watercolor VFX overdraw; prefer unlit/additive materials and limited sprite counts.
- Profile with `stat unit`, `stat gpu`, `stat scenerendering`, `stat rhi`, and Unreal Insights.
- Nanite masked materials are supported, but WPO must be clamped; Lumen cost grows with instance count.

## Anti-patterns

- Treating watercolor as an animated fluid simulation for gameplay VFX.
- Multiple full-screen styles writing the same channel at the same blendable location.
- Hard depth-cut masks that create visible seams.
- Screen-space random noise that swims under TSR.
- Running a multi-pass Kuwahara before profiling a single-pass approximation.
- Letting the painterly far field reduce combat readability.
- Assuming TSR can remove all shimmer without ghosting.
- Per-object style assignments without a coverage check; untagged objects fall through.

## Verify-first

- Re-verify post-process blendable locations, SceneTexture/CustomStencil, and volume blending against dev.epicgames.com.
- Re-verify `ISceneViewExtension` signatures for UE 5.8 (the API page checked was 5.7).
- Re-verify TSR cvars and visualize modes for the installed engine version.
- Profile the Kuwahara/watercolor stack on target hardware before building content around it.

## Related

`paper-parchment-style.md` · `ue-performance.md` · `ue5-overview.md` · `features/combat-spellcasting.md`
