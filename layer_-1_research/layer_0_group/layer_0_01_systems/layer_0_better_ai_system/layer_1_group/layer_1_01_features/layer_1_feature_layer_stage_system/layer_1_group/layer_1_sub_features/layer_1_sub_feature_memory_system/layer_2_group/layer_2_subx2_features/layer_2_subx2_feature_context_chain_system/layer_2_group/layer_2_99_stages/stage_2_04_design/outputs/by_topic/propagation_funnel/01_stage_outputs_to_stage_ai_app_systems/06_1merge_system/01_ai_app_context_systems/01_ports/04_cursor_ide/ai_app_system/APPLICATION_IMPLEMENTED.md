---
resource_id: "d5071c0c-65d6-4109-b6a2-96f48831b63e"
resource_type: "output"
resource_name: "APPLICATION_IMPLEMENTED"
---
# Cursor IDE — Application-Implemented Features

**Date**: 2026-02-27
**Focus**: What users must create/customize (the content and strategy)

---

## Overview

Cursor provides the **mechanisms**. Users/developers must provide the **strategy and content**:

1. **.cursor/rules files** (context rules strategy)
2. **Memory Bank organization** (what to remember and when)
3. **MCP server configuration** (.cursor/mcp.json setup)
4. **Hooks configuration** (automation triggers)
5. **Semantic search strategy** (when/how to use search)
6. **Agent CLI task definition** (what tasks to delegate)
7. **IDE workflow** (how to organize work in Cursor)

---

## 1. .cursor/rules Files — Content & Strategy

### What You Must Create

Cursor's rules are entirely user-defined. Cursor just **loads and applies** them; you decide **what goes in them**.

### Examples of Decisions YOU Make

**Global Rules** (`~/.cursor/rules/`):
- What code style conventions? (naming, formatting, patterns)
- What testing approach? (unit, integration, e2e)
- What security constraints? (no hardcoded secrets, input validation)
- What documentation standards? (JSDoc, docstrings, README format)

**Project Rules** (`project/.cursor/rules/`):
- What's unique to this project? (specific patterns, tech stack)
- What frameworks/libraries are in use? (React, Django, custom)
- What folder structure and conventions? (src/, tests/, config/)
- What are the main constraints? (performance targets, compatibility)

**Component-Level Rules** (`project/src/components/.cursor/rules/`):
- What's specific to this component? (API contracts, state management)
- What should the AI know about dependencies? (external libraries, internal modules)
- What patterns should be followed here? (component structure, hooks usage)

### User Responsibility

- **Write** rule files from scratch
- **Maintain** accuracy (outdated rules mislead Cursor)
- **Update** when code standards change
- **Test** rules work as intended (check AI responses)
- **Organize** rules hierarchically (global → project → component)

### Example Rule Structure

```yaml
---
mode: "Always Apply"
description: "JavaScript/TypeScript best practices"
---

# Code Style
- Use ES6+ syntax exclusively
- Prefer `const` over `let` over `var`
- Use camelCase for variables and functions
- Use PascalCase for classes and components
- Use UPPER_SNAKE_CASE for constants

# Imports
- Sort imports: third-party libraries first, then local imports
- Use absolute imports from src (import from 'components/...' not '../../components/...')
- Avoid circular imports

# Functions
- Prefer pure functions
- Add JSDoc comments to exported functions
- Include type hints (TypeScript)
- Keep functions focused (single responsibility)

# Testing
- Write tests for all exported functions
- Use Jest for unit tests
- Use React Testing Library for component tests
- Aim for >80% code coverage

# Security
- Never hardcode API keys or secrets
- Validate all user inputs
- Sanitize HTML content
- Use HTTPS for all external requests
```

---

## 2. Memory Bank Organization — What to Remember

### What You Must Decide

Cursor provides Memory Bank storage; **you** decide **what to store and when**:

**Types of Memories**:
- **Project context** — Key info about current project (structure, important files, architecture decisions)
- **Session summaries** — What was accomplished, what's next
- **Decision logs** — Important choices and trade-offs
- **Bug trackers** — Known issues and their status
- **Reference guides** — Frequently needed information

### Strategic Decisions YOU Make

**What to Remember**:
- Which project-wide conventions matter most?
- What are the critical design decisions?
- What gotchas should Cursor know about?
- What is the project roadmap?

**Memory Organization**:
- One memory per topic? Or combined?
- How detailed? (summary vs. full reference)
- When to update memories? (daily, weekly, per-session)

**Memory Lifecycle**:
- When are memories stale? (after X days)
- Should memories be archived? (move old ones elsewhere)

### User Responsibility

- **Create** useful memories (not every conversation)
- **Keep** memories up-to-date (stale memories are worse than none)
- **Organize** memories logically (Cursor finds relevant ones automatically)
- **Review** memories periodically (delete outdated ones)
- **Link** memories when they reference each other

### Example Memory Structure

