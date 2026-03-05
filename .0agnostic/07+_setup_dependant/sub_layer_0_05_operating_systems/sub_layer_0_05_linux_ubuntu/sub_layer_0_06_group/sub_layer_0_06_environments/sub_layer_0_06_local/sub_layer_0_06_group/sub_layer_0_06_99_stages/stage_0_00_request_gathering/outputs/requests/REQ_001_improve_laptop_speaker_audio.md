---
resource_id: "6d3a4f94-4370-4030-9b1b-5466f67af014"
resource_type: "output"
resource_name: "REQ_001_improve_laptop_speaker_audio"
---
# Request: Improve Laptop Speaker Audio Quality

<!-- section_id: "f38ca3ea-0ceb-4e2e-a77b-650752fa96d4" -->
## Request ID
REQ_001

<!-- section_id: "0d5819e7-cfb1-4b04-bc3d-0ad5d05fe22f" -->
## Date
2026-01-26

<!-- section_id: "e1037f90-1bd3-4ac7-8f37-405e6f9e4429" -->
## Priority
High

<!-- section_id: "6e34a90b-12bc-4496-aaff-93dc14dcfe9d" -->
## Description
Laptop speaker audio quality on Linux (Ubuntu 24.04) is significantly worse than on Windows. The same hardware sounds noticeably better on the Windows side of the dual-boot system.

<!-- section_id: "684a7be6-36da-4dd5-9ce1-dbfe428e038c" -->
## Hardware
- **Laptop**: Lenovo Yoga Pro 9 16IMH9
- **Audio Chip**: Intel Meteor Lake-P HD Audio (sof-hda-dsp)
- **Current Driver**: SOF (Sound Open Firmware)

<!-- section_id: "d9ee4b0e-089b-457f-91e1-d1bab80173b2" -->
## Current State
- EasyEffects installed with basic preset
- Audio is functional but lacks:
  - Bass depth
  - Stereo width
  - Overall fullness
  - Clarity at higher volumes

<!-- section_id: "1d8449b6-6196-4409-a7fd-5b0382820957" -->
## Desired Outcome
Audio quality that approaches Windows Dolby-enhanced sound:
- Fuller bass response
- Wider stereo image
- Clearer vocals/dialogue
- No distortion at high volumes

<!-- section_id: "67998c51-a580-4626-9fde-ed8d17005020" -->
## Known Constraints
- No access to proprietary Dolby DSP
- No access to Lenovo speaker tuning profiles
- Hardware speakers are physically limited

<!-- section_id: "c01e3b32-ca76-49e7-b5a3-e02444d045c5" -->
## Research Questions
1. Are there AutoEQ profiles for this specific laptop?
2. Can we extract/reverse-engineer Windows audio profiles?
3. Are there better EasyEffects presets for laptop speakers?
4. Is there alternative firmware or drivers that sound better?
5. Are there PipeWire filter chains optimized for this hardware?

<!-- section_id: "8d450ce5-0c83-430e-ab31-251d68ed87dd" -->
## Status
- [ ] Research phase
- [ ] Solution identified
- [ ] Implementation
- [ ] Verification
