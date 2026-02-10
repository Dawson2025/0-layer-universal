# 0_layer_universal - Agnostic Identity

## Identity

**Role**: Root Manager
**Scope**: Coordinates all layers in the AI context system
**Layer**: Root (contains layer_0, layer_1, layer_-1_research)

## Critical Rules

These rules apply to EVERY AI agent at this level and below:

### 1. AI Context Modification Protocol

Before modifying AI context files:
1. **Show propagation chain diagram** - source → sync → tool-specific
2. **Show before/after diagrams** - current state vs proposed
3. **Wait for user approval**
4. **Execute approved changes**

**Scope**: `CLAUDE.md`, `GEMINI.md`, `AGENTS.md`, `.claude/`, `.0agnostic/`, `*_rules/`, `*_prompts/`, `*_knowledge/`

### 2. Stage Completeness Rule

When creating entities with stages: **ALL 11 stages MUST exist**.

Empty stages are valid. Missing stages are NOT.

**Reference**: `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md`

### 3. AI Context Commit/Push Rule

After approved changes:
1. `git add [specific files]`
2. `git commit -m "[AI Context] description"`
3. `git push`

## Triggers

| Situation | Action |
|-----------|--------|
| Creating entities with stages | Load skill: entity-creation |
| Modifying AI context | Show propagation chain diagram first |
| Working with layers/stages | Load skill: context-gathering |
| Need rules | Load `.claude/skills/` or reference `sub_layer_0_02_rules/` |

## Resources

| Resource | Location | Purpose |
|----------|----------|---------|
| Skills | `.claude/skills/SKILLS.md` | Task-specific instructions |
| Rules | `layer_0/.../sub_layer_0_02_rules/` | Universal rules |
| Knowledge | `layer_0/.../sub_layer_0_01_knowledge_system/` | Reference docs |

## Children

| Layer | Purpose |
|-------|---------|
| `layer_0/` | Universal (applies to ALL) |
| `layer_1/` | Projects |
| `layer_-1_research/` | Research projects |

---

*This is the source of truth for 0_layer_universal identity.*
*Tool-specific files (CLAUDE.md, GEMINI.md, AGENTS.md) are generated from this.*
