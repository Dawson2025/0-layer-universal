# Cursor IDE — Porting Strategy for 0AGNOSTIC.md and .0agnostic/ System

**Date**: 2026-02-27
**Focus**: How to port both the 0AGNOSTIC.md file AND .0agnostic/ directory structure into Cursor IDE's native system

---

## Overview

Porting to Cursor IDE means mapping two things:

1. **0AGNOSTIC.md file** (identity, triggers, resources) → Cursor's **.cursor/rules** files (YAML-based context)
2. **.0agnostic/ directory** (rules, knowledge, protocols, skills) → Cursor's **Memory Bank** + **hooks.json** + **project configuration**

Cursor IDE has no direct `.0agnostic/` equivalent — you implement these patterns using .cursor/rules files and the Memory Bank system.

---

## Part 1: Porting 0AGNOSTIC.md → .cursor/rules Files

### Step 1: Extract STATIC Context

Read the STATIC section of your 0AGNOSTIC.md:

```markdown
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──
## Identity
[Your identity: role, scope, parent, children]

## Key Behaviors
[What you DO and DON'T DO]

## Triggers
[When this context applies]

# ── Current Status ──
## Current Status
[Phase, key findings]
```

### Step 2: Create .cursor/rules Files

The STATIC section becomes one or more **YAML rule files**:

**Structure**:
```
project/.cursor/rules/
├── identity.md          # Your role and scope
├── key-behaviors.md     # What you do/don't do
├── conventions.md       # Code style, naming, patterns
├── architecture.md      # Technical stack, design patterns
└── current-status.md    # Phase, known issues, readiness
```

### Step 3: Rule File Format

Each file uses YAML frontmatter + markdown:

```yaml
---
mode: "Always Apply"          # How to apply: Always Apply | Intelligently | Specific Files | Manual
description: "Project identity and role definition"
glob: "**/*"                  # File pattern this applies to (optional)
---

# Identity

You are an expert [domain] developer.

## Role
[Your role from 0AGNOSTIC.md]

## Scope
[What you can and should do]

## Parent Context
[Reference to parent entity]

## Current Status
[Phase, key findings, what's ready]

## Key Behaviors

### DO:
- [Behavior 1]
- [Behavior 2]

### DON'T:
- [Behavior 3]
- [Behavior 4]
```

### Example: Identity Rule File

**From 0AGNOSTIC.md (STATIC)**:
```markdown
## Identity

You are an expert Python data analyst.
- **Role**: Build and optimize data processing pipelines
- **Scope**: Python, pandas, numpy, data ETL, performance optimization
- **Parent**: data_systems entity
- **Children**: None

## Key Behaviors

### What You DO
- Optimize pandas operations for large datasets
- Suggest efficient algorithms
- Include type hints consistently

### What You DON'T DO
- Use data unsafely (SQL injection patterns)
- Ignore performance implications
```

**To .cursor/rules/identity.md**:
```yaml
---
mode: "Always Apply"
description: "Data analyst role and identity"
---

# Data Analyst Identity

You are an expert Python data analyst specializing in high-performance data processing.

## Role
Build and optimize data processing pipelines. Provide clear explanations for architectural decisions.

## Scope
- Python 3.8+
- pandas, numpy, dask for data manipulation
- Performance optimization and profiling
- ETL pipeline design

You do NOT handle business logic outside data processing or manage infrastructure.

## Current Status
- Phase: Active data analysis work
- Key dataset: 500M rows, parquet format
- Optimizations in place: vectorized operations, chunked processing
- Known issues: string operations slower than expected

## Key Behaviors

### DO:
- Optimize pandas operations using vectorization
- Profile performance before and after changes
- Use type hints (mypy compatible)
- Include docstrings with example usage
- Test on realistic data sizes
- Document trade-offs clearly

### DON'T:
- Use data unsafely (no SQL injection-like patterns)
- Ignore performance implications
- Over-engineer simple operations
- Skip documentation
```

### Step 4: Create Triggers Rules

Map 0AGNOSTIC.md TRIGGERS to rule application:

