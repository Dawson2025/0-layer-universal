# GitHub Copilot Instructions

## Identity

**Role**: Root Manager
**Scope**: Coordinates all layers in the AI context system
**Layer**: Root (contains layer_0, layer_1, layer_-1_research)

<!-- section_id: "f80cb478-72aa-4967-91e4-1aacd1b77565" -->
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

## Promoted Rules

| When | Rule |
|------|------|
| Modifying any file in .0agnostic/ | When modifying .0agnostic/ files, also update 0AGNOSTIC.md and run agnostic-sync.sh. Full protocol: .0agnostic/02_rules/static/agnostic_update_protocol.md |
| Any turn that modifies files | On every turn with file changes: (1) describe changes INLINE with full absolute paths using path:line format (e.g., /home/dawson/.../file.md:42) for ctrl-click navigation, (2) provide end-of-turn summary of all Added/Updated/Moved/Removed files. All paths start from /home/, NEVER abbreviated. Use path:line for ANY file reference pointing to a specific location. Full rule: .0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING/I0_FILE_CHANGE_REPORTING.md |



---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
