# Claude Code Context

---
resource_id: "6512d4dd-e3d9-4286-b7c4-48d54da4cf6d"
resource_type: "agnostic
document"
resource_name: "0AGNOSTIC"
---
# 0_layer_universal - Agnostic Identity

<!-- section_id: "b2aab0fd-e9c1-4f32-85ff-4d13f0649c26" -->
## Identity

**Role**: Root Manager
**Scope**: Coordinates all layers in the AI context system
**Layer**: Root (contains layer_0, layer_1, layer_-1_research)

<!-- section_id: "f80cb478-72aa-4967-91e4-1aacd1b77565" -->
## Critical Rules

These rules apply to EVERY AI agent at this level and below:

<!-- section_id: "60ba0156-da52-4d22-a78a-7d5b1b1c9765" -->
### 1. Filesystem Change Visualization Protocol

**Two tiers** — show proposed changes before executing:

**Tier 1 (AI Context — strict)**: Before modifying AI context files, show propagation chain diagram, store proposal in registry, wait for approval.
**Scope**: `0AGNOSTIC.md`, `.0agnostic/`, `.1merge/`, `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`, `OPENAI.md`, `.claude/`, `.cursor/`, `*_rules/`, `*_prompts/`, `*_knowledge/`, `status.json`, `*.gab.jsonld`, `*.integration.md`

**Tier 2 (General Filesystem — standard)**: Before structural filesystem changes (2+ dirs, 3+ files, reorganization), show before/after diagram, wait for approval.
**Exemptions**: Single file edits, single file creation, appends.

**Full rule**: `.0agnostic/02_rules/0_every_api_request/AI_CONTEXT_MODIFICATION_PROTOCOL/AI_CONTEXT_MODIFICATION_PROTOCOL.md`

<!-- section_id: "4bda3538-1a9c-45f7-8ead-48acec10920e" -->
### 2. Stage Completeness Rule

When creating entities with stages: **ALL 11 stages MUST exist**.

Empty stages are valid. Missing stages are NOT.

**Reference**: `layer_0/.../layer_stage_system/STAGES_EXPLAINED.md`

<!-- section_id: "d98bbf96-7989-4c0d-b933-707f4a989053" -->
### 3. AI Context Commit/Push Rule

After approved changes:
1. `git add [specific files]`
2. `git commit -m "[AI Context] description"`
3. `git push`

<!-- section_id: "2c6faf1a-3bb1-4b09-ba53-3d0deefa908d" -->
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

<!-- section_id: "a1b2c3d4-e5f6-4a7b-8c9d-0e1f2a3b4c5d" -->
## UUID Identity System

Every entity, stage, file, and directory has a stable UUID that survives renames and moves.

| Component | Where | Example |
|-----------|-------|---------|
| Entity UUIDs | `entity_id:` in every `0AGNOSTIC.md` | `entity_id: "a79b61a7-..."` |
| File UUIDs | `resource_id:` in file headers | `resource_id: "6512d4dd-..."` |
| Stage UUIDs | `stage_index.json` in stage registries | Maps stage names to UUIDs |
| Section UUIDs | `<!-- section_id: "..." -->` comments | Anchor links within files |
| Directory UUIDs | `.dir-id` file in each directory | Single UUID per directory |
| Global index | `.uuid-index.json` at repo root | 5,313 entries (entities + stages + resources) |

**Fast entity lookup** (run from repo root):

```bash
.0agnostic/entity-find.sh memory            # Find entities by name (~5ms, no Python)
.0agnostic/entity-find.sh --path chain       # Just show paths
.0agnostic/entity-find.sh --uuid memory      # Just show UUIDs
```

**Advanced commands** (full UUID system, uses Python):

```bash
pointer-sync.sh --query type=entity name=*memory*   # Find entities by name
pointer-sync.sh --lookup <uuid>                      # Look up any UUID
pointer-sync.sh --parent <uuid>                      # Get parent entity
pointer-sync.sh --children <uuid>                    # List child entities
pointer-sync.sh --find-references <uuid>             # Find all references before rename/delete
pointer-sync.sh --query type=resource entity_id=<uuid>  # Resources within an entity
```

**Full reference**: Load `/uuid-query` skill or read `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md`

