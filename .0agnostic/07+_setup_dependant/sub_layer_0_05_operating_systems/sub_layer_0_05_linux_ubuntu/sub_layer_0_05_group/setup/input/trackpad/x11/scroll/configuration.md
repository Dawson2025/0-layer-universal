---
resource_id: "b8c463b8-bd38-4c05-a303-da6ab098594b"
resource_type: "document"
resource_name: "configuration"
---
# Scroll Configuration

**Last Updated**: January 11, 2026
**System**: Ubuntu 24.04 GNOME
**Driver**: libinput

<!-- section_id: "d0460db5-5175-4c96-b365-b24db5043142" -->
## Current Configuration

<!-- section_id: "caced589-39e8-476f-8f99-69bc67d76a57" -->
### Base Settings
```bash
# Set scrolling pixel distance (higher = slower baseline)
xinput set-prop <TRACKPAD_ID> "libinput Scrolling Pixel Distance" 40

# Enable custom acceleration profile (same as cursor)
xinput set-prop <TRACKPAD_ID> "libinput Accel Profile Enabled" 0, 0, 1
```

<!-- section_id: "3109d62e-ede5-4ed6-9921-aabac9afca45" -->
### Acceleration Curve (11-Zone Piecewise Function)
```bash
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Step" 0.05
```

<!-- section_id: "fa57c31e-763e-4df1-b85a-0018ab174fc4" -->
## Zone Breakdown

| Zone | Velocity Range | Multiplier | Use Case |
|------|----------------|------------|----------|
| 1 | 0.00 - 0.10 | 0.1x | Careful reading, line-by-line |
| 2 | 0.10 - 0.20 | 0.15x | Slow browsing |
| 3 | 0.20 - 0.30 | 0.25x | Paragraph navigation |
| 4 | 0.30 - 0.40 | 0.35x | Section navigation |
| 5 | 0.40 - 0.50 | 0.5x | Normal scrolling |
| 6 | 0.50 - 0.60 | 0.65x | Quick browsing |
| 7 | 0.60 - 0.70 | 0.8x | Fast navigation |
| 8 | 0.70 - 0.80 | 0.9x | Rapid scrolling |
| 9 | 0.80 - 0.90 | 1.0x | Very fast scrolling |
| 10 | 0.90 - 1.00 | 1.2x | Page skimming |
| 11 | 1.00+ | 1.5x | Maximum speed |

<!-- section_id: "7c856bc3-43ce-4b0b-8bf5-d0d4512badc7" -->
## Why 11 Zones (vs Cursor's 7)?

| Aspect | Cursor | Scroll | Reason |
|--------|--------|--------|--------|
| **Zone Count** | 7 | 11 | Scrolling benefits from smoother transitions |
| **Progression** | ~3x | ~1.5-2x | Smaller jumps feel better for scrolling |
| **Min Speed** | 0.0001x | 0.1x | Scrolling needs effectiveness, not precision |
| **Max Speed** | 0.1x | 1.5x | Scrolling benefits from higher top speed |

<!-- section_id: "c6d83891-307f-4a0a-aebd-3332a4299f7f" -->
### Key Differences Explained

**Cursor needs precision**: Pixel-perfect placement requires extremely slow zones (0.0001x)

**Scroll needs effectiveness**: Even slow scrolling should move the page meaningfully (0.1x minimum)

**Scroll needs smoothness**: More zones with smaller jumps feel natural when scrolling

**Scroll can be faster**: Flicking through pages benefits from 1.5x max speed

<!-- section_id: "d14c3366-4d1f-4c71-a5e7-2b6eac5d70e1" -->
## How Piecewise Scroll Acceleration Works

```
0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
    └Zone1┘ └Zone 2┘ └Zone 3┘ └Zone 4┘ └Zone5┘ └Zone 6┘ └Zone7┘ └Zone8┘ └Zone9┘ └Zone10┘ Zone11
```

- Repeated values create flat "plateaus" within each zone
- Step size 0.05 means each zone spans 0.10 velocity units
- 11 zones × 0.05 step = ~0.55 velocity range

<!-- section_id: "f495fb67-db83-4064-beb2-e39fa255c889" -->
## Key Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Pixel Distance | 40 | Baseline scroll speed (default=15) |
| Profile | Custom (0, 0, 1) | Enables piecewise acceleration |
| Step Size | 0.05 | Controls zone width (matches cursor) |
| Zones | 11 | Number of speed tiers |
| Min Multiplier | 0.1x | Effective slow scrolling |
| Max Multiplier | 1.5x | Fast page traversal |
| Progression | ~1.5-2x | Smooth jumps between zones |

