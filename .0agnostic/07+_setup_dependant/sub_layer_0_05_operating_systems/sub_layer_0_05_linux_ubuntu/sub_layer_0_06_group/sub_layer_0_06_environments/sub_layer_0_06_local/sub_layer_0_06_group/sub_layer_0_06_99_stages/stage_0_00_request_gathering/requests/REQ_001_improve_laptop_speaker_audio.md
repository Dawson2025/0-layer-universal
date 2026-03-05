---
resource_id: "cbe74f07-6c6c-4420-b91c-90e3e5893113"
resource_type: "document"
resource_name: "REQ_001_improve_laptop_speaker_audio"
---
# Request: Improve Laptop Speaker Audio Quality

<!-- section_id: "e769474d-3d01-4bc1-ad50-3f015bab535e" -->
## Request ID
REQ_001

<!-- section_id: "b883e54d-48c4-48c8-a43f-20a618c18373" -->
## Date
2026-01-26

<!-- section_id: "570507f1-087f-422d-8524-5bd3ec40ccce" -->
## Priority
High

<!-- section_id: "a2fdf879-ea35-4be4-8fbb-cc37739bba34" -->
## Description
Laptop speaker audio quality on Linux (Ubuntu 24.04) is significantly worse than on Windows. The same hardware sounds noticeably better on the Windows side of the dual-boot system.

<!-- section_id: "b7836d4e-19e9-4141-8414-9cf53f56cbc6" -->
## Hardware
- **Laptop**: Lenovo Yoga Pro 9 16IMH9
- **Audio Chip**: Intel Meteor Lake-P HD Audio (sof-hda-dsp)
- **Current Driver**: SOF (Sound Open Firmware)
- **Kernel**: 6.14.0-37-generic (includes all SOF fixes)

<!-- section_id: "deb70f55-585b-457b-881d-f68322374739" -->
## Current State
- EasyEffects installed with multiple presets
- Audio is functional but lacks:
  - Bass depth
  - Stereo width
  - Overall fullness
  - Clarity at higher volumes

<!-- section_id: "dbf24696-ff8f-498d-b4de-e6afed8287be" -->
## Desired Outcome
Audio quality that approaches Windows Dolby-enhanced sound:
- Fuller bass response
- Wider stereo image
- Clearer vocals/dialogue
- No distortion at high volumes

<!-- section_id: "22553474-751a-423f-be90-ee3ec8359880" -->
## Known Constraints
- No access to proprietary Dolby DSP
- No access to Lenovo speaker tuning profiles
- Hardware speakers are physically limited

<!-- section_id: "84624337-5ad3-442d-ab53-a935cedd9d3b" -->
## Status
- [x] Research phase (completed 2026-01-26)
- [x] Solution identified (multiple presets + JamesDSP option)
- [x] Implementation (in progress)
- [ ] Verification

<!-- section_id: "889927c1-df07-4497-9cc7-344a9a67bfd2" -->
## Implementation Progress
- Installed community EasyEffects presets (JackHack96)
- Installed "Dolby-Like (Framework)" preset from Framework Community
- Currently testing presets

<!-- section_id: "f4982eff-b81a-4c8c-82a7-b587e7bcc8e7" -->
## Available Presets to Test
1. `Dolby-Like (Framework)` - Multiband compression + bass enhancer + stereo widening (CURRENT)
2. `Advanced Auto Gain` - Laptop speaker optimized with volume normalization
3. `Bass Enhancing + Perfect EQ` - EQ-focused approach
4. `LaptopSpeakers` - Custom basic preset

<!-- section_id: "09bf3640-fa13-4f7a-9a60-db237dc8bfbe" -->
## Research Output
See: `stage_0_01_research/outputs/REQ_001_audio_improvement_research.md`
