# Scroll Configuration

**Last Updated**: December 31, 2025
**System**: Ubuntu 24.04 GNOME
**Driver**: libinput

## Current Configuration

### Base Settings
```bash
# Set scrolling pixel distance (higher = slower baseline)
xinput set-prop <TRACKPAD_ID> "libinput Scrolling Pixel Distance" 40

# Enable custom acceleration profile (same as cursor)
xinput set-prop <TRACKPAD_ID> "libinput Accel Profile Enabled" 0, 0, 1
```

### Acceleration Curve (11-Zone Piecewise Function)
```bash
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Step" 0.05
```

## Zone Breakdown

| Zone | Trackpad Velocity Range | Scroll Speed Multiplier | Description |
|------|------------------------|-------------------------|-------------|
| 1 | 0.00 - 0.10 | 0.1x | Very slow |
| 2 | 0.10 - 0.20 | 0.15x | Extra slow |
| 3 | 0.20 - 0.30 | 0.25x | Slow+ |
| 4 | 0.30 - 0.40 | 0.35x | Medium-slow |
| 5 | 0.40 - 0.50 | 0.5x | Medium |
| 6 | 0.50 - 0.60 | 0.65x | Medium+ |
| 7 | 0.60 - 0.70 | 0.8x | Medium-fast |
| 8 | 0.70 - 0.80 | 0.9x | Fast |
| 9 | 0.80 - 0.90 | 1.0x | Faster |
| 10 | 0.90 - 1.00 | 1.2x | Very fast |
| 11 | 1.00+ | 1.5x | Maximum |

## Design Rationale

### Why 11 Zones (vs Cursor's 7)?
- **Smoother transitions**: More zones = smaller jumps between speeds
- **Better feel**: Scrolling benefits from very smooth acceleration
- **Wider range**: 11 zones span 0.1x to 1.5x with gradual steps

### Why ~1.5-2x Progression (vs Cursor's ~3x)?
- Cursor needs distinct precision zones, scrolling needs smoothness
- Smaller jumps (0.1 → 0.15 → 0.25) feel more natural for scrolling
- Less jarring when transitioning between scroll speeds

### Why Start at 0.1x (vs Cursor's 0.0001x)?
- Scrolling doesn't need extreme precision like cursor placement
- 0.1x minimum ensures slow scrolling still moves the page effectively
- Starting too low (0.01x) made slow scrolling feel ineffective

### Why Maximum 1.5x (vs Cursor's 0.1x)?
- Scrolling benefits from faster maximum speed
- 1.5x allows quick page traversal when flicking
- Combined with pixel distance 40, this provides good control

### Why Pixel Distance 40?
- Default is 15 (too fast for baseline scrolling)
- 40 slows down baseline scroll speed
- Combined with acceleration zones, provides controlled scrolling

## Key Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Pixel Distance | 40 | Baseline scroll speed (higher = slower) |
| Step Size | 0.05 | Controls velocity range per zone |
| Zones | 11 | Number of distinct speed tiers |
| Minimum Multiplier | 0.1x | Effective slow scrolling |
| Maximum Multiplier | 1.5x | Fast page traversal |
| Progression Factor | ~1.5-2x | Smooth multiplier increase between zones |

## Differences from Cursor Configuration

| Aspect | Cursor | Scroll | Reason |
|--------|--------|--------|--------|
| Zones | 7 | 11 | Scrolling needs smoother transitions |
| Min Speed | 0.0001x | 0.1x | Scrolling needs effectiveness over precision |
| Max Speed | 0.1x | 1.5x | Scrolling benefits from higher top speed |
| Progression | ~3x | ~1.5-2x | Smaller jumps feel better for scrolling |
| Purpose | Precision placement | Smooth page navigation | Different use cases |

## Adjustment Guidelines

### To make slow scrolling more effective
```bash
# Increase minimum zone values
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.15 0.15 0.2 0.2 0.3 0.3 0.4 0.4 0.55 0.55 0.7 0.7 0.85 0.85 0.95 0.95 1.05 1.05 1.25 1.25 1.5
```

### To slow down baseline scrolling
```bash
# Increase pixel distance
xinput set-prop <TRACKPAD_ID> "libinput Scrolling Pixel Distance" 50
```

### To speed up fast scrolling
```bash
# Increase maximum zone value
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 2.0
```

### To make transitions even smoother
```bash
# Add more zones with smaller jumps (example with 15 zones)
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.12 0.12 0.15 0.15 0.2 0.2 0.25 0.25 0.3 0.3 0.4 0.4 0.5 0.5 0.6 0.6 0.7 0.7 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
```

### To require faster physical movement for zone transitions
```bash
# Increase step size
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Step" 0.1
```

## Troubleshooting

### Slow scrolling doesn't move the page enough
- Increase minimum zone multipliers (0.1 → 0.15 or 0.2)
- Decrease pixel distance (40 → 35 or 30)

### Fast scrolling is too aggressive
- Decrease maximum zone multiplier (1.5 → 1.2 or 1.0)
- Increase step size to make fast zones harder to reach

### Scrolling feels jumpy
- Add more zones for smoother transitions
- Reduce progression factor (make smaller jumps between zones)
- Decrease step size for more gradual zone changes

### Scrolling is too fast overall
- Increase pixel distance (40 → 50 or 60)
- Reduce all multipliers proportionally

## Related Documentation
- [Cursor Configuration](../cursor/configuration.md)
- [Full Trackpad Setup Guide](/home/dawson/code/setup-hub/docs/ubuntu-trackpad-advanced-config.md)
