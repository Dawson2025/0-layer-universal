# Research: Yoga Pro 9 Speaker I2C Configuration

## Request Reference
REQ_002 - Fix Yoga Pro 9 Subwoofer/Speaker Quality on Linux

## Date
2026-01-26

## Problem Statement

Linux audio on Lenovo Yoga Pro 9 sounds significantly worse than Windows:
- Thin, weak sound lacking bass
- Sound quality noticeably inferior to Windows Dolby Atmos
- Previous EasyEffects attempts improved but didn't match Windows

## Research Sources

### Primary Source
**GitHub Repository**: [maximmaxim345/yoga_pro_9i_gen9_linux](https://github.com/maximmaxim345/yoga_pro_9i_gen9_linux)

### Related Resources
- [Kernel Bug Report #217449](https://bugzilla.kernel.org/show_bug.cgi?id=217449)
- [GitHub Issue: karypid/YogaPro-16IMH9#2](https://github.com/karypid/YogaPro-16IMH9/issues/2)
- Perplexity deep research on Linux laptop audio optimization

## Key Findings

### Finding 1: Subwoofer Disabled by Default

The Yoga Pro 9 subwoofer is **disabled by default** on Linux due to a kernel bug:

> "Speakers require some configuration. Subwoofer is disabled by default due to a bug"

This explains why Linux audio lacked bass - the bass speakers weren't even active.

### Finding 2: I2C Bypass Script Required

The subwoofer can be enabled via I2C commands to the TAS2781 amplifier:
- Script: `2pa-byps.sh`
- Sends specific I2C register values to addresses 0x3f and 0x38
- Must run at boot and after sleep/hibernate

### Finding 3: Kernel Driver Conflict

The `snd_hda_scodec_tas2781_i2c` kernel driver **resets** the I2C configuration:
- Driver is loaded by default
- Overwrites manual I2C settings
- Causes sound to revert to weak state after script runs

**Solution**: Blacklist the driver in `/etc/modprobe.d/`

### Finding 4: Model-Specific Configuration

Different Yoga Pro 9 variants require different I2C addresses:
- Model 83BY (16IRP8): addresses 0x39, 0x38, 0x3d, 0x3b
- Model 83DN (16IMH9): addresses 0x3f, 0x38
- Model 83L0 (16IAH10): uses different I2C bus index

### Finding 5: EasyEffects Presets Available

The GitHub repo includes pre-tuned EasyEffects presets:
- `Yoga Pro 9i gen 9.json`
- `Yoga Pro 9i gen 9 v2.json`
- `Yoga Pro 9i gen 9 v2 less bass.json`

## Conclusions

1. The weak audio was NOT just missing Dolby processing - the subwoofer hardware was disabled
2. I2C bypass script enables the subwoofer at hardware level
3. Kernel driver must be blacklisted to prevent reset
4. Combination of hardware enable + EasyEffects preset = best Linux audio

## Recommended Implementation

1. Install i2c-tools package
2. Create I2C bypass script at `/usr/local/bin/2pa-byps.sh`
3. Create systemd service to run script at boot/resume
4. Blacklist `snd_hda_scodec_tas2781_i2c` driver
5. Install EasyEffects with Yoga Pro 9i preset
