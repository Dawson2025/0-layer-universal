---
resource_id: "9f8d39cd-b1f7-4384-8eb9-357eb3f8dcf9"
resource_type: "document"
resource_name: "configuration"
---
# Trackpad Configuration for Wayland (GNOME)

**Last Updated**: January 11, 2026
**System**: Ubuntu 24.04 GNOME on Wayland
**Hardware**: ELAN06FA:00 04F3:32FD Touchpad (149mm × 93mm)

<!-- section_id: "a9584e9c-e4d0-4723-8607-4915d9507399" -->
## Overview

Wayland provides **fewer customization options** than X11 for trackpad settings. The custom piecewise acceleration curves available on X11 (via xinput) **do not work on Wayland**.

<!-- section_id: "533a0037-31a3-4a31-9dd1-adc1c46fbea7" -->
## Why Wayland Has Limited Trackpad Controls

| Aspect | Reason |
|--------|--------|
| **Security** | Apps can't access raw input (more secure) |
| **Architecture** | Compositor handles input directly |
| **Tool support** | xinput doesn't work; tools haven't caught up |

<!-- section_id: "999aa11c-580e-4584-821e-0c5001d055bb" -->
## Available Settings

<!-- section_id: "8e8e99ed-6c92-4f83-822c-03cd87cd7c58" -->
### Cursor Speed
```bash
# Check current speed
gsettings get org.gnome.desktop.peripherals.touchpad speed

# Set speed (-1.0 to 1.0)
gsettings set org.gnome.desktop.peripherals.touchpad speed 0.15
```

| Value | Feel |
|-------|------|
| -1.0 | Very slow |
| -0.5 | Slow |
| 0.0 | Default |
| 0.15 | **Current setting** |
| 0.25 | Slightly faster |
| 0.5 | Moderate |
| 1.0 | Very fast |

<!-- section_id: "8101765c-a16e-421e-98b5-3aa430749d1a" -->
### Acceleration Profile
```bash
# Check current profile
gsettings get org.gnome.desktop.peripherals.touchpad accel-profile

# Set profile
gsettings set org.gnome.desktop.peripherals.touchpad accel-profile 'adaptive'
```

| Profile | Behavior |
|---------|----------|
| `adaptive` | Slow movements = slow cursor, fast movements = accelerated (recommended) |
| `flat` | Linear, no acceleration |

<!-- section_id: "5e2a565e-bfbe-4b42-baf5-c86adf6b03a0" -->
### Other Touchpad Settings
```bash
# Natural scrolling (reverse direction)
gsettings set org.gnome.desktop.peripherals.touchpad natural-scroll true

# Tap to click
gsettings set org.gnome.desktop.peripherals.touchpad tap-to-click true

# Disable while typing
gsettings set org.gnome.desktop.peripherals.touchpad disable-while-typing true
```

<!-- section_id: "91d5f7cd-3583-48bd-bdcd-b698c9f8e759" -->
## Scroll Speed Workaround

**Problem**: GNOME Wayland has no scroll speed setting.

**Solution**: Use hwdb to set a virtual touchpad size. Larger virtual size = slower scrolling.

<!-- section_id: "ae675d58-ea05-4437-b075-7438b680b365" -->
### Current Configuration

File: `/etc/udev/hwdb.d/99-touchpad-scroll-speed.hwdb`
```
# Slow down touchpad scrolling by increasing virtual size
# Original: 149x93mm, Virtual: 224x140mm (1.5x slower scroll)
evdev:name:ELAN06FA:00 04F3:32FD Touchpad:*
 EVDEV_ABS_00=::22
 EVDEV_ABS_01=::31
 EVDEV_ABS_35=::22
 EVDEV_ABS_36=::31
```

<!-- section_id: "401d09fc-db44-48b8-b9f2-f92a23b30581" -->
### How to Adjust Scroll Speed

**To make scrolling slower** (2x):
```bash
# Calculate: original_resolution * 2
# Resolution 22 → 44, Resolution 31 → 62
sudo tee /etc/udev/hwdb.d/99-touchpad-scroll-speed.hwdb << 'EOF'
evdev:name:ELAN06FA:00 04F3:32FD Touchpad:*
 EVDEV_ABS_00=::44
 EVDEV_ABS_01=::62
 EVDEV_ABS_35=::44
 EVDEV_ABS_36=::62
EOF
sudo systemd-hwdb update && sudo udevadm trigger
# Log out and back in
```

**To make scrolling faster** (1.25x slower than default):
```bash
sudo tee /etc/udev/hwdb.d/99-touchpad-scroll-speed.hwdb << 'EOF'
evdev:name:ELAN06FA:00 04F3:32FD Touchpad:*
 EVDEV_ABS_00=::18
 EVDEV_ABS_01=::25
 EVDEV_ABS_35=::18
 EVDEV_ABS_36=::25
EOF
sudo systemd-hwdb update && sudo udevadm trigger
# Log out and back in
```

**To remove scroll speed adjustment** (back to default):
```bash
sudo rm /etc/udev/hwdb.d/99-touchpad-scroll-speed.hwdb
sudo systemd-hwdb update && sudo udevadm trigger
# Log out and back in
```

<!-- section_id: "ca3e89c1-b1e4-4716-aac8-a8aefad1c1cd" -->
### Known Issues with Scroll Speed Workaround

