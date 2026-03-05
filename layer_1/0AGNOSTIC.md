# Layer 1 - Projects Context

## Identity

entity_id: "d39b1b99-83b0-4e73-96b4-22fd8b03e835"

You are an AI agent working within the layer_1 (projects) context. This layer contains project-specific content, features, and components.

## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Universal rules**: Inherit from `../.0agnostic/rules/`
- **Project features**: `layer_1_features/`
- **Project components**: `layer_1_components/`

## Key Behaviors

### Agent Context Loading
Each directory may have a `.gab.jsonld` agent definition with a matching `.integration.md` summary (same base name):
- e.g., `layer_N_orchestrator.gab.jsonld` → `layer_N_orchestrator.integration.md`
- Read the `.integration.md` for a quick summary; query the `.gab.jsonld` via jq for precise mode constraints
- `.integration.md` files are auto-generated — do not edit directly

### Context Discovery
Before starting any task:
1. Read this file (0AGNOSTIC.md)
2. Check `../.0agnostic/02_rules/` for universal rules
3. Check `.0agnostic/` for project-specific resources
4. Find the `.gab.jsonld` for your role and read its matching `.integration.md`
5. Read episodic memory if resuming work

### Episodic Memory
Record your work in `.0agnostic/episodic_memory/`:
- Create session files for significant work
- Update divergence.log when changing outputs
- Enable next session to continue seamlessly
- **Quick review**: Check `memory/episodic.md` (auto-memory topic file) for recent session history across all layers
- **After updating**: Run `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh` to sync episodic memory to auto-memory

### Multi-Agent Safety
When modifying shared outputs:
- Check for locks before writing
- Use atomic writes (temp file → rename)
- Log changes to divergence.log

## Triggers

| Situation | Action |
|-----------|--------|
| Need universal rules | Load `../.0agnostic/rules/` |
| Need project-specific rules | Load `.0agnostic/rules/` |
| Starting new session | Read `.0agnostic/episodic_memory/index.md` |
| Modifying outputs | Check `.locks/` first |
| Working on feature | Navigate to `layer_1_features/` |

## Quick Reference

- **Layer**: 1 (projects - specific to projects)
- **Inherits**: layer_0 universal rules
- **Stages**: 01-11 (request → archive workflow)
- **Memory**: Episodic (sessions preserve context)

## Stage Navigation

Stages are numbered 01-11 and represent workflow phases:

| Stage | Name | Purpose |
|-------|------|---------|
| 01 | Request Gathering | Clarify requirements |
| 02 | Research | Explore, gather info |
| 03 | Instructions | Define constraints |
| 04 | Planning | Break into subtasks |
| 05 | Design | Architecture |
| 06 | Development | Implementation |
| 07 | Testing | Verification |
| 08 | Criticism | Review |
| 09 | Fixing | Corrections |
| 10 | Current Product | Deliverable |
| 11 | Archives | History |

**To identify current stage**: Check your working directory path for `stage_*_NN_*` pattern.

**To find stage content**: Use `0INDEX.md` at `layer_N_99_stages/` directory.

---

*This is a tool-agnostic context file. See `.0agnostic/` for detailed resources.*
*Generate CLAUDE.md via: bash ../.0agnostic/agnostic-sync.sh .*

