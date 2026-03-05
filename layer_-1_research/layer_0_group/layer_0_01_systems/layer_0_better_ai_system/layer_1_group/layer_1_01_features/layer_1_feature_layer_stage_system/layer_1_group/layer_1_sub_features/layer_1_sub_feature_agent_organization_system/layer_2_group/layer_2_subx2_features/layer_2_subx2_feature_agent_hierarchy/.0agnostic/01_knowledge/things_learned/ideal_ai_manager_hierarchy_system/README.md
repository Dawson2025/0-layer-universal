---
resource_id: "d7941d4a-4f95-42bc-ab5a-5c82f202ff6e"
resource_type: "readme
knowledge"
resource_name: "README"
---
<!-- section_id: "b1fadff5-9eac-4f6f-9280-03c4a2fc7fd1" -->
## Ideal AI Manager Hierarchy System – Directory Guide

This folder contains all of the documentation for your **Ideal AI Manager Hierarchy System**.  
It is organized so that:

- You (and your agents) can start from a **short summary**.
- Then drill down into **long-form specs** and **focused reference docs**.
- While keeping the overall structure clear and stable as the system grows.

This file explains the layout and how to use it.

---

<!-- section_id: "30c75766-8b99-4a8a-bff2-790beaf91dc0" -->
### 1. Top-Level Layout

Current contents:

- `summary/`
  - `README.md` – primary overview for agents and humans; short, context-friendly explanation of the system and links to everything else.
  - `IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md` – long-form specification of the ideal hierarchy, written in a summary-neutral, pattern-first way.

- `architecture.md`  
  – Detailed architecture: layers, stages, managers/workers, handoffs, supervisors, and parallelism.

- `tools_and_context_systems.md`  
  – How specific tools (Claude Code, Codex CLI, Gemini CLI, Cursor IDE, and others) implement the generic Tool Interface, with details about `CLAUDE.md`, `AGENTS.md`, `GEMINI.*`, `.cursor/rules/*.mdc`, etc.

- `os_and_quartets.md`  
  – How OS differences are modeled via `os/<os-id>/...` subfolders, and how tool-specific context “quartets” (and larger sets) are organized.

- `token_and_policy_strategy.md`  
  – Guidance on which tools to use for which layers/stages/tasks, with an explicit policy mapping that can be updated as models and costs change.

You may also have other helper files or subdirectories here in the future (e.g., templates, examples, or test cases). This guide should be updated if you add major new sections.

---

<!-- section_id: "aabda3d6-a4e7-4b30-ba62-fd27a4f380c6" -->
### 2. Recommended Reading Order

For a **human reader**:

1. Start with `summary/README.md` to get the mental model.
2. Skim `summary/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md` when you want the full conceptual spec.
3. Dive into:
   - `architecture.md` if you are working on filesystem layout, stages, or supervisors.
   - `tools_and_context_systems.md` if you are configuring or swapping tools.
   - `os_and_quartets.md` when you’re wiring up WSL/Ubuntu/Windows/macOS or new environments.
   - `token_and_policy_strategy.md` when tuning costs and choosing which tools to use where.

For an **AI agent**:

1. Provide `summary/README.md` as the initial context.
2. If more depth is needed, additionally provide:
   - `summary/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md`, and/or
   - A specific reference file (`architecture.md`, `tools_and_context_systems.md`, etc.) tailored to the task.

---

<!-- section_id: "450e0fce-1578-4f9b-8492-764c4c454f37" -->
### 3. How This Fits the Larger Repo

This directory is part of:

- `code/0_layer_universal/0_context/-1_research/things_learned/`

and is meant to capture **what you’ve learned** about:

- Layered AI manager hierarchies,
- Chronological stage pipelines,
- Tool specialization and context management,
- OS-aware orchestration and parallelism.

It is intentionally **decoupled from any one project** so that:

- You can re-use this architecture across multiple codebases in `code/`,
- And agents can load the same high-level rules no matter which project they are working on.

---

<!-- section_id: "a21e9897-6f50-474e-9a12-840355d8624a" -->
### 4. Evolving the Structure

As you continue refining your system, you can:

- Add new reference documents here (e.g., `security_and_governance.md`, `examples/`).
- Update `summary/README.md` and this guide to point to new material.
- Keep `summary/README.md` and `summary/IDEAL_AI_MANAGER_HIERARCHY_SYSTEM.md` as the **canonical overview** files.

The goal is that anyone (or any agent) who lands in this folder can quickly answer:

- “What is this system?”  
- “Where do I start?”  
- “Where do I find the deep details I need for my task?”  

and then navigate accordingly.


