---
resource_id: "c72b9d88-83f1-445f-9d4b-561affc63423"
resource_type: "document"
resource_name: "ubuntu-trackpad-advanced-config"
---
# Ubuntu Trackpad Advanced Configuration Guide

**Last Updated**: December 2, 2025
**System**: Ubuntu 24.04 GNOME
**Trackpad Driver**: libinput

This document captures the detailed process of configuring trackpad settings for optimal cursor and scroll behavior, including lessons learned from extensive iteration.

<!-- section_id: "35a6b644-4a9f-47b4-9e76-e672a8237553" -->
## Goals

1. **Cursor behavior**: Small/slow movements should be slow and smooth; fast movements should move the cursor much further (acceleration)
2. **Scroll behavior**: Similar adaptive behavior - slow scrolls should be slow, fast scrolls should be fast
3. **No jerkiness**: Smooth transitions at all speeds
4. **Persistent settings**: Configuration must survive reboots

<!-- section_id: "0a04ef8a-d7e5-4d7a-a1c9-b9a4adde98f9" -->
## Hardware Context

- **Trackpad**: ELAN06FA:00 04F3:32FD Touchpad (device ID 10)
- **Desktop Environment**: GNOME (ubuntu:GNOME)
- **Driver**: libinput

<!-- section_id: "99c19e6e-531f-4bb3-86e1-712687b89642" -->
## Key Learnings

<!-- section_id: "894fc664-d549-4570-ae2f-0eb2f35e20a9" -->
### 1. Two Independent Speed Systems

There are **two separate systems** that control trackpad speed:

- **gsettings** (GNOME level): `org.gnome.desktop.peripherals.touchpad speed`
- **xinput** (libinput level): `libinput Accel Speed`

**Critical lesson**: Both must be set to the same value, or behavior becomes unpredictable.

<!-- section_id: "5a7bfa3d-b430-4891-ac63-0162d00068e4" -->
### 2. Cursor Speed vs Scroll Speed

- **Cursor speed**: Controlled by `libinput Accel Speed` and acceleration profiles
- **Scroll speed**: Controlled by `libinput Scrolling Pixel Distance` (higher = slower scrolling)
- These are **completely independent** settings

<!-- section_id: "b01a1a9c-875b-4e62-81f6-5b31c80cfe2e" -->
### 3. Acceleration Profiles

libinput provides three acceleration profiles:

1. **Adaptive** (1, 0, 0): Built-in acceleration curve for cursor only, no scroll acceleration
2. **Flat** (0, 1, 0): No acceleration, linear movement
3. **Custom** (0, 0, 1): Allows custom acceleration curves for **both** cursor AND scroll

**Critical discovery**: Only the **custom profile** supports scroll acceleration.

<!-- section_id: "a5e4a620-94c2-4ed9-8826-3ddd8f12e165" -->
### 4. Custom Acceleration Curves

Custom profiles use two key properties:

- **Points**: Define the acceleration curve (e.g., "0.0 0.1 0.3 0.6 1.0 1.5")
  - First number = multiplier at slowest speed
  - Last number = multiplier at fastest speed
  - Middle numbers = intermediate steps for smooth transitions

- **Step**: Controls the granularity of speed detection (smaller = smoother)
  - 0.01 = standard smoothness
  - 0.005 = smoother
  - 0.002 = very smooth

**Critical lesson**: Even with minimum base speed (-1.0), an aggressive acceleration curve can make small movements too fast. The curve starting points matter more than the base speed for small movements.

<!-- section_id: "cbe7d281-6ab0-4ba0-9c99-253a5bef1e17" -->
## What Didn't Work

<!-- section_id: "a172ce3b-954e-4429-8767-c56e3b2106c2" -->
### Attempt 1: Simple gsettings Speed Increase
```bash
gsettings set org.gnome.desktop.peripherals.touchpad speed 0.5
```
**Problem**: Increased overall speed but no differentiation between slow and fast movements. Scrolling unaffected.

<!-- section_id: "41cd1ed5-a8f1-4a31-a64e-12493d553e1f" -->
### Attempt 2: Adaptive Profile with High Base Speed
```bash
gsettings set org.gnome.desktop.peripherals.touchpad speed 0.7
gsettings set org.gnome.desktop.peripherals.touchpad accel-profile 'adaptive'
```
**Problem**: Adaptive profile works for cursor but doesn't support scroll acceleration. Acceleration was too aggressive.

