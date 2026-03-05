---
resource_id: "d5071c0c-65d6-4109-b6a2-96f48831b63e"
resource_type: "output"
resource_name: "APPLICATION_IMPLEMENTED"
---
# Cursor IDE — Application-Implemented Features

**Date**: 2026-02-27
**Focus**: What users must create/customize (the content and strategy)

---

<!-- section_id: "24fdd0a1-95d9-4ac2-95dd-ba482f8da969" -->
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

<!-- section_id: "01d2aed2-cb5d-4543-bdf2-a4eb3fbeeb98" -->
## 1. .cursor/rules Files — Content & Strategy

<!-- section_id: "2b48d9f8-f590-4490-92b7-e03856480ba9" -->
### What You Must Create

Cursor's rules are entirely user-defined. Cursor just **loads and applies** them; you decide **what goes in them**.

<!-- section_id: "1adc683a-4442-49c7-a5d1-79985b2916f6" -->
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

<!-- section_id: "46a31ff5-27ce-433e-babf-74b698d11b4a" -->
### User Responsibility

- **Write** rule files from scratch
- **Maintain** accuracy (outdated rules mislead Cursor)
- **Update** when code standards change
- **Test** rules work as intended (check AI responses)
- **Organize** rules hierarchically (global → project → component)

<!-- section_id: "da6dfd4e-0534-4986-8c74-f1cf085e731c" -->
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

<!-- section_id: "fc7fa3cc-c42c-4d13-969d-4f4e4b1aa942" -->
## 2. Memory Bank Organization — What to Remember

<!-- section_id: "78dce609-ec55-4017-801f-b0fe7619e285" -->
### What You Must Decide

Cursor provides Memory Bank storage; **you** decide **what to store and when**:

**Types of Memories**:
- **Project context** — Key info about current project (structure, important files, architecture decisions)
- **Session summaries** — What was accomplished, what's next
- **Decision logs** — Important choices and trade-offs
- **Bug trackers** — Known issues and their status
- **Reference guides** — Frequently needed information

<!-- section_id: "19a57693-71cf-4d31-a6cf-de5c40b276e1" -->
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

<!-- section_id: "bbfbcba1-b5ad-4ef1-a699-c3799473e3c1" -->
### User Responsibility

- **Create** useful memories (not every conversation)
- **Keep** memories up-to-date (stale memories are worse than none)
- **Organize** memories logically (Cursor finds relevant ones automatically)
- **Review** memories periodically (delete outdated ones)
- **Link** memories when they reference each other

<!-- section_id: "f672ef02-1c82-475e-b9c7-b105b8b25f3a" -->
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

<!-- section_id: "51b0ee50-cffd-4d22-bc21-f6aa19cc9346" -->
## 3. MCP Server Configuration — Which Tools to Enable

<!-- section_id: "736538a8-3cf8-4e6c-a053-cd017a3367fc" -->
### What You Must Decide

Cursor supports MCP servers; **you** decide **which to configure**:

**Available Servers** (examples):
- Canvas (access course assignments, grades)
- GitHub (repo operations, issue management)
- Tavily Search (web search)
- Custom servers (your own APIs)

<!-- section_id: "f8c6716d-a014-4df1-8921-c7a5d511dc48" -->
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

<!-- section_id: "b738e31e-d6a7-493f-815e-cc3d9a8fc384" -->
### User Responsibility

- **Research** which MCP servers exist (not part of Cursor)
- **Install** servers (following their documentation)
- **Configure** credentials securely (env vars, not hardcoded)
- **Test** server access (verify they work)
- **Enable/disable** servers per project (avoid unnecessary overhead)

<!-- section_id: "b57f0ace-ca2e-4c1b-9abf-1d0c4648db6f" -->
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

<!-- section_id: "77df8b7e-9a17-4686-8092-66a8fa6cbc66" -->
## 4. Hooks Configuration — Automation Triggers

<!-- section_id: "668677af-da0e-490b-b8ae-aa1e859c2e89" -->
### What You Must Decide

Hooks automate actions on file events; **you** decide **which hooks to set up**:

**Common Hook Scenarios**:
- Auto-format code on save
- Run tests automatically
- Lint before commit
- Generate documentation
- Update dependencies

