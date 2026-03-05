---
resource_id: "9cc756bf-2788-40d9-ae2c-59fc311e1fe0"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-035815-IF2WOGZ"
---
# Trackpad Configuration

**Last Updated**: December 31, 2025
**System**: Ubuntu 24.04 GNOME
**Hardware**: ELAN06FA:00 04F3:32FD Touchpad
**Driver**: libinput

<!-- section_id: "77efeab6-dfde-451b-b1d2-8f5f75db38bf" -->
## Overview

This directory contains the complete trackpad configuration using custom libinput acceleration profiles. The configuration uses piecewise functions to create distinct speed zones for both cursor movement and scrolling.

<!-- section_id: "a5cc2c03-d308-4e8e-835b-5183389d8e8d" -->
## Directory Structure

```
trackpad/
├── README.md                    # This file
├── cursor/
│   └── configuration.md         # Cursor movement settings and zones
└── scroll/
    └── configuration.md         # Scroll settings and zones
```

<!-- section_id: "a75cda50-6fb6-4c7e-9d0f-715bcabbb347" -->
## Quick Summary

<!-- section_id: "7bb463a9-f334-453f-ab42-be9753131311" -->
### Cursor Movement
- **7 zones**: Precision-focused (0.0001x to 0.1x)
- **Progression**: ~3x between zones
- **Purpose**: Pixel-perfect precision for slow movements, controlled speed for fast movements

<!-- section_id: "081e2c44-5eb8-40e2-8647-0db6dc16a2ab" -->
### Scrolling
- **11 zones**: Smoothness-focused (0.1x to 1.5x)
- **Progression**: ~1.5-2x between zones
- **Purpose**: Effective slow scrolling, smooth acceleration to fast page traversal

<!-- section_id: "34479fd5-c842-4b13-9f4e-86d39588eb43" -->
## Key Configuration Files

**Active Configuration**: `~/.config/trackpad-settings.sh`
- Auto-runs on login via `~/.config/autostart/trackpad-settings.desktop`
- Contains all current settings
- Persists across reboots

<!-- section_id: "95abed17-5202-4167-8400-624dbf4c423b" -->
## Current Settings at a Glance

| Setting | Cursor | Scroll | Purpose |
|---------|--------|--------|---------|
| **Zones** | 7 | 11 | Cursor: precision, Scroll: smoothness |
| **Min Speed** | 0.0001x | 0.1x | Cursor needs extreme precision |
| **Max Speed** | 0.1x | 1.5x | Scroll benefits from higher speeds |
| **Step Size** | 0.05 | 0.05 | Both use wide zone spacing |
| **Base Speed** | -1.0 | -1.0 | Minimum for both |
| **Progression** | ~3x | ~1.5-2x | Cursor: distinct zones, Scroll: smooth |

<!-- section_id: "61642fdd-d6da-4194-ba85-f8b8378f7ea9" -->
## Implementation

Both cursor and scroll use libinput's **custom acceleration profile**, which allows:
- Independent configuration of cursor and scroll acceleration
- Piecewise functions via repeated values (e.g., "0.001 0.001" creates a flat zone)
- Precise control over zone boundaries via step size
- Velocity-based acceleration (faster physical movement = higher multiplier)

<!-- section_id: "c4d4051b-c924-41b6-b500-f8d140360de7" -->
## Design Philosophy

<!-- section_id: "4ff75e25-c7ee-466e-845e-caf869e7b7b7" -->
### Piecewise Over Smooth Curves
- **Predictable**: Each zone maintains consistent behavior
- **Intentional**: Harder to accidentally activate fast zones
- **Tunable**: Can adjust each zone independently

<!-- section_id: "10870705-3ebf-4571-bc10-905953e5736a" -->
### Independent Cursor & Scroll
- **Different use cases**: Cursor needs precision, scroll needs effectiveness
- **Different zone counts**: More zones where smoothness matters
- **Different multiplier ranges**: Each optimized for its purpose

<!-- section_id: "6971aa38-0371-488e-b8d0-ee885a7d52b0" -->
### Extensive Iteration
- Started with smooth curves → too unpredictable
- Tried simple multipliers → not enough control
- Arrived at piecewise functions → optimal for both feel and control

<!-- section_id: "8f83380f-87e1-4490-b335-939c62806e6a" -->
## Quick Reference Commands

<!-- section_id: "ef508d1a-c7f2-445c-b6ea-785027276ff4" -->
### Check Current Settings
```bash
# Cursor acceleration
xinput list-props 10 | grep "Custom Motion"

# Scroll acceleration
xinput list-props 10 | grep "Custom Scroll"

# Base speed
xinput list-props 10 | grep "Accel Speed"
```

<!-- section_id: "38b78675-dca2-4ffe-b621-51ac3d106dae" -->
### Apply Settings Manually
```bash
# Run the autostart script
~/.config/trackpad-settings.sh
```

<!-- section_id: "ee627381-e38a-4319-af75-1f9c2e6782cc" -->
### Find Trackpad Device ID
```bash
xinput list | grep -i touchpad
```

<!-- section_id: "bb5de8b0-249a-4043-90ad-34f2ab8100bc" -->
## Related Documentation

- [Cursor Configuration Details](cursor/configuration.md)
- [Scroll Configuration Details](scroll/configuration.md)
- [Complete Setup Guide](/home/dawson/code/setup-hub/docs/ubuntu-trackpad-advanced-config.md)
  - Includes full iteration history
  - Troubleshooting guide
  - Key insights and learnings

<!-- section_id: "7171d4cf-d1a6-4c0e-a931-18602941975e" -->
## Key Learnings

1. **Step size controls zone boundaries**: Small step (0.002) = narrow zones, large step (0.05) = wide zones
2. **Zone progression matters**: ~3x feels natural for cursor, ~1.5-2x feels smoother for scroll
3. **Curve shape > base speed**: Starting point of acceleration curve matters more than base speed setting
4. **More zones = smoother**: But diminishing returns beyond 7-11 zones
5. **Different tools for different jobs**: Cursor optimized for precision, scroll optimized for smoothness

<!-- section_id: "baa0c119-4c7c-4735-8440-33932cc78a0c" -->
## Version History

- **v1.0** (Dec 31, 2025): Initial 7-zone cursor + 11-zone scroll configuration
  - Cursor: 0.0001x to 0.1x with ~3x progression
  - Scroll: 0.1x to 1.5x with ~1.5-2x progression
  - Step size: 0.05 for both
