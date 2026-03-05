---
resource_id: "f0880425-8771-487c-a5fe-b3493961f510"
resource_type: "knowledge"
resource_name: "linux_audio_stack"
---
# Linux Audio Stack

<!-- section_id: "e1c53cea-7fde-4388-afb7-713cf56fc3bf" -->
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

<!-- section_id: "72c68010-5d7c-43ef-a557-f798efb04fbd" -->
## Key Components

<!-- section_id: "f34e1393-bb8c-4399-b32c-9fde081759b4" -->
### PipeWire
- Modern audio/video server
- Handles audio routing between apps and hardware
- Supports effects via filter chains
- Config: `~/.config/pipewire/`

<!-- section_id: "1637562b-79f2-4244-9a62-796b938af288" -->
### SOF (Sound Open Firmware)
- Open-source DSP firmware for Intel audio
- Used on modern Intel laptops (Meteor Lake, etc.)
- Driver: `sof-hda-dsp`
- Firmware: `/lib/firmware/intel/sof/`

<!-- section_id: "3442f036-98cb-4ee8-8f0e-4df37a767003" -->
### ALSA
- Low-level audio interface
- Kernel-level sound driver
- Config: `/etc/asound.conf`, `~/.asoundrc`

<!-- section_id: "d6eb0bd7-50a3-4e26-8330-742f4b9efb6e" -->
## Why Linux Audio Sounds Worse Than Windows

<!-- section_id: "ebf0bf4f-7773-4540-8b2d-8078281bfa8c" -->
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

<!-- section_id: "57a518e0-025c-40c7-afbc-04f72a26dbb1" -->
### The Reality

Laptop speakers are physically limited. Windows makes them sound better through extensive software processing. Linux provides the raw, unprocessed audio.

<!-- section_id: "910c7726-c7fd-47b5-9fb9-3e25d98a5d9d" -->
## Solutions

<!-- section_id: "9de3fad7-011d-429e-8404-3f0a27a3f07c" -->
### EasyEffects
- GUI application for audio effects
- Adds EQ, bass boost, compression, limiting
- Can approximate (but not replicate) Dolby processing
- Install: `sudo apt install easyeffects calf-plugins`

<!-- section_id: "36fa02e9-0b54-4d01-897d-eaa2977fda27" -->
### External Audio
- Headphones bypass all speaker issues
- External speakers/DACs sound identical on Linux and Windows

<!-- section_id: "a67ce780-3a5c-4c86-8822-3b6ff20e04cd" -->
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