<!-- section_id: "42e2feee-d9a7-4224-9109-fb5f54d382c5" -->
## Adjustment Guide

<!-- section_id: "f2d4bf9c-ba21-4fae-a625-e8b39b488a66" -->
### Slower Baseline Scrolling
```bash
# Increase pixel distance (40 → 50)
xinput set-prop <ID> "libinput Scrolling Pixel Distance" 50
```

<!-- section_id: "4ad74395-cb19-467f-b21f-f2b27b5305d5" -->
### Faster Slow-Zone Scrolling
```bash
# Increase minimum zone multiplier (0.1 → 0.15)
xinput set-prop <ID> "libinput Accel Custom Scroll Points" 0.0 0.15 0.15 0.2 0.2 0.3 0.3 0.4 0.4 0.55 0.55 0.7 0.7 0.85 0.85 0.95 0.95 1.05 1.05 1.25 1.25 1.5
```

<!-- section_id: "d44229ae-6bbd-4719-8b28-ee72b2f2d93c" -->
### Faster Maximum Speed
```bash
# Increase max from 1.5x to 2.0x
xinput set-prop <ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 2.0
```

<!-- section_id: "e7585513-5b68-4dc1-8ad0-d492aab20574" -->
### Even Smoother Transitions (15 zones)
```bash
# Add more intermediate zones
xinput set-prop <ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.12 0.12 0.15 0.15 0.2 0.2 0.25 0.25 0.32 0.32 0.4 0.4 0.5 0.5 0.6 0.6 0.72 0.72 0.85 0.85 1.0 1.0 1.2 1.2 1.5
```

<!-- section_id: "a271f910-0e44-4161-b93c-c3d09a4981f7" -->
### Harder to Reach Fast Zones
```bash
# Increase step size from 0.05 to 0.1
xinput set-prop <ID> "libinput Accel Custom Scroll Step" 0.1
```

<!-- section_id: "68e75e64-d0a7-4693-8d4b-fd794c5fcdc6" -->
## Iteration History

Scroll configuration evolved separately from cursor:

1. **Simple 2-zone (0.5x to 1.01x)**: Too simple, slow scrolling ineffective
2. **7-zone (0.01x to 1.0x)**: Better but slow scrolling still too slow
3. **7-zone (increased minimums)**: Transitions felt jumpy with 3x progression
4. **11-zone (0.1x to 1.5x)**: **Final solution** - smooth transitions, effective slow scrolling

Key insight: **Scroll needs more zones with smaller jumps** than cursor. The ~3x progression that works for cursor feels jarring for scroll.

<!-- section_id: "34185246-b0fd-4c02-92d9-2c8a715023cb" -->
## Pixel Distance Explained

`libinput Scrolling Pixel Distance` controls baseline scroll speed:

| Value | Effect |
|-------|--------|
| 15 | Default, quite fast |
| 25 | Moderate slow-down |
| 40 | **Current setting** - noticeably slower baseline |
| 50 | Very slow baseline |
| 60 | Extremely slow baseline |

This interacts with the acceleration curve:
- Higher pixel distance = slower baseline
- Acceleration curve multiplies from this baseline
- Current: 40 pixel distance × 0.1x to 1.5x multipliers

<!-- section_id: "d276e790-96c0-4934-9130-125645e1815a" -->
## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Slow scrolling doesn't move enough | Min multiplier too low | Increase 0.1 to 0.15 or 0.2 |
| Slow scrolling too fast | Min multiplier too high | Decrease 0.1 to 0.05 |
| Fast scrolling too aggressive | Max multiplier too high | Reduce 1.5 to 1.2 or 1.0 |
| Transitions feel jumpy | Not enough zones | Add more zones (11 → 15) |
| Overall too fast | Pixel distance too low | Increase from 40 to 50+ |
| Overall too slow | Pixel distance too high | Decrease from 40 to 30 |
| Settings not applying | Wrong device ID | Check with `xinput list` |

<!-- section_id: "ade0de28-30c3-4a7d-a011-c4ec39b1c62c" -->
## Related

- [Cursor Configuration](../cursor/configuration.md)
- [Main Trackpad README](../README.md)
