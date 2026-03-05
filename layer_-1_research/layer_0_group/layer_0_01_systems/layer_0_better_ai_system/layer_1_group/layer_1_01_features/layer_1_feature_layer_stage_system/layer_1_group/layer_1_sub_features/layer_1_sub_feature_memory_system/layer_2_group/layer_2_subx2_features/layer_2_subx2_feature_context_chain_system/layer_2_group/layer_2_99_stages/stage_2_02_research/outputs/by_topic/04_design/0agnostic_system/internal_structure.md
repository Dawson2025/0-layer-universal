---
resource_id: "88f4c099-31cd-419d-a8d9-2a99cca21c8a"
resource_type: "output"
resource_name: "internal_structure"
---
# Design — .0agnostic/ Internal Structure

## Purpose

Design document defining the canonical internal structure of `.0agnostic/` directories. Sub-layers (knowledge, rules, protocols) are dissolved as standalone directories and absorbed into `.0agnostic/` as internal subdirectories, preserving the taxonomy while gaining native tool integration through sync.

---

## Decision

**Sub-layers become subdirectories inside `.0agnostic/`.**

The organizational taxonomy (knowledge, rules, protocols) is preserved — it moves from being a parallel directory structure (`layer_0_04_sub_layers/sub_layer_0_XX_*`) into the `.0agnostic/` directory that every entity already has. From there, `agnostic-sync.sh` syncs content to each tool's native dot folder (`.claude/`, `.cursor/`, `.codex/`, `.gemini/`).

---

## Current State

### Sub-Layer Hierarchy (Being Dissolved)

```
layer_0/layer_0_04_sub_layers/
├── sub_layer_0_01_knowledge_system/    (~38 files)
│   ├── aalang_gab_system/
│   ├── agent_coordination/
│   ├── context_loading/
│   ├── entity_lifecycle/
│   ├── layer_stage_system/
│   ├── naming_conventions/
│   ├── navigation_patterns/
│   ├── principles/
│   └── software_engineering_knowledge_system/
├── sub_layer_0_02_rules/               (~200+ files)
│   ├── 0_every_api_request/
│   ├── 0_instruction_docs/
│   ├── 1_scenario_based/
│   ├── 3_archive_docs/
│   ├── dynamic/
│   ├── static/
│   └── sub_layer_0_04_99_stages/
├── sub_layer_0_03_protocols/           (~20 files)
└── sub_layer_0_04+_setup_dependant/    (~100+ files)
    └── sub_layer_0_05_operating_systems/
```

### Current .0agnostic/ (Being Extended)

255 `.0agnostic/` directories exist across the hierarchy. Most are minimal:

```
.0agnostic/                    # Typical minimal structure
├── agents/
├── episodic/
├── hooks/scripts/
└── skills/
```

Only `.0agnostic/` has a fuller structure with rules, scripts, templates, and tests.

---

## New .0agnostic/ Canonical Structure

```
.0agnostic/
├── knowledge/                  # Reference docs — NOT auto-loaded
│   ├── principles/             # Core principles (subset may sync to rules/)
│   └── resources/              # Templates, databases, reference material used by knowledge files
│
├── rules/                      # Behavioral constraints — synced to tool dot folders
│   ├── static/                 # Always-loaded rules WITH full protocol inline
│   └── dynamic/                # Triggers only — reference protocols/ for procedures
│
├── protocols/                  # Full step-by-step procedures — referenced by dynamic rules
│
├── skills/                     # Callable skills (existing, unchanged)
│   └── */SKILL.md
│
├── agents/                     # Agent definitions (existing, unchanged)
│
├── episodic_memory/            # Session records (existing, unchanged)
│   └── index.md
│
├── hooks/                      # Pre/post hooks (existing, unchanged)
│   └── scripts/
│
├── scripts/                    # Utility scripts (existing, unchanged)
│
├── templates/                  # Templates for entity creation (existing, unchanged)
│
└── tests/                      # Validation tests (existing, unchanged)
```

### Core Relationship: Rules Inform Protocols

Rules and protocols are not independent — **protocols are informed by rules**. The relationship differs between static and dynamic:

