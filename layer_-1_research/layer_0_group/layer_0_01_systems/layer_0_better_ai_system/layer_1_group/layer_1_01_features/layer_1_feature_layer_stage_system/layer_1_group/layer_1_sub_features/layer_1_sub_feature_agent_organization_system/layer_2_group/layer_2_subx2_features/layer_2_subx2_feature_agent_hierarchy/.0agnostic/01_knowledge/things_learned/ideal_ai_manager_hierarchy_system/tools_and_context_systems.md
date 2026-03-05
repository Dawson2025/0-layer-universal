---
resource_id: "bdaa33fa-48bf-428c-9f80-c1d88715bf28"
resource_type: "knowledge"
resource_name: "tools_and_context_systems"
---
<!-- section_id: "15a3c2ce-be15-4ee9-8175-8c4daa15d317" -->
## Tools and Context Systems

This document expands on how specific tools and their context systems fit into the ideal AI manager hierarchy system.

It builds on the generic Tool Interface described in:

- `IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`
- `architecture.md`

The goal is to keep the **architecture tool-agnostic**, while capturing enough **tool-specific detail** to be practically useful.

---

<!-- section_id: "ff3a399f-39b6-48bd-b8bc-bde1d94d11d5" -->
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

<!-- section_id: "c5f3fb4d-71d5-447b-8f21-4db2b220e3c8" -->
## 2. Claude Code and `CLAUDE.md`

<!-- section_id: "401aee67-ee6d-4693-9958-37e126c03f8c" -->
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

<!-- section_id: "cd5661fb-7c59-4248-b030-9cc7d4bb64e3" -->
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

<!-- section_id: "ae652b3b-65b8-4397-a3b0-71896e554735" -->
### 2.3 Ideal Usage in This System

Claude Code is best used for:

- L0–L2 managers that benefit from cascading `CLAUDE.md`.
- Criticism/fixing/debugging stages where:
  - Multi-file context is needed.
  - Deep reasoning is required.
- Limited but precise coding tasks where correctness is more important than speed/cost.

---

<!-- section_id: "fcea0192-a647-4869-ad4f-5efd1149a131" -->
## 3. Codex CLI and `AGENTS.md`

<!-- section_id: "ad5a17de-32d3-4539-8bb0-3e2309ab692e" -->
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

<!-- section_id: "a025e3ba-2780-4c69-ab33-ae7eb8918bf1" -->
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

<!-- section_id: "8fa2a4d1-21f2-4151-82f7-2bf5f99201eb" -->
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

<!-- section_id: "d115afeb-14d8-4719-bb5a-c9ba4007a765" -->
## 4. Gemini CLI and `GEMINI` System Prompts

<!-- section_id: "30f15c3c-c16e-4fe4-96be-a42319ca3a7a" -->
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

<!-- section_id: "e81536d1-5977-4251-b6e6-dd531b8ba5d9" -->
### 4.2 Long-Context Reasoning

Gemini is well-suited to:

- Long dialog sessions (tens of turns).
- Heavy research (docs, web, APIs).
- Complex clarification in `request` and `instructions` stages.

Because:

- System instructions stay pinned in `systemInstruction`.
- Large context windows allow long clarifying conversations.

<!-- section_id: "4a24ac91-5a12-436a-91ef-1041190efe16" -->
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

<!-- section_id: "3053615f-bf56-4b1a-a3f8-193381bf675e" -->
## 5. Cursor IDE and Rules

<!-- section_id: "3cc69625-6615-448d-a1b6-08880c22c9c9" -->
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

<!-- section_id: "aca771b2-047c-4dfa-b5a6-b7312fda26cf" -->
### 5.2 Terminal and Orchestration Constraints

Cursor excels at:

- Planning complex refactors (Planning Mode).
- Running multiple agents in parallel worktrees.
- Interactively applying and reviewing diffs.

But has known constraints:

- Terminal hangs (especially with fancy prompts, long-running commands).
- No programmatic API to launch agents from external CLIs.
- No standardized handoff JSON interface.

<!-- section_id: "bacc4f7f-66b8-4c41-8a02-a024b17c377b" -->
### 5.3 Ideal Usage in This System

Cursor is best treated as:

- A **human-in-the-loop power tool**:
  - Interactive debugging.
  - Manual review and refactoring.
  - Exploratory coding with persistent project rules.

It is **not** a first-class participant in the automated CLI-based hierarchy, but complements it when humans are present in the loop.

---

<!-- section_id: "f6ad7ede-2509-4353-96aa-5d93fee589cb" -->
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

<!-- section_id: "3eacc79b-c566-4c59-ab1b-a9df19814922" -->
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


