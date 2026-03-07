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

<!-- section_id: "1aa0e072-d338-4d31-a103-534f50df4ab8" -->

## Promoted Rules

| When | Rule |
|------|------|
| Modifying any file in .0agnostic/ | When modifying .0agnostic/ files, also update 0AGNOSTIC.md and run agnostic-sync.sh. Full protocol: .0agnostic/02_rules/static/agnostic_update_protocol.md |
| Any turn that modifies files | On every turn with file changes: (1) describe changes INLINE with full absolute paths using path:line format (e.g., /home/dawson/.../file.md:42) for ctrl-click navigation, (2) provide end-of-turn summary of all Added/Updated/Moved/Removed files. All paths start from /home/, NEVER abbreviated. Use path:line for ANY file reference pointing to a specific location. Full rule: .0agnostic/02_rules/static/I0_FILE_CHANGE_REPORTING/I0_FILE_CHANGE_REPORTING.md |



---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
