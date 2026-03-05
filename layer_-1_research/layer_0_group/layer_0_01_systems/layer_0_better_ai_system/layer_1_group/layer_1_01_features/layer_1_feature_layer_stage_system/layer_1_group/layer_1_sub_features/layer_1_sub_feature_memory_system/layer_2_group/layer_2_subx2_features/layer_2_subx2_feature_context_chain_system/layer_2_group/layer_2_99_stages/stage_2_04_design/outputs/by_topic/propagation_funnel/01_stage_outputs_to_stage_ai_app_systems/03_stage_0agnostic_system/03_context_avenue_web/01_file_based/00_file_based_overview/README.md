---
resource_id: "2230d429-673e-4985-ad79-e39c53554a73"
resource_type: "readme
output"
resource_name: "README"
---
# File-Based Avenues (01-08) — Ordered by Comprehensiveness

<!-- section_id: "710f23f5-ec15-437e-91ac-4144b2891eba" -->
## Overview

The file-based avenues (01-08) are the **primary delivery mechanisms** for context. They are human-readable, version-controllable, and ordered from **most comprehensive to most fragmented**.

<!-- section_id: "ae1bae87-d84c-4ec7-ae86-abe216b728a0" -->
## Ordering Principle: Most Detailed → Least Detailed

The avenues are deliberately ordered from most comprehensive to most fragmented:

```
01 ← Most comprehensive (full detail)
02 ← Nearly complete
05 ← Focused detail
04 ← Curated references
06 ← Lightweight
07 ← Scoped
08 ← Least comprehensive (specific fragments)
```

This ordering reflects **information density and detail level**, not importance or frequency of use.

<!-- section_id: "142df3da-6986-4277-b62f-be96ceb85663" -->
## File-Based Avenues (01-08) in Detail

<!-- section_id: "3058d356-4c36-4908-b33e-951507c70d1e" -->
### Avenue 01: AALang JSON-LD — Most Comprehensive

**Detail Level**: Maximum

**Purpose**: Complete agent definitions with all structural information

**What it contains**:
- Complete mode definitions (all modes for this agent)
- All actors in each mode
- Full constraint definitions (every MUST/MUST NOT rule)
- Complete state machine definition
- Skill mappings
- Persona definitions
- Transitions

**Example**: `layer_2_orchestrator.gab.jsonld`
- 816 lines of JSON-LD
- 38 @graph entries
- 5 complete modes
- All constraints, actors, transitions
- 100% detail coverage

**Use when**: Need the complete, authoritative agent definition

<!-- section_id: "51a022dc-d8bd-4c35-b588-3d6cf9e2f2c7" -->
### Avenue 02: AALang Markdown Integration — Nearly Complete

**Detail Level**: ~80% (readable form)

**Purpose**: Human-readable summaries of Avenue 01

**What it contains**:
- Mode descriptions and purposes
- State actor roles (not full definitions)
- Constraints in readable form (not JSON-LD syntax)
- Mode flow diagrams
- Skill integration points
- References back to JSON-LD for detail

**Example**: `layer_2_orchestrator.integration.md`
- ~40 lines (readable version of 816-line JSON-LD)
- Modes table, actors, constraints, flow
- Easy to scan and understand

**Use when**: Need readable reference without JSON-LD syntax

<!-- section_id: "75eaa262-b813-494e-ac4e-316af6bc060c" -->
### Avenue 05: Skills — Focused Detail

**Detail Level**: Complete for task execution

**Purpose**: Step-by-step instructions for specific tasks

**What it contains**:
- Task name and description
- WHEN to use / WHEN NOT to use conditions
- Prerequisites (what must be true)
- Full execution steps
- Inputs and outputs
- References to related skills/knowledge

**Example**: `/calc-dashboard` skill
- Task description (calculate grade dashboard)
- Prerequisites (Canvas data available)
- 7-step workflow with full detail
- Inputs (course_id, rubric)
- Outputs (markdown dashboard)

**Use when**: Need to execute a specific task

<!-- section_id: "f6270582-f4cb-49b8-99ee-7d26163fc2b0" -->
### Avenue 04: @Import References — Curated Detail

**Detail Level**: Organized navigation and discovery

**Purpose**: Curated reference collections for finding related content

**What it contains**:
- Entity structure canonical trees
- Compliance checklists
- Architecture decision matrices
- Knowledge indexes
- Cross-referenced guides
- Navigation pointers

