# Codex CLI — Application-Implemented Features

**Date**: 2026-02-27
**Focus**: What users must create/customize (the content and strategy)

---

## Overview

Codex provides the **mechanisms**. Users/teams must provide the **content and strategy**:

1. **AGENTS.md files** (what instructions to define)
2. **config.toml** (what settings to configure)
3. **Workspace initialization** (which projects to link)
4. **Session management** (when to resume or start new sessions)
5. **IDE extension setup** (which IDEs to integrate, what to configure)
6. **MCP server setup** (which external tools to connect)
7. **Project structure** (how to organize for AGENTS.md hierarchy)

---

## 1. AGENTS.md Files — Content & Strategy

### What You Must Create

Each AGENTS.md file is entirely user-written. Codex just **finds and loads** it; you decide **what goes in it**.

### Examples of Decisions YOU Make

**Global (~/.codex/AGENTS.md)**:
- What are my universal instructions? (code style, testing approach, documentation standards)
- What resources should always be available? (links to knowledge bases, rulebooks, conventions)
- What triggers apply to all projects? (when to load additional context, when to invoke MCP tools)

**Project-Level (/project/AGENTS.md)**:
- What's the tech stack? (languages, frameworks, libraries)
- What are project-specific conventions? (folder structure, naming patterns, commit format)
- What model and reasoning_effort should default to? (balance speed vs depth)
- What context window and max_tokens for this project?

