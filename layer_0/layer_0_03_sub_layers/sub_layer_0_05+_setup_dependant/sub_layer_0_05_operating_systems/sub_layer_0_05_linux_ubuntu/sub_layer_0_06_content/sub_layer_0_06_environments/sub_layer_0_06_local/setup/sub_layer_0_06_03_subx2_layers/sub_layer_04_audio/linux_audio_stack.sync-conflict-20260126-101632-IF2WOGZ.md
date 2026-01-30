# Linux Audio Stack

## Overview

Linux audio on modern systems uses PipeWire as the audio server, replacing PulseAudio.

```
┌─────────────────────────────────────────────┐
│              Applications                    │
│         (YouTube, Spotify, etc.)            │
├─────────────────────────────────────────────┤
│              PipeWire                        │
│    (Audio server, session management)        │
├─────────────────────────────────────────────┤
│          ALSA / SOF Driver                   │
│     (Hardware abstraction layer)             │
├─────────────────────────────────────────────┤
│           Audio Hardware                     │
│    (Speakers, microphones, DACs)             │
└─────────────────────────────────────────────┘
```

## Key Components

### PipeWire
- Modern audio/video server
- Handles audio routing between apps and hardware
- Supports effects via filter chains
- Config: `~/.config/pipewire/`

### SOF (Sound Open Firmware)
- Open-source DSP firmware for Intel audio
- Used on modern Intel laptops (Meteor Lake, etc.)
- Driver: `sof-hda-dsp`
- Firmware: `/lib/firmware/intel/sof/`

### ALSA
- Low-level audio interface
- Kernel-level sound driver
- Config: `/etc/asound.conf`, `~/.asoundrc`

## Why Linux Audio Sounds Worse Than Windows

### Missing Proprietary Processing

Windows laptops include:
1. **Dolby Atmos/Audio** - Spatial audio, bass enhancement
2. **Manufacturer Tuning** - Custom EQ for specific speakers
3. **Smart Amplifier** - Prevents speaker damage at high volumes
4. **Advanced DSP** - Noise cancellation, echo removal

Linux has:
1. **Basic SOF driver** - Functional but untuned
2. **No Dolby** - Proprietary, not licensed for Linux
3. **No speaker profiles** - Generic audio only

### The Reality

Laptop speakers are physically limited. Windows makes them sound better through extensive software processing. Linux provides the raw, unprocessed audio.

## Solutions

### EasyEffects
- GUI application for audio effects
- Adds EQ, bass boost, compression, limiting
- Can approximate (but not replicate) Dolby processing
- Install: `sudo apt install easyeffects calf-plugins`

### External Audio
- Headphones bypass all speaker issues
- External speakers/DACs sound identical on Linux and Windows

## Diagnostic Commands

```bash
# Check audio devices
cat /proc/asound/cards

# Check PipeWire status
pactl info

# List audio sinks
pactl list sinks short

# Check SOF firmware
ls /lib/firmware/intel/sof/
```
