---
resource_id: "ccb764da-38b8-4b5d-8be9-d283837eb938"
resource_type: "knowledge"
resource_name: "token_and_policy_strategy"
---
## Token and Policy Strategy

This document expands on how **tools are assigned to tasks** in a cost-aware, quality-aware way.

It explains:

- How to think about **token usage** and **model strengths**.
- How to encode those decisions into a **policy mapping**.
- How to evolve that policy as tools and models change.

---

## 1. Policy Mapping (Conceptual)

We describe tool choice as a mapping:

> `(layer, stage, taskKind, environment) → toolProfile`

Where:

- `layer`: e.g., `0` (universal) through `3` (component) or beyond (`4+`).
- `stage`: request, planning, design, implementation, testing, criticism, fixing, archiving, or custom.
- `taskKind`: rough category of work (research, reasoning, code-gen, refactor, test-writing, debugging, etc.).
- `environment`: OS variant and context (e.g., `wsl`, `ubuntu`, `windows`, `macos`).
- `toolProfile`: choice of tool(s), configuration, max turns, timeouts, and budget.

This mapping is:

- **Not hard-coded**; it is a **policy** you can update.
- The primary place to express:
  - Cost constraints,
  - Quality requirements,
  - Risk tolerance,
  - And your preferences.

---

## 2. Current Policy (Example)

Based on the research and current tool capabilities, a reasonable initial policy is:

### 2.1 Claude Code

Use Claude Code for:

- **Managers at higher layers**:
  - L0–L2 where:
    - Layered `CLAUDE.md` cascading is crucial.
    - Many constraints across projects/features must be honored.
- **Criticism and fixing**:
  - Stages where:
    - Multi-file context and deep reasoning are needed.
    - You want stronger guarantees of correctness and coherence.
- **Difficult debugging and complex refactors**:
  - Cases where cheaper tools often fail or produce low-quality output.

Tradeoffs:

- Higher per-token cost.
- Better reasoning and adherence to complex, long-lived instructions.

### 2.2 Codex CLI

Use Codex CLI for:

- **Leaf-level implementation**:
  - L3/L4 tasks that:
    - Touch a small number of files.
    - Are bounded in scope (one component, test or refactor).
- **Testing and automation**:
  - Generating and running unit tests.
  - Small modifications where speed and cost matter more than deep context.

Constraints:

- Treat Codex sessions as **short-lived** (1–3 main turns).
- Do not rely on Codex for:
  - Long planning.
  - Deep reasoning across layers.

Tradeoffs:

- Low cost, fast.
- Vulnerable to instruction dilution in long chats.

### 2.3 Gemini CLI

Use Gemini CLI for:

- **Long reasoning and research**:
  - `request`, `instructions`, and sometimes `planning` stages at L1/L2.
  - Multi-turn clarification with large context (docs, APIs, external knowledge).
- **Research-heavy design**:
  - Exploring APIs, searching the web (via tools/MCP), and summarizing findings into handoffs.

Constraints:

- Requires manual prompt merging for layered system instructions.
- For code-heavy tasks, it may lag behind Claude/Codex until more advanced models (e.g., Gemini 3) are preferred.

Tradeoffs:

- Long context and good general reasoning.
- Moderate cost compared to Claude.

### 2.4 Cursor IDE

Use Cursor for:

- **Interactive debugging, refactor, and exploration**:
  - When you are “in the code” and want strong assistance inside your editor.
- **Manual review steps**:
  - When a human wants to inspect and guide high-impact changes.

Constraints:

- GUI-based, not ideal for headless automation.
- Terminal integration is imperfect and may require workarounds.

Tradeoffs:

- Great UX and productivity in manual flows.
- Not directly invocable from the CLI hierarchy as an automated worker.

---

## 3. Stage-Level Guidelines

Here is a coarse mapping between stages and preferred tools (examples, not exhaustive).

### 3.1 Request / Instructions

- **Primary**: Gemini CLI or Claude Code.
  - Gemini for long, exploratory clarification.
  - Claude when tight adherence to layered rules is essential.
- **Session Characteristics**:
  - Many turns, high context.
  - Output: detailed handoff with requirements and constraints.

### 3.2 Planning / Design

- **Primary**: Claude Code (planning sub-agents) or Gemini CLI.
  - Gemini for broad research and brainstorming.
  - Claude for converting that into executable, constraint-aware plans.
- **Session Characteristics**:
  - 5–20 turns.
  - Output: structured plan (subtasks, dependencies, success criteria).

### 3.3 Implementation / Testing

- **Primary**: Codex CLI (atomic workers), Claude Code where necessary.
  - Codex:
    - Implement specific functions.
    - Write/adjust tests.
  - Claude:
    - Cross-file refactors.
    - Tricky code that failed in cheaper tools.
- **Session Characteristics**:
  - Codex: 1–3 interactions per task.
  - Claude: fewer tasks, but more complex ones.

### 3.4 Criticism / Fixing

- **Primary**: Claude Code.
  - Multi-file review.
  - Checking against universal + project + feature + component constraints.
  - Coordinating multiple fixes and re-runs.

### 3.5 Archiving

- **Primary**: Any reasoning-capable tool (Claude, Gemini).
  - Summarizing sessions.
  - Updating indexes and long-lived context docs.

---

## 4. Turn Limits and Budget Hints

To keep costs reasonable:

- **Codex CLI**:
  - Hard limit: 1–3 main turns per worker session.
  - If more needed, consider:
    - New Codex session (fresh context).
    - Escalation to Claude or Gemini for more complex reasoning.

- **Gemini CLI**:
  - Flexible but still bounded:
    - Recommend 20–50 turns maximum for a single request/instructions session.
  - For extremely long interactions:
    - Break into phases, with each producing a clear handoff.

- **Claude Code**:
  - Use judiciously for:
    - Planning of complex tasks.
    - Criticism/fixing of high-impact changes.
  - Prefer lighter tools for:
    - Bulk generation that can be easily reviewed.

Supervisors can enforce:

- Per-task or per-stage budgets.
- Global rate limits or credit ceilings.

---

## 5. Evolving the Policy

The policy mapping is designed to change over time as:

- New models emerge (e.g., Gemini 3 as a better coder).
- Local models become strong enough for many tasks.
- Tool ecosystems evolve (new CLIs, IDEs, frameworks).

When updating the policy:

1. Evaluate candidate tools:
   - Quality on your tasks.
   - Cost and latency.
   - Reliability and ergonomics.
2. Update the mapping:
   - Change which tools are **primary** for each `(layer, stage, taskKind)`.
   - Adjust max turns and budgets.
3. Keep the architecture unchanged:
   - Layers, stages, handoffs, and OS/tool variant patterns stay the same.
   - Only the `toolProfile` selection logic changes.

This separation allows:

- Long-lived architecture and workflows.
- Short-lived, easily swappable tooling decisions.

---

## 6. Summary

- The architecture does not hard-code a particular model or tool.
- It assumes only that:
  - Tools can accept context and handoffs.
  - Tools can emit new handoffs.
- The **policy layer** decides:
  - Which tool is used where.
  - For how long.
  - With what budget.

By adjusting this policy over time, you can:

- Keep costs under control.
- Gradually improve quality with better models.
- Maintain a consistent workflow structure for both humans and agents.


