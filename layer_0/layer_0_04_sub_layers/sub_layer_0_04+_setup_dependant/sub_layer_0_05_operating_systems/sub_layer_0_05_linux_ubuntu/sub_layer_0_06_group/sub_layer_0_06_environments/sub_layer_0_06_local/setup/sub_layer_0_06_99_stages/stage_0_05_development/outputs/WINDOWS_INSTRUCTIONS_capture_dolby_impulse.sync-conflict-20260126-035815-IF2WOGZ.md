# Windows Instructions: Capture Dolby Atmos Impulse Response

## Purpose
Capture the Dolby Atmos audio processing as an impulse response file (.irs) that can be used on Linux to replicate the same audio quality.

## Prerequisites on Windows
1. **Audacity** - Download from https://www.audacityteam.org/
2. **VLC Media Player** - Download from https://www.videolan.org/
3. **Impulse WAV file** - Download from link below

## Step-by-Step Instructions

### Step 1: Download the Impulse File
Download this impulse WAV file:
```
https://github.com/shuhaowu/linux-thinkpad-speaker-improvements/raw/main/irs/impulse.wav
```

Or create one in Audacity:
1. Open Audacity
2. Generate > Tone: 1 sample at max amplitude
3. Export as WAV (impulse.wav)

### Step 2: Configure Dolby Atmos
1. Open **Dolby Access** or **Dolby Audio** app
2. Ensure Dolby Atmos is **ENABLED**
3. Set to your preferred profile (Music, Movie, etc.)
4. Make sure it's active for Speakers (not just headphones)

### Step 3: Configure Audacity for Recording
1. Open Audacity
2. Go to **Edit > Preferences > Devices**
3. Set **Host** to: `Windows WASAPI`
4. Set **Recording Device** to: `Speakers (loopback)` or similar
   - Look for your speaker device with "(loopback)" in the name
5. Set **Channels** to: `2 (Stereo)`
6. Click OK

### Step 4: Record the Impulse
1. In Audacity, click the **Record** button (red circle)
2. Open VLC and play the `impulse.wav` file
3. You should see the waveform appear in Audacity
4. Stop recording after the impulse plays (about 1-2 seconds)

### Step 5: Process the Recording
1. In Audacity, select all the audio (Ctrl+A)
2. Trim silence from the beginning if needed
3. **Important**: The impulse should start at the very beginning of the file
4. Normalize: **Effect > Normalize** (set to -1 dB)

### Step 6: Export the Impulse Response
1. **File > Export > Export as WAV**
2. Save as: `dolby_yoga_pro_9.wav`
3. Choose: **Signed 32-bit float** (or 24-bit PCM)
4. Save to a location that syncs to Linux (your Syncthing folder)

### Step 7: Rename for Linux
Rename the file to have `.irs` extension:
```
dolby_yoga_pro_9.irs
```

## File Location
Save the final `.irs` file here (syncs to Linux):
```
[Your Syncthing folder]/dolby_yoga_pro_9.irs
```

Or save to:
```
This same folder: setup/sub_layer_0_06_99_stages/stage_0_05_development/outputs/
```

## Verification
The file should be:
- WAV format (despite .irs extension)
- Stereo (2 channels)
- ~1-2 seconds long
- Starting with the impulse at time 0

## After Capture
Once you boot back to Linux:
1. Copy the .irs file to `~/.config/easyeffects/irs/`
2. Open EasyEffects
3. Add Convolver effect
4. Load the `dolby_yoga_pro_9.irs` file
5. Add Limiter AFTER convolver (threshold: 0 dB)

## Troubleshooting

### Can't see loopback device
- Make sure Windows WASAPI is selected as host
- Try different audio host options
- Update Audacity to latest version

### Recording is silent
- Check Dolby is actually enabled
- Verify speakers are the active output device
- Try increasing VLC volume

### Audio sounds distorted after capture
- Normalize to -3 dB instead of -1 dB
- Make sure to add Limiter on Linux

## Reference
Based on: https://github.com/shuhaowu/linux-thinkpad-speaker-improvements
