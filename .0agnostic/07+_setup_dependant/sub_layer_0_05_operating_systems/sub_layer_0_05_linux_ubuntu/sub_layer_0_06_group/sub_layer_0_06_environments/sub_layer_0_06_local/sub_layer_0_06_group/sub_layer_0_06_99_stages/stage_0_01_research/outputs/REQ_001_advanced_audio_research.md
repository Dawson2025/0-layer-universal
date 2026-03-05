---
resource_id: "92814683-1181-4433-a4c5-6b5fd9ff92a4"
resource_type: "output"
resource_name: "REQ_001_advanced_audio_research"
---
# Advanced Research: Maximum Audio Quality on Linux

<!-- section_id: "b0f880d8-fdcf-4d4d-84a0-6f5a6d5ec153" -->
## Request Reference
REQ_001 - Improve Laptop Speaker Audio Quality

<!-- section_id: "509e88f3-83d5-4747-9576-e8ee9b1564f9" -->
## Date
2026-01-26

<!-- section_id: "11456edc-c44a-42c0-bd01-27bf1f1c154a" -->
## Executive Summary

**CRITICAL DISCOVERY**: The Yoga Pro 9's bass speakers (TAS2781 Smart Amplifiers) may not be properly initialized on Linux, meaning bass speakers could be completely non-functional. This must be fixed BEFORE any software processing will help.

<!-- section_id: "7c38193a-2276-46e4-abcd-64095a833b3f" -->
## Critical Finding #1: Hardware Not Fully Enabled

<!-- section_id: "a97522a5-dcb0-4e56-b87c-4bacbf1e1133" -->
### The Problem
The Yoga Pro 9 16IMH9 has:
- Realtek ALC3306 codec (misidentified as ALC287 by Linux)
- Texas Instruments TAS2781 Smart Amplifier for bass speakers
- 6 speakers (2W dual side woofers + 2W tweeters)

**On Linux, the TAS2781 amplifiers are NOT properly initialized**, causing:
- Bass speakers completely silent or severely attenuated
- Only tweeters producing sound
- Massively degraded audio compared to Windows

<!-- section_id: "5379ff4d-93cd-4c1e-9b6d-39eca2d3c027" -->
### The Fix
A dedicated project exists: **https://github.com/maximmaxim345/yoga_pro_9i_gen9_linux**

This requires:
1. Creating a systemd service that configures the TAS2781 via I2C
2. Running at boot AND after resume from sleep
3. Properly initializing the bass speaker amplifiers

**This is likely why audio sounds so much worse than Windows - the bass speakers aren't even working!**

---

<!-- section_id: "28646094-510c-4d49-85cb-5017eaf5b3a0" -->
## Critical Finding #2: Dolby Impulse Response Extraction

<!-- section_id: "fd2dd46b-5159-4477-9133-7a570021293b" -->
### What's Possible
You CAN extract the actual Dolby Atmos processing from Windows and use it on Linux!

<!-- section_id: "1a27ce72-b903-4d75-98be-2b31cb51b28c" -->
### How It Works
1. On Windows with Dolby enabled, play an impulse audio file
2. Simultaneously record the output through WASAPI loopback
3. Process the recording to extract the impulse response
4. Use that .irs file in EasyEffects Convolver on Linux

<!-- section_id: "7e6fc3c8-fda4-4f1b-8380-2ee7eeda2be5" -->
### Project with Instructions
**https://github.com/shuhaowu/linux-thinkpad-speaker-improvements**

Provides:
- Step-by-step capture procedure
- Pre-captured impulse responses for various ThinkPads
- EasyEffects configuration guidance

<!-- section_id: "4166e75b-8fdd-432a-9f2f-258b65ceb759" -->
### Key Notes
- Impulse response is device-specific (must match exact model)
- Add Limiter AFTER Convolver to prevent clipping
- May need to capture your own if Yoga Pro 9 isn't in the database

---

<!-- section_id: "864f3e17-3487-498f-b0a0-393417062476" -->
## Finding #3: JamesDSP vs EasyEffects

<!-- section_id: "5b72de9e-7a22-43d2-90c8-0200148c8737" -->
### EasyEffects (Recommended for most users)
- Better stability
- Direct PipeWire integration
- Simpler configuration
- Sufficient for most needs

<!-- section_id: "d0732ce9-83b9-44a5-9020-349bc0ef827b" -->
### JamesDSP (For power users)
- More sophisticated processing
- EEL2 scripting engine for custom effects
- ViPER-DDC support
- AutoEQ database integration
- Lower latency potential
- Higher CPU usage

**Recommendation**: Start with EasyEffects. Switch to JamesDSP only if you need custom scripting or ViPER-DDC.