| Issue | Description | Workaround |
|-------|-------------|------------|
| Click misalignment | Mouse clicks may not align with cursor | Remove hwdb rule |
| Requires relogin | Changes only apply after logout/login | Reboot for reliability |
| Per-device | Must match exact touchpad name | Check with `cat /proc/bus/input/devices` |

<!-- section_id: "ad08a9ac-49cb-4483-b0c1-3f9a3ed289ba" -->
## Current Settings Summary

| Setting | Value | Method |
|---------|-------|--------|
| Cursor Speed | 0.15 | gsettings |
| Accel Profile | adaptive | gsettings |
| Scroll Speed | ~1.5x slower | hwdb virtual size (requires logout) |

<!-- section_id: "4e8adee4-501e-48cd-ade1-2f0a0a0540b0" -->
## Configuration History & Rationale

<!-- section_id: "c34fa8a9-91e9-4ee5-9c39-5ea596329f3c" -->
### Why These Settings?

This configuration was developed through iterative testing on January 11, 2026.

#### Cursor Speed Journey
1. Started at **0.5** - felt okay but wanted to fine-tune
2. Reduced to **0.3** - still slightly fast for precision work
3. Reduced to **0.25** - good balance, but user wanted slightly slower
4. Settled on **0.15** - comfortable for both precision and general use

#### Scroll Speed Solution
GNOME Wayland has **no native scroll speed setting**. The workaround:
1. Discovered hwdb can set "virtual" touchpad dimensions
2. Larger virtual size = system thinks finger moved less = slower scrolling
3. Set virtual size to 1.5x actual (149×93mm → ~224×140mm)
4. This slows scrolling by approximately 1.5x

#### Why Adaptive Acceleration?
- **Adaptive**: Slow movements stay slow (precision), fast movements accelerate
- **Flat**: Linear movement regardless of speed
- Adaptive better matches natural hand movement expectations

<!-- section_id: "539784d2-d0c1-474d-be5a-090793663739" -->
### What We Tried That Didn't Work (on Wayland)

| Approach | Why It Failed |
|----------|---------------|
| xinput commands | Only work on X11, not Wayland |
| Custom acceleration curves | Not supported by Wayland compositor |
| libinput config files | GNOME doesn't read them on Wayland |
| gsettings scroll speed | Setting doesn't exist |

<!-- section_id: "74bb7dbb-34ce-41c9-a65a-5f5ea424bb88" -->
### Key Insight: Wayland Limitations

Wayland prioritizes security over customization. The compositor (Mutter for GNOME) handles all input directly, so:
- Apps can't intercept or modify input events
- Low-level tools like xinput don't have access
- Configuration is limited to what the compositor exposes

This is a **tradeoff**: better security, smoother graphics, but fewer tweaking options.

<!-- section_id: "8db007b0-bfe2-444d-8531-5dbac1c2c826" -->
## Wayland vs X11 Comparison

| Feature | Wayland | X11 |
|---------|---------|-----|
| Custom acceleration curves | No | Yes (xinput) |
| Cursor speed | gsettings only | gsettings + xinput |
| Scroll speed | hwdb hack only | xinput direct control |
| Piecewise zones | Not possible | 7+ zones configurable |
| Security | Better (isolated apps) | Worse (apps can spy) |
| Graphics | Smoother | Can have tearing |
| Overall | Modern, limited tweaks | Legacy, full control |

<!-- section_id: "c1b58cb4-89db-422f-89c2-3f22e07b8e12" -->
## Checking Display Server

```bash
# Check if on Wayland or X11
echo $XDG_SESSION_TYPE
```

<!-- section_id: "d9ed4aea-b77d-4f5b-95c1-5dd69bd4652f" -->
## Switching to X11 (for full trackpad control)

If you need the advanced piecewise acceleration:

1. Log out
2. On login screen, click your username
3. Click the **gear icon** (bottom right)
4. Select **"Ubuntu on Xorg"**
5. Log in
6. Run `~/.config/trackpad-settings.sh` to apply X11 settings

<!-- section_id: "52fbae50-817e-4403-89c3-cd579e8ba2fd" -->
## Troubleshooting

| Issue | Solution |
|-------|----------|
| Cursor too fast | Decrease speed: `gsettings set org.gnome.desktop.peripherals.touchpad speed 0.1` |
| Cursor too slow | Increase speed: `gsettings set org.gnome.desktop.peripherals.touchpad speed 0.4` |
| No acceleration | Set profile: `gsettings set org.gnome.desktop.peripherals.touchpad accel-profile 'adaptive'` |
| Scroll too fast | Create/adjust hwdb rule with larger virtual size |
| Settings not applying | Try logout/login or full reboot |

<!-- section_id: "32c2bf02-a058-43d0-ab47-f3088545945c" -->
## Related Documentation

- [X11 Configuration](../x11/) - For advanced piecewise acceleration
- [Main Trackpad README](../README.md) - Overview

<!-- section_id: "dce8686e-87ed-4a2c-a4bb-8d3c3e5517c6" -->
## Sources

- [Adjust Touchpad Scrolling Speed in Ubuntu 24.04](https://ubuntuhandbook.org/index.php/2023/05/adjust-touchpad-scrolling-ubuntu/)
- [Changing touchpad scroll speed on Gnome Wayland](https://rostislavjadavan.com/posts/gnome-wayland-scroll-speed)
- [GNOME Discourse: Touchpad Scroll Sensitivity](https://discourse.gnome.org/t/add-touchpad-scroll-sensitivity-adjustment-feature/18097)
