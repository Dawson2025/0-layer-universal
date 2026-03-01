# Claude Code CLI — Application-Implemented Features

**Date**: 2026-02-27
**Focus**: What users must create/customize (the content and strategy)

---

## Overview

Claude Code provides the **mechanisms**. Users/teams must provide the **content and strategy**:

1. **CLAUDE.md files** (what rules/instructions to define)
2. **MEMORY.md organization** (what knowledge to store)
3. **Skills creation** (reusable workflows you design)
4. **MCP server setup** (which external tools to connect)
5. **Subagent strategy** (when to parallelize work)
6. **Context management strategy** (how to stay under token limits)
7. **File organization** (how to structure project for @references)

---

## 1. CLAUDE.md Files — Content & Strategy

### What You Must Create

Each CLAUDE.md file is entirely user-written. Claude Code just **finds and loads** it; you decide **what goes in it**.

### Examples of Decisions YOU Make

**Global (~/.claude/CLAUDE.md)**:
- What are my universal rules? (file change visualization, commit protocol, etc.)
- What resources do I always want available? (rules, skills, knowledge bases)
- What triggers apply to all projects? (when to load context, when to invoke skills)

**Project-Level (/project/CLAUDE.md)**:
- What's the tech stack? (languages, frameworks, conventions)
- What are project-specific rules? (where to put files, how to test)
- What skills does this project need? (what `/commands` are available?)
- What layer/stage are we working in? (if using layer-stage system)

**Subdirectory-Level (/project/src/CLAUDE.md)**:
- What's the architecture of THIS module? (patterns, constraints)
- What's forbidden in this directory? (don't touch this, it's legacy)
- What should Claude know about THIS component?

### User Responsibility

- **Write** CLAUDE.md files from scratch
- **Maintain** accuracy (outdated CLAUDE.md misleads Claude)
- **Update** when architecture changes
- **Keep concise** (context is limited)
- **Organize** content logically (users read these too)

---

## 2. MEMORY.md — What & How to Remember

### What You Must Create

`~/.claude/projects/[project-id]/memory/MEMORY.md` is entirely user-managed.

### Strategic Decisions YOU Make

