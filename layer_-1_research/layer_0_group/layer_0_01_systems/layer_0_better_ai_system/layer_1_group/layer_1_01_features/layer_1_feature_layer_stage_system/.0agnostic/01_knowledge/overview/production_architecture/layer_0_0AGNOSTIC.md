---
resource_id: "77416e41-f267-497e-8e76-8acb75a1f4d9"
resource_type: "knowledge"
resource_name: "layer_0_0AGNOSTIC"
---
# Layer 0 - Universal Context

<!-- section_id: "2b752fc3-5f82-47db-9a6d-300f747126d8" -->
## Identity
You are an AI agent working within the layer_0 (universal) context. This layer contains rules, prompts, and knowledge that apply across ALL projects.

<!-- section_id: "4ddce6b4-a547-4ea2-b2d2-6a6fee31ad2d" -->
## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Rules**: `.0agnostic/rules/`
- **Prompts**: `.0agnostic/prompts/`
- **Knowledge**: `.0agnostic/knowledge/`
- **Agents**: `.0agnostic/agents/`

<!-- section_id: "285ba593-3ec0-4846-8c97-09ba5e28effe" -->
## Key Behaviors

<!-- section_id: "d3ba5cda-dcb8-4b35-909a-af5fce0fdb14" -->
### Context Discovery
Before starting any task, traverse the context hierarchy:
1. Read this file (0AGNOSTIC.md)
2. Check `.0agnostic/` for detailed resources if needed
3. Follow layer-stage framework conventions

<!-- section_id: "c30b2588-0ffc-4476-bd2c-2f038d9fef7d" -->
### Episodic Memory
Record your work in `outputs/episodic/`:
- Create session files for significant work
- Update divergence.log when changing outputs
- Enable next session to continue seamlessly

<!-- section_id: "874b8a3f-5d71-441a-9def-f99a7e3cda5d" -->
### Multi-Agent Safety
When modifying shared outputs:
- Check for locks before writing
- Use atomic writes (temp file → rename)
- Log changes to divergence.log

<!-- section_id: "4df63c0c-0059-4339-a5c4-ad46ef15ac10" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Need detailed rules | Load `.0agnostic/rules/` |
| Need implementation prompts | Load `.0agnostic/prompts/` |
| Need reference knowledge | Load `.0agnostic/knowledge/` |
| Need agent definitions | Load `.0agnostic/agents/` |
| Starting new session | Read `outputs/episodic/index.md` |
| Modifying outputs | Check `.locks/` first |

<!-- section_id: "7e919160-51a8-456d-82e9-908b04597930" -->
## Agnostic System

This directory uses the agnostic system for tool-independent context:

- **Source of truth**: This `0AGNOSTIC.md` file — edit this, NOT `CLAUDE.md` (which is auto-generated)
- **On-demand resources**: `.0agnostic/` contains rules, skills, agents, knowledge, scripts
- **After changes**: Run `agnostic-sync.sh` to regenerate tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md)
- **Tool overrides**: `.1merge/` (if present) provides tool-specific overrides via 3-tier merge (synced → overrides → additions)

<!-- section_id: "1d7a87df-104b-45b3-9d1f-8fca38d89c26" -->
## Quick Reference

- **Layer**: 0 (universal - applies everywhere)
- **Stages**: 01-11 (request → archive workflow)
- **Memory**: Episodic (sessions preserve context)
- **Sync**: File locking + hash tracking

<!-- section_id: "82d7802b-c7a0-4966-a512-5b411eab182a" -->
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

