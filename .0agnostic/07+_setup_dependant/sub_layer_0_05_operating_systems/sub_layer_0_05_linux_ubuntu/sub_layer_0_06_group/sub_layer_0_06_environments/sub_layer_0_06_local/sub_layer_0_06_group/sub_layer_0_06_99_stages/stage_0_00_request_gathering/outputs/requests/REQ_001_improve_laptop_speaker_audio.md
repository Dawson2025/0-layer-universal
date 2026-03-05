---
resource_id: "6d3a4f94-4370-4030-9b1b-5466f67af014"
resource_type: "output"
resource_name: "REQ_001_improve_laptop_speaker_audio"
---
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

## Current State
- EasyEffects installed with basic preset
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

## Research Questions
1. Are there AutoEQ profiles for this specific laptop?
2. Can we extract/reverse-engineer Windows audio profiles?
3. Are there better EasyEffects presets for laptop speakers?
4. Is there alternative firmware or drivers that sound better?
5. Are there PipeWire filter chains optimized for this hardware?

## Status
- [ ] Research phase
- [ ] Solution identified
- [ ] Implementation
- [ ] Verification