**From 0AGNOSTIC.md**:
```markdown
## Triggers

| Situation | Action |
|-----------|--------|
| User asks about data | Load dashboard skill |
| Working with pandas | Load optimization protocol |
| Debugging performance | Load profiling knowledge |
```

**To .cursor/rules/triggers.md**:
```yaml
---
mode: "Intelligently"
description: "Context-specific rule triggers"
---

# Dynamic Triggers

## When to Load Dashboard Context
- User asks: "how am I doing", "grade", "progress"
- Load memory: "Dashboard implementation patterns"
- Action: Use dashboard skill

## When to Load Optimization Context
- File path: "pandas", "dataframe"
- User asks: "optimize", "performance", "speed"
- Action: Apply optimization patterns

## When to Load Debugging Context
- User asks: "slow", "bottleneck", "profile"
- File: Any Python script with pandas
- Action: Suggest profiling approach
```

---

## Part 2: Porting .0agnostic/ Directory → Memory Bank + Configuration

The `.0agnostic/` directory doesn't map directly to Cursor. Implement these patterns:

### Mapping .0agnostic/ Directories

| .0agnostic/ Directory | Cursor Port | Implementation |
|----------------------|-----------|-----------------|
| `01_knowledge/` | Memory Bank entries | Create memories for each topic |
| `02_rules/static/` | .cursor/rules YAML files | Rules files for enforcement |
| `02_rules/dynamic/` | .cursor/rules (Intelligently mode) | Conditional rules |
| `03_protocols/` | Memory Bank (reference) | Document step-by-step procedures |
| `04_episodic_memory/` | Memory Bank (sessions) | Session notes and progress |
| `05_handoff_documents/` | Memory Bank (project context) | Incoming context from managers |
| `06_context_avenue_web/skills/` | Reusable code snippets in Memory Bank | Code templates and patterns |
| `07+_setup_dependant/` | .cursor/mcp.json + project config | Tool configuration |

### Detailed Implementation

#### 01_knowledge/ → Memory Bank Entries

