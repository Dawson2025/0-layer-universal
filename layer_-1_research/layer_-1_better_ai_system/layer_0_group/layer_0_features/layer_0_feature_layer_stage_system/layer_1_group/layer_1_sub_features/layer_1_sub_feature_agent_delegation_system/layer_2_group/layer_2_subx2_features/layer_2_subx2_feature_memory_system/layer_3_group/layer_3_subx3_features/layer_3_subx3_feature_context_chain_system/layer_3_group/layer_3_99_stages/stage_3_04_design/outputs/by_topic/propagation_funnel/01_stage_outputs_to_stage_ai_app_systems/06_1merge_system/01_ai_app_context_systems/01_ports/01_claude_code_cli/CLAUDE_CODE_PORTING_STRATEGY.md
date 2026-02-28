# Claude Code — Porting Strategy from 0AGNOSTIC.md

**Date Created**: 2026-02-27
**Status**: Strategy Complete (Claude Code is native to 0AGNOSTIC.md system)

---

## Overview

Claude Code's context system **was designed around the 0AGNOSTIC.md model**. Porting from 0AGNOSTIC.md to Claude Code means the system is already aligned — no translation needed. However, this document covers:

1. **Validation**: Ensuring 0AGNOSTIC.md is properly structured for Claude Code
2. **Propagation**: How to cascade context through the layer-stage hierarchy
3. **Optimization**: Best practices for token efficiency and context loading
4. **Extension**: Adding new context elements (rules, skills, knowledge)

---

## Part 1: Validation Checklist

### 1.1 0AGNOSTIC.md Structure Validation

**Required Elements** (Claude Code expects all of these):

```markdown
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──
## Identity
- Role description
- Scope
- Parent (if not root)
- Children (if any)

## Key Behaviors
- Core workflows
- Primary responsibilities

## Triggers
- When to load this context
- Conditions for activation

# ── Current Status ──
- Phase, last updated, brief summary

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──
- Detailed state information

# ── References ──
- Navigation links
- Resource pointers
```

**Validation Script**:

```bash
# Check for required markers
grep -q "# ═══ STATIC CONTEXT" 0AGNOSTIC.md || echo "ERROR: Missing STATIC marker"
grep -q "# ═══ DYNAMIC CONTEXT" 0AGNOSTIC.md || echo "ERROR: Missing DYNAMIC marker"
grep -q "# ── Entity Definition" 0AGNOSTIC.md || echo "ERROR: Missing Entity Definition"
grep -q "# ── Current Status" 0AGNOSTIC.md || echo "ERROR: Missing Current Status"

# Check for Critical sections in STATIC
grep -A50 "# ── Entity Definition" 0AGNOSTIC.md | grep -q "## Identity" || echo "WARN: No Identity section"
grep -A50 "# ── Entity Definition" 0AGNOSTIC.md | grep -q "## Key Behaviors" || echo "WARN: No Key Behaviors"
grep -A50 "# ── Entity Definition" 0AGNOSTIC.md | grep -q "## Triggers" || echo "WARN: No Triggers section"

# Check Current Status substantiveness (not just one line)
current_status_lines=$(grep -A10 "# ── Current Status" 0AGNOSTIC.md | grep -v "^#" | wc -l)
[ $current_status_lines -lt 3 ] && echo "WARN: Current Status too brief (< 3 lines)"
```

### 1.2 .0agnostic/ Directory Validation

**Required Directories**:

```
.0agnostic/
├── 01_knowledge/                    # Per-topic organization
├── 02_rules/
│   ├── static/                      # Always-on rules
│   └── dynamic/                     # Conditional rules
├── 03_protocols/                    # Procedural workflows
├── 04_episodic_memory/
│   ├── sessions/
│   └── changes/
├── 05_handoff_documents/
│   ├── 01_incoming/
│   └── 02_outgoing/
├── 06_context_avenue_web/           # Multi-avenue context
│   ├── 00_context_avenue_web_registry/
│   ├── 01_file_based/
│   │   ├── 01_aalang/
│   │   ├── 02_aalang_markdown_integration/
│   │   ├── 03_auto_memory/
│   │   ├── 04_@import_references/
│   │   ├── 05_skills/
│   │   ├── 06_agents/
│   │   ├── 07_path_specific_rules/
│   │   └── 08_hooks/
│   └── 02_data_based/
└── 07+_setup_dependant/
```

**Validation**:

