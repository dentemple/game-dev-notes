---
title: Paper & Parchment Visual Style (UE)
tags: [art, rendering, paper, parchment, post-process, materials, decals, nanite, substrate, ui, manuscript]
source: https://www.gamedeveloper.com/art/deep-dive-the-art-of-pentiment (accessed 2026-11-19)
updated: 2026-11-19
---

# Paper & Parchment Visual Style (UE)

## Goal & scope

A production-feasible paper/parchment look for a mythic-tale game in UE 5.8: painted parchment surfaces, ink and stain decals, screen-space outline/grain, book-style UI, and selective papercraft props. Does **not** require a fully physical paper world or cloth simulation.

## Primary sources

- Pentiment art deep-dive (Hannah Kennedy):
  https://www.gamedeveloper.com/art/deep-dive-the-art-of-pentiment (accessed 2026-11-19)
- Tearaway GDC 2013 session (Rex Crowle):
  https://www.gdcvault.com/play/1019140/contactUs (accessed 2026-11-19)
- The Plucky Squire Unreal interview (reported; page blocked this session):
  https://www.unrealengine.com/developer-interviews/the-plucky-squire-blends-2d-and-3d-visuals-in-aesthetically-pleasing-and-mechanically-interesting-ways (accessed 2026-11-19)
- Epic — Post Process Materials:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/post-process-materials-in-unreal-engine (accessed 2026-11-19)
- Epic — Decals:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/decal-actors-in-unreal-engine (accessed 2026-11-19)
- Epic — Substrate (Beta):
  https://dev.epicgames.com/documentation/en-us/unreal-engine/substrate-materials-in-unreal-engine (accessed 2026-11-19)
- Epic — Nanite:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/nanite-virtualized-geometry-in-unreal-engine (accessed 2026-11-19)
- Epic — Lumen:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/lumen-global-illumination-and-reflections-in-unreal-engine (accessed 2026-11-19)
- Epic — Runtime Virtual Textures:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/runtimevirtual-texturing-quick-start-in-unreal-engine (accessed 2026-11-19)
- Epic — Stat commands:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/stat-commands-in-unreal-engine (accessed 2026-11-19)

## Three reference models

- **Painted 2D in 3D space (Pentiment).** Painted characters and environments, track-constrained movement, a camera that keeps characters facing “north,” bespoke greyboxes before final art. Cheapest high-fidelity parchment route, but it is an authored-2D pipeline, not a 3D material trick.
- **Full papercraft 3D (Tearaway).** 3D meshes with paper materials, folds, creases, edge wear, and paper-like animation. The world itself is the style; every prop must read as paper.
- **Storybook hybrid (The Plucky Squire).** Simple 2D book world contrasted with a realistic 3D room; the value is the contrast, and camera continuity between the two is the hard part.

## Recommended hybrid

**Paint the surfaces; papercraft the props.**

- 3D world with parchment/painted textures and decals.
- One LDR post-process material for ink outline, paper grain, LUT, and vignette.
- Book-style UMG for menus and story pages.
- A small set of papercraft hero props with thickness, masked edges, and World Position Offset flutter.
- Do not attempt an all-paper 3D world or two full art styles.

## Materials and textures

- **Paper base:** scanned paper/parchment base color; subtle fiber and crease normal; high roughness (about 0.8–1.0); ambient occlusion in creases; metallic 0.
- **Decals:** ink, stains, soot, handwriting, tears, burns, wax, and stitching as deferred decals. Keep decal boxes small; cost depends on screen-space box size and shader complexity, not on the target mesh.
- **Two-sided paper:** enable TwoSided; prefer masked/alpha-test or dithered opacity over translucent. Translucency adds sorting and overdraw.
- **Subsurface/thin translucency:** only for backlit parchment hero moments.
- **Page curl/fold/flutter:** World Position Offset driven by vertex-color masks. Keep heavy deformation on low-poly sheets; clamp Nanite displacement.
- **Substrate:** Beta in current docs; do not build the shipped look on it in 5.8. Use a traditional material graph with a toon/ramp or post-process treatment.
- **Nanite:** fine for static papercraft cliffs/props with masked materials; not for heavily deforming pages (clamped WPO, no morph targets).

