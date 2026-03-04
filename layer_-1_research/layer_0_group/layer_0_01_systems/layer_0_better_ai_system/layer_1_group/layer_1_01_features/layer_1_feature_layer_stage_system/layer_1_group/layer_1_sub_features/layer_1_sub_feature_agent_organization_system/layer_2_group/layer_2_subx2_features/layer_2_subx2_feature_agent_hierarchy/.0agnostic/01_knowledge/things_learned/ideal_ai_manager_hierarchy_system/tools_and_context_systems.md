## Tools and Context Systems

This document expands on how specific tools and their context systems fit into the ideal AI manager hierarchy system.

It builds on the generic Tool Interface described in:

- `IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`
- `architecture.md`

The goal is to keep the **architecture tool-agnostic**, while capturing enough **tool-specific detail** to be practically useful.

---

## 1. Generic Tool Interface (Recap)

Any tool (CLI, IDE, framework, or agent) is modeled as:

- **Inputs**
  - System-like context (rules, role, constraints).
  - One or more handoffs (JSON/Markdown).
  - Environment (OS, paths, credentials, network).

- **Behavior**
  - Reads context + handoffs.
  - Performs reasoning and/or actions (edit files, run commands, call tools).
  - Produces code/artefacts and at least one output handoff.

- **Outputs**
  - Modified files / repo state.
  - Structured handoff(s) describing results/next steps.

Context can be injected via:

- API `system` fields (Claude, Gemini).
- Context prefixes (Cursor Rules).
- Initial user messages (Codex `AGENTS.md`).
- Any future mechanism that reliably pins instructions.

---

## 2. Claude Code and `CLAUDE.md`

### 2.1 System Prompt Sources

Claude Code can draw its system prompt from multiple sources (summarized conceptually):

- Built-in “claude_code” preset (tools + safety + basic coding guidance).
- Global `~/.claude/CLAUDE.md`.
- Project-level `./CLAUDE.md`.
- Subdirectory `CLAUDE.md` files (closer to target files).
- Output styles and custom agents (e.g., `.claude/output-styles/*.md`).
- CLI flags such as `--system-prompt` and `--append-system-prompt`.

These are **merged** into a single system string that is sent to the model’s `system` field.

Key points:

- System prompt is **re-injected every API call**.
- Project and directory-specific `CLAUDE.md` files give you **filesystem-as-config**.
- Output styles and custom agents let you define reusable personas (e.g., “Security Reviewer”).

### 2.2 Sub-Agents and Hierarchies

Claude Code offers:

- In-IDE/CLI **sub-agent** support: specialized agents (planners, reviewers, testers).
- A **flat sub-agent tree** by default (main agent → sub-agents, but sub-agents don’t spawn sub-agents directly).

However, you can construct **deeper hierarchies** by:

- Using CLI chaining:
  - Each `claude-code` invocation acts as:
    - A manager (reading handoffs, spawning others).
    - Or a worker (processing a single handoff).
- Ensuring each invocation:
  - Loads the correct `CLAUDE.md` stack.
  - Reads the right `incoming` handoff.
  - Writes the right `outgoing` handoff.

This effectively creates:

- L0 main managers spawning L1 managers.
- L1 managers spawning L2/L3 managers/workers.
- Deeper recursive chains as needed.

### 2.3 Ideal Usage in This System

Claude Code is best used for:

- L0–L2 managers that benefit from cascading `CLAUDE.md`.
- Criticism/fixing/debugging stages where:
  - Multi-file context is needed.
  - Deep reasoning is required.
- Limited but precise coding tasks where correctness is more important than speed/cost.

---

## 3. Codex CLI and `AGENTS.md`

### 3.1 Context via AGENTS.md

Codex CLI uses `AGENTS.md` files to provide filesystem-based context:

- Global: `~/.codex/AGENTS.md`.
- Repo root: `./AGENTS.md` or override variants.
- Subdirectories: deeper `AGENTS.md` files refine context for subtrees.

Codex merges these into a **single text block**, which is injected as:

- The first user message (`messages[0]`) at session start.

Important:

- The actual `system` field of the API call is a **hard-coded internal prompt**.
- `AGENTS.md` lives inside the **chat history**, not the system field.

### 3.2 Dilution and Session Length

Because `AGENTS.md` is a user message:

- As chat history grows (code diffs, tool outputs, back-and-forth), the AGENTS block:
  - Moves deeper into the context window.
  - Becomes less salient to the model.

