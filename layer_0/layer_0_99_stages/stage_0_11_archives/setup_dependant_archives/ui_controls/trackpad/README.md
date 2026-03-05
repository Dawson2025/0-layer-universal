---
resource_id: "4e93604f-f92e-4e06-ae1a-08a8ce8424c4"
resource_type: "readme
document"
resource_name: "README"
---
# Trackpad Configuration

**Last Updated**: December 31, 2025
**System**: Ubuntu 24.04 GNOME
**Hardware**: ELAN06FA:00 04F3:32FD Touchpad
**Driver**: libinput

<!-- section_id: "d753f8de-d3d0-4fa1-ac62-84a23ce5566c" -->
## Overview

This directory contains the complete trackpad configuration using custom libinput acceleration profiles. The configuration uses piecewise functions to create distinct speed zones for both cursor movement and scrolling.

<!-- section_id: "8e4c9f2f-70b3-4444-a972-5a7565c21193" -->
## Directory Structure

```
trackpad/
├── README.md                    # This file
├── cursor/
│   └── configuration.md         # Cursor movement settings and zones
└── scroll/
    └── configuration.md         # Scroll settings and zones
```

<!-- section_id: "b2cba77b-966e-4bff-a877-eb9f4e229674" -->
## Quick Summary

<!-- section_id: "573372ea-1857-424d-943c-a6d0e58856c5" -->
### Cursor Movement
- **7 zones**: Precision-focused (0.0001x to 0.1x)
- **Progression**: ~3x between zones
- **Purpose**: Pixel-perfect precision for slow movements, controlled speed for fast movements

<!-- section_id: "bb5b54c8-c10b-4b05-b334-35dccb648f04" -->
### Scrolling
- **11 zones**: Smoothness-focused (0.1x to 1.5x)
- **Progression**: ~1.5-2x between zones
- **Purpose**: Effective slow scrolling, smooth acceleration to fast page traversal

<!-- section_id: "cdb9e8c6-91f1-4cbc-9df2-9816ac13634d" -->
## Key Configuration Files

**Active Configuration**: `~/.config/trackpad-settings.sh`
- Auto-runs on login via `~/.config/autostart/trackpad-settings.desktop`
- Contains all current settings
- Persists across reboots

<!-- section_id: "d9c291da-97b5-4e79-b4b4-91d44ae3759c" -->
## Current Settings at a Glance

| Setting | Cursor | Scroll | Purpose |
|---------|--------|--------|---------|
| **Zones** | 7 | 11 | Cursor: precision, Scroll: smoothness |
| **Min Speed** | 0.0001x | 0.1x | Cursor needs extreme precision |
| **Max Speed** | 0.1x | 1.5x | Scroll benefits from higher speeds |
| **Step Size** | 0.05 | 0.05 | Both use wide zone spacing |
| **Base Speed** | -1.0 | -1.0 | Minimum for both |
| **Progression** | ~3x | ~1.5-2x | Cursor: distinct zones, Scroll: smooth |

<!-- section_id: "61447e7f-ac3c-4662-b194-4d359d918cc5" -->
## Implementation

Both cursor and scroll use libinput's **custom acceleration profile**, which allows:
- Independent configuration of cursor and scroll acceleration
- Piecewise functions via repeated values (e.g., "0.001 0.001" creates a flat zone)
- Precise control over zone boundaries via step size
- Velocity-based acceleration (faster physical movement = higher multiplier)

<!-- section_id: "363fa233-1dc0-4358-9167-2d222b0bebab" -->
## Design Philosophy

<!-- section_id: "8d0a4609-a462-4896-972c-db8b8bbd864c" -->
### Piecewise Over Smooth Curves
- **Predictable**: Each zone maintains consistent behavior
- **Intentional**: Harder to accidentally activate fast zones
- **Tunable**: Can adjust each zone independently

<!-- section_id: "0cbdcac0-7add-47e6-b339-cd631fae4731" -->
### Independent Cursor & Scroll
- **Different use cases**: Cursor needs precision, scroll needs effectiveness
- **Different zone counts**: More zones where smoothness matters
- **Different multiplier ranges**: Each optimized for its purpose

<!-- section_id: "c2b2044f-9c21-45fc-9335-6cabe786d184" -->
### Extensive Iteration
- Started with smooth curves → too unpredictable
- Tried simple multipliers → not enough control
- Arrived at piecewise functions → optimal for both feel and control

<!-- section_id: "9ce675b7-f0af-4288-bbf9-3744e7d8cca4" -->
## Quick Reference Commands

<!-- section_id: "6f151819-9976-439f-b6d6-fea4d536b53a" -->
### Check Current Settings
```bash
# Cursor acceleration
xinput list-props 10 | grep "Custom Motion"

# Scroll acceleration
xinput list-props 10 | grep "Custom Scroll"

# Base speed
xinput list-props 10 | grep "Accel Speed"
```

<!-- section_id: "93d927e8-b985-489e-aea2-daed8e98fe91" -->
### Apply Settings Manually
```bash
# Run the autostart script
~/.config/trackpad-settings.sh
```

<!-- section_id: "2435eb45-aef0-4bfe-8b01-7e19a7f31ba8" -->
### Find Trackpad Device ID
```bash
xinput list | grep -i touchpad
```

<!-- section_id: "26c93568-a4ef-44e3-bf97-0b718db42b2d" -->
## Related Documentation

- [Cursor Configuration Details](cursor/configuration.md)
- [Scroll Configuration Details](scroll/configuration.md)
- [Complete Setup Guide](/home/dawson/code/setup-hub/docs/ubuntu-trackpad-advanced-config.md)
  - Includes full iteration history
  - Troubleshooting guide
  - Key insights and learnings

<!-- section_id: "b26ba6d1-31ef-4f83-b288-62d7f6210f8b" -->
## Key Learnings

1. **Step size controls zone boundaries**: Small step (0.002) = narrow zones, large step (0.05) = wide zones
2. **Zone progression matters**: ~3x feels natural for cursor, ~1.5-2x feels smoother for scroll
3. **Curve shape > base speed**: Starting point of acceleration curve matters more than base speed setting
4. **More zones = smoother**: But diminishing returns beyond 7-11 zones
5. **Different tools for different jobs**: Cursor optimized for precision, scroll optimized for smoothness

<!-- section_id: "475b9bbd-9548-40de-aaad-e1a704b0ae32" -->
## Version History

- **v1.0** (Dec 31, 2025): Initial 7-zone cursor + 11-zone scroll configuration
  - Cursor: 0.0001x to 0.1x with ~3x progression
  - Scroll: 0.1x to 1.5x with ~1.5-2x progression
  - Step size: 0.05 for both