## Post-process style pass

One After-Tonemapping post-process material can carry most of the look:

- **Ink outline:** depth/normal discontinuity detection (optionally a 3×3 Sobel kernel). For selective outlines, use Custom Depth/Stencil with per-mesh stencil values and read `SceneTexture:CustomStencil`; inverted-hull geometry handles external silhouettes.
- **Paper grain:** screen-space grain overlay, low-frequency mottling, and optional halftone/dither.
- **Painterly filter:** optional Kuwahara/blur-quantize pass; keep it subtle to avoid noise.
- **Color:** warm parchment LUT, restrained contrast, soft vignette, light tilt-shift/DoF for the diorama feel.
- **RVT:** use Runtime Virtual Textures for large-area ink/grain blending across terrain.

Prefer the LDR After-Tonemapping blendable location; it is the cheaper post-process slot. Keep the stack single-pass where possible.

## 3D construction and lighting

- Papercraft props: visible thickness, folds, cutouts, layered planes for pop-up depth.
- Staging: slight orthographic/tilt-shift camera, forced perspective, diorama framing.
- Lighting: soft Lumen GI, rim light on paper edges, AO in creases; a stylized shadow ramp reads better than photoreal contact shadows.
- Page/book transitions: render the scene to a texture on the page, then animate page WPO/UV; budget camera continuity, not just the shader.

## Text and UI

- Handwritten/illuminated display font, drop caps, marginalia, gold-leaf accents.
- Body text on flat UMG panels for legibility; avoid long text on curved paper.
- Use Text3D or texture-on-plane only for hero titles.
- Keep one paper-material family for menus, page edges, wax seals, and ribbons.

## Performance

- Overdraw is the main risk: layered translucent pages and grain overlays stack fill-rate. Prefer masked/dithered opacity; keep the grain overlay LDR and single-pass.
- Decals: watch screen-space box size and count.
- WPO: cost scales with vertex count; clamp Nanite displacement.
- Profile with `stat unit`, `stat gpu`, `stat scenerendering`, `stat rhi`, `stat memory`, and Unreal Insights.
- Paper textures compress well as standard sRGB maps; keep normal maps subtle.

## Art pipeline

- Build a paper **trim sheet + decal atlas** (fiber, stains, ink, gold leaf, torn/burned edges, stitches) and reuse it everywhere.
- Lock a small period-pigment palette.
- Vertex-paint fold/crease masks.
- Greybox bespoke scenes before final art; hand-drawn/painted texture work is expensive to revise repeatedly.
- Test the post-process stack before detailing textures; a noisy texture plus grain is the classic muddy result.

## Build order

1. Post-process style pass: outline + grain + LUT + vignette in one After-Tonemapping material.
2. One parchment material + one decal atlas on a greybox scene.
3. Lighting: Lumen, rim, AO, tilt-shift/ortho camera.
4. Parchment UMG for menus and story pages.
5. Selective papercraft props with WPO flutter and masked edges.
6. Page/book transitions last.

## Anti-patterns

- Translucent layered pages causing overdraw.
- Muddy/noisy paper textures; put grain in post, not in base color.
- Over-outlining everything; Sobel noise destroys readability.
- Wrong material response: metallic paper, glossy paper, or strong normal detail.
- Building the shipped look on Beta Substrate.
- Real cloth/paper physics simulation for every page.
- Two full art styles (2D book + realistic 3D room) without the team to support both.
- Long body text on curved paper.
- Inconsistent style across props; one atlas and one palette prevent it.

## Verify-first

- Re-verify Substrate’s status in UE 5.8 before using it.
- Re-verify post-process blendable locations, Custom Depth/Stencil, and decal modes against dev.epicgames.com.
- Re-verify Nanite masked/WPO limits and Lumen costs.
- Profile the post-process stack on target hardware before building content around it.

## Related

`ue5-overview.md` · `ue-performance.md` · `design-best-practices.md` · `features/combat-spellcasting.md`
