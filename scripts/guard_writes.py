#!/usr/bin/env python3
"""PreToolUse guard — scope unreal-engine-dev writes.

The hook input carries `agent_type`, so this guard can distinguish the Unreal
subagent from the main session. It is a safety net, not an OS sandbox: it
covers Write/Edit and the common Bash write forms, not arbitrary code that
opens files itself.

Rules for `unreal-engine-dev`:

- Instruction and history surfaces are always denied: `.claude/`, `.git/`,
  `CLAUDE.md`, `CLAUDE.local.md`, and `AGENTS.md`.
- The curated knowledge store is agent-researcher's: writes under `knowledge/`
  are allowed only in `knowledge/agent-memory/` and
  `knowledge/research-requests/`.
- When no `.uproject` is present, planning mode applies: writes are limited to
  those two knowledge paths, and build/test commands are denied.
- When a `.uproject` is present, implementation mode applies: project code and
  tests may be written anywhere inside the project or its immediate parent.
- `git commit`/`push`/`reset --hard`/`clean -f` and destructive `rm -rf` are
  denied; the human owns git history.

Exit 0 = allow; exit 2 = block (stderr is fed back to the agent).
"""

import json
import os
import re
import sys
from pathlib import Path

AGENT = "unreal-engine-dev"
BLOCKED_NAMES = {"claude.md", "claude.local.md", "agents.md"}
BLOCKED_DIRS = {".claude", ".git"}
ALLOWED_STORE_SUBDIRS = ("agent-memory", "research-requests")

BUILD_RE = re.compile(
    r"(?:Build\.bat|UnrealBuildTool|UnrealEditor-Cmd|Automation\s+RunTests)",
    re.IGNORECASE,
)
GIT_DENY_RE = re.compile(
    r"\bgit\s+(?:commit|push|reset\s+--hard|clean\s+-[a-z]*f)", re.IGNORECASE
)
RM_DENY_RE = re.compile(r"\brm\s+-[a-z]*[rf]", re.IGNORECASE)
WRITE_RE = re.compile(r"(?<![0-9])>>?\s*([^\s;|&]+)")
TEE_RE = re.compile(r"\btee\s+(?:-a\s+)?([^\s;|&]+)")
CP_MV_RE = re.compile(r"\b(?:cp|mv|rm)\s+([^;|&]+)")
SED_I_RE = re.compile(r"\b(?:sed|perl)\b[^;|&]*\s-[a-z]*i[^;|&]*", re.IGNORECASE)
BYPASS_RE = re.compile(
    r"(?:\bopen\s*\(|\bwrite_text\s*\(|\bwrite_bytes\s*\(|"
    r"\b(?:sed|perl)\b[^;|&]*\s-[a-z]*i|\b(?:cp|mv|rm|tee)\b)",
    re.IGNORECASE,
)
DENIED_TOKENS = ("CLAUDE.md", "CLAUDE.local.md", "AGENTS.md", ".claude/", ".git/")


def is_agent(agent_type):
    """True for the bare name and plugin-prefixed forms."""
    if not agent_type:
        return False
    return (
        agent_type == AGENT
        or agent_type.endswith(":" + AGENT)
        or agent_type.endswith("/" + AGENT)
    )


def allowed_roots(cwd):
    """The project root and its immediate parent."""
    roots = [cwd]
    if cwd.parent != cwd:
        roots.append(cwd.parent)
    return roots


def project_root(payload, cwd):
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or cwd).resolve()


def store_root(payload, cwd):
    return project_root(payload, cwd) / "knowledge"


def has_project(root):
    """A .uproject at the root or one level down means implementation mode."""
    try:
        if any(root.glob("*.uproject")):
            return True
        return any(root.glob("*/*.uproject"))
    except OSError:
        return False


def resolve_target(raw, cwd):
    target = Path(raw)
    if not target.is_absolute():
        target = cwd / target
    return target.resolve()


