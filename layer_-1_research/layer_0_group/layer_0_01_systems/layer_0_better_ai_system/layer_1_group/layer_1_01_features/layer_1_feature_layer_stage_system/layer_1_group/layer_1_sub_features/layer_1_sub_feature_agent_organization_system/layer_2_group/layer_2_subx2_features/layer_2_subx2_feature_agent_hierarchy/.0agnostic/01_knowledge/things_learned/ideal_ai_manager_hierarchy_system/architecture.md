---
resource_id: "ee4b6c15-b10a-4797-b784-8e76cd196283"
resource_type: "knowledge"
resource_name: "architecture"
---
## Architecture, Tools, and OS Variants (Detailed)

This document describes the architecture, tool roles, and OS-aware patterns for your ideal AI manager hierarchy system, as distilled from `../../../chat_history/ai-manager-hierarchy-system-research.md`.

It is intended as a detailed companion to:

- `summary/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md` (long-form spec), and
- `summary/README.md` (short overview).

---

## 1. Layered & Staged Architecture (Recap)

### 1.1 Layers (Abstraction / Specificity)

The system is structured into a stack of layers:

1. **Layer 0 – Universal**  
   - Global rules: languages, frameworks, security posture, coding style, testing expectations.
   - Examples:
     - Use TypeScript by default.
     - Prefer small, auditable dependencies.
     - Enforce security best practices (no secrets, input validation).

2. **Layer 1 – Project**  
   - Per-project context and constraints.
   - Examples:
     - “E‑commerce platform with Stripe integration, GDPR compliance.”
     - “University math coursework automation (ALEKS, homework PDFs, grading).”

3. **Layer 2 – Feature**  
   - Individual feature domains, e.g.:
     - `auth-system`, `shopping-cart`, `reporting-dashboard`, `dynamic-memory-system`.

4. **Layer 3 – Component**  
   - Concrete pieces inside a feature:
     - `LoginForm`, `PasswordResetFlow`, `CartItemList`, `GradeCalculator`.

5. **Layer 4+ – Sub-components**  
   - Optional deeper splits for parallelism or complexity management:
     - `login/form-ui`, `login/validation`, `login/api-handler`, `login/types`, etc.

#### 1.1.1 Layer Responsibilities

Each layer has:

- A **Manager**:
  - Owns the layer’s `*.00_ai_manager_system/` and `*.01_manager_handoff_documents/`.
  - Reads high-level goals (from above or from a user).
  - Decomposes work into:
    - Layer-local stages (request, planning, etc.).
    - Subtasks for lower layers.
  - Aggregates upward into summarised handoffs.

- A **Context Stack**:
  - `LayerContext(L) = Context(L0) + Context(L1) + … + Context(L)` (plus OS/tool-specific overrides).
  - Maintained via `CLAUDE.md`, `AGENTS.md`, `GEMINI.*`, `.cursor/rules/*.mdc`, etc.

### 1.2 Stages (Chronological Pipeline)

Within each layer, you operate through a canonical pipeline:

