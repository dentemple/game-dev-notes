---
title: UE Performance & Profiling
tags: [performance, profiling, frame-budget, stat-unit, gpu, cpu, insights, optimization]
source: https://www.intel.com/content/www/us/en/developer/articles/technical/unreal-engine-optimization-profiling-fundamentals.html (accessed 2026-11-18)
updated: 2026-11-18
---

# UE Performance & Profiling

## Frame budgets (primary)

- "Frame Budgets are: 33.33ms for 30 FPS, 16.66ms for 60 FPS." 120 FPS = 8.33ms.
- Both CPU and GPU must fit inside the budget or the frame is missed.

## Measure first (primary)

- "the best approach is to use a packaged build, preferably **Test** Configuration" — the editor and **Development** builds skew results substantially.
- Start with `stat unit` / `stat gpu`: "if the Draw Time is ~95% of Frame Time it is an indicator that it is GPU-Bound"; if Game Time ≈ Frame Time and Draw Time < 90%, it's CPU-bound.
- **Unreal Insights** (trace-based timing) and **CSVProfiler** ("a built-in lightweight profiler that gathers per-frame metrics") for deeper dives.
Source: https://www.intel.com/content/www/us/en/developer/articles/technical/unreal-engine-optimization-profiling-fundamentals.html (accessed 2026-11-18).

## Common bottlenecks (practitioner)

- GPU-bound: Lumen/Nanite suitability, resolution/upscaling (TSR), post-processing, translucency/particle overdraw.
- CPU-bound: draw calls (instancing/merging), Blueprint Tick (move to events/timers), physics/animation, garbage collection.
- Shader/PSO stutter: PSO precaching and cache warm-up from real playthroughs.
Source: https://www.strayspark.studio/blog/ue5-performance-profiling-101 (accessed 2026-11-18).

## Note for solo dev

Profile packaged builds early, fix the measured bottleneck (not guesses), and re-measure after each change — one variable at a time.
