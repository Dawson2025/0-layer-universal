---
resource_id: "b52b3b1d-983b-4f07-8602-6d95a122b7ef"
resource_type: "document"
resource_name: "configuration"
---
# Cursor Movement Configuration

**Last Updated**: December 31, 2025
**System**: Ubuntu 24.04 GNOME
**Driver**: libinput

<!-- section_id: "447e5784-ec75-407b-baff-eb6c1b3de02b" -->
## Current Configuration

<!-- section_id: "b807daa2-b8db-43f0-ba21-fce856945feb" -->
### Base Settings
```bash
# Set base speed to minimum
gsettings set org.gnome.desktop.peripherals.touchpad speed -1.0
xinput set-prop <TRACKPAD_ID> "libinput Accel Speed" -1.0

# Enable custom acceleration profile
xinput set-prop <TRACKPAD_ID> "libinput Accel Profile Enabled" 0, 0, 1
```

<!-- section_id: "bbdfd62d-feb8-492d-9fdf-60520e33ac10" -->
### Acceleration Curve (7-Zone Piecewise Function)
```bash
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Points" 0.0 0.0001 0.0001 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.1
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Step" 0.05
```

<!-- section_id: "2fba18c0-d44e-4943-bca6-42b6382ef2a2" -->
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

<!-- section_id: "05f252a9-3cd5-4895-9309-102990b3a6fe" -->
## Design Rationale

<!-- section_id: "fdfaa3f9-9926-4750-b2aa-2a775aa085d6" -->
### Why Piecewise Function?
- **Predictable behavior**: Each zone maintains consistent speed
- **Intentional transitions**: Harder to accidentally jump to fast zones
- **Precision control**: Zone 1 (0.0001x) allows pixel-perfect cursor placement

<!-- section_id: "59a0d94c-9529-4ecd-836e-7833e590faf5" -->
### Why ~3x Progression?
- 2x jumps (0.0001 → 0.0002) feel too gradual
- 10x jumps (0.001 → 0.01) feel too aggressive
- ~3x jumps (0.0001 → 0.0003 → 0.001 → 0.003) provide natural-feeling acceleration

<!-- section_id: "825a8d08-a8a1-4535-8562-531511437344" -->
### Why 7 Zones?
- Fewer zones (3-5): Too jumpy, not enough granularity
- More zones (10+): Diminishing returns, harder to feel distinct zones
- 7 zones: Optimal balance of smoothness and distinct behavior

<!-- section_id: "c4a11d59-5b96-411f-b7f4-242a2d400888" -->
### Why Step Size 0.05?
- Small step (0.002): Zones transition too quickly, hard to stay in slow zones
- Large step (0.05): Spreads zones across wide velocity range (~0.7 units total)
- Prevents accidental fast zone activation during medium movements

<!-- section_id: "8c340cf7-0ae6-447f-a02d-df00dd32b63e" -->
### Why Maximum 0.1x?
- Higher values (0.5x, 1.0x) made even fast movements feel uncontrollable
- 0.1x provides good speed for fast movements while maintaining control
- Combined with base speed -1.0, this is the optimal balance

<!-- section_id: "6c881be0-6db3-4978-a452-baefbf93d554" -->
## Key Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| Base Speed | -1.0 | Minimum speed, provides extremely slow baseline |
| Step Size | 0.05 | Controls velocity range per zone |
| Zones | 7 | Number of distinct speed tiers |
| Minimum Multiplier | 0.0001x | Precision work |
| Maximum Multiplier | 0.1x | Fast movement |
| Progression Factor | ~3x | Multiplier increase between zones |

<!-- section_id: "4f21219e-d251-4247-afb2-1c79d4e126c2" -->
## Adjustment Guidelines

<!-- section_id: "1b0adce0-9f37-45ce-9d70-f44a0fdb785f" -->
### To make slow movements even slower
```bash
# Reduce first zone values
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Points" 0.0 0.00005 0.00005 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.1
```

<!-- section_id: "3e5aea6a-306d-4e5f-aa27-e8e5912eb3e1" -->
### To make fast movements faster
```bash
# Increase last zone value
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Points" 0.0 0.0001 0.0001 0.0003 0.0003 0.001 0.001 0.003 0.003 0.01 0.01 0.03 0.03 0.15
```

<!-- section_id: "76e649cb-da81-4d51-9523-c7a9c2e3bb3f" -->
### To require faster physical movement for zone transitions
```bash
# Increase step size
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Step" 0.1
```

<!-- section_id: "64c872b4-d98f-47df-a1de-0b4929feb5cf" -->
### To make transitions smoother (more gradual)
```bash
# Decrease step size
xinput set-prop <TRACKPAD_ID> "libinput Accel Custom Motion Step" 0.03
```

<!-- section_id: "4f753e95-5126-4165-9eda-e4eb9a9c593f" -->
## Related Documentation
- [Scroll Configuration](../scroll/configuration.md)
- [Full Trackpad Setup Guide](/home/dawson/code/setup-hub/docs/ubuntu-trackpad-advanced-config.md)
