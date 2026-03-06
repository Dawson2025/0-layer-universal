---
resource_id: "6ea3cb00-a671-4f55-82f9-5d4a6e98b2a7"
resource_type: "readme
document"
resource_name: "README"
---
# Local Environment Setup - Ubuntu Linux

**Purpose**: Setup, configuration, and troubleshooting for the local Ubuntu Linux environment.

<!-- section_id: "cc888331-86ad-4b9d-a77d-bdea8db9d58f" -->
## Structure

```
setup/
├── sub_layer_0_06_00_layer_registry/
├── sub_layer_0_06_01_ai_manager_system/
├── sub_layer_0_06_02_manager_handoff_documents/
├── sub_layer_0_06_03_subx2_layers/
│   ├── sub_layer_01_linux_fundamentals/
│   │   └── inotify.md
│   ├── sub_layer_02_ubuntu_desktop/
│   │   └── gnome_architecture.md
│   └── sub_layer_03_system_services/
│       └── systemd_user_services.md
├── sub_layer_0_06_99_stages/
│   ├── stage_0_01_request_gathering/outputs/
│   ├── stage_0_01_research/outputs/
│   ├── stage_0_02_instructions/outputs/
│   ├── stage_0_03_planning/outputs/
│   ├── stage_0_04_design/outputs/
│   ├── stage_0_05_development/outputs/
│   ├── stage_0_06_testing/outputs/
│   ├── stage_0_07_criticism/outputs/
│   ├── stage_0_08_fixing/outputs/
│   ├── stage_0_09_current_product/outputs/
│   │   └── inotify_fix.md
│   ├── stage_0_10_archives/outputs/
│   └── status.json
└── 0_instruction_docs/                   # Legacy (being migrated)
    └── github/
```

<!-- section_id: "e8550df5-912b-4dc7-93bd-b7b2d3f4c0c8" -->
## Knowledge Layers (subx2_layers)

Traverse from universal → specific:

| Layer | Content | When to Read |
|-------|---------|--------------|
| `sub_layer_01_linux_fundamentals` | Core Linux concepts (inotify, kernel) | Understanding root causes |
| `sub_layer_02_ubuntu_desktop` | GNOME, desktop services | Desktop-specific issues |
| `sub_layer_03_system_services` | Systemd, service management | Service troubleshooting |

<!-- section_id: "d12d5cc1-ef7e-4135-a602-aa97bd5149f5" -->
## Stages (Workflow)

| Stage | Purpose |
|-------|---------|
| `stage_0_01_request_gathering` | Problem reports |
| `stage_0_01_research` | Investigation |
| `stage_0_02_instructions` | Constraints/requirements |
| `stage_0_03_planning` | Solution design |
| `stage_0_04_design` | Architecture decisions |
| `stage_0_05_development` | Implementation |
| `stage_0_06_testing` | Verification |
| `stage_0_07_criticism` | Review |
| `stage_0_08_fixing` | Corrections |
| `stage_0_09_current_product` | **Active fixes** |
| `stage_0_10_archives` | Historical fixes |

<!-- section_id: "0a9370d4-32fa-4b31-b416-aa0a9b019aac" -->
## Current Issues

See `sub_layer_0_06_99_stages/status.json` for tracked issues.

<!-- section_id: "a3b4c5d6-e7f8-9012-3456-789abcdef012" -->
### Active
- **GSD Session Startup** (2026-03-06): DISPLAY race condition causes gsd-media-keys/gsd-power to fail after every reboot
  - Entity: `gsd_session_startup/` — dedicated entity with full stage hierarchy
  - Root cause: Unity doesn't import DISPLAY into systemd user env before GNOME services start
  - Current workaround: `sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/gsd_keepalive_fix.md`

<!-- section_id: "b9ebc2ec-8cc0-41f1-b9a5-12f5931f40d3" -->
### Resolved
- **Inotify Exhaustion** (2026-01-25): Volume keys, brightness keys, app launching fixed
  - Fix: `sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/inotify_fix.md`

<!-- section_id: "b4bfef3b-a8ab-485a-94bb-f5ea6e050bde" -->
## Quick Reference

<!-- section_id: "f217bd31-04b7-4c55-8253-dda6b7fe9884" -->
### Check System Health
```bash
systemctl --user is-system-running
systemctl --user --failed
```

<!-- section_id: "58d5cc55-3fb7-4cd4-9bea-135169cff45b" -->
### Common Fixes
- [Inotify Limits](sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/inotify_fix.md)
