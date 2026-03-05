---
resource_id: "359c28a9-011d-4a63-aedb-2151dca5cadd"
resource_type: "knowledge"
resource_name: "IDEAL_AI_MANAGER_HIERARCHY_SYSTEM"
---
<!-- section_id: "374d7f67-b525-444a-9d65-9c39a1ee9711" -->
## IDEAL AI Manager Hierarchy System

This document captures an idealized **AI manager hierarchy system** derived from the research conversation in `../../../chat_history/ai-manager-hierarchy-system-research.md`.  
It is written to be:

- **Pattern-first**: it defines generic layers, stages, tools, and protocols.
- **Summary-neutral**: it does not assume in advance what the research “is about”; it reflects themes that actually appear.
- **Open-world and extensible**: any future tools, OSes, layers, and workflows that satisfy the interfaces here can participate without changing the core design.

Nothing in this spec is meant to exclude unmentioned concepts from the research.  
If something exists in the research (or is added later) and fits the patterns defined here, it is considered valid in this system.

---

<!-- section_id: "bb5635f4-5d67-4fa8-bb3e-68d0415bd6c2" -->
## 1. Goals and Core Ideas

<!-- section_id: "c8203a6d-b8a8-47fd-9f25-603252925120" -->
### 1.1 High-level Goal

Build an **Agent Operating System (Agent OS)** for software development that:

- Uses the filesystem as a **hierarchical configuration surface**.
- Orchestrates **manager → sub‑manager → worker** agents.
- Uses **chronological stages** to structure work (from request to archiving).
- Relies on **handoff documents** (JSON/Markdown) for persistent state and inter-agent communication.
- Supports **parallel execution** across many workers.
- Keeps **instructions sticky** via system-level or system-like prompts instead of bloated chat history.
- Remains **tool-agnostic and future-proof**.

<!-- section_id: "1d6cf1e8-ea64-46d8-a4e3-f69fef284e15" -->
### 1.2 Non-exclusion and Discovery Principles

To avoid hidden assumptions:

- **Non-Exclusion Principle**:  
  Any concept or tool in the research (and any future ones) is not “out of scope” simply because it is not named in this document. Enumerated items are examples, not exhaustive lists.

- **Discovery-before-framing**:  
  Document structure and emphasis are derived from:
  - What the research repeatedly discusses.
  - Explicit user goals (e.g., layered hierarchy, stage pipeline, tool comparison).
  - Observable relationships (e.g., Claude vs Codex vs Gemini vs Cursor behavior).

- **Pattern over instance**:  
  The spec defines patterns (e.g., “Tool Interface”, “Handoff Schema”) and then maps **current instances** (Claude Code, Codex CLI, Gemini CLI, Cursor IDE, OS types) into them.

---

<!-- section_id: "b56499ee-a275-4275-b512-1e59fb63d1f3" -->
## 2. Architecture Overview (Layers, Stages, Agents)

<!-- section_id: "3ac52cd8-69e0-4f10-b2c3-e1930ca29d0e" -->
### 2.1 Generic Layer Hierarchy

Layers represent **levels of abstraction/specificity**, similar to CSS:

- **Layer 0 (Universal)**  
  Global rules that apply everywhere: languages, security, general coding standards, universal workflows.

- **Layer 1 (Project)**  
  Project-specific constraints (domain, tech stack, business rules, project-level architecture).

- **Layer 2 (Feature)**  
  Feature-level logic and domain rules (e.g., “Auth System”, “Shopping Cart”, “ALEKS automation”).

- **Layer 3 (Component)**  
  Concrete implementation units within a feature (e.g., `LoginForm`, `PaymentGateway`, `GraphingWidget`).

- **Layer 4+ (Sub-component and deeper)**  
  Optional finer-grained units created for parallelism or separation of concerns (e.g., `login-form-ui`, `login-validation`, `login-api-handler`).

#### 2.1.1 Layer Properties

Every layer `L` has:

- A **Layer Manager** agent responsible for:
  - Accepting high-level tasks (from layer `L‑1` or external request).
  - Decomposing them into subtasks for:
    - Its own chronological stages.
    - Sub-layers `L+1` (sub‑managers/workers).
  - Aggregating results and generating upward handoffs.

