# Research requests (unreal-engine-dev → agent-researcher)

`unreal-engine-dev` writes a brief here when a task needs research the store
does not cover. `agent-researcher` picks it up, researches it, and writes the
curated topic plus its index row. The engineering agent does not do open-ended
discovery itself; it may only fetch a URL the store already cites to check a
load-bearing claim.

## Brief template

```markdown
# <Topic>

- Requested by: unreal-engine-dev
- Date: YYYY-MM-DD
- Why (blocking task): <what you are trying to build or decide>
- Questions: <3–6 concrete questions>
- Already checked: <URLs / file:line and what they did or did not answer>
- Desired output: `knowledge/<slug>.md` or `knowledge/features/<slug>.md` + index row
- Notes: <engine version, project constraints, related topics>
```

## Accepted order (from the 2026-11-18 review)

1. UMG / UI (Widget Blueprint, Slate)
2. Animation (Animation Blueprint, montages, Anim Notify)
3. Physics / collision / traces
4. Navigation / NavMesh / AI perception
5. RPCs / replication graph / multiplayer architecture
6. Build / cook / package
7. Audio / MetaSounds
8. Rendering / materials / Niagara
9. Plugin authoring
