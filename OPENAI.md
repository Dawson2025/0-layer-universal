# OpenAI Context


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

### 4. Submodule Integrity Protocol

When any nested repository exists in a child path:
1. The parent repository MUST track it as a real submodule (mode `160000` gitlink) and MUST have a matching entry in `.gitmodules`.
2. Never leave a gitlink without `.gitmodules` mapping. This breaks recursive submodule operations.
3. Commit/push order is always bottom-up:
   - deepest child repo first
   - then each parent repo submodule pointer
   - root repo last
4. Before ending a session, run:
   - `git submodule status --recursive`
   - `find . -name .git | sed 's#/.git$##'` (sanity check for unexpected nested repos)
5. Any nested repo discovered without mapping must be either:
   - properly registered as a submodule, or
   - de-initialized as a standalone repo and converted to regular tracked files.

## Triggers

| Situation | Action |
|-----------|--------|
| Creating entities with stages | Load skill: entity-creation |
| Modifying AI context | Show propagation chain diagram first |
| Modifying `.0agnostic/` files | Follow agnostic update protocol: `.0agnostic/02_rules/static/agnostic_update_protocol.md` |
| Working with layers/stages | Load skill: context-gathering |
| Need rules | Load `.claude/skills/` or reference `.0agnostic/02_rules/` |

## Resources

| Resource | Location | Purpose |
|----------|----------|---------|
| Skills | `.claude/skills/SKILLS.md` | Task-specific instructions |
| Rules | `.0agnostic/02_rules/` | Universal rules |
| Update Protocol | `.0agnostic/02_rules/static/agnostic_update_protocol.md` | Sync chain for .0agnostic/ changes |
| Knowledge | `.0agnostic/01_knowledge/` | Reference docs |

## Children

| Layer | Purpose |
|-------|---------|
| `layer_0/` | Universal (applies to ALL) |
| `layer_1/` | Projects |
| `layer_-1_research/` | Research projects |

---

*This is the source of truth for 0_layer_universal identity.*
*Tool-specific files (CLAUDE.md, GEMINI.md, AGENTS.md) are generated from this.*

## Mandatory Checkpoint Cadence

1. Commit and push for each new item.
2. Commit and push for each update.
3. In submodule chains, push deepest children first, then parent pointers to root.


Active chain map (school -> module_03):
- `0_layer_universal` tracks `layer_1/layer_1_projects/layer_1_project_school` as submodule.
- `layer_1_project_school` currently contains one active nested gitlink at `.../school-machine-learning-module03-teamwork`.
- If any additional nested repos appear, they must be declared in `.gitmodules` at the same repository level before commit/push.

## Promoted Rules

| When | Rule |
|------|------|
| Modifying any file in .0agnostic/ | When modifying .0agnostic/ files, also update 0AGNOSTIC.md and run agnostic-sync.sh. Full protocol: .0agnostic/02_rules/static/agnostic_update_protocol.md |
| Any turn that modifies files | On every turn with file changes, report all Added/Updated/Moved/Removed files with full absolute paths at end of response. Full rule: .0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING.md |


## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
