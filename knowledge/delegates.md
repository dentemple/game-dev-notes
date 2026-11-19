---
title: Delegates
tags: [delegate, multicast, dynamic, broadcast, blueprintassignable]
source: https://dev.epicgames.com/documentation/unreal-engine/multicast-delegates-in-unreal-engine (accessed 2026-11-18)
updated: 2026-11-18
---

# Delegates

## Multicast (primary)

- `DECLARE_MULTICAST_DELEGATE[_RetVal, ...]( DelegateName )` — "Creates a multi-cast delegate."
- `DECLARE_DYNAMIC_MULTICAST_DELEGATE[_RetVal, ...]( DelegateName )` — "Creates a dynamic
  multi-cast delegate."
- `Broadcast()` — "Broadcasts this delegate to all bound objects, except to those that may have
  expired." Multicast delegates return no value and execution order is not guaranteed; calling
  `Broadcast()` unbound is always safe.
- Source: https://dev.epicgames.com/documentation/unreal-engine/multicast-delegates-in-unreal-engine (accessed 2026-11-18).

## Binding functions (primary, same page)

`Add()`, `AddStatic()`, `AddRaw()`, `AddLambda()`, `AddSP()`, `AddUObject()`, `AddWeakLambda()`,
`Remove()`, `RemoveAll()`.

## Dynamic vs non-dynamic (community, re-verify if load-bearing)

- `DECLARE_DYNAMIC_DELEGATE` / `DECLARE_DYNAMIC_MULTICAST_DELEGATE` bind `UFUNCTION`s and are
  Blueprint-visible; expose with `UPROPERTY(BlueprintAssignable)`; bind via `BindDynamic()` /
  `AddDynamic()` / `RemoveDynamic()`.
- Non-dynamic (`DECLARE_DELEGATE`, `DECLARE_MULTICAST_DELEGATE`) bind C++ functions only, faster
  (no reflection lookup), not Blueprint-exposed.
- Execution: `Execute()`, `ExecuteIfBound()`, `IsBound()`.

## Verify-first

Confirm the exact macro arity/parameter forms against
https://dev.epicgames.com/documentation/unreal-engine/dynamic-delegates-in-unreal-engine before
use.
