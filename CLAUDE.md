# game-dev-notes

A home for the `unreal-engine-dev` Claude Code agent — game development and
software engineering for Unreal Engine (C++ and Blueprint). This checkout is
the planning and knowledge workspace; the game project may live in a separate
directory. Until a `.uproject` is present, the agent operates in planning mode
and does not build or test.

## Invocation and discovery

- The definition lives at `.claude/agents/unreal-engine-dev.md`. Claude Code
  scans `.claude/agents/` at session start, so a session opened in this
  directory (or a subdirectory) discovers it automatically.
- Invoke explicitly with `@agent-unreal-engine-dev` — the mention form is
  `@agent-<name>`, and the name is `unreal-engine-dev`. The description also
  triggers automatic delegation for Unreal engineering and debugging work.

## Standing rules

- When a project is present, the agent and the human each run the build and
  automation tests independently as a cross-check; the human commits. In this
  planning checkout (no `.uproject`), the agent does not build or test.
- No claimed-working code without a clean compile and passing automation tests
  (output shown). In planning mode, never claim a build or test result.
- Knowledge lives in committed files, never memory-only. The agent's own
  durable working memory lives in `knowledge/agent-memory/`.

## Knowledge store

- `agent-researcher` curates the on-demand knowledge store at `knowledge/`;
  `unreal-engine-dev` reads it on demand — index first
  (`knowledge/README.md`, then `knowledge/features/README.md` for a feature),
  then only the relevant topic files.
- `unreal-engine-dev` does not edit curated topics or indexes. It writes
  research briefs to `knowledge/research-requests/` and its own notes to
  `knowledge/agent-memory/`.
- The store is the durable home for domain notes — commit it.

## Write guard

- `.claude/settings.json` installs `scripts/guard_writes.py` as a PreToolUse
  hook for `unreal-engine-dev`.
- It denies `CLAUDE.md`, `CLAUDE.local.md`, `AGENTS.md`, `.claude/`, `.git/`,
  and curated `knowledge/` topics/indexes.
- It allows `knowledge/agent-memory/` and `knowledge/research-requests/` in
  both modes. With no `.uproject` it is planning mode: code writes and
  build/test commands are denied.
- The guard is a safety net, not an OS sandbox; the prompt rules still apply.

## Gotchas

- A session started before `.claude/agents/` existed does not discover agents
  until it is restarted.
- The definition pins `model: deepseek-v4-pro[1m]` for DeepSeek backends. On a
  vanilla Anthropic backend, change it to `sonnet` (implementation work) or
  `opus` (architecture-heavy work). The `[1m]` suffix is a client context
  annotation, not part of the API model ID; the harness logs an
  `unrecognized_model` notice for the custom provider ID but honors the 1M
  window. The plain ID makes the harness assume 200K and auto-compact, so keep
  the annotation.
- This checkout is planning-only until a `.uproject` is present. The agent will
  not build or test here; it hands the exact commands to the human.
- `--bare`, `--safe-mode`, and `--disable-slash-commands` can suppress
  discovery; use plain sessions when testing agents.
- This directory is not yet a git repository — run `git init` and commit before
  relying on durability.
