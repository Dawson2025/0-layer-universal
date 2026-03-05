---
resource_id: "5c480dc7-3485-44c2-98b0-ec2cebd3f099"
resource_type: "output"
resource_name: "PORTING_STRATEGY"
---
# Codex CLI — Porting Strategy

**Date**: 2026-02-27
**Focus**: How to port 0AGNOSTIC.md file AND .0agnostic/ directory system into Codex

---

<!-- section_id: "5baf583a-8295-47b8-8a44-94037137f624" -->
## Part 1: Porting 0AGNOSTIC.md (The File)

<!-- section_id: "c057477e-8120-45f8-80d8-795c352a1064" -->
### Understanding 0AGNOSTIC.md

Your 0AGNOSTIC.md follows a two-level structure:

```markdown
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──
  ## Identity
  ## Key Behaviors
  ## Triggers
  ## Delegation Contract

# ── Current Status ──
  ## Current Status

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──
  ## Current State Detail

# ── References ──
  ## Navigation
  ## Resources
```

<!-- section_id: "4879a64b-99b1-40cd-bb16-30ff0910defa" -->
### Port 0AGNOSTIC.md → AGENTS.md (Three-Level Structure)

Codex uses a simpler three-level structure. Here's how to map your content:

#### Mapping Table: 0AGNOSTIC.md → Codex AGENTS.md

| From (0AGNOSTIC.md) | To (AGENTS.md) | How | Notes |
|-------------|---------------|-----|-------|
| Identity | `## Identity` (top of file) | Copy verbatim | Who are we, what's our role, scope |
| Key Behaviors | `## Key Behaviors` | Copy verbatim | What should this AI do, mindset |
| Triggers | `## Triggers` (table) | Copy verbatim | When does this context apply |
| Current Status | `## Current Status` | Copy as summary | One-line status of phase/readiness |
| Delegation Contract | `## Delegation Contract` (table) | Summarize inputs/outputs | What we receive, what we produce |
| Resources | `## Resources` (table) | Create mapping table | Where to find knowledge, rules, skills |
| Navigation | `## Navigation` (table) | Create path pointers | Parent, children, key directories |

#### Part 1.1: Create Global AGENTS.md

Create `~/.codex/AGENTS.md` with identity and triggers that apply to ALL projects:

```markdown
# Global Codex Instructions

## Identity

**Role**: AI Assistant for code work across all projects
**Scope**: Universal context, rules, and behaviors
**Parent**: None (global)

### Key Behaviors

- Always follow [CRITICAL] rules first
- Check project-level AGENTS.md for overrides
- Load directory-level AGENTS.md if in subdirectory
- Report context usage when asked

## Triggers

| Situation | Action |
|-----------|--------|
| Starting any project | Load project/AGENTS.md next |
| Entering subdirectory | Check for subdir/AGENTS.md |
| Need rules | Load from ~/.codex/AGENTS.md + project/AGENTS.md |
| Need resources | Check Resources table below |

## Resources

| Type | Path | Purpose |
|------|------|---------|
| Universal Rules | ~/.codex/rules/ | Always-apply rules (static) |
| Project Rules | [project]/config.toml | Project-specific settings |
| Knowledge | [project]/knowledge/ | Domain knowledge files |
| Tools | MCP servers | External tool integration |
```

#### Part 1.2: Create Project AGENTS.md

For each project, create `/project/AGENTS.md` with project-specific instructions:

```markdown
# [Project Name] — Codex Instructions

## Identity

**Role**: Project AI Assistant
**Scope**: All work in this project
**Parent**: ~/.codex/AGENTS.md (global)
**Tech Stack**: [languages, frameworks]

### Key Behaviors

[Project-specific behaviors: code style, testing approach, documentation]

## Triggers

| Situation | Action |
|-----------|--------|
| User mentions [keyword] | Load [specific context] |
| Working on [module] | Consider [specific approach] |

## Current Status

**Phase**: [design/development/testing]
**Status**: [brief summary]

## Resources

| Type | Path | Purpose |
|------|------|---------|
| Architecture Docs | /docs/ | Design decisions |
| Code Patterns | /src/patterns/ | Reusable patterns |
| Tests | /tests/ | Test examples |

## Model Settings

```toml
model = "codex-sonnet"
reasoning_effort = "medium"
max_tokens = 4096
```
```

