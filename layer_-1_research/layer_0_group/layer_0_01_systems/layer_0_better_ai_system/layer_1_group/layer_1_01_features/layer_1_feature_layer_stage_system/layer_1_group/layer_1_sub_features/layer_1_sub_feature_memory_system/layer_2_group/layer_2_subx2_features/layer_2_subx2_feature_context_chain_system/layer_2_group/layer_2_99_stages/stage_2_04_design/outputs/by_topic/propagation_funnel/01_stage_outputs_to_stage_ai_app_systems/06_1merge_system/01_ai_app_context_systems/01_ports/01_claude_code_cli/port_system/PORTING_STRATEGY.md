# Claude Code CLI — Porting Strategy for 0AGNOSTIC.md & .0agnostic/

**Date**: 2026-02-27
**Focus**: How to port our custom 0AGNOSTIC.md system + .0agnostic/ directories into Claude Code CLI's native system

---

## Overview

We use a custom **0AGNOSTIC.md + .0agnostic/ system** (user-designed context architecture). Claude Code CLI has **native CLAUDE.md + .claude/ system** (native mechanism). This document explains the mapping.

### Key Insight

Our system is **APPLICATION-IMPLEMENTED** in Claude Code CLI's terminology:
- Claude Code provides the mechanism (CLAUDE.md cascade, MEMORY.md injection)
- We provide the strategy (0AGNOSTIC.md structure, .0agnostic/ organization)

---

## Part 1: Porting 0AGNOSTIC.md (The File)

### Our Structure: 0AGNOSTIC.md

Our 0AGNOSTIC.md has two sections:

```markdown
# ═══ STATIC CONTEXT (always loaded) ═══
  ├─ Entity Definition (Identity, Key Behaviors, Delegation, Methodology)
  ├─ Current Status (concise summary)
  └─ [Other static info]

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══
  ├─ Current State Detail
  ├─ References
  ├─ Resources Available
  └─ [Other dynamic info]
```

### Claude Code's Native Structure: CLAUDE.md

Claude Code's CLAUDE.md is just Markdown — no rigid sections. But we can organize it similarly:

```markdown
# [Entity Name] — Claude Code Context

## Identity
[What we are, role, scope, parent, children]

## Key Behaviors
[What we do, constraints, methodology]

## Triggers
[When to load what context (table)]

## Resources
[Navigation: where to find things]

## Current Status
[Summary of state, readiness, key findings]

---

## [Additional sections as needed]
[Anything you want loaded every session]
```

### Mapping: 0AGNOSTIC STATIC → CLAUDE.md

| Our 0AGNOSTIC.md STATIC | Maps To Claude Code CLAUDE.md |
|--------------------------|-------------------------------|
| Entity Definition (Identity) | `## Identity` section |
| Key Behaviors | `## Key Behaviors` section |
| Current Status | `## Current Status` section |
| Delegation Contract | `## Triggers` (when to delegate) |
| Methodology | `## Key Behaviors` + `## Methodology` |
| Triggers (table) | `## Triggers` table (which context to load when) |

**Example Mapping**:

**0AGNOSTIC.md STATIC**:
```markdown
# ─ Entity Definition ─
- **Role**: Layer 1 project coordinator
- **Scope**: All school-related work
- **Parent**: user root (layer 0)
- **Children**: layer_1_sub_projects

# ─ Current Status ─
**Phase**: Active — 5 courses running, 2 redesigned
```

**↓ Becomes CLAUDE.md**:
```markdown
## Identity
You are an agent at Layer 1 (Project).
- **Role**: School project coordinator
- **Scope**: All school-related work (courses, projects, planning)
- **Parent**: User root (~/CLAUDE.md)
- **Children**: layer_1_sub_projects

## Current Status
**Phase**: Active — 5 courses running, 2 courses redesigned | **Last Updated**: 2026-02-27

5 courses active (CSE 300, MATH 119, etc.). 2 courses redesigned with new grading systems. Focus on grade strategy dashboards and student support.
```

