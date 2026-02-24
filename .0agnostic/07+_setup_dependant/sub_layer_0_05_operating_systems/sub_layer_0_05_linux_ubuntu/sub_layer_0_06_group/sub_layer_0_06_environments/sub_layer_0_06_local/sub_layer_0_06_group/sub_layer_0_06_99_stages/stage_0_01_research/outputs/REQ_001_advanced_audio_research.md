# Advanced Research: Maximum Audio Quality on Linux

## Request Reference
REQ_001 - Improve Laptop Speaker Audio Quality

## Date
2026-01-26

## Executive Summary

**CRITICAL DISCOVERY**: The Yoga Pro 9's bass speakers (TAS2781 Smart Amplifiers) may not be properly initialized on Linux, meaning bass speakers could be completely non-functional. This must be fixed BEFORE any software processing will help.

## Critical Finding #1: Hardware Not Fully Enabled

### The Problem
The Yoga Pro 9 16IMH9 has:
- Realtek ALC3306 codec (misidentified as ALC287 by Linux)
- Texas Instruments TAS2781 Smart Amplifier for bass speakers
- 6 speakers (2W dual side woofers + 2W tweeters)

**On Linux, the TAS2781 amplifiers are NOT properly initialized**, causing:
- Bass speakers completely silent or severely attenuated
- Only tweeters producing sound
- Massively degraded audio compared to Windows

### The Fix
A dedicated project exists: **https://github.com/maximmaxim345/yoga_pro_9i_gen9_linux**

This requires:
1. Creating a systemd service that configures the TAS2781 via I2C
2. Running at boot AND after resume from sleep
3. Properly initializing the bass speaker amplifiers

**This is likely why audio sounds so much worse than Windows - the bass speakers aren't even working!**

---

## Critical Finding #2: Dolby Impulse Response Extraction

### What's Possible
You CAN extract the actual Dolby Atmos processing from Windows and use it on Linux!

### How It Works
1. On Windows with Dolby enabled, play an impulse audio file
2. Simultaneously record the output through WASAPI loopback
3. Process the recording to extract the impulse response
4. Use that .irs file in EasyEffects Convolver on Linux

### Project with Instructions
**https://github.com/shuhaowu/linux-thinkpad-speaker-improvements**

Provides:
- Step-by-step capture procedure
- Pre-captured impulse responses for various ThinkPads
- EasyEffects configuration guidance

### Key Notes
- Impulse response is device-specific (must match exact model)
- Add Limiter AFTER Convolver to prevent clipping
- May need to capture your own if Yoga Pro 9 isn't in the database

---

## Finding #3: JamesDSP vs EasyEffects

### EasyEffects (Recommended for most users)
- Better stability
- Direct PipeWire integration
- Simpler configuration
- Sufficient for most needs

### JamesDSP (For power users)
- More sophisticated processing
- EEL2 scripting engine for custom effects
- ViPER-DDC support
- AutoEQ database integration
- Lower latency potential
- Higher CPU usage

**Recommendation**: Start with EasyEffects. Switch to JamesDSP only if you need custom scripting or ViPER-DDC.

---

## Finding #4: No AutoEQ Profiles Exist

No professional measurements exist for the Yoga Pro 9 speakers.

### Options:
1. **Measure yourself** using Room EQ Wizard (REW) with calibrated microphone
2. **Use generic laptop speaker profiles** as starting point
3. **Extract Dolby impulse response** (better option)

---

## Finding #5: Wine/VM Approach Not Viable

Running Windows Dolby software through Wine or VM is **not practical**:
- Wine doesn't support multichannel DSP properly
- DirectSound limitations
- Can't access hardware amplifiers
- Latency issues in VM

**Conclusion**: Native Linux solutions (EasyEffects + Convolution) are superior.

---

## Finding #6: PipeWire Filter-Chain

For maximum quality, implement processing at PipeWire level:
- Lower latency than application-level
- Guaranteed to process all audio
- Supports LADSPA/LV2 plugins
- Can combine convolution + EQ + limiting

Configuration location: `~/.config/pipewire/filter-chain.conf.d/`

---

## Recommended Implementation Path

### Phase 1: FIX THE HARDWARE (CRITICAL)
```
Priority: HIGHEST
```
1. Check if bass speakers are actually working
2. Implement TAS2781 amplifier fix from yoga_pro_9i_gen9_linux repo
3. Verify all 6 speakers produce sound

### Phase 2: Capture Dolby Impulse Response
```
Priority: HIGH (if Windows available)
```
1. Boot into Windows
2. Follow impulse capture procedure
3. Generate .irs file
4. Import into EasyEffects Convolver

### Phase 3: Optimize Processing Chain
```
Priority: MEDIUM
```
Recommended chain:
1. High-pass filter (remove sub-bass)
2. Convolver (Dolby impulse response)
3. Parametric EQ (fine-tuning)
4. Multiband Compressor (dynamics)
5. Limiter (0dB threshold, prevent clipping)

### Phase 4: Advanced (Optional)
- JamesDSP for custom scripting
- Room measurement with REW
- PipeWire filter-chain for system-level processing

---

## Resources

### Yoga Pro 9 Linux Support
- https://github.com/maximmaxim345/yoga_pro_9i_gen9_linux

### Dolby Impulse Response Capture
- https://github.com/shuhaowu/linux-thinkpad-speaker-improvements

### JamesDSP
- https://github.com/Audio4Linux/JDSP4Linux

### Room EQ Wizard (Measurement)
- https://www.roomeqwizard.com

### AutoEQ Database
- https://github.com/jaakkopasanen/AutoEq

---

## Expected Outcome

If Phase 1 (hardware fix) is successful:
- **Dramatic improvement** - bass speakers will actually work
- Combined with Dolby impulse response: near-Windows quality
- May exceed Windows in some aspects due to customization

If hardware is already working correctly:
- Impulse response convolution: significant improvement
- Still won't perfectly match Windows without proper amplifier config

---

## Action Items

1. [ ] **VERIFY** if bass speakers are currently producing sound
2. [ ] **IMPLEMENT** TAS2781 amplifier fix if needed
3. [ ] **CAPTURE** Dolby impulse response from Windows (if accessible)
4. [ ] **CONFIGURE** EasyEffects with convolution + limiting
5. [ ] **TEST** and iterate on processing chain