- A **Context stack** composed of:
  - All higher-layer rules `L0…L-1`.
  - Its own layer rules `L`.
  - Optional OS/tool-specific overrides.

The system is defined for **any number of layers**; L0–L3/L4 are common, but it can extend deeper where useful.

<!-- section_id: "c852428f-2e19-4872-9fb8-537e38f3676a" -->
### 2.2 Chronological Stage Pipeline

Stages represent **time-ordered roles** in a development loop.  
Concrete stages used in the research, mapped to generic roles:

- **Request-like stages**  
  - `request/`  
  - Purpose: gather or clarify initial goals.

- **Instruction-like stages**  
  - `instructions/`  
  - Purpose: convert vague requests into explicit instructions and constraints.

- **Plan-like stages**  
  - `planning/`  
  - Purpose: decompose work into subtasks and task graphs.

- **Design-like stages**  
  - `design/`  
  - Purpose: select architectures, data flows, interfaces, UX patterns.

- **Implement-like stages**  
  - `implementation/`  
  - Purpose: write or modify code, configs, docs.

- **Test-like stages**  
  - `testing/`  
  - Purpose: generate and run tests, capture results.

- **Criticize-like stages**  
  - `criticism/`  
  - Purpose: review outputs against constraints and quality standards.

- **Fix-like stages**  
  - `fixing/`  
  - Purpose: apply corrections and refactors based on criticism and failures.

- **Archive-like stages**  
  - `archiving/` / `archives/`  
  - Purpose: consolidate artifacts, update documentation, record decisions.

The stage set is **open**: new stages can be added as long as they:

- Accept a handoff as input.
- Produce a compatible handoff as output.
- Respect the “don’t destroy previous stages’ artifacts” rule (append or refine).

<!-- section_id: "ddda49eb-6529-4f76-a502-194a87c4de0c" -->
### 2.3 Manager / Sub-Manager / Worker Model

The system uses a generic **Manager / Worker** abstraction:

- **Manager Agent (any layer)**  
  - Reads incoming handoffs.
  - Decides which stages and sub-layers to engage.
  - Spawns workers (potentially in parallel) via CLI or other mechanisms.
  - Aggregates results into new handoffs.

- **Worker Agent (leaf or near-leaf)**  
  - Reads exactly one incoming handoff.
  - Performs a bounded unit of work (ideally 1–3 main actions).
  - Writes one outgoing handoff (or set of artifacts) and exits.

Managers and workers are *roles*, not tied to specific tools. Any agent that satisfies this IO contract can be used as a manager or worker, regardless of model/provider.

#### 2.3.1 Example Hierarchy (Conceptual)

At a high level, the hierarchy may look like:

- L0 Manager → L1 Project Managers → L2 Feature Managers → L3 Component Managers → L3/L4 Workers.

Workers may themselves be managers of deeper sub-layers (e.g., L3 Manager controlling L4 workers).

---

<!-- section_id: "d85544ff-0d9d-4859-9749-75021795721e" -->
## 3. Tool Abstraction and Current Specializations

<!-- section_id: "76c669f0-dce9-4af4-8541-6d476c4ce04a" -->
### 3.1 Generic Tool Interface

Any tool (CLI, IDE agent, remote API) participating in this system is modeled as:

- **Inputs**
  - Some form of **system-like context** (rules, role, constraints).
  - One or more **handoff documents**.
  - An **environment** (OS, paths, credentials, network policy).

- **Behavior**
  - Reads context and handoff(s).
  - May read/write files, run commands, or call tools (subject to safety policies).
  - Produces new code, data, and at least one output handoff.

- **Outputs**
  - Zero or more modified artifacts (code, configs, docs).
  - One or more structured handoffs describing results and next steps.

This interface is independent of vendor (Anthropic, OpenAI, Google, local LLMs) and independent of particular CLIs.  
Claude Code, Codex CLI, Gemini CLI, Cursor IDE, as well as frameworks like LangGraph/AutoGen/CrewAI, can all be seen as implementations or compositions of this interface.

<!-- section_id: "da45955b-2595-4b2f-8319-5daf4800342f" -->
### 3.2 Current Tool Instances (Examples)

