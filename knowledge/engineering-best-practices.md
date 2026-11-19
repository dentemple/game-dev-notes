---
title: Engineering Best Practices (Patterns & Anti-Patterns)
tags: [best-practices, patterns, kiss, yagni, tick, cast, blueprint, cpp, anti-pattern]
source: https://gameprogrammingpatterns.com/architecture-performance-and-games.html (accessed 2026-11-18)
updated: 2026-11-18
---

# Engineering Best Practices (Patterns & Anti-Patterns)

## The first rule (primary)

"it's easier to make a fun game fast than it is to make a fast game fun." Prototype first: "keep the code flexible until the design settles down and then tear out some of the abstraction later." "If you are going to ditch code, don't waste time making it pretty."
Source: https://gameprogrammingpatterns.com/architecture-performance-and-games.html (accessed 2026-11-18).

## KISS / prototype discipline (primary)

"Rule #1 - Do not optimize. Rule #2 - Do not overcomplicate. Rule #3 - Prototype." "The user doesn't really care if your code follows conventions or if it is optimized."
Source: https://www.gamedeveloper.com/programming/just-make-the-prototype-work- (accessed 2026-11-18).

## Pattern catalog (primary reference)

Nystrom's *Game Programming Patterns* — reach for a pattern when a concrete problem appears, not before:

- **Decoupling**: Component, Event Queue, Service Locator.
- **Behavior**: State, Observer, Command.
- **Sequencing**: Game Loop, Update Method, Double Buffer.
- **Optimization**: Data Locality, Object Pool, Dirty Flag, Spatial Partition.
Source: https://gameprogrammingpatterns.com (accessed 2026-11-18).

## UE anti-patterns (practitioner consensus)

- **Tick overuse**: prefer event-driven logic, timers, or tick intervals; disable Tick unless truly per-frame. Avoid heavy work in Tick (line traces, GetAllActorsOfClass, casting).
- **Cast ladders**: "never use Cast" is a myth — Cast is cheap (~0.5µs C++, ~3.5µs BP); the real cost is hard references / load-time dependencies. Prefer interfaces for soft references.
- **Blueprint vs C++ split**: keep performance-critical, frequently-called logic in C++; Blueprint for glue and flow.
- Disable "Start with Tick Enabled" by default; validate references (`IsValid`); avoid non-deterministic randomness in Construction Scripts.
Source: Epic "Myth-busting Best Practices" tutorial + community consensus (accessed 2026-11-18; RESEARCH).

## Over-engineering warning (RESEARCH consensus)

Premature abstraction is a "loan" that may never be repaid; most indie games die from code that is "too clean to finish," not from messy code. Two exceptions worth doing early: a **save/state layer** and **input mapping**.
Source: Unity/Godot/LinkedIn consensus (accessed 2026-11-18).

## Note for solo dev

The bottleneck is motivation, not architecture. Ship a playable prototype fast; refactor when a real problem forces it.
