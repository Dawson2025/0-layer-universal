---
resource_id: "0e594ffb-6865-4212-b768-9aca1ab0131b"
resource_type: "document"
resource_name: "use_cases"
---
# Use Case Recommendations

**Last Updated**: January 12, 2026

## By Activity

### Coding / Development

| Priority | Tool | Why |
|----------|------|-----|
| Quick dictation in IDE | [Vibe Typer](../platform_options/vibe_typer.md) | Fast, works everywhere |
| Privacy-conscious dev | [Whisper-Dictation](../platform_options/whisper_dictation.md) | Code stays local |
| Hands-free coding | [Linux-Dictation-Project](../platform_options/linux_dictation_project.md) | Voice commands for navigation |

### Writing / Documentation

| Priority | Tool | Why |
|----------|------|-----|
| Long-form writing | [Vibe Typer](../platform_options/vibe_typer.md) | AI rewrite tools helpful |
| Private journals/notes | [Whisper-Dictation](../platform_options/whisper_dictation.md) | Content never leaves machine |
| Auto-formatting needs | [BlabbyAI](../platform_options/blabby_ai.md) (upcoming) | Auto punctuation/capitalization |

### Communication (Email, Chat, Slack)

| Priority | Tool | Why |
|----------|------|-----|
| Quick replies | [Vibe Typer](../platform_options/vibe_typer.md) | AI reply generation |
| Privacy-focused | [OpenWhispr](../platform_options/openwhispr.md) | Balance of ease and privacy |

### Accessibility / RSI Prevention

| Priority | Tool | Why |
|----------|------|-----|
| Full keyboard replacement | [Linux-Dictation-Project](../platform_options/linux_dictation_project.md) | Voice commands for everything |
| Basic dictation | [Vibe Typer](../platform_options/vibe_typer.md) | Lowest friction |

## By Environment

### GNOME Desktop

| Situation | Tool |
|-----------|------|
| Just want it to work | [Vibe Typer](../platform_options/vibe_typer.md) |
| Open source preference | [OpenWhispr](../platform_options/openwhispr.md) |
| Wayland + privacy | [Whisper-Dictation](../platform_options/whisper_dictation.md) (may need testing) |

### KDE Plasma

| Situation | Tool |
|-----------|------|
| Wayland session | [Whisper-Dictation](../platform_options/whisper_dictation.md) (optimized) |
| X11 session | Most tools work |
| Voice commands | [Linux-Dictation-Project](../platform_options/linux_dictation_project.md) |

### XFCE / Lightweight DEs

| Situation | Tool |
|-----------|------|
| X11 (typical) | Most tools work well |
| Low resources | [Vibe Typer](../platform_options/vibe_typer.md) (cloud = less local CPU) |
| Local processing | Smaller Whisper model |

## By Constraint

### Air-Gapped / No Internet

| Situation | Tool |
|-----------|------|
| Must work offline | [Whisper-Dictation](../platform_options/whisper_dictation.md) or [Linux-Dictation-Project](../platform_options/linux_dictation_project.md) |
| Setup requires internet | Download models first, then go offline |

### Limited Hardware

| Situation | Tool |
|-----------|------|
| Low RAM (<4GB) | [Vibe Typer](../platform_options/vibe_typer.md) (cloud processing) |
| No GPU | [Vibe Typer](../platform_options/vibe_typer.md) or small Whisper model |
| Powerful machine | [Whisper-Dictation](../platform_options/whisper_dictation.md) with large model |

### Corporate / Enterprise

| Situation | Tool |
|-----------|------|
| Data must stay local | [Whisper-Dictation](../platform_options/whisper_dictation.md) |
| Need audit trail | Open source options |
| Custom integration | [Cloud APIs](../platform_options/cloud_apis.md) |

## By Experience Level

### Beginner

| Preference | Tool |
|------------|------|
| Just want dictation | [Vibe Typer](../platform_options/vibe_typer.md) |
| Want open source | [OpenWhispr](../platform_options/openwhispr.md) |

### Intermediate

| Preference | Tool |
|------------|------|
| Local processing | [Whisper-Dictation](../platform_options/whisper_dictation.md) |
| Customization | Any open source option |

### Advanced

| Preference | Tool |
|------------|------|
| Full control | [Linux-Dictation-Project](../platform_options/linux_dictation_project.md) |
| Custom scripts | [Whisper-Dictation](../platform_options/whisper_dictation.md) |
| Build own solution | [Cloud APIs](../platform_options/cloud_apis.md) |

## Migration Paths

### Starting Simple, Growing Complex

```
Vibe Typer (easy start)
    │
    ├─ Want more privacy? → OpenWhispr
    │
    └─ Want full local? → Whisper-Dictation
                              │
                              └─ Want voice commands? → Linux-Dictation-Project
```

### Starting with Requirements

```
Privacy Required → Whisper-Dictation → Add voice commands? → Linux-Dictation-Project
Open Source Required → OpenWhispr or Whisper-Dictation
Cross-platform Required → OpenWhispr
```

## Related

- [Quick Decision Guide](quick_decision.md) - Priority-based recommendations
- [Comparison Matrix](comparison_matrix.md) - Full feature comparison
- [Platform Options](../platform_options/) - Detailed docs for each tool
