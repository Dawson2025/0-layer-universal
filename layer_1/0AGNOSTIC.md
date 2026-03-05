---
resource_id: "461b3727-1d41-4c7f-acfb-76ff379ee383"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# Layer 1 - Projects Context

<!-- section_id: "d2e71817-26bc-428c-908d-24202e596e94" -->
## Identity

entity_id: "d39b1b99-83b0-4e73-96b4-22fd8b03e835"

You are an AI agent working within the layer_1 (projects) context. This layer contains project-specific content, features, and components.

<!-- section_id: "040157b6-d00c-4116-b130-88790868d4f9" -->
## Navigation
- **Detailed resources**: `.0agnostic/` folder
- **Universal rules**: Inherit from `../.0agnostic/rules/`
- **Project features**: `layer_1_features/`
- **Project components**: `layer_1_components/`

<!-- section_id: "81b9d968-66e5-49a0-956a-044da301e7bc" -->
## Key Behaviors

<!-- section_id: "6c099288-0919-4946-8e93-47005eabf2a5" -->
### Agent Context Loading
Each directory may have a `.gab.jsonld` agent definition with a matching `.integration.md` summary (same base name):
- e.g., `layer_N_orchestrator.gab.jsonld` → `layer_N_orchestrator.integration.md`
- Read the `.integration.md` for a quick summary; query the `.gab.jsonld` via jq for precise mode constraints
- `.integration.md` files are auto-generated — do not edit directly

<!-- section_id: "a3a8eccd-3743-4349-9b3b-7b590cd3abca" -->
### Context Discovery
Before starting any task:
1. Read this file (0AGNOSTIC.md)
2. Check `../.0agnostic/02_rules/` for universal rules
3. Check `.0agnostic/` for project-specific resources
4. Find the `.gab.jsonld` for your role and read its matching `.integration.md`
5. Read episodic memory if resuming work

<!-- section_id: "ec405fac-d2b8-400a-9fb5-1ac8422f5307" -->
### Episodic Memory
Record your work in `.0agnostic/episodic_memory/`:
- Create session files for significant work
- Update divergence.log when changing outputs
- Enable next session to continue seamlessly
- **Quick review**: Check `memory/episodic.md` (auto-memory topic file) for recent session history across all layers
- **After updating**: Run `.0agnostic/01_knowledge/layer_stage_system/resources/tools/episodic-sync.sh` to sync episodic memory to auto-memory

<!-- section_id: "58e982bb-1f92-4e69-8bfd-a355a43234df" -->
### Multi-Agent Safety
When modifying shared outputs:
- Check for locks before writing
- Use atomic writes (temp file → rename)
- Log changes to divergence.log

<!-- section_id: "1cd46d5a-9c13-4586-a24e-8683da847e4f" -->
## Triggers

| Situation | Action |
|-----------|--------|
| Need universal rules | Load `../.0agnostic/rules/` |
| Need project-specific rules | Load `.0agnostic/rules/` |
| Starting new session | Read `.0agnostic/episodic_memory/index.md` |
| Modifying outputs | Check `.locks/` first |
| Working on feature | Navigate to `layer_1_features/` |

<!-- section_id: "22f3b3a8-4080-42f4-9e37-6a35761cc29e" -->
## Quick Reference

- **Layer**: 1 (projects - specific to projects)
- **Inherits**: layer_0 universal rules
- **Stages**: 01-11 (request → archive workflow)
- **Memory**: Episodic (sessions preserve context)

<!-- section_id: "c4e29272-f8d7-4a33-bfca-aeb3e7cec12c" -->
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

