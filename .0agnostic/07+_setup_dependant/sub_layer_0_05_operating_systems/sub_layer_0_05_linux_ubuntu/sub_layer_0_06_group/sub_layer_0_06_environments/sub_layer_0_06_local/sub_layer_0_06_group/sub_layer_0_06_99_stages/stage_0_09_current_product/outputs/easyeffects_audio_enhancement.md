---
resource_id: "59939c33-b5ab-45fd-b577-ccb4679aa095"
resource_type: "output"
resource_name: "easyeffects_audio_enhancement"
---
# EasyEffects Audio Enhancement Setup

<!-- section_id: "a5456e1f-6b71-45ba-bf48-de900337de88" -->
## Problem

Linux laptop speakers sound significantly worse than Windows due to missing proprietary audio processing:
- No Dolby Atmos / Dolby Audio
- No Lenovo-specific speaker tuning profiles
- No hardware DSP effects
- Raw SOF (Sound Open Firmware) driver without enhancements

<!-- section_id: "9aa69e2b-77a8-4ff2-a140-06f29252faf4" -->
## Solution

Installed EasyEffects with custom preset to compensate for missing Dolby processing.

<!-- section_id: "1b6edc59-2334-4a36-a783-7be9bacc6614" -->
### Packages Installed

```bash
sudo apt install -y easyeffects calf-plugins
```

- `easyeffects` - PipeWire audio effects processor
- `calf-plugins` - LV2 plugins for bass enhancer, stereo tools, etc.

<!-- section_id: "f80cb0f2-0d22-4d05-8b68-70931c3058d3" -->
### Preset Created

**~/.config/easyeffects/output/LaptopSpeakers.json**

Effects chain:
1. **Bass Enhancer** - 8dB boost at 180Hz (compensates for weak laptop bass)
2. **10-band Equalizer** - Bass +7dB, treble +4dB, smiley curve
3. **Stereo Widener** - Makes laptop speakers sound wider
4. **Loudness Compensation** - Fuller sound at any volume level
5. **Compressor** - Evens out dynamics for clearer dialogue
6. **Limiter** - Prevents distortion at high volumes

<!-- section_id: "4d979b0a-6cbb-4901-b57c-26ddaf585daa" -->
### Auto-start Enabled

```bash
mkdir -p ~/.config/autostart
cp /usr/share/applications/com.github.wwmm.easyeffects.desktop ~/.config/autostart/
```

<!-- section_id: "6f3618da-4585-4cd6-a11f-4113c7e642df" -->
### Commands

```bash
# Load preset
easyeffects --load-preset LaptopSpeakers

# Run as background service
easyeffects --gapplication-service &
```

<!-- section_id: "7ae69b11-3bb7-4932-9d0d-87bfb3f6d273" -->
## Limitations

This is a workaround, not a full replacement for Dolby:
- Windows has manufacturer-tuned DSP profiles specific to speaker hardware
- Linux lacks access to proprietary speaker calibration data
- For critical audio, use headphones or external speakers

<!-- section_id: "ee5e74aa-ab01-419f-bd03-808c992c80b4" -->
## Customization

Open EasyEffects from app menu to:
- Adjust bass/treble levels
- Add/remove effects
- Create different presets for different use cases

<!-- section_id: "63037081-8482-4982-ad86-5ec98f7b6933" -->
## Files

- Preset: `~/.config/easyeffects/output/LaptopSpeakers.json`
- Autostart: `~/.config/autostart/com.github.wwmm.easyeffects.desktop`
