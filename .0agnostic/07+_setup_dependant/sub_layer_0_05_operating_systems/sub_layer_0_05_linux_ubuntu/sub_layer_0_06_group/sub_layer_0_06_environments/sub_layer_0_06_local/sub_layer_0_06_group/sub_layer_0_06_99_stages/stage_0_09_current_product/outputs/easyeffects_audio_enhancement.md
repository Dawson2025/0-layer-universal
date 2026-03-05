---
resource_id: "59939c33-b5ab-45fd-b577-ccb4679aa095"
resource_type: "output"
resource_name: "easyeffects_audio_enhancement"
---
# EasyEffects Audio Enhancement Setup

## Problem

Linux laptop speakers sound significantly worse than Windows due to missing proprietary audio processing:
- No Dolby Atmos / Dolby Audio
- No Lenovo-specific speaker tuning profiles
- No hardware DSP effects
- Raw SOF (Sound Open Firmware) driver without enhancements

## Solution

Installed EasyEffects with custom preset to compensate for missing Dolby processing.

### Packages Installed

```bash
sudo apt install -y easyeffects calf-plugins
```

- `easyeffects` - PipeWire audio effects processor
- `calf-plugins` - LV2 plugins for bass enhancer, stereo tools, etc.

### Preset Created

**~/.config/easyeffects/output/LaptopSpeakers.json**

Effects chain:
1. **Bass Enhancer** - 8dB boost at 180Hz (compensates for weak laptop bass)
2. **10-band Equalizer** - Bass +7dB, treble +4dB, smiley curve
3. **Stereo Widener** - Makes laptop speakers sound wider
4. **Loudness Compensation** - Fuller sound at any volume level
5. **Compressor** - Evens out dynamics for clearer dialogue
6. **Limiter** - Prevents distortion at high volumes

### Auto-start Enabled

```bash
mkdir -p ~/.config/autostart
cp /usr/share/applications/com.github.wwmm.easyeffects.desktop ~/.config/autostart/
```

### Commands

```bash
# Load preset
easyeffects --load-preset LaptopSpeakers

# Run as background service
easyeffects --gapplication-service &
```

## Limitations

This is a workaround, not a full replacement for Dolby:
- Windows has manufacturer-tuned DSP profiles specific to speaker hardware
- Linux lacks access to proprietary speaker calibration data
- For critical audio, use headphones or external speakers

## Customization

Open EasyEffects from app menu to:
- Adjust bass/treble levels
- Add/remove effects
- Create different presets for different use cases

## Files

- Preset: `~/.config/easyeffects/output/LaptopSpeakers.json`
- Autostart: `~/.config/autostart/com.github.wwmm.easyeffects.desktop`