### Mapping: 0AGNOSTIC DYNAMIC → MEMORY.md (First 200 Lines)

| Our 0AGNOSTIC.md DYNAMIC | Maps To Claude Code MEMORY.md |
|--------------------------|-------------------------------|
| Current State Detail | First 200 lines: "Current Status" section |
| Key References | First 200 lines: Navigation table |
| Open Items | First 200 lines if critical, full MEMORY.md if exploratory |
| Success Criteria | `## Triggers` (when to consider success) |

**Example Mapping**:

**0AGNOSTIC.md DYNAMIC**:
```markdown
# ─ Current State ─
- Stage 06 (Development): Implementing grade dashboards for CSE 300 and MATH 119
- Working on: Canvas MCP integration, assignment classification, priority scoring
- Blockers: None, on track

# ─ References ─
| Location | Purpose |
| .0agnostic/03_protocols/grade_strategy_system/ | Trajectory stores |
```

**↓ Becomes MEMORY.md (First 200 Lines)**:
```markdown
# Auto Memory — School Project

## Current Status
Stage 06 (Development): Implementing grade dashboards for CSE 300 and MATH 119. Working on Canvas MCP integration. No blockers.

## Key References
- **Trajectory stores**: `.0agnostic/03_protocols/grade_strategy_system/`
- **Skills**: Canvas-fetch, grade-calculator, calc-dashboard, cse300-dashboard
- **Grading models**: CSE 300 percentage-based, MATH 119 specs-based

---
[Detailed content beyond 200 lines]
```

---

## Part 2: Porting .0agnostic/ Directory System

### Our Structure: .0agnostic/ (Numbered Directories)

```
.0agnostic/
├── 01_knowledge/
│   └── [by topic: canvas_integration, grading_models, etc.]
├── 02_rules/
│   ├── static/
│   └── dynamic/
├── 03_protocols/
│   └── [step-by-step procedures]
├── 04_episodic_memory/
│   └── [sessions, changes logs]
├── 05_handoff_documents/
│   ├── 01_incoming/
│   └── 02_outgoing/
├── 06_context_avenue_web/
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

### Claude Code's Native Structure: ~/.claude/

```
~/.claude/
├── CLAUDE.md
├── settings.json
├── projects/[hash]/
│   └── memory/
│       ├── MEMORY.md
│       ├── [topic-files].md
│       └── ...
├── skills/
│   └── [skill-name]/SKILL.md
├── plans/
│   └── [plan-files].md
├── hooks/
│   └── [hook-scripts].sh
└── [other state dirs]
```

### Mapping: .0agnostic/ → ~/.claude/

| Our .0agnostic/ | Maps To ~/.claude/ |
|-----------------|-------------------|
| `01_knowledge/` | `projects/[hash]/memory/[topic-files].md` + MEMORY.md |
| `02_rules/static/` | `CLAUDE.md` sections |
| `02_rules/dynamic/` | Triggers table in CLAUDE.md |
| `03_protocols/` | `projects/[hash]/memory/[topic-files].md` (detailed procedures) |
| `04_episodic_memory/` | `projects/[hash]/memory/episodic.md` (auto-aggregated) |
| `05_handoff_documents/` | `projects/[hash]/memory/[topic-files].md` (session notes) |
| `06_context_avenue_web/01_skills/` | `skills/` directory |
| `06_context_avenue_web/08_hooks/` | `hooks/` directory |
| `07+_setup_dependant/` | Project-specific setup (Canvas creds, etc.) |

---

## Part 3: Detailed Porting Examples

### Example 1: Porting Knowledge (01_knowledge/)

**Our Structure**:
```
.0agnostic/01_knowledge/
├── canvas_integration/
│   ├── principles/
│   │   └── grading_model_types.md
│   ├── docs/
│   │   └── assignment_type_taxonomy.md
│   └── resources/
│       └── templates/
│           └── grading_model_template.md
```

**↓ Ports To Claude Code As**:
```
~/.claude/projects/[hash]/memory/
├── MEMORY.md (first 200 lines: entry point + nav)
├── canvas_integration.md (principles + docs merged)
├── grading_models.md (knowledge + examples)
└── templates.md (if complex, separate file)
```

**Practical Porting**:
1. Read our `.0agnostic/01_knowledge/canvas_integration/principles/grading_model_types.md`
2. Extract key concepts (specs-based vs percentage-based)
3. Merge with `.0agnostic/01_knowledge/canvas_integration/docs/`
4. Write `~/.claude/projects/[hash]/memory/canvas_integration.md` combining both
5. Reference in MEMORY.md first 200 lines: "See `/memory` for Canvas integration patterns"

### Example 2: Porting Rules (02_rules/)

**Our Structure**:
```
.0agnostic/02_rules/
├── static/
│   └── grade_strategy_rules.md (always apply)
└── dynamic/
    └── grade_strategy_triggers/
        └── grade_strategy_triggers.md (scenario-specific)
