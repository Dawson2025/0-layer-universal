---
resource_id: "fa548aa0-644e-4de4-a553-017ba5006022"
resource_type: "document"
resource_name: "README.sync-conflict-20260126-102106-IF2WOGZ"
---
# Trackpad Configuration

**Last Updated**: December 31, 2025
**System**: Ubuntu 24.04 GNOME
**Hardware**: ELAN06FA:00 04F3:32FD Touchpad
**Driver**: libinput

<!-- section_id: "101f7697-4751-490e-950e-7d08e2f54d29" -->
## Overview

This directory contains the complete trackpad configuration using custom libinput acceleration profiles. The configuration uses piecewise functions to create distinct speed zones for both cursor movement and scrolling.

<!-- section_id: "7363d378-49ca-44f9-95e8-371bbce1cae6" -->
## Directory Structure

```
trackpad/
├── README.md                    # This file
├── cursor/
│   └── configuration.md         # Cursor movement settings and zones
└── scroll/
    └── configuration.md         # Scroll settings and zones
```

<!-- section_id: "b8a79e64-226c-4f35-bec2-38412b450ad8" -->
## Quick Summary

<!-- section_id: "3f47b13f-5ab0-4b1c-ad27-642c174ffc60" -->
### Cursor Movement
- **7 zones**: Precision-focused (0.0001x to 0.1x)
- **Progression**: ~3x between zones
- **Purpose**: Pixel-perfect precision for slow movements, controlled speed for fast movements

<!-- section_id: "a3938a2b-3330-4aed-b187-6a9dfc9c80a2" -->
### Scrolling
- **11 zones**: Smoothness-focused (0.1x to 1.5x)
- **Progression**: ~1.5-2x between zones
- **Purpose**: Effective slow scrolling, smooth acceleration to fast page traversal

<!-- section_id: "74ddaf51-4511-4709-b6f5-f59c642d32c8" -->
## Key Configuration Files

**Active Configuration**: `~/.config/trackpad-settings.sh`
- Auto-runs on login via `~/.config/autostart/trackpad-settings.desktop`
- Contains all current settings
- Persists across reboots

<!-- section_id: "564385af-27e0-48b6-8299-369714b87d8b" -->
## Current Settings at a Glance

| Setting | Cursor | Scroll | Purpose |
|---------|--------|--------|---------|
| **Zones** | 7 | 11 | Cursor: precision, Scroll: smoothness |
| **Min Speed** | 0.0001x | 0.1x | Cursor needs extreme precision |
| **Max Speed** | 0.1x | 1.5x | Scroll benefits from higher speeds |
| **Step Size** | 0.05 | 0.05 | Both use wide zone spacing |
| **Base Speed** | -1.0 | -1.0 | Minimum for both |
| **Progression** | ~3x | ~1.5-2x | Cursor: distinct zones, Scroll: smooth |

<!-- section_id: "a3de216e-1890-46e9-ba2e-1a6f42e4ead3" -->
## Implementation

Both cursor and scroll use libinput's **custom acceleration profile**, which allows:
- Independent configuration of cursor and scroll acceleration
- Piecewise functions via repeated values (e.g., "0.001 0.001" creates a flat zone)
- Precise control over zone boundaries via step size
- Velocity-based acceleration (faster physical movement = higher multiplier)

<!-- section_id: "fc101318-27a4-497c-b2e1-b3db05da0173" -->
## Design Philosophy

<!-- section_id: "2940d5b3-3572-4f6f-a524-e2df7ff177d4" -->
### Piecewise Over Smooth Curves
- **Predictable**: Each zone maintains consistent behavior
- **Intentional**: Harder to accidentally activate fast zones
- **Tunable**: Can adjust each zone independently

<!-- section_id: "d7cd3930-6532-4ac1-9f90-a2cbdea81ce2" -->
### Independent Cursor & Scroll
- **Different use cases**: Cursor needs precision, scroll needs effectiveness
- **Different zone counts**: More zones where smoothness matters
- **Different multiplier ranges**: Each optimized for its purpose

<!-- section_id: "6f8d36e2-c72b-4eb3-8c69-47dc5155280b" -->
### Extensive Iteration
- Started with smooth curves → too unpredictable
- Tried simple multipliers → not enough control
- Arrived at piecewise functions → optimal for both feel and control

<!-- section_id: "dd5b92e5-ce79-40aa-b5a6-bd6eb044d971" -->
## Quick Reference Commands

<!-- section_id: "9257d8cf-b0b5-4ae8-9b93-8fde25f8b2a2" -->
### Check Current Settings
```bash
# Cursor acceleration
xinput list-props 10 | grep "Custom Motion"

# Scroll acceleration
xinput list-props 10 | grep "Custom Scroll"

# Base speed
xinput list-props 10 | grep "Accel Speed"
```

<!-- section_id: "d586241f-23f1-4003-9b4d-dc2666ea9649" -->
### Apply Settings Manually
```bash
# Run the autostart script
~/.config/trackpad-settings.sh
```

<!-- section_id: "5a4b4846-09b6-47e7-965f-7015bfcd83d5" -->
### Find Trackpad Device ID
```bash
xinput list | grep -i touchpad
```

<!-- section_id: "07c9fa75-75ca-42b4-b294-df44e1a06f5a" -->
## Related Documentation

- [Cursor Configuration Details](cursor/configuration.md)
- [Scroll Configuration Details](scroll/configuration.md)
- [Complete Setup Guide](/home/dawson/code/setup-hub/docs/ubuntu-trackpad-advanced-config.md)
  - Includes full iteration history
  - Troubleshooting guide
  - Key insights and learnings

<!-- section_id: "f4d220c1-7d15-4408-935e-2f3369d9a90c" -->
## Key Learnings

1. **Step size controls zone boundaries**: Small step (0.002) = narrow zones, large step (0.05) = wide zones
2. **Zone progression matters**: ~3x feels natural for cursor, ~1.5-2x feels smoother for scroll
3. **Curve shape > base speed**: Starting point of acceleration curve matters more than base speed setting
4. **More zones = smoother**: But diminishing returns beyond 7-11 zones
5. **Different tools for different jobs**: Cursor optimized for precision, scroll optimized for smoothness

<!-- section_id: "1bc90acf-becb-4a86-89d6-594b5e9f2fb1" -->
## Version History

- **v1.0** (Dec 31, 2025): Initial 7-zone cursor + 11-zone scroll configuration
  - Cursor: 0.0001x to 0.1x with ~3x progression
  - Scroll: 0.1x to 1.5x with ~1.5-2x progression
  - Step size: 0.05 for both