```
STATIC RULES (always loaded):
┌─────────────────────────────────────────┐
│ rules/static/context_modification.md    │
│                                         │
│ ## Rule                                 │
│ Always show a diagram before modifying  │
│ AI context files.                       │
│                                         │
│ ## Protocol (inline)                    │
│ 1. Identify all files to change         │
│ 2. Draw diagram with full paths         │
│ 3. Wait for user approval               │
│ 4. Execute changes exactly as approved  │
│ 5. Commit and push                      │
└─────────────────────────────────────────┘
  ↑ Full protocol included — always in context anyway

DYNAMIC RULES (loaded by path match):
┌─────────────────────────────────────────┐
│ rules/dynamic/research_workflow.md      │
│                                         │
│ ---                                     │
│ paths: layer_-1_research/**             │
│ ---                                     │
│                                         │
│ ## When                                 │
│ Working in research directories.        │
│                                         │
│ ## Why                                  │
│ Research follows stage progression.     │
│                                         │
│ ## What To Do                           │
│ Follow: protocols/research_workflow.md  │
│ Use skill: /stage-workflow              │
└─────────────────────────────────────────┘
  ↑ Trigger only — references protocol for the full procedure

┌─────────────────────────────────────────┐
│ protocols/research_workflow.md          │
│                                         │
│ ## Research Workflow Protocol            │
│ 1. Identify current stage (01-11)       │
│ 2. Read stage outputs directory         │
│ 3. Check status.json for progress       │
│ 4. Produce deliverables for the stage   │
│ 5. Update status.json                   │
│ 6. Create handoff if ending session     │
└─────────────────────────────────────────┘
  ↑ Full procedure — loaded on-demand when referenced
```

**Why this split matters:**
- Static rules are always in context, so including the protocol inline costs nothing extra
- Dynamic rules are loaded conditionally — keeping them lightweight (triggers only) minimizes context when the rule loads
- The full procedure lives in protocols/ and is loaded only when the agent needs to execute it
- This gives two levels of progressive disclosure: the rule triggers awareness, the protocol provides instruction

### What Changed

| Component | Before | After |
|-----------|--------|-------|
| Knowledge | `sub_layer_0_01_knowledge_system/` | `.0agnostic/knowledge/` |
| Principles | `sub_layer_0_01_knowledge_system/principles/` | `.0agnostic/knowledge/principles/` |
| Static rules | `sub_layer_0_02_rules/static/` | `.0agnostic/rules/static/` |
| Dynamic rules | `sub_layer_0_02_rules/dynamic/` | `.0agnostic/rules/dynamic/` |
| Protocols | `sub_layer_0_03_protocols/` | `.0agnostic/protocols/` |
| Setup-dependent | `sub_layer_0_04+_setup_dependant/` | `.0agnostic/knowledge/setup/` or tool-specific in `.1merge/` |
| Resources | Scattered (templates in various locations) | `.0agnostic/knowledge/resources/` |
| Skills | `.0agnostic/skills/` | `.0agnostic/skills/` (unchanged) |
| Agents | `.0agnostic/agents/` | `.0agnostic/agents/` (unchanged) |

---

## How Each Subdirectory Works

### knowledge/

**Purpose:** Reference documentation that provides context but should NOT be auto-loaded into every session.

**Contents:**
- Domain knowledge (aalang_gab_system/, layer_stage_system/, entity_lifecycle/)
- Agent coordination patterns
- Navigation guides
- Naming conventions
- Software engineering knowledge

**How agents access it:**
- Via @import references from CLAUDE.md or rules
- Via skill references ("read knowledge/X before proceeding")
- Via explicit agent search when working in related areas
- Via protocol references (protocols point to knowledge for background)
- NOT auto-loaded — too large for static context

**Why NOT auto-loaded:** Knowledge files are reference material. Loading 38+ files into every API message wastes context budget. Agents should pull knowledge on-demand when the task requires it.

### knowledge/principles/

**Purpose:** Core principles that guide all work. A subset of knowledge that is foundational enough to warrant special treatment.

**Contents:**
- Universal principles that apply to all layers
- Design principles for the framework
- Decision-making guidelines

**How agents access it:**
- Short, critical principles: extracted into `.0agnostic/rules/static/` so they auto-load
- Detailed principle documents: stay in `knowledge/principles/` and are accessed on-demand
- This is a "promote the summary, reference the detail" pattern

### knowledge/resources/

**Purpose:** Supporting material that knowledge files reference — templates, databases, data tables, examples, and other reference artifacts.