```markdown
# Project: E-commerce Platform

## Architecture Overview
- Monorepo with 3 main packages: frontend (React), backend (Node.js), shared
- Database: PostgreSQL with Prisma ORM
- Deployment: Docker + Kubernetes
- Key services: auth, payments, inventory

## Important Decisions
- Chose Next.js for SSR capabilities (not CRA)
- Using Postgres for transactions (not MongoDB)
- Implemented custom auth (not Auth0) for PCI compliance

## Current Phase
- Q1 2026: Payment redesign
- High-priority: Reduce payment processing time by 50%
- Known issue: Checkout flow has 15% abandonment rate

## Gotchas
- `NODE_ENV` must be set before running migrations
- Prisma client must be regenerated after schema changes
- Database timeouts if queries take >30 seconds

## Team Conventions
- PR reviews required before merge
- All commits must have linked issue
- Deployment only on Tuesdays (if possible)
```

---

## 3. MCP Server Configuration — Which Tools to Enable

### What You Must Decide

Cursor supports MCP servers; **you** decide **which to configure**:

**Available Servers** (examples):
- Canvas (access course assignments, grades)
- GitHub (repo operations, issue management)
- Tavily Search (web search)
- Custom servers (your own APIs)

### Strategic Decisions YOU Make

**Which Servers to Use**:
- Do I need Canvas? (if managing courses)
- Do I need GitHub? (if working on multi-repo projects)
- Do I need web search? (research-heavy work)
- Do I have custom APIs to integrate?

**Server Configuration**:
- What credentials are needed? (API keys, tokens)
- How to store secrets securely? (env vars, credential manager)
- Per-project or global? (share across projects or specific?)

### User Responsibility

- **Research** which MCP servers exist (not part of Cursor)
- **Install** servers (following their documentation)
- **Configure** credentials securely (env vars, not hardcoded)
- **Test** server access (verify they work)
- **Enable/disable** servers per project (avoid unnecessary overhead)

### Example MCP Configuration

```json
{
  "mcpServers": {
    "canvas": {
      "command": "python",
      "args": ["-m", "mcp_canvas"],
      "env": {
        "CANVAS_API_TOKEN": "${CANVAS_TOKEN}",
        "CANVAS_API_URL": "https://canvas.instructure.com/api/v1"
      }
    },
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    },
    "tavily": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-tavily"],
      "env": {
        "TAVILY_API_KEY": "${TAVILY_API_KEY}"
      }
    }
  }
}
```

**Storage**:
- Save to `.cursor/mcp.json` (project-specific)
- Or `~/.cursor/mcp.json` (global)
- Use environment variables for secrets (`${VAR_NAME}`)

---

## 4. Hooks Configuration — Automation Triggers

### What You Must Decide

Hooks automate actions on file events; **you** decide **which hooks to set up**:

**Common Hook Scenarios**:
- Auto-format code on save
- Run tests automatically
- Lint before commit
- Generate documentation
- Update dependencies

### Strategic Decisions YOU Make

**Which Hooks to Use**:
- Should code format automatically? (eslint --fix)
- Should tests run on save? (npm test on changed files)
- Should linting block save? (eslint --strict)
- Should documentation generate? (jsdoc on file create)

**Hook Scope**:
- Apply to all files? Or specific patterns?
- Run synchronously or asynchronously?
- Block the save or run in background?

### User Responsibility

