---
resource_id: "39886bbe-4505-4ebe-9cbb-ba2645efc4f8"
resource_type: "output"
resource_name: "REQ_001_audio_fixes"
---
# Fixes Applied: Laptop Speaker Audio Enhancement

<!-- section_id: "6945ba84-4061-424a-9b3e-5d585f0c30a8" -->
## Request Reference
REQ_001 - Improve Laptop Speaker Audio Quality

<!-- section_id: "07a57637-2574-480f-b901-b474a3f0dd72" -->
## Date
2026-01-26

<!-- section_id: "8aac7e9c-6dd7-4e4e-a679-78f57b45c612" -->
## Fix 1: Audio Routing Through EasyEffects

<!-- section_id: "b1154e75-1384-4bb0-8f27-e433544e2d8a" -->
### Problem
Audio was going directly to hardware speakers, bypassing EasyEffects processing entirely.

<!-- section_id: "3350b062-808a-4024-a33b-35f3661c96ff" -->
### Diagnosis
```bash
pactl get-default-sink
# Output: alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink
# Expected: easyeffects_sink
```

<!-- section_id: "d205d3f4-e270-4e65-8969-e78e3d5058e8" -->
### Fix
```bash
pactl set-default-sink easyeffects_sink
```

<!-- section_id: "4bdf566f-3d2d-49d8-9ca0-581e7d043eaa" -->
### Verification
```bash
wpctl status | grep -A 5 "Streams:"
# Should show applications routing to "Easy Effects Sink"
```

<!-- section_id: "587c9c64-a1e8-433c-80ef-05d874cc6b47" -->
### Result
Audio now processes through EasyEffects. User confirmed improvement.

---

<!-- section_id: "c5a9cf7d-80bd-429e-bebc-a23c51ea4498" -->
## Fix 2: Volume Button Control

<!-- section_id: "83f1f418-1e04-4caa-8dde-2f466272063a" -->
### Problem
After routing audio through EasyEffects:
- Volume buttons showed EasyEffects popup
- Actual speaker volume didn't change
- EasyEffects virtual sink stuck at 100%

<!-- section_id: "18b7faa7-3b42-4b6a-9177-f2c3d252fa88" -->
### Diagnosis
```bash
wpctl status | grep -A 10 "Sinks:"
# Shows:
#   74. ...Speaker + Headphones [vol: 0.58]  <- Hardware (not controlled)
#  *137. Easy Effects Sink [vol: 1.00]       <- Virtual (being controlled)
```

<!-- section_id: "1fd482fd-a982-4839-87b9-f974edec7d85" -->
### Fix
Set hardware as default sink (for volume control) while keeping existing app streams routed through EasyEffects:

```bash
pactl set-default-sink alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink
```

<!-- section_id: "1a0a44f6-e571-4fb9-9d38-145e974f423e" -->
### Why This Works
- PipeWire/WirePlumber preserves existing stream routing
- Apps already connected to EasyEffects stay connected
- GNOME now controls hardware volume via default sink
- Volume buttons work again

<!-- section_id: "bf20e1de-cc0b-4bc2-bc68-2c36f2345edc" -->
### Caveat
New applications launched after this change may go directly to hardware. To ensure all apps use EasyEffects:
1. Open EasyEffects application
2. Go to Settings
3. Enable "Process all output streams"

<!-- section_id: "6f798b0b-1a87-4a93-b532-234b8145c923" -->
### Verification
```bash
# Check default sink
pactl get-default-sink
# Should be: alsa_output...sofhdadsp__sink

# Check apps still route through EasyEffects
wpctl status | grep -A 5 "Streams:"
# Should show apps -> Easy Effects Sink
```

<!-- section_id: "2aef148e-0236-497d-8640-c5809e91569c" -->
### Result
Volume buttons now control hardware speaker volume. Audio enhancement still active.

---

<!-- section_id: "3d3c41f5-8da1-4cf2-8136-50a10d4dd220" -->
## Fix 3: gsd-* Daemon Restart

<!-- section_id: "f6c149aa-0a9a-40cf-8ad7-7538bd34bf20" -->
### Problem
When fixing audio routing, gsd-media-keys and gsd-power crashed again, breaking volume and brightness buttons.

<!-- section_id: "e2887a8e-c6f2-4aaa-b652-3b0c63d104a2" -->
### Fix
Manually restarted daemons:
```bash
DISPLAY=:0 /usr/libexec/gsd-media-keys &
DISPLAY=:0 /usr/libexec/gsd-power &
```

<!-- section_id: "20bfc56c-dc54-48b3-8424-bd36bfa26018" -->
### Long-term Fix
Already configured gsd-keepalive.timer from earlier session (see gsd_keepalive_fix.md).

---

<!-- section_id: "f11266b9-5d5d-4fa0-a35b-33ccef720019" -->
## Summary of Final Configuration

<!-- section_id: "d16e6236-6bc8-421c-8164-98b9afbd2c21" -->
### Audio Chain
```
Applications → EasyEffects Sink → Processing → Hardware Speakers
                    ↑                              ↑
            (apps route here)            (volume controlled here)
```

<!-- section_id: "fdc4093c-a18f-4e06-97ca-b7636f27e023" -->
### Key Settings
| Setting | Value |
|---------|-------|
| Default Sink | Hardware (for volume control) |
| App Routing | EasyEffects (for processing) |
| Active Preset | "Dolby-Like (Framework)" |
| EasyEffects Service | Running via autostart |

<!-- section_id: "79a66edd-258e-4ae6-a1bd-e93bd91d987b" -->
### Files
| File | Purpose |
|------|---------|
| `~/.config/easyeffects/output/Dolby-Like (Framework).json` | Active audio preset |
| `~/.config/autostart/com.github.wwmm.easyeffects.desktop` | Auto-start on login |
| `~/.config/systemd/user/gsd-keepalive.timer` | Restart crashed daemons |

<!-- section_id: "f1bd8725-3eae-4ab9-8404-3d025c90657f" -->
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