**Contents:**
- Templates (entity templates, document templates, boilerplate)
- Data tables and lookup references
- Example files and sample configurations
- Databases or structured data that knowledge files point to
- Diagrams, schemas, and visual references

**How agents access it:**
- Referenced from within knowledge files ("see resources/entity_template.md")
- Referenced from protocols ("use the template at knowledge/resources/...")
- Never accessed directly by rules — rules reference protocols or knowledge, which in turn reference resources
- NOT auto-loaded — pulled only when a knowledge file or protocol needs it

**Relationship:** Resources are the leaf nodes of the reference chain. Knowledge files explain concepts and point to resources for concrete artifacts. Protocols use resources when executing procedures (e.g., "create entity from template at knowledge/resources/...").

### rules/static/

**Purpose:** Rules that must be followed in every session, regardless of context. These are the highest-priority behavioral constraints. **Static rules include their full protocol inline** — since they're always loaded anyway, there's no context cost to including the complete procedure.

**Contents:**
- AI context modification protocol (rule + full procedure)
- Commit/push rules (rule + full procedure)
- Context traversal requirements (rule + full procedure)
- File path linking rule (rule + full procedure)
- Documentation protocol (rule + full procedure)

**Structure of a static rule file:**
```markdown
# Rule: AI Context Modification Protocol

## Constraint
ALWAYS show a diagram before modifying AI context files.
NEVER proceed without explicit user approval.

## Protocol
1. Identify all files that will change
2. Draw a complete diagram with full paths
3. Present to user and wait for approval
4. Execute changes exactly as approved
5. Stage, commit with [AI Context] prefix, push
```

**Sync behavior:**
- `agnostic-sync.sh` copies these to `.claude/rules/` (and equivalent for other tools)
- Claude Code auto-loads all `.md` files in `.claude/rules/` at session start with high priority
- No agent decision needed — the tool handles auto-loading

**Key property:** Files here are loaded into EVERY API message. They include both the constraint AND the procedure because both are always needed. The agent sees the rule and knows exactly what to do — no second lookup required.

### rules/dynamic/

**Purpose:** Rules that apply only in specific contexts — certain directories, file types, or project areas. **Dynamic rules contain only triggers** — when, where, why, and a description of what to do. The full procedure lives in `protocols/` and is referenced by the dynamic rule.

**Contents:**
- Path-scoped triggers (e.g., "when in research directories, follow protocol X")
- File-type-scoped triggers (e.g., "when editing .gab.jsonld files, follow protocol Y")
- Project-specific triggers

**Structure of a dynamic rule file:**
```yaml
---
paths: layer_-1_research/**
---
```
```markdown
# Trigger: Research Stage Workflow

## When
Working in any research directory (`layer_-1_research/`).

## Where
All research layers, features, sub-features, and their stage directories.

## Why
Research follows a structured stage progression (01-11). Skipping stages
or working in the wrong stage produces disorganized output.

## What To Do
Follow the research workflow protocol:
→ `protocols/research_workflow.md`
→ Or invoke skill: `/stage-workflow`

## Description
Ensures research work proceeds through stages systematically,
producing deliverables at each stage before advancing.
```

**Sync behavior:**
- `agnostic-sync.sh` copies these to `.claude/rules/` with YAML `paths:` frontmatter
- Claude Code auto-loads these only when the agent works with matching file paths
- Other tools use their equivalent path-scoping mechanism

**Key property:** Dynamic rules are lightweight triggers. They tell the agent WHEN something applies and WHERE to find the full procedure — but they don't include the procedure itself. This keeps them small so path-matching loads minimal context.

**Why triggers only:** Dynamic rules load conditionally based on path. If the agent is working in a research directory, the trigger loads and says "follow this protocol." The full protocol loads only if the agent actually needs to execute it. Two levels of progressive disclosure: trigger → protocol.

### protocols/

**Purpose:** Full step-by-step procedures for recurring workflows. Protocols are the "how to do it" — the complete instruction set. **Protocols are informed by rules** — rules define the constraints and triggers, protocols define the execution.

**Contents:**
- Context loading protocol (full procedure)
- Entity creation workflow (full procedure)
- Session handoff procedure (full procedure)
- Stage transition workflow (full procedure)
- Hierarchy adoption checklist (full procedure)
- Research workflow protocol (full procedure)

