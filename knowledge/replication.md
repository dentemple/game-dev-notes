---
title: Property Replication
tags: [replication, networking, replicated, dorplifetime, onrep, server]
source: https://dev.epicgames.com/documentation/unreal-engine/property-replication-in-unreal-engine (accessed 2026-11-18)
updated: 2026-11-18
---

# Property Replication

## Direction and reliability (primary)

- "The server will send an update to each client whenever a replicated property changes its
  value."
- "the client will never send property updates to the server or other clients."
- "Actor property replication is reliable."
- Source: https://dev.epicgames.com/documentation/unreal-engine/property-replication-in-unreal-engine (fetched `?application_version=5.0&lang=en-US`, accessed 2026-11-18).

## Three steps to replicate a property (primary)

1. Mark with `UPROPERTY(Replicated)` (or `ReplicatedUsing=OnRep_X` for a RepNotify callback):
   `UPROPERTY(Replicated) uint32 Health;`
2. Set `bReplicates = true;` in the constructor.
3. Register it in `GetLifetimeReplicatedProps` — always call `Super::` first:
   ```cpp
   #include "Net/UnrealNetwork.h"
   void AThing::GetLifetimeReplicatedProps(TArray<FLifetimeProperty>& OutLifetimeProps) const {
       Super::GetLifetimeReplicatedProps(OutLifetimeProps);
       DOREPLIFETIME(AThing, Health);
   }
   ```
   (Primary: "you need to make sure you have the `replicated` keyword as one of the parameters
   to the UPROPERTY declaration" and "you need to implement the GetLifetimeReplicatedProps
   function:" with `DOREPLIFETIME( AActor, Owner );`.)

## Verify-first

- Confirm `ReplicatedUsing` / `OnRep_` exact signature against the "Replicate Actor Properties"
  page before use (the primary page above did not cover `ReplicatedUsing`).
- Reliable = clients converge on the server value but may skip intermediate changes (100→300,
  not 200). Clients must not mutate replicated state.
