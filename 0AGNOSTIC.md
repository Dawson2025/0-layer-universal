---
resource_id: "6512d4dd-e3d9-4286-b7c4-48d54da4cf6d"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# 0_layer_universal - Agnostic Identity

## Identity

**Role**: Root Manager
**Scope**: Coordinates all layers in the AI context system
**Layer**: Root (contains layer_0, layer_1, layer_-1_research)

## Critical Rules

These rules apply to EVERY AI agent at this level and below:

### 1. Filesystem Change Visualization Protocol

**Two tiers** — show proposed changes before executing:

**Tier 1 (AI Context — strict)**: Before modifying AI context files, show propagation chain diagram, store proposal in registry, wait for approval.
**Scope**: `0AGNOSTIC.md`, `.0agnostic/`, `.1merge/`, `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `OPENAI.md`, `.claude/`, `.cursor/`, `*_rules/`, `*_prompts/`, `*_knowledge/`, `status.json`, `*.gab.jsonld`, `*.integration.md`

**Tier 2 (General Filesystem — standard)**: Before structural filesystem changes (2+ dirs, 3+ files, reorganization), show before/after diagram, wait for approval.
**Exemptions**: Single file edits, single file creation, appends.

**Full rule**: `.0agnostic/02_rules/0_every_api_request/AI_CONTEXT_MODIFICATION_PROTOCOL/AI_CONTEXT_MODIFICATION_PROTOCOL.md`

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
| Creating, updating, or finding duplicate documentation | Load rule: `.0agnostic/02_rules/documentation_deduplication_rule.md` |
| Creating entities with stages | Load skill: entity-creation |
| Modifying AI context | Show propagation chain diagram first |
| Modifying `.0agnostic/` files | Follow agnostic update protocol: `.0agnostic/02_rules/static/agnostic_update_protocol/agnostic_update_protocol.md` |
| Working with layers/stages | Load skill: context-gathering |
| Need rules | Load `.claude/skills/` or reference `.0agnostic/02_rules/` |
| Local Ubuntu desktop issues (volume, brightness, keybindings, audio, GNOME, post-sleep) | Load `.0agnostic/02_rules/dynamic/local_ubuntu_desktop_troubleshooting/` |
| User says "use research context chain" | Load `.0agnostic/02_rules/dynamic/CONTEXT_CHAIN_MODE/context_chain_mode.md` and switch to research mode |
| Promoting research to production | Load `.0agnostic/03_protocols/research_promotion_protocol.md` |
| Creating or modifying pointer files | Follow `.0agnostic/03_protocols/pointer_sync_protocol.md` and run `pointer-sync.sh --validate` |
| Modifying agent delegation patterns | Load `.0agnostic/02_rules/dynamic/agent_delegation_workspace_rule/agent_delegation_workspace_rule.md` |

## Resources

| Resource | Location | Purpose |
|----------|----------|---------|
| Skills | `.claude/skills/SKILLS.md` | Task-specific instructions |
| Rules | `.0agnostic/02_rules/` | Universal rules |
| Deduplication Rule | `.0agnostic/02_rules/documentation_deduplication_rule.md` | MANDATORY: Single-source-of-truth for all documentation |
| Deduplication Pattern | `.0agnostic/01_knowledge/deduplication_pattern.md` | Complete guide to naming conventions and pointer format |
| Deduplication Onboarding | `.0agnostic/01_knowledge/deduplication_onboarding.md` | Team guide for following the deduplication pattern |
| Deduplication Summary | `.0agnostic/01_knowledge/deduplication_project_summary.md` | Project overview: what was accomplished and why |
| Update Protocol | `.0agnostic/02_rules/static/agnostic_update_protocol/agnostic_update_protocol.md` | Sync chain for .0agnostic/ changes |
| Knowledge | `.0agnostic/01_knowledge/` | Reference docs |
| Research Knowledge Index | `.0agnostic/01_knowledge/layer_stage_system/docs/RESEARCH_KNOWLEDGE_INDEX.md` | Index of all research outputs with paths and promotion status |
| Setup-Dependant | `.0agnostic/07+_setup_dependant/` | Machine/OS-specific context (Ubuntu, coding apps, etc.) |
| Research Promotion Protocol | `.0agnostic/03_protocols/research_promotion_protocol.md` | How to promote validated research to production |
| Pointer Sync Protocol | `.0agnostic/03_protocols/pointer_sync_protocol.md` | Auto-updating pointer files when canonical paths change |
| Pointer Sync Knowledge | `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md` | How the pointer sync system works |
| Pointer Sync Rule | `.0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md` | Always-apply rule for pointer file format |
| Context Chain Mode | `.0agnostic/02_rules/dynamic/CONTEXT_CHAIN_MODE/context_chain_mode.md` | Default vs Research mode switching |

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
- `layer_1_project_school` currently contains one active nested gitlink at `.../layer_6_sub_feature_team_work/school-machine-learning-teamwork`.
- If any additional nested repos appear, they must be declared in `.gitmodules` at the same repository level before commit/push.