**Structure of a protocol file:**
```markdown
# Protocol: Entity Creation

## Prerequisites
- Current layer and stage identified
- Entity type determined (project, feature, sub-feature)

## Steps
1. Read entity structure template from `knowledge/resources/entity_template/`
2. Create directory structure per template
3. Create `0AGNOSTIC.md` using template from `knowledge/resources/templates/`
4. Create `.0agnostic/` with appropriate subdirectories
5. Create `.1merge/` with tool-specific override directories
6. Run `agnostic-sync.sh` to generate tool files
7. Create `0INDEX.md`
8. Commit and push

## References
- Template: `knowledge/resources/templates/0AGNOSTIC.md.template`
- Entity types: `knowledge/entity_lifecycle/ENTITY_TYPES.md`
- Naming: `knowledge/naming_conventions/HIERARCHY_NAMING_CONVENTION.md`
```

**Relationship to rules:**
- **Static rules** include protocols inline (always loaded, no extra cost)
- **Dynamic rules** reference protocols by path (loaded on-demand when needed)
- Protocols may reference `knowledge/` files for background and `knowledge/resources/` for templates and artifacts

**Sync behavior:**
- `agnostic-sync.sh` transforms protocols into `.claude/skills/*/SKILL.md` format
- Each protocol becomes a skill with WHEN/WHEN NOT conditions
- Skill descriptions load at session start (~16K char budget)
- Full protocol content loads only when the skill is invoked

**Key distinction from rules:** Rules define constraints ("always/never") and triggers ("when X, do Y"). Protocols define procedures ("step 1, step 2, step 3"). A rule without a protocol tells you what to do but not how. A protocol without a rule has no trigger — the agent won't know when to use it. Together they form a complete instruction.

---

## Sync Flow

```
.0agnostic/                         Tool Dot Folders
─────────────────────────           ─────────────────────────
rules/static/*.md          ──sync──→ .claude/rules/*.md          (auto-loaded, high priority)
                           ──sync──→ .cursor/rules/*.mdc         (transformed to .mdc format)
                           ──sync──→ .codex/ (in AGENTS.md)

rules/dynamic/*.md         ──sync──→ .claude/rules/*.md          (with paths: frontmatter)
                           ──sync──→ .cursor/rules/*.mdc         (with auto-attach globs)

protocols/*.md             ──sync──→ .claude/skills/*/SKILL.md   (progressive disclosure)
                           ──sync──→ .codex/.agents/skills/      (Codex skill format)

knowledge/                 ──stay──→ .0agnostic/knowledge/       (accessed via @import/skills)

skills/                    ──sync──→ .claude/skills/             (already synced)
                           ──sync──→ .codex/.agents/skills/

.1merge/.1claude_merge/    ──merge─→ .claude/                    (tool-specific overrides)
.1merge/.1cursor_merge/    ──merge─→ .cursor/                    (tool-specific overrides)
.1merge/.1codex_merge/     ──merge─→ .codex/                     (tool-specific overrides)
```

### Three-Tier Merge (Existing Pattern, Unchanged)

```
Tier 1: .0agnostic/           ← Source of truth (tool-agnostic)
Tier 2: .1merge/.1X_merge/    ← Tool-specific overrides
Tier 3: .claude/ (generated)  ← Final output (what the tool reads)
```

---

## Inheritance Across the Hierarchy

Not every `.0agnostic/` needs all subdirectories. The structure is additive:

### Root Level (.0agnostic/)
```
.0agnostic/
├── knowledge/principles/     # Universal principles
├── rules/static/             # Universal rules (apply everywhere)
├── protocols/                # Universal protocols
└── skills/                   # Universal skills
```

### Layer 0 (.0agnostic/)
```
.0agnostic/
├── knowledge/                # Framework knowledge (aalang, entity lifecycle, etc.)
│   └── principles/           # Layer-0 principles
├── rules/
│   ├── static/               # Framework rules
│   └── dynamic/              # Path-scoped framework rules
├── protocols/                # Framework protocols
├── skills/                   # Framework skills
├── scripts/                  # Utility scripts
└── templates/                # Entity creation templates
```

### Project Level (layer_1_project_X/.0agnostic/)
```
.0agnostic/
├── knowledge/                # Project-specific knowledge (if any)
├── rules/
│   ├── static/               # Project rules (if any)
│   └── dynamic/              # Project-specific path rules (if any)
├── skills/                   # Project skills
└── episodic_memory/          # Project session history
```