<!-- section_id: "f19f03d6-4bba-4600-8cea-ce950c5c3aaa" -->
### Attempt 3: Custom Profile with Aggressive Curves
```bash
xinput set-prop 10 "libinput Accel Profile Enabled" 0, 0, 1
xinput set-prop 10 "libinput Accel Custom Motion Points" 0.0 0.5 1.0 2.5
xinput set-prop 10 "libinput Accel Custom Scroll Points" 0.0 0.5 1.0 3.0
```
**Problem**: Far too aggressive - small movements were jerky and too fast despite the intention.

<!-- section_id: "9b1217bf-7150-44dd-bf5e-b23852cf6d23" -->
### Attempt 4: Reducing Acceleration Multipliers
Progressive attempts with multipliers: 1.5x → 1.3x → 1.2x → 1.1x → 1.05x → 1.02x → 1.01x

**Problem**: Even minimal acceleration multipliers combined with positive base speeds made small movements too fast.

<!-- section_id: "411b623a-cd76-4e31-ba95-352fd8ec4f62" -->
### Attempt 5: Negative Base Speeds with Aggressive Curves
```bash
xinput set-prop 10 "libinput Accel Speed" -0.3
xinput set-prop 10 "libinput Accel Custom Motion Points" 0.0 0.5 1.0 1.02
```
**Problem**: Base speed alone isn't enough - the acceleration curve's starting point matters more for small movements.

<!-- section_id: "6710d4c4-b86a-4995-b0d6-5f810e94ca51" -->
### Attempt 6: Minimum Base Speed with Gentler Curves
Progressive curve adjustments with base speed at -1.0:
- 0.0, 0.3, 0.7, 1.0, 1.5 → Still too fast
- 0.0, 0.1, 0.3, 0.6, 1.0, 1.5 → Still too fast
- 0.0, 0.05, 0.15, 0.4, 0.8, 1.3 → Getting closer
- 0.0, 0.01, 0.05, 0.15, 0.3, 0.5 → Better, but still too fast overall

**Key insight**: Even tiny starting values like 0.1 can feel too fast. The difference between 0.1 and 0.05 is perceptible and significant.

<!-- section_id: "ad0bb9f0-9245-4136-b282-a4bdcbc5ed6a" -->
### Attempt 7: Extreme Reduction (1/10th scale)
Reduced all values to 1/10th:
- 0.0, 0.0005, 0.002, 0.008, 0.015, 0.025 → Much better baseline achieved

**Problem**: Still needed even slower small movements while keeping fast movements at the same speed.

<!-- section_id: "8068136e-4e96-4502-9feb-6d930ea3ceff" -->
### Attempt 8: Piecewise Function Approach
Switched from smooth curves to piecewise step functions:
- 3 zones: 0.0001, 0.01, 0.5 → Good concept but too few zones, jumped to fast zones too easily
- 5 zones: 0.0001, 0.001, 0.01, 0.1, 0.5 with step 0.002 → Still reached fast zones too easily

**Problem**: Small step size (0.002) meant zones transitioned across a very narrow velocity range.

<!-- section_id: "41743c53-79e5-4c3b-a851-b3d746523a00" -->
### Attempt 9: Larger Step Size with Piecewise
Increased step size from 0.002 to 0.05 (25x increase):
- Required much faster physical movement to reach higher zones
- Made zone transitions more intentional

**Problem**: With 5 zones, medium movements jumped too quickly from 0.001x to 0.01x - too aggressive.

<!-- section_id: "13bcacbd-922d-454d-aa9f-11e4d4907ba6" -->
### Attempt 10: 7-Zone Piecewise with Smoother Progression (FINAL CURSOR SOLUTION)
Added more intermediate zones with ~3x progression between steps:
- 0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1
- Step size: 0.05 (keeps zones spread across wide velocity range)

**Success**: Slow movements stay slow, medium movements have smoother progression, fast movements are fast. The ~3x multiplier between zones provides natural-feeling acceleration.

