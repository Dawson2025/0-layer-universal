# Environment Considerations for Speech-to-Text

**Last Updated**: January 12, 2026

## Overview

Speech-to-text tools on Linux behave differently depending on your display server and desktop environment. This directory covers compatibility and configuration for different setups.

## Contents

| Topic | Description | Doc |
|-------|-------------|-----|
| Wayland vs X11 | Display server differences and compatibility | [wayland_vs_x11.md](wayland_vs_x11.md) |
| Desktop Environments | DE-specific notes and compatibility | [desktop_environments.md](desktop_environments.md) |

## Quick Reference

### Check Your Display Server
```bash
echo $XDG_SESSION_TYPE
```
- `wayland` → See [wayland_vs_x11.md](wayland_vs_x11.md)
- `x11` → See [wayland_vs_x11.md](wayland_vs_x11.md)

### Check Your Desktop Environment
```bash
echo $XDG_CURRENT_DESKTOP
```
- `GNOME` → See [desktop_environments.md](desktop_environments.md)
- `KDE` → See [desktop_environments.md](desktop_environments.md)
- Other → See [desktop_environments.md](desktop_environments.md)
