# Desktop Environment Compatibility

**Last Updated**: January 12, 2026

## Overview

Different Linux desktop environments have varying levels of support for speech-to-text tools, particularly around global hotkeys and text injection.

## Check Your Desktop Environment

```bash
echo $XDG_CURRENT_DESKTOP
```

## DE-Specific Notes

### GNOME

| Aspect | Status |
|--------|--------|
| Default on Ubuntu | Yes |
| Global hotkeys | Via Settings > Keyboard > Shortcuts |
| Wayland support | Primary target |
| Text injection | May need workarounds on Wayland |

**Tool compatibility:**
- Vibe Typer: Works across most DEs including GNOME
- Whisper-Dictation: Less tested on GNOME (KDE focus)

**Hotkey setup:**
1. Settings > Keyboard > Keyboard Shortcuts
2. Add custom shortcut
3. Assign to your dictation tool's trigger

### KDE Plasma

| Aspect | Status |
|--------|--------|
| Global hotkeys | Excellent support via KDE Shortcuts |
| Wayland support | Strong |
| Text injection | Good portal support |

**Tool compatibility:**
- Whisper-Dictation: **Optimized for KDE/Wayland**
- Vibe Typer: Should work
- Linux-Dictation-Project: Check compatibility

**Hotkey setup:**
1. System Settings > Shortcuts
2. Add custom command
3. Set global shortcut

### XFCE

| Aspect | Status |
|--------|--------|
| Display server | Typically X11 |
| Global hotkeys | Via Settings > Keyboard |
| Lightweight | Yes |

**Tool compatibility:**
- Most tools work well on X11
- Fewer Wayland complications

### Other DEs (Cinnamon, MATE, etc.)

| Aspect | General Status |
|--------|----------------|
| X11-based | Usually good compatibility |
| Wayland-based | Check individual tool support |

## Tool-DE Matrix

| Tool | GNOME | KDE | XFCE | Other |
|------|-------|-----|------|-------|
| Vibe Typer | Yes | Yes | Yes | Likely |
| Whisper-Dictation | Check | **Best** | Check | Check |
| Linux-Dictation-Project | Check | Check | Likely | Check |
| OpenWhispr | Yes | Yes | Yes | Likely |

## Common Issues by DE

### GNOME on Wayland
| Issue | Solution |
|-------|----------|
| Global hotkey not triggering | Use GNOME's built-in shortcut system |
| Text not injecting | Check if app is native Wayland or XWayland |

### KDE on Wayland
| Issue | Solution |
|-------|----------|
| Permission dialogs | Grant input permissions when prompted |
| Hotkey conflicts | Check KDE Shortcuts for conflicts |

### XFCE on X11
| Issue | Solution |
|-------|----------|
| Hotkey not working | Verify xbindkeys or XFCE keyboard settings |

## Recommendations by DE

| Desktop Environment | Recommended Tool |
|---------------------|------------------|
| GNOME (Wayland) | Vibe Typer (easiest) or test others |
| GNOME (X11) | Most tools work |
| KDE (Wayland) | Whisper-Dictation (optimized) |
| KDE (X11) | Most tools work |
| XFCE | Most tools work (X11 based) |

## Related Documentation

- [Wayland vs X11](wayland_vs_x11.md) - Display server differences
- [Platform Options](../platform_options/) - Individual tool docs
