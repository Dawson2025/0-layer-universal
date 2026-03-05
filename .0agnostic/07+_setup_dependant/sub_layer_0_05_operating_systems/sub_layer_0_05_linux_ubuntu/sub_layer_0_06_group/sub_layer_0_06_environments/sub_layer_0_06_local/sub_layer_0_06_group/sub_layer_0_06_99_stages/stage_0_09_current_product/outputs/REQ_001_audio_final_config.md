---
resource_id: "b66f056e-3c77-4bf7-80f9-69b180dcaf78"
resource_type: "output"
resource_name: "REQ_001_audio_final_config"
---
# Final Configuration: Laptop Speaker Audio Enhancement

<!-- section_id: "72270ac2-e097-4966-bfd2-42fc7f5db075" -->
## Request Reference
REQ_001 - Improve Laptop Speaker Audio Quality

<!-- section_id: "672f1ab9-8691-45c6-ad70-1204a28bd973" -->
## Date
2026-01-26

<!-- section_id: "2dc9ab20-c271-43cb-ac37-5a887b42bec6" -->
## Status
**IMPLEMENTED** - Using captured Windows Dolby impulse response via convolution

<!-- section_id: "cc4b21fe-2036-48d7-ac3e-c45506f8473d" -->
## Current Configuration

<!-- section_id: "121d31ca-720d-49b0-b948-c07ae625c5db" -->
### Audio Processing Chain
```
┌─────────────┐     ┌─────────────────┐     ┌──────────────────┐
│ Applications│ ──▶ │  EasyEffects    │ ──▶ │ Hardware Speakers│
│  (Chrome,   │     │  (processing)   │     │  (volume here)   │
│   etc.)     │     │                 │     │                  │
└─────────────┘     └─────────────────┘     └──────────────────┘
```

<!-- section_id: "33413b33-7bb5-45e9-9183-9c772dbfca62" -->
### Active Preset: "Dolby Atmos (Captured)"

**Processing Chain:**
1. **Convolver** - Applies captured Windows Dolby Atmos impulse response
2. **Limiter** - Prevents distortion at high volumes

**Impulse Response:**
- File: `~/.config/easyeffects/irs/dolby_yoga_pro_9.irs`
- Source: Captured from Windows 11 Dolby Atmos processing
- Format: WAV 32-bit float, stereo, 44100Hz, 0.33 seconds
- Method: VLC + Audacity WASAPI loopback recording

<!-- section_id: "5a3c9418-9b39-480d-b72d-e0932df7d0e0" -->
### Volume Control
- **Default Sink:** Hardware speakers (for GNOME volume control)
- **App Routing:** EasyEffects sink (for audio processing)
- **Volume Buttons:** Working, control hardware volume

---

<!-- section_id: "51cc6a22-37ae-44f5-b8f6-e09638d72b8b" -->
## Installed Components

<!-- section_id: "26c52d42-2246-4f05-b06a-bd3a86e128d8" -->
### Packages
```bash
sudo apt install easyeffects calf-plugins lsp-plugins
```

<!-- section_id: "6ffd56b7-2286-4d37-8b29-56fe5ac4be98" -->
### Presets Available
| Preset | Description | Use Case |
|--------|-------------|----------|
| Dolby Atmos (Captured) | Convolver with captured Windows Dolby IR | **Current - Closest to Windows** |
| Dolby-Like (Framework) | Multiband compression + bass + stereo | General use fallback |
| Advanced Auto Gain | Volume normalization + laptop optimization | Inconsistent volume sources |
| Bass Enhancing + Perfect EQ | EQ-focused approach | Music listening |
| Bass Boosted | Heavy bass emphasis | Bass-heavy content |
| LaptopSpeakers | Basic custom preset | Fallback |

<!-- section_id: "bc0e4e10-ba44-4620-ada5-adf8d72ec539" -->
### Services
| Service | Status | Purpose |
|---------|--------|---------|
| EasyEffects | Autostart | Audio processing |
| gsd-keepalive.timer | Enabled | Restart volume/brightness daemons |

---

<!-- section_id: "56d5db3f-527d-469d-b45a-d7c7f2c8de59" -->
## How to Use

