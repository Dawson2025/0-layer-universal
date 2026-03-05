# Layer 0 - Universal Context

## Identity

entity_id: "aa24709f-a54e-43db-ac3b-f2b61b2bbaac"

You are an AI agent working within the layer_0 (universal) context. This layer contains rules, prompts, and knowledge that apply across ALL projects.

## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Rules**: `.0agnostic/rules/`
- **Prompts**: `.0agnostic/prompts/`
- **Knowledge**: `.0agnostic/knowledge/`
- **Agents**: `.0agnostic/agents/`

## Key Behaviors

### Context Discovery
Before starting any task, traverse the context hierarchy:
1. Read this file (0AGNOSTIC.md)
2. Check `.0agnostic/` for detailed resources if needed
3. Follow layer-stage framework conventions

### Episodic Memory
Record your work in `.0agnostic/episodic_memory/`:
- Create session files for significant work
- Update divergence.log when changing outputs
- Enable next session to continue seamlessly

### Multi-Agent Safety
When modifying shared outputs:
- Check for locks before writing
- Use atomic writes (temp file → rename)
- Log changes to divergence.log

## Triggers

| Situation | Action |
|-----------|--------|
| Need detailed rules | Load `.0agnostic/rules/` |
| Need implementation prompts | Load `.0agnostic/prompts/` |
| Need reference knowledge | Load `.0agnostic/knowledge/` |
| Need agent definitions | Load `.0agnostic/agents/` |
| Starting new session | Read `.0agnostic/episodic_memory/index.md` |
| Modifying outputs | Check `.locks/` first |

## Agnostic System

This directory uses the agnostic system for tool-independent context:

- **Source of truth**: This `0AGNOSTIC.md` file — edit this, NOT `CLAUDE.md` (which is auto-generated)
- **On-demand resources**: `.0agnostic/` contains rules, skills, agents, knowledge, scripts
- **After changes**: Run `agnostic-sync.sh` to regenerate tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md)
- **Tool overrides**: `.1merge/` (if present) provides tool-specific overrides via 3-tier merge (synced → overrides → additions)

## Quick Reference

- **Layer**: 0 (universal - applies everywhere)
- **Stages**: 01-11 (request → archive workflow)
- **Memory**: Episodic (sessions preserve context)
- **Sync**: File locking + hash tracking

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
*Generated CLAUDE.md and other tool-specific files via `agnostic-sync.sh`.*

