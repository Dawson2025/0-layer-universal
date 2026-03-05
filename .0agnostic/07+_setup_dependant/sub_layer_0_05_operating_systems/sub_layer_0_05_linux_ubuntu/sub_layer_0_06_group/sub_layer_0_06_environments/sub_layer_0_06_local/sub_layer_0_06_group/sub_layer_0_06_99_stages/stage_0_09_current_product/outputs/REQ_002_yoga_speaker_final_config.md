---
resource_id: "c83f6aad-ba31-4586-9129-9f6c88340e38"
resource_type: "output"
resource_name: "REQ_002_yoga_speaker_final_config"
---
# Final Configuration: Yoga Pro 9 Speaker I2C Fix

<!-- section_id: "352f4239-d062-4051-999c-b8550aa805df" -->
## Request Reference
REQ_002 - Fix Yoga Pro 9 Subwoofer/Speaker Quality on Linux

<!-- section_id: "f63fa09e-b63d-4fe9-9947-3fd42c782c86" -->
## Date
2026-01-26

<!-- section_id: "7d0d7627-4363-4496-93af-83c7a1859fd1" -->
## Status
**COMPLETED** - Subwoofer enabled via I2C, audio significantly improved

---

<!-- section_id: "a3d688be-e637-4071-8dda-075447431d96" -->
## Problem Solved

The Lenovo Yoga Pro 9 subwoofer was **disabled by default** on Linux due to a kernel bug. This caused:
- Thin, weak audio lacking bass
- Sound quality significantly worse than Windows
- EasyEffects processing alone couldn't compensate for missing hardware

---

<!-- section_id: "84655774-232a-4aa4-aa6f-6e5bd206bedb" -->
## Current Configuration

<!-- section_id: "8ca449c1-71be-4e3f-bda2-abc6d53ac280" -->
### System Files

| File | Purpose |
|------|---------|
| `/usr/local/bin/2pa-byps.sh` | I2C bypass script to enable subwoofer |
| `/etc/systemd/system/yoga-16imh9-speakers.service` | Runs script at boot/resume |
| `/etc/modprobe.d/disable-tas2781-driver.conf` | Blacklists conflicting kernel driver |
| `~/.config/easyeffects/output/Yoga Pro 9i Official.json` | Tuned audio preset |

<!-- section_id: "4df812ae-49dc-4e4f-982d-d4c6b4d37c91" -->
### Services

| Service | Status | Purpose |
|---------|--------|---------|
| yoga-16imh9-speakers.service | Enabled | Enable subwoofer at boot/resume |
| EasyEffects | Autostart | Audio enhancement |

<!-- section_id: "d9ed94f0-d211-4dfc-a638-0c537cc17318" -->
### Blacklisted Drivers

| Driver | Reason |
|--------|--------|
| snd_hda_scodec_tas2781_i2c | Resets I2C configuration |

---

<!-- section_id: "793fe857-f5db-400d-8197-257dd063e952" -->
## How It Works

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         AUDIO CHAIN                                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌──────────┐     ┌─────────────┐     ┌──────────────┐     ┌─────────┐ │
│  │   Apps   │ ──▶ │ EasyEffects │ ──▶ │ PipeWire/    │ ──▶ │ TAS2781 │ │
│  │ (Chrome, │     │ (Yoga Pro   │     │ ALSA         │     │ Amp     │ │
│  │  etc.)   │     │  9i preset) │     │              │     │         │ │
│  └──────────┘     └─────────────┘     └──────────────┘     └────┬────┘ │
│                                                                  │      │
│                                                                  ▼      │
│                                              ┌───────────────────────┐  │
│                                              │  I2C Bypass Script    │  │
│                                              │  (enables subwoofer)  │  │
│                                              └───────────┬───────────┘  │
│                                                          │              │
│                                                          ▼              │
│                                              ┌───────────────────────┐  │
│                                              │  Speakers + Subwoofer │  │
│                                              │  (hardware enabled)   │  │
│                                              └───────────────────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

<!-- section_id: "8fa6e66f-ac2a-4b8b-9922-243c6907170d" -->
## Recovery Commands

<!-- section_id: "826a11ee-4195-4cfa-8207-9df81414c0ed" -->
### If Audio Sounds Weak/Thin

```bash
# Re-run the I2C bypass script
sudo /usr/local/bin/2pa-byps.sh

# Check if driver got loaded somehow
lsmod | grep snd_hda_scodec_tas2781_i2c

# If driver is loaded, unload it
sudo rmmod snd_hda_scodec_tas2781_i2c
```

<!-- section_id: "03ed3f64-b90e-42da-b2ba-e66cb0ddf1bc" -->
### If Audio Enhancement Stops

```bash
# Restart EasyEffects
pkill easyeffects
easyeffects --gapplication-service &
sleep 3
easyeffects --load-preset "Yoga Pro 9i Official"
```

<!-- section_id: "234f5089-ce9a-419b-ba24-2e2c0157f178" -->
### After Kernel Update

Kernel updates may re-enable the blacklisted driver. If audio becomes weak after an update:

```bash
# Verify blacklist still exists
cat /etc/modprobe.d/disable-tas2781-driver.conf

# If missing, recreate it
sudo tee /etc/modprobe.d/disable-tas2781-driver.conf << 'EOF'
blacklist snd_hda_scodec_tas2781_i2c
EOF

# Reboot or unload driver manually
sudo rmmod snd_hda_scodec_tas2781_i2c
sudo /usr/local/bin/2pa-byps.sh
```

---

<!-- section_id: "2b2625e2-574a-4cbb-b376-bd49a89abfa2" -->
## Known Characteristics

- **Bass vibration**: Normal - the subwoofer is now actually working
- **Louder overall**: Expected - more speakers are active
- **Requires reboot after install**: To permanently blacklist driver

---

<!-- section_id: "699bc19b-a669-4d06-b714-ccc0ee9b757b" -->
## Limitations

- Still not identical to Windows Dolby Atmos (proprietary DSP)
- May need to re-run bypass script after some sleep cycles
- Kernel updates may require re-verification

---

<!-- section_id: "2ac8d03e-2737-49c0-af41-5737e27f7cef" -->
## Related Documentation

| Stage | Document |
|-------|----------|
| Research | `stage_0_01_research/outputs/REQ_002_yoga_speaker_i2c_research.md` |
| Implementation | `stage_0_05_development/outputs/REQ_002_yoga_speaker_implementation.md` |
| Testing | `stage_0_06_testing/outputs/REQ_002_yoga_speaker_testing.md` |
| Fixes | `stage_0_08_fixing/outputs/REQ_002_yoga_speaker_fixes.md` |

---

<!-- section_id: "75a13d95-2995-4a1e-82b3-e40fb953d795" -->
## Credits

- [maximmaxim345/yoga_pro_9i_gen9_linux](https://github.com/maximmaxim345/yoga_pro_9i_gen9_linux) - Original I2C bypass script and EasyEffects preset