These are **current** examples from the research, not an exhaustive or permanent list.

#### 3.2.1 Claude Code

- Behaves as:
  - A strong **manager** (L0–L2) and **critic/fixer** (later stages).
  - A capable worker for complex multi-file coding tasks.
- System prompt:
  - Uses `CLAUDE.md` (global, project, subdir) plus flags/output styles.
  - Merges multiple sources into a single `system` field for each API call.
  - Re-injects system prompt on every call → high instruction stickiness.
- Fits well as:
  - **Layer managers** across the hierarchy.
  - **Criticism/fixing** stages for difficult, multi-file work.

#### 3.2.2 Codex CLI

- Behaves as:
  - A fast, code-focused **worker** for atomic tasks.
  - Limited as a manager due to fixed internal system prompt and chat-history-based custom prompts.
- Context:
  - Uses `AGENTS.md` (global and layered) which is injected as the first **user** message, not system.
  - Context drifts as sessions grow: good for 1–3 turns, not long sessions.
- Fits well as:
  - **Leaf workers** (L3/L4) performing one or two focused tasks per session:
    - Implement a small component.
    - Write or run tests.
    - Apply a simple refactor.

#### 3.2.3 Gemini CLI

- Behaves as:
  - A reasoning and research-focused **worker/manager**, especially for long conversations.
  - Can act as a sub-manager in some hierarchies (e.g., L1/L2 planning) via shell tools.
- Context:
  - Can set true `systemInstruction` (system-like prompt) via flags/env vars.
  - Does not automatically cascade prompts from the filesystem; merging is manual.
  - Large context window makes it suitable for long request/instructions sessions.
- Fits well as:
  - **Request/instructions/planning** stages at L1/L2, especially where many turns are needed.
  - **Research** roles (docs reading, API exploration).

#### 3.2.4 Cursor IDE

- Behaves as:
  - An IDE-centric **interactive orchestrator/worker** with:
    - Parallel agents in isolated worktrees.
    - Strong planning and refactoring agents.
  - Not directly callable from external CLIs.
- Context:
  - Uses `.cursor/rules/*.mdc` files as rules injected at the top of each request’s context.
  - Rules persist across requests and cascade by glob patterns and priorities.
- Fits well as:
  - **Human-in-the-loop** debugging, complex interactive refactors, and code exploration.
  - Not part of the automated CLI hierarchy, but very useful as a manual companion.

#### 3.2.5 Other Frameworks (LangGraph, AutoGen, CrewAI, MetaGPT, etc.)

The research also discusses **multi-agent frameworks** like:

- LangGraph (graph-based flows).
- AutoGen (conversational multi-agent coding).
- CrewAI (role-based teams).
- MetaGPT (predefined software-team patterns).

Within this spec, these frameworks are treated as:

- Potential **high-level orchestrators** or **specialized manager workers** that can:
  - Implement Manager interfaces (stages, subtasks, handoffs).
  - Call tools (CLIs, APIs) as workers.

They are not mandated; they are compatible implementations of the patterns defined here.

---

<!-- section_id: "9b03acf6-3b22-46ef-80dc-33324d915a7b" -->
## 4. Filesystem Layout and Cascading Rules

<!-- section_id: "1cd8fe13-d33a-4748-8e1f-85b45038eb3b" -->
### 4.1 Generic Layout Pattern

The filesystem acts as a **universal configuration database**.  
Abstractly:

- `layer_0_*` → universal layer.
- `layer_2_*` → project layers.
- `layer_2_*` → feature layers.
- `layer_4_*` → component layers.
- Optionally `layer_4_*` and deeper.

Each layer directory typically contains:

- A **manager system** (e.g., `<L>.00_ai_manager_system/`).
- **Manager handoffs** (e.g., `<L>.01_manager_handoff_documents/`).
- **Sub-layers** (e.g., `<L>.02_sub_layers/…`).
- A set of **stages** (e.g., `<L>.99_stages/`), each with:
  - `ai_agent_system/`
  - `hand_off_documents/`

The exact numeric prefixes can vary; what matters is that:

- There is a consistent mapping from filesystem paths to:
  - Layer index `L`.
  - Stage type.
  - Manager vs worker roles.