<!-- section_id: "de02eca7-38ba-422c-83f2-46ea04923b46" -->
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
| Querying UUID identity system (entity lookup, hierarchy, resources) | Load skill: uuid-query |
| Locating an entity by name or finding where something lives | Run `.0agnostic/entity-find.sh <name>` (fast, no Python) |
| Finding an entity, stage, or resource by name or UUID | Run `pointer-sync.sh --query` or load skill: uuid-query |
| Checking references before renaming or deleting an entity | Run `pointer-sync.sh --find-references <uuid>` |
| Multi-step development tasks | Load `.0agnostic/02_rules/1_scenario_based/sequential_development_methodology/sequential_development_methodology.md` |
| Security decisions, access control, or sensitive operations | Load `.0agnostic/02_rules/1_scenario_based/safety_governance/safety_governance.md` |
| Creating file headers or context headers | Load `.0agnostic/02_rules/1_scenario_based/LAYER_CONTEXT_HEADER_PROTOCOL/LAYER_CONTEXT_HEADER_PROTOCOL.md` |
| Cross-platform or multi-OS work | Load `.0agnostic/02_rules/1_scenario_based/CROSS_OS_COMPATIBILITY_RULES/CROSS_OS_COMPATIBILITY_RULES.md` |
| Running stages in parallel or managing concurrent stage work | Load `.0agnostic/02_rules/dynamic/PARALLEL_STAGES_RULE/PARALLEL_STAGES_RULE.md` |
| Looping between stages (testing→criticism→fixing) | Load `.0agnostic/02_rules/dynamic/STAGE_LOOP_RULE/STAGE_LOOP_RULE.md` |
| Source of truth conflicts or duplicate content | Load `.0agnostic/02_rules/dynamic/I0_source_of_truth_rule/I0_source_of_truth_rule.md` |
| CLI vs GUI launcher issues (apps opening wrong way) | Load `.0agnostic/02_rules/dynamic/cli_gui_launcher_mismatch_rule/cli_gui_launcher_mismatch_rule.md` |
| Browser content extraction | Load `.0agnostic/02_rules/dynamic/browser_extraction_rule/browser_extraction_rule.md` |
| Manager delegating to stage agents | Load `.0agnostic/02_rules/static/MANAGER_DELEGATION_RULE/MANAGER_DELEGATION_RULE.md` |
| Stage boundary transitions (entering/exiting stages) | Load `.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE/STAGE_BOUNDARY_RULE.md` |
| Writing or reading stage reports | Load `.0agnostic/02_rules/static/STAGE_REPORT_RULE/STAGE_REPORT_RULE.md` |
| Designing system architecture or creating diagrams | Load `.0agnostic/03_protocols/design_diagramming_protocol.md` |
| Context loading or chain traversal | Load `.0agnostic/03_protocols/context_loading_protocol.md` |
| Checking context quality | Load `.0agnostic/03_protocols/context_quality_checklist.md` |
| Initializing features or sub-features | Load `.0agnostic/03_protocols/features_init_prompt.md` |
| Adopting the hierarchy in a new project | Load `.0agnostic/03_protocols/HIERARCHY_ADOPTION_CHECKLIST.md` and `.0agnostic/03_protocols/HIERARCHY_QUICK_START.md` |
| Consolidating, renaming, or reorganizing layers | Load `.0agnostic/03_protocols/layer_consolidation_and_naming_protocol.md` |
| Migrating to the layer-stage system | Load `.0agnostic/03_protocols/MIGRATION_GUIDE.md` |
| Testing rules | Load `.0agnostic/03_protocols/rule_testing_protocol.md` |
| SQLite database creation issues | Load `.0agnostic/03_protocols/sqlite_database_creation_troubleshooting_trajectory.md` |
| Writing or reviewing stage reports (protocol) | Load `.0agnostic/03_protocols/stage_report_protocol.md` |
| Deciding what to work on next | Load `.0agnostic/03_protocols/what_to_do_next.md` |