**Directory-Level (/workspace/subdir/AGENTS.md)**:
- What's the purpose of THIS subdirectory? (API layer, UI components, data models)
- What constraints apply HERE? (don't touch legacy code, follow specific patterns)
- What should Claude know about THIS component before starting?

### User Responsibility

- **Write** AGENTS.md files from scratch
- **Maintain** accuracy (outdated AGENTS.md misleads Claude)
- **Update** when architecture changes
- **Keep concise** (context is limited)
- **Organize** content logically (you'll read these too)

---

## 2. config.toml — What & How to Configure

### What You Must Decide

`~/.codex/config.toml` and `/project/config.toml` are entirely user-managed.

### Strategic Decisions YOU Make

**Global Settings** (applies everywhere):
- What model family to default to? (opus for deep work, sonnet for speed, haiku for lightweight)
- What temperature setting? (0.7 for balanced, 0.0 for deterministic, 1.5+ for creative)
- What max_tokens default? (4096 for typical, 8192 for long responses, 2048 for quick answers)
- What reasoning_effort? (low for fast, medium for standard, high for complex)

**Project-Level Settings** (override global):
- Should this project use specific model? (e.g., research project always uses opus)
- Should max_tokens be different? (small APIs: 2048, large APIs: 8192)
- Should reasoning_effort be different? (ML projects: high, web projects: medium)

**Workspace Context**:
- How large is typical context needed? (small project: 50K tokens, large: 128K)
- Should GitHub integration be on? (if managing via GitHub, enable sync)
- What session_persistence setting? (persistent for long projects, ephemeral for experiments)

### User Responsibility

- **Decide** what settings matter for each project
- **Maintain** config.toml accuracy (wrong settings degrade experience)
- **Update** when project needs change (add reasoning_effort, increase max_tokens)
- **Balance** performance (higher reasoning = slower but more accurate)
- **Organize** settings logically (defaults at global, overrides at project)

---

## 3. Workspace Initialization — Which Projects to Link

### What You Must Decide

When you create a workspace, you choose which projects to link:

```bash
codex init https://github.com/user/repo  # Link to GitHub project
# OR
codex init  # Start with local project
# OR
codex init /path/to/existing/project  # Link to local directory
```

### Strategic Decisions YOU Make

**Initial Setup**:
- Which GitHub repository to link? (start with active project)
- What branch to use? (main/master for production, feature branch for WIP)
- What project structure? (single repo vs monorepo)

**Ongoing Workspace**:
- When to start new sessions? (per task, per day, per feature)
- When to resume old sessions? (continuing work, debugging same feature)
- How to organize sessions? (by feature, by date, by priority)

### User Responsibility

- **Choose** which projects to initialize
- **Link** repositories correctly (GitHub auth must be configured)
- **Manage** workspace state (archive old sessions, keep active ones)
- **Track** which session is active (current = context for this session)
- **Clean up** completed sessions (optional, but keeps workspace lean)

---

## 4. Session Management — When to Resume vs. Start New

### What You Must Decide

Codex provides session persistence, but **you** decide how to use it:

```bash
codex resume [session-id]  # Continue previous conversation
codex                       # Start new session (in current directory)
```

### Strategic Decisions YOU Make

**Session Boundaries**:
- One session per feature? (coherent context, can get long)
- One session per task? (focused, but many sessions)
- One session per day? (natural boundary, may lose context)

**Session Resumption**:
- When is old context valuable? (debugging same issue, continuing work)
- When should you start fresh? (new feature, unrelated task)
- What's the typical session lifespan? (2 hours, 8 hours, 1 day)

### User Responsibility

- **Decide** session boundaries (no right answer, personal preference)
- **Name/track** sessions meaningfully (list-sessions shows IDs, you track purpose)
- **Resume** appropriately (context matters for decision)
- **Archive** old sessions (clean up when done, optional)
- **Balance** context load (long sessions use more tokens)

---

## 5. IDE Extension Setup — Which IDEs to Integrate

### What You Must Decide

Codex integrates with VS Code, Cursor, Windsurf — but **you** choose which:

**VS Code**:
- Install extension from marketplace (codex-vscode)
- Configure in VS Code settings (model, reasoning_effort)
- Enable/disable features (inline completions, chat sidebar)

**Cursor**:
- Built-in Codex integration (no separate install)
- Configure in Cursor settings
- Leverage Cursor-specific features (Memory Bank, semantic search)

**Windsurf**:
- Install Codex extension if not built-in
- Configure agent-first workflow (Flow mode)
- Set IDE preferences

### Strategic Decisions YOU Make

**IDE Choice**:
- Which IDE for this project? (may use multiple)
- Should CLI and IDE stay in sync? (usually yes)
- What IDE-specific features to enable? (inline completions: yes/no)

**IDE-Specific Context**:
- Does IDE extend AGENTS.md? (Cursor reads AGENTS.md + .cursor/rules)
- Should IDE context differ from CLI? (usually same, but can customize per IDE)
- What context should IDE auto-include? (current file, directory, project)

### User Responsibility

- **Install** extensions (VS Code via marketplace, others as built-in)
- **Configure** for your workflow (keybindings, model, reasoning_effort)
- **Enable** useful features (chat sidebar, inline completions, Memory Bank)
- **Keep in sync** between CLI and IDE (same config.toml)
- **Customize** IDE-specific rules if needed (e.g., .cursor/rules in Cursor)

---

## 6. MCP Server Setup — Which External Tools to Connect

### What You Must Decide

Codex provides the **mechanism** to connect MCP servers. **You** decide:

**Which Servers to Use**:
- Canvas MCP (if managing Canvas-based courses)
- GitHub MCP (if integrating with repo operations)
- Tavily Search (if needing web search)
- Custom MCP server (your own tools/APIs)

**Installation & Configuration**:
- Each MCP server has its own installation process
- You configure API keys/credentials securely
- You enable/disable servers per project

**When to Use Each Server**:
- Do I need Canvas grades? → Load Canvas MCP
- Do I need GitHub repo access? → Load GitHub MCP
- Do I need web search? → Load Tavily

### User Responsibility

- **Research** which MCP servers exist (not part of Codex)
- **Install** servers (following their instructions)
- **Configure** credentials/API keys securely (no plain text in config)
- **Enable/disable** servers based on task (don't always load all)
- **Monitor** costs (some MCP servers are paid)
- **Update** servers as new versions release

---

## 7. Project Structure — How to Organize for AGENTS.md Hierarchy

### What You Must Decide

Codex provides **three-level hierarchy**. **You** decide:

**Project Structure**:
- How to organize code files? (by feature, by layer, by type)
- Should related code be in same folder? (enables AGENTS.md at that level)
- Are there "context clusters"? (files that should load together)

**AGENTS.md Placement**:
- Global ~/.codex/AGENTS.md — applies to all projects
- /project/AGENTS.md — applies to this project
- /project/src/AGENTS.md — applies to src/ subdirectory
- /project/src/api/AGENTS.md — applies to src/api/ subdirectory

**Naming Conventions**:
- Should files be named for easy reference? (AGENTS.md mentions them)
- Are long paths navigable? (Codex doesn't have @folder syntax like Claude Code)
- Can Codex easily find what it needs?

### Example Organization

**Good** (supports AGENTS.md hierarchy):
```
project/
├── AGENTS.md (project instructions)
├── src/
│   ├── AGENTS.md (src/ specific context)
│   ├── api/
│   │   ├── AGENTS.md (API guidelines)
│   │   ├── users.py
│   │   └── products.py
│   └── models/
│       ├── user.py
│       └── product.py
└── tests/
    └── test_api.py

User mentions src/api → Codex loads src/AGENTS.md AND src/api/AGENTS.md
```

**Poor** (hard to navigate):
```
project/
├── AGENTS.md
├── main.py (1000 lines: api, models, utils mixed)
└── helpers.py (2000 lines: helpers for everything)

Hard for Codex to know what context applies where
```

### User Responsibility

- **Organize** code logically (helps Codex find context)
- **Think** about AGENTS.md hierarchy (where should instructions live?)
- **Document** structure in AGENTS.md (explain layout)
- **Refactor** if organization becomes hard to navigate
- **Balance** with code quality (don't over-modularize just for AGENTS.md)

---

## Summary: Application-Implemented = Strategy & Content

| Aspect | Codex Does | You Must Provide |
|--------|-----------|------------------|
| **AGENTS.md** | Loads & merges hierarchy | Write content, decide what rules matter |
| **config.toml** | Parses & applies settings | Choose values, decide what to customize |
| **Workspace** | Initializes, syncs to cloud | Link projects, manage workspace state |
| **Sessions** | Persists automatically | Decide boundaries, when to resume |
| **IDE Integration** | Connects to IDEs | Install extensions, configure settings |
| **MCP Servers** | Connects & calls tools | Choose, install, configure servers |
| **Project Structure** | Loads AGENTS.md from hierarchy | Organize logically, enable AGENTS.md at right levels |

---

## Key Principle

**Codex provides the mechanisms. You provide the strategy and content.**

If Codex is not working well, the issue is usually:
- Outdated/inaccurate AGENTS.md
- Wrong config.toml settings (model, reasoning_effort, max_tokens)
- Workspace not properly initialized (project not linked)
- MCP server missing (needed tool not available)
- Project structure doesn't support AGENTS.md hierarchy
- IDE extension not installed or misconfigured
- Session boundaries not matching your workflow

All of these are **your** decisions, not Codex's.