<!-- section_id: "103cc973-74dd-4a4e-ba02-5f73e82bf0bb" -->
### 4.2 Context Cascading

Every context system follows a **cascading rule**:

- Starting from the root of the repo (and global config locations), walk **down** toward the active directory.
- At each step, merge any relevant context files:
  - For Claude: `CLAUDE.md`.
  - For Codex: `AGENTS.md`.
  - For Gemini: `GEMINI.*` designated as system context.
  - For Cursor: `.cursor/rules/*.mdc` matching the current files.
- The active agent’s **effective context** is the combination of:
  - All global context.
  - All context in ancestor directories.
  - Context in the current directory (layer/stage/OS/tool).

This rule applies **generically**: any new context file type for a new tool can be incorporated by specifying a similar cascading rule.

<!-- section_id: "b0736e62-cf90-42cb-af74-ca562f728b10" -->
### 4.3 Example Cascade (Informal)

For a login implementation stage at L3:

- Layer 0 context: universal TypeScript and security rules.
- Layer 1 context: project-specific ecommerce rules.
- Layer 2 context: auth system rules (tokens, OAuth, rate limits).
- Layer 3 context: login component rules (CSRF, 2FA, UX constraints).
- Stage context: implementation-specific constraints (testing strategy, output format).

Each tool’s view:

- Claude Code: merges all relevant `CLAUDE.md` into the `system` field.
- Codex CLI: merges relevant `AGENTS.md` into an initial user message.
- Gemini CLI: manual merge of `GEMINI.*` into a systemInstruction file/env var.
- Cursor: merges `.cursor/rules/*.mdc` for universal, project, feature, and component rules.

---

<!-- section_id: "0ecaa189-b87c-4e44-93bf-926337fb1075" -->
## 5. Handoff Protocol (Schema and Flow)

<!-- section_id: "38535d61-16a1-4cbb-989f-ae008ed0f83d" -->
### 5.1 Generic Handoff Schema

Handoffs are **versioned, forward-compatible** documents.  
A generic JSON structure might include:

- `schemaVersion`: version of the handoff schema.
- `kind`: type of handoff (e.g., `request`, `plan`, `design`, `implResult`, `testResult`).
- `layer`: the logical layer number or ID.
- `stage`: the stage name (`request`, `planning`, etc.).
- `from`: identifier of the sending agent (layer, stage, tool).
- `to`: intended receiving agent(s).
- `task`: structured description of what needs to be done.
- `constraints`: list of rules and requirements.
- `artifacts`: references to files, URLs, or previous results.
- `subtasks`: list of subtasks (for planners/managers).
- `results`: stage-specific outputs (summaries, test results, diffs).
- `status`: e.g., `pending`, `in_progress`, `complete`, `failed`.

The schema is **extensible**: additional fields are allowed and should be ignored by agents that do not understand them.

<!-- section_id: "653423ab-827b-4910-9a5e-0d16377171cc" -->
### 5.2 Vertical Handoffs (Layer-to-Layer)

Vertical handoffs propagate work **up and down the abstraction stack**:

- L0 → L1: universal goals and constraints to project managers.
- L1 → L2: project-level tasks (e.g., “build auth feature for ecommerce project”) to feature managers.
- L2 → L3/L4: feature tasks to component/sub-component managers and workers.

These handoffs allow:

- High-level agents to push constraints downward.
- Low-level agents to report results upward with enough context for aggregation.

<!-- section_id: "417ff644-154d-4529-adb6-a5a1e77e3f2f" -->
### 5.3 Horizontal Handoffs (Stage-to-Stage)

Horizontal handoffs move work through the **chronological pipeline** within a layer:

- `request` → `instructions` → `planning` → `design` → `implementation` → `testing` → `criticism` → `fixing` → `archiving`.

Each stage:

- Reads from `hand_off_documents/incoming.*`.
- Writes to `hand_off_documents/outgoing.*`.
- Preserves prior context in the handoff while appending its own data (e.g., `plans`, `designs`, `testResults`), rather than deleting upstream fields.

Stages may be skipped or repeated if the handoff’s `status` or `kind` indicates that a loop is necessary (e.g., planning → design → planning again).

---