**Example**: `entity_structure.md`
- Canonical directory tree
- Naming conventions
- Required files for each type
- Links to instantiation guides

**Use when**: Need to find/understand related entities or templates

<!-- section_id: "5bd08e8e-ff85-42d9-8d24-ac26999102c9" -->
### Avenue 06: Agents — Lightweight Definition

**Detail Level**: Identity and capability summary

**Purpose**: Quick agent identity and purpose without full detail

**What it contains**:
- Agent identity (who/what is this?)
- Purpose statement
- Available modes (listed, not detailed)
- Delegation pattern
- Quick reference (1-2 page summary)

**Example**: `stage_delegator.agent.jsonld`
- Agent identity
- Purpose (delegate to appropriate stage)
- Modes available (summary)
- Links to full definition

**Use when**: Need to understand agent purpose quickly

<!-- section_id: "19bb5c09-d32f-466c-91fa-c472b70d17f8" -->
### Avenue 07: Path-Specific Rules — Scoped Context

**Detail Level**: Directory-specific, minimal

**Purpose**: Rules and context that apply specifically in this directory

**What it contains**:
- Rules that apply in this path
- Relevant skills for this location
- Navigation hints
- Context-specific triggers
- Shortcuts and shortcuts

**Example**: `.claude/rules/agnostic-edits.md`
- Rules for editing .0agnostic/ files
- Relevant skills to invoke
- Commit message format
- Links to update protocol

**Use when**: Working in this specific directory/path

<!-- section_id: "0f27640b-8753-4986-8e0e-24ecff1f6def" -->
### Avenue 08: Hooks — Most Fragmented

**Detail Level**: Event-specific actions

**Purpose**: Automation and validation scripts for specific events

**What it contains**:
- Pre-commit hooks (validate before commit)
- Post-merge hooks (update after merge)
- Sync scripts (propagate changes)
- Validation scripts (check structure)
- Event-triggered automations

**Example**: `.git/hooks/pre-commit`
- Specific trigger (before commit)
- Validation logic (check files)
- Action (run tests, lint, validate)
- Minimal context (focused on one event)

**Use when**: Need to automate a specific event

<!-- section_id: "47c72b51-de20-4e98-a69a-2446e75cca6d" -->
## Why This Ordering?

Think of the avenues as **layers of detail you peel back**:

1. **Start here** (01): Get the complete agent definition — understand EVERYTHING
2. **Or use this** (02): Get a readable summary if JSON-LD is too complex
3. **Focus on task** (05): Just want to execute a skill? Load skills
4. **Navigate** (04,07): Need to find related content or this directory's rules?
5. **Automate** (08): Just need event-specific scripts?

The ordering reflects **decreasing comprehensiveness** as you move from 01 → 08.

<!-- section_id: "6071ad67-af02-43c7-b0cd-756c089aafed" -->
## Any-One-Fires Resilience

Each avenue is independent and self-contained. An AI system can load via:

- **Avenue 01 only** → Parse JSON-LD, extract complete agent definition
- **Avenue 02 only** → Read markdown, understand mode descriptions and constraints
- **Avenue 05 only** → Read skills, execute step-by-step instructions
- **Avenue 07 only** → Read path rules, follow directory-specific guidance
- **Any combination** → Load multiple avenues for redundancy

If one avenue is unavailable, others provide the same context.

<!-- section_id: "bae4da51-2ebc-433c-bc46-c343293606fa" -->
## File Organization

| Avenue | Location | Format | Count |
|--------|----------|--------|-------|
| 01 | `01_aalang/` | `.gab.jsonld` | ~50 per entity |
| 02 | `02_aalang_markdown_integration/` | `.integration.md` | ~50 per entity |
| 05 | `05_skills/` | `SKILL.md` | ~10-20 per entity |
| 04 | `04_@import_references/` | `.md` | ~20-30 total |
| 06 | `06_agents/` | `.agent.jsonld` | ~20 per layer |
| 07 | `07_path_specific_rules/` | `.md` | ~5-10 per directory |
| 08 | `08_hooks/` | `.sh` | ~5-10 per layer |

<!-- section_id: "21e89f67-52e2-4290-a875-b3c20e67b858" -->
## Next Steps

For each avenue, read the detailed subdirectory README (once created) to understand file organization and specific patterns used in each avenue.
