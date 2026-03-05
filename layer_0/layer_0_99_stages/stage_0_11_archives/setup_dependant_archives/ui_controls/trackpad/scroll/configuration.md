---
resource_id: "5a216a61-cd59-4312-811c-05ea45b8bbb7"
resource_type: "document"
resource_name: "configuration"
---
# Scroll Configuration

**Last Updated**: December 31, 2025
**System**: Ubuntu 24.04 GNOME
**Driver**: libinput

<!-- section_id: "4fa886f3-b4d4-44fa-8592-f2a351b66121" -->
## Current Configuration

<!-- section_id: "2257626e-e5ee-4113-a307-30bb592bc2e3" -->
### Base Settings
```bash
# Set scrolling pixel distance (higher = slower baseline)
xinput set-prop <TRACKPAD_ID> "libinput Scrolling Pixel Distance" 40

# Enable custom acceleration profile (same as cursor)
xinput set-prop <TRACKPAD_ID> "libinput Accel Profile Enabled" 0, 0, 1
```

<!-- section_id: "77969500-a935-43f5-9bf4-20fe95aaf8fd" -->
### Acceleration Curve (11-Zone Piecewise Function)
```bash
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Step" 0.05
```

<!-- section_id: "192f2f8f-c321-48b7-8bb0-a13af834518d" -->
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

<!-- section_id: "f2a2bcba-dcf3-4ad6-a185-0fb0db792a90" -->
## Design Rationale

<!-- section_id: "058b08e5-918c-4c95-80ba-1abed029ed1b" -->
### Why 11 Zones (vs Cursor's 7)?
- **Smoother transitions**: More zones = smaller jumps between speeds
- **Better feel**: Scrolling benefits from very smooth acceleration
- **Wider range**: 11 zones span 0.1x to 1.5x with gradual steps

<!-- section_id: "13c707ae-60bb-4d18-a69c-df93d8f17f6c" -->
### Why ~1.5-2x Progression (vs Cursor's ~3x)?
- Cursor needs distinct precision zones, scrolling needs smoothness
- Smaller jumps (0.1 → 0.15 → 0.25) feel more natural for scrolling
- Less jarring when transitioning between scroll speeds

<!-- section_id: "5745d12a-a9f5-4003-af7d-b8fe6b35b74f" -->
### Why Start at 0.1x (vs Cursor's 0.0001x)?
- Scrolling doesn't need extreme precision like cursor placement
- 0.1x minimum ensures slow scrolling still moves the page effectively
- Starting too low (0.01x) made slow scrolling feel ineffective

<!-- section_id: "3b00a3cf-2cd2-4017-a26a-eb85ca3da799" -->
### Why Maximum 1.5x (vs Cursor's 0.1x)?
- Scrolling benefits from faster maximum speed
- 1.5x allows quick page traversal when flicking
- Combined with pixel distance 40, this provides good control

<!-- section_id: "cef7a9f5-f4ba-4134-bb99-3c37ad6b16f7" -->
### Why Pixel Distance 40?
- Default is 15 (too fast for baseline scrolling)
- 40 slows down baseline scroll speed
- Combined with acceleration zones, provides controlled scrolling

<!-- section_id: "54337c51-857d-42c8-90d7-34a06cd1a229" -->
## Key Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Pixel Distance | 40 | Baseline scroll speed (higher = slower) |
| Step Size | 0.05 | Controls velocity range per zone |
| Zones | 11 | Number of distinct speed tiers |
| Minimum Multiplier | 0.1x | Effective slow scrolling |
| Maximum Multiplier | 1.5x | Fast page traversal |
| Progression Factor | ~1.5-2x | Smooth multiplier increase between zones |

<!-- section_id: "ef02da74-dabc-4e09-abc5-189c4c3bc42f" -->
## Differences from Cursor Configuration

| Aspect | Cursor | Scroll | Reason |
|--------|--------|--------|--------|
| Zones | 7 | 11 | Scrolling needs smoother transitions |
| Min Speed | 0.0001x | 0.1x | Scrolling needs effectiveness over precision |
| Max Speed | 0.1x | 1.5x | Scrolling benefits from higher top speed |
| Progression | ~3x | ~1.5-2x | Smaller jumps feel better for scrolling |
| Purpose | Precision placement | Smooth page navigation | Different use cases |

<!-- section_id: "b4875f64-c73e-427b-bb7e-66aaa933d387" -->
## Adjustment Guidelines

<!-- section_id: "41e681f4-989b-4504-96d5-2fe5a2523706" -->
### To make slow scrolling more effective
```bash
# Increase minimum zone values
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.15 0.15 0.2 0.2 0.3 0.3 0.4 0.4 0.55 0.55 0.7 0.7 0.85 0.85 0.95 0.95 1.05 1.05 1.25 1.25 1.5
```

<!-- section_id: "62fc83d0-eb92-44a4-9b69-860b8bb53b8b" -->
### To slow down baseline scrolling
```bash
# Increase pixel distance
xinput set-prop <TRACKPAD_ID> "libinput Scrolling Pixel Distance" 50
```

<!-- section_id: "3fbb9748-f3d4-4dd4-aeba-99999ca173ad" -->
### To speed up fast scrolling
```bash
# Increase maximum zone value
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.15 0.15 0.25 0.25 0.35 0.35 0.5 0.5 0.65 0.65 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 2.0
```

<!-- section_id: "acd46758-dd58-46da-b0b4-b6bdd78e808b" -->
### To make transitions even smoother
```bash
# Add more zones with smaller jumps (example with 15 zones)
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Points" 0.0 0.1 0.1 0.12 0.12 0.15 0.15 0.2 0.2 0.25 0.25 0.3 0.3 0.4 0.4 0.5 0.5 0.6 0.6 0.7 0.7 0.8 0.8 0.9 0.9 1.0 1.0 1.2 1.2 1.5
```

<!-- section_id: "08093f18-fad3-4bdb-9650-b7ede9aaf2bc" -->
### To require faster physical movement for zone transitions
```bash
# Increase step size
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Scroll Step" 0.1
```

<!-- section_id: "c9bf7f19-bd91-4794-8089-d96f2109c9da" -->
## Troubleshooting

<!-- section_id: "254f7eb5-3bfe-499b-b883-ccb588c92761" -->
### Slow scrolling doesn't move the page enough
- Increase minimum zone multipliers (0.1 → 0.15 or 0.2)
- Decrease pixel distance (40 → 35 or 30)

<!-- section_id: "982f982c-f8ab-49d8-885f-ac21711a6809" -->
### Fast scrolling is too aggressive
- Decrease maximum zone multiplier (1.5 → 1.2 or 1.0)
- Increase step size to make fast zones harder to reach

<!-- section_id: "2c75a1fe-38f5-46cb-8459-d4817931b401" -->
### Scrolling feels jumpy
- Add more zones for smoother transitions
- Reduce progression factor (make smaller jumps between zones)
- Decrease step size for more gradual zone changes

<!-- section_id: "654d4da9-d8b3-4251-832d-e97d6ba738de" -->
### Scrolling is too fast overall
- Increase pixel distance (40 → 50 or 60)
- Reduce all multipliers proportionally

<!-- section_id: "964c4add-2a37-4a85-a612-f7fca1aabc58" -->
## Related Documentation
- [Cursor Configuration](../cursor/configuration.md)
- [Full Trackpad Setup Guide](/home/dawson/code/setup-hub/docs/ubuntu-trackpad-advanced-config.md)
