---
resource_id: "9c374ad3-b49d-4c79-85e2-f478dd7a74e2"
resource_type: "document"
resource_name: "desktop_environments"
---
# Desktop Environment Compatibility

**Last Updated**: January 12, 2026

<!-- section_id: "4e4c76c4-c2b3-4a99-a827-b199c0614427" -->
## Overview

Different Linux desktop environments have varying levels of support for speech-to-text tools, particularly around global hotkeys and text injection.

<!-- section_id: "c25c82ac-f2d5-4ba8-9b67-af6d7613856b" -->
## Check Your Desktop Environment

```bash
echo $XDG_CURRENT_DESKTOP
```

<!-- section_id: "31dc1b8d-5e38-4b99-9766-10db4c1fd7e5" -->
## DE-Specific Notes

<!-- section_id: "4024fd51-3761-498c-806d-a2e138fff06e" -->
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

<!-- section_id: "eb2de54c-f519-4f1b-9598-c9bfa40d8a07" -->
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

<!-- section_id: "5c8a0d8a-3f8e-4306-8c5e-172af2bbf2b1" -->
### XFCE

| Aspect | Status |
|--------|--------|
| Display server | Typically X11 |
| Global hotkeys | Via Settings > Keyboard |
| Lightweight | Yes |

**Tool compatibility:**
- Most tools work well on X11
- Fewer Wayland complications

<!-- section_id: "03cbeed3-55fc-4709-ae98-1f9491e10152" -->
### Other DEs (Cinnamon, MATE, etc.)

| Aspect | General Status |
|--------|----------------|
| X11-based | Usually good compatibility |
| Wayland-based | Check individual tool support |

<!-- section_id: "f766398d-bc34-468c-bbbb-40425b1220ad" -->
## Tool-DE Matrix

| Tool | GNOME | KDE | XFCE | Other |
|------|-------|-----|------|-------|
| Vibe Typer | Yes | Yes | Yes | Likely |
| Whisper-Dictation | Check | **Best** | Check | Check |
| Linux-Dictation-Project | Check | Check | Likely | Check |
| OpenWhispr | Yes | Yes | Yes | Likely |

<!-- section_id: "815a1777-055c-4211-983b-b2efdcb3b7a6" -->
## Common Issues by DE

<!-- section_id: "99720943-ef6c-4459-9c28-802a285712fb" -->
### GNOME on Wayland
| Issue | Solution |
|-------|----------|
| Global hotkey not triggering | Use GNOME's built-in shortcut system |
| Text not injecting | Check if app is native Wayland or XWayland |

<!-- section_id: "8a45ae2c-9a40-4a70-946d-95fe9d5d00e5" -->
### KDE on Wayland
| Issue | Solution |
|-------|----------|
| Permission dialogs | Grant input permissions when prompted |
| Hotkey conflicts | Check KDE Shortcuts for conflicts |

<!-- section_id: "f16510b6-af66-428c-bb24-f018e1db5f20" -->
### XFCE on X11
| Issue | Solution |
|-------|----------|
| Hotkey not working | Verify xbindkeys or XFCE keyboard settings |

<!-- section_id: "8fa8c5e4-7b74-4947-b6ea-08461d736882" -->
## Recommendations by DE

| Desktop Environment | Recommended Tool |
|---------------------|------------------|
| GNOME (Wayland) | Vibe Typer (easiest) or test others |
| GNOME (X11) | Most tools work |
| KDE (Wayland) | Whisper-Dictation (optimized) |
| KDE (X11) | Most tools work |
| XFCE | Most tools work (X11 based) |

<!-- section_id: "b509c2cf-7461-4c03-b22a-95e488e29ad5" -->
## Related Documentation

- [Wayland vs X11](wayland_vs_x11.md) - Display server differences
- [Platform Options](../platform_options/) - Individual tool docs