<!-- section_id: "a8210de1-06a1-41c2-8a76-80fed09174d9" -->
### Attempt 11: Scroll Configuration Evolution
- Started with simple 2-zone (0.5x to 1.01x) - too simple, slow scrolling didn't move enough
- Tried 7-zone piecewise (0.01x to 1.0x) - better but transitions felt jumpy
- Final: 11-zone piecewise (0.1x to 1.5x) with ~1.5-2x progression

**Success**: 11 zones provide very smooth scroll transitions. Starting at 0.1x (vs 0.01x) makes slow scrolling more effective while maintaining smooth acceleration to 1.5x for fast scrolling.

<!-- section_id: "3ac0fae1-a620-4d3c-8abf-a5f1ab0a13a4" -->
## What Worked: Final Solution

<!-- section_id: "a268b144-396c-49b7-a569-b75317d73e9f" -->
### Summary: Complete Configuration

**Cursor Movement**: 7 zones (0.0001x to 0.1x) - Precision-focused with ~3x progression
**Scrolling**: 11 zones (0.1x to 1.5x) - Smooth transitions with ~1.5-2x progression
**Step Size**: 0.05 for both (spreads zones across wide velocity range)
**Base Speed**: -1.0 (minimum) for both cursor and scroll

<!-- section_id: "70e8558b-bdd4-4b1f-b08e-651fad135074" -->
### Core Configuration

**Base Speed**: Set to minimum (-1.0)
```bash
gsettings set org.gnome.desktop.peripherals.touchpad speed -1.0
xinput set-prop 10 "libinput Accel Speed" -1.0
```

**Acceleration Profile**: Custom (enables both cursor and scroll acceleration)
```bash
xinput set-prop 10 "libinput Accel Profile Enabled" 0, 0, 1
```

**Cursor Acceleration**: 7-zone piecewise function with distinct speed tiers
```bash
xinput set-prop 10 "libinput Accel Custom Motion Points" 0.0 0.0001 0.0001 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.1
xinput set-prop 10 "libinput Accel Custom Motion Step" 0.05
```

**Zone Breakdown:**

| Zone | Trackpad Velocity Range | Cursor Speed Multiplier | Description |
|------|------------------------|------------------------|-------------|
| 1 | 0.00 - 0.10 | 0.0001x | Very slow (precision) |
| 2 | 0.10 - 0.20 | 0.0003x | Extra slow |
| 3 | 0.20 - 0.30 | 0.001x | Slow |
| 4 | 0.30 - 0.40 | 0.003x | Medium-slow |
| 5 | 0.40 - 0.50 | 0.01x | Medium |
| 6 | 0.50 - 0.60 | 0.03x | Medium-fast |
| 7 | 0.60+ | 0.1x | Fast |

**Key Design Decisions:**
- **Piecewise vs smooth curve**: Distinct zones provide predictable behavior at different speeds
- **~3x progression**: Each zone is roughly 3x faster than the previous (0.0001 → 0.0003 → 0.001 → 0.003, etc.)
- **Large step size (0.05)**: Spreads zones across a wide velocity range, preventing accidental fast zone activation
- **Repeated values**: Creates flat "plateaus" (e.g., "0.0001 0.0001") to maintain consistent speed within each zone
- **Starting at 0.0001x**: Extremely slow baseline for precision work
- **Maximum 0.1x**: Even fast movements stay controlled (not 0.5x or 1.0x which proved too aggressive)

**Scroll Acceleration**: 11-zone piecewise function for smooth scrolling
```bash
xinput set-prop 10 "libinput Scrolling Pixel Distance" 40  # Higher = slower baseline
xinput set-prop 10 "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
xinput set-prop 10 "libinput Accel Custom Scroll Step" 0.05
```

**Scroll Zone Breakdown:**

| Zone | Trackpad Velocity Range | Scroll Speed Multiplier | Description |
|------|------------------------|-------------------------|-------------|
| 1 | 0.00 - 0.10 | 0.1x | Very slow |
| 2 | 0.10 - 0.20 | 0.15x | Extra slow |
| 3 | 0.20 - 0.30 | 0.25x | Slow+ |
| 4 | 0.30 - 0.40 | 0.35x | Medium-slow |
| 5 | 0.40 - 0.50 | 0.5x | Medium |
| 6 | 0.50 - 0.60 | 0.65x | Medium+ |
| 7 | 0.60 - 0.70 | 0.8x | Medium-fast |
| 8 | 0.70 - 0.80 | 0.9x | Fast |
| 9 | 0.80 - 0.90 | 1.0x | Faster |
| 10 | 0.90 - 1.00 | 1.2x | Very fast |
| 11 | 1.00+ | 1.5x | Maximum |

