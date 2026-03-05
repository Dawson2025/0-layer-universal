---
resource_id: "a3daf7eb-0ca8-46ac-8c04-4c95f4d9dd8f"
resource_type: "output"
resource_name: "REQ_001_audio_implementation"
---
# Implementation: Laptop Speaker Audio Enhancement

<!-- section_id: "71241573-732e-401f-aff7-37164e292933" -->
## Request Reference
REQ_001 - Improve Laptop Speaker Audio Quality

<!-- section_id: "af9a90c0-434c-4d0f-8487-b0cb4b79451f" -->
## Date
2026-01-26

<!-- section_id: "c5d991ef-28e8-442f-8f00-eca90c6d4000" -->
## Implementation Attempts

<!-- section_id: "a640e956-1078-426f-a034-ef3923adf78c" -->
### Attempt 1: Basic EasyEffects Preset

**What was done:**
1. Installed EasyEffects: `sudo apt install easyeffects`
2. Installed Calf plugins: `sudo apt install calf-plugins`
3. Created basic `LaptopSpeakers.json` preset with:
   - Bass Enhancer (4dB)
   - Loudness compensation
   - Limiter

**Result:** Minimal improvement. User reported audio still not good.

**Issue identified:** Settings were too conservative.

---

<!-- section_id: "5af7e5a0-4091-4375-b21f-6aab9e2b6ac3" -->
### Attempt 2: Aggressive Custom Preset

**What was done:**
1. Created more aggressive preset with:
   - Bass Enhancer: 8dB boost at 180Hz
   - 10-band EQ with bass +7dB, treble +4dB
   - Stereo Widener: 30% base expansion
   - Loudness Compensation
   - Compressor
   - Limiter

**Result:** Still not satisfactory.

**Issue identified:** Audio was bypassing EasyEffects entirely!

---

<!-- section_id: "41a7f9c4-becb-4dd4-99e6-5296b30b7946" -->
### Attempt 3: Community Presets

**What was done:**
1. Cloned JackHack96/EasyEffects-Presets repository
2. Installed presets:
   - Advanced Auto Gain.json
   - Bass Boosted.json
   - Bass Enhancing + Perfect EQ.json
   - Loudness+Autogain.json
   - Perfect EQ.json

3. Downloaded Framework Community "Dolby-Like" preset:
   - Source: https://community.frame.work/t/guide-yet-another-easyeffects-profile/40509
   - Includes multiband compressor, bass enhancer, exciter, stereo tools

**Presets installed to:** `~/.config/easyeffects/output/`

---

<!-- section_id: "5ce66ad3-241c-45f0-8d8c-7c509e05123f" -->
### Attempt 4: Fix Audio Routing

**Critical discovery:**
```bash
pactl get-default-sink
# Output: alsa_output...sofhdadsp__sink (hardware directly)
# Should be: easyeffects_sink
```

Audio was going directly to hardware, completely bypassing EasyEffects processing.

**Fix applied:**
```bash
pactl set-default-sink easyeffects_sink
```

**Result:** Audio enhancement now working. User confirmed improvement.

---

<!-- section_id: "535d0f70-e16c-4228-a4b5-30274fff9a74" -->
### Attempt 5: Fix Volume Button Conflict

**Problem:** After routing audio through EasyEffects:
- Volume buttons showed EasyEffects popup
- Volume didn't actually change (EasyEffects sink at 100%)

**Root cause:**
- GNOME controls volume of default sink
- Default sink = EasyEffects (virtual, always 100%)
- Hardware speaker volume not being controlled

**Fix applied:**
```bash
# Set hardware as default (for volume control)
pactl set-default-sink alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink
```

**Result:**
- Volume buttons now control hardware speaker volume
- Existing apps still route through EasyEffects (stream routing preserved)
- New apps may need manual routing to EasyEffects

---

<!-- section_id: "3a863d50-319e-4bf7-8f4c-8069942df78d" -->
## Files Created/Modified

<!-- section_id: "ad01e8f8-477e-4456-adc3-12203b3db035" -->
### EasyEffects Presets
- `~/.config/easyeffects/output/LaptopSpeakers.json` - Custom basic preset
- `~/.config/easyeffects/output/Dolby-Like (Framework).json` - Community Dolby-like preset
- `~/.config/easyeffects/output/Advanced Auto Gain.json` - JackHack96 preset
- `~/.config/easyeffects/output/*.json` - Other community presets

<!-- section_id: "24d80f8b-17d2-4125-9852-f4066cd2811c" -->
### Scripts
- `~/.local/bin/volume-control.sh` - Hardware volume control script (created but not used in final solution)

<!-- section_id: "9b3a05cc-b76e-4a24-95eb-dee7795d10a3" -->
### Autostart
- `~/.config/autostart/com.github.wwmm.easyeffects.desktop` - EasyEffects autostart

<!-- section_id: "a9dbf6b9-4e6d-49f7-bd72-dde26eece24f" -->
## Commands Used

```bash
# Install packages
sudo apt install easyeffects calf-plugins

# Clone community presets
git clone https://github.com/JackHack96/EasyEffects-Presets.git
cp EasyEffects-Presets/*.json ~/.config/easyeffects/output/

# Load preset
easyeffects --load-preset "Dolby-Like (Framework)"

# Check audio routing
pactl list sinks short
pactl get-default-sink
wpctl status

# Route audio through EasyEffects
pactl set-default-sink easyeffects_sink

# Fix volume buttons (set hardware as default)
pactl set-default-sink alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink
```