- **Define** which hooks matter for your workflow
- **Test** hooks work correctly (and don't slow down IDE)
- **Maintain** hook commands (update if tools change)
- **Balance** automation vs. control (too many hooks = slow IDE)
- **Document** why each hook exists

### Example Hook Configuration

```json
{
  "hooks": {
    "pre-save": [
      {
        "event": "file.save",
        "command": "eslint --fix ${file}",
        "glob": "src/**/*.js",
        "description": "Auto-format JavaScript on save"
      },
      {
        "event": "file.save",
        "command": "black --quiet ${file}",
        "glob": "src/**/*.py",
        "description": "Auto-format Python on save"
      }
    ],
    "post-save": [
      {
        "event": "file.save",
        "command": "npm test -- ${file}",
        "glob": "src/**/*.test.js",
        "description": "Run tests for changed test files"
      }
    ],
    "on-create": [
      {
        "event": "file.create",
        "command": "jsdoc ${file} --nocolor",
        "glob": "src/**/*.js",
        "description": "Generate JSDoc documentation"
      }
    ]
  }
}
```

---

## 5. Semantic Search Strategy — When/How to Use

### What You Must Decide

Cursor provides semantic search; **you** decide **when to use it**:

**When Semantic Search Helps**:
- Finding similar code patterns across large projects
- Discovering related functionality in unfamiliar codebases
- Locating deprecated patterns for migration
- Understanding code relationships without knowing exact location

### Strategic Decisions YOU Make

**Search Strategy**:
- How often to use semantic search vs. text search?
- What types of queries are most useful? (architectural, specific features)
- How to refine search queries for better results?

**Integration with Workflow**:
- Should semantic search be the default? (or use Ctrl+Shift+F for text search)
- When to switch from text search to semantic?

### User Responsibility

- **Learn** semantic search syntax and best practices
- **Experiment** with different query types
- **Balance** semantic vs. text search for different tasks
- **Understand** when semantic search might fail (edge cases)

### Example Semantic Search Queries

```
# Good queries (semantic search excels)
"How do we handle authentication?"
"Find all database migrations"
"Where are state updates handled?"
"Show error handling patterns"

# Better suited for text search (use Ctrl+Shift+F)
"find all instances of 'const token'"
"search for 'TODO comments"
"locate specific variable names"
```

---

## 6. Agent CLI Task Definition — What to Delegate

### What You Must Decide

Cursor Agent CLI can execute tasks autonomously; **you** decide **what tasks to delegate**:

**Good Tasks for Agents**:
- Refactoring (rename variables, reorganize code)
- Bug fixing (investigate and fix)
- Feature implementation (based on detailed spec)
- Testing (write and fix tests)
- Documentation (write docs, update READMEs)

**Poor Tasks for Agents**:
- Vague requests ("make the app better")
- Tasks requiring deep business logic knowledge
- Tasks with high ambiguity
- High-risk changes (database schema changes)

### Strategic Decisions YOU Make

**Task Selection**:
- What kinds of tasks are safe to delegate to agents?
- What requires human review before completion?
- What's the approval process? (interactive or batch)

**Agent Configuration**:
- How much autonomy should agents have?
- Should agents ask for confirmation? (before/after)
- What shell commands are allowed?

### User Responsibility

- **Define** tasks clearly and specifically
- **Provide** context (relevant code, requirements, constraints)
- **Review** agent work before merging
- **Learn** what makes a good agent task (specific, bounded)
- **Avoid** vague or high-risk delegations

### Example Agent Tasks

```bash
# Good: Specific and bounded
cursor agent "Add TypeScript types to src/utils.js. \
  Make all functions have return type annotations. \
  Keep behavior identical."

# Good: Clear requirements
cursor agent "Refactor src/auth.js to use async/await. \
  Replace all Promise chains with async/await syntax. \
  Keep all error handling intact."

# Poor: Vague
cursor agent "Improve the code quality"

# Poor: High-risk without context
cursor agent "Update the database schema"

# Better (with context):
cursor agent "Update database schema: add 'email' column to users table. \
  Run migrations in test environment first. \
  Generate migration file and update schema.prisma"
```

---

## 7. IDE Workflow — How to Organize Work

### What You Must Decide

How you work in Cursor depends on your preferences:

**Workflow Questions**:
- Chat-first or code-first? (use chat sidebar or inline suggestions)
- How to structure multi-file projects? (open tabs, use File Explorer)
- When to use Memory Bank? (per-session or per-task)
- How to leverage AI assistant? (request code, review, refactor, explain)

### Strategic Decisions YOU Make

**Chat vs. Inline**:
- Use chat for high-level discussions and planning
- Use inline suggestions for quick fixes and completions
- Use chat for multi-file refactoring

**Context Management**:
- Keep relevant files open in tabs
- Use current file context automatically
- Use Memory Bank for long-context needs

**AI Interaction Style**:
- Request complete implementations or outlines?
- Ask for explanations or just accept code?
- Use AI for code review or just generation?

### User Responsibility

- **Develop** a workflow that works for your style
- **Experiment** with chat vs. inline vs. Memory Bank
- **Keep** rules and memories updated
- **Document** your workflow (for consistency)
- **Iterate** as you learn what works best

---

## Summary: Application-Implemented = Strategy & Content

| Aspect | Cursor Does | You Must Provide |
|--------|-----------|------------------|\
| **.cursor/rules** | Loads and applies them | Write content, decide conventions |
| **Memory Bank** | Stores and retrieves | Decide what to remember, keep updated |
| **MCP Servers** | Manages and routes tools | Choose servers, configure credentials |
| **Hooks** | Executes on file events | Define hooks, test them |
| **Semantic Search** | Finds similar code | Use strategically, refine queries |
| **Agent CLI** | Executes tasks autonomously | Define tasks clearly, review results |
| **Workflow** | Provides IDE features | Organize work, use features intentionally |

---

## Key Principle

**Cursor provides the mechanisms. You provide the strategy and content.**

If Cursor is not helping you effectively, the issue is usually:
- Outdated or inaccurate .cursor/rules files
- Memory Bank not being maintained (stale memories)
- MCP servers not configured or needed tools missing
- Hooks not set up (missing automation opportunities)
- Not using semantic search strategically
- Asking agents for vague or high-risk tasks
- IDE workflow not optimized for your style

All of these are **your** decisions, not Cursor's.