#### Part 1.3: Create Directory-Level AGENTS.md (Optional)

For important subdirectories, create `/project/src/AGENTS.md` with context specific to that directory:

```markdown
# src/ Module Instructions

## What's in This Directory

[Description of src/ module]

## Rules for This Directory

[Module-specific conventions]

## Key Files

[Important files to remember]
```

<!-- section_id: "66abe894-2e44-42e5-ab01-ebaa86605e03" -->
### Port 0AGNOSTIC.md DYNAMIC Sections → External Files

Your DYNAMIC context (everything after the marker) should be stored as separate files that you reference from AGENTS.md:

```markdown
# AGENTS.md

## Resources

| Type | Path | Purpose |
|------|------|---------|
| Architecture | /docs/architecture.md | Design decisions |
| API Reference | /docs/api.md | Endpoints, schemas |
| Database | /docs/database.md | Schema, migrations |
| Deployment | /docs/deployment.md | How to deploy |
```

Then create `/docs/` files as-needed. Codex will read them when you reference them in your prompts ("read /docs/architecture.md").

---

<!-- section_id: "3849b214-146d-476e-a24d-e2df7fd3ff8b" -->
## Part 2: Porting .0agnostic/ Directory Structure

<!-- section_id: "0b14fe42-58a1-479e-aeb8-495e7a6f5aea" -->
### Understanding .0agnostic/

Your .0agnostic/ has 9 numbered subdirectories:

```
.0agnostic/
├── 01_knowledge/          # Domain knowledge (per-topic)
├── 02_rules/              # Rules (static + dynamic)
├── 03_protocols/          # Step-by-step procedures
├── 04_episodic_memory/    # Session history
├── 05_handoff_documents/  # Handoff between agents
├── 06_context_avenue_web/ # Multi-avenue context (agents, skills, etc.)
├── 07+_setup_dependant/   # Machine/OS-specific setup
└── [everything maps to Codex somehow]
```

<!-- section_id: "e1caac5b-b37b-4dad-9941-55b9b07942fa" -->
### Port .0agnostic/ → Codex

#### 01_knowledge → config.toml + Documentation Files

**Port to**:
- Important settings → `config.toml` (model, reasoning_effort, max_tokens)
- Knowledge docs → `/docs/`, `/knowledge/`, or project README
- Principles → Inline in AGENTS.md (brief summary)
- Resources/templates → Separate files referenced in AGENTS.md

**Example**:
```
.0agnostic/01_knowledge/
├── principles/
│   └── lean_context.md         → Inline summary in AGENTS.md
├── docs/
│   ├── architecture.md         → /docs/architecture.md
│   └── api_design.md           → /docs/api.md
└── resources/
    └── templates/
        └── entity_template.md  → /templates/entity.md
```

**Porting**:
```bash
# Copy knowledge docs to project
cp .0agnostic/01_knowledge/docs/*.md /docs/

# Reference in AGENTS.md
cat << 'EOF' >> /project/AGENTS.md

## Resources

See /docs/ for detailed knowledge:
- architecture.md: Design decisions
- api.md: API reference
- deployment.md: Deployment guide
EOF
```

#### 02_rules → AGENTS.md + config.toml

**Port to**:
- Static rules (always-apply) → AGENTS.md `## [CRITICAL] Rules` section
- Dynamic rules (scenario-triggered) → Inline in AGENTS.md `## Rules` table
- Config rules → `config.toml` settings

**Example**:
```
.0agnostic/02_rules/
├── static/
│   ├── I0_FILE_CHANGE_REPORTING.md  → Inline in AGENTS.md
│   └── commit_protocol.md           → Reference in AGENTS.md
└── dynamic/
    └── grade_strategy_triggers/
        └── triggers.md              → Triggers table in AGENTS.md
```

