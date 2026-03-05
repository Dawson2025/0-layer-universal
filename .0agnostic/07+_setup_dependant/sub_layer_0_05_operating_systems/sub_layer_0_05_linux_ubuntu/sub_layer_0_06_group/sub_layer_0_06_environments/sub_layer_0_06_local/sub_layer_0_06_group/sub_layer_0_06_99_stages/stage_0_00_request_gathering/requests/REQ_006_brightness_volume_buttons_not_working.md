---
resource_id: "de8ac279-c863-49e3-b0eb-28eaeb1d6a45"
resource_type: "document"
resource_name: "REQ_006_brightness_volume_buttons_not_working"
---
# REQ_006: Brightness and Volume Buttons Not Working

**Date Reported**: 2026-01-29
**Status**: Active - Investigating
**Severity**: Medium (system works via CLI, buttons just inoperative)

---

## Problem Summary

Physical brightness and volume buttons on the laptop are not working. Tested:
- Volume up/down buttons: No effect
- Brightness up/down buttons: No effect
- Alternative test via pactl: ✅ Works (`pactl set-sink-volume` works fine)

---

## Investigation Findings

### Step 1: GNOME Settings Check
- ✅ Key bindings ARE configured correctly in gsettings:
  - `volume-up`: `['XF86AudioRaiseVolume']`
  - `volume-down`: `['XF86AudioLowerVolume']`
  - `screen-brightness-up`: `['XF86MonBrightnessUp']`
  - `screen-brightness-down`: `['XF86MonBrightnessDown']`
- ✅ gsd-sound daemon is running
- ❌ gsd-media-keys daemon CAN start but fails to grab key bindings

### Step 2: acpid Installation and Testing
- ✅ `acpid` installed successfully
- ✅ `acpid` service started: `sudo systemctl start acpid`
- ❌ No ACPI events detected when buttons are pressed
- Tested with: `acpi_listen` (no output when buttons pressed)
- Tested with: `/proc/acpi/event` (no events generated)

### Step 3: Input Event Analysis
- ✅ Multiple input devices present (`/dev/input/event0-16`)
- ❌ **Critical finding**: No input device for volume/brightness buttons
- ❌ No hardware detected as generating XF86 key events
- Kernel not reporting button presses at all

### Step 4: gsd-media-keys Error
When attempting to start gsd-media-keys manually, got warnings:
```
Failed to grab accelerator for keybinding settings:volume-up
Failed to grab accelerator for keybinding settings:volume-down
Failed to grab accelerator for keybinding settings:screen-brightness-up
Failed to grab accelerator for keybinding settings:screen-brightness-down
```

This indicates the X11/input system is not receiving key events from the buttons.

---

## Root Cause Analysis

**The buttons are not being detected by the Linux kernel at all.**

Possible causes:
1. **Kernel driver issue**: This specific laptop model's brightness/volume buttons may not be supported by the Linux kernel
2. **BIOS/firmware issue**: The BIOS may not expose these buttons as standard ACPI events
3. **Missing kernel module**: Special laptop-specific module might be needed
4. **Hardware configuration**: The buttons might be on a non-standard bus (EC, SMBus, etc.)

Evidence:
- No ACPI events when buttons pressed
- No input device events when buttons pressed
- acpi_listen shows no events
- `/proc/acpi/event` shows no events
- No XF86 keycodes in X11 keymap

---

## What We Tried

| Approach | Result |
|----------|--------|
| Resetting gsettings media-keys bindings | ✅ Keys configured, but not received |
| Restarting gsd-sound | ✅ Restarted, but still failed to grab keys |
| Installing acpid | ✅ Installed and started, but no events detected |
| Running gsd-media-keys daemon | ❌ Fails to grab accelerators (no events available) |
| Checking /etc/acpi/events | ❌ No configuration files present |
| Using acpi_listen | ❌ No output when buttons pressed |
| Checking /proc/acpi/event | ❌ No events generated |
| Checking /dev/input devices | ❌ No volume/brightness input device exists |

---

## Next Steps / Solutions to Try

### Option 1: Check Laptop-Specific Configuration
```bash
# Check if GNOME on this laptop has special brightness handling
dbus-send --session --print-reply --dest=org.gnome.SettingsDaemon.Power \
  /org/gnome/SettingsDaemon/Power org.gnome.SettingsDaemon.Power.GetPercentage

# Check available backlight drivers
ls /sys/class/backlight/
cat /sys/class/backlight/*/max_brightness
```

### Option 2: Verify Kernel Support
```bash
# Check if kernel sees ACPI button device
grep -r "button" /sys/bus/acpi/drivers/

# Check BIOS version and updates
sudo dmidecode | grep -i "BIOS"
```

### Option 3: Install Laptop-Specific Tools
For Lenovo Yoga laptops specifically:
```bash
sudo apt install tlp  # Lenovo-specific power management
# or
sudo apt install laptop-mode-tools
```

### Option 4: Use Hotkey Daemon (Alternative)
Instead of relying on GNOME's media-keys handling, use a dedicated hotkey daemon:
```bash
sudo apt install xbindkeys
# Then configure custom key bindings
```

### Option 5: Manual Workaround
Create keyboard shortcuts in GNOME that map physical keys to volume/brightness commands:
```bash
# Set custom key binding
gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings "['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/']"
```

---

## Workaround (Immediate)

Until the root cause is found, use these commands:
```bash
# Volume up
pactl set-sink-volume @DEFAULT_SINK@ +5%

# Volume down
pactl set-sink-volume @DEFAULT_SINK@ -5%

# Brightness up
xrandr --output HDMI-1 --brightness 1.2

# Or use backlight directly
echo 200 | sudo tee /sys/class/backlight/intel_backlight/brightness > /dev/null
```

---

## Notes

- System audio and brightness controls work perfectly via CLI/pactl
- The issue is specifically with the physical hardware buttons
- This suggests kernel/firmware integration issue rather than software configuration
- May require BIOS update or specialized kernel module

---

## Status

- Gsettings configuration: ✅ DONE
- acpid installation: ✅ DONE
- Root cause identified: ✅ BUTTONS NOT DETECTED BY KERNEL
- **Requires**: Kernel driver investigation or laptop-specific configuration