```bash
# Check if .0agnostic structure exists
for dir in 01_knowledge 02_rules 03_protocols 04_episodic_memory 05_handoff_documents 06_context_avenue_web 07+_setup_dependant; do
  [ -d ".0agnostic/$dir" ] || echo "MISSING: .0agnostic/$dir"
done

# Check 02_rules subdivisions
[ -d ".0agnostic/02_rules/static" ] || echo "MISSING: .0agnostic/02_rules/static"
[ -d ".0agnostic/02_rules/dynamic" ] || echo "MISSING: .0agnostic/02_rules/dynamic"

# Check 06_context_avenue_web structure
for subdir in 01_file_based 02_data_based; do
  [ -d ".0agnostic/06_context_avenue_web/$subdir" ] || echo "MISSING: avenue $subdir"
done
```

---

## Part 2: Propagation Strategy

### 2.1 Hierarchical Context Cascading

Claude Code loads context in this order (highest to lowest priority):

```
1. User-level ~/.0agnostic/ (most general)
   ↓
2. Root-level layer_0/.0agnostic/ (universal to all projects)
   ↓
3. Project-level layer_1/.0agnostic/ (project scope)
   ↓
4. Entity-level layer_2+/.0agnostic/ (entity scope)
   ↓
5. Stage-level layer_N/99_stages/stage_NN/.0agnostic/ (stage scope)
```

**Principle**: Lower levels inherit and can override higher levels.

**Example Propagation** (School Project):

```
~/.0agnostic/                              (User defaults, skills, rules)
  ↓
layer_0_universal/.0agnostic/              (Universal skills, protocols, knowledge)
  ↓
layer_1_project_school/.0agnostic/         (School project context)
  ↓
layer_2_sub_project_classes/.0agnostic/    (Universal class grading strategies)
  ↓
layer_4_subx3_project_cse300/.0agnostic/   (CSE 300 specific)
  ↓
layer_4_99_stages/stage_04_design/.0agnostic/ (Design phase specifics)
```

Each level adds refinement while preserving parent context.

### 2.2 Trigger-Based Loading

Triggers in 0AGNOSTIC.md determine which resources load on-demand.

**Trigger Table Format**:

```markdown
## Triggers

| Trigger Condition | Action | Context to Load | Skill to Invoke |
|-------------------|--------|-----------------|-----------------|
| User mentions keyword X | Load context Y | `.0agnostic/path/resource.md` | `/skill-name` |
```

**Execution Flow**:

1. User message arrives
2. Claude Code reads all STATIC sections (including Triggers table)
3. If user message matches a trigger condition:
   - Load referenced `.0agnostic/` resource
   - Invoke referenced skill
   - Execute workflow

**Example**:

```markdown
| User asks about grade status in [class] | Load dashboard workflow | `.0agnostic/03_protocols/grade_strategy_system/canvas_grade_dashboard_trajectory.md` | Class-specific dashboard skill |
```

When user says "How am I doing in CSE 300?":
1. Matches trigger: "asks about grade status in [class]"
2. Load trajectory from `.0agnostic/03_protocols/`
3. Invoke `/cse300-dashboard` skill
4. Execute 7-step workflow from trajectory

---

## Part 3: Optimization Strategies

### 3.1 Token Efficiency

Claude Code's default context window: **200,000 input tokens**

**Recommended allocation**:

```
Fixed overhead:
  - System prompt (Claude Code instructions): ~500 tokens
  - 0AGNOSTIC.md STATIC sections: ~2,000 tokens
  - Critical rules (I0_*): ~1,000 tokens
  ────────────────────────────
  Subtotal: ~3,500 tokens

Dynamic context (per request):
  - Triggers table (first 20 rows): ~500 tokens
  - Matched resources from .0agnostic/: variable (500-5,000)
  - Conversation history: variable (1,000-20,000)
  ────────────────────────────
  Subtotal: ~20,000 tokens (typical)

Available for task execution: ~175,000 tokens
```

**Optimization Tactics**:

1. **Keep STATIC sections lean** — Only include essential context that applies to EVERY request. Move details to DYNAMIC.
2. **Use @ imports** — Instead of embedding full knowledge in 0AGNOSTIC.md, use `@import_references/` to link to detailed files.
3. **Reference, don't embed** — Rather than pasting full skill code, reference it: "See `.claude/skills/skill-name/SKILL.md` for protocol."
4. **Compress cascading context** — If a child layer overrides parent context, prefer child-only in that layer's 0AGNOSTIC.md.
5. **Archive old context** — Move outdated information to `11_archives/` (not referenced by triggers).

