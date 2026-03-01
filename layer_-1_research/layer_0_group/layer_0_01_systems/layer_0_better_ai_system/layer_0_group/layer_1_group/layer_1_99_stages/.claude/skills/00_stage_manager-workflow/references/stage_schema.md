# Stage Directory Schema

Template for stage directory structure.

## Standard Stage Structure

```
stage_-1_XX_name/
├── CLAUDE.md                     # Stage context and purpose
├── .claude/
│   ├── agents/
│   │   └── XX_name-agent.md      # Stage-specific agent
│   ├── commands/
│   │   ├── XX_name-complete.md   # Mark stage complete
│   │   └── XX_name-status.md     # Check stage status
│   ├── hooks/
│   │   ├── hooks.json
│   │   └── scripts/
│   │       └── on-stage-enter.sh
│   ├── scripts/
│   │   └── README.md
│   ├── settings.json
│   └── skills/
│       └── XX_name-workflow/
│           ├── SKILL.md
│           └── references/
│               └── README.md
├── hand_off_documents/
│   ├── README.md
│   ├── incoming/
│   │   └── README.md
│   └── outgoing/
│       └── README.md
└── outputs/
    └── (stage deliverables)
```

## CLAUDE.md Template

```markdown
# stage_-1_XX_name

## Purpose
[What this stage accomplishes]

## Structure
- `.claude/` - AI agent configurations
- `hand_off_documents/` - Stage transitions
- `outputs/` - Stage deliverables

## Context
- **Layer**: -1
- **Stage**: XX - name
- **Project**: better_ai_system

## Workflow
When working in this stage:
1. Check `hand_off_documents/incoming/` for context
2. Perform stage activities
3. Place deliverables in `outputs/`
4. Prepare `hand_off_documents/outgoing/` for next stage

## Incoming From
- **Stage**: XX-1 (previous_stage_name)
- **Expected**: [What should be received]

## Outgoing To
- **Stage**: XX+1 (next_stage_name)
- **Deliverables**: [What should be passed]
```

## settings.json Template

```json
{
  "stage": "XX_name",
  "layer": "-1",
  "project": "better_ai_system",
  "status": "active"
}
```

## Agent Template

```markdown
---
name: XX_name-agent
description: Specialized agent for [stage purpose]
tools: Read, Glob, [additional tools]
model: sonnet
color: [color]
---

# XX_name Agent

You are a specialized agent for the **XX_name** stage.

## Purpose
[Stage purpose]

## Your Role
- Focus on XX_name activities
- Use outputs/ for deliverables
- Check hand_off_documents/ for context

## Stage-Specific Guidelines
- [Guideline 1]
- [Guideline 2]
```

## Skill Template

```markdown
---
name: XX_name-workflow
description: Workflow skill for [stage purpose]
version: 1.0.0
---

# XX_name Workflow Skill

## When to Use
- When entering the XX_name stage
- When performing XX_name activities

## Workflow Steps
1. **Initialize**: Check incoming handoff
2. **Execute**: Perform stage work
3. **Document**: Place outputs
4. **Handoff**: Prepare for next stage

## Key Files
- `outputs/` - Deliverables
- `hand_off_documents/` - Context
```
