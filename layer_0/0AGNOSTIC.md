---
resource_id: "2ed456db-f36e-48f9-8568-9d0c1dba8803"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# Layer 0 - Universal Context

<!-- section_id: "e623545a-0723-4b6b-8a4e-ac1bed5e0d1d" -->
## Identity

entity_id: "aa24709f-a54e-43db-ac3b-f2b61b2bbaac"

You are an AI agent working within the layer_0 (universal) context. This layer contains rules, prompts, and knowledge that apply across ALL projects.

<!-- section_id: "03f4402c-f5ac-433a-8cd0-4a5508dba2d3" -->
## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Rules**: `.0agnostic/rules/`
- **Prompts**: `.0agnostic/prompts/`
- **Knowledge**: `.0agnostic/knowledge/`
- **Agents**: `.0agnostic/agents/`

<!-- section_id: "79b79b45-0d65-49f6-a2d7-b73326690b89" -->
## Key Behaviors

<!-- section_id: "cc9a7e7d-5959-4ac5-9a24-290623cac711" -->
### Context Discovery
Before starting any task, traverse the context hierarchy:
1. Read this file (0AGNOSTIC.md)
2. Check `.0agnostic/` for detailed resources if needed
3. Follow layer-stage framework conventions

<!-- section_id: "b1340897-fdcb-4869-8f4b-2f6c9ec1d801" -->
### Episodic Memory
Record your work in `.0agnostic/episodic_memory/`:
- Create session files for significant work
- Update divergence.log when changing outputs
- Enable next session to continue seamlessly

<!-- section_id: "3d89ac6d-f3ad-4221-87b4-f10533a43812" -->
### Multi-Agent Safety
When modifying shared outputs:
- Check for locks before writing
- Use atomic writes (temp file → rename)
- Log changes to divergence.log

<!-- section_id: "3eba7537-7a6a-4e0e-83e3-c17a0c0924e4" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Need detailed rules | Load `.0agnostic/rules/` |
| Need implementation prompts | Load `.0agnostic/prompts/` |
| Need reference knowledge | Load `.0agnostic/knowledge/` |
| Need agent definitions | Load `.0agnostic/agents/` |
| Starting new session | Read `.0agnostic/episodic_memory/index.md` |
| Modifying outputs | Check `.locks/` first |

<!-- section_id: "96c68067-c855-4a3e-bee4-89d4a98a5803" -->
## Agnostic System

This directory uses the agnostic system for tool-independent context:

- **Source of truth**: This `0AGNOSTIC.md` file — edit this, NOT `CLAUDE.md` (which is auto-generated)
- **On-demand resources**: `.0agnostic/` contains rules, skills, agents, knowledge, scripts
- **After changes**: Run `agnostic-sync.sh` to regenerate tool-specific files (CLAUDE.md, AGENTS.md, GEMINI.md, OPENAI.md)
- **Tool overrides**: `.1merge/` (if present) provides tool-specific overrides via 3-tier merge (synced → overrides → additions)

<!-- section_id: "16fd2a16-e29b-44cf-95c9-7624d1e8ea2c" -->
## Quick Reference

- **Layer**: 0 (universal - applies everywhere)
- **Stages**: 01-11 (request → archive workflow)
- **Memory**: Episodic (sessions preserve context)
- **Sync**: File locking + hash tracking

<!-- section_id: "58b53b60-a470-4042-8bbb-5df60a5143b5" -->
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

