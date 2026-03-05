<!-- derived_from: "0481b56e-80a9-4ebc-9e9c-6dda3a9fca9d" -->
# Claude Code Context


## Identity
You are an agent at **Layer 1** (Feature), **Feature**: Multimodal System.
- **Role**: Future multimodal capabilities — voice, vision, and other modalities
- **Scope**: Multimodal input/output, modality-specific workflows, future capabilities
- **Parent**: `../../0AGNOSTIC.md` (layer_0_better_ai_system)
- **Children**: `layer_2_group/layer_2_sub_features/` contains 1 sub-feature (audio)

## Triggers
Load this context when:
- User mentions: multimodal, voice, vision, audio, image processing
- Working on: Multimodal integration, new modality support
- Entering: `layer_1_feature_multimodal_system/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_0_group/layer_0_99_stages/` for stage progress

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../0AGNOSTIC.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| Audio sub-feature | `layer_2_group/layer_2_sub_features/layer_2_sub_feature_audio/` |

## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/episodic_memory/` |

## Platform Dependencies
Multimodal features (especially audio/TTS) depend on the local desktop environment. The local Ubuntu entity has been restructured as a proper entity with knowledge topics:

**Local entity root** (from repo root): `.0agnostic/07+_setup_dependant/sub_layer_0_05_operating_systems/sub_layer_0_05_linux_ubuntu/sub_layer_0_06_group/sub_layer_0_06_environments/sub_layer_0_06_local/`

Key resources within the local entity:
- **Entity context**: `0AGNOSTIC.md` — start here for all local Ubuntu issues
- **GNOME architecture**: `.0agnostic/01_knowledge/ubuntu_desktop/docs/gnome_architecture.md`
- **Audio stack**: `.0agnostic/01_knowledge/audio/docs/linux_audio_stack.md`
- **System services**: `.0agnostic/01_knowledge/system_services/docs/systemd_user_services.md`
- **GSD keepalive fix**: `sub_layer_0_06_group/sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/gsd_keepalive_fix.md`

**Dynamic rule**: Universal rule at `.0agnostic/02_rules/dynamic/local_ubuntu_desktop_troubleshooting/` triggers for desktop/audio issues.

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
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
