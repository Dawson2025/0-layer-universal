---
resource_id: "693f3f3b-193a-4a90-bff7-a49c606f9e25"
resource_type: "output"
resource_name: "REQ_001_audio_improvement_research"
---
# Research: Improving Laptop Speaker Audio on Linux

<!-- section_id: "fc4bbdaf-5b6e-4c8e-a9b4-a75edbafc965" -->
## Request Reference
REQ_001 - Improve Laptop Speaker Audio Quality

<!-- section_id: "998350e0-60d8-4b3e-94ee-977d539ef889" -->
## Research Date
2026-01-26

<!-- section_id: "eb46e545-6a3b-4ab6-b6db-a071222491cf" -->
## Executive Summary

Multiple viable approaches exist to significantly improve Linux laptop audio quality. The most promising solutions combine:
1. **AutoEQ frequency response correction** - Science-based EQ profiles
2. **Advanced EasyEffects presets** - Multi-stage processing chains
3. **PipeWire filter-chains** - Low-level audio processing
4. **JamesDSP** - Dolby-like processing with lower latency

<!-- section_id: "c894171d-6b40-4093-92ca-dc2e0a3b13c6" -->
## Key Findings

<!-- section_id: "f470993b-6b2f-4148-8145-3825ca700893" -->
### 1. AutoEQ Profiles (Highest Impact)

AutoEQ generates scientifically-measured equalizer settings that correct frequency response.

**How it works:**
- Measures actual speaker frequency response
- Generates parametric EQ to match target curve
- Can load directly into PipeWire filter-chain

**Resources:**
- https://autoeq.app - Web application
- Can generate PipeWire-compatible configurations
- Works with PipeWire's builtin parametric EQ

**Implementation:**
```bash
# Place generated config in:
~/.config/pipewire/filter-chain.conf.d/
```

<!-- section_id: "22420c2d-1200-4cfc-8de4-c3478033ebfb" -->
### 2. Advanced EasyEffects Presets

Community-developed presets specifically for laptop speakers:

**Best Presets:**
1. **JackHack96/EasyEffects-Presets** - "Advanced Auto Gain" preset
   - GitHub: https://github.com/JackHack96/EasyEffects-Presets
   - Targets laptop speakers
   - Normalizes volume across different media

2. **Framework Community Preset** - "Dolby-like" processing
   - GitHub: https://community.frame.work/t/guide-yet-another-easyeffects-profile/40509
   - Uses exciter for harmonics on highs
   - Multiband compression
   - Reported as "far superior to any EQ profile"

**Recommended Processing Chain:**
1. Limiter (prevent clipping)
2. High-pass filter (130-160 Hz cutoff)
3. Bass Enhancer (harmonic generation, not just EQ boost)
4. Multiband Compressor (balance frequency bands)
5. Stereo Widener (expand soundstage)
6. Exciter (high-frequency presence)

<!-- section_id: "1d50971e-c1e4-45fc-86e6-3b12384efb46" -->
### 3. JamesDSP for Linux (Dolby Alternative)

**What it is:**
- Open-source sound effects for PipeWire
- Lower latency than EasyEffects
- Includes ViPER-DDC for parametric EQ
- Realistic surround effects
- Multiband stereo wideness controller

**GitHub:** https://github.com/Audio4Linux/JDSP4Linux

**Key Features:**
- Convolution engine for impulse responses
- Can load HeSuVi IRs (Dolby Atmos, DTS simulations)
- Real-time EQ adjustment

<!-- section_id: "62f17e73-923a-420f-adac-6eef61c956b7" -->
### 4. PipeWire Filter-Chain (Advanced)

Direct configuration of audio processing in PipeWire:

**Example normalization chain:**
```
~/.config/pipewire/filter-chain.conf.d/normalize.conf
```

Components:
- SC4 compressor (threshold -12dB, ratio 12:1)
- Limiter (boost input, limit to -6dB max)
- Can chain LADSPA/LV2 plugins

<!-- section_id: "35237dd2-cbde-4521-b0ec-c8bf8b53a148" -->
### 5. Virtual Surround Sound

