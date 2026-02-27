# Subsystem 02: AI App Personal System Prompts

## Purpose

**AI App Personal System Prompts** is how we port **0AGNOSTIC.md content** into each AI application's native **system prompt file format**.

This enables:
- Each AI app (Claude, Cursor, Gemini, GitHub Copilot, etc.) loads appropriate context from its own system prompt file
- Single source of truth (0AGNOSTIC.md) automatically propagates to 6+ tool-specific formats
- Tool-specific formatting: each system prompt follows its platform's conventions
- Automated generation: agnosync creates all system prompts from 0AGNOSTIC.md

## System Prompt Files

Each AI app has its own personal system prompt file:

| AI App | System Prompt File | Format | Location |
|--------|-------------------|--------|----------|
| **Claude Code** | `CLAUDE.md` | Markdown | Entity root |
| **Multi-Agent** | `AGENTS.md` | YAML + Markdown | Entity root |
| **Google Gemini** | `GEMINI.md` | Markdown | Entity root |
| **OpenAI/Codex** | `OPENAI.md` | Markdown | Entity root |
| **Cursor IDE** | `.cursorrules` | Plain text | Entity root |
| **GitHub Copilot** | `.github/copilot-instructions.md` | Markdown | `.github/` |

### What Goes In Each File

All system prompt files contain the same **core content** from 0AGNOSTIC.md STATIC CONTEXT section:

1. **Identity**: Role, scope, parent, children
2. **Key Behaviors**: What the agent should do
3. **Triggers**: When to load this context
4. **Triggers Table**: Specific trigger conditions
5. **Resources**: Where to find knowledge/rules/skills
6. **Navigation**: How to traverse hierarchy
7. **Current Status**: Brief status summary

### Differences Per Tool

Each tool's system prompt is formatted for that platform's conventions:

**CLAUDE.md** (Claude Code):
```markdown
# Claude Code Context

## Identity
You are an agent at **Layer X**...

## Navigation
- Detailed resources: `.0agnostic/` folder
- ...

## Key Behaviors
...

## Triggers
...

---
*Auto-generated from 0AGNOSTIC.md*
```

**AGENTS.md** (Multi-Agent):
```yaml
# Multi-Agent Context

agents:
  - name: Research Agent
    role: ...
    scope: ...
    triggers:
      - condition: ...
        action: ...
```

**.cursorrules** (Cursor IDE):
```
You are an agent at Layer X.

Role: [role from Identity]
Scope: [scope from Identity]

Key Behaviors:
- [behavior 1]
- [behavior 2]

Triggers:
- When [trigger condition] → [action]
```

**.github/copilot-instructions.md** (GitHub Copilot):
```markdown
# GitHub Copilot Instructions

## Identity
You are [role] for [scope].

## When to Help
- [trigger 1]
- [trigger 2]

## Resources
- Rules: .github/rules/
- ...
```

## Generation Process: 0AGNOSTIC.md → System Prompts

### Step 1: Extract STATIC CONTEXT

From 0AGNOSTIC.md, extract:

```markdown
# ═══ STATIC CONTEXT (always loaded) ═══

# ── Entity Definition ──

## Identity
...

## Key Behaviors
...

## Triggers
...

# ── Current Status ──

## Current Status
...
```