**Porting**:
```markdown
# AGENTS.md

## [CRITICAL] Rules

[Copy from .0agnostic/02_rules/static/]
- Always report file changes
- Follow git commit protocol
- Maintain this-file accuracy

## Rules (Dynamic)

| Trigger | Rule |
|---------|------|
| User asks about grades | Load grade_strategy_context |
| Modifying AGENTS.md | Update config.toml too |
| New session | Check /docs/onboarding.md |
```

#### 03_protocols → /docs/ or /knowledge/

**Port to**:
- Procedures → `/docs/procedures/` or `/knowledge/` directory
- Reference from AGENTS.md when needed
- Complex procedures → README files in relevant directories

**Example**:
```
.0agnostic/03_protocols/
├── grade_strategy_system/
│   ├── canvas_grade_dashboard_trajectory.md  → /docs/procedures/grade_dashboard.md
│   └── assignment_classification.md          → /docs/procedures/classify_assignments.md
└── ...
```

**Porting**:
```bash
# Copy protocols to docs
cp -r .0agnostic/03_protocols/ /docs/procedures/

# Reference in AGENTS.md
# See /docs/procedures/ for step-by-step guides
```

#### 04_episodic_memory → Session Management Strategy

**Port to**:
- Don't copy files (Codex has its own session history)
- Instead, document your session management in AGENTS.md
- Use Codex's built-in `codex resume [session-id]` instead

**How to Port**:
```markdown
# AGENTS.md

## Session Management Strategy

**Boundary**: One session per feature/task
**Resumption**: Use `codex resume [session-id]` to continue
**Cleanup**: Archive completed sessions monthly

Current active sessions: [list important ones]
```

#### 05_handoff_documents → Project README or Wiki

**Port to**:
- Don't create formal handoff documents (Codex works synchronously)
- Instead, document responsibilities in README
- Use AGENTS.md current status + project structure to communicate
- If multi-agent work: use GitHub Issues or projects

**How to Port**:
```markdown
# README.md

## Architecture

[Port from handoff docs]

## Active Work

[Current status]

## Dependencies

[What we depend on, what depends on us]
```

#### 06_context_avenue_web → Skills, Tools, Agents

