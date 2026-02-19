# X11 Trackpad Configuration

**Last Updated**: January 11, 2026
**System**: Ubuntu 24.04 GNOME on X11 (Xorg)
**Hardware**: ELAN06FA:00 04F3:32FD Touchpad
**Driver**: libinput

## Overview

X11 allows **advanced trackpad customization** using xinput and libinput's custom acceleration profiles. This includes:
- Custom piecewise acceleration curves
- Independent cursor and scroll acceleration
- Fine-grained zone control

**Note**: These settings **only work on X11**, not Wayland.

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

## Quick Summary

| Feature | Cursor | Scroll |
|---------|--------|--------|
| Zones | 7 | 11 |
| Min Speed | 0.0001x | 0.1x |
| Max Speed | 0.1x | 1.5x |
| Progression | ~3x | ~1.5-2x |
| Step Size | 0.05 | 0.05 |

## Switching to X11

1. Log out
2. On login screen, click your username
3. Click the **gear icon** (bottom right)
4. Select **"Ubuntu on Xorg"**
5. Log in

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

## Why Use X11 for Trackpad?

| Advantage | Description |
|-----------|-------------|
| Piecewise acceleration | Distinct speed zones (not just smooth curves) |
| Extreme precision | 0.0001x multiplier for pixel-perfect control |
| Independent scroll | Separate acceleration curve for scrolling |
| Fine-tuned zones | 7+ zones with custom progression |
| Direct control | xinput provides immediate feedback |

## Tradeoffs vs Wayland

| Aspect | X11 | Wayland |
|--------|-----|---------|
| Trackpad customization | Excellent | Limited |
| Security | Lower | Higher |
| Graphics smoothness | May tear | Smooth |
| Multi-monitor scaling | Worse | Better |
| Future support | Maintenance only | Active development |

## Related Documentation

- [Cursor Configuration](cursor/configuration.md)
- [Scroll Configuration](scroll/configuration.md)
- [Wayland Configuration](../wayland/configuration.md)
- [Main Trackpad README](../README.md)