**From .0agnostic/01_knowledge/**:
```
01_knowledge/
├── principles/
│   ├── principle_1_performance.md
│   └── principle_2_clarity.md
├── docs/
│   └── optimization_patterns.md
└── resources/
    └── templates/
        └── pipeline_template.py
```

**To Memory Bank** (Create memories):

Memory 1 — "Performance & Clarity Principles":
```markdown
# Data Pipeline Principles

## Principle 1: Performance First
Optimize for user experience. Measure before optimizing.

## Principle 2: Code Clarity
All code must be readable. Prefer clear variable names over clever one-liners.

## Pattern: Vectorized Operations
Use pandas vectorization instead of loops.

```python
# Bad: Loop
for idx, row in df.iterrows():
    df.loc[idx, 'new_col'] = row['a'] + row['b']

# Good: Vectorized
df['new_col'] = df['a'] + df['b']
```
```

#### 02_rules/static/ → .cursor/rules Files

**From .0agnostic/02_rules/static/**:
```
02_rules/static/
├── data_validation.md
│   "All inputs must be validated"
└── error_handling.md
    "All API calls must include retry logic"
```

**To .cursor/rules/enforcement.md**:
```yaml
---
mode: "Always Apply"
description: "Static enforcement rules"
---

# Enforcement Rules

## Rule 1: Data Validation
All inputs must be validated before processing.

```python
# Template
def process(self, data):
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input must be DataFrame")
    if data.empty:
        raise ValueError("Input cannot be empty")
    # ... process
```

## Rule 2: Error Handling
All external API calls must include retry logic.

```python
# Template
@retry(max_attempts=3, backoff_factor=2)
def call_api(endpoint):
    response = requests.get(endpoint, timeout=10)
    response.raise_for_status()
    return response.json()
```
```

#### 03_protocols/ → Memory Bank Reference

**From .0agnostic/03_protocols/data_processing_protocol.md**:
```markdown
# Data Processing Protocol

## Step 1: Validate Input
- Check type is DataFrame
- Check no null values in key columns

## Step 2: Transform
- Apply business logic
- Log transformations

## Step 3: Validate Output
- Check shape as expected
- Check no data loss
```

**To Memory Bank** — "Data Processing Protocol":
```markdown
# Data Processing Protocol (Reference)

See: .0agnostic/03_protocols/data_processing_protocol.md

## Quick Reference
1. Validate input (type, nulls, required columns)
2. Transform (apply logic, log steps)
3. Validate output (shape, data loss check)

When implementing, reference full protocol for details.
```

#### 04_episodic_memory/ → Memory Bank Sessions

**From .0agnostic/04_episodic_memory/sessions/**:
```
sessions/
├── 2026-02-26-session-1.md
│   "Optimized query performance by 50%"
└── 2026-02-27-session-2.md
    "Refactored data pipeline to use vectorization"
```

**To Memory Bank** — Create per-session memories:

Session Memory: "2026-02-27: Pipeline Refactoring"
```markdown
# Session 2026-02-27: Pipeline Refactoring

## What was accomplished
- Refactored 15 data pipelines to use vectorized operations
- Reduced processing time from 45s to 12s (73% faster)
- All tests passing

## What we learned
- String operations are the bottleneck (need optimization)
- Vectorization works for numeric operations only
- Memory usage reduced significantly

## Next steps
- Optimize string operations in pipeline
- Add profiling to identify future bottlenecks
- Update performance guidelines document
```

#### 05_handoff_documents/ → Memory Bank Project Context

**From .0agnostic/05_handoff_documents/01_incoming/01_from_above/**:
```
01_from_above/
└── context.md
    "Project context from manager"
```

**To Memory Bank** — "Project Context from Manager":
```markdown
# Project Context (From Manager)

[Content from incoming handoff document]

This memory provides context from the parent level about project goals, constraints, and current focus.
```

#### 06_context_avenue_web/skills/ → Code Snippets in Memory Bank

**From .0agnostic/06_context_avenue_web/05_skills/optimization/**:
```markdown
# Optimization Skill

Use when: Performance is slow
Pattern: Profile → Identify bottleneck → Optimize → Verify
```

**To Memory Bank** — "Optimization Patterns & Code":
```markdown
# Optimization Workflow

## Pattern: Identify & Fix
1. Profile current code
2. Find bottleneck
3. Optimize that specific part
4. Verify with benchmarks

## Common Optimizations

### Vectorization (pandas)
```python
# Before: Loop (slow)
for idx, row in df.iterrows():
    df.loc[idx, 'result'] = process_row(row)

# After: Vectorized (fast)
df['result'] = df.apply(lambda row: process_row(row), axis=1)
# Or better: Use built-in operations
df['result'] = df['a'] + df['b']  # if just arithmetic
```
```

#### 07+_setup_dependant/ → .cursor/mcp.json + Project Config

**From .0agnostic/07+_setup_dependant/cursor_config.json**:
```json
{
    "mcp_servers": {
        "tavily": {
            "enabled": true,
            "credentials": "env:TAVILY_API_KEY"
        }
    },
    "workspace": {
        "session_auto_save": true
    }
}
```

**To .cursor/mcp.json**:
```json
{
  "mcpServers": {
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

**To .cursor/hooks.json** (automation):
```json
{
  "hooks": {
    "pre-save": [
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
        "command": "pytest ${file}",
        "glob": "tests/**/*.py",
        "description": "Run tests for changed test files"
      }
    ]
  }
}
```

---

## Part 3: Complete Integration Example

### Directory Structure

```
project/
├── .cursor/
│   ├── rules/
│   │   ├── identity.md
│   │   ├── key-behaviors.md
│   │   ├── conventions.md
│   │   ├── architecture.md
│   │   └── triggers.md
│   ├── mcp.json
│   └── hooks.json
├── .cursorignore
├── src/
│   └── pipelines/
│       └── main.py
└── tests/
    └── test_pipelines.py
