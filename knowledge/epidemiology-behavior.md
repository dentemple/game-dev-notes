---
title: Epidemiology & Population Models (SIR, Lotka-Volterra, Corrupted Blood)
tags: [behavior, epidemiology, sir, seir, pathogen, population, lotka-volterra, agent-based, cellular-automata, corrupted-blood, simulation]
source: https://en.wikipedia.org/wiki/Corrupted_Blood_incident (accessed 2026-11-18)
updated: 2026-11-18
---

# Epidemiology & Population Models (SIR, Lotka-Volterra, Corrupted Blood)

## Goal & scope

Algorithmic models of pathogens and populations, plus the Corrupted Blood case study — and the *behavior*
lesson they teach for simulation design. Companion to simulation-agents.md (needs/utility/directors) and
emergent-behavior.md (emergence).

## Primary sources

- **Wikipedia — Corrupted Blood incident** — https://en.wikipedia.org/wiki/Corrupted_Blood_incident (accessed 2026-11-18)
- **EurekAlert — Lofgren & Fefferman** — https://www.eurekalert.org/news-releases/815479 (accessed 2026-11-18)
- **Epidemiological / population models** (RESEARCH) — SIR/SEIR, Lotka-Volterra (accessed 2026-11-18)

## Pathogen models (RESEARCH)

- **SIR / SEIR** (Kermack–McKendrick 1927): divide a population into Susceptible / Exposed / Infectious /
  Recovered compartments; the key threshold is **R0** (basic reproduction number) — spread if >1, die-out
  if <1. Variants: SIS (no immunity), SEIRS (temporary immunity).
- **ODE vs. spatial models**: ODE compartmental models assume a *well-mixed* population (analytically
  tractable); **cellular automata / agent-based models** capture *spatial* heterogeneity and local
  interaction (e.g., neighborhood size as social-distancing proxy). Combine them for rigor + spatial realism.

## Population effects (RESEARCH)

- **Lotka-Volterra** predator-prey: the classic two-equation model; the standard fix is **logistic growth
  with a carrying capacity K** (otherwise it has unrealistic neutral oscillations). Generalizes to food
  webs via the generalized Lotka-Volterra matrix.

## The Corrupted Blood incident

In Sept 2005, Zul'Gurub boss **Hakkar the Soulflayer** cast a **"Corrupted Blood"** debuff meant to last
10 seconds / until Hakkar died. It escaped because "developers had forgotten to include an 'off-switch'":
infected hunter **pets in suspended animation** (and NPCs that "became asymptomatic carriers") carried it
out of the raid. The result was a genuine virtual pandemic — "Corrupted Blood quickly became pandemic in
Azeroth," with 4M+ subscribers, outbreaks in the capital cities, 263-337 damage every 2 seconds, and no
in-game cure. Blizzard's **quarantine failed** ("some players managed to bypass Blizzard's containment
measures"), and after a week they **hard-reset the servers**.

## The academic lesson

Lofgren & Fefferman's core argument: **"human-agent virtual simulation may bridge the gap between
real-world epidemiological studies and large-scale computer studies"** — by "including the variability and
unexpected outcomes that arise as a result of the behaviour of individuals," because "players' economic
and social behaviour often mimics their real-world behaviour."

Observed behaviors (RESEARCH): altruism (players rushing in to heal), quarantine defiance ("the stupid
factor" — getting close "just to look"), deliberate super-spreaders/griefers, and scapegoating/misinformation
(hunters blamed). These map directly onto COVID-era phenomena (teleport ≈ air travel; social-distancing
compliance; misinformation). Later virtual-epidemic experiments confirmed the pattern: **free-riding**
(deferring vaccination when surrounded by the immunized), **social learning**, and players **transferring
real-world tendencies** into the game.

## Lessons for modeling behavior (ANALYSIS)

1. **Heterogeneous agent types, not uniform rules** — the outbreak was shaped by carriers, healers,
   griefers, and fleers. Model *distinct behavioral roles*, not one average agent.
2. **Behavior matters as much as R0** — the pathogen math gives the ceiling; the *social response* sets
   the actual curve.
3. **Virtual worlds are behavioral labs** — real human decisions (altruism/panic/rule-breaking) emerge
   where scripted agent models can't reproduce them.
4. **Capture data as it happens** — the Corrupted Blood lesson's biggest miss was *no systematic logging*
   during the outbreak; instrument your sim from day one.

## Anti-patterns / gotchas

- Modeling a population as uniform well-mixed agents (misses the whole behavioral lesson).
- Ignoring that in-game behavior may not perfectly generalize to real-world behavior.
- No data capture — you can't learn from an emergent event you didn't log.

## Verify-first

Re-verify the SIR/Lotka-Volterra equations against a standard reference and the Corrupted Blood specifics
against Wikipedia before quoting them; the *pattern* (heterogeneous agents + social response + logging) is
robust regardless.
