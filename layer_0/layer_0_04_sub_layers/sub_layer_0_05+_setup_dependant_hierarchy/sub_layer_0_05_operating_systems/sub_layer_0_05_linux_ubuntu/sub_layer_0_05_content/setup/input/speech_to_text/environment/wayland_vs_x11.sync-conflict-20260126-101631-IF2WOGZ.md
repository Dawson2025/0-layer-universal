# Wayland vs X11 for Speech-to-Text

**Last Updated**: January 12, 2026

## Overview

The display server you use affects how speech-to-text tools can inject text into applications. This is a critical compatibility consideration.

## Check Your Display Server

```bash
echo $XDG_SESSION_TYPE
```

| Output | Display Server |
|--------|----------------|
| `wayland` | Wayland (modern, more secure) |
| `x11` | X11/Xorg (legacy, more compatible) |

## Comparison

| Aspect | Wayland | X11 |
|--------|---------|-----|
| **Security** | Better (apps isolated) | Lower (apps can access input) |
| **Text injection** | Restricted | Full access |
| **Tool compatibility** | Some issues | Generally works |
| **Default on Ubuntu 24.04** | Yes | No (opt-in) |

## Why This Matters for Dictation

Speech-to-text tools need to **inject text** into whatever app you're focused on. This is how:

### On X11
- Tools can use `xdotool`, `xclip`, or direct X11 APIs
- Text injection works in almost any application
- Lower security barrier = easier implementation

### On Wayland
- Apps are sandboxed and can't freely access input
- Text injection requires compositor cooperation
- Some tools use workarounds (clipboard paste, portals)
- Some tools don't work at all

## Tool Compatibility

| Tool | Wayland | X11 | Notes |
|------|---------|-----|-------|
| Vibe Typer | Should work | Yes | Verify with your DE |
| Whisper-Dictation | Primary target | May work | Designed for Wayland |
| Linux-Dictation-Project | Check | Yes | May need X11 for full features |
| OpenWhispr | Check | Yes | Cross-platform, verify |

## Common Issues on Wayland

| Issue | Cause | Workaround |
|-------|-------|------------|
| Text not appearing | Input injection blocked | Use clipboard-based paste |
| Hotkeys not working | Global hotkey restrictions | Configure via DE settings |
| Works in some apps only | Per-app Wayland support | Use XWayland apps |

## Switching Display Servers

### To X11 (for better compatibility)
1. Log out
2. On login screen, click your username
3. Click the **gear icon** (bottom right)
4. Select **"Ubuntu on Xorg"**
5. Log in

### To Wayland (default, more secure)
1. Log out
2. On login screen, click your username
3. Click the **gear icon** (bottom right)
4. Select **"Ubuntu"** (without Xorg)
5. Log in

## Recommendations

| Your Situation | Recommendation |
|----------------|----------------|
| Dictation tools not working | Try X11 session |
| Security is priority | Stay on Wayland, use compatible tools |
| Using KDE | Whisper-Dictation designed for KDE/Wayland |
| Need it to "just work" | X11 has fewer surprises |

## XWayland Fallback

Some tools can work on Wayland through XWayland (X11 compatibility layer):
- Apps running in XWayland mode may accept text injection
- Native Wayland apps may not
- Check if your target apps run in XWayland: `xlsclients`

## Related Documentation

- [Desktop Environments](desktop_environments.md) - DE-specific compatibility
- [Trackpad: Wayland Config](../../trackpad/wayland/) - Input differences on Wayland
