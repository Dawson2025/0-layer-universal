---
resource_id: "e9644de5-d9ad-43d2-bfb6-a44c7a62e978"
resource_type: "agnostic_document"
resource_name: "0AGNOSTIC"
---
# 0AGNOSTIC.md - layer_1_feature_multimodal_system

<!-- section_id: "53b981fc-3d5a-41ad-8dd9-0971baa3767b" -->
## Identity

entity_id: "0481b56e-80a9-4ebc-9e9c-6dda3a9fca9d"

You are an agent at **Layer 1** (Feature), **Feature**: Multimodal System.
- **Role**: Future multimodal capabilities — voice, vision, and other modalities
- **Scope**: Multimodal input/output, modality-specific workflows, future capabilities
- **Parent**: `../../0AGNOSTIC.md` (layer_0_better_ai_system)
- **Children**: `layer_2_group/layer_2_sub_features/` contains 1 sub-feature (audio)

<!-- section_id: "e5d59058-f8e6-4902-b4d2-54479848541c" -->
## Triggers
Load this context when:
- User mentions: multimodal, voice, vision, audio, image processing
- Working on: Multimodal integration, new modality support
- Entering: `layer_1_feature_multimodal_system/`

<!-- section_id: "c32f4768-ea96-44bc-972c-30ec9ae420b8" -->
## Pointers
<!-- section_id: "8c884a19-e409-4597-9dcb-f5c4d70ec4a4" -->
### On Entry
1. Read `0INDEX.md` for current state
2. Check `layer_0_group/layer_0_99_stages/` for stage progress

<!-- section_id: "5e81a99c-62d2-4194-8855-e6a5c1376d2a" -->
### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../0AGNOSTIC.md` |
| Stages | `layer_1_group/layer_1_99_stages/` |
| Audio sub-feature | `layer_2_group/layer_2_sub_features/layer_2_sub_feature_audio/` |

<!-- section_id: "77a197ab-4e43-4b90-bec6-67efd0d56078" -->
## Where to Contribute
| Work Type | Location |
|-----------|----------|
| Research | Appropriate stage `outputs/` directory |
| Session notes | `.0agnostic/episodic_memory/` |

<!-- section_id: "e527bc9b-94e9-4679-b6ce-573d82b5d4d2" -->
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