<!-- section_id: "1aa0e072-d338-4d31-a103-534f50df4ab8" -->
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
| Entity Find Tool | `.0agnostic/entity-find.sh` | Fast entity lookup by name (~5ms, no Python) |
| Resource Index Tool | `.0agnostic/create-resource-indexes.sh` | Generate per-entity `resource_index.json` files for resource UUID traversal |
| Pointer Sync Protocol | `.0agnostic/03_protocols/pointer_sync_protocol.md` | Auto-updating pointer files when canonical paths change |
| Pointer Sync Knowledge | `.0agnostic/01_knowledge/pointer_sync/pointer_sync_knowledge.md` | How the pointer sync system works |
| Pointer Sync Rule | `.0agnostic/02_rules/static/pointer_sync_rule/pointer_sync_rule.md` | Always-apply rule for pointer file format |
| Context Chain Mode | `.0agnostic/02_rules/dynamic/CONTEXT_CHAIN_MODE/context_chain_mode.md` | Default vs Research mode switching |
| UUID Query Skill | `.0agnostic/06_context_avenue_web/01_file_based/05_skills/uuid-query/SKILL.md` | Agent interface for UUID system queries |
| Skills Index | `.0agnostic/06_context_avenue_web/01_file_based/05_skills/SKILLS.md` | All available skills |
| Canonical Entity Structure | `.0agnostic/06_context_avenue_web/01_file_based/04_@import_references/entity_structure.md` | Authoritative entity directory structure entrypoint |
| AALang/GAB System | `.0agnostic/01_knowledge/aalang_gab_system/` | AALang language spec, agent definitions, JSON-LD patterns |
| Agent Coordination | `.0agnostic/01_knowledge/agent_coordination/` | Multi-agent coordination patterns |
| Context Loading | `.0agnostic/01_knowledge/context_loading/` | Context chain traversal and loading strategies |
| Entity Lifecycle | `.0agnostic/01_knowledge/entity_lifecycle/` | Entity creation, instantiation, types |
| Naming Conventions | `.0agnostic/01_knowledge/naming_conventions/` | Layer-stage naming rules |
| Navigation Patterns | `.0agnostic/01_knowledge/navigation_patterns/` | How agents navigate the hierarchy |
| Principles | `.0agnostic/01_knowledge/principles/` | Core design principles |
| Visualization Tools | `.0agnostic/01_knowledge/visualization_tools/` | Diagram and visualization resources |
| Desktop Environment Health | `.0agnostic/01_knowledge/desktop_environment_health/` | GNOME/desktop troubleshooting knowledge |
| Software Engineering Knowledge | `.0agnostic/01_knowledge/software_engineering_knowledge_system/` | General software engineering reference |
| File Change Reporting Rule | `.0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING/I0_FILE_CHANGE_REPORTING.md` | Mandatory path:line file references on every turn |
| Manager Delegation Rule | `.0agnostic/02_rules/static/MANAGER_DELEGATION_RULE/` | How managers delegate to stage agents |
| Stage Boundary Rule | `.0agnostic/02_rules/static/STAGE_BOUNDARY_RULE/` | Rules for entering/exiting stages |
| Stage Report Rule | `.0agnostic/02_rules/static/STAGE_REPORT_RULE/` | Stage report format and timing |
| Source of Truth Rule | `.0agnostic/02_rules/dynamic/I0_source_of_truth_rule/` | Canonical vs derived content rules |
| Context Loading Protocol | `.0agnostic/03_protocols/context_loading_protocol.md` | Step-by-step context loading procedure |
| Stage Report Protocol | `.0agnostic/03_protocols/stage_report_protocol.md` | Stage report format and delivery |
| Context Quality Checklist | `.0agnostic/03_protocols/context_quality_checklist.md` | Verify context completeness |
| Design Diagramming Protocol | `.0agnostic/03_protocols/design_diagramming_protocol.md` | Creating architecture diagrams |
| Hierarchy Quick Start | `.0agnostic/03_protocols/HIERARCHY_QUICK_START.md` | Fast onboarding to the hierarchy |
| CLI vs GUI Diagnosis | `.0agnostic/03_protocols/cli_vs_gui_launcher_diagnosis_protocol.md` | Diagnosing launcher mismatches |
| Source of Truth Protocol | `.0agnostic/03_protocols/source_of_truth_protocol.md` | Resolving canonical vs derived conflicts |
| Universal Init Prompt | `.0agnostic/03_protocols/universal_init_prompt.md` | Standard agent initialization prompt |
| Protocols README | `.0agnostic/03_protocols/README.md` | Overview of all protocols |