```

**↓ Ports To Claude Code As**:
```
CLAUDE.md (both static + dynamic)

## Key Behaviors
[From static rules: what we always do]

## Triggers
[From dynamic rules: when to load what context (table)]
```

**Practical Porting**:
1. Read our static rules: "Always use Canvas MCP for grade data"
2. Write into CLAUDE.md: `## Key Behaviors → "Use Canvas MCP for all grade queries"`
3. Read our dynamic triggers: "If user asks about grade status, load grade_strategy_trajectory.md"
4. Write into CLAUDE.md: `## Triggers` table

### Example 3: Porting Protocols (03_protocols/)

**Our Structure**:
```
.0agnostic/03_protocols/
└── grade_strategy_system/
    ├── canvas_grade_dashboard_trajectory.md (7-step workflow)
    ├── grading_model_analysis_trajectory.md (analysis steps)
    └── assignment_classification_trajectory.md (classification steps)
```

**↓ Ports To Claude Code As**:
```
~/.claude/projects/[hash]/memory/
├── grade_dashboard_workflow.md (detailed steps)
├── grading_analysis_patterns.md (how-to guide)
└── assignment_classification.md (patterns + examples)
```

**Practical Porting**:
1. Read trajectory: `canvas_grade_dashboard_trajectory.md` (7-step workflow)
2. Convert to `grade_dashboard_workflow.md` (more concise for memory)
3. Include key steps: fetch → classify → count → score → deadline → priority → output
4. Reference in MEMORY.md: "See `/memory` for grade dashboard workflow"

### Example 4: Porting Skills (06_context_avenue_web/05_skills/)

**Our Structure**:
```
.0agnostic/06_context_avenue_web/01_file_based/05_skills/
├── canvas-fetch/
│   └── SKILL.md
└── grade-calculator/
    └── SKILL.md
```

**↓ Ports Directly To Claude Code**:
```
~/.claude/skills/
├── canvas-fetch/
│   └── SKILL.md (unchanged)
└── grade-calculator/
    └── SKILL.md (unchanged)
```

**Practical Porting**:
1. Our skill files are already CLAUDE.md format
2. Copy directly: `cp -r .0agnostic/06_context_avenue_web/01_file_based/05_skills/* ~/.claude/skills/`
3. Update paths in CLAUDE.md to reference new location
4. Done!

---

## Part 4: Practical Porting Workflow

### Step 1: Create Project CLAUDE.md

```bash
# Create structure
mkdir -p ~/.claude/projects/school-project/memory
mkdir -p ~/.claude/skills

# Create CLAUDE.md from 0AGNOSTIC.md
cat > ~/.claude/projects/school-project/0AGNOSTIC_MAPPED.md << 'EOF'
# ═══ Mapping Template ═══
## Original 0AGNOSTIC.md File
[Read and copy STATIC context here]

## Mapped to CLAUDE.md
[Translate to CLAUDE.md structure]

## Mapped to MEMORY.md (first 200 lines)
[Extract most important content]
EOF
```

