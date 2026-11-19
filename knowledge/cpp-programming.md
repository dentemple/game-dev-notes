---
title: C++ Programming Fundamentals
tags: [cpp, uclass, uproperty, ufunction, reflection, modules, gc, naming]
source: https://dev.epicgames.com/documentation/unreal-engine/programming-with-cpp-in-unreal-engine (accessed 2026-11-18)
updated: 2026-11-18
---

# C++ Programming Fundamentals

## Reflection macros (primary)

- "`UCLASS()`, `UFUNCTION()`, and `UPROPERTY()` macros can be used to make Unreal Engine aware
  of the new classes, functions, and variables."
- "a variable with a declaration prefaced by a `UPROPERTY()` macro can be garbage collected by
  the engine" and "can be displayed and edited within Unreal Editor."
- A `UPARAM()` macro exists primarily for exposing C++ to Blueprints.
- Source: https://dev.epicgames.com/documentation/unreal-engine/programming-with-cpp-in-unreal-engine (accessed 2026-11-18).

## Naming prefixes (primary)

"Template classes are prefixed by T." / "Classes that inherit from UObject are prefixed by U." /
"Classes that inherit from AActor are prefixed by A." / "Classes that inherit from SWidget are
prefixed by S." / "Classes that are abstract interfaces are prefixed by I." / "Enums are
prefixed by E." / "Boolean variables must be prefixed by b." / "Most other classes are prefixed
by F" — https://dev.epicgames.com/documentation/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine (accessed 2026-11-18).

## Module basics

- Each module holds many C++ classes; declare module dependencies in the module's `.Build.cs`
  (e.g. `"Core", "CoreUObject", "Engine"`). Missing deps = unresolved-symbol link errors.
- A `.Build.cs` declares the module; a `.Target.cs` declares the build target.

## Load-bearing rules (community, re-verify against API ref where load-bearing)

- Header layout: `UCLASS()` above the class, `GENERATED_BODY()` as first line of the body, and
  `#include "ClassName.generated.h"` as the **last include**. UHT requires this.
- GC only tracks `UPROPERTY()`-marked pointers; a raw `UObject*` member without `UPROPERTY()`
  dangles. In UE5 use `TObjectPtr<T>` for `UPROPERTY` object members.
- Use `CreateDefaultSubobject<T>(TEXT("Name"))` in constructors for components.
- Do not use `TSharedPtr` on UObjects (GC/refcount conflict).

## Verify-first

Re-verify the exact macro signatures and specifiers against the API reference before relying on
them in code: https://dev.epicgames.com/documentation/en-us/unreal-engine/API.