<!-- section_id: "7a3af372-8f41-431b-b5ed-e58c6c883565" -->
## Children

| Layer | Purpose |
|-------|---------|
| `layer_0/` | Universal (applies to ALL) |
| `layer_1/` | Projects |
| `layer_-1_research/` | Research projects |

---

*This is the source of truth for 0_layer_universal identity.*
*Tool-specific files (CLAUDE.md, GEMINI.md, AGENTS.md) are generated from this.*

<!-- section_id: "4dc9b6d7-b64d-4d67-9e22-7ff75e2e800e" -->
## Mandatory Checkpoint Cadence

1. Commit and push for each new item.
2. Commit and push for each update.
3. In submodule chains, push deepest children first, then parent pointers to root.


Active chain map (school -> module_03):
- `0_layer_universal` tracks `layer_1/layer_1_projects/layer_1_project_school` as submodule.
- `layer_1_project_school` currently contains one active nested gitlink at `.../layer_6_sub_feature_team_work/school-machine-learning-teamwork`.
- If any additional nested repos appear, they must be declared in `.gitmodules` at the same repository level before commit/push.

## Promoted Rules

| When | Rule |
|------|------|
| Modifying any file in .0agnostic/ | When modifying .0agnostic/ files, also update 0AGNOSTIC.md and run agnostic-sync.sh. Full protocol: .0agnostic/02_rules/static/agnostic_update_protocol.md |
| Any turn that modifies files | On every turn with file changes: (1) describe changes INLINE with full absolute paths using path:line format (e.g., /home/dawson/.../file.md:42) for ctrl-click navigation, (2) provide end-of-turn summary of all Added/Updated/Moved/Removed files. All paths start from /home/, NEVER abbreviated. Use path:line for ANY file reference pointing to a specific location. Full rule: .0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING/I0_FILE_CHANGE_REPORTING.md |


## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
resource_id: "4ad5e701-2fdd-4fee-8453-cb78a1f8d309"
resource_type: "document"
resource_name: "tool_additions"
---
# Claude Code CLI — Universal Additions

<!-- section_id: "e59fa8d3-f2c3-425a-8362-dc3acab35963" -->
## Browser Extraction Capabilities

Claude Code CLI has browser extraction capabilities via the **Claude in Chrome** MCP server. When you need to extract content from web pages — especially pages that use React rendering (Perplexity, SPAs) — use the following:

<!-- section_id: "bee1bdb1-028f-4325-9173-8c5aecf85506" -->
### Available Skills

| Skill | Trigger | What It Does |
|-------|---------|--------------|
| `/perplexity-extract` | User provides a Perplexity URL | Extracts structured content + citation source URLs using React fiber traversal |

<!-- section_id: "26803820-3e44-47fb-aaba-5baead604ad7" -->
### When to Use Browser Extraction

- User shares a Perplexity search URL and wants the content/citations preserved
- User needs citation URLs from a Perplexity page (standard copy/paste loses them)
- Content extraction from React-rendered pages where `querySelectorAll('a[href]')` fails
- Any page where URLs are stored in React component props, not DOM attributes
- User asks to open Claude in Chrome and navigate to or work in Perplexity (e.g., "open Perplexity in the browser", "search Perplexity for X")

<!-- section_id: "c3908443-8b63-4644-a07f-a21bd382685b" -->
### Prerequisites

- Claude in Chrome MCP server must be connected (check with `tabs_context_mcp`)
- If MCP server is not available, fall back to `WebFetch` for basic content or ask the user to copy/paste

<!-- section_id: "1a3c3a40-d60e-45fc-8ded-b28eb49ea7f5" -->
### Key Knowledge

- React fiber traversal (`__reactFiber$*` → `memoizedProps.children.props`) is the ONLY reliable method for Perplexity citation URLs
- Standard DOM queries return ~0 external links on Perplexity
- Must scroll through all answers before extraction (React virtualization unloads offscreen DOM)
- Detailed knowledge at: `.0agnostic/07+_setup_dependant/.../sub_layer_0_10_claude_in_chrome/.0agnostic/01_knowledge/perplexity_extraction/`

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
