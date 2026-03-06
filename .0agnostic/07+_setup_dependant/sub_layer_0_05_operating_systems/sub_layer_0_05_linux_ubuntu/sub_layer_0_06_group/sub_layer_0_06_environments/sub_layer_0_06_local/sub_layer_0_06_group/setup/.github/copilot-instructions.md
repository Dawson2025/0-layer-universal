# GitHub Copilot Instructions

## Identity

entity_id: "c26536ad-4655-48f2-8517-a832d7e19b6c"

**Role**: Setup Container — Local Ubuntu Environment Setup
**Scope**: Setup, configuration, and troubleshooting for the local Ubuntu Linux desktop environment. Groups all setup-related entities and tracks system-level requirements.
**Parent**: `../../0AGNOSTIC.md` (Local Ubuntu Entity)
**Children**: `gsd_session_startup/` (GSD Session Startup Fix)

<!-- section_id: "285e0f6c-1f5b-4ca2-909b-f357be49dd7e" -->
## Triggers

Load this context when:
- User mentions: setup, configuration, troubleshooting, post-reboot issues, desktop environment problems
- Working on: System setup, daemon failures, keybinding issues, brightness issues, audio stack problems
- Entering: `setup/`

### Traversal Triggers

| Condition | Traverse To | Why |
|-----------|-------------|-----|
| gsd daemon failures, DISPLAY race condition, GDK_BACKEND mismatch on X11, brightness keys broken after reboot, Ctrl+Alt+S not working after boot | `gsd_session_startup/` | Dedicated entity for fixing systemd user env startup (DISPLAY import + backend mismatch) |
| inotify exhaustion, "Too many open files" errors | `../sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/inotify_fix.md` | Resolved fix for file watcher limits |
| Audio stack issues (PipeWire, WirePlumber, EasyEffects) | `../sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/` | Current product fixes |

<!-- section_id: "e843f1db-b0f4-4c97-8f84-f10493164db9" -->


---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
