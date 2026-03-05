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

## Overview

This directory contains the complete trackpad configuration using custom libinput acceleration profiles. The configuration uses piecewise functions to create distinct speed zones for both cursor movement and scrolling.

## Directory Structure

```
trackpad/
├── README.md                    # This file
├── cursor/
│   └── configuration.md         # Cursor movement settings and zones
└── scroll/
    └── configuration.md         # Scroll settings and zones
```

## Quick Summary

### Cursor Movement
- **7 zones**: Precision-focused (0.0001x to 0.1x)
- **Progression**: ~3x between zones
- **Purpose**: Pixel-perfect precision for slow movements, controlled speed for fast movements

### Scrolling
- **11 zones**: Smoothness-focused (0.1x to 1.5x)
- **Progression**: ~1.5-2x between zones
- **Purpose**: Effective slow scrolling, smooth acceleration to fast page traversal

## Key Configuration Files

**Active Configuration**: `~/.config/trackpad-settings.sh`
- Auto-runs on login via `~/.config/autostart/trackpad-settings.desktop`
- Contains all current settings
- Persists across reboots

## Current Settings at a Glance

| Setting | Cursor | Scroll | Purpose |
|---------|--------|--------|---------|
| **Zones** | 7 | 11 | Cursor: precision, Scroll: smoothness |
| **Min Speed** | 0.0001x | 0.1x | Cursor needs extreme precision |
| **Max Speed** | 0.1x | 1.5x | Scroll benefits from higher speeds |
| **Step Size** | 0.05 | 0.05 | Both use wide zone spacing |
| **Base Speed** | -1.0 | -1.0 | Minimum for both |
| **Progression** | ~3x | ~1.5-2x | Cursor: distinct zones, Scroll: smooth |

## Implementation

Both cursor and scroll use libinput's **custom acceleration profile**, which allows:
- Independent configuration of cursor and scroll acceleration
- Piecewise functions via repeated values (e.g., "0.001 0.001" creates a flat zone)
- Precise control over zone boundaries via step size
- Velocity-based acceleration (faster physical movement = higher multiplier)

## Design Philosophy

### Piecewise Over Smooth Curves
- **Predictable**: Each zone maintains consistent behavior
- **Intentional**: Harder to accidentally activate fast zones
- **Tunable**: Can adjust each zone independently

### Independent Cursor & Scroll
- **Different use cases**: Cursor needs precision, scroll needs effectiveness
- **Different zone counts**: More zones where smoothness matters
- **Different multiplier ranges**: Each optimized for its purpose

### Extensive Iteration
- Started with smooth curves → too unpredictable
- Tried simple multipliers → not enough control
- Arrived at piecewise functions → optimal for both feel and control

## Quick Reference Commands

### Check Current Settings
```bash
# Cursor acceleration
xinput list-props 10 | grep "Custom Motion"

# Scroll acceleration
xinput list-props 10 | grep "Custom Scroll"

# Base speed
xinput list-props 10 | grep "Accel Speed"
```

### Apply Settings Manually
```bash
# Run the autostart script
~/.config/trackpad-settings.sh
```

### Find Trackpad Device ID
```bash
xinput list | grep -i touchpad
```

## Related Documentation

- [Cursor Configuration Details](cursor/configuration.md)
- [Scroll Configuration Details](scroll/configuration.md)
- [Complete Setup Guide](/home/dawson/code/setup-hub/docs/ubuntu-trackpad-advanced-config.md)
  - Includes full iteration history
  - Troubleshooting guide
  - Key insights and learnings

## Key Learnings

1. **Step size controls zone boundaries**: Small step (0.002) = narrow zones, large step (0.05) = wide zones
2. **Zone progression matters**: ~3x feels natural for cursor, ~1.5-2x feels smoother for scroll
3. **Curve shape > base speed**: Starting point of acceleration curve matters more than base speed setting
4. **More zones = smoother**: But diminishing returns beyond 7-11 zones
5. **Different tools for different jobs**: Cursor optimized for precision, scroll optimized for smoothness

## Version History

- **v1.0** (Dec 31, 2025): Initial 7-zone cursor + 11-zone scroll configuration
  - Cursor: 0.0001x to 0.1x with ~3x progression
  - Scroll: 0.1x to 1.5x with ~1.5-2x progression
  - Step size: 0.05 for both