**Key Design Decisions:**
- **11 zones**: More zones than cursor (7) for smoother scroll transitions
- **~1.5-2x progression**: Smaller jumps between zones (0.1 → 0.15 → 0.25) for smoother feel
- **Higher starting point (0.1x)**: Slow scrolling moves the page more effectively than cursor precision zones
- **Maximum 1.5x**: Fast scrolling gets boost without being too aggressive
- **Same step size (0.05)**: Consistent zone boundaries with cursor movement

<!-- section_id: "48d64a3e-2189-4368-8bc9-22bad06c3bf3" -->
### Persistence: Autostart Script

Settings applied via xinput don't persist across reboots. Solution: Create autostart script.

**Script**: `~/.config/trackpad-settings.sh`
```bash
#!/bin/bash
# Trackpad settings configuration script

# Wait for X server to be ready
sleep 2

# Find the trackpad device ID
TRACKPAD_ID=$(xinput list | grep -i "touchpad" | grep -oP 'id=\K\d+' | head -n 1)

if [ -n "$TRACKPAD_ID" ]; then
    # Set base speed for cursor movement (slow movements - negative = slower)
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Speed" -1.0

    # Set scrolling pixel distance (higher = slower scrolling)
    xinput set-prop "$TRACKPAD_ID" "libinput Scrolling Pixel Distance" 40

    # Enable custom acceleration profile for both cursor and scroll acceleration
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Profile Enabled" 0, 0, 1

    # Configure scroll acceleration (piecewise: 11 distinct zones for very smooth progression)
    # Zones: 0.1, 0.15, 0.25, 0.35, 0.5, 0.65, 0.8, 0.9, 1.0, 1.2, 1.5
    # Step 0.05 = requires faster movement to reach higher zones
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Custom Scroll Step" 0.05

    # Configure cursor acceleration (piecewise: 7 distinct zones with smoother progression)
    # Zone 1: Very slow = 0.0001, Zone 2: 0.0003, Zone 3: 0.001, Zone 4: 0.003
    # Zone 5: 0.01, Zone 6: 0.03, Zone 7: 0.1
    # Step 0.05 = requires faster movement to reach higher zones
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Custom Motion Points" 0.0 0.0001 0.0001 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.1
    xinput set-prop "$TRACKPAD_ID" "libinput Accel Custom Motion Step" 0.05
fi
```

**Autostart Entry**: `~/.config/autostart/trackpad-settings.desktop`
```ini
[Desktop Entry]
Type=Application
Name=Trackpad Settings
Exec=/home/dawson/.config/trackpad-settings.sh
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Comment=Apply custom trackpad settings on login
```

Make script executable:
```bash
chmod +x ~/.config/trackpad-settings.sh
```

<!-- section_id: "5d45745e-b0a7-471a-b7d0-4fc10be046bd" -->
## Key Insights

1. **Curve shape matters more than base speed**: For controlling small movements, the acceleration curve's starting points (first few values) are more critical than the base speed setting.

2. **Piecewise functions provide better control than smooth curves**: Creating distinct zones with repeated values (e.g., "0.001 0.001") allows predictable, consistent behavior within each speed range.

3. **Step size controls zone boundaries**:
   - Small step (0.002) = zones transition quickly, hard to stay in slow zones
   - Large step (0.05) = zones spread across wide velocity range, more intentional transitions
   - With 7 zones and step 0.05, velocity range spans ~0.7 units

4. **Zone progression matters**:
   - 2x jumps (0.0001 → 0.0002 → 0.0004) feel too gradual
   - 10x jumps (0.001 → 0.01 → 0.1) feel too aggressive
   - ~3x jumps (0.0001 → 0.0003 → 0.001 → 0.003) provide natural-feeling progression

5. **More zones = smoother experience**: 
   - Cursor: Started with 3 zones (too jumpy), 5 zones (better), 7 zones (optimal for smooth progression from precision to speed)
   - Scroll: Started with 2 zones (too simple), 7 zones (better), 11 zones (optimal for very smooth scroll transitions)

