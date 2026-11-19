---
title: Automation Testing
tags: [automation, fatomationtestbase, latent, command, runtests]
source: https://dev.epicgames.com/documentation/unreal-engine/write-cplusplus-tests-in-unreal-engine (accessed 2026-11-18)
updated: 2026-11-18
---

# Automation Testing

## Framework (primary)

- "The **Automation System** is built on top of the **Functional Testing Framework**."
- "You can use the **Automation Test Framework** to perform automated unit, feature, and content
  stress tests."
- Test types: functional, low-level core, and Editor tests. Tests can run out of order or
  parallel; do not assume game/Editor state.
- Source: https://dev.epicgames.com/documentation/unreal-engine/automation-test-framework-in-unreal-engine (accessed 2026-11-18).

## Writing a C++ test (primary)

- "Both types are implemented as derived classes based on `FAutomationTestBase`."
- "Simple Tests are declared using the `IMPLEMENT_SIMPLE_AUTOMATION_TEST` macro" — pass a class
  name, a hierarchical display string, and automation flags; override `RunTest`.
- `RunTest` "returning `true` to indicate that the test passed, or `false` to indicate that it
  failed."
- Source: https://dev.epicgames.com/documentation/unreal-engine/write-cplusplus-tests-in-unreal-engine (accessed 2026-11-18).

## Latent commands (re-verify exact signatures)

The official Automation Technical Guide documents latent commands for multi-frame work, but its
body was not extractable this session. Corroborated facts (re-verify before relying on exact
macros):
- `DEFINE_LATENT_AUTOMATION_COMMAND` / `_ONE_PARAMETER` / `_TWO_PARAMETER` variants; implement
  `Update()` returning `true` when finished, `false` to run next frame.
- Queue with `ADD_LATENT_AUTOMATION_COMMAND(YourCommand(...))`.
- Re-verify: https://dev.epicgames.com/documentation/unreal-engine/automation-technical-guide (accessed 2026-11-18).

## Running tests

- Editor: Automation tab → Start Tests.
- Command line (from this repo's agent definition; the `-testexit` flag is not
  checked against Epic's primary reference):
  `UnrealEditor-Cmd.exe "<path>.uproject" -ExecCmds="Automation RunTests <TestName>; Quit" -unattended -nopause -NullRHI -nosplash -ReportExportPath="<path>" -testexit="Automation Test Queue Empty"`.
  Confirm the `-testexit` value against Epic before relying on it.
