# Final Configuration: Laptop Speaker Audio Enhancement

## Request Reference
REQ_001 - Improve Laptop Speaker Audio Quality

## Date
2026-01-26

## Status
**IMPLEMENTED** - Audio quality improved, not Windows-equivalent

## Current Configuration

### Audio Processing Chain
```
┌─────────────┐     ┌─────────────────┐     ┌──────────────────┐
│ Applications│ ──▶ │  EasyEffects    │ ──▶ │ Hardware Speakers│
│  (Chrome,   │     │  (processing)   │     │  (volume here)   │
│   etc.)     │     │                 │     │                  │
└─────────────┘     └─────────────────┘     └──────────────────┘
```

### Active Preset: "Dolby-Like (Framework)"

**Processing Chain:**
1. **High-pass Filter** (120Hz) - Removes sub-bass speakers can't reproduce
2. **Bass Enhancer** - Harmonic generation for perceived bass depth
3. **Exciter** - High-frequency presence and detail
4. **Multiband Compressor** (4 bands) - Balances frequency ranges
5. **Stereo Tools** - 30% stereo base widening
6. **Limiter** - Prevents distortion at high volumes

### Volume Control
- **Default Sink:** Hardware speakers (for GNOME volume control)
- **App Routing:** EasyEffects sink (for audio processing)
- **Volume Buttons:** Working, control hardware volume

---

## Installed Components

### Packages
```bash
sudo apt install easyeffects calf-plugins lsp-plugins
```

### Presets Available
| Preset | Description | Use Case |
|--------|-------------|----------|
| Dolby-Like (Framework) | Multiband compression + bass + stereo | **Current - Best for general use** |
| Advanced Auto Gain | Volume normalization + laptop optimization | Inconsistent volume sources |
| Bass Enhancing + Perfect EQ | EQ-focused approach | Music listening |
| Bass Boosted | Heavy bass emphasis | Bass-heavy content |
| LaptopSpeakers | Basic custom preset | Fallback |

### Services
| Service | Status | Purpose |
|---------|--------|---------|
| EasyEffects | Autostart | Audio processing |
| gsd-keepalive.timer | Enabled | Restart volume/brightness daemons |

---

## How to Use

### Switch Presets
```bash
easyeffects --load-preset "Advanced Auto Gain"
easyeffects --load-preset "Dolby-Like (Framework)"
easyeffects --load-preset "Bass Boosted"
```

### Open GUI
Launch "Easy Effects" from application menu to:
- Adjust individual effect parameters
- Monitor audio levels
- Create custom presets

### If Audio Processing Stops
```bash
# Restart EasyEffects
pkill easyeffects
easyeffects --gapplication-service &
easyeffects --load-preset "Dolby-Like (Framework)"

# Ensure routing
pactl set-default-sink easyeffects_sink
sleep 2
pactl set-default-sink alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink
```

### If Volume Buttons Stop
```bash
# Restart GNOME settings daemons
DISPLAY=:0 /usr/libexec/gsd-media-keys &
DISPLAY=:0 /usr/libexec/gsd-power &
```

---

## Limitations

### What Works
- ✅ Fuller bass (via harmonic generation)
- ✅ Wider stereo image
- ✅ Better dynamics
- ✅ Volume normalization
- ✅ Distortion prevention

### What Doesn't Match Windows
- ❌ Proprietary Dolby Atmos spatial processing
- ❌ Lenovo-specific speaker calibration profiles
- ❌ Hardware DSP tuning
- ❌ Exact Windows audio quality

### Known Issues
1. **New apps may bypass EasyEffects** - Enable "Process all output streams" in EasyEffects settings
2. **Volume OSD shows wrong device** - Cosmetic issue, volume still works
3. **Requires EasyEffects running** - Included in autostart

---

## Future Improvements

1. **JamesDSP** - Lower latency alternative with ViPER-DDC
2. **AutoEQ** - Generate measurement-based profile for Yoga Pro 9
3. **PipeWire filter-chain** - Native processing without EasyEffects
4. **Custom measurement** - Use REW to measure and correct specific room/position

---

## Related Documentation
- Research: `stage_0_01_research/outputs/REQ_001_audio_improvement_research.md`
- Implementation: `stage_0_05_development/outputs/REQ_001_audio_implementation.md`
- Testing: `stage_0_06_testing/outputs/REQ_001_audio_testing.md`
- Fixes: `stage_0_08_fixing/outputs/REQ_001_audio_fixes.md`