def relative_to_roots(target, roots):
    for root in roots:
        try:
            return target.relative_to(root)
        except ValueError:
            continue
    return None


def is_instruction_surface(rel):
    """Deny instruction and history surfaces wherever they appear."""
    parts = rel.parts
    if any(part.lower() in BLOCKED_DIRS for part in parts):
        return True
    return bool(parts and parts[-1].lower() in BLOCKED_NAMES)


def in_allowed_store(target, store):
    for sub in ALLOWED_STORE_SUBDIRS:
        try:
            target.relative_to(store / sub)
            return True
        except ValueError:
            continue
    return False


def is_curated_store_path(target, store):
    try:
        target.relative_to(store)
        return not in_allowed_store(target, store)
    except ValueError:
        return False


def is_store_protocol(target, store):
    """The memory/research-request READMEs define the handoff protocol."""
    return target in {
        (store / "agent-memory" / "README.md").resolve(),
        (store / "research-requests" / "README.md").resolve(),
    }


CODE_PATH_RE = re.compile(r"(?<![\w.-])((?:[\w.-]+/)+[\w.-]+)")
REPO_PREFIXES = (
    "knowledge/",
    ".claude/",
    ".git/",
    "Source/",
    "Content/",
    "Config/",
    "Plugins/",
    "Binaries/",
    "Intermediate/",
    "Saved/",
)
REPO_SUFFIXES = (".md", ".cpp", ".h", ".cs", ".json", ".ini", ".py", ".txt", ".uproject")


def looks_like_repo_path(raw):
    if "://" in raw:
        return False
    return raw.startswith(REPO_PREFIXES) or raw.endswith(REPO_SUFFIXES)


def bash_write_targets(command):
    """Extract likely write destinations from common shell forms."""
    targets = []
    for regex in (WRITE_RE, TEE_RE):
        targets.extend(regex.findall(command))
    for chunk in CP_MV_RE.findall(command):
        parts = chunk.split()
        if parts:
            targets.append(parts[-1])
    if SED_I_RE.search(command):
        for part in re.split(r"[;|&]", command):
            if re.search(r"\b(?:sed|perl)\b", part, re.IGNORECASE):
                tokens = part.split()
                if tokens:
                    targets.append(tokens[-1])
    return [t.strip("'\"") for t in targets if t and not t.startswith("-")]


def decide_write(payload):
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        return 2, "unreal-engine-dev write has no usable tool_input; denied"
    raw_path = tool_input.get("file_path") or tool_input.get("path")
    if not isinstance(raw_path, str) or not raw_path:
        return 2, "unreal-engine-dev write has no file_path; denied"
    cwd = Path(payload.get("cwd") or os.getcwd()).resolve()
    try:
        target = resolve_target(raw_path, cwd)
    except (OSError, RuntimeError) as exc:
        return 2, f"unreal-engine-dev path cannot be resolved ({exc}); denied"

    rel = relative_to_roots(target, allowed_roots(cwd))
    if rel is None:
        return 2, (
            "unreal-engine-dev may write only inside this project, its sibling "
            f"directories, or its immediate parent; denied {target}"
        )
    if is_instruction_surface(rel):
        return 2, (
            "unreal-engine-dev may not write instruction/history surfaces "
            f"(CLAUDE.md, CLAUDE.local.md, AGENTS.md, .claude/, .git/); denied {rel}"
        )

    store = store_root(payload, cwd)
    if is_curated_store_path(target, store):
        return 2, (
            "curated knowledge topics/indexes belong to agent-researcher; use "
            f"knowledge/research-requests/ or knowledge/agent-memory/; denied {rel}"
        )
    if is_store_protocol(target, store):
        return 2, (
            "the memory/research-request READMEs define the protocol and are "
            f"not agent-writable; denied {rel}"
        )

    if not has_project(project_root(payload, cwd)) and not in_allowed_store(target, store):
        return 2, (
            "planning mode: no .uproject is present; writes are limited to "
            f"knowledge/agent-memory/ and knowledge/research-requests/; denied {rel}"
        )
    return 0, ""