(Ignore DYNAMIC CONTEXT — that's for on-demand reading)

### Step 2: Transform to Tool Format

For each tool, transform STATIC content to its native format:

**Template Transformation** (CLAUDE.md):

```
0AGNOSTIC.md STATIC CONTEXT
            ↓
Remove markdown headers (# ═══, # ──)
            ↓
Keep markdown body (paragraphs, tables, lists)
            ↓
Add tool header ("# Claude Code Context")
            ↓
Reorder for readability (Identity, Navigation, Behaviors, Triggers, Resources)
            ↓
Add footer ("*Auto-generated from 0AGNOSTIC.md*")
            ↓
CLAUDE.md (final system prompt)
```

### Step 3: Apply Three-Tier Merge

**Tier 0 (Synced)**: agnosync-generated content from 0AGNOSTIC.md

```markdown
# Claude Code Context

## Identity
You are an agent at Layer 4 (Project), Project: Professional Readiness (CSE 300)...

## Key Behaviors
CSE 300 uses percentage-based grading...

## Triggers
| Situation | Action |
|-----------|--------|
| User asks about grade status | Load canvas_grade_dashboard_trajectory.md |

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
```

**Tier 1 (Overrides)**: Tool-specific customizations (from .1merge/)

`.1merge/.1claude_merge/1_overrides/tool_boilerplate.md`:
```markdown
# CLAUDE-SPECIFIC TEMPLATE

## Additional Context for Claude Code
- Canvas MCP server location: ...
- Required environment variables: ...
- Keyboard shortcuts for this context: ...
```

**Tier 2 (Additions)**: Custom enhancements

`.1merge/.1claude_merge/2_additions/tool_additions.md`:
```markdown
# Claude Code Enhancements

## Custom Skills
- /calc-dashboard — specific to MATH 119
- /cse300-dashboard — specific to CSE 300

## Keyboard Bindings
- Ctrl+Shift+G — open grade dashboard
```

**Final Merge Result**:
```
Tier 0 (base) + Tier 1 (overrides) + Tier 2 (additions) = CLAUDE.md (final)
```

## Example: CSE 300 CLAUDE.md

```markdown
# Claude Code Context

## Identity

You are an agent at **Layer 4** (Project), **Project**: Professional Readiness (CSE 300).

- **Role**: Course project manager for CSE 300
- **Scope**: All coursework (learning activities, assignments, final project, participation)
- **Parent**: `../../0AGNOSTIC.md` (layer_3_subx2_project_computer_science)

## Key Behaviors

### Course Structure

CSE 300 uses **percentage-based grading** — points accumulate, total percentage determines letter grade.

**Total Points**: 1,082 across 30 assignments

**Categories**:
- Weekly Learning Activities (7 × 10 pts = 70 pts)
- Status Updates (7 × 5 pts = 35 pts)
- Major Assignments (7 × 100 pts = 700 pts)
- Final Project (1 × 200 pts = 200 pts)
- Participation (1 × 77 pts = 77 pts)

### Assignment Workflow

1. Weekly Learning Activities → Complete quiz → auto-graded
2. Status Updates → Submit video/text → auto-graded
3. Major Assignments → Upload document → rubric-graded
4. Final Project → Portfolio → rubric-graded
5. Participation → Instructor awards throughout course

## Triggers

Load this context when:
- User mentions: professional readiness, CSE 300, career prep, resume, cover letter, LinkedIn
- Working on: Any CSE 300 coursework
- Entering: `layer_4_subx3_project_professional_readiness/`

| Trigger | Action |
|---------|--------|
| User asks about grade status, progress, or what to work on next | Invoke `/cse300-dashboard` skill |

## Skills

| Skill | Location | Purpose |
|-------|----------|---------|
| `/cse300-dashboard` | `.claude/skills/cse300-dashboard/SKILL.md` | Live Canvas-powered grade dashboard |

## Resources

| Resource | Location | Purpose |
|----------|----------|---------|
| Grading model | `.0agnostic/01_knowledge/course_info/grading_model.md` | Percentage-based, 1,082 pts |
| Assignment patterns | `.0agnostic/01_knowledge/course_info/assignment_categories.yaml` | 30 assignments mapped |
| Schedule | `.0agnostic/01_knowledge/course_info/schedule.md` | 7-week calendar |

---

*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
```

## Format Specifications

### CLAUDE.md Format

- **Type**: Markdown
- **Max lines**: 400 (target, flexible)
- **Sections**: Identity, Navigation, Key Behaviors, Triggers, Resources, Current Status
- **Footer**: `*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*`

### .cursorrules Format

- **Type**: Plain text (no markdown)
- **Line length**: Max 100 chars (IDE constraint)
- **Sections**: Imperative statements ("You are", "When", "Do this")
- **No footer** (Cursor doesn't render it)

### AGENTS.md Format

- **Type**: YAML + Markdown hybrid
- **Structure**: Agents list with mode/actor definitions
- **Metadata**: agent_id, mode, actor, trigger, transition, constraint

### .github/copilot-instructions.md Format

- **Type**: Markdown
- **Sections**: Brief (instructions must be concise)
- **Focus**: When/how Copilot should help in this repo
- **Length**: 100-200 lines max

## Validation Checklist

After generating system prompt files:

- ✅ All 6 system prompt files present (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md, .cursorrules, .github/copilot-instructions.md)
- ✅ Each file contains STATIC CONTEXT from 0AGNOSTIC.md
- ✅ Each file formatted for its tool (markdown, YAML, plain text)
- ✅ Identity section clear (role, scope, parent)
- ✅ Key Behaviors describe what agent should do
- ✅ Triggers table covers all conditions
- ✅ Resources point to .0agnostic/ folders
- ✅ Current Status included (substantive, >2 lines)
- ✅ No DYNAMIC CONTEXT included (on-demand only)
- ✅ All paths/references valid
- ✅ Grammar and clarity reviewed
- ✅ Footer present (if tool supports)
- ✅ Files are readable by their tools

## Propagation Chain

When you edit `0AGNOSTIC.md`:

```
1. User edits 0AGNOSTIC.md (source of truth)
2. User runs: bash .0agnostic/agnosync.sh
3. Script extracts STATIC CONTEXT from 0AGNOSTIC.md
4. For each tool:
   a. Apply tool template transformation
   b. Read .1merge/.1{tool}_merge/1_overrides/tool_boilerplate.md (Tier 1)
   c. Read .1merge/.1{tool}_merge/2_additions/tool_additions.md (Tier 2)
   d. Merge: Tier 0 + Tier 1 + Tier 2 → {TOOL}.md
5. Commit and push all {TOOL}.md files
6. All AI apps load updated context from their respective system prompt files
```

## Phase in Propagation Funnel

AI App Personal System Prompts are the **final output** of the propagation funnel:

- **Input**: 0AGNOSTIC.md (canonical entity context)
- **Process**: agnosync + .1merge three-tier system
- **Output**: 6 tool-specific system prompt files

Without this subsystem:
- Context would be in 0AGNOSTIC.md but unavailable to tools
- Each tool would need manual prompt setup
- Updates wouldn't propagate to tools

With this subsystem:
- 0AGNOSTIC.md automatically becomes context for all tools
- Changes propagate instantly when agnosync runs
- Tool-specific customizations isolated in .1merge
- Single source of truth (0AGNOSTIC.md)

## See Also

- 0AGNOSTIC.md → Source of truth for all system prompts
- .1merge/ → Tool-specific overrides and additions
- `agnostic-sync.sh` → Script that generates all system prompts
- AI App Context Systems → How folder structure is mirrored to tools