<!-- section_id: "2cb500b5-7ef4-44bf-a320-8c7822ac9294" -->
## 6. Execution and Orchestration Patterns

<!-- section_id: "f834deb8-537d-4153-b112-d7f7f25b1ee4" -->
### 6.1 Abstract Command Model

At runtime, all actions can be seen as calls to a generic function:

> `run_agent(layer, stage, tool, osVariant, options)`

Where:

- `layer`: e.g., `0`, `1`, `2`, `3`, `4`.
- `stage`: one of the stage names or a custom stage.
- `tool`: any tool/CLI/agent that implements the Tool Interface.
- `osVariant`: e.g., `wsl`, `ubuntu`, `windows`, `macos`, `custom-*`.
- `options`: additional configuration (timeouts, max turns, log levels).

Concrete wrapper scripts (e.g., `l3-impl-codex`, `l1-request-gemini`) are **named instances** of this interface.

<!-- section_id: "39ca7b2c-2f2a-41b2-a0f6-9fa42bd0d0ac" -->
### 6.2 Wrapper Responsibilities (Manager vs Stage)

Two broad wrapper types:

- **Manager Wrappers**
  - Run at layer manager locations.
  - Read high-level handoffs and global context.
  - Decide which stages and sub-layers to invoke (possibly in parallel).
  - Spawn stage wrappers or other manager wrappers.
  - Aggregate outputs into new handoffs for upper layers.

- **Stage Wrappers**
  - Run inside specific stage directories (e.g., `layer_2/.../stage_3.04_development/ai_agent_system`).
  - Load stage-relevant context (all cascading files + OS/tool variants).
  - Read `incoming` handoff.
  - Run one stage of work with bounded turns.
  - Write `outgoing` handoff.

The design does not limit how many wrappers exist; new wrappers can be added freely if they obey these responsibilities.

<!-- section_id: "0ac9157b-ff5d-49f0-b024-5af6c344f32a" -->
### 6.3 Parallel Execution

Managers can run multiple workers **in parallel** as long as:

- Their input and output handoffs are logically independent (or carefully synchronized).
- Available compute and rate limits are respected.

Typical patterns:

- L2 Manager:
  - Decomposes a feature into multiple components/sub-components.
  - Spawns one worker per component (e.g., UI, validation, API handler, docs).
  - Waits for each component’s `outgoing` handoff to arrive.
  - Aggregates results into a feature-level `results` handoff for upper layers.

This parallelism can scale to many workers across L3/L4 and beyond.

<!-- section_id: "923a1fc4-e18e-47a3-83bd-32fa45f4a5df" -->
### 6.4 Supervisor Patterns

Supervisors implement generic orchestration logic outside any specific agent:

- **Core behaviors**
  - Discover tasks by scanning handoffs and repo state.
  - Schedule tasks based on priority, dependencies, and resource budgets.
  - Launch wrappers via `run_agent`-like calls.
  - Monitor progress and collect results.
  - Handle failure: retries, fallbacks, escalation to humans or higher layers.

- **Implementation neutrality**
  - Can be written in Python, TypeScript, shell, or even as a higher-level LLM agent.
  - Can run locally, on CI, or in cloud infrastructure.

Frameworks like LangGraph or AutoGen can be used to implement or enhance these supervisors, but are not required for the architecture to hold.

---

<!-- section_id: "e1d63a85-b270-46d3-ad96-59debc6a00f8" -->
## 7. OS and Tool Variant “Quartet” Pattern

<!-- section_id: "f4745b77-6337-4fc6-a3fe-4924a346488e" -->
### 7.1 OS Variant Dimension

OS differences (WSL, Ubuntu, Windows, macOS, etc.) are treated as a separate **dimension** orthogonal to layers, stages, and tools:

- Each layer/stage directory may have:
  - `os/<os-id>/CLAUDE.md`
  - `os/<os-id>/AGENTS.md`
  - `os/<os-id>/GEMINI.*`
  - `os/<os-id>/.cursor/rules/*.mdc`

Where `<os-id>` is open-ended (e.g., `wsl`, `ubuntu`, `windows`, `macos`, `termux`, `freebsd`).

<!-- section_id: "a78d2006-5a83-40df-83fc-9b01e8dc0c40" -->
### 7.2 Auto-Selection