1. **request/** – Clarify goals and scope.  
2. **instructions/** – Turn goals into explicit instructions and constraints.  
3. **planning/** – Produce a plan: tasks, ordering, dependencies.  
4. **design/** – Specify architectures, interfaces, data flows, and UX.  
5. **implementation/** – Modify code, write new modules, scripts, or configs.  
6. **testing/** – Write and run tests; collect results.  
7. **criticism/** – Review outputs against constraints and quality criteria.  
8. **fixing/** – Apply fixes, refactor, and re-run tests.  
9. **archiving/** – Capture final state, notes, and pointers to artifacts.

This list is **not closed**; you may add, split, or rename stages as long as they still use the handoff protocol described below.

### 1.3 Managers & Workers

#### 1.3.1 Manager Agents

Managers are long-lived, reasoning-heavy agents, typically:

- **Claude Code** for high-level orchestration and deep code reasoning.
- **Gemini CLI** for long, research-heavy planning and request stages.

They:

- Maintain the full layer+stage context in their system prompt.
- Interpret and update multi-stage, multi-file handoffs.
- Spawn worker agents (via CLI / shell / other frameworks).

#### 1.3.2 Worker Agents

Workers are short-lived, execution-focused agents, typically:

- **Codex CLI** for small code changes or test runs.
- Sometimes **Gemini CLI** for research or analysis steps.
- Potentially other tools or local LLMs that implement the same interface.

They:

- Take a single, well-scoped handoff.
- Perform a bounded number of steps (usually 1–3 turns).
- Write an `outgoing` handoff with results or a failure state.

Workers never assume global authority over the project; they just satisfy the contract for their current handoff.

---

## 2. Handoff Protocol (Detailed)

### 2.1 Structure

Every handoff document (JSON or Markdown with an embedded JSON block) should include:

- **Metadata**
  - `schemaVersion`: e.g., `"1.0.0"`.
  - `id`: unique identifier for traceability.
  - `createdAt`, `updatedAt`: timestamps (ISO 8601).
  - `from`: e.g., `"layer_2/auth-system/planning"` or `"layer_2/login-component/implementation"`.
  - `to`: target agent or stage, e.g., `"layer_2/login-component/implementation"`, `"layer_2/auth-system/testing"`.

- **Context**
  - `layer`: numeric or string ID (`0`, `1`, `feature:auth-system`, etc.).
  - `stage`: name of current or next stage.
  - `parentIds`: array of parent handoff IDs (for DAG lineage).
  - `constraints`: array of constraint strings or objects (security, performance, style, etc.).
  - `environment`: OS, repo path, branch, feature flag info.

- **Work Description**
  - `task`: human-readable summary of what must be done.
  - `subtasks`: list of smaller tasks or TODOs.
  - `acceptanceCriteria`: bullets describing success (tests pass, metrics thresholds, etc.).
  - `artifacts`: references to files, URLs, database entities, or other resources.

- **Results / Status**
  - `status`: `"pending" | "in_progress" | "completed" | "failed" | "blocked"`.
  - `results`: summary of what was done / found.
  - `errors`: descriptions of failures, exceptions, or blockers.
  - `nextActions`: suggested next steps (for the next stage or manager).

Agents are free to add more fields (e.g., `securityFindings`, `perfMetrics`, `notes`) as long as they keep the top-level schema backwards-compatible.

### 2.2 File Locations

Each stage directory has:

- `hand_off_documents/`
  - `incoming.json` – the handoff to be processed by the stage.
  - `outgoing.json` – the handoff produced after work.
  - Optionally:
    - `incoming/` and `outgoing/` subdirs for multiple parallel tasks.
    - E.g., `incoming/login.json`, `incoming/reset-password.json`.

Vertical handoffs between layers use similar patterns, just under each layer’s `*.01_manager_handoff_documents/` directory:

- E.g., `layer_2_project/1.01_manager_handoff_documents/1.00_to_universal/incoming.json`
- E.g., `layer_2_features/2.01_manager_handoff_documents/2.01_to_components/outgoing.json`

This keeps all cross-layer state explicit and inspectable in the filesystem.

### 2.3 Flow Types

#### 2.3.1 Vertical Flows

From a manager at Layer `L` to the next layer:

1. Manager at `L` writes a handoff into `L+1`’s `.../handoff_documents/incoming.json`.
2. Manager (or supervisor) spawns the manager at `L+1` to process it.
3. Manager at `L+1` runs its own stages and sub-managers/workers.
4. When done, `L+1` writes `outgoing.json` to its manager handoff directory.
5. `L` reads `L+1`’s `outgoing.json` and updates its own `results/nextActions`.

#### 2.3.2 Horizontal Flows

Within a single layer `L`, a stage network might look like:

1. `request/` writes `outgoing.json` with clarified requirements.
2. `instructions/` reads `incoming.json` ← `request/outgoing.json`, enriches constraints, emits `outgoing.json`.
3. `planning/` reads that and emits `plan.json` with `subtasks`.
4. `implementation/` may spawn multiple workers using copies of that plan or per-subtask handoffs.
5. `testing/` reads from implementation outputs, executes tests, populates `results`.
6. `criticism/` reads all results and flags issues.
7. `fixing/` uses those issues to drive further worker calls.
8. `archiving/` writes final long-term notes and statuses.

---

## 3. Tools & Context Systems (Pointer)

Tool selection and prompt mechanics are described in detail in:

- `../tools_and_context_systems.md`

In brief:

- **Claude Code**
  - Auto-merges `CLAUDE.md` files and uses them as true `system` prompts.
  - Best for managers, deep analysis, and complex fixes.

- **Codex CLI**
  - Uses `AGENTS.md` as first user message; good for short-lived, atomic workers.

- **Gemini CLI**
  - Uses `systemInstruction` with manual composition; ideal for long reasoning and research-heavy stages.

- **Cursor IDE**
  - Uses `.cursor/rules/*.mdc` as re-injected context; best for interactive work.

Any future tool with a way to:

- Load a persistent “system-like” context, and
- Read/write handoff files,

can be slotted into this architecture as either a manager or worker.

---

## 4. OS-Aware Patterns (Pointer)

OS and environment differences are captured in:

- `../os_and_quartets.md`

Key points:

- Each stage/layer can include `os/<os-id>/...` directories with OS-specific context files:
  - `CLAUDE.md`, `AGENTS.md`, `GEMINI.*`, `.cursor/rules/*.mdc`.
- Supervisors detect which `<os-id>` to use based on `OSTYPE`, `uname`, `WSL_DISTRO_NAME`, etc.
- This allows the same logical hierarchy to run:
  - On WSL, native Linux, macOS, Windows, containers, or other environments.

---

## 5. Supervisors and Parallel Execution

Supervisors are the “process schedulers” of your Agent OS:

- Observe handoff directories for new `incoming` work.
- Apply a **tool policy** (see `../token_and_policy_strategy.md`) to decide which agents and tools to run.
- Spawn background processes for each worker, e.g.:
  - `codex ... &`
  - `gemini ... &`
  - `python3 scripts/terminal_wrapper.py --script ... &`
- Synchronize on outputs:
  - Poll for `hand_off_documents/outgoing.json` to appear.
  - Aggregate results when all required workers finish.

Parallelization can scale horizontally as far as resources allow, because:

- Work is decomposed into **independent handoffs**.
- Each worker sees only the slice of the world that matters for its task.
- Managers can be written to treat each `outgoing` handoff as a unit in a DAG.

Frameworks like LangGraph or AutoGen can be used to implement this supervisory logic in a more declarative or graphical way, but the underlying file-and-process protocol remains the same.

---

## 6. Extending the Architecture

The system is designed to be future-proof:

- **New layers**: add more `layer_N_*` trees and ensure managers know how to call them.
- **New stages**: add new stage directories and update supervisor/manager logic to include them in the pipeline.
- **New tools**: define a context file pattern and CLI entrypoint, then map it in `token_and_policy_strategy.md`.
- **New OSes**: add `os/<os-id>/...` directories and detection rules.

As long as each new piece:

- Participates in the handoff protocol, and
- Implements the generic Tool Interface,

it can be introduced without altering existing semantics.

## Architecture Details: Ideal AI Manager Hierarchy System

This document expands on the architectural aspects of the system sketched in:

- `IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`

It focuses on **layers**, **stages**, **agents**, **handoffs**, **supervisors**, and **parallelism**.

---

## 1. Layers (Abstraction / Specificity)

Layers are a stack of abstraction levels, similar to CSS:

- **L0 – Universal**
  - Global constraints for all work and tools.
  - Examples: always use TypeScript, security-first, no secrets, dependency size limits.

- **L1 – Project**
  - Rules and context specific to a single project or codebase.
  - Examples: ecommerce vs math workflow vs personal knowledge system.

- **L2 – Feature**
  - Logic and invariants for a feature within a project.
  - Examples: auth system, homework automation, progress tracking.

- **L3 – Component**
  - Concrete units of implementation (files, modules, UI components, tasks).
  - Examples: `LoginForm`, `GradeCalculator`, `GraphRenderer`.

- **L4+ – Sub-Component and Below**
  - Optional deeper splits where needed for parallelism or clean separation.
  - Examples: `login-form-ui`, `login-validation`, `login-api`, etc.

### 1.1 Layer Inheritance

Each layer `L` inherits:

- All higher-layer constraints `L0…L-1`.
- Its own additional constraints and context.
- Possibly OS- and tool-specific refinements.

Effective behavior at any point = **merge(L0..L, OS variant, tool context)**.

---

## 2. Stages (Chronological Pipeline)

Stages provide a **time-ordered** structure within each layer:

1. **Request**: understand what is being asked.
2. **Instructions**: transform vague request into specific instructions.
3. **Planning**: break the work into subtasks.
4. **Design**: choose architectures, flows, and interfaces.
5. **Implementation**: write or edit code/configs/docs.
6. **Testing**: verify via tests and tools.
7. **Criticism**: review results against constraints and quality bars.
8. **Fixing**: resolve problems, refactor, or rework.
9. **Archiving**: summarize, store artifacts, and close the loop.

Stages:

- Are **open-ended**; new ones can be introduced as long as:
  - They consume a handoff.
  - They emit a compatible handoff.
  - They don’t silently destroy previous stages’ data.

- May be **skipped or repeated** depending on `status`/`kind` in the handoff.

---

## 3. Agents: Managers and Workers

### 3.1 Manager Agents

Managers exist at any layer where coordination is required:

- Accept high-level handoffs from upper layers (or external users).
- Decide:
  - Which stages to run.
  - Which sub-layers or components to engage.
  - When to run tasks in parallel.
- Aggregate results from workers and synthesize new handoffs.

Managers are defined by behavior, not by a specific tool; any agent with this interface can be a manager.

### 3.2 Worker Agents

Workers are leaf or near-leaf agents that:

- Read a single incoming handoff (or small bundle).
- Perform a **bounded** unit of work (usually 1–3 actions).
- Write an outgoing handoff (and optionally code or other artifacts).
- Exit cleanly.

Workers should:

- Avoid long conversational drift.
- Be cheap and fast where possible (e.g., Codex, future local models).

---

## 4. Handoffs (Data Flow)

Handoffs are structured representations of work-in-progress.

### 4.1 Vertical Handoffs (Layer ↔ Layer)

Vertical handoffs pass tasks and results between layers:

- Downward:
  - L0 → L1: “Project-level goals with universal constraints.”
  - L1 → L2: “Feature-level tasks with project + universal constraints.”
  - L2 → L3/L4: “Component/sub-component tasks with all above constraints.”

- Upward:
  - L3/L4 → L2 → L1 → L0: results, summaries, metrics, and status.

Vertical flow ensures:

- Universal rules are visible everywhere.
- Local decisions and progress can be understood higher up.

### 4.2 Horizontal Handoffs (Stage ↔ Stage)

Within a layer:

- Each stage reads from `hand_off_documents/incoming.*`.
- Each stage writes to `hand_off_documents/outgoing.*`.
- Outgoing from one stage becomes incoming to the next.

This forms the internal pipeline:

> request → instructions → planning → design → implementation → testing → criticism → fixing → archiving

Stages can be:

- Run sequentially.
- Skipped if the handoff indicates they are unnecessary.
- Re-run when criticism/fixing demands a new plan or design.

---

## 5. Supervisors and Orchestration

Supervisors are meta-components that orchestrate agents:

- May be implemented:
  - As scripts (Python/TS/shell).
  - As higher-level LLM agents.
  - Via frameworks (LangGraph, AutoGen, CrewAI, etc.).

### 5.1 Supervisor Responsibilities

- Discover tasks by:
  - Watching handoff directories.
  - Reading “task queues” or status files.
- Map tasks to:
  - Layers and stages.
  - Tools/agents (via policy).
  - OS variants and quotas.
- Launch:
  - Manager and stage wrappers via CLI calls.
- Monitor:
  - Progress (handoff updates, exit codes, logs).
- Handle:
  - Errors, retries, backoff.
  - Escalation to humans or higher layers.

### 5.2 Abstract Command Model

Supervisors treat everything as:

> `run_agent(layer, stage, tool, osVariant, options)`

Where:

- `layer` and `stage` locate the correct directory.
- `tool` selects the CLI/agent/driver.
- `osVariant` selects `os/<os-id>/` context.
- `options` controls max turns, timeouts, logging, etc.

This keeps orchestration logic generic and tool-independent.

---

## 6. Parallelism and Scaling

Parallelism is obtained through **independent workers**:

- Manager decomposes a task into sub-tasks that do not conflict.
- Each sub-task is assigned to a worker (or sub-manager) at the appropriate layer and stage.
- Workers run concurrently and write their output handoffs.
- Manager waits for all required handoffs and aggregates them.

Examples:

- L2 Feature Manager:
  - Spawns:
    - L3 UI worker.
    - L3 validation worker.
    - L3 API worker.
    - L3 docs worker.
  - Aggregates all four outputs into a feature-level result.

Scaling up:

- Same pattern extends to dozens or hundreds of workers at L3/L4+.
- Supervisors can implement rate limiting, batching, and prioritization.

---

## 7. Extensibility

The architecture is deliberately **open-ended**:

- New layers: follow naming patterns, add managers and stages.
- New stages: define how they transform handoffs and where they sit in the pipeline.
- New tools: map them to the Tool Interface and define their context files.
- New OS environments: add `os/<os-id>/...` variants.

As long as new elements respect:

- The Layer/Stage structure,
- The Handoff schema and IO rules,
- And the run_agent abstraction,

they fit naturally into this architecture without redesign.