### Step 2: Write CLAUDE.md

```bash
cat > ~/.claude/CLAUDE.md << 'EOF'
# School Project — Claude Code Configuration

## Identity
[From 0AGNOSTIC.md: Entity Definition]

## Key Behaviors
[From 0AGNOSTIC.md: Key Behaviors + static rules]

## Triggers
[From 0AGNOSTIC.md: Triggers table + dynamic rules]

## Skills
[List all skills with WHEN/WHEN NOT]

## Resources
[Navigation: where to find memory, skills, etc.]

## Current Status
[From 0AGNOSTIC.md: Current Status summary]
EOF
```

### Step 3: Write MEMORY.md

```bash
cat > ~/.claude/projects/school-project/memory/MEMORY.md << 'EOF'
# Auto Memory — School Project

## Current Status
[Most important status from 0AGNOSTIC.md Current Status section]

## Key References
[Quick navigation to skills, docs, etc.]

## Quick Reference
[Essentials that apply to every session]

---
[BEYOND 200 LINES]
---

## Canvas Integration (Topic 1)
[Detailed content from .0agnostic/01_knowledge/canvas_integration/]

## Grading Models (Topic 2)
[Detailed content from .0agnostic/01_knowledge/grading_models/]

## Grade Dashboard Workflow (Topic 3)
[Detailed content from .0agnostic/03_protocols/grade_strategy_system/]
EOF
```

### Step 4: Copy Skills

```bash
# Copy skills from .0agnostic to ~/.claude/skills
cp -r .0agnostic/06_context_avenue_web/01_file_based/05_skills/* ~/.claude/skills/

# Verify
ls ~/.claude/skills/
# Should show: canvas-fetch/, grade-calculator/, calc-dashboard/, cse300-dashboard/
```

### Step 5: Create Topic Files (Optional)

```bash
# For complex topics, create separate memory files

cat > ~/.claude/projects/school-project/memory/debugging.md << 'EOF'
# Debugging Patterns — School Project

[From .0agnostic/04_episodic_memory/ + experience]
EOF

cat > ~/.claude/projects/school-project/memory/architecture.md << 'EOF'
# Architecture Notes — School Project

[From .0agnostic/01_knowledge/layer_stage_system/ + experiences]
EOF
```

---

## Part 5: Migration Checklist

- [ ] Create ~/.claude/projects/[project-id]/ structure
- [ ] Write ~/.claude/CLAUDE.md (global rules)
- [ ] Write /project/CLAUDE.md (project-specific, if multi-project)
- [ ] Write ~/.claude/projects/[project-id]/memory/MEMORY.md (first 200 lines essentials)
- [ ] Add topic files to memory/ (knowledge, debugging, architecture, etc.)
- [ ] Copy skills from .0agnostic/06_context_avenue_web/01_file_based/05_skills/ → ~/.claude/skills/
- [ ] Update CLAUDE.md Triggers table with skill references
- [ ] Test: `/context` shows correct context window
- [ ] Test: `/memory` shows full MEMORY.md
- [ ] Test: `/skill-name` invokes skill correctly
- [ ] Document any custom MCP servers needed (Canvas, GitHub, etc.)
- [ ] Set up ~/.claude/settings.json for preferences

---

## Part 6: Key Trade-Offs & Limitations

### What Works Well in Claude Code

✅ CLAUDE.md cascade (matches our 0AGNOSTIC.md approach)
✅ MEMORY.md organization (200 lines auto-injected is enough)
✅ Skills system (direct port from .0agnostic/06/05_skills/)
✅ Triggers table (we define when to load context)
✅ Auto-compaction (matches our context management philosophy)
✅ MCP integration (Canvas, GitHub, Tavily, custom)

### What Requires Adaptation

