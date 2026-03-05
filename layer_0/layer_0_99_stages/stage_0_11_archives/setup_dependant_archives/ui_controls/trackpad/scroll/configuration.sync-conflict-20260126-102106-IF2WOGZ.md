---
resource_id: "a7ab972a-1a7f-45f2-af8c-147bbeea8223"
resource_type: "document"
resource_name: "configuration.sync-conflict-20260126-102106-IF2WOGZ"
---
# Scroll Configuration

**Last Updated**: December 31, 2025
**System**: Ubuntu 24.04 GNOME
**Driver**: libinput

<!-- section_id: "9d7a906a-7f64-4b23-97bc-a3140075878f" -->
## Current Configuration

<!-- section_id: "6f97c43f-7020-4697-93a5-e51cf4f73762" -->
### Base Settings
```bash
# Set scrolling pixel distance (higher = slower baseline)
xinput set-prop <TRACKPAD_ID> "libinput Scrolling Pixel Distance" 40

# Enable custom acceleration profile (same as cursor)
xinput set-prop <TRACKPAD_ID> "libinput Accel Profile Enabled" 0, 0, 1
```

<!-- section_id: "9ec21934-600c-4bc4-98f0-608dfedc62f6" -->
### Acceleration Curve (11-Zone Piecewise Function)
```bash
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Step" 0.05
```

<!-- section_id: "f3b1b0e7-502c-4a46-8c95-6d9459304108" -->
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

<!-- section_id: "fe2593f7-c4ed-4857-abb6-f6fe6641179a" -->
## Design Rationale

<!-- section_id: "6199f489-67f2-460f-ae13-2d00c70441b4" -->
### Why 11 Zones (vs Cursor's 7)?
- **Smoother transitions**: More zones = smaller jumps between speeds
- **Better feel**: Scrolling benefits from very smooth acceleration
- **Wider range**: 11 zones span 0.1x to 1.5x with gradual steps

<!-- section_id: "0d530402-403b-4200-82d6-8ed46e415480" -->
### Why ~1.5-2x Progression (vs Cursor's ~3x)?
- Cursor needs distinct precision zones, scrolling needs smoothness
- Smaller jumps (0.1 → 0.15 → 0.25) feel more natural for scrolling
- Less jarring when transitioning between scroll speeds

<!-- section_id: "add121d2-a3e9-4fe2-8ac8-57834170ffe8" -->
### Why Start at 0.1x (vs Cursor's 0.0001x)?
- Scrolling doesn't need extreme precision like cursor placement
- 0.1x minimum ensures slow scrolling still moves the page effectively
- Starting too low (0.01x) made slow scrolling feel ineffective

<!-- section_id: "c76a2343-09fd-495b-9a85-9e4028012427" -->
### Why Maximum 1.5x (vs Cursor's 0.1x)?
- Scrolling benefits from faster maximum speed
- 1.5x allows quick page traversal when flicking
- Combined with pixel distance 40, this provides good control

<!-- section_id: "69f03b5d-65e4-49d7-afd9-96ed05c66098" -->
### Why Pixel Distance 40?
- Default is 15 (too fast for baseline scrolling)
- 40 slows down baseline scroll speed
- Combined with acceleration zones, provides controlled scrolling

<!-- section_id: "eb90ebcd-a292-4db6-9244-03b9cd23f711" -->
## Key Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Pixel Distance | 40 | Baseline scroll speed (higher = slower) |
| Step Size | 0.05 | Controls velocity range per zone |
| Zones | 11 | Number of distinct speed tiers |
| Minimum Multiplier | 0.1x | Effective slow scrolling |
| Maximum Multiplier | 1.5x | Fast page traversal |
| Progression Factor | ~1.5-2x | Smooth multiplier increase between zones |

<!-- section_id: "12dfec99-afbb-42b2-9fe6-5cacc9633a52" -->
## Differences from Cursor Configuration

| Aspect | Cursor | Scroll | Reason |
|--------|--------|--------|--------|
| Zones | 7 | 11 | Scrolling needs smoother transitions |
| Min Speed | 0.0001x | 0.1x | Scrolling needs effectiveness over precision |
| Max Speed | 0.1x | 1.5x | Scrolling benefits from higher top speed |
| Progression | ~3x | ~1.5-2x | Smaller jumps feel better for scrolling |
| Purpose | Precision placement | Smooth page navigation | Different use cases |

<!-- section_id: "748201e1-c5cc-4aeb-80df-4e7ed97d038b" -->
## Adjustment Guidelines

<!-- section_id: "4ece5af2-e7d7-4f1a-9144-260344343a5e" -->
### To make slow scrolling more effective
```bash
# Increase minimum zone values
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.15 0.15 0.2 0.2 0.3 0.3 0.4 0.4 0.55 0.55 0.7 0.7 0.85 0.85 0.95 0.95 1.05 1.05 1.25 1.25 1.5
```

<!-- section_id: "3ddd84ce-670c-4c1e-868d-64e3d63c9f65" -->
### To slow down baseline scrolling
```bash
# Increase pixel distance
xinput set-prop <TRACKPAD_ID> "libinput Scrolling Pixel Distance" 50
```

<!-- section_id: "7ee0baad-8fd7-4d0c-84da-7b6907fdf217" -->
### To speed up fast scrolling
```bash
# Increase maximum zone value
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 2.0
```

<!-- section_id: "252e4375-e99d-4a6c-a242-c68f767a72cb" -->
### To make transitions even smoother
```bash
# Add more zones with smaller jumps (example with 15 zones)
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.12 0.12 0.15 0.15 0.2 0.2 0.25 0.25 0.3 0.3 0.4 0.4 0.5 0.5 0.6 0.6 0.7 0.7 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
```

<!-- section_id: "2f0eb1b2-072b-44a3-9936-fb6fa563b1ac" -->
### To require faster physical movement for zone transitions
```bash
# Increase step size
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Step" 0.1
```

<!-- section_id: "6076a7dc-ce2d-499e-87ba-2291c34a9ef2" -->
## Troubleshooting

<!-- section_id: "ab9ba45c-e5cf-4bc9-b632-2c5632a85799" -->
### Slow scrolling doesn't move the page enough
- Increase minimum zone multipliers (0.1 → 0.15 or 0.2)
- Decrease pixel distance (40 → 35 or 30)

<!-- section_id: "25e9096c-70f0-4aee-8d29-b81eadcaa07d" -->
### Fast scrolling is too aggressive
- Decrease maximum zone multiplier (1.5 → 1.2 or 1.0)
- Increase step size to make fast zones harder to reach

<!-- section_id: "db07e872-0ee0-488a-b3e3-ab8d236dc56a" -->
### Scrolling feels jumpy
- Add more zones for smoother transitions
- Reduce progression factor (make smaller jumps between zones)
- Decrease step size for more gradual zone changes

<!-- section_id: "2ebd2274-ffb8-4e4e-a815-92b046cf5483" -->
### Scrolling is too fast overall
- Increase pixel distance (40 → 50 or 60)
- Reduce all multipliers proportionally

<!-- section_id: "e3abbade-e284-47db-baa3-fab3d4791ffd" -->
## Related Documentation
- [Cursor Configuration](../cursor/configuration.md)
- [Full Trackpad Setup Guide](/home/dawson/code/setup-hub/docs/ubuntu-trackpad-advanced-config.md)