def decide_bash(payload):
    tool_input = payload.get("tool_input")
    if not isinstance(tool_input, dict):
        return 0, ""
    command = tool_input.get("command")
    if not isinstance(command, str) or not command.strip():
        return 0, ""

    cwd = Path(payload.get("cwd") or os.getcwd()).resolve()
    root = project_root(payload, cwd)
    store = store_root(payload, cwd)

    if GIT_DENY_RE.search(command):
        return 2, "git history is human-owned; do not commit/push/reset/clean"
    if RM_DENY_RE.search(command):
        return 2, "destructive rm is not allowed"
    if not has_project(root) and BUILD_RE.search(command):
        return 2, "planning mode: no .uproject is present; do not run a build/test"

    lowered = command.lower()
    if any(token.lower() in lowered for token in DENIED_TOKENS) and BYPASS_RE.search(command):
        return 2, "unreal-engine-dev may not write instruction/history surfaces via Bash"

    # Catch simple code-based writes (open(), write_text(), etc.) that do not
    # use a shell redirection.
    if BYPASS_RE.search(command):
        for raw in CODE_PATH_RE.findall(command):
            if not looks_like_repo_path(raw):
                continue
            try:
                target = resolve_target(raw, cwd)
            except (OSError, RuntimeError):
                continue
            rel = relative_to_roots(target, allowed_roots(cwd))
            if rel is None:
                continue
            if is_instruction_surface(rel):
                return 2, (
                    "unreal-engine-dev may not write instruction/history surfaces "
                    f"via Bash; denied {rel}"
                )
            if is_curated_store_path(target, store):
                return 2, (
                    "curated knowledge topics/indexes belong to agent-researcher; "
                    f"denied {rel}"
                )
            if is_store_protocol(target, store):
                return 2, (
                    "the memory/research-request READMEs define the protocol and "
                    f"are not agent-writable; denied {rel}"
                )
            if not has_project(root) and not in_allowed_store(target, store):
                return 2, (
                    "planning mode: no .uproject is present; Bash writes are limited "
                    f"to knowledge/agent-memory/ and knowledge/research-requests/; denied {raw}"
                )

    for raw in bash_write_targets(command):
        try:
            target = resolve_target(raw, cwd)
        except (OSError, RuntimeError):
            continue
        rel = relative_to_roots(target, allowed_roots(cwd))
        if rel is not None and is_instruction_surface(rel):
            return 2, (
                "unreal-engine-dev may not write instruction/history surfaces "
                f"via Bash; denied {rel}"
            )
        if is_curated_store_path(target, store):
            return 2, (
                "curated knowledge topics/indexes belong to agent-researcher; "
                f"denied {rel or target}"
            )
        if not has_project(root) and not in_allowed_store(target, store):
            return 2, (
                "planning mode: no .uproject is present; Bash writes are limited "
                f"to knowledge/agent-memory/ and knowledge/research-requests/; denied {raw}"
            )
    return 0, ""


def decide(payload):
    if not isinstance(payload, dict) or not is_agent(payload.get("agent_type")):
        return 0, ""
    tool_name = payload.get("tool_name")
    if tool_name in {"Write", "Edit", "MultiEdit", "NotebookEdit"}:
        return decide_write(payload)
    if tool_name == "Bash":
        return decide_bash(payload)
    return 0, ""


def main():
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError) as exc:
        print(f"guard_writes: unreadable hook input ({exc}); allowing", file=sys.stderr)
        return 0
    if not isinstance(payload, dict):
        print("guard_writes: hook input is not an object; allowing", file=sys.stderr)
        return 0
    code, message = decide(payload)
    if message:
        print(f"guard_writes: {message}", file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(main())
