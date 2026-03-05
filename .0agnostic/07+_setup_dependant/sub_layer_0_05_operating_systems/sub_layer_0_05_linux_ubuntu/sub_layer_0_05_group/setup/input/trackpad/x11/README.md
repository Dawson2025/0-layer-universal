---
resource_id: "3d1716c9-154a-493a-a62d-afa4c4519e28"
resource_type: "readme
document"
resource_name: "README"
---
# X11 Trackpad Configuration

**Last Updated**: January 11, 2026
**System**: Ubuntu 24.04 GNOME on X11 (Xorg)
**Hardware**: ELAN06FA:00 04F3:32FD Touchpad
**Driver**: libinput

<!-- section_id: "cdeb80f9-df97-4646-bb53-5f3c2e768283" -->
## Overview

X11 allows **advanced trackpad customization** using xinput and libinput's custom acceleration profiles. This includes:
- Custom piecewise acceleration curves
- Independent cursor and scroll acceleration
- Fine-grained zone control

**Note**: These settings **only work on X11**, not Wayland.

<!-- section_id: "b53ef8bd-bfe6-4fcd-bfa5-1287e3a413da" -->
## Directory Contents

```
x11/
├── README.md                    # This file
├── cursor/
│   └── configuration.md         # 7-zone cursor acceleration
├── scroll/
│   └── configuration.md         # 11-zone scroll acceleration
└── scripts/
    └── trackpad-settings.sh     # Autostart script
```

<!-- section_id: "f7c9d170-ba94-4876-849c-350d43ae4a1e" -->
## Quick Summary

| Feature | Cursor | Scroll |
|---------|--------|--------|
| Zones | 7 | 11 |
| Min Speed | 0.0001x | 0.1x |
| Max Speed | 0.1x | 1.5x |
| Progression | ~3x | ~1.5-2x |
| Step Size | 0.05 | 0.05 |

<!-- section_id: "b368b9d0-a915-4f11-a02b-bafefdda3b3a" -->
## Switching to X11

1. Log out
2. On login screen, click your username
3. Click the **gear icon** (bottom right)
4. Select **"Ubuntu on Xorg"**
5. Log in

<!-- section_id: "c54d9210-aa83-4107-bf7c-1ecb937d9d43" -->
## Applying Settings

```bash
# Copy script to config
cp scripts/trackpad-settings.sh ~/.config/

# Make executable
chmod +x ~/.config/trackpad-settings.sh

# Run immediately
~/.config/trackpad-settings.sh

# Create autostart entry
mkdir -p ~/.config/autostart
cat > ~/.config/autostart/trackpad-settings.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=Trackpad Settings
Exec=/home/$USER/.config/trackpad-settings.sh
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Comment=Apply custom trackpad settings on login
EOF
```

<!-- section_id: "a5d7d45f-7e48-46f8-94de-d9530e0fba7d" -->
## Why Use X11 for Trackpad?

| Advantage | Description |
|-----------|-------------|
| Piecewise acceleration | Distinct speed zones (not just smooth curves) |
| Extreme precision | 0.0001x multiplier for pixel-perfect control |
| Independent scroll | Separate acceleration curve for scrolling |
| Fine-tuned zones | 7+ zones with custom progression |
| Direct control | xinput provides immediate feedback |

<!-- section_id: "492732ef-76d2-49c9-b871-4692258f6230" -->
## Tradeoffs vs Wayland

| Aspect | X11 | Wayland |
|--------|-----|---------|
| Trackpad customization | Excellent | Limited |
| Security | Lower | Higher |
| Graphics smoothness | May tear | Smooth |
| Multi-monitor scaling | Worse | Better |
| Future support | Maintenance only | Active development |

<!-- section_id: "e6ee8474-6098-4744-a20b-cfe6459d0449" -->
## Related Documentation

- [Cursor Configuration](cursor/configuration.md)
- [Scroll Configuration](scroll/configuration.md)
- [Wayland Configuration](../wayland/configuration.md)
- [Main Trackpad README](../README.md)
