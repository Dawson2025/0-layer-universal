## OS Variants and Quartets

This document expands on how **operating system differences** and **tool-specific context files** are handled in the ideal AI manager hierarchy system.

It builds on the OS/variant ideas in:

- `IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`
- `architecture.md`
- `tools_and_context_systems.md`

---

## 1. OS as an Independent Dimension

The OS is treated as a **separate dimension** from:

- Layer (L0, L1, L2, …),
- Stage (request, planning, implementation, etc.),
- Tool (Claude, Codex, Gemini, Cursor, or others).

Instead of baking OS differences into every path, we use:

- `os/<os-id>/...` subfolders.

Where `<os-id>` is arbitrary, for example:

- `wsl`
- `ubuntu`
- `windows`
- `macos`
- `termux`
- `freebsd`
- `alpine`
- `custom-*` (for project-specific environments)

---

## 2. OS-Specific Context Layout

Within any layer/stage directory, you may have:

```text
os/
  wsl/
    CLAUDE.md
    AGENTS.md
    GEMINI.md
    .cursor/
      rules/
        wsl.mdc
  ubuntu/
    CLAUDE.md
    AGENTS.md
    GEMINI.md
  windows/
    CLAUDE.md
    AGENTS.md
    GEMINI.md
  macos/
    CLAUDE.md
    AGENTS.md
    GEMINI.md
  custom-my-cluster/
    CLAUDE.md
    AGENTS.md
    GEMINI.md
```

The intent:

- Each OS variant folder provides:
  - OS-specific versions of the tool context files.
  - Any extra rules or constraints for that environment.

Examples:

- `os/wsl/CLAUDE.md`:
  - Could include guidance about `wsl.exe`, Windows paths, mount points, etc.
- `os/windows/AGENTS.md`:
  - Might specify PowerShell commands or `npm.cmd` differences.
- `os/macos/GEMINI.md`:
  - Might mention Homebrew, default shells, or file system quirks.

---

## 3. Auto-Detection and Selection

Supervisors or wrapper scripts:

- Detect the current OS and environment using:
  - `OSTYPE` (POSIX),
  - `uname` output,
  - `WSL_DISTRO_NAME` for WSL,
  - Environment-specific variables (e.g., `TERMUX_VERSION`).

They then:

1. Compute an `os-id` string (e.g., `wsl`, `ubuntu`, `windows`, `macos`).
2. Look for `os/<os-id>/` under the relevant layer/stage directory.
3. If found:
   - Use the context files in that directory when launching agents.
4. If not found:
   - Fall back to a default OS variant (e.g., `os/ubuntu/` or global defaults),
   - Or fail fast and request manual configuration.

This logic is under your control; the spec just defines the pattern.

---

## 4. Quartets (and Beyond)

In the research and top-level spec, a **quartet** per OS appears as:

- `CLAUDE.md` – Claude Code context.
- `AGENTS.md` – Codex CLI context.
- `GEMINI.*` – Gemini CLI context (e.g., `GEMINI.md`, `GEMINI.yaml`).
- `.cursor/rules/*.mdc` – Cursor IDE rules.

The quartet can be:

- Extended to **N-tuples** by adding:
  - New context types for new tools (e.g., `GROK.md`, `LLAMA.md`).
  - New rule/config formats as needed.

The rule:

- Any file in `os/<os-id>/` that matches a tool’s context pattern participates in that tool’s cascade.

---

## 5. Using OS Variants in Practice

### 5.1 Example: L3 Implementation Stage

Directory snippet:

```text
layer_3_components/.../stage_3.04_development/ai_agent_system/
  CLAUDE.md             # generic
  AGENTS.md             # generic
  GEMINI.md             # generic
  os/
    wsl/
      CLAUDE.md
      AGENTS.md
      GEMINI.md
    ubuntu/
      CLAUDE.md
      AGENTS.md
```

When launching:

- On WSL:
  - Use `os/wsl/` variants if present; fall back to generic where missing.
- On native Ubuntu:
  - Use `os/ubuntu/` variants, fall back to generic elsewhere.

### 5.2 Example: Cross-Platform Project

You may use:

- A generic `CLAUDE.md` for universal logic.
- Per-OS `AGENTS.md` to adjust Codex commands:
  - On Windows: use `npm.cmd`, `dir`, PowerShell.
  - On Linux/macOS: use `npm`, `ls`, bash/zsh.

---

## 6. Extending to New Tools

When adding a new tool:

1. Define its context file name/pattern.
2. Decide whether it needs OS-specific variants (likely yes).
3. Add those context files under each `os/<os-id>/` where relevant.
4. Update supervisor/wrapper logic so:
   - It knows how to cascade and load this context.
   - It selects the right OS variant folder for that tool.

New tools do not require rewriting the architecture; they just plug into:

- The `os/<os-id>/` structure, and
- The overall context cascade pattern.

---

## 7. Benefits of This Pattern

- **Separation of concerns**:
  - Layer and stage focus on abstraction and chronology.
  - OS variants focus on environmental details.
  - Tools focus on behaviors and capabilities.

- **Scalability**:
  - Adding a new OS or environment only touches:
    - `os/<os-id>/` folders.
    - Detection logic.

- **Clarity for agents**:
  - Agents always see:
    - Layer + stage constraints.
    - Tool-specific rules.
    - OS-specific quirks.

All without overloading a single monolithic prompt or config file.


