---
resource_id: "b1c8b604-ccba-4a33-88aa-00b381ab1104"
resource_type: "output"
resource_name: "REQ_002_yoga_speaker_i2c_research"
---
# Research: Yoga Pro 9 Speaker I2C Configuration

<!-- section_id: "9eeb27c5-028a-460e-bed3-8c5be591d99e" -->
## Request Reference
REQ_002 - Fix Yoga Pro 9 Subwoofer/Speaker Quality on Linux

<!-- section_id: "3db014a5-0b30-47ab-bb82-77a5bc9db6df" -->
## Date
2026-01-26

<!-- section_id: "e6f6422d-90d2-49a8-81d0-5caacfc732f8" -->
## Problem Statement

Linux audio on Lenovo Yoga Pro 9 sounds significantly worse than Windows:
- Thin, weak sound lacking bass
- Sound quality noticeably inferior to Windows Dolby Atmos
- Previous EasyEffects attempts improved but didn't match Windows

<!-- section_id: "54b7dd69-d3ee-4307-8291-65c5638f3b9f" -->
## Research Sources

<!-- section_id: "b0113fbf-7646-417f-af54-6dbbf49cf52d" -->
### Primary Source
**GitHub Repository**: [maximmaxim345/yoga_pro_9i_gen9_linux](https://github.com/maximmaxim345/yoga_pro_9i_gen9_linux)

<!-- section_id: "da05e068-3ddc-4f47-b28b-ec2b01bea66d" -->
### Related Resources
- [Kernel Bug Report #217449](https://bugzilla.kernel.org/show_bug.cgi?id=217449)
- [GitHub Issue: karypid/YogaPro-16IMH9#2](https://github.com/karypid/YogaPro-16IMH9/issues/2)
- Perplexity deep research on Linux laptop audio optimization

<!-- section_id: "c75f4dd9-629d-46d1-9121-bb473c5ccbbe" -->
## Key Findings

<!-- section_id: "73e5b3a1-790e-49a8-91fe-ceae9e7ee7e8" -->
### Finding 1: Subwoofer Disabled by Default

The Yoga Pro 9 subwoofer is **disabled by default** on Linux due to a kernel bug:

> "Speakers require some configuration. Subwoofer is disabled by default due to a bug"

This explains why Linux audio lacked bass - the bass speakers weren't even active.

<!-- section_id: "a7988915-6eb7-4fe6-8a92-86dc4e83dc7b" -->
### Finding 2: I2C Bypass Script Required

The subwoofer can be enabled via I2C commands to the TAS2781 amplifier:
- Script: `2pa-byps.sh`
- Sends specific I2C register values to addresses 0x3f and 0x38
- Must run at boot and after sleep/hibernate

<!-- section_id: "89353410-5fa3-48a2-b9ad-58e986de2a2c" -->
### Finding 3: Kernel Driver Conflict

The `snd_hda_scodec_tas2781_i2c` kernel driver **resets** the I2C configuration:
- Driver is loaded by default
- Overwrites manual I2C settings
- Causes sound to revert to weak state after script runs

**Solution**: Blacklist the driver in `/etc/modprobe.d/`

<!-- section_id: "7362a223-130e-4ee0-9dea-99973c5f622f" -->
### Finding 4: Model-Specific Configuration

Different Yoga Pro 9 variants require different I2C addresses:
- Model 83BY (16IRP8): addresses 0x39, 0x38, 0x3d, 0x3b
- Model 83DN (16IMH9): addresses 0x3f, 0x38
- Model 83L0 (16IAH10): uses different I2C bus index

<!-- section_id: "1c083c29-8263-4914-b524-4275d47f39e3" -->
### Finding 5: EasyEffects Presets Available

The GitHub repo includes pre-tuned EasyEffects presets:
- `Yoga Pro 9i gen 9.json`
- `Yoga Pro 9i gen 9 v2.json`
- `Yoga Pro 9i gen 9 v2 less bass.json`

<!-- section_id: "4ac4dca4-f1cd-4e67-b556-90a55b984e20" -->
## Conclusions

1. The weak audio was NOT just missing Dolby processing - the subwoofer hardware was disabled
2. I2C bypass script enables the subwoofer at hardware level
3. Kernel driver must be blacklisted to prevent reset
4. Combination of hardware enable + EasyEffects preset = best Linux audio

<!-- section_id: "e54fb5a1-1393-4845-937d-2f3d49a4c980" -->
## Recommended Implementation

1. Install i2c-tools package
2. Create I2C bypass script at `/usr/local/bin/2pa-byps.sh`
3. Create systemd service to run script at boot/resume
4. Blacklist `snd_hda_scodec_tas2781_i2c` driver
5. Install EasyEffects with Yoga Pro 9i preset