**Port to**:
- 01_aalang/ → Document agent patterns in /docs/agents.md
- 05_skills/ → MCP servers or inline procedures in AGENTS.md
- 06_agents/ → Document coordinating patterns if multi-agent
- 08_hooks/ → No direct port (Codex doesn't have hooks)

**How to Port**:

**AALang Agents** (01_aalang/):
```bash
# Port to documentation (not executable in Codex)
# Create /docs/agent_patterns.md describing the pattern

cat << 'EOF' > /docs/agent_patterns.md
# Agent Patterns

## 5-Mode-13-Actor Pattern

[Describe the pattern you use]
[Document the modes and what each does]
[Link to specific agent responsibilities]
EOF
```

**Skills** (05_skills/):
```bash
# Port to MCP servers (if tool-like) or procedures

# If skill is a reusable procedure:
cp .0agnostic/06_context_avenue_web/01_file_based/05_skills/*/SKILL.md /docs/procedures/

# If skill is tool-like, create MCP server or document as procedure
```

#### 07+_setup_dependant → setup.sh or Install Guide

**Port to**:
- Machine-specific setup → `/setup.sh` or `SETUP.md`
- OS-specific context → AGENTS.md with setup notes
- Tool-specific config → config.toml or `.codex/setup/`

**How to Port**:
```bash
# Create setup documentation
cat << 'EOF' > SETUP.md
# Setup Instructions

## Prerequisites

[From .0agnostic/07+_setup_dependant/]

## Installation

[Setup steps]

## Configuration

[config.toml setup]
EOF
```

---

<!-- section_id: "d2b8a87e-3b7f-4051-9dee-67d3b8a2f75b" -->
## Part 3: Detailed Porting Examples

<!-- section_id: "fb16cfee-7a1d-4353-8d1e-4303821d9aa7" -->
### Example 1: Knowledge Porting

**Original** (Claude Code):
```markdown
# CLAUDE.md

## Resources

| Resource | Location | Purpose |
|----------|----------|---------|
| Canvas Integration | .0agnostic/01_knowledge/canvas_integration/ | Canvas MCP patterns |

# MEMORY.md (first 200 lines)

## Canvas MCP Patterns

[knowledge about Canvas...]
```

**Ported to Codex**:
```markdown
# AGENTS.md

## Resources

| Resource | Location | Purpose |
|----------|----------|---------|
| Canvas Integration | /docs/canvas/ | Canvas MCP patterns |

## Canvas Integration

[Inline summary of key patterns]
See /docs/canvas/ for full reference.
```

```bash
# /docs/canvas/README.md
Canvas MCP Integration

## Available Tools

- canvas_assignment_list(course_id)
- canvas_get_my_submission(course_id, assignment_id)
...
```

<!-- section_id: "57ce1a68-360a-4dc2-b79b-1051b81aca26" -->
### Example 2: Rules Porting

**Original** (Claude Code):
```markdown
# 0AGNOSTIC.md

# ── Current Status ──

## Triggers

| Trigger Condition | Action | Rule |
|-------------------|--------|------|
| User asks about grades | Load dashboard skill | grade_strategy_triggers.md |

# DYNAMIC CONTEXT

# ── References ──

## Rules

| Rule | Path | Purpose |
|------|------|---------|
| Grade Strategy Triggers | .0agnostic/02_rules/dynamic/ | When to load grade context |
```

**Ported to Codex**:
```markdown
# AGENTS.md

## [CRITICAL] Rules

[List most important rules from static rules]

## Dynamic Rules

| Trigger | Action |
|---------|--------|
| User asks about grades | Consider loading grade_strategy context |
| Modifying AGENTS.md | Update config.toml settings too |

## Related Documentation

See /docs/rules/ for detailed rule explanations
```

<!-- section_id: "0c41b823-3bd2-427e-ac60-9be13192da0e" -->
### Example 3: Protocol Porting

**Original** (Claude Code):
```
.0agnostic/03_protocols/
├── grade_strategy_system/
│   ├── canvas_grade_dashboard_trajectory.md  [7-step workflow]
│   └── grading_model_analysis_trajectory.md  [How to analyze grading]
```

**Ported to Codex**:
```bash
# Create /docs/procedures/
mkdir -p /docs/procedures/grade_strategy

# Copy the step-by-step content
cp .0agnostic/03_protocols/grade_strategy_system/canvas_grade_dashboard_trajectory.md \
   /docs/procedures/grade_strategy/dashboard.md

# Reference in AGENTS.md
```

```markdown
# AGENTS.md

## Grade Strategy Context

When user asks about grades:

1. Read /docs/procedures/grade_strategy/dashboard.md
2. Fetch Canvas data via Canvas MCP
3. Compute total score and percentage
4. Generate dashboard markdown

See /docs/procedures/ for detailed procedures.
```

<!-- section_id: "8f4055e0-bbfa-43d1-b511-6142442d9daa" -->
### Example 4: Skills Porting

**Original** (Claude Code):
```
.0agnostic/06_context_avenue_web/01_file_based/05_skills/
├── canvas-fetch/SKILL.md  [Generic Canvas data fetcher]
└── grade-calculator/SKILL.md  [Rubric-agnostic scoring]
```

**Ported to Codex**:

**Option A** (As MCP Server):
```bash
# If these are reusable across projects, create MCP server
# See .mcp_server/ or create custom MCP

# Example: canvas-fetch becomes Canvas MCP tool
# (already built into Codex, no porting needed)
```

**Option B** (As Procedures):
```bash
# Or document as procedures in /docs/

mkdir -p /docs/procedures/canvas

cat << 'EOF' > /docs/procedures/canvas/fetch_data.md
# Canvas Data Fetching Procedure

## Prerequisites

- Canvas course ID

## Steps

1. Call canvas_assignment_list(course_id)
2. Call canvas_get_my_submission(course_id, assignment_id) for each
3. Aggregate results
4. Return structured data

## Example

[Example with actual data]
EOF
```

**Option C** (Reference in AGENTS.md):
```markdown
# AGENTS.md

## Canvas Integration Skills

### Fetch Canvas Data

**When to use**: Need to get grades, assignments, or submission data

**Steps**:
1. [step 1]
2. [step 2]

See Canvas MCP reference: [link]
```

---

<!-- section_id: "20c60896-8faa-4892-adf2-4471c8099158" -->
## Part 4: Practical Porting Workflow

<!-- section_id: "c33b1587-f986-4092-aa2a-6ef0427aef45" -->
### Step 1: Read Source Files

```bash
# Examine your 0AGNOSTIC.md structure
head -100 0AGNOSTIC.md

# Check .0agnostic/ contents
find .0agnostic/ -name "*.md" | head -20
```

<!-- section_id: "f8f4fb35-4ef6-4e8d-b399-8013d7799b6b" -->
### Step 2: Create Directory Structure

```bash
# Create Codex directories
mkdir -p ~/.codex/
mkdir -p [project]/docs/
mkdir -p [project]/docs/procedures/
mkdir -p [project]/knowledge/
mkdir -p [project]/templates/
```

<!-- section_id: "918c1d3e-d038-4d5d-9f73-5373f87b881a" -->
### Step 3: Port 0AGNOSTIC.md

```bash
# Create global AGENTS.md
cat > ~/.codex/AGENTS.md << 'EOF'
# Global Codex Instructions

[From 0AGNOSTIC.md STATIC context, global parts]
EOF

# Create project AGENTS.md
cat > [project]/AGENTS.md << 'EOF'
# [Project] — Codex Instructions

[From 0AGNOSTIC.md STATIC context, project parts]
[From config.toml if exists]
EOF
```

<!-- section_id: "1c54ff26-cc27-44ab-805d-6f359de9cf46" -->
### Step 4: Port Knowledge (.0agnostic/01_knowledge/)

```bash
# Copy docs
cp -r .0agnostic/01_knowledge/docs/*.md [project]/docs/

# Create knowledge index
cat > [project]/docs/INDEX.md << 'EOF'
# Knowledge Index

[List all docs with brief descriptions]
EOF
```

<!-- section_id: "940b5c40-360a-422a-bd74-9cb445fd7fab" -->
### Step 5: Port Rules (.0agnostic/02_rules/)

```bash
# Extract static rules into AGENTS.md
grep -A 20 "# ── Current Status ──" 0AGNOSTIC.md >> [project]/AGENTS.md

# Copy dynamic rules to /docs/rules/
mkdir -p [project]/docs/rules/
cp .0agnostic/02_rules/dynamic/*/*.md [project]/docs/rules/
```

<!-- section_id: "651e81e4-c8f3-4043-9721-f02b2f540961" -->
### Step 6: Port Protocols (.0agnostic/03_protocols/)

```bash
# Copy all protocols
mkdir -p [project]/docs/procedures/
cp -r .0agnostic/03_protocols/* [project]/docs/procedures/

# Create procedures index
cat > [project]/docs/procedures/INDEX.md << 'EOF'
# Procedures Index

[List procedures]
EOF
```

<!-- section_id: "56f61869-96fa-4a62-9a87-307ee3493c91" -->
### Step 7: Create config.toml

```bash
cat > [project]/config.toml << 'EOF'
[default]
model = "codex-sonnet"
temperature = 0.7
max_tokens = 4096
reasoning_effort = "medium"
context_window = "128k"
session_persistence = true
EOF
```

<!-- section_id: "4b6ea0a7-2793-4cf8-a6fc-947bf6f3ba44" -->
### Step 8: Update AGENTS.md with Resources Table

```bash
cat >> [project]/AGENTS.md << 'EOF'

## Resources

| Type | Path | Purpose |
|------|------|---------|
| Architecture | /docs/architecture.md | Design decisions |
| Procedures | /docs/procedures/ | Step-by-step guides |
| Knowledge | /docs/ | Domain knowledge |
| Templates | /templates/ | Scaffolding files |
EOF
```

<!-- section_id: "cbef3b2e-95cf-4765-b0b2-911aecf59ac3" -->
### Step 9: Verify Structure

```bash
# Check AGENTS.md exists at all levels
find [project] -name "AGENTS.md" -type f

# Check key resources exist
ls [project]/docs/
ls [project]/docs/procedures/
```

<!-- section_id: "c7401b4f-1c7a-467d-9357-51e75d59704c" -->
### Step 10: Test Codex

```bash
cd [project]
codex
# Test that context loads correctly
```

---

<!-- section_id: "e4b2a3a3-9f88-469f-ad6c-0503d1db1320" -->
## Part 5: Migration Checklist

Complete each item to ensure proper porting:

- [ ] **Create ~/.codex/AGENTS.md** (global instructions)
- [ ] **Create [project]/AGENTS.md** (project instructions)
- [ ] **Create [project]/config.toml** (model and settings)
- [ ] **Copy /docs/** (all knowledge docs from .0agnostic/01_knowledge/)
- [ ] **Copy /docs/rules/** (dynamic rules from .0agnostic/02_rules/dynamic/)
- [ ] **Copy /docs/procedures/** (all procedures from .0agnostic/03_protocols/)
- [ ] **Create /templates/** (copy from .0agnostic/01_knowledge/resources/templates/)
- [ ] **Update AGENTS.md Resources table** (point to all docs)
- [ ] **Test Codex context loading** (`codex context` to verify)
- [ ] **Verify no critical content lost** (read key procedures, ensure they migrated)
- [ ] **Adjust config.toml** (set model/reasoning_effort for your project)
- [ ] **Create README.md** (explain project structure, key files)

---

<!-- section_id: "7ed0ad02-65d3-4076-b2d6-a5090ea53982" -->
## Part 6: Trade-offs & Limitations

<!-- section_id: "8aff1d3d-ac23-44b2-9930-3bcbfca2cd4d" -->
### What Ports Cleanly ✅

These things port from our 0AGNOSTIC.md system to Codex without issue:

- **Static rules** → AGENTS.md (direct copy)
- **Knowledge docs** → /docs/ (direct copy)
- **Procedures** → /docs/procedures/ (direct copy, no changes needed)
- **Protocols** → /docs/procedures/ (step-by-step guides work as-is)
- **Model settings** → config.toml (direct mapping)
- **Current status** → AGENTS.md Current Status (one-liner)

<!-- section_id: "7fffe5ec-b7bb-4854-a2f6-6783965bf2b6" -->
### What Requires Adaptation ⚠️

These things need modification when porting:

- **MEMORY.md** → No direct equivalent. Instead:
  - Use Codex session persistence (`codex resume`)
  - Put important info in AGENTS.md Current Status
  - Keep procedural memory in /docs/procedures/

- **@file/@folder references** → No equivalent in Codex. Instead:
  - Mention file paths in prompts ("read /docs/architecture.md")
  - Use markdown file structure (/docs/ hierarchy is searchable)
  - Reference README and INDEX files

- **Auto-compaction** → No equivalent. Instead:
  - Manage session cleanup manually (`codex list-sessions`, archive old)
  - Keep AGENTS.md files concise (target <500 lines)
  - Monitor token usage (`codex context`)

- **Skills** → Codex uses MCP servers instead. Instead:
  - Complex workflows → /docs/procedures/ (documented steps)
  - Tool integration → MCP servers (Canvas, GitHub, etc.)
  - Tool-specific skills → Inline in AGENTS.md (brief summaries)

<!-- section_id: "5bba6f6f-267a-44f2-80eb-4b41f7ea2a02" -->
### What Stays as Reference 📚

These don't directly port — keep as reference documentation:

- **AALang agent definitions** (.gab.jsonld files)
  - Port to: /docs/agent_patterns.md (describe the pattern)
  - Codex doesn't execute AALang, but you can document patterns

- **Data-based avenues** (.0agnostic/06_context_avenue_web/02_data_based/)
  - Port to: Documentation of vector embeddings, knowledge graphs
  - Codex doesn't generate these, but you can reference them

- **Episodic memory** (.0agnostic/04_episodic_memory/)
  - Port to: Session management strategy in AGENTS.md
  - Codex has built-in session history, no need to migrate

<!-- section_id: "e083e898-1e5d-44c3-ac81-2e7449599b63" -->
### What's NOT Supported 🚫

These things don't have equivalents in Codex:

- **Multi-agent coordination** (multiple AI agents working together)
  - Workaround: Document patterns in /docs/, manually coordinate
  - Codex is single-user, single-agent (you don't spawn subagents)

- **Hierarchical entity structure** (layer 0 → layer 1 → layer 2...)
  - Workaround: Document hierarchy in README + /docs/
  - Codex is flat (one workspace), not nested

- **.1merge system** (tool-specific overrides)
  - Workaround: Use config.toml for simple overrides
  - No .1merge equivalent in Codex

---

<!-- section_id: "bc8af9b4-9407-4548-8b58-14f2bb9433f5" -->
## Part 7: Validation

<!-- section_id: "6127f9dc-8550-44a9-bc2b-c2685346b518" -->
### After Porting, Verify

#### Test 1: AGENTS.md Loads Correctly

```bash
cd [project]
codex
# Check that context includes AGENTS.md content
# You should see references to your instructions
```

#### Test 2: Resources Are Accessible

```bash
# Verify all docs exist and are readable
cat docs/architecture.md
cat docs/procedures/INDEX.md

# Verify referenced files can be mentioned in prompts
```

#### Test 3: config.toml Is Applied

```bash
# Check model setting
codex status  # Should show correct model

# Ask Codex to use reasoning
# Should take appropriate time for reasoning_effort level
```

#### Test 4: No Critical Content Lost

```bash
# Spot-check key procedures
grep -r "7-step workflow" docs/procedures/  # Should find procedure

# Verify important rules are in AGENTS.md
grep -r "\[CRITICAL\]" [project]/AGENTS.md  # Should find rules
```

<!-- section_id: "d7b37461-9056-4fd4-885e-ec10af207961" -->
### Checklist for Successful Port

- [ ] AGENTS.md includes all [CRITICAL] rules
- [ ] config.toml has correct model and reasoning_effort
- [ ] /docs/ contains all important knowledge
- [ ] /docs/procedures/ contains all step-by-step guides
- [ ] Resources table in AGENTS.md points to actual files
- [ ] Codex loads context correctly (no errors)
- [ ] Can reference /docs/ files in prompts
- [ ] Session history works (`codex resume` brings back context)

---

<!-- section_id: "540cb023-3dc3-40f6-9a3d-016f44159fa9" -->
## Summary

**Porting our 0AGNOSTIC.md system to Codex** requires mapping three things:

1. **0AGNOSTIC.md file** → Split into:
   - AGENTS.md (three-level: global, project, directory)
   - config.toml (model, reasoning_effort, max_tokens)
   - /docs/, /knowledge/, /templates/ (external files)

2. **.0agnostic/ directories** → Port to:
   - 01_knowledge/ → /docs/ + config.toml settings
   - 02_rules/ → AGENTS.md + /docs/rules/
   - 03_protocols/ → /docs/procedures/
   - 04_episodic/ → (use Codex sessions instead)
   - 05_handoff/ → (keep in README/project docs)
   - 06_avenue_web/ → (document patterns, don't execute)
   - 07+ setup/ → SETUP.md or config notes

3. **Session management** → Replace with:
   - Codex `codex resume [session-id]` instead of MEMORY.md
   - Concise AGENTS.md Current Status
   - /docs/procedures/ for procedural memory

**Result**: A functioning Codex workspace with all the context and procedures from your layer-stage system, adapted to Codex's native architecture.

