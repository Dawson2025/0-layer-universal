---
resource_id: "f460cddd-1251-485a-8e2a-357b66481c8a"
resource_type: "document"
resource_name: "configuration.sync-conflict-20260126-035820-IF2WOGZ"
---
# Cursor Movement Configuration

**Last Updated**: December 31, 2025
**System**: Ubuntu 24.04 GNOME
**Driver**: libinput

## Current Configuration

### Base Settings
```bash
# Set base speed to minimum
gsettings set org.gnome.desktop.peripherals.touchpad speed -1.0
xinput set-prop <TRACKPAD_ID> "libinput Accel Speed" -1.0

# Enable custom acceleration profile
xinput set-prop <TRACKPAD_ID> "libinput Accel Profile Enabled" 0, 0, 1
```

### Acceleration Curve (7-Zone Piecewise Function)
```bash
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Points" 0.0 0.0001 0.0001 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.1
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Step" 0.05
```

## Zone Breakdown

| Zone | Trackpad Velocity Range | Cursor Speed Multiplier | Description |
|------|------------------------|------------------------|-------------|
| 1 | 0.00 - 0.10 | 0.0001x | Very slow (precision) |
| 2 | 0.10 - 0.20 | 0.0003x | Extra slow |
| 3 | 0.20 - 0.30 | 0.001x | Slow |
| 4 | 0.30 - 0.40 | 0.003x | Medium-slow |
| 5 | 0.40 - 0.50 | 0.01x | Medium |
| 6 | 0.50 - 0.60 | 0.03x | Medium-fast |
| 7 | 0.60+ | 0.1x | Fast |

## Design Rationale

### Why Piecewise Function?
- **Predictable behavior**: Each zone maintains consistent speed
- **Intentional transitions**: Harder to accidentally jump to fast zones
- **Precision control**: Zone 1 (0.0001x) allows pixel-perfect cursor placement

### Why ~3x Progression?
- 2x jumps (0.0001 → 0.0002) feel too gradual
- 10x jumps (0.001 → 0.01) feel too aggressive
- ~3x jumps (0.0001 → 0.0003 → 0.001 → 0.003) provide natural-feeling acceleration

### Why 7 Zones?
- Fewer zones (3-5): Too jumpy, not enough granularity
- More zones (10+): Diminishing returns, harder to feel distinct zones
- 7 zones: Optimal balance of smoothness and distinct behavior

### Why Step Size 0.05?
- Small step (0.002): Zones transition too quickly, hard to stay in slow zones
- Large step (0.05): Spreads zones across wide velocity range (~0.7 units total)
- Prevents accidental fast zone activation during medium movements

### Why Maximum 0.1x?
- Higher values (0.5x, 1.0x) made even fast movements feel uncontrollable
- 0.1x provides good speed for fast movements while maintaining control
- Combined with base speed -1.0, this is the optimal balance

## Key Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Base Speed | -1.0 | Minimum speed, provides extremely slow baseline |
| Step Size | 0.05 | Controls velocity range per zone |
| Zones | 7 | Number of distinct speed tiers |
| Minimum Multiplier | 0.0001x | Precision work |
| Maximum Multiplier | 0.1x | Fast movement |
| Progression Factor | ~3x | Multiplier increase between zones |

## Adjustment Guidelines

### To make slow movements even slower
```bash
# Reduce first zone values
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Points" 0.0 0.00005 0.00005 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.1
```

### To make fast movements faster
```bash
# Increase last zone value
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Points" 0.0 0.0001 0.0001 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.15
```

### To require faster physical movement for zone transitions
```bash
# Increase step size
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Step" 0.1
```

### To make transitions smoother (more gradual)
```bash
# Decrease step size
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Step" 0.03
```

## Related Documentation
- [Scroll Configuration](../scroll/configuration.md)
- [Full Trackpad Setup Guide](/home/dawson/code/setup-hub/docs/ubuntu-trackpad-advanced-config.md)
