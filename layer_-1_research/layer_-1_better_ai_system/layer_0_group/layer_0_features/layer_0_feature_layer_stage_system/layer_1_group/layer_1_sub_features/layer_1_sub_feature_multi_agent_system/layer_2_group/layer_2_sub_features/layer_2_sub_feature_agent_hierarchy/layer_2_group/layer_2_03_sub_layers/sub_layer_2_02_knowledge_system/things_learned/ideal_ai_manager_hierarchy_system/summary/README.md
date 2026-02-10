## Ideal AI Manager Hierarchy System – Overview

This file is the **primary overview** of the ideal AI manager hierarchy system.  
It is designed to be short enough to fit comfortably into an AI agent’s context, while pointing to more detailed documents.

The system is derived from the research in:

- `../../../chat_history/ai-manager-hierarchy-system-research.md`

and the detailed analysis under:

- `../` (the `ideal_ai_manager_hierarchy_system` folder)

It is:

- **Pattern-first**: it describes generic layers, stages, tools, and protocols.
- **Summary-neutral**: it does not assume a single narrow topic; it reflects the themes present in the research.
- **Open-world and extensible**: any future tools, OSes, layers, and workflows that fit these patterns can be plugged in.

---

### 1. High-Level Idea

You have an **Agent OS** for software development that:

- Organizes work across **layers of abstraction**  
  (Layer 0: Universal → Layer 1: Project → Layer 2: Feature → Layer 3: Component → optional Layer 4+ Sub-components).

- Moves work through **chronological stages**  
  `request → instructions → planning → design → implementation → testing → criticism → fixing → archiving`.

- Uses **handoff documents** (JSON/Markdown) to pass structured state between agents:
  - Vertical handoffs: between layers (L0↔L1↔L2↔L3…).
  - Horizontal handoffs: between stages within a layer.

- Coordinates a mix of **manager agents** and **worker agents**:
  - Managers read high-level handoffs, plan, and spawn workers (possibly in parallel).
  - Workers perform bounded tasks (1–3 actions), then write an `outgoing` handoff and exit.

- Keeps instructions **sticky** by using system-level or system-like prompts:
  - Avoids re-sending long instructions in chat history where they get buried.

---

### 2. Core Components (Very Short)

- **Layers**  
  - L0–L3 (and optionally L4+), each with its own manager, sub-layers, and stage directories.
  - Lower layers inherit all constraints from higher layers (CSS-like cascade).

- **Stages**  
  - Each layer has a `*.99_stages/` directory with subfolders for each stage (request, planning, design, etc.).
  - Each stage has:
    - `ai_agent_system/` – where the stage’s agents operate.
    - `hand_off_documents/` – where `incoming` and `outgoing` handoffs are stored.

- **Managers & Workers**  
  - Managers: long-lived, higher-intelligence agents (often Claude or Gemini) that orchestrate.
  - Workers: short-lived, focused agents (often Codex or similar) that execute atomic tasks.

- **Handoffs**  
  - Versioned JSON/Markdown with fields like:
    - `schemaVersion`, `kind`, `layer`, `stage`, `from`, `to`, `task`, `constraints`, `artifacts`, `subtasks`, `results`, `status`.

- **Tools (current examples)**  
  - **Claude Code** – strong for layered managers, criticism, fixing, deep debugging.
  - **Codex CLI** – fast, cheap leaf worker for small implementation/testing tasks.
  - **Gemini CLI** – long-context reasoning for request/instructions/planning and research.
  - **Cursor IDE** – interactive debugging and refactor companion (human-in-the-loop).

- **OS / Tool Variants**  
  - `os/<os-id>/...` subfolders hold OS-specific context for each tool:
    - `CLAUDE.md`, `AGENTS.md`, `GEMINI.*`, `.cursor/rules/*.mdc`, etc.

---

### 3. Where to Find More Detail

Use this file when you need a quick mental model or to prime an AI agent.  
For deeper details, use:

- **Long-form specification**  
  - `IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md` (this same `summary/` folder)  
    – describes the full architecture, handoff schema, orchestration patterns, and extensibility.

- **Architecture details**  
  - `../architecture.md` – deep dive on layers, stages, managers, workers, handoffs, supervisors, and parallelism.

- **Tool and context systems**  
  - `../tools_and_context_systems.md` – specifics of Claude, Codex, Gemini, Cursor, and how they use `CLAUDE.md`, `AGENTS.md`, `GEMINI.*`, `.cursor/rules/*.mdc`, etc.

- **OS variants and quartets**  
  - `../os_and_quartets.md` – `wonder.os/<os-id>/...` layouts, OS detection logic, and extensible tool-variant schemes.

- **Token and policy strategy**  
  - `../token_and_policy_strategy.md` – cost-aware routing and how to decide which tool to use for which stage/layer/task.

This `summary/README.md` is the recommended overview and link hub for agents operating in the ideal AI manager hierarchy system.