---

<!-- section_id: "aef04f66-fd73-47ab-8ea1-8f1f57d4eae5" -->
## Finding #4: No AutoEQ Profiles Exist

No professional measurements exist for the Yoga Pro 9 speakers.

<!-- section_id: "f2cf815d-3903-4e6b-a1a1-169ca1f4e427" -->
### Options:
1. **Measure yourself** using Room EQ Wizard (REW) with calibrated microphone
2. **Use generic laptop speaker profiles** as starting point
3. **Extract Dolby impulse response** (better option)

---

<!-- section_id: "f9fff662-aca4-4666-9a64-523bb4061f50" -->
## Finding #5: Wine/VM Approach Not Viable

Running Windows Dolby software through Wine or VM is **not practical**:
- Wine doesn't support multichannel DSP properly
- DirectSound limitations
- Can't access hardware amplifiers
- Latency issues in VM

**Conclusion**: Native Linux solutions (EasyEffects + Convolution) are superior.

---

<!-- section_id: "a4bed94d-e4c2-4d21-afa4-2425a5bb4b68" -->
## Finding #6: PipeWire Filter-Chain

For maximum quality, implement processing at PipeWire level:
- Lower latency than application-level
- Guaranteed to process all audio
- Supports LADSPA/LV2 plugins
- Can combine convolution + EQ + limiting

Configuration location: `~/.config/pipewire/filter-chain.conf.d/`

---

<!-- section_id: "ba8721e8-8d1a-4a59-99ab-d08c2c81484d" -->
## Recommended Implementation Path

<!-- section_id: "6a2b3940-e0fc-4e4b-a20e-39b1c60a7c3b" -->
### Phase 1: FIX THE HARDWARE (CRITICAL)
```
Priority: HIGHEST
```
1. Check if bass speakers are actually working
2. Implement TAS2781 amplifier fix from yoga_pro_9i_gen9_linux repo
3. Verify all 6 speakers produce sound

<!-- section_id: "99bae764-cc68-49fa-aa8b-015706398ef9" -->
### Phase 2: Capture Dolby Impulse Response
```
Priority: HIGH (if Windows available)
```
1. Boot into Windows
2. Follow impulse capture procedure
3. Generate .irs file
4. Import into EasyEffects Convolver

<!-- section_id: "88ba2c94-93e4-433d-a39b-dbe64e6972bb" -->
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

<!-- section_id: "8ea7fcf3-4ca9-49ce-910f-fb2073275489" -->
### Phase 4: Advanced (Optional)
- JamesDSP for custom scripting
- Room measurement with REW
- PipeWire filter-chain for system-level processing

---

<!-- section_id: "0e0ef2f9-733f-44a2-a693-e188c0c152d5" -->
## Resources

<!-- section_id: "91e20a84-30a9-4380-9334-d8d78a64e214" -->
### Yoga Pro 9 Linux Support
- https://github.com/maximmaxim345/yoga_pro_9i_gen9_linux

<!-- section_id: "11658f9c-bddf-4037-8cf8-6b82972f6600" -->
### Dolby Impulse Response Capture
- https://github.com/shuhaowu/linux-thinkpad-speaker-improvements

<!-- section_id: "7802159b-3172-4d6b-8feb-06003befc5b4" -->
### JamesDSP
- https://github.com/Audio4Linux/JDSP4Linux

<!-- section_id: "685c2642-c0b7-4783-8ecb-a8862c574e92" -->
### Room EQ Wizard (Measurement)
- https://www.roomeqwizard.com

<!-- section_id: "80487632-7bc7-4bdc-a423-7bd83f26e371" -->
### AutoEQ Database
- https://github.com/jaakkopasanen/AutoEq

---

<!-- section_id: "af649773-ea71-422f-a1c7-3d421c85e0ed" -->
## Expected Outcome

If Phase 1 (hardware fix) is successful:
- **Dramatic improvement** - bass speakers will actually work
- Combined with Dolby impulse response: near-Windows quality
- May exceed Windows in some aspects due to customization

If hardware is already working correctly:
- Impulse response convolution: significant improvement
- Still won't perfectly match Windows without proper amplifier config

---

<!-- section_id: "4508c568-040a-4b43-9585-531ee2f6e32f" -->
## Action Items

1. [ ] **VERIFY** if bass speakers are currently producing sound
2. [ ] **IMPLEMENT** TAS2781 amplifier fix if needed
3. [ ] **CAPTURE** Dolby impulse response from Windows (if accessible)
4. [ ] **CONFIGURE** EasyEffects with convolution + limiting
5. [ ] **TEST** and iterate on processing chain
