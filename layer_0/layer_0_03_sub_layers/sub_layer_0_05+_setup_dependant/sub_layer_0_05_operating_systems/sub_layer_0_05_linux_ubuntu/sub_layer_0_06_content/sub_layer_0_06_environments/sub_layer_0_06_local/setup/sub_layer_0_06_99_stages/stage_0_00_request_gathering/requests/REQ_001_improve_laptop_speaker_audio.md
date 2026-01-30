# Request: Improve Laptop Speaker Audio Quality

## Request ID
REQ_001

## Date
2026-01-26

## Priority
High

## Description
Laptop speaker audio quality on Linux (Ubuntu 24.04) is significantly worse than on Windows. The same hardware sounds noticeably better on the Windows side of the dual-boot system.

## Hardware
- **Laptop**: Lenovo Yoga Pro 9 16IMH9
- **Audio Chip**: Intel Meteor Lake-P HD Audio (sof-hda-dsp)
- **Current Driver**: SOF (Sound Open Firmware)
- **Kernel**: 6.14.0-37-generic (includes all SOF fixes)

## Current State
- EasyEffects installed with multiple presets
- Audio is functional but lacks:
  - Bass depth
  - Stereo width
  - Overall fullness
  - Clarity at higher volumes

## Desired Outcome
Audio quality that approaches Windows Dolby-enhanced sound:
- Fuller bass response
- Wider stereo image
- Clearer vocals/dialogue
- No distortion at high volumes

## Known Constraints
- No access to proprietary Dolby DSP
- No access to Lenovo speaker tuning profiles
- Hardware speakers are physically limited

## Status
- [x] Research phase (completed 2026-01-26)
- [x] Solution identified (multiple presets + JamesDSP option)
- [x] Implementation (in progress)
- [ ] Verification

## Implementation Progress
- Installed community EasyEffects presets (JackHack96)
- Installed "Dolby-Like (Framework)" preset from Framework Community
- Currently testing presets

## Available Presets to Test
1. `Dolby-Like (Framework)` - Multiband compression + bass enhancer + stereo widening (CURRENT)
2. `Advanced Auto Gain` - Laptop speaker optimized with volume normalization
3. `Bass Enhancing + Perfect EQ` - EQ-focused approach
4. `LaptopSpeakers` - Custom basic preset

## Research Output
See: `stage_0_01_research/outputs/REQ_001_audio_improvement_research.md`