<!-- section_id: "322813f4-370f-4f01-ae6e-7e16debf102c" -->
### Switch Presets
```bash
easyeffects --load-preset "Dolby Atmos (Captured)"
easyeffects --load-preset "Dolby-Like (Framework)"
easyeffects --load-preset "Advanced Auto Gain"
easyeffects --load-preset "Bass Boosted"
```

<!-- section_id: "e4bd8a3e-5976-4ec7-9d90-4dececc8582e" -->
### Open GUI
Launch "Easy Effects" from application menu to:
- Adjust individual effect parameters
- Monitor audio levels
- Create custom presets

<!-- section_id: "59a817c3-ebcb-481c-bb83-db80c26a126c" -->
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

<!-- section_id: "6f5425fe-ef65-4e44-a571-8538b91204c5" -->
### If No Audio Sinks Available (auto_null only)
```bash
# Check WirePlumber status
systemctl --user status wireplumber

# If failed, reset and restart
systemctl --user reset-failed wireplumber
systemctl --user restart pipewire pipewire-pulse wireplumber
```

<!-- section_id: "f3a6d9b0-1623-4120-8542-38b4a891d99b" -->
### If Volume Buttons Stop
```bash
# Restart GNOME settings daemons
DISPLAY=:0 /usr/libexec/gsd-media-keys &
DISPLAY=:0 /usr/libexec/gsd-power &
```

---

<!-- section_id: "b4ed97f7-c1d8-4ad8-9b69-1ea590648b55" -->
## Limitations

<!-- section_id: "906e1377-9a8f-43bd-a2c5-43cf829e12d5" -->
### What Works
- ✅ Captured Dolby Atmos processing via convolution
- ✅ Same frequency response as Windows (via impulse response)
- ✅ Volume buttons control hardware
- ✅ EasyEffects processes all audio
- ✅ Distortion prevention via limiter

<!-- section_id: "57e28a0a-7402-4446-b00b-6ee7b1947d49" -->
### Remaining Differences
- ⚠️ Convolution is a linear approximation of Dolby processing
- ⚠️ Dolby's dynamic/adaptive processing isn't captured in IR
- ⚠️ No real-time spatial audio adaptation

<!-- section_id: "4b050298-3a94-4c41-a75f-889480eb21e5" -->
### Known Issues
1. **New apps may bypass EasyEffects** - Enable "Process all output streams" in EasyEffects settings
2. **Volume OSD shows wrong device** - Cosmetic issue, volume still works
3. **Requires EasyEffects running** - Included in autostart

---

<!-- section_id: "bce7c622-141b-478f-81c0-976a84a88d04" -->
## Future Improvements

1. **JamesDSP** - Lower latency alternative with ViPER-DDC
2. **AutoEQ** - Generate measurement-based profile for Yoga Pro 9
3. **PipeWire filter-chain** - Native processing without EasyEffects
4. **Custom measurement** - Use REW to measure and correct specific room/position

---

<!-- section_id: "d3a59185-f6f4-4a39-8964-f917a9c02f9d" -->
## Files

| File | Purpose |
|------|---------|
| `~/.config/easyeffects/irs/dolby_yoga_pro_9.irs` | Captured Dolby Atmos impulse response |
| `~/.config/easyeffects/output/Dolby Atmos (Captured).json` | Active audio preset |
| `~/.config/autostart/com.github.wwmm.easyeffects.desktop` | Auto-start on login |
| `~/.config/systemd/user/gsd-keepalive.timer` | Restart crashed daemons |

<!-- section_id: "0d0aed7f-c3cb-4163-90f7-1fa8aebf818d" -->
## Related Documentation
- Research: `stage_0_01_research/outputs/REQ_001_audio_improvement_research.md`
- Advanced Research: `stage_0_01_research/outputs/REQ_001_advanced_audio_research.md`
- Windows Instructions: `stage_0_05_development/outputs/WINDOWS_INSTRUCTIONS_capture_dolby_impulse.md`
- Implementation: `stage_0_05_development/outputs/REQ_001_audio_implementation.md`
- Testing: `stage_0_06_testing/outputs/REQ_001_audio_testing.md`
- Fixes: `stage_0_08_fixing/outputs/REQ_001_audio_fixes.md`
- WirePlumber Fix: `stage_0_09_current_product/outputs/wireplumber_crash_fix.md`
