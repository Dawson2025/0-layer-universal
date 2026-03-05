---
resource_id: "caa5cffa-a258-483f-bcb7-7454c8bb1ba0"
resource_type: "readme
output"
resource_name: "README"
---
# Stage 02: 0AGNOSTIC System Prompt Generation

## Purpose

**0AGNOSTIC System Prompt** is the authoritative **single source of truth** that converts stage reports and accumulated context into structured context for agents.

From the stage report, we synthesize:
- **Identity**: Who is this agent?
- **Scope**: What can this agent do?
- **Key Behaviors**: What should this agent do?
- **Triggers**: When should this context load?
- **Current Status**: What's the state right now?
- **Resources**: What tools/knowledge are available?

This becomes the `0AGNOSTIC.md` file at each entity level.

## When to Create

Create a 0AGNOSTIC system prompt **after stage reports are complete** and consolidated:

1. **Stage 04 (Design)** → Create entity-level 0AGNOSTIC.md
2. **Stage 05 (Planning)** → Update 0AGNOSTIC.md with planned structure
3. **Stage 06 (Development)** → Update 0AGNOSTIC.md with implemented resources
4. **Stage 10 (Current Product)** → Finalize 0AGNOSTIC.md as shipped context

## Location Convention

**At each level** (01-04 in propagation funnel):

```
{level}/05_0AGNOSTIC_system_prompt/
├── 0AGNOSTIC.md.template (optional: starter template)
├── 0AGNOSTIC_synthesis_guide.md (how to synthesize from stage reports)
└── 0AGNOSTIC_structure.md (canonical structure reference)
```

**In the layer-stage system** (actual context):

```
entity_root/
├── 0AGNOSTIC.md (source of truth for this entity)
├── 0INDEX.md (status dashboard, references 0AGNOSTIC.md)
└── .0agnostic/
    └── {resources loaded on-demand from 0AGNOSTIC.md}
```

## 0AGNOSTIC.md Structure

### Canonical Two-Section Format

```markdown
# Entity Name

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity
- Role
- Scope
- Parent reference
- Children (if any)

## Key Behaviors
- What this entity does
- Principles guiding behavior

## Triggers
- When to load this context
- Trigger conditions table

# ── Current Status ──

## Current Status
- **Phase**: description
- **Last Updated**: date
- Substantive summary (key findings, readiness, blockers)

---

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

# ── Current State ──

## Current State Detail
- Extended details
- Open items
- Handoff information

# ── References ──

## Navigation
- Parent path
- Child paths
- Key locations

## Resources
- Where to find what
- .0agnostic/ structure
- On-demand resources
```

### Key Rules

1. **STATIC CONTEXT**: Always loaded by agents. Keep lean (<400 lines total for chain).
2. **DYNAMIC CONTEXT**: Loaded on-demand. Can be comprehensive.
3. **Current Status** goes in STATIC, not DYNAMIC — agents see it every time.
4. **Sources are 0AGNOSTIC.md, NOT CLAUDE.md** — CLAUDE.md is auto-generated via agnostic-sync.sh

## Synthesis Process: Stage Report → 0AGNOSTIC.md

**Step 1: Extract Stage Report Sections**

From stage report, extract:

| Stage Report Section | → | 0AGNOSTIC.md Section |
|----------------------|---|----------------------|
| Executive Summary | → | Current Status |
| Key Findings | → | Key Behaviors (updated) |
| Key Decisions | → | Identity / Triggers (updated) |
| Outputs | → | Resources / References (updated) |
| Open Items | → | DYNAMIC: Current State Detail |
| Handoff Readiness | → | DYNAMIC: Handoff |

**Step 2: Structure as 0AGNOSTIC.md**

Example from CSE 300 Grade Strategy:

```markdown
# layer_3_subx2_project_professional_readiness — CSE 300

# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity
- **Role**: Course project manager for CSE 300
- **Scope**: All coursework including learning activities, status updates, major assignments, final project, participation
- **Parent**: `../../0AGNOSTIC.md` (layer_2_subx2_project_computer_science)

## Key Behaviors

### Course Structure
CSE 300 uses **percentage-based grading** — points accumulate, total percentage determines letter grade.

**Total Points**: 1,082 across 30 assignments

### Assignment Workflow
1. Weekly Learning Activities → auto-graded
2. Status Updates → auto-graded
3. Major Assignments → rubric-graded
4. Final Project → rubric-graded
5. Participation → instructor-graded

## Triggers

Load this context when:
- User mentions: professional readiness, CSE 300, career prep, resume, cover letter, LinkedIn
- Working on: Any CSE 300 coursework

## Skills

| Skill | Purpose |
|-------|---------|
| `/cse300-dashboard` | Live Canvas-powered grade dashboard |

# ── Current Status ──

## Current Status

**Phase**: Active — entity infrastructure created, grading model documented (1,082 pts), dashboard skill created | **Last Updated**: 2026-02-26

Percentage-based grading model documented. 30 assignments mapped. Dashboard skill inherits from layer_2 trajectory stores. As of 2026-02-26, post-Week 7 (final project period due 2026-02-28).

---

# ═══ DYNAMIC CONTEXT (loaded on-demand) ═══

[... full details ...]
```

**Step 3: Validate & Finalize**

Checklist before committing 0AGNOSTIC.md:

- ✅ Identity section clear (role, scope, parent, children)
- ✅ Key Behaviors describe WHAT agent does, not HOW
- ✅ Triggers table covers all load conditions
- ✅ Current Status is substantive (>2 lines, includes scope + key findings)
- ✅ Resources section lists all .0agnostic/ content
- ✅ Parent chain is correct (can traverse to root)
- ✅ All URLs/paths are valid
- ✅ Grammar and clarity reviewed

**Step 4: Run agnostic-sync.sh**

```bash
cd /entity/root
bash /.0agnostic/agnostic-sync.sh .
```

This generates:
- CLAUDE.md (from STATIC context)
- AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules (tool-specific)
- .github/copilot-instructions.md (GitHub Copilot config)

## Progressive Disclosure

0AGNOSTIC.md implements **four-level progressive disclosure**:

1. **Trigger**: When agent needs context
2. **STATIC summary**: 200-line snapshot (Identity + Behaviors + Triggers + Current Status)
3. **DYNAMIC detail**: Full context on demand (Current State + Resources + Navigation)
4. **Resource documents**: Protocols, knowledge, rules (`.0agnostic/` on-demand)

## Phase in Propagation Funnel

0AGNOSTIC system prompts are the **translation layer** between:
- **Upstream**: Stage reports (hierarchical work outputs)
- **Downstream**: AI app prompts (tool-specific formats)

0AGNOSTIC.md is the **canonical form** that cascades to all AI apps via agnostic-sync.sh and .1merge system.

## See Also

- `.0agnostic/01_knowledge/layer_stage_system/stage_guides/STAGE_AGENT_TEMPLATE.md` — Template for new entities
- Agnostic Update Protocol → How to keep 0AGNOSTIC.md in sync
- Level 03 (Entity Reports) → Customizes 0AGNOSTIC.md per entity
- Level 04 (AI App Ports) → Transpiles 0AGNOSTIC.md to tool-specific formats