```

### Memory Bank Organization

```
Memory Bank:
├── Project Context (from manager/parent)
├── Identity & Role
├── Principles & Conventions
├── Protocol References
├── Code Patterns & Snippets
├── Session Notes (2026-02-27: ...)
└── Known Issues & Gotchas
```

### Cursor IDE Workflow

```
1. User opens project in Cursor IDE

2. Cursor loads:
   - All .cursor/rules/ YAML files
   - Memory Bank entries
   - .cursor/mcp.json configuration
   - .cursor/hooks.json hooks

3. User types in chat:
   "How should I optimize this query?"

4. Cursor applies:
   - identity.md (understanding your role)
   - key-behaviors.md (following your patterns)
   - conventions.md (coding style)
   - Relevant memory entries (optimization patterns)

5. Cursor generates response:
   - Following your principles
   - Using your conventions
   - Referencing your documented patterns
   - Respecting your scope

6. User requests optimization:
   - Cursor suggests pattern from "Optimization Patterns & Code" memory
   - Applies to specific code
   - Pre-save hook runs: black --quiet (formats)
   - Post-save hook runs: pytest (tests)
   - Changes verified automatically
```

---

## Part 4: Migration Checklist

- [ ] Extract STATIC section from 0AGNOSTIC.md
- [ ] Create `.cursor/rules/identity.md` with role/scope
- [ ] Create `.cursor/rules/key-behaviors.md` with DO/DON'T
- [ ] Create `.cursor/rules/conventions.md` with code style
- [ ] Create `.cursor/rules/architecture.md` with tech stack
- [ ] Create `.cursor/rules/current-status.md` with phase/readiness
- [ ] Create `.cursor/rules/triggers.md` with dynamic rules
- [ ] Create Memory Bank entry: "Project Context" (from parent)
- [ ] Create Memory Bank entry: "Principles & Conventions"
- [ ] Create Memory Bank entry: "Code Patterns & Snippets"
- [ ] Create `.cursor/mcp.json` with tool configuration
- [ ] Create `.cursor/hooks.json` with automation rules
- [ ] Test rule loading (verify rules appear in chat)
- [ ] Test Memory Bank (verify memories are referenced)
- [ ] Test hooks (verify pre-save/post-save work)
- [ ] Test MCP servers (verify tools are available)
- [ ] Create `.cursorignore` (exclude unneeded files)
- [ ] Document your Cursor workflow (chat-first, code-first, etc.)

---

## Part 5: Best Practices

### Rule Organization

**Global Rules** (`~/.cursor/rules/`):
- Code style and naming conventions
- Universal security rules
- Testing approach

**Project Rules** (`project/.cursor/rules/`):
- Project-specific patterns
- Tech stack conventions
- Architecture decisions

**Component Rules** (`project/src/component/.cursor/rules/`):
- Component-specific constraints
- API contracts
- Specialized patterns

### Memory Bank Strategy

**What to Remember**:
- Principles and key decisions
- Code patterns and templates
- Protocol references
- Session summaries
- Known issues and gotchas

**What NOT to Remember**:
- Every conversation (only important sessions)
- Code you've already written (reference by file path)
- General knowledge (keep rule files for that)

### Hook Strategy

Use hooks for automation, not enforcement:
- Auto-format code (black, prettier)
- Run tests on file change
- Generate documentation
- Check for common mistakes

Don't overload hooks (slow IDE if too many).

---

## Summary

Porting to Cursor IDE requires:

1. **0AGNOSTIC.md STATIC** → `.cursor/rules/` YAML files (what Cursor sees)
2. **0AGNOSTIC.md DYNAMIC** → Memory Bank + Configuration (what you control)
3. **02_rules/static/** → `.cursor/rules/` enforcement files
4. **02_rules/dynamic/** → `.cursor/rules/` (Intelligently mode)
5. **03_protocols/** → Memory Bank references
6. **04_episodic_memory/** → Memory Bank session entries
7. **05_handoff_documents/** → Memory Bank project context
8. **06_skills/** → Memory Bank code patterns
9. **07+_setup_dependant/** → `.cursor/mcp.json` + hooks

All patterns are **reversible** — Cursor's native mechanisms support this structure, and you can iterate as you learn what works best.

