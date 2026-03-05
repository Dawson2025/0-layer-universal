---
resource_id: "5c267084-47d4-433e-9ed9-63e3872d0b66"
resource_type: "output"
resource_name: "WINDOWS_INSTRUCTIONS_capture_dolby_impulse"
---
# Windows Instructions: Capture Dolby Atmos Impulse Response

<!-- section_id: "378a2b90-f5a9-45bb-90c0-68c1edbee2a0" -->
## Purpose
Capture the Dolby Atmos audio processing as an impulse response file (.irs) that can be used on Linux to replicate the same audio quality.

<!-- section_id: "4ba5db62-4482-431e-ac42-b3b8826f18d2" -->
## Prerequisites on Windows
1. **Audacity** - Download from https://www.audacityteam.org/
2. **VLC Media Player** - Download from https://www.videolan.org/
3. **Impulse WAV file** - Download from link below

<!-- section_id: "e2670b39-f13f-4942-afc5-d320c4b57bb6" -->
## Step-by-Step Instructions

<!-- section_id: "23fc7431-a331-4428-949e-2ab8fbdaf208" -->
### Step 1: Download the Impulse File
Download this impulse WAV file:
```
https://github.com/shuhaowu/linux-thinkpad-speaker-improvements/raw/main/irs/impulse.wav
```

Or create one in Audacity:
1. Open Audacity
2. Generate > Tone: 1 sample at max amplitude
3. Export as WAV (impulse.wav)

<!-- section_id: "602aaf3d-2190-4f61-ba8b-96dd3898ac33" -->
### Step 2: Configure Dolby Atmos
1. Open **Dolby Access** or **Dolby Audio** app
2. Ensure Dolby Atmos is **ENABLED**
3. Set to your preferred profile (Music, Movie, etc.)
4. Make sure it's active for Speakers (not just headphones)

<!-- section_id: "8c516cc7-b13a-4927-8027-eb099db82b9a" -->
### Step 3: Configure Audacity for Recording
1. Open Audacity
2. Go to **Edit > Preferences > Devices**
3. Set **Host** to: `Windows WASAPI`
4. Set **Recording Device** to: `Speakers (loopback)` or similar
   - Look for your speaker device with "(loopback)" in the name
5. Set **Channels** to: `2 (Stereo)`
6. Click OK

<!-- section_id: "f40fccdf-0e6c-4af5-b025-af856d2df17b" -->
### Step 4: Record the Impulse
1. In Audacity, click the **Record** button (red circle)
2. Open VLC and play the `impulse.wav` file
3. You should see the waveform appear in Audacity
4. Stop recording after the impulse plays (about 1-2 seconds)

<!-- section_id: "d6a4911a-c013-4aa1-8160-34bdd77e76cd" -->
### Step 5: Process the Recording
1. In Audacity, select all the audio (Ctrl+A)
2. Trim silence from the beginning if needed
3. **Important**: The impulse should start at the very beginning of the file
4. Normalize: **Effect > Normalize** (set to -1 dB)

<!-- section_id: "2aade271-0ac0-4160-a0b6-df986a8f2288" -->
### Step 6: Export the Impulse Response
1. **File > Export > Export as WAV**
2. Save as: `dolby_yoga_pro_9.wav`
3. Choose: **Signed 32-bit float** (or 24-bit PCM)
4. Save to a location that syncs to Linux (your Syncthing folder)

<!-- section_id: "a0e13f18-31a5-4984-a6af-6fc7bab1e2aa" -->
### Step 7: Rename for Linux
Rename the file to have `.irs` extension:
```
dolby_yoga_pro_9.irs
```

<!-- section_id: "54e00bd0-8f2f-48b5-a624-e033785c26f9" -->
## File Location
Save the final `.irs` file here (syncs to Linux):
```
[Your Syncthing folder]/dolby_yoga_pro_9.irs
```

Or save to:
```
This same folder: setup/sub_layer_0_06_99_stages/stage_0_05_development/outputs/
```

<!-- section_id: "68ffb3d7-ea9b-45fa-b52f-834f0efdd83e" -->
## Verification
The file should be:
- WAV format (despite .irs extension)
- Stereo (2 channels)
- ~1-2 seconds long
- Starting with the impulse at time 0

<!-- section_id: "2aa32cd6-d86b-42a7-885e-c181875c1410" -->
## After Capture
Once you boot back to Linux:
1. Copy the .irs file to `~/.config/easyeffects/irs/`
2. Open EasyEffects
3. Add Convolver effect
4. Load the `dolby_yoga_pro_9.irs` file
5. Add Limiter AFTER convolver (threshold: 0 dB)

<!-- section_id: "90b52e64-d0e9-4d83-83bc-adf8b80f039a" -->
## Troubleshooting

<!-- section_id: "777b351b-e1e2-41f7-8bef-99d0d67ac0ed" -->
### Can't see loopback device
- Make sure Windows WASAPI is selected as host
- Try different audio host options
- Update Audacity to latest version

<!-- section_id: "c253838f-36de-4311-8c98-ee862b065e7d" -->
### Recording is silent
- Check Dolby is actually enabled
- Verify speakers are the active output device
- Try increasing VLC volume

<!-- section_id: "107a1749-1e74-4351-9870-f09cb308f59b" -->
### Audio sounds distorted after capture
- Normalize to -3 dB instead of -1 dB
- Make sure to add Limiter on Linux

<!-- section_id: "015f1503-d5e1-4922-b35c-da24711e6435" -->
## Reference
Based on: https://github.com/shuhaowu/linux-thinkpad-speaker-improvements
