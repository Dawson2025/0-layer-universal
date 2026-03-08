---
resource_id: "b0f70c2a-5338-455a-bb6d-f1cf4196e7e5"
resource_type: "readme_document"
resource_name: "README"
---
# Trackpad Configuration for Ubuntu Linux

**Last Updated**: January 11, 2026
**System**: Ubuntu 24.04 GNOME
**Hardware**: ELAN06FA:00 04F3:32FD Touchpad (Lenovo Yoga Pro 9)

<!-- section_id: "9e9c1a2d-6a76-41ff-bdef-fbcda963822b" -->
## Overview

This directory contains comprehensive trackpad configuration for both **Wayland** and **X11** display servers. The configuration approach differs significantly between the two.

<!-- section_id: "c9b5f876-a525-41d3-8b84-a891f40bdb67" -->
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

<!-- section_id: "ecfff3fe-a3a7-4e24-be56-f13bf20cba21" -->
## Which Display Server Am I Using?

```bash
echo $XDG_SESSION_TYPE
```
- Returns `wayland` → Use Wayland configuration
- Returns `x11` → Use X11 configuration

<!-- section_id: "8138ebc1-d19b-417b-8b91-2290dfcf5adf" -->
## Quick Comparison

| Feature | Wayland | X11 |
|---------|---------|-----|
| **Cursor speed** | gsettings (-1.0 to 1.0) | gsettings + custom curves |
| **Scroll speed** | hwdb hack only | xinput direct control |
| **Piecewise zones** | Not possible | 7+ zones configurable |
| **Precision control** | Basic | 0.0001x multiplier available |
| **Security** | Better | Lower |
| **Recommended** | General use | Trackpad enthusiasts |

<!-- section_id: "7fb3d3bc-dc91-401e-bf94-f5ef110f9af2" -->
## Current Configuration

<!-- section_id: "f55cd34a-6e8d-4e11-a24c-1ab9b7ad6a5b" -->
### If on Wayland (Default for Ubuntu 24.04)

| Setting | Value | Command |
|---------|-------|---------|
| Cursor Speed | 0.25 | `gsettings set org.gnome.desktop.peripherals.touchpad speed 0.25` |
| Accel Profile | adaptive | `gsettings set org.gnome.desktop.peripherals.touchpad accel-profile 'adaptive'` |
| Scroll Speed | ~1.5x slower | hwdb rule in `/etc/udev/hwdb.d/99-touchpad-scroll-speed.hwdb` |

<!-- section_id: "f819e5f8-ed86-4715-bdc5-79fb292dceb0" -->
### If on X11

| Setting | Cursor | Scroll |
|---------|--------|--------|
| Zones | 7 | 11 |
| Min Speed | 0.0003x | 0.1x |
| Max Speed | 0.3x | 1.5x |
| Step Size | 0.05 | 0.05 |

<!-- section_id: "d29fcbc7-d5e5-4b83-b547-c972842c8623" -->
## Quick Setup

<!-- section_id: "9b25a56c-431a-4e2a-bfca-796a5c420530" -->
### For Wayland
```bash
# Set cursor speed
gsettings set org.gnome.desktop.peripherals.touchpad speed 0.25
gsettings set org.gnome.desktop.peripherals.touchpad accel-profile 'adaptive'

# Scroll speed requires hwdb rule - see wayland/configuration.md
```

<!-- section_id: "4ac5c384-26e5-4ee4-b654-ab02a9a13721" -->
### For X11
```bash
# Copy and run the settings script
cp x11/scripts/trackpad-settings.sh ~/.config/
chmod +x ~/.config/trackpad-settings.sh
~/.config/trackpad-settings.sh
```

<!-- section_id: "f31a8cf0-3a21-499e-b459-b4185a566cdd" -->
## Switching Between Display Servers

<!-- section_id: "caa1ffbe-44e6-4b0a-8683-7ded64ddd282" -->
### To Switch to X11 (for advanced trackpad control)
1. Log out
2. On login screen, click your username
3. Click the **gear icon** (bottom right)
4. Select **"Ubuntu on Xorg"**
5. Log in

<!-- section_id: "73946f34-1981-4684-af37-d9f3aa275738" -->
### To Switch to Wayland (default, more secure)
1. Log out
2. On login screen, click your username
3. Click the **gear icon** (bottom right)
4. Select **"Ubuntu"** (without Xorg)
5. Log in

<!-- section_id: "99add816-7c93-4807-bf74-182d446a2cb9" -->
## Design Philosophy

<!-- section_id: "e472e71b-f930-4866-be7e-b0fe7c5c2019" -->
### Piecewise vs Smooth Acceleration
- **Piecewise (X11)**: Distinct zones with consistent behavior - predictable, tunable
- **Smooth (default)**: Gradual changes - can feel unpredictable

<!-- section_id: "2a75c05b-a675-415d-a4f9-99140d578baf" -->
### Why Different Cursor vs Scroll Settings?
- **Cursor**: Needs extreme precision (0.0001x) for pixel-perfect work
- **Scroll**: Needs effective movement even when slow (0.1x minimum)

<!-- section_id: "02350d14-369a-4a13-8fe9-cad26615c6c8" -->
### Zone Progression
- **Cursor (~3x)**: Distinct precision tiers
- **Scroll (~1.5-2x)**: Smoother feel between zones

<!-- section_id: "717b26f0-1711-4d8e-8cd3-24a8a2bde628" -->
## Troubleshooting

| Issue | Wayland Solution | X11 Solution |
|-------|-----------------|--------------|
| Cursor too fast | Decrease gsettings speed | Reduce curve multipliers |
| Cursor too slow | Increase gsettings speed | Increase curve multipliers |
| Scroll too fast | Increase hwdb virtual size | Increase Scrolling Pixel Distance |
| Scroll too slow | Decrease hwdb virtual size | Decrease Scrolling Pixel Distance |
| Settings not applying | Logout/login or reboot | Run trackpad-settings.sh |

<!-- section_id: "c909ae89-9683-482c-9fb1-f2d1a978b442" -->
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Dec 31, 2025 | Initial X11 config with 7-zone cursor + 11-zone scroll |
| 2.0 | Jan 11, 2026 | Added Wayland support, reorganized into x11/wayland folders |

<!-- section_id: "fa19362b-48a5-4c90-b376-7830dfc7975e" -->
## Related Documentation

- [Wayland Configuration](wayland/configuration.md) - For Wayland users
- [X11 Configuration](x11/README.md) - For X11 users with full control
- [Setup Hub Guide](https://github.com/Dawson2025/setup-hub/blob/main/docs/ubuntu-trackpad-advanced-config.md) - Full iteration history