**What to put in first 200 lines** (auto-injected every session):
- Current project status (most important)
- Quick reference items (used every session)
- Key learnings (don't re-solve same problems)
- Navigation shortcuts (how to find things)

**What to put beyond 200 lines** (on-demand via `/memory`):
- Detailed notes (reference only when needed)
- Historical context (background, why decisions made)
- Topic-specific knowledge (debugging patterns, performance tips)

**Topic file strategy**:
- `debugging.md` — Debugging patterns and gotchas
- `patterns.md` — Code patterns, architectural patterns
- `api.md` — API endpoints, response formats
- `database.md` — Database schema, queries
- Custom topics as needed

### User Responsibility

- **Decide** what's important enough to remember
- **Organize** content (what goes in first 200 lines?)
- **Maintain** accuracy (update when reality changes)
- **Prune** old content (don't let it grow indefinitely)
- **Use `/remember`** to capture insights as you work
- **Balance** completeness vs. brevity

---

## 3. Skills Creation — Reusable Workflows

### What You Must Create

`~/.claude/skills/[skill-name]/SKILL.md` — entirely user-designed.

### Strategic Decisions YOU Make

**What skills to create**:
- Do I have a repeated workflow? (candidate for skill)
- Is it complex enough to document? (multi-step process)
- Will it save time if automated? (template + instructions)

**Skill structure** (you decide):
```markdown
---
name: skill-name
description: "What this skill does"
---

# [Skill Name]

## WHEN to Use
[List conditions]

## WHEN NOT to Use
[Counterexamples]

## Prerequisites
[What must be true first]

## Execution Steps
1. Step 1
2. Step 2
...

## Example Usage
[Real example]

## References
[Related documentation]
```

### Examples of Skills You Might Create

- **`/code-review`** — Systematic code review checklist
- **`/refactor`** — Refactoring template for specific pattern
- **`/debug`** — Debugging methodology for your codebase
- **`/test-new-feature`** — Test-first workflow for new features
- **`/performance-profile`** — Steps to find performance bottlenecks

### User Responsibility

- **Identify** workflows worth encapsulating
- **Document** clearly (other users will read this)
- **Maintain** as architecture evolves
- **Test** (invoke skill, verify it works)
- **Organize** logically (directory structure)

---

## 4. MCP Server Setup — Which Tools to Connect

### What You Must Decide

Claude Code provides the **mechanism** to connect MCP servers. **You** decide:

**Which servers to use**:
- Canvas MCP (for Canvas LMS access)
- GitHub MCP (for repo operations)
- Tavily Search (for web search)
- Custom MCP server (your own tools)

**Installation & configuration**:
- Each MCP server has its own setup
- You follow that server's installation docs
- You configure in `~/.claude/` or project-specific location

**When to use each server**:
- Do I need Canvas grades? → Load Canvas MCP
- Do I need GitHub repo access? → Load GitHub MCP
- Do I need web search? → Load Tavily

### User Responsibility

- **Research** which MCP servers exist (not part of Claude Code)
- **Install** servers (following their instructions)
- **Configure** credentials/API keys securely
- **Enable/disable** servers based on task
- **Monitor** costs (some MCP servers are paid)
- **Update** servers as new versions release

---

## 5. Subagent Strategy — When to Parallelize

### What You Must Decide

Claude Code provides subagent **capability**. **You** decide:

**When to spawn subagents**:
- Single agent sufficient? → Don't spawn
- Can work parallelize? → Consider subagents
- Multiple independent tasks? → Good candidate

**How many subagents**:
- Overhead increases with count
- Typical: 2-4 subagents per task
- Maximum: ~10 recommended

**What to give each subagent**:
- Clear, focused task description
- No parent conversation history (unless needed)
- Access to same MCP servers (if required)

### Example Strategy

```
Task: "Review codebase, test suite, and documentation"

Strategy (with subagents):
├─ Subagent 1: "Review code quality in src/"
├─ Subagent 2: "Analyze test coverage and test quality"
└─ Subagent 3: "Review docs for accuracy and completeness"

Parent agent: Aggregates summaries, identifies patterns
```

### User Responsibility

- **Analyze** task parallelizability
- **Write** clear task descriptions for subagents
- **Balance** overhead vs. benefit (parallelize only if worth it)
- **Monitor** costs (each subagent is an API call)
- **Learn** when parallelization helps vs. hurts

---

## 6. Context Management Strategy — Staying Under Limits

### What You Must Decide

Claude Code provides **auto-compaction**. **You** decide:

**Structuring information**:
- What goes in STATIC context (always loaded)?
- What goes in DYNAMIC context (loaded on-demand)?
- What goes in MEMORY.md vs. elsewhere?

**Managing file references**:
- Should I load full file or just snippet?
- Should I use @folder or @file?
- How much context can I spare for each file?

**When to split work**:
- Is this one session, or two?
- Should I use subagents to parallelize?
- Can I complete before context fills?

### Strategic Decisions

**Lean static context**:
- CLAUDE.md should be concise
- MEMORY.md first 200 lines should be essential only
- Defer details to on-demand loading

**Progressive disclosure**:
- Start narrow (specific question)
- Load more context only if needed
- Avoid "dump everything" approach

**Session management**:
- Know when context is filling
- Use `/compact` proactively if needed
- Save state and start fresh session if stuck

### User Responsibility

- **Design** context hierarchically
- **Measure** token usage (via `/context`)
- **Optimize** what's always-loaded vs. on-demand
- **Learn** your pattern (how much context needed for typical tasks)
- **Plan** for large work (multi-session, subagents, etc.)

---

## 7. File Organization — Structuring for @References

### What You Must Decide

Claude Code provides **@file/@folder** loading. **You** decide:

**Project structure**:
- How to organize code files?
- Should related code be in same folder?
- Are there "context clusters" (files that always load together)?

**Naming conventions**:
- Should files be named for easy @reference?
- Are long paths navigable?
- Can Claude find what it needs via @folder?

**What's in each file**:
- Related code together → easier to load with @folder
- Modular code split across files → load only needed @files

### Example Organization

**Good** (easy to @reference):
```
src/
├── auth/
│   ├── login.py
│   ├── register.py
│   └── password_reset.py
├── api/
│   ├── users.py
│   ├── products.py
│   └── orders.py
└── models/
    ├── user.py
    ├── product.py
    └── order.py

User says: "@src/auth/ Add error handling"
Claude loads all auth-related files
```

**Poor** (hard to @reference):
```
src/
├── main.py (1000 lines: auth, api, models mixed)
├── utils.py (2000 lines: helpers for everything)
└── config.py
```

### User Responsibility

- **Organize** code logically (helps Claude, not just humans)
- **Think** about @reference patterns (will Claude need these together?)
- **Document** structure (in CLAUDE.md: explain layout)
- **Refactor** if organization becomes hard to navigate
- **Balance** with code quality (don't over-modularize just for references)

---

## Summary: Application-Implemented = Strategy & Content

| Aspect | Claude Code Does | You Must Provide |
|--------|------------------|-----------------|
| **CLAUDE.md** | Loads & merges | Write content, decide what rules matter |
| **MEMORY.md** | Auto-injects 200 lines, stores full file | Organize content, decide what's essential |
| **Skills** | Loads & invokes on demand | Create skills, document workflows |
| **MCP Servers** | Connects & calls tools | Choose, install, configure servers |
| **Subagents** | Spawns, isolates, aggregates | Decide when to parallelize, write task descriptions |
| **Context Management** | Auto-compacts, reports usage | Design static/dynamic split, optimize balance |
| **File Organization** | Loads via @references | Structure logically, think about @reference patterns |

---

## Key Principle

**Claude Code provides the mechanisms. You provide the strategy and content.**

If Claude is confused or not working well, the issue is usually:
- Outdated/inaccurate CLAUDE.md
- Poor MEMORY.md organization
- Missing MCP server for needed capability
- Not using skills when you should
- Not parallelizing when beneficial
- Context too bloated (didn't curate static vs. dynamic)

All of these are **your** decisions, not Claude Code's.
