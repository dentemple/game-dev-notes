---
title: Agentic AI (Unreal MCP & AI Agents)
tags: [ai, mcp, agent, llm, claude-code, codex, cursor, toolset, assistant]
source: https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor (accessed 2026-11-18)
updated: 2026-11-18
---

# Agentic AI (Unreal MCP & AI Agents)

## Unreal MCP (primary, Experimental)

Unreal MCP is an **Experimental** editor plugin that "embeds a Model Context Protocol (MCP) server
inside the Unreal Editor." Epic's guidance: "Use caution when shipping a project with it." It exposes
engine functionality — actors, Blueprints, UMG, materials, MetaSounds, PCG, Niagara, Sequencer, Slate
inspection, automation tests — as callable tools via a **Toolset Registry**.
Source: https://dev.epicgames.com/documentation/unreal-engine/unreal-mcp-in-unreal-editor (accessed 2026-11-18).

- Loopback-only, no auth: "only accepts connections from the same machine, has no authentication
  layer, and isn't designed for remote use."
- Transport: "Supports Streamable HTTP and Server-Sent Events (SSE) only" (no stdio/WebSocket); tool
  calls run one at a time on the game thread.
- Tool search (default on) returns four discovery meta-tools instead of every tool: `list_toolsets`,
  `describe_toolsets`, `describe_tools`, `call_tool`.

## Supported agents and setup

- Agents: "Claude Code, Codex, Cursor, Gemini CLI, Visual Studio Code with GitHub Copilot, or the
  MCP Inspector." The 5.9 **Unreal Assistant** panel also runs OpenCode and custom ACP agents.
- Setup: enable **Unreal MCP** + **All Toolsets** plugins, confirm auto-start (on by default), generate
  a client config (`ModelContextProtocol.GenerateClientConfig <Client>`), then launch the agent from
  the folder holding the config.

## Extending (custom toolsets)

- Author toolsets in Python (`unreal.ToolsetDefinition`) or C++ (`UToolsetDefinition`); metadata:
  `AICallable`, `AIRuntimeCallable` (safe in cooked/runtime builds), `AIAccessMode` (Read/Write/Execute).
- `ModelContextProtocol.RefreshTools` after authoring. "Live Coding doesn't pick up new `UFUNCTION`
  declarations" — a new `UFUNCTION` needs a full editor restart.

## UE 5.9 additions (primary)

- A Knowledge Base that "lets the assistant and agents query knowledge built from the live engine
  state," plus Semantic Search, Fab image/mesh generation, and a per-agent tool-access setting
  (Ask, Read, Edit, Auto, Full).
  Source: https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-5-9-release-notes (accessed 2026-11-18).
- Epic on 5.9 Preview: "is the first Unreal Engine release built primarily with agentic workflows" —
  "A handful of people directed fleets of agents to port the AI tooling from our UE6 development
  branch." Source: https://forums.unrealengine.com/t/unreal-engine-5-9-megajam-preview/2852840 (accessed 2026-11-18).

## Third-party ecosystem (self-reported; not independently tested)

- Autonomix, Unreal-MCP (IvanMurzak), UnrealMasterAI, unreal-api-mcp, Tether, mcp-unreal-agent,
  Convai. These are editor plugins / MCP servers that give agents read/write control over the editor.
- unreal-api-mcp is a version-specific (UE 5.5–5.8) API lookup that prevents hallucinated signatures,
  wrong `#include` paths, and deprecated-API use; benchmark 14/14 vs 11/14 vs 12/14, and "the gap
  opens on recent deprecations" (e.g. `IsSplitScreen` → `HasMultipleLocalPlayers` in 5.8).
  Source: https://github.com/codeturion/unreal-api-mcp (accessed 2026-11-18).

## Limitations (load-bearing — re-verify before relying)

- Experimental: APIs and data formats may change.
- **Hallucination is the main failure mode** — models invent API signatures and use deprecated APIs
  across versions. Verify generated code against the version-specific API reference before relying on it.
- Practitioner field report (April 2026): reliable for asset setup/configuration, boilerplate, test
  scaffolding, batch operations, docs/CI; unreliable for runtime debugging, multiplayer
  (replication/authority/prediction/lag compensation), complex material graphs, and feel/balance
  tuning ("Agents are bad at runtime debugging in UE"; replication/prediction yields "confidently
  wrong answers").
  Source: https://www.strayspark.studio/blog/autonomous-ai-agents-unreal-development-april-2026 (accessed 2026-11-18).
- Cooked/shipping builds expose only `AIRuntimeCallable` tools (no reflection metadata at runtime).

## Verify-first

Re-verify agent-generated API signatures against
https://dev.epicgames.com/documentation/en-us/unreal-engine/API before relying on them in code.
