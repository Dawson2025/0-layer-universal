# Claude Code Context


## Identity
You are an agent at **Layer 0** (Feature), **Feature**: Multimodal System.
- **Role**: Future multimodal capabilities — voice, vision, and other modalities
- **Scope**: Multimodal input/output, modality-specific workflows, future capabilities
- **Parent**: `../0AGNOSTIC.md` (layer_0_features)
- **Children**: `layer_1_group/layer_1_sub_features/` contains 1 sub-feature (audio)

## Triggers
Load this context when:
- User mentions: multimodal, voice, vision, audio, image processing
- Working on: Multimodal integration, new modality support
- Entering: `layer_0_feature_multimodal_system/`

## Pointers
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_0_group/layer_0_99_stages/` for stage progress

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../0AGNOSTIC.md` |
| Stages | `layer_0_group/layer_0_99_stages/` |
| Audio sub-feature | `layer_1_group/layer_1_sub_features/layer_1_sub_feature_audio/` |

## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/episodic_memory/` |

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