<!-- section_id: "7904fd36-d060-40e0-8ce3-0f0f76de70ff" -->
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

<!-- section_id: "81188d7e-123c-47bd-acfc-1f2c564bb47f" -->
### User Responsibility

- **Define** which hooks matter for your workflow
- **Test** hooks work correctly (and don't slow down IDE)
- **Maintain** hook commands (update if tools change)
- **Balance** automation vs. control (too many hooks = slow IDE)
- **Document** why each hook exists

<!-- section_id: "44bd5186-6c44-492d-817b-1cac1f33aa69" -->
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

<!-- section_id: "21411a81-f590-4584-832d-73b58adae756" -->
## 5. Semantic Search Strategy — When/How to Use

<!-- section_id: "6a8b7cfb-5496-43f3-888e-d83f8d652ffe" -->
### What You Must Decide

Cursor provides semantic search; **you** decide **when to use it**:

**When Semantic Search Helps**:
- Finding similar code patterns across large projects
- Discovering related functionality in unfamiliar codebases
- Locating deprecated patterns for migration
- Understanding code relationships without knowing exact location

<!-- section_id: "bc1454fa-db46-4771-b669-a5ca3d59f78b" -->
### Strategic Decisions YOU Make

**Search Strategy**:
- How often to use semantic search vs. text search?
- What types of queries are most useful? (architectural, specific features)
- How to refine search queries for better results?

**Integration with Workflow**:
- Should semantic search be the default? (or use Ctrl+Shift+F for text search)
- When to switch from text search to semantic?

<!-- section_id: "ca65247b-c4b0-4777-be15-a1660f666ac8" -->
### User Responsibility

- **Learn** semantic search syntax and best practices
- **Experiment** with different query types
- **Balance** semantic vs. text search for different tasks
- **Understand** when semantic search might fail (edge cases)

<!-- section_id: "964af637-554c-46cf-9e8a-5a94439ddef2" -->
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

<!-- section_id: "328958f7-fc9b-4e45-acb4-712b5b77b9f4" -->
## 6. Agent CLI Task Definition — What to Delegate

<!-- section_id: "711a8843-a516-4f6b-8329-ba44e3277e44" -->
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

<!-- section_id: "d0112ab7-9d89-4909-b171-e65eaf9a9e17" -->
### Strategic Decisions YOU Make

**Task Selection**:
- What kinds of tasks are safe to delegate to agents?
- What requires human review before completion?
- What's the approval process? (interactive or batch)

**Agent Configuration**:
- How much autonomy should agents have?
- Should agents ask for confirmation? (before/after)
- What shell commands are allowed?

<!-- section_id: "a07a39a5-ff21-4bbb-9f13-b581f35f6eee" -->
### User Responsibility

- **Define** tasks clearly and specifically
- **Provide** context (relevant code, requirements, constraints)
- **Review** agent work before merging
- **Learn** what makes a good agent task (specific, bounded)
- **Avoid** vague or high-risk delegations

<!-- section_id: "ff012d8e-01f5-4e2f-8783-200c4964d408" -->
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

<!-- section_id: "192fe6a3-a1f0-48c1-8cc1-14a5a329bfc0" -->
## 7. IDE Workflow — How to Organize Work

<!-- section_id: "4e664172-2a1b-4234-86df-5c04b583d26e" -->
### What You Must Decide

How you work in Cursor depends on your preferences:

**Workflow Questions**:
- Chat-first or code-first? (use chat sidebar or inline suggestions)
- How to structure multi-file projects? (open tabs, use File Explorer)
- When to use Memory Bank? (per-session or per-task)
- How to leverage AI assistant? (request code, review, refactor, explain)

<!-- section_id: "b7631720-f1cb-4566-af5e-b0f1351110d4" -->
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

<!-- section_id: "5cda188b-e107-4812-9e59-c7f5cffb6983" -->
### User Responsibility

- **Develop** a workflow that works for your style
- **Experiment** with chat vs. inline vs. Memory Bank
- **Keep** rules and memories updated
- **Document** your workflow (for consistency)
- **Iterate** as you learn what works best

---

<!-- section_id: "c6e241b9-c4c7-470e-a5d3-af5b75e8b85e" -->
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

<!-- section_id: "bcde4c2a-2b17-48a5-9450-f25aa27fc97b" -->
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

