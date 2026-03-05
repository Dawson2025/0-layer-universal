---
resource_id: "91ae6a1d-2487-4e99-9806-31e7ce3dc8d2"
resource_type: "document"
resource_name: "configuration.sync-conflict-20260126-035819-IF2WOGZ"
---
# Scroll Configuration

**Last Updated**: December 31, 2025
**System**: Ubuntu 24.04 GNOME
**Driver**: libinput

<!-- section_id: "93b35a36-61d6-4403-bcea-935e01504f2a" -->
## Current Configuration

<!-- section_id: "5cf5f7ee-605d-49d0-9c4c-ead6fe7bb65b" -->
### Base Settings
```bash
# Set scrolling pixel distance (higher = slower baseline)
xinput set-prop <TRACKPAD_ID> "libinput Scrolling Pixel Distance" 40

# Enable custom acceleration profile (same as cursor)
xinput set-prop <TRACKPAD_ID> "libinput Accel Profile Enabled" 0, 0, 1
```

<!-- section_id: "bcfb1479-2c79-4a8c-8747-5356e183ea9e" -->
### Acceleration Curve (11-Zone Piecewise Function)
```bash
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Step" 0.05
```

<!-- section_id: "f81b76b7-9ca6-4e27-9b9e-375557d6c4d8" -->
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

<!-- section_id: "c71c4413-89cd-40e8-a3ca-96640f12a274" -->
## Design Rationale

<!-- section_id: "c6024fe0-c92c-4b83-84bb-2c450dd114e8" -->
### Why 11 Zones (vs Cursor's 7)?
- **Smoother transitions**: More zones = smaller jumps between speeds
- **Better feel**: Scrolling benefits from very smooth acceleration
- **Wider range**: 11 zones span 0.1x to 1.5x with gradual steps

<!-- section_id: "d9693550-861b-4154-b01f-a8619dfa05ce" -->
### Why ~1.5-2x Progression (vs Cursor's ~3x)?
- Cursor needs distinct precision zones, scrolling needs smoothness
- Smaller jumps (0.1 → 0.15 → 0.25) feel more natural for scrolling
- Less jarring when transitioning between scroll speeds

<!-- section_id: "fa7fdd89-948b-4cd8-bc08-2ae31ee1fb86" -->
### Why Start at 0.1x (vs Cursor's 0.0001x)?
- Scrolling doesn't need extreme precision like cursor placement
- 0.1x minimum ensures slow scrolling still moves the page effectively
- Starting too low (0.01x) made slow scrolling feel ineffective

<!-- section_id: "951606fc-5125-49be-a15e-f614a3f6e8dd" -->
### Why Maximum 1.5x (vs Cursor's 0.1x)?
- Scrolling benefits from faster maximum speed
- 1.5x allows quick page traversal when flicking
- Combined with pixel distance 40, this provides good control

<!-- section_id: "c704d238-39b2-42f8-ab30-35114d2d4e7c" -->
### Why Pixel Distance 40?
- Default is 15 (too fast for baseline scrolling)
- 40 slows down baseline scroll speed
- Combined with acceleration zones, provides controlled scrolling

<!-- section_id: "78a6ac79-ba3f-41cf-8e39-646d934e579c" -->
## Key Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Pixel Distance | 40 | Baseline scroll speed (higher = slower) |
| Step Size | 0.05 | Controls velocity range per zone |
| Zones | 11 | Number of distinct speed tiers |
| Minimum Multiplier | 0.1x | Effective slow scrolling |
| Maximum Multiplier | 1.5x | Fast page traversal |
| Progression Factor | ~1.5-2x | Smooth multiplier increase between zones |

<!-- section_id: "2df31b47-cef8-44c6-b24e-c714c14a00df" -->
## Differences from Cursor Configuration

| Aspect | Cursor | Scroll | Reason |
|--------|--------|--------|--------|
| Zones | 7 | 11 | Scrolling needs smoother transitions |
| Min Speed | 0.0001x | 0.1x | Scrolling needs effectiveness over precision |
| Max Speed | 0.1x | 1.5x | Scrolling benefits from higher top speed |
| Progression | ~3x | ~1.5-2x | Smaller jumps feel better for scrolling |
| Purpose | Precision placement | Smooth page navigation | Different use cases |

<!-- section_id: "38ff484c-43c7-480d-95fa-b83dd530cf63" -->
## Adjustment Guidelines

<!-- section_id: "07bda121-3808-46b6-a8ff-e0711938c912" -->
### To make slow scrolling more effective
```bash
# Increase minimum zone values
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.15 0.15 0.2 0.2 0.3 0.3 0.4 0.4 0.55 0.55 0.7 0.7 0.85 0.85 0.95 0.95 1.05 1.05 1.25 1.25 1.5
```

<!-- section_id: "2d8dd087-96de-420c-9686-b832d39d3f01" -->
### To slow down baseline scrolling
```bash
# Increase pixel distance
xinput set-prop <TRACKPAD_ID> "libinput Scrolling Pixel Distance" 50
```

<!-- section_id: "682e0135-2e3d-46f7-9431-4732a9b5379e" -->
### To speed up fast scrolling
```bash
# Increase maximum zone value
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 2.0
```

<!-- section_id: "be0471f9-fd5c-48b5-899f-edfa59e848ef" -->
### To make transitions even smoother
```bash
# Add more zones with smaller jumps (example with 15 zones)
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.12 0.12 0.15 0.15 0.2 0.2 0.25 0.25 0.3 0.3 0.4 0.4 0.5 0.5 0.6 0.6 0.7 0.7 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
```

<!-- section_id: "b666bc2d-80a6-45d2-9116-d88cc6d6d7dd" -->
### To require faster physical movement for zone transitions
```bash
# Increase step size
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Step" 0.1
```

<!-- section_id: "26d04723-f131-4863-b29d-e87934b6c130" -->
## Troubleshooting

<!-- section_id: "5ac11fae-6069-4da2-883f-a7381ef8fd04" -->
### Slow scrolling doesn't move the page enough
- Increase minimum zone multipliers (0.1 → 0.15 or 0.2)
- Decrease pixel distance (40 → 35 or 30)

<!-- section_id: "0d7454aa-fb5b-4daa-b339-969c200ebb7a" -->
### Fast scrolling is too aggressive
- Decrease maximum zone multiplier (1.5 → 1.2 or 1.0)
- Increase step size to make fast zones harder to reach

<!-- section_id: "b53693bc-0896-458a-b967-c53806639a17" -->
### Scrolling feels jumpy
- Add more zones for smoother transitions
- Reduce progression factor (make smaller jumps between zones)
- Decrease step size for more gradual zone changes

<!-- section_id: "e2238ba1-a03e-4e06-9cd9-9241cdb4577c" -->
### Scrolling is too fast overall
- Increase pixel distance (40 → 50 or 60)
- Reduce all multipliers proportionally

<!-- section_id: "a89619ae-a8a3-4556-aa5a-186a275c7ef6" -->
## Related Documentation
- [Cursor Configuration](../cursor/configuration.md)
- [Full Trackpad Setup Guide](/home/dawson/code/setup-hub/docs/ubuntu-trackpad-advanced-config.md)