⚠️ **No native agent delegation** — 0AGNOSTIC.md covers agent context, but Claude Code has limited multi-agent support (subagents are isolated, not coordinated)
  - **Solution**: Use subagents for parallel analysis only, not for complex coordination

⚠️ **No native handoff documents** — .0agnostic/05_handoff_documents/ doesn't map directly
  - **Solution**: Store handoff notes in memory/episodic.md (topic file)

⚠️ **No native AALang/JSON-LD** — .0agnostic/06_context_avenue_web/01_aalang/ doesn't port
  - **Solution**: Store agent modes as text descriptions in CLAUDE.md or separate memory files

⚠️ **No native data-based avenues** — .0agnostic/06_context_avenue_web/02_data_based/ (knowledge graphs, embeddings) not supported
  - **Solution**: Simulate via well-organized memory files + semantic file references

### What To Keep in .0agnostic/

- ✅ `.0agnostic/01_knowledge/` — Port to MEMORY.md topic files
- ✅ `.0agnostic/02_rules/` → Port to CLAUDE.md sections
- ✅ `.0agnostic/03_protocols/` → Port to MEMORY.md topic files
- ✅ `.0agnostic/06_context_avenue_web/01_file_based/05_skills/` → Copy to ~/.claude/skills/
- ❓ `.0agnostic/04_episodic_memory/` → Optional (use MEMORY.md instead)
- ❓ `.0agnostic/05_handoff_documents/` → Optional (use MEMORY.md topic instead)
- ❌ `.0agnostic/06_context_avenue_web/01_aalang/` → Keep as documentation, not used by Claude Code
- ❌ `.0agnostic/06_context_avenue_web/02_data_based/` → Keep as reference, not used by Claude Code

---

## Part 7: Validation

### How to Know Porting Worked

1. **Session Start**: Run `claude`
   - Should see CLAUDE.md loaded
   - `/context` should show token usage
   - `/memory` should show full MEMORY.md

2. **Skills Available**: Type `/@` and autocomplete should show available skills
   - `/canvas-fetch`
   - `/grade-calculator`
   - `/calc-dashboard`
   - `/cse300-dashboard`

3. **File References**: Try `@src/auth.py` (or relevant file)
   - Should load file contents
   - `/context` should show file token count

4. **Compaction Works**: Generate lots of conversation
   - Context should auto-compact at 90%
   - Conversation should continue uninterrupted
   - Check `/context` to see freed tokens

---

## Summary: Porting Strategy

| What | From 0AGNOSTIC.md | To Claude Code CLI | Notes |
|------|-------------------|-------------------|-------|
| **File Structure** | 0AGNOSTIC.md (STATIC + DYNAMIC) | CLAUDE.md + MEMORY.md | Direct mapping, same concepts |
| **Knowledge** | .0agnostic/01_knowledge/ | memory/[topic-files].md | Flattened, merged by topic |
| **Rules** | .0agnostic/02_rules/ | CLAUDE.md sections + Triggers | 1:1 mapping |
| **Protocols** | .0agnostic/03_protocols/ | memory/[topic-files].md | Treated as detailed procedures |
| **Skills** | .0agnostic/06/05_skills/ | ~/.claude/skills/ | Direct copy, no changes needed |
| **Episodic Memory** | .0agnostic/04_episodic/ | memory/episodic.md | Auto-aggregated topic file |
| **Handoffs** | .0agnostic/05_handoff/ | memory/[notes].md | Store as session notes |
| **Agents (AALang)** | .0agnostic/06_context_avenue_web/01_aalang/ | Keep as documentation | Claude Code doesn't use JSON-LD |
| **Data-Based** | .0agnostic/06_context_avenue_web/02_data_based/ | Keep as reference | Claude Code not a data structure store |

**Key Principle**: Our 0AGNOSTIC.md system is **user-designed architecture** layered ON TOP of Claude Code's native CLAUDE.md system. Most of it ports cleanly; some advanced features (AALang, knowledge graphs) are kept as documentation reference.
