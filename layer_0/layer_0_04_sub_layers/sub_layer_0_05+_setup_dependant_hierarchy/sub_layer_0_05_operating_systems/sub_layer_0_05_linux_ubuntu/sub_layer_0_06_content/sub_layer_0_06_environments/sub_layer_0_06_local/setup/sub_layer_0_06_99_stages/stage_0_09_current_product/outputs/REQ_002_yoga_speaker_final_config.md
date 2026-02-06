# Final Configuration: Yoga Pro 9 Speaker I2C Fix

## Request Reference
REQ_002 - Fix Yoga Pro 9 Subwoofer/Speaker Quality on Linux

## Date
2026-01-26

## Status
**COMPLETED** - Subwoofer enabled via I2C, audio significantly improved

---

## Problem Solved

The Lenovo Yoga Pro 9 subwoofer was **disabled by default** on Linux due to a kernel bug. This caused:
- Thin, weak audio lacking bass
- Sound quality significantly worse than Windows
- EasyEffects processing alone couldn't compensate for missing hardware

---

## Current Configuration

### System Files

| File | Purpose |
|------|---------|
| `/usr/local/bin/2pa-byps.sh` | I2C bypass script to enable subwoofer |
| `/etc/systemd/system/yoga-16imh9-speakers.service` | Runs script at boot/resume |
| `/etc/modprobe.d/disable-tas2781-driver.conf` | Blacklists conflicting kernel driver |
| `~/.config/easyeffects/output/Yoga Pro 9i Official.json` | Tuned audio preset |

### Services

| Service | Status | Purpose |
|---------|--------|---------|
| yoga-16imh9-speakers.service | Enabled | Enable subwoofer at boot/resume |
| EasyEffects | Autostart | Audio enhancement |

### Blacklisted Drivers

| Driver | Reason |
|--------|--------|
| snd_hda_scodec_tas2781_i2c | Resets I2C configuration |

---

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

## Recovery Commands

### If Audio Sounds Weak/Thin

```bash
# Re-run the I2C bypass script
sudo /usr/local/bin/2pa-byps.sh

# Check if driver got loaded somehow
lsmod | grep snd_hda_scodec_tas2781_i2c

# If driver is loaded, unload it
sudo rmmod snd_hda_scodec_tas2781_i2c
```

### If Audio Enhancement Stops

```bash
# Restart EasyEffects
pkill easyeffects
easyeffects --gapplication-service &
sleep 3
easyeffects --load-preset "Yoga Pro 9i Official"
```

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

## Known Characteristics

- **Bass vibration**: Normal - the subwoofer is now actually working
- **Louder overall**: Expected - more speakers are active
- **Requires reboot after install**: To permanently blacklist driver

---

## Limitations

- Still not identical to Windows Dolby Atmos (proprietary DSP)
- May need to re-run bypass script after some sleep cycles
- Kernel updates may require re-verification

---

## Related Documentation

| Stage | Document |
|-------|----------|
| Research | `stage_0_01_research/outputs/REQ_002_yoga_speaker_i2c_research.md` |
| Implementation | `stage_0_05_development/outputs/REQ_002_yoga_speaker_implementation.md` |
| Testing | `stage_0_06_testing/outputs/REQ_002_yoga_speaker_testing.md` |
| Fixes | `stage_0_08_fixing/outputs/REQ_002_yoga_speaker_fixes.md` |

---

## Credits

- [maximmaxim345/yoga_pro_9i_gen9_linux](https://github.com/maximmaxim345/yoga_pro_9i_gen9_linux) - Original I2C bypass script and EasyEffects preset
