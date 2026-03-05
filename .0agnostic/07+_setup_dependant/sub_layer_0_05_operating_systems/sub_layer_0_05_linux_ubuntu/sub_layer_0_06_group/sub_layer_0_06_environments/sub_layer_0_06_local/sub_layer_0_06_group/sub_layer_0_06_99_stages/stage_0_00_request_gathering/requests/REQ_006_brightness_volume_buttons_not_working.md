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

<!-- section_id: "0dec2b8a-9b49-4220-a7ba-4eaa27a67eb2" -->
## Problem Summary

Physical brightness and volume buttons on the laptop are not working. Tested:
- Volume up/down buttons: No effect
- Brightness up/down buttons: No effect
- Alternative test via pactl: ✅ Works (`pactl set-sink-volume` works fine)

---

<!-- section_id: "3dc37bb0-b281-42f3-89da-6290be581cfb" -->
## Investigation Findings

<!-- section_id: "3ece9d31-acf6-473a-9f00-7dbd449998bb" -->
### Step 1: GNOME Settings Check
- ✅ Key bindings ARE configured correctly in gsettings:
  - `volume-up`: `['XF86AudioRaiseVolume']`
  - `volume-down`: `['XF86AudioLowerVolume']`
  - `screen-brightness-up`: `['XF86MonBrightnessUp']`
  - `screen-brightness-down`: `['XF86MonBrightnessDown']`
- ✅ gsd-sound daemon is running
- ❌ gsd-media-keys daemon CAN start but fails to grab key bindings

<!-- section_id: "9973149f-b905-4d9b-bbaf-1a744d63cb8f" -->
### Step 2: acpid Installation and Testing
- ✅ `acpid` installed successfully
- ✅ `acpid` service started: `sudo systemctl start acpid`
- ❌ No ACPI events detected when buttons are pressed
- Tested with: `acpi_listen` (no output when buttons pressed)
- Tested with: `/proc/acpi/event` (no events generated)

<!-- section_id: "27f3d845-16ad-47ee-9c9b-d5efd908faa0" -->
### Step 3: Input Event Analysis
- ✅ Multiple input devices present (`/dev/input/event0-16`)
- ❌ **Critical finding**: No input device for volume/brightness buttons
- ❌ No hardware detected as generating XF86 key events
- Kernel not reporting button presses at all

<!-- section_id: "5274af81-7192-40bb-b37b-b4fbe499966c" -->
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

<!-- section_id: "24dec418-128b-4de2-a851-99b990c865ea" -->
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

<!-- section_id: "d8cb6760-306e-4fea-a395-82e0b647cdd9" -->
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

<!-- section_id: "a5f96347-7f5c-4104-ad1c-002c2bc899f2" -->
## Next Steps / Solutions to Try

<!-- section_id: "d7840422-412c-40d5-adc6-2c7aac7ca9cd" -->
### Option 1: Check Laptop-Specific Configuration
```bash
# Check if GNOME on this laptop has special brightness handling
dbus-send --session --print-reply --dest=org.gnome.SettingsDaemon.Power \
  /org/gnome/SettingsDaemon/Power org.gnome.SettingsDaemon.Power.GetPercentage

# Check available backlight drivers
ls /sys/class/backlight/
cat /sys/class/backlight/*/max_brightness
```

<!-- section_id: "7cfdaea2-77d9-4909-8409-6d2d93a9555c" -->
### Option 2: Verify Kernel Support
```bash
# Check if kernel sees ACPI button device
grep -r "button" /sys/bus/acpi/drivers/

# Check BIOS version and updates
sudo dmidecode | grep -i "BIOS"
```

<!-- section_id: "04cda6a8-7dfb-442d-a8a7-8aab8087a125" -->
### Option 3: Install Laptop-Specific Tools
For Lenovo Yoga laptops specifically:
```bash
sudo apt install tlp  # Lenovo-specific power management
# or
sudo apt install laptop-mode-tools
```

<!-- section_id: "3b3cb745-5883-4100-9690-19dd62d7dd7e" -->
### Option 4: Use Hotkey Daemon (Alternative)
Instead of relying on GNOME's media-keys handling, use a dedicated hotkey daemon:
```bash
sudo apt install xbindkeys
# Then configure custom key bindings
```

<!-- section_id: "2fa696fc-ec5c-47d4-bbdb-a43613bb77e4" -->
### Option 5: Manual Workaround
Create keyboard shortcuts in GNOME that map physical keys to volume/brightness commands:
```bash
# Set custom key binding
gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings "['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/']"
```

---

<!-- section_id: "b5de6b3f-d48e-429a-b485-d2d5b98d5789" -->
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

<!-- section_id: "cf5cc5e7-b501-44b4-94a8-56ac3bf9fd9a" -->
## Notes

- System audio and brightness controls work perfectly via CLI/pactl
- The issue is specifically with the physical hardware buttons
- This suggests kernel/firmware integration issue rather than software configuration
- May require BIOS update or specialized kernel module

---

<!-- section_id: "9856c763-ce30-48e8-8f39-bb131b64d874" -->
## Status

- Gsettings configuration: ✅ DONE
- acpid installation: ✅ DONE
- Root cause identified: ✅ BUTTONS NOT DETECTED BY KERNEL
- **Requires**: Kernel driver investigation or laptop-specific configuration
