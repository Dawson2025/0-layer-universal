---
resource_id: "b0f70c2a-5338-455a-bb6d-f1cf4196e7e5"
resource_type: "readme
document"
resource_name: "README"
---
# Trackpad Configuration for Ubuntu Linux

**Last Updated**: January 11, 2026
**System**: Ubuntu 24.04 GNOME
**Hardware**: ELAN06FA:00 04F3:32FD Touchpad (Lenovo Yoga Pro 9)

## Overview

This directory contains comprehensive trackpad configuration for both **Wayland** and **X11** display servers. The configuration approach differs significantly between the two.

## Directory Structure

```
trackpad/
├── README.md                    # This file - Overview and quick reference
├── wayland/
│   └── configuration.md         # Wayland-specific settings (limited)
└── x11/
    ├── README.md                # X11 overview
    ├── cursor/
    │   └── configuration.md     # 7-zone cursor piecewise acceleration
    ├── scroll/
    │   └── configuration.md     # 11-zone scroll piecewise acceleration
    └── scripts/
        └── trackpad-settings.sh # Autostart script for X11
```

## Which Display Server Am I Using?

```bash
echo $XDG_SESSION_TYPE
```
- Returns `wayland` → Use Wayland configuration
- Returns `x11` → Use X11 configuration

## Quick Comparison

| Feature | Wayland | X11 |
|---------|---------|-----|
| **Cursor speed** | gsettings (-1.0 to 1.0) | gsettings + custom curves |
| **Scroll speed** | hwdb hack only | xinput direct control |
| **Piecewise zones** | Not possible | 7+ zones configurable |
| **Precision control** | Basic | 0.0001x multiplier available |
| **Security** | Better | Lower |
| **Recommended** | General use | Trackpad enthusiasts |

## Current Configuration

### If on Wayland (Default for Ubuntu 24.04)

| Setting | Value | Command |
|---------|-------|---------|
| Cursor Speed | 0.25 | `gsettings set org.gnome.desktop.peripherals.touchpad speed 0.25` |
| Accel Profile | adaptive | `gsettings set org.gnome.desktop.peripherals.touchpad accel-profile 'adaptive'` |
| Scroll Speed | ~1.5x slower | hwdb rule in `/etc/udev/hwdb.d/99-touchpad-scroll-speed.hwdb` |

### If on X11

| Setting | Cursor | Scroll |
|---------|--------|--------|
| Zones | 7 | 11 |
| Min Speed | 0.0003x | 0.1x |
| Max Speed | 0.3x | 1.5x |
| Step Size | 0.05 | 0.05 |

## Quick Setup

### For Wayland
```bash
# Set cursor speed
gsettings set org.gnome.desktop.peripherals.touchpad speed 0.25
gsettings set org.gnome.desktop.peripherals.touchpad accel-profile 'adaptive'

# Scroll speed requires hwdb rule - see wayland/configuration.md
```

### For X11
```bash
# Copy and run the settings script
cp x11/scripts/trackpad-settings.sh ~/.config/
chmod +x ~/.config/trackpad-settings.sh
~/.config/trackpad-settings.sh
```

## Switching Between Display Servers

### To Switch to X11 (for advanced trackpad control)
1. Log out
2. On login screen, click your username
3. Click the **gear icon** (bottom right)
4. Select **"Ubuntu on Xorg"**
5. Log in

### To Switch to Wayland (default, more secure)
1. Log out
2. On login screen, click your username
3. Click the **gear icon** (bottom right)
4. Select **"Ubuntu"** (without Xorg)
5. Log in

## Design Philosophy

### Piecewise vs Smooth Acceleration
- **Piecewise (X11)**: Distinct zones with consistent behavior - predictable, tunable
- **Smooth (default)**: Gradual changes - can feel unpredictable

### Why Different Cursor vs Scroll Settings?
- **Cursor**: Needs extreme precision (0.0001x) for pixel-perfect work
- **Scroll**: Needs effective movement even when slow (0.1x minimum)

### Zone Progression
- **Cursor (~3x)**: Distinct precision tiers
- **Scroll (~1.5-2x)**: Smoother feel between zones

## Troubleshooting

| Issue | Wayland Solution | X11 Solution |
|-------|-----------------|--------------|
| Cursor too fast | Decrease gsettings speed | Reduce curve multipliers |
| Cursor too slow | Increase gsettings speed | Increase curve multipliers |
| Scroll too fast | Increase hwdb virtual size | Increase Scrolling Pixel Distance |
| Scroll too slow | Decrease hwdb virtual size | Decrease Scrolling Pixel Distance |
| Settings not applying | Logout/login or reboot | Run trackpad-settings.sh |

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Dec 31, 2025 | Initial X11 config with 7-zone cursor + 11-zone scroll |
| 2.0 | Jan 11, 2026 | Added Wayland support, reorganized into x11/wayland folders |

## Related Documentation

- [Wayland Configuration](wayland/configuration.md) - For Wayland users
- [X11 Configuration](x11/README.md) - For X11 users with full control
- [Setup Hub Guide](https://github.com/Dawson2025/setup-hub/blob/main/docs/ubuntu-trackpad-advanced-config.md) - Full iteration history
