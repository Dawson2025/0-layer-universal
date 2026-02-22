# Layer -1 - Research Context

## Identity
You are an AI agent working within the layer_-1 (research) context. This layer contains research projects, experiments, and exploratory work.

## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Universal rules**: Inherit from `../.0agnostic/rules/`
- **Research projects**: Direct children of this layer
- **Active research**: Check 0INDEX.md for current projects

## Key Behaviors

### Agent Context Loading
Each directory may have a `.gab.jsonld` agent definition with a matching `.integration.md` summary (same base name):
- e.g., `agent_orchestrator.gab.jsonld` → `agent_orchestrator.integration.md`
- Read the `.integration.md` for a quick summary; query the `.gab.jsonld` via jq for precise mode constraints
- `.integration.md` files are auto-generated — do not edit directly

### Context Discovery
Before starting any task:
1. Read this file (0AGNOSTIC.md)
2. Check `../.0agnostic/02_rules/` for universal rules
3. Read project-specific context in research directories
4. Find the `.gab.jsonld` for your role and read its matching `.integration.md`
5. Read episodic memory if resuming work

### Episodic Memory
Record your work in `.0agnostic/episodic_memory/`:
- Create session files for significant work
- Update divergence.log when changing outputs
- Enable next session to continue seamlessly
- **Quick review**: Check `memory/episodic.md` (auto-memory topic file) for recent session history across all layers
- **After updating**: Run `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh` to sync episodic memory to auto-memory

### Research Protocol
Research projects follow stages 01-11 (see Stage Navigation below).

## Triggers

| Situation | Action |
|-----------|--------|
| Need universal rules | Load `../.0agnostic/rules/` |
| Starting research | Navigate to project's stage_-1_02_research |
| Designing solutions | Navigate to project's stage_-1_04_design |
| Starting new session | Read `.0agnostic/episodic_memory/index.md` |

## Active Research Projects

- **layer_-1_better_ai_system**: SHIMI concepts, agent memory, multi-agent sync

## Quick Reference

- **Layer**: -1 (research - experimental work)
- **Inherits**: layer_0 universal rules
- **Stages**: 01-11 (research workflow)
- **Memory**: Episodic (sessions preserve context)

## Stage Navigation

Stages are numbered 01-11 and represent workflow phases:

| Stage | Name | Purpose |
|-------|------|---------|
| 01 | Request Gathering | Clarify requirements |
| 02 | Research | Explore, gather info |
| 03 | Instructions | Define constraints |
| 04 | Design | Architecture |
| 05 | Planning | Break into subtasks |
| 06 | Development | Implementation |
| 07 | Testing | Verification |
| 08 | Criticism | Review |
| 09 | Fixing | Corrections |
| 10 | Current Product | Deliverable |
| 11 | Archives | History |

**To identify current stage**: Check your working directory path for `stage_*_NN_*` pattern.

**To find stage content**: Use `0INDEX.md` at project's `layer_-1_99_stages/` directory.

---

*This is a tool-agnostic context file. See `.0agnostic/` for detailed resources.*

