---
resource_id: "0e594ffb-6865-4212-b768-9aca1ab0131b"
resource_type: "document"
resource_name: "use_cases"
---
# Use Case Recommendations

**Last Updated**: January 12, 2026

<!-- section_id: "331841d3-731e-4bc6-8568-366930b2c360" -->
## By Activity

<!-- section_id: "832099fc-2092-4bce-81ba-79e1b01f0733" -->
### Coding / Development

| Priority | Tool | Why |
|----------|------|-----|
| Quick dictation in IDE | [Vibe Typer](../platform_options/vibe_typer.md) | Fast, works everywhere |
| Privacy-conscious dev | [Whisper-Dictation](../platform_options/whisper_dictation.md) | Code stays local |
| Hands-free coding | [Linux-Dictation-Project](../platform_options/linux_dictation_project.md) | Voice commands for navigation |

<!-- section_id: "bf66e5fd-edb5-489f-9e98-f62718372a27" -->
### Writing / Documentation

| Priority | Tool | Why |
|----------|------|-----|
| Long-form writing | [Vibe Typer](../platform_options/vibe_typer.md) | AI rewrite tools helpful |
| Private journals/notes | [Whisper-Dictation](../platform_options/whisper_dictation.md) | Content never leaves machine |
| Auto-formatting needs | [BlabbyAI](../platform_options/blabby_ai.md) (upcoming) | Auto punctuation/capitalization |

<!-- section_id: "d540f550-185a-4d52-85a5-05e050eb9130" -->
### Communication (Email, Chat, Slack)

| Priority | Tool | Why |
|----------|------|-----|
| Quick replies | [Vibe Typer](../platform_options/vibe_typer.md) | AI reply generation |
| Privacy-focused | [OpenWhispr](../platform_options/openwhispr.md) | Balance of ease and privacy |

<!-- section_id: "740384df-38d6-4a82-b4f9-49e0740e9575" -->
### Accessibility / RSI Prevention

| Priority | Tool | Why |
|----------|------|-----|
| Full keyboard replacement | [Linux-Dictation-Project](../platform_options/linux_dictation_project.md) | Voice commands for everything |
| Basic dictation | [Vibe Typer](../platform_options/vibe_typer.md) | Lowest friction |

<!-- section_id: "9b83df12-7fb4-4045-ad6e-ad5b81d0c0a6" -->
## By Environment

<!-- section_id: "1735d076-99dd-41ba-9007-f8de3cd37ce6" -->
### GNOME Desktop

| Situation | Tool |
|-----------|------|
| Just want it to work | [Vibe Typer](../platform_options/vibe_typer.md) |
| Open source preference | [OpenWhispr](../platform_options/openwhispr.md) |
| Wayland + privacy | [Whisper-Dictation](../platform_options/whisper_dictation.md) (may need testing) |

<!-- section_id: "609b89d1-1056-400b-a8e4-bcc90fb3bedd" -->
### KDE Plasma

| Situation | Tool |
|-----------|------|
| Wayland session | [Whisper-Dictation](../platform_options/whisper_dictation.md) (optimized) |
| X11 session | Most tools work |
| Voice commands | [Linux-Dictation-Project](../platform_options/linux_dictation_project.md) |

<!-- section_id: "575a33a9-f718-4265-ae76-d00b5c8d040d" -->
### XFCE / Lightweight DEs

| Situation | Tool |
|-----------|------|
| X11 (typical) | Most tools work well |
| Low resources | [Vibe Typer](../platform_options/vibe_typer.md) (cloud = less local CPU) |
| Local processing | Smaller Whisper model |

<!-- section_id: "126bdd02-4123-47d3-beba-4a5b4f17778b" -->
## By Constraint

<!-- section_id: "27ee8553-8c08-438e-8126-c97e2a4c7359" -->
### Air-Gapped / No Internet

| Situation | Tool |
|-----------|------|
| Must work offline | [Whisper-Dictation](../platform_options/whisper_dictation.md) or [Linux-Dictation-Project](../platform_options/linux_dictation_project.md) |
| Setup requires internet | Download models first, then go offline |

<!-- section_id: "4dd73394-d195-409e-9554-b05326dc2dd5" -->
### Limited Hardware

| Situation | Tool |
|-----------|------|
| Low RAM (<4GB) | [Vibe Typer](../platform_options/vibe_typer.md) (cloud processing) |
| No GPU | [Vibe Typer](../platform_options/vibe_typer.md) or small Whisper model |
| Powerful machine | [Whisper-Dictation](../platform_options/whisper_dictation.md) with large model |

<!-- section_id: "1b3aa668-a006-42a2-85a8-271f8f630a96" -->
### Corporate / Enterprise

| Situation | Tool |
|-----------|------|
| Data must stay local | [Whisper-Dictation](../platform_options/whisper_dictation.md) |
| Need audit trail | Open source options |
| Custom integration | [Cloud APIs](../platform_options/cloud_apis.md) |

<!-- section_id: "94ea50df-f190-459b-b436-892a1204ffb9" -->
## By Experience Level

<!-- section_id: "a538d498-b632-409d-9364-4c842beb39b9" -->
### Beginner

| Preference | Tool |
|------------|------|
| Just want dictation | [Vibe Typer](../platform_options/vibe_typer.md) |
| Want open source | [OpenWhispr](../platform_options/openwhispr.md) |

<!-- section_id: "5aed6f70-cf86-41b2-b434-152fc729afc7" -->
### Intermediate

| Preference | Tool |
|------------|------|
| Local processing | [Whisper-Dictation](../platform_options/whisper_dictation.md) |
| Customization | Any open source option |

<!-- section_id: "02d59c06-d71c-404c-a499-620470f2041c" -->
### Advanced

| Preference | Tool |
|------------|------|
| Full control | [Linux-Dictation-Project](../platform_options/linux_dictation_project.md) |
| Custom scripts | [Whisper-Dictation](../platform_options/whisper_dictation.md) |
| Build own solution | [Cloud APIs](../platform_options/cloud_apis.md) |

<!-- section_id: "c1dbfde0-8ccd-4d92-b0d2-76f5f1f4956d" -->
## Migration Paths

<!-- section_id: "5838c6de-e6e5-465e-a69a-ab876cf263cd" -->
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

<!-- section_id: "c0d22698-564c-4f30-aec5-6d8f75d894ff" -->
### Starting with Requirements

```
Privacy Required → Whisper-Dictation → Add voice commands? → Linux-Dictation-Project
Open Source Required → OpenWhispr or Whisper-Dictation
Cross-platform Required → OpenWhispr
```

<!-- section_id: "3eab4bfe-5536-4bd8-9a7d-8bc5241b359b" -->
## Related

- [Quick Decision Guide](quick_decision.md) - Priority-based recommendations
- [Comparison Matrix](comparison_matrix.md) - Full feature comparison
- [Platform Options](../platform_options/) - Detailed docs for each tool