### 3.2 Cascade Optimization Example

**Before** (inefficient — 8,000 STATIC tokens):

```markdown
# ── Entity Definition ──

## Identity
[Full description of entire entity family tree]

## Key Behaviors
1. [Behavior 1 with full explanation]
2. [Behavior 2 with full explanation]
... (40 behaviors listed)
```

**After** (efficient — 1,500 STATIC tokens):

```markdown
# ── Entity Definition ──

## Identity
[Concise role, scope, parent/children]

## Key Behaviors
Primary: [3 critical behaviors]
See `.0agnostic/01_knowledge/behaviors/` for full list.
```

---

## Part 4: Extension Framework

### 4.1 Adding New Rules

**When to add**:
- New constraint affecting ALL requests in scope (add to `.0agnostic/02_rules/static/`)
- Conditional rule (add to `.0agnostic/02_rules/dynamic/`)

**Process**:

1. Create rule file: `.0agnostic/02_rules/[static|dynamic]/RULE_NAME.md`
2. Include rule reference in 0AGNOSTIC.md under "Rules" section
3. Use importance prefix: `I0_` (critical), `I1_` (high), `I2_` (standard)
4. Document trigger condition if dynamic

**Example**:

```markdown
# New rule: I0_SECURITY_BOUNDARY.md

## What This Rule Governs
Interactions with external APIs and user data handling.

## When Triggered
Always (I0 prefix)

## Key Constraints
- MUST validate user input before API calls
- MUST NOT store sensitive data in context
```

Then add to 0AGNOSTIC.md:

```markdown
| Rule | Location | Importance | Purpose |
|------|----------|-----------|---------|
| Security Boundary | `.0agnostic/02_rules/static/I0_SECURITY_BOUNDARY.md` | I0 (Critical) | Data handling constraints |
```

### 4.2 Adding New Skills

**When to add**:
- Recurring workflow (automate with a skill)
- Tool integration needed (create skill wrapper)
- User needs quick access to complex operation (skill shorthand)

**Process**:

1. Create skill: `.claude/skills/skill-name/SKILL.md`
2. Include in 0AGNOSTIC.md under "Skills" section
3. Add trigger in Triggers table if context-dependent
4. Reference in relevant trajectories/protocols

**Example**:

```markdown
---
name: grade-dashboard
description: "Fetch live Canvas grade data and compute priority strategy."
---

# Grade Dashboard Skill

## WHEN to Use
- User asks about grade status
- User wants study recommendations

## Prerequisites
- Course ID provided
- Canvas MCP connected

## Steps
[Detailed workflow from trajectory]
```

### 4.3 Adding New Knowledge

**When to add**:
- Domain-specific information (principles, documentation, examples)
- Taxonomy or reference material
- Templates for future use

**Structure**:

```
.0agnostic/01_knowledge/[topic]/
├── principles/
│   └── core_principle_1.md
├── docs/
│   ├── reference_1.md
│   └── how_to_2.md
└── resources/
    ├── templates/
    │   └── template_1.md
    └── tools/
        └── utility_script.sh
```

**Example**:

```markdown
.0agnostic/01_knowledge/canvas_integration/
├── principles/
│   └── grading_models.md           # Specs vs percentage vs hybrid
├── docs/
│   ├── canvas_mcp_api.md           # API reference
│   └── assignment_types.md         # Canvas types
└── resources/
    └── templates/
        └── dashboard_template.md   # Copy-paste starter
```

---

## Part 5: Implementation Workflow

### 5.1 Creating a New Entity

When adding a new project/feature/class:

1. **Create structure** (use `/entity-creation` skill)
   ```bash
   /entity-creation
   ```

2. **Create `0AGNOSTIC.md`** (use template from `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md`)
   - Fill in Identity (role, scope, parent/children)
   - Document Key Behaviors
   - Add Triggers table
   - Add Current Status

3. **Create `.0agnostic/` subdirectories**
   ```bash
   mkdir -p .0agnostic/{01_knowledge,02_rules/{static,dynamic},03_protocols,04_episodic_memory/{sessions,changes},05_handoff_documents/{01_incoming,02_outgoing},06_context_avenue_web/01_file_based/{01_aalang,02_aalang_markdown_integration,03_auto_memory,04_@import_references,05_skills,06_agents,07_path_specific_rules,08_hooks},07+_setup_dependant}
   ```

