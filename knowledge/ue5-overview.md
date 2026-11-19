---
title: Unreal Engine 5 Overview
tags: [ue5, version, cpp20, resources, docs]
source: https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-9-release-notes (accessed 2026-11-18)
updated: 2026-11-18
---

# Unreal Engine 5 Overview

## Current state (as of 2026-11)

- UE **5.9** is the current documented release and is in **Preview** (not full release):
  "Unreal Engine 5.9 Preview comes with significant improvements to Python scripting and the
  Unreal MCP" — https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-9-release-notes (accessed 2026-11-18).
- UE **5.8** is the current **stable** full release (released 2026; per press reports, not
  Epic's own release-note page which is JS-only via fetch). Treat 5.8 as the safe production
  baseline; confirm the installed engine's exact version before relying on flags.

## Language standard (load-bearing)

- UE builds as **C++20** by default and **requires a minimum of C++20**:
  "Unreal Engine compiles with a language version of C++20 by default and requires a minimum
  version of C++20 to build." — https://dev.epicgames.com/documentation/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine (accessed 2026-11-18).
- Do not set a Cpp14/Cpp17 override in `.Target.cs` for 5.8+.

## Compiler/toolchain minimums (UE 5.8, primary)

| Tool | Minimum | Recommended |
|------|---------|-------------|
| MSVC | 14.38 | 14.50 |
| Windows SDK | 10.0.22621.0 | 10.0.26100 or newer |
| LLVM | 18.1.8 | 20.1.8 |

Source: https://dev.epicgames.com/documentation/unreal-engine/setting-up-visual-studio-development-environment-for-cplusplus-projects-in-unreal-engine (accessed 2026-11-18).

## Canonical references

- Documentation root (docs.unrealengine.com redirects here):
  https://dev.epicgames.com/documentation/en-us/unreal-engine
- C++ API reference: https://dev.epicgames.com/documentation/en-us/unreal-engine/API
- Official sample (Lyra) — reference for GAS, Enhanced Input, modular gameplay:
  https://dev.epicgames.com/documentation/en-us/unreal-engine/lyra-sample-game-in-unreal-engine

## Note

- Epics docs render lazily; some pages (release notes, automation technical guide) return only
  a table of contents to a text fetcher. Prefer the API reference and pages that return full
  body; re-fetch or use a markdown mirror when the body is absent.