6. **Test iteratively**: What sounds good in theory (e.g., "1.1x acceleration is minimal") can feel very different in practice. Test every change.

7. **Separate cursor and scroll**: They have different use cases and may need different acceleration characteristics:
   - Cursor: Needs extreme precision (0.0001x) for small movements, fewer zones (7) with larger jumps (~3x)
   - Scroll: Needs effective movement even when slow (0.1x minimum), more zones (11) with smaller jumps (~1.5-2x) for smoothness

8. **Extreme values work**: Don't be afraid of very small multipliers like 0.0001x - they're necessary for precision control when base speed is at minimum (-1.0).

<!-- section_id: "4f4c4eed-19e8-41a8-a96c-719c557b6c85" -->
## Troubleshooting

<!-- section_id: "820bf6a7-cab1-4c50-bdfc-12a53e68104d" -->
### Small movements still too fast
- Reduce the first zone values in the custom motion curve (e.g., change 0.0001 to 0.00005)
- Ensure base speed is at minimum (-1.0)
- Check that custom profile is enabled, not adaptive
- Verify step size is large enough (0.05 or higher)

<!-- section_id: "1717ed85-b4e4-43a4-a179-cafd434cc686" -->
### Reaching fast zones too easily
- Increase step size (try 0.1 instead of 0.05)
- This spreads zones across a wider velocity range
- Makes it harder to accidentally trigger fast zones with moderate movements

<!-- section_id: "76cea3c6-1303-4317-a087-a679d22f5a14" -->
### Medium movements feel jumpy or too fast
- Add more intermediate zones to smooth the progression
- Reduce the multiplier difference between adjacent zones
- Current ~3x progression (0.001 → 0.003 → 0.01) can be reduced to ~2x if needed

<!-- section_id: "0ddc9b3d-4f5d-42a5-9037-0f2bde52e9c3" -->
### Scrolling too fast
- Increase `libinput Scrolling Pixel Distance` (try 50, 60, etc.)
- Reduce scroll acceleration multipliers (currently 0.1x to 1.5x)
- Reduce the maximum scroll zone value (currently 1.5x, try 1.2x or 1.0x)

<!-- section_id: "20128327-d663-41c9-bea0-a8b3140bfd5b" -->
### Scrolling too slow (especially slow scrolling)
- Increase the starting scroll zone values (currently 0.1x, try 0.15x or 0.2x)
- Reduce `libinput Scrolling Pixel Distance` (currently 40, try 30 or 35)

<!-- section_id: "6403a737-37e0-4447-9ae4-6bffbbc1dc61" -->
### Settings not persisting after reboot
- Verify autostart script exists and is executable
- Check that script is in `~/.config/autostart/` directory
- Test script manually: `~/.config/trackpad-settings.sh`

<!-- section_id: "9a945e30-a5de-4bf8-b6b1-3353a93208a2" -->
### Jerkiness in cursor movement
- Reduce step size (try 0.001)
- Add more intermediate points to the curve
- Ensure no competing settings from other tools

<!-- section_id: "aa4c1f0e-2a1c-48ff-ad4b-378d204ac3fd" -->
## Quick Reference Commands

**Check current settings**:
```bash
# Check speed
gsettings get org.gnome.desktop.peripherals.touchpad speed
xinput list-props 10 | grep "Accel Speed"

# Check profile
xinput list-props 10 | grep "Accel Profile Enabled"

# Check curve
xinput list-props 10 | grep "Custom Motion"

# Check scroll settings
xinput list-props 10 | grep "Scroll"
```

**Apply settings immediately**:
```bash
# Run the autostart script manually
~/.config/trackpad-settings.sh
```

<!-- section_id: "1cbc2501-3a0f-44fa-8f1b-01f931a26f22" -->
## Related Documentation

- [Ubuntu Linux Setup Guide](ubuntu-linux-setup.md) - Basic trackpad configuration
- [xinput man page](https://manpages.ubuntu.com/manpages/noble/man1/xinput.1.html)
- [libinput documentation](https://wayland.freedesktop.org/libinput/doc/latest/)

---

**Note**: These settings were developed through extensive iteration on an ELAN trackpad. Your hardware may respond differently. Use this as a starting point and adjust based on feel.
