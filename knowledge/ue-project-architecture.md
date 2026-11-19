---
title: UE Project Structure & Source Control
tags: [structure, folder, naming, git, lfs, source-control, conventions]
source: https://crdg.jp/studio-tech-1/en/2025/05/22/3390/ (accessed 2026-11-18)
updated: 2026-11-18
---

# UE Project Structure & Source Control

## Folder structure (primary)

- Native layout: `Config/`, `Content/`, `Source/`, `Plugins/` + `.uproject`.
- Content tree: `_Dev/` (personal WIP, excluded from cooking), then `Audio/`, `Blueprints/`, `Characters/`, `Data/`, `Environment/`, `FX/`, `Maps/`, `Materials/`, `UI/`. Feature-based grouping for characters; type-based grouping for shared assets.
Source: https://www.strayspark.studio/blog/ue5-project-architecture-naming-conventions (accessed 2026-11-18).

## Naming (primary)

- "Every asset gets a type prefix for instant identification": `BP_` (Blueprint), `SM_` (Static Mesh), `SK_` (Skeletal Mesh), `M_` (Material), `MI_` (Material Instance), `MF_` (Material Function), `T_` (Texture), `AS_` (Anim Sequence), `AM_` (Anim Montage), `ABP_` (Anim Blueprint), `NS_` (Niagara), `SC_` (Sound Cue), `SW_` (Sound Wave), `WBP_` (Widget Blueprint), `DT_` (Data Table), `LV_` (Level), `GM_` (Game Mode), `GI_` (Game Instance), `PC_` (Player Controller).
- Texture suffixes: `_BC`, `_N`, `_R`, `_M`, `_AO`, `_E`, `_H`, `_A`, `_ORM`. Variants `_01`/`_02`; LODs `_LOD0`/`_LOD1`; sizes `_S`/`_M`/`_L`.
Source: https://www.strayspark.studio/blog/ue5-project-architecture-naming-conventions (accessed 2026-11-18).

## Source control (primary)

- Commit `Config/`, `Content/`, `Source/`, `Plugins/`, `.uproject`. Ignore `Binaries/`, `Saved/`, `Intermediate/`, `DerivedDataCache/`, `Build/`, `*_BuiltData.uasset`.
- Git LFS: run `git lfs install` once; track binary types via `.gitattributes` (e.g. `*.uasset filter=lfs diff=lfs merge=lfs -text`). Configure LFS **before** committing binary assets — retrofitting is painful.
- "UE5 assets are binary files that can't be merged" — use LFS/Perforce file locking and small, focused changes.
Source: https://crdg.jp/studio-tech-1/en/2025/05/22/3390/ and https://www.strayspark.studio/blog/ue5-project-architecture-naming-conventions (accessed 2026-11-18).

## Note for solo dev

Git + Git LFS, trunk-based development, small frequent commits; ignore generated folders from day one.
