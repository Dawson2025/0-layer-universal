---
resource_id: "39886bbe-4505-4ebe-9cbb-ba2645efc4f8"
resource_type: "output"
resource_name: "REQ_001_audio_fixes"
---
# Fixes Applied: Laptop Speaker Audio Enhancement

## Request Reference
REQ_001 - Improve Laptop Speaker Audio Quality

## Date
2026-01-26

## Fix 1: Audio Routing Through EasyEffects

### Problem
Audio was going directly to hardware speakers, bypassing EasyEffects processing entirely.

### Diagnosis
```bash
pactl get-default-sink
# Output: alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink
# Expected: easyeffects_sink
```

### Fix
```bash
pactl set-default-sink easyeffects_sink
```

### Verification
```bash
wpctl status | grep -A 5 "Streams:"
# Should show applications routing to "Easy Effects Sink"
```

### Result
Audio now processes through EasyEffects. User confirmed improvement.

---

## Fix 2: Volume Button Control

### Problem
After routing audio through EasyEffects:
- Volume buttons showed EasyEffects popup
- Actual speaker volume didn't change
- EasyEffects virtual sink stuck at 100%

### Diagnosis
```bash
wpctl status | grep -A 10 "Sinks:"
# Shows:
#   74. ...Speaker + Headphones [vol: 0.58]  <- Hardware (not controlled)
#  *137. Easy Effects Sink [vol: 1.00]       <- Virtual (being controlled)
```

### Fix
Set hardware as default sink (for volume control) while keeping existing app streams routed through EasyEffects:

```bash
pactl set-default-sink alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink
```

### Why This Works
- PipeWire/WirePlumber preserves existing stream routing
- Apps already connected to EasyEffects stay connected
- GNOME now controls hardware volume via default sink
- Volume buttons work again

### Caveat
New applications launched after this change may go directly to hardware. To ensure all apps use EasyEffects:
1. Open EasyEffects application
2. Go to Settings
3. Enable "Process all output streams"

### Verification
```bash
# Check default sink
pactl get-default-sink
# Should be: alsa_output...sofhdadsp__sink

# Check apps still route through EasyEffects
wpctl status | grep -A 5 "Streams:"
# Should show apps -> Easy Effects Sink
```

### Result
Volume buttons now control hardware speaker volume. Audio enhancement still active.

---

## Fix 3: gsd-* Daemon Restart

### Problem
When fixing audio routing, gsd-media-keys and gsd-power crashed again, breaking volume and brightness buttons.

### Fix
Manually restarted daemons:
```bash
DISPLAY=:0 /usr/libexec/gsd-media-keys &
DISPLAY=:0 /usr/libexec/gsd-power &
```

### Long-term Fix
Already configured gsd-keepalive.timer from earlier session (see gsd_keepalive_fix.md).

---

## Summary of Final Configuration

### Audio Chain
```
Applications → EasyEffects Sink → Processing → Hardware Speakers
                    ↑                              ↑
            (apps route here)            (volume controlled here)
```

### Key Settings
| Setting | Value |
|---------|-------|
| Default Sink | Hardware (for volume control) |
| App Routing | EasyEffects (for processing) |
| Active Preset | "Dolby-Like (Framework)" |
| EasyEffects Service | Running via autostart |

### Files
| File | Purpose |
|------|---------|
| `~/.config/easyeffects/output/Dolby-Like (Framework).json` | Active audio preset |
| `~/.config/autostart/com.github.wwmm.easyeffects.desktop` | Auto-start on login |
| `~/.config/systemd/user/gsd-keepalive.timer` | Restart crashed daemons |

### Commands for Manual Recovery
```bash
# If audio effects stop working:
pactl set-default-sink easyeffects_sink
easyeffects --load-preset "Dolby-Like (Framework)"
pactl set-default-sink alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink

# If volume buttons stop working:
DISPLAY=:0 /usr/libexec/gsd-media-keys &
DISPLAY=:0 /usr/libexec/gsd-power &
```
