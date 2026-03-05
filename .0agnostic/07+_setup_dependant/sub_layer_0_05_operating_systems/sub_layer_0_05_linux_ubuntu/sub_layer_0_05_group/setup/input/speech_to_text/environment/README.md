---
resource_id: "a760a1bc-739a-4eff-8ac2-f637450a0916"
resource_type: "readme
document"
resource_name: "README"
---
# Environment Considerations for Speech-to-Text

**Last Updated**: January 12, 2026

<!-- section_id: "53ee8cb8-698b-4b4c-ac1d-7ec87d1115f6" -->
## Overview

Speech-to-text tools on Linux behave differently depending on your display server and desktop environment. This directory covers compatibility and configuration for different setups.

<!-- section_id: "ebad3a46-b84c-4391-942e-b2d76b9e01f1" -->
## Contents

| Topic | Description | Doc |
|-------|-------------|-----|
| Wayland vs X11 | Display server differences and compatibility | [wayland_vs_x11.md](wayland_vs_x11.md) |
| Desktop Environments | DE-specific notes and compatibility | [desktop_environments.md](desktop_environments.md) |

<!-- section_id: "4d996972-e3b7-4738-91ed-8150adacc9eb" -->
## Quick Reference

<!-- section_id: "2c27165e-3147-4acf-998d-41496fe6bcd2" -->
### Check Your Display Server
```bash
echo $XDG_SESSION_TYPE
```
- `wayland` → See [wayland_vs_x11.md](wayland_vs_x11.md)
- `x11` → See [wayland_vs_x11.md](wayland_vs_x11.md)

<!-- section_id: "ea113396-3132-4b42-a240-139d4c305265" -->
### Check Your Desktop Environment
```bash
echo $XDG_CURRENT_DESKTOP
```
- `GNOME` → See [desktop_environments.md](desktop_environments.md)
- `KDE` → See [desktop_environments.md](desktop_environments.md)
- Other → See [desktop_environments.md](desktop_environments.md)
