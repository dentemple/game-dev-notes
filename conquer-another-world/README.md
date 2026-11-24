# Conquer Another World

## Project Setup

### 1. Verify the Unreal Engine install

- Windows/macOS: open Epic Games Launcher → Unreal Engine → Library and confirm the installed engine slot and exact version (latest 5.8.x patch).
- Linux: confirm the installed engine path and version in `Engine/Build/Build.version`.
- Use a stable 5.8.x release; skip the 5.9 Preview (unstable, full release planned for 2027).
- Click the version dropdown → Verify to re-check the installation files.
- Install to an ASCII path with no spaces; keep 100+ GB free.

### 2. Install the C++ toolchain

- Windows: Visual Studio 2022 version 17.8 or later (17.14 recommended). VS 2019 is unsupported; VS 2026 is experimental only.
- Sele#ct workloads: Game development with C++, Desktop development with C++, .NET desktop development.
- Select components: MSVC v143, Windows 10/11 SDK 10.0.18362+ (10.0.22621+ recommended), C++ profiling tools.
- Linux: clang 18.1.x, .NET 8 SDK, and the standard UE Linux build prerequisites.

### 3. Set up version control

- Install Git and Git LFS, then run `git lfs install`.
- Set `git config --global user.name "..."` and `git config --global user.email "..."`.
- Run `git init` in this directory.
- Add the standard Unreal `.gitignore` and `.gitattributes` before the first `.uproject` exists; route `*.uasset`, `*.umap`, `*.ubulk`, and `*.uexp` through Git LFS.

### 4. Install Claude Code

- Windows PowerShell: `irm https://claude.ai/install.ps1 | iex`
- Linux/macOS: `curl -fsSL https://claude.ai/install.sh | bash`
- Alternative (needs Node.js 18+): `npm install -g @anthropic-ai/claude-code`
- Verify with `claude --version` and `claude doctor`.

### 5. Get DeepSeek credentials

- Create an API key at platform.deepseek.com and add account credit.
- Store the key as a secret; never put it in the repository or commit it.

### 6. Point Claude Code at DeepSeek

- Set these persistent user environment variables (Windows `setx`, or append exports to `~/.bashrc`/`~/.zshrc`):

```bash
export ANTHROPIC_BASE_URL="https://api.deepseek.com/anthropic"
export ANTHROPIC_AUTH_TOKEN="<your DeepSeek API key>"
export ANTHROPIC_MODEL="deepseek-flash[1m]"
export ANTHROPIC_DEFAULT_OPUS_MODEL="deepseek-flash[1m]"
export ANTHROPIC_DEFAULT_SONNET_MODEL="deepseek-flash[1m]"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="deepseek-flash"
export CLAUDE_CODE_SUBAGENT_MODEL="deepseek-flash"
export CLAUDE_CODE_EFFORT_LEVEL="max"
export CLAUDE_CODE_AUTO_COMPACT_WINDOW="786432"
```

- Remove any existing `ANTHROPIC_API_KEY` and do not run an Anthropic `/login`; the DeepSeek token is the only credential.
- Open a new terminal so the variables take effect.
- Optional: use `ANTHROPIC_MODEL="deepseek-v4-pro[1m]"` for harder engineering work (billed at the higher V4 Pro rate).

### 7. Smoke-test before creating the project

- Run `cd /home/owl/dev/game-dev-notes/conquer-another-world && claude`.
- Confirm `/status` shows the expected DeepSeek model and that no Anthropic login or subscription is required.
- Run one tool-using prompt (for example, "create test.txt, then read it back") and verify the file operations work.
- Confirm `claude doctor` reports no errors; then delete the test file.

### 8. Create and compile the project

- Launch the 5.8.x editor (Epic Games Launcher on Windows/macOS; the installed `UnrealEditor` binary on Linux) → New Project → Games → Blank (C++) → Desktop.
- Set the parent location to the repo root (`/home/owl/dev/game-dev-notes/conquer-another-world` on this machine), name it `ConquerAnotherWorld`, and create it.
- Windows: if a `.sln` is not generated, right-click the `.uproject` → Generate Visual Studio project files, then build `Development Editor` / `Win64` and confirm 0 errors.
- Linux: build the `Development Editor` target with the engine's Linux build script and confirm 0 errors.
- Launch the project, run Play-In-Editor, and confirm the default map loads before adding any content.
- Confirm the Git LFS rules cover `*.uasset`, `*.umap`, `*.ubulk`, and `*.uexp`, then commit the generated project.
- Optional: Edit → Revision Control → Connect Revision Control → Git LFS 2, and verify the settings.

### 9. Enable the Unreal MCP server

- Edit → Plugins: enable **Unreal MCP** and **All Toolsets**, then restart the editor.
- Edit → Editor Preferences → Agentic Workflows → Model Context Protocol: enable **Auto Start Server**.
- Confirm the default endpoint `http://127.0.0.1:8000/mcp` (port 8000, path `/mcp`).
- In the editor console, run `ModelContextProtocol.GenerateClientConfig ClaudeCode`; this writes `.mcp.json` to the project root:

```json
{
  "mcpServers": {
    "unreal-mcp": {
      "type": "http",
      "url": "http://127.0.0.1:8000/mcp"
    }
  }
}
```

- If auto-start is off, run `ModelContextProtocol.StartServer`; stop it with `ModelContextProtocol.StopServer`.
- Note: the server is loopback-only and unauthenticated, and tool calls run serially on the game thread.

### 10. Connect Claude Code to the editor

- With the editor and MCP server running, set `TERM=xterm-256color` in the terminal to avoid degraded output.
- From the directory containing `.mcp.json`, run `claude` and approve the project-scoped `unreal-mcp` server.
- Confirm `/mcp` lists `unreal-mcp` as connected.
- Smoke-test with "What actors do I have selected?" or "What toolsets are available, and what can you do with them?"
- Split long editor tasks into short calls: Claude Code times out around 120 seconds, and overlapping calls are not supported.
- Optional: UE 5.9's Unreal Assistant panel supports Claude Code without `.mcp.json`, one editor at a time.
- Optional: install Epic's Claude Code plugin with `/plugin install unreal-engine-skills-for-claude-code@claude-plugins-official`; it adds the `unreal-mcp`, `create-toolset`, and `unreal-skill` skills.