4. **Add critical rules** (I0_* rules)
   - Copy from parent or reference parent rules

5. **Create skills** (if needed)
   - Reference in Triggers table
   - Store in `.claude/skills/`

6. **Generate tool files** (CLAUDE.md, AGENTS.md, etc.)
   ```bash
   bash ../.0agnostic/agnostic-sync.sh .
   ```

7. **Commit**
   ```bash
   git add .
   git commit -m "[AI Context] Create new entity with 0AGNOSTIC.md structure"
   git push
   ```

### 5.2 Updating Context at a Layer

1. **Identify change scope** (affects which layers?)
2. **Edit 0AGNOSTIC.md** in appropriate layer
3. **Run agnostic-sync.sh**
4. **Verify propagation** (check CLAUDE.md, AGENTS.md generated correctly)
5. **Test triggers** (confirm context loads when expected)
6. **Commit and push**

---

## Part 6: Comparison Table

| Aspect | 0AGNOSTIC.md | Claude Code Generated Files | Why Different |
|--------|-------------|---------------------------|----------------|
| **Source of Truth** | 0AGNOSTIC.md | ← (derived from 0AGNOSTIC.md) | CLAUDE.md is generated; edit 0AGNOSTIC.md |
| **Context Format** | Markdown with markers | Markdown (CLAUDE.md) + JSON (AGENTS.md, GEMINI.md) | Different tools need different formats |
| **Update Method** | Edit directly | Via `agnostic-sync.sh` | No direct edits to generated files |
| **Scope** | Single entity | Multiple entities (cascading) | Hierarchy enables context reuse |
| **Storage Location** | `0AGNOSTIC.md` | `.claude/`, `.cursor/`, `.gemini/`, `.github/` | Tool-specific directories |

---

## Part 7: Critical Rules for Claude Code Porting

### 7.1 The "No Direct CLAUDE.md Edits" Rule

**CRITICAL**: Never edit generated files directly. Always edit `0AGNOSTIC.md` first.

**Why**: Generated files sync with 0AGNOSTIC.md via `agnostic-sync.sh`. Direct edits get overwritten next sync.

**Workflow**:
1. Find what needs changing
2. Identify which 0AGNOSTIC.md it came from
3. Edit that 0AGNOSTIC.md
4. Run `agnostic-sync.sh`
5. Verify CLAUDE.md updated
6. Commit

### 7.2 The "Trigger Loading" Rule

**CRITICAL**: Resources in `.0agnostic/` are NOT automatically included in context.

They only load when:
- Explicitly referenced in Triggers table
- Explicitly referenced in STATIC section
- Explicitly referenced by a skill

**Why**: Token efficiency. Don't load 100 docs for every request.

**Example**:

```markdown
# BAD: Resource never loads
.0agnostic/03_protocols/my_workflow.md  (not referenced anywhere)

# GOOD: Resource loads via trigger
| User mentions X | Load workflow | `.0agnostic/03_protocols/my_workflow.md` | Skill |
```

### 7.3 The "Cascade Inheritance" Rule

**CRITICAL**: Child layers inherit parent context automatically.

Overrides happen at child layer, not parent.

**Why**: Avoids duplication and ensures consistency.

**Example**:

```
layer_1_project_school/.0agnostic/02_rules/static/
  └── grading_rules.md (applies to ALL school projects)

layer_4_subx3_project_cse300/.0agnostic/02_rules/static/
  └── cse300_specific_rule.md (CSE 300 only, doesn't override parent)
```

---

## Summary: Porting Checklist

- [ ] Validate 0AGNOSTIC.md structure (2.1 marker check)
- [ ] Validate .0agnostic/ directories exist (1.2)
- [ ] Ensure STATIC sections are substantive but lean
- [ ] Confirm Triggers table is complete
- [ ] All .0agnostic/ resources referenced in Triggers or STATIC
- [ ] Skills documented and referenced
- [ ] Rules categorized by importance (I0, I1, I2, etc.)
- [ ] Run `agnostic-sync.sh` to generate tool files
- [ ] Test context loading with sample user queries
- [ ] Verify cascading works (parent → child)
- [ ] Commit and push

---

## References

- **Source of Truth**: `0AGNOSTIC.md` at each layer
- **System**: `.0agnostic/` with numbered directories
- **Generation**: `agnostic-sync.sh` (at repo root)
- **Validation**: `.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING.md`
- **Cascade Logic**: Layer-stage system in layer_0/CLAUDE.md
