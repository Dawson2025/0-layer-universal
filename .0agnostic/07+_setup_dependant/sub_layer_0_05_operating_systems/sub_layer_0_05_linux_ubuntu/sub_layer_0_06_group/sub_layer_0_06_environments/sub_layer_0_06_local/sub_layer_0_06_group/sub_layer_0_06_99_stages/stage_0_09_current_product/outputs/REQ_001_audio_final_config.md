# Final Configuration: Laptop Speaker Audio Enhancement

## Request Reference
REQ_001 - Improve Laptop Speaker Audio Quality

## Date
2026-01-26

## Status
**IMPLEMENTED** - Using captured Windows Dolby impulse response via convolution

## Current Configuration

### Audio Processing Chain
```
┌─────────────┐     ┌─────────────────┐     ┌──────────────────┐
│ Applications│ ──▶ │  EasyEffects    │ ──▶ │ Hardware Speakers│
│  (Chrome,   │     │  (processing)   │     │  (volume here)   │
│   etc.)     │     │                 │     │                  │
└─────────────┘     └─────────────────┘     └──────────────────┘
```

### Active Preset: "Dolby Atmos (Captured)"

**Processing Chain:**
1. **Convolver** - Applies captured Windows Dolby Atmos impulse response
2. **Limiter** - Prevents distortion at high volumes

**Impulse Response:**
- File: `~/.config/easyeffects/irs/dolby_yoga_pro_9.irs`
- Source: Captured from Windows 11 Dolby Atmos processing
- Format: WAV 32-bit float, stereo, 44100Hz, 0.33 seconds
- Method: VLC + Audacity WASAPI loopback recording

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
| Dolby Atmos (Captured) | Convolver with captured Windows Dolby IR | **Current - Closest to Windows** |
| Dolby-Like (Framework) | Multiband compression + bass + stereo | General use fallback |
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
easyeffects --load-preset "Dolby Atmos (Captured)"
easyeffects --load-preset "Dolby-Like (Framework)"
easyeffects --load-preset "Advanced Auto Gain"
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
sleep 3
easyeffects --load-preset "Dolby Atmos (Captured)"

# Ensure routing
pactl set-default-sink easyeffects_sink
sleep 2
pactl set-default-sink alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink
```

### If No Audio Sinks Available (auto_null only)
```bash
# Check WirePlumber status
systemctl --user status wireplumber

# If failed, reset and restart
systemctl --user reset-failed wireplumber
systemctl --user restart pipewire pipewire-pulse wireplumber
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
- ✅ Captured Dolby Atmos processing via convolution
- ✅ Same frequency response as Windows (via impulse response)
- ✅ Volume buttons control hardware
- ✅ EasyEffects processes all audio
- ✅ Distortion prevention via limiter

### Remaining Differences
- ⚠️ Convolution is a linear approximation of Dolby processing
- ⚠️ Dolby's dynamic/adaptive processing isn't captured in IR
- ⚠️ No real-time spatial audio adaptation

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

## Files

| File | Purpose |
|------|---------|
| `~/.config/easyeffects/irs/dolby_yoga_pro_9.irs` | Captured Dolby Atmos impulse response |
| `~/.config/easyeffects/output/Dolby Atmos (Captured).json` | Active audio preset |
| `~/.config/autostart/com.github.wwmm.easyeffects.desktop` | Auto-start on login |
| `~/.config/systemd/user/gsd-keepalive.timer` | Restart crashed daemons |

## Related Documentation
- Research: `stage_0_01_research/outputs/REQ_001_audio_improvement_research.md`
- Advanced Research: `stage_0_01_research/outputs/REQ_001_advanced_audio_research.md`
- Windows Instructions: `stage_0_05_development/outputs/WINDOWS_INSTRUCTIONS_capture_dolby_impulse.md`
- Implementation: `stage_0_05_development/outputs/REQ_001_audio_implementation.md`
- Testing: `stage_0_06_testing/outputs/REQ_001_audio_testing.md`
- Fixes: `stage_0_08_fixing/outputs/REQ_001_audio_fixes.md`
- WirePlumber Fix: `stage_0_09_current_product/outputs/wireplumber_crash_fix.md`
