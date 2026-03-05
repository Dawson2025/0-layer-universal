---
resource_id: "f8cbe544-8c7b-4981-b26c-24d763caa242"
resource_type: "document"
resource_name: "configuration"
---
# Cursor Movement Configuration

**Last Updated**: January 11, 2026
**System**: Ubuntu 24.04 GNOME
**Driver**: libinput

<!-- section_id: "1c895ea1-23f7-4680-b0ec-9e643cc27ec3" -->
## Current Configuration

<!-- section_id: "8da16eff-f538-49a8-8b73-5afc29f33613" -->
### Base Settings
```bash
# Set base speed to minimum (-1.0 to 1.0 range)
gsettings set org.gnome.desktop.peripherals.touchpad speed -1.0
xinput set-prop <TRACKPAD_ID> "libinput Accel Speed" -1.0

# Enable custom acceleration profile (0=adaptive, 1=flat, 2=custom)
xinput set-prop <TRACKPAD_ID> "libinput Accel Profile Enabled" 0, 0, 1
```

<!-- section_id: "7c9f66fb-f619-4019-bb91-513aa81c6248" -->
### Acceleration Curve (7-Zone Piecewise Function)
```bash
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Points" 0.0 0.0001 0.0001 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.1
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Step" 0.05
```

<!-- section_id: "8df744fd-fc1a-4e7e-9f16-82d82298043f" -->
## Zone Breakdown

| Zone | Velocity Range | Multiplier | Use Case |
|------|----------------|------------|----------|
| 1 | 0.00 - 0.10 | 0.0001x | Pixel-perfect precision work |
| 2 | 0.10 - 0.20 | 0.0003x | Fine adjustments |
| 3 | 0.20 - 0.30 | 0.001x | Slow deliberate movement |
| 4 | 0.30 - 0.40 | 0.003x | Medium-slow navigation |
| 5 | 0.40 - 0.50 | 0.01x | Normal navigation |
| 6 | 0.50 - 0.60 | 0.03x | Quick navigation |
| 7 | 0.60+ | 0.1x | Fast cursor movement |

<!-- section_id: "c13691ee-d4b7-42fc-bf0e-975daccdf04f" -->
## How Piecewise Acceleration Works

The curve is defined by pairs of values that create "plateaus":
```
0.0 0.0001 0.0001 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.1
    └─Zone 1─┘    └─Zone 2─┘    └─Zone 3─┘    └─Zone 4─┘   └─Zone 5─┘  └Zone 6┘  Zone 7
```

- **Repeated values** (e.g., "0.0001 0.0001") create flat zones
- **Step size (0.05)** determines velocity range per zone
- **7 zones × 0.05 step = ~0.35 velocity range** before reaching max speed

<!-- section_id: "e0f6f669-2acc-4b45-ac35-db250bc59f25" -->
## Design Rationale

<!-- section_id: "91ed0412-d9f3-4d9a-85f1-cfbcea12c39f" -->
### Why 7 Zones?
| Zone Count | Result |
|------------|--------|
| 3 zones | Too jumpy, not enough granularity |
| 5 zones | Better, but medium movements still jerky |
| 7 zones | Optimal balance of smoothness and distinct behavior |
| 10+ zones | Diminishing returns, harder to feel distinct zones |

<!-- section_id: "c8bd2e82-ad0a-4da8-8428-1444e08834a1" -->
### Why ~3x Progression?
| Progression | Result |
|-------------|--------|
| 2x jumps | Too gradual, takes forever to speed up |
| 3x jumps | Natural feeling, distinct zones |
| 10x jumps | Too aggressive, loses precision |

<!-- section_id: "663eb73b-3ef4-42ea-8de1-2606bdaab91c" -->
### Why Start at 0.0001x?
- Base speed is at minimum (-1.0)
- Need extremely slow multiplier for precision
- 0.001x was still too fast for pixel-level work
- 0.0001x provides true precision control

<!-- section_id: "0f3e6e9f-91fb-4f7b-a379-68c2f1789c48" -->
### Why Maximum 0.1x?
- Higher values (0.5x, 1.0x) felt uncontrollable
- Even with fast physical movement, cursor should stay manageable
- 0.1x is fast enough for practical use

