# AutoGen Agent Context

---
resource_id: "06514dfc-47ce-4cea-864e-d123c820f0c3"
resource_type: "agnostic_document"
resource_name: "setup_root"
---
# Setup Container — Agnostic Identity

<!-- section_id: "8aebfa7e-ec56-4c3b-a1e5-65176c52d559" -->
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
## Pointers

### On Entry
1. Read `0INDEX.md` or `README.md` for current state
2. Check `requirements_tree.md` for the tree of needs
3. Check children for active work

### Navigation
| Direction | Path |
|-----------|------|
| Parent | `../../0AGNOSTIC.md` (Local Ubuntu Entity) |
| Child: GSD Session Startup | `gsd_session_startup/0AGNOSTIC.md` |
| Requirements Tree | `requirements_tree.md` |
| Current Products | `../sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/` |
| Knowledge | `../../.0agnostic/01_knowledge/` (ubuntu_desktop, audio, system_services, linux_fundamentals) |
| README (legacy) | `README.md` |

<!-- section_id: "6d59be49-aeef-45d7-9735-7b5ea376423f" -->
## Tree of Needs (Summary)

Full tree: `requirements_tree.md`

| Need | Description | Status | Detailed In |
|------|-------------|--------|-------------|
| N1: Desktop Services | gsd-media-keys and gsd-power must run reliably | Implemented (pre-reboot verified), reboot validation pending | `gsd_session_startup/stages/stage_10_current_product/outputs/current_fix.md` |
| N2: System Resource Limits | inotify limits, file descriptors | Resolved | `../sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/inotify_fix.md` |
| N3: Audio Stack | PipeWire, EasyEffects, WirePlumber stable | Resolved (workarounds in place) | `../sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/` |
| N4: Display Server Availability | DISPLAY/XAUTHORITY available in systemd user env before services and correct GDK backend for X11 session | Implemented (pre-reboot verified), reboot validation pending | `gsd_session_startup/stages/stage_10_current_product/outputs/current_fix.md` |

<!-- section_id: "c4764996-6ea7-4f44-9d12-b25dbb310fad" -->
## Dependent Entities (Who Cares About This)

These entities depend on the local desktop setup being correct:

| Entity | Why It Depends | Location (from repo root) |
|--------|---------------|--------------------------|
| Audio (Sub-Feature) | TTS keybindings need gsd-media-keys | `layer_-1_research/.../layer_1_sub_feature_audio/` |
| Laptop Linux Ubuntu | Platform-specific TTS needs working desktop | `layer_-1_research/.../layer_2_subx2_feature_laptop_linux_ubuntu/` |
| System TTS | Ctrl+Alt+S speak-selection needs gsd-media-keys | `layer_-1_research/.../layer_3_subx3_feature_system_tts/` |

## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
