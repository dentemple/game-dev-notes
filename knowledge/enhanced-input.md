---
title: Enhanced Input
tags: [input, enhancedinput, inputaction, mappingcontext, triggers, modifiers]
source: https://dev.epicgames.com/documentation/unreal-engine/enhanced-input-in-unreal-engine (accessed 2026-11-18)
updated: 2026-11-18
---

# Enhanced Input

## Status (primary)

- "Enhanced Input is enabled by default." (UE5; the current default input system.)

## Four core concepts (primary)

- "The Enhanced Input system has four main concepts, Input Actions, Input Mapping Contexts,
  Input Modifiers, and Input Triggers."
- **Input Actions** — "the communication link between the Enhanced Input system and your
  project's code" (Bool / Axis1D / Axis2D / Axis3D).
- **Input Mapping Contexts** — "a collection of Input Actions that represents a certain context
  that the player can be in" (add/remove per-player, priority ordered).
- **Input Modifiers** — "pre-processors that alter the raw input values" (dead zone, negate,
  swizzle, smoothing, response curves).
- **Input Triggers** — "determine whether user input, after passing through an optional list of
  Input Modifiers, should activate" (Pressed, Released, Hold, Tap, Chorded, …).
- Source: https://dev.epicgames.com/documentation/unreal-engine/enhanced-input-in-unreal-engine (accessed 2026-11-18).

## Legacy input (primary vs third-party)

- Epic's page frames legacy (UE4 default) input as having "an upgrade path and backward
  compatibility from the default input system from Unreal Engine 4." It does **not** use the
  word "deprecated."
- Third-party/Meta sources call legacy `BindAction`/`BindAxis` mappings "deprecated." Treat
  "deprecated" as third-party wording; prefer Enhanced Input for all new work.

## C++ integration

- Add `"EnhancedInput"` to `.Build.cs`; use `UInputAction` data assets and
  `UEnhancedInputComponent::BindAction(...)`. Re-verify exact bind signature against the page
  above before use.