### Feature/Sub-Feature Level
```
.0agnostic/
├── skills/                   # Feature-specific skills (if any)
└── episodic_memory/          # Feature session history
```

**Principle:** The deeper in the hierarchy, the leaner the `.0agnostic/`. Most features only need skills and episodic memory. Knowledge and rules are primarily at root and layer_0 levels.

---

## What Happens to layer_0_04_sub_layers/

The `layer_0/layer_0_04_sub_layers/` directory is dissolved. Its contents migrate:

| Current Location | New Location | Notes |
|------------------|-------------|-------|
| `sub_layer_0_01_knowledge_system/aalang_gab_system/` | `.0agnostic/knowledge/aalang_gab_system/` | Reference docs |
| `sub_layer_0_01_knowledge_system/agent_coordination/` | `.0agnostic/knowledge/agent_coordination/` | Reference docs |
| `sub_layer_0_01_knowledge_system/context_loading/` | `.0agnostic/knowledge/context_loading/` | Reference docs |
| `sub_layer_0_01_knowledge_system/entity_lifecycle/` | `.0agnostic/knowledge/entity_lifecycle/` | Reference docs |
| `sub_layer_0_01_knowledge_system/layer_stage_system/` | `.0agnostic/knowledge/layer_stage_system/` | Reference docs |
| `sub_layer_0_01_knowledge_system/naming_conventions/` | `.0agnostic/knowledge/naming_conventions/` | Reference docs |
| `sub_layer_0_01_knowledge_system/navigation_patterns/` | `.0agnostic/knowledge/navigation_patterns/` | Reference docs |
| `sub_layer_0_01_knowledge_system/principles/` | `.0agnostic/knowledge/principles/` | Detailed principles |
| `sub_layer_0_01_knowledge_system/software_engineering_knowledge_system/` | `.0agnostic/knowledge/software_engineering/` | Reference docs |
| `sub_layer_0_02_rules/0_every_api_request/` | `.0agnostic/rules/static/` | Auto-loaded rules |
| `sub_layer_0_02_rules/1_scenario_based/` | `.0agnostic/rules/dynamic/` | Path-scoped rules |
| `sub_layer_0_02_rules/0_instruction_docs/` | `.0agnostic/knowledge/instruction_docs/` | Reference (not rules) |
| `sub_layer_0_02_rules/3_archive_docs/` | Archive or delete | Historical, not active |
| `sub_layer_0_02_rules/sub_layer_0_04_99_stages/` | Evaluate per stage | Some may be rules, some knowledge |
| `sub_layer_0_03_protocols/` | `.0agnostic/protocols/` | Become skills via sync |
| `sub_layer_0_04+_setup_dependant/` | `.0agnostic/knowledge/setup/` + `.1merge/` | OS-specific → .1merge/ |

---

## Benefits Over Sub-Layer Hierarchy

| Aspect | Sub-Layer Hierarchy | .0agnostic/ Internal |
|--------|--------------------|--------------------|
| Auto-discovery | No tool finds them | Tools auto-load from synced dot folders |
| Priority | Standard (file content) | High (same as CLAUDE.md) for rules |
| Path scoping | Manual, requires agent awareness | Native YAML frontmatter |
| Progressive disclosure | None | Skills provide on-demand loading |
| Context cost | Agent must remember hierarchy structure | No extra context needed |
| Sync to tools | N/A | agnostic-sync.sh handles it |
| Industry alignment | Custom pattern | Matches every major tool's convention |
| Maintenance | Manual cross-referencing | Automated sync scripts |

---

## Related: Multi-Avenue Redundancy, Sync, and .1merge

The internal structure described above is one component of the larger 0Agnostic System. The other components are documented in dedicated files:

- **[Multi-Avenue Redundancy](multi_avenue_redundancy.md)** — How all 8 context avenues link together, effectiveness per tool, AALang/GAB integration, and the "any-one-fires" resilience model
- **[Sync System](sync_system.md)** — How `agnostic-sync.sh` transforms `.0agnostic/` content into tool-specific formats (`.claude/`, `.cursor/`, `.codex/`, etc.)
- **[.1merge Override System](merge_system.md)** — The three-tier merge system for tool-specific customizations
- **[System Overview](README.md)** — How all components connect

---

*Design document for .0agnostic/ internal structure*
*Created: 2026-02-16*