**PipeWire SOFA Spatializer:**
- Built-in to PipeWire filter-chain
- Places sound in 3D space
- Creates binaural stereo output

**HeSuVi Impulse Responses:**
- Recorded from Dolby Atmos Headphone, DTS Headphone:X, Windows Sonic
- Can be loaded via convolution
- Source: https://sourceforge.net/projects/hesuvi/

<!-- section_id: "9b23c7dc-c9c9-476b-b131-d64c3deb211a" -->
### 6. Kernel/Driver Considerations

**Important for Lenovo Yoga Pro 9:**
- Kernel 6.8+ includes critical SOF fixes
- Fixes for "weak sound and lack of volume control"
- GitHub issue tracking: https://github.com/PJungkamp/yoga9-linux/issues/11

**Check current kernel:**
```bash
uname -r
```

<!-- section_id: "3b2dbae5-24ff-4a96-a810-3347c5ff95f6" -->
## Recommended Implementation Order

<!-- section_id: "4be1c62e-c94e-4419-8f34-fa224b1503bf" -->
### Phase 1: Foundation
1. Verify kernel is 6.8+ (or update if needed)
2. Verify ALSA mixer controls work (`alsamixer`)
3. Confirm PipeWire is active (`pactl info`)

<!-- section_id: "39ca76a6-b5aa-4d8e-a02a-ba1d58b238a9" -->
### Phase 2: Frequency Response Correction
1. Generate AutoEQ profile for laptop speakers
2. Implement via PipeWire parametric EQ
3. Test with bass-heavy content

<!-- section_id: "7d148ccc-09f1-4465-a869-4504b00cb718" -->
### Phase 3: Effects Processing
1. Install JamesDSP (lower latency than EasyEffects)
2. Apply "Dolby-like" preset with:
   - Bass enhancer (harmonics, not just boost)
   - Multiband compression
   - Exciter for presence
   - Stereo widening

<!-- section_id: "6f67978a-c290-4c44-8ce0-3e6b4e9bed49" -->
### Phase 4: Fine-tuning
1. Test different content types (music, voice, movies)
2. Create multiple presets for different use cases
3. Consider measurement-based optimization (REW software)

<!-- section_id: "e85d539b-795f-4226-bb38-5a72fa21c192" -->
## Tools to Install

```bash
# JamesDSP (AUR or build from source)
# Better than EasyEffects for this use case

# Already installed:
# - easyeffects
# - calf-plugins

# Additional tools:
sudo apt install lsp-plugins  # More LV2 effects
```

<!-- section_id: "664e0684-0aae-4684-ad90-7015bcb3fcfb" -->
## Realistic Expectations

**What's achievable:**
- Significantly fuller sound
- Better bass perception (through harmonics)
- Wider stereo image
- Clearer vocals
- Consistent volume levels

**What's NOT achievable:**
- Perfect Dolby replication (proprietary algorithms)
- Physical bass below speaker resonance
- Windows-identical sound (different tuning)

<!-- section_id: "e987f8d0-3632-4f8a-a018-e9c05c70ba7f" -->
## Next Steps

1. [ ] Check kernel version, update if < 6.8
2. [ ] Install JamesDSP
3. [ ] Download Framework Community EasyEffects preset
4. [ ] Generate AutoEQ profile if available for Yoga Pro 9
5. [ ] Test and iterate on processing chain
6. [ ] Document final working configuration

<!-- section_id: "29bbe159-dc32-4cf7-ae66-f56bb60baf0d" -->
## Sources

- AutoEQ: https://autoeq.app
- JamesDSP: https://github.com/Audio4Linux/JDSP4Linux
- EasyEffects Presets: https://github.com/JackHack96/EasyEffects-Presets
- Framework Preset: https://community.frame.work/t/guide-yet-another-easyeffects-profile/40509
- PipeWire Filter-Chain Docs: https://docs.pipewire.org/page_module_filter_chain.html
- HeSuVi (surround IRs): https://sourceforge.net/projects/hesuvi/
- Yoga9 Linux Issues: https://github.com/PJungkamp/yoga9-linux/issues/11