Practical implications:

- AGENTS-based instructions are strong in the first few turns.
- They get weaker and eventually effectively disappear in long sessions.

Therefore:

- Codex CLI is ideally used for **short, atomic sessions**:
  - 1–3 main turns.
  - A single compact task per session.

### 3.3 Ideal Usage in This System

Codex CLI fits perfectly as:

- **Leaf workers** at L3/L4:
  - Implementation tasks for single components or files.
  - Small refactors.
  - Writing and running tests.

Managers and supervisors should:

- Open **fresh Codex sessions** for each atomic task.
- Avoid dragging Codex into multi-stage, long-running roles.

---

## 4. Gemini CLI and `GEMINI` System Prompts

### 4.1 SystemInstruction and Merging

Gemini CLI allows:

- Setting a **true system prompt** via:
  - CLI flags (e.g., `--system "..."`).
  - Environment variables that reference a system file.
- This system text populates the model’s `systemInstruction` field.

Unlike Claude:

- Gemini does **not automatically** cascade prompts from multiple files.
- Merging across layers must be done **manually**, for example:
  - Concatenate relevant layer/feature/component files into a single system file.
  - Point Gemini CLI at that file.

### 4.2 Long-Context Reasoning

Gemini is well-suited to:

- Long dialog sessions (tens of turns).
- Heavy research (docs, web, APIs).
- Complex clarification in `request` and `instructions` stages.

Because:

- System instructions stay pinned in `systemInstruction`.
- Large context windows allow long clarifying conversations.

### 4.3 Ideal Usage in This System

Use Gemini CLI primarily for:

- **Request gathering** and **instructions** at L1/L2:
  - When many Q&A turns are needed.
  - When lots of external material (docs, web) must be pulled in.
- **Planning and design** when:
  - The cost of Claude’s premium reasoning is not justified.
  - The main challenge is breadth, not deep code correctness.

Execution-heavy or multi-file code changes are better left to Claude or Codex.

---

## 5. Cursor IDE and Rules

### 5.1 Cursor Rules as Context

Cursor uses `.cursor/rules/*.mdc` files:

- Each rule file can specify:
  - Title, description.
  - Globs for matching files.
  - Priority and `alwaysApply` behavior.
- Cursor merges **all applicable rules** for a given request and injects them at:
  - The top of the context (before file snippets, history, and the current prompt).

This gives:

- Persistent, layered project rules for interactive use.
- CSS-like cascading via `globs` plus priorities.

### 5.2 Terminal and Orchestration Constraints

Cursor excels at:

- Planning complex refactors (Planning Mode).
- Running multiple agents in parallel worktrees.
- Interactively applying and reviewing diffs.

But has known constraints:

- Terminal hangs (especially with fancy prompts, long-running commands).
- No programmatic API to launch agents from external CLIs.
- No standardized handoff JSON interface.

### 5.3 Ideal Usage in This System

Cursor is best treated as:

- A **human-in-the-loop power tool**:
  - Interactive debugging.
  - Manual review and refactoring.
  - Exploratory coding with persistent project rules.

It is **not** a first-class participant in the automated CLI-based hierarchy, but complements it when humans are present in the loop.

---

## 6. Other Frameworks (LangGraph, AutoGen, CrewAI, MetaGPT, etc.)

The research references several multi-agent frameworks:

- **LangGraph**: graphs and DAG-based orchestration.
- **AutoGen**: conversational multi-agent setups.
- **CrewAI**: team-of-agents with roles.
- **MetaGPT**: prescriptive “software team in a box.”

In this system:

- They can be used to implement:
  - Supervisors.
  - Managers at particular layers.
  - Or even specialized workers.

The key requirement:

- They must respect the **Tool Interface** and **Handoff Protocol**:
  - Read context and handoffs.
  - Produce new handoffs with well-defined schemas.

---

## 7. Adding New Tools

To add a new tool (CLI, IDE, service, or framework):

1. Define how it accepts system-like instructions:
   - API system field?
   - Context prefix?
   - Initial pairing message?
2. Define its context files:
   - E.g., `GROK.md`, `LLAMA.md`, or new rule files.
3. Specify a cascading rule:
   - How does it combine layer/feature/component/OS context?
4. Map it into:
   - The tool policy (which stages/layers it should handle).
   - `run_agent` invocations (how wrappers call it).

If these four steps are clear, the new tool seamlessly fits into the existing architecture.


