---
resource_id: "664d0c5c-507b-4e27-b7b5-5ce321d1f08e"
resource_type: "document"
resource_name: "wayland_vs_x11"
---
# Wayland vs X11 for Speech-to-Text

**Last Updated**: January 12, 2026

<!-- section_id: "b3497eb8-c788-4860-85db-fb003ac6110f" -->
## Overview

The display server you use affects how speech-to-text tools can inject text into applications. This is a critical compatibility consideration.

<!-- section_id: "a327654c-c45b-48af-a3b8-477a8d46cd06" -->
## Check Your Display Server

```bash
echo $XDG_SESSION_TYPE
```

| Output | Display Server |
|--------|----------------|
| `wayland` | Wayland (modern, more secure) |
| `x11` | X11/Xorg (legacy, more compatible) |

<!-- section_id: "73ae5ea2-2092-4b5b-a04e-06a8637d37e5" -->
## Comparison

| Aspect | Wayland | X11 |
|--------|---------|-----|
| **Security** | Better (apps isolated) | Lower (apps can access input) |
| **Text injection** | Restricted | Full access |
| **Tool compatibility** | Some issues | Generally works |
| **Default on Ubuntu 24.04** | Yes | No (opt-in) |

<!-- section_id: "8e35a914-75e3-4385-b65e-55d8005e3021" -->
## Why This Matters for Dictation

Speech-to-text tools need to **inject text** into whatever app you're focused on. This is how:

<!-- section_id: "98d17948-f53a-4c81-b381-f866f122ac78" -->
### On X11
- Tools can use `xdotool`, `xclip`, or direct X11 APIs
- Text injection works in almost any application
- Lower security barrier = easier implementation

<!-- section_id: "73949758-04c6-4472-9d6b-c2013baae1d2" -->
### On Wayland
- Apps are sandboxed and can't freely access input
- Text injection requires compositor cooperation
- Some tools use workarounds (clipboard paste, portals)
- Some tools don't work at all

<!-- section_id: "6d2b7b3e-e722-46ee-bf8c-af5d914b3336" -->
## Tool Compatibility

| Tool | Wayland | X11 | Notes |
|------|---------|-----|-------|
| Vibe Typer | Should work | Yes | Verify with your DE |
| Whisper-Dictation | Primary target | May work | Designed for Wayland |
| Linux-Dictation-Project | Check | Yes | May need X11 for full features |
| OpenWhispr | Check | Yes | Cross-platform, verify |

<!-- section_id: "f92e9c66-559c-4288-a6d3-13b88a7d0288" -->
## Common Issues on Wayland

| Issue | Cause | Workaround |
|-------|-------|------------|
| Text not appearing | Input injection blocked | Use clipboard-based paste |
| Hotkeys not working | Global hotkey restrictions | Configure via DE settings |
| Works in some apps only | Per-app Wayland support | Use XWayland apps |

<!-- section_id: "ca55bbe0-1621-4f7d-be6d-bb982538add4" -->
## Switching Display Servers

<!-- section_id: "5c7c85a0-773f-42e9-9279-8c9a66b68fc7" -->
### To X11 (for better compatibility)
1. Log out
2. On login screen, click your username
3. Click the **gear icon** (bottom right)
4. Select **"Ubuntu on Xorg"**
5. Log in

<!-- section_id: "aa92ec5d-68b2-46d8-b4b9-765e5bbc9b94" -->
### To Wayland (default, more secure)
1. Log out
2. On login screen, click your username
3. Click the **gear icon** (bottom right)
4. Select **"Ubuntu"** (without Xorg)
5. Log in

<!-- section_id: "2ccebed5-b292-44bb-ab4c-5e12fca82822" -->
## Recommendations

| Your Situation | Recommendation |
|----------------|----------------|
| Dictation tools not working | Try X11 session |
| Security is priority | Stay on Wayland, use compatible tools |
| Using KDE | Whisper-Dictation designed for KDE/Wayland |
| Need it to "just work" | X11 has fewer surprises |

<!-- section_id: "190b9f9f-c6e5-4209-9c33-0841a22a86a9" -->
## XWayland Fallback

Some tools can work on Wayland through XWayland (X11 compatibility layer):
- Apps running in XWayland mode may accept text injection
- Native Wayland apps may not
- Check if your target apps run in XWayland: `xlsclients`

<!-- section_id: "a14a4439-8f78-497a-a9e2-7c69aa93d5c6" -->
## Related Documentation

- [Desktop Environments](desktop_environments.md) - DE-specific compatibility
- [Trackpad: Wayland Config](../../trackpad/wayland/) - Input differences on Wayland