<!-- section_id: "86bdbf81-472e-49a9-bebc-288c0c025f05" -->
### Why Step Size 0.05?
| Step Size | Result |
|-----------|--------|
| 0.002 | Zones transition in tiny velocity range, hard to control |
| 0.01 | Better, but still transitions too quickly |
| 0.05 | Wide zones, intentional transitions, requires real speed for fast zones |
| 0.1 | Too wide, hard to reach fast zones |

<!-- section_id: "02a9e263-1775-453e-8ef3-05d5dd10a8b0" -->
## Key Parameters Summary

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Base Speed | -1.0 | Minimum speed, slowest baseline |
| Profile | Custom (0, 0, 1) | Enables piecewise acceleration |
| Step Size | 0.05 | Controls zone width |
| Zones | 7 | Number of speed tiers |
| Min Multiplier | 0.0001x | Precision work |
| Max Multiplier | 0.1x | Fast but controlled |
| Progression | ~3x | Jump between zones |

<!-- section_id: "8088f866-f8a3-4ba0-9e2d-4f71bff95176" -->
## Adjustment Guide

<!-- section_id: "5a0d1199-e9f8-4985-b9c7-9806ca7773ce" -->
### Slower Precision Zone
```bash
# Change 0.0001 to 0.00005
xinput set-prop <ID> "libinput Accel Custom Motion Points" 0.0 0.00005 0.00005 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.1
```

<!-- section_id: "f1154856-f742-4d68-93a8-0e047ea381f2" -->
### Faster Maximum Speed
```bash
# Change 0.1 to 0.15
xinput set-prop <ID> "libinput Accel Custom Motion Points" 0.0 0.0001 0.0001 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.15
```

<!-- section_id: "47bbc227-4cfa-48a5-9746-027cc8e02081" -->
### Harder to Reach Fast Zones
```bash
# Increase step size from 0.05 to 0.1
xinput set-prop <ID> "libinput Accel Custom Motion Step" 0.1
```

<!-- section_id: "fae5d629-b6ca-43c3-b71f-fae1b429e736" -->
### More Gradual Transitions
```bash
# Add more zones with smaller jumps (9 zones, ~2x progression)
xinput set-prop <ID> "libinput Accel Custom Motion Points" 0.0 0.0001 0.0001 0.0002 0.0002 0.0005 0.0005 0.001 0.001 0.002 0.002 0.005 0.005 0.01 0.01 0.03 0.03 0.1
```

<!-- section_id: "3d7c7e56-29be-447a-b2f4-1a273edd4b5c" -->
## Iteration History

This configuration was reached through extensive iteration:

1. **Smooth curves (1.0x - 2.5x)**: Too fast, unpredictable
2. **Reduced multipliers (0.5x)**: Still too fast
3. **Aggressive reduction (0.1x max)**: Getting better
4. **1/10th scale (0.01x - 0.025x)**: Good baseline achieved
5. **Piecewise approach**: Much better control
6. **5 zones + step 0.002**: Transitioned too fast
7. **5 zones + step 0.05**: Better zone boundaries
8. **7 zones + ~3x progression**: **Final solution**

Key insight: **Curve shape matters more than base speed**. Even with base speed at -1.0, a poorly designed curve makes small movements too fast.

<!-- section_id: "c95bbd19-f8da-4512-80d3-bd92ced80c77" -->
## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| Small movements too fast | First zone multiplier too high | Reduce 0.0001 to 0.00005 |
| Can't do precise work | Curve starts too high | Ensure first non-zero value is 0.0001 or lower |
| Accidentally in fast zone | Step size too small | Increase step from 0.05 to 0.1 |
| Medium movements jerky | Zone jumps too aggressive | Add more zones, reduce progression to ~2x |
| Settings not applying | Wrong device ID | Check with `xinput list` |

<!-- section_id: "0a9c9a2d-ab74-4adf-92c8-5fcc45ea65b9" -->
## Related

- [Scroll Configuration](../scroll/configuration.md)
- [Main Trackpad README](../README.md)