Launchers or supervisors:

- Detect the current OS/host environment via:
  - `OSTYPE`, `uname`, `WSL_DISTRO_NAME`, or other signals.
- Choose the matching `os/<os-id>/` context set.
- If no exact match exists, they may:
  - Fall back to a default OS variant.
  - Refuse to run until a proper variant is defined.

This pattern generalizes easily to new OSes: just add a new `os/<os-id>/` folder and detection rule.

<!-- section_id: "9ca5e5c0-20a0-4838-a2b4-546602194ecb" -->
### 7.3 Tool Extension

New tools can be integrated by:

- Defining a tool-specific context file type (e.g., `GROK.md`, `LLAMA.md`).
- Specifying how those files cascade and which field (system, messages, rules) they populate.
- Adding them as targets in the `run_agent` layer/stage mapping.

The Tool Interface and OS variant patterns ensure this can be done without revisiting the rest of the design.

---

<!-- section_id: "d5e72f49-1834-41d3-98ca-8df36e572074" -->
## 8. Token and Responsibility Strategy (Policy)

Tool usage is governed by a **policy mapping**:

> `(layer, stage, taskKind, environment) → toolProfile`

This mapping is not hard-coded; it can change over time as tools evolve.  
Current examples inferred from the research:

- Use **Claude Code** for:
  - L0–L2 managers and deep planning where prompt cascading is critical.
  - Criticism and fixing stages that span many files and complex refactors.

- Use **Codex CLI** for:
  - L3/L4 implementation/testing tasks where 1–3 turns suffice.
  - Situations where the overhead of long system prompts is undesirable.

- Use **Gemini CLI** for:
  - Request/instructions/planning stages that require long dialogues and/or heavy research.
  - Environments where large context windows are most beneficial.

- Use **Cursor IDE** for:
  - Manual debugging, interactive refactors, and exploratory work in your main editor.
  - Cases where an agent’s GUI capabilities are helpful but CLI automation is less important.

The policy is continuously revisable: future models (e.g., Gemini 3 or new local coders) can be swapped into any slot that matches the Tool Interface.

---

<!-- section_id: "fba37ceb-f5c6-497a-bb0a-01db5779e349" -->
## 9. Extensibility, Open World, and Additional Themes

<!-- section_id: "6216f2e3-e296-47ab-a181-e518be7d3875" -->
### 9.1 Extending Layers and Stages

- New layers (`layer_4_*`, `layer_5_*`, etc.) can be introduced by:
  - Following the same directory naming patterns.
  - Adding layer-level context files (quartets or more).
  - Ensuring managers and supervisors know how to traverse the new level.

- New stages can be added by:
  - Creating new stage directories within `*.99_stages`.
  - Defining their role and handoff transformations.
  - Updating the policy mapping to route tasks to appropriate tools.

<!-- section_id: "0c55e510-a923-4dfb-95ef-3c23b4cc1a60" -->
### 9.2 Additional Concepts from the Research

The research also touches on:

- **Token-cost optimization** and cost-aware routing.
- **Failure modes and workarounds** (e.g., Cursor terminal hangs, Codex prompt dilution).
- **Security and governance** concerns around prompt injection and context control.
- **Human-in-the-loop ergonomics**, especially with IDE-based agents.

These are compatible with the patterns here and can be expanded into dedicated documents or sections as needed.  
They are not considered “out of scope” merely because they are summarized lightly here.

<!-- section_id: "7f4a4f5b-8369-432d-8df0-1c650bc1dcc1" -->
### 9.3 Summary-Neutrality and Future Work

This specification does **not** claim the research is only about one thing.  
Rather, it:

- Distills a coherent architecture for an AI manager hierarchy system.
- Leaves room for all other themes to coexist and evolve alongside it.
- Provides patterns that any future tools, OSes, frameworks, or workflows can plug into.

Future work might include:

- A dedicated security/governance spec.
- A detailed supervisor implementation blueprint (Python/TS or LangGraph/AutoGen-based).
- Concrete examples tailored to specific projects in your workspace.

As long as new work respects the generic interfaces (Tool Interface, Handoff Schema, Layer/Stage patterns), it will remain compatible with this ideal AI manager hierarchy system.


