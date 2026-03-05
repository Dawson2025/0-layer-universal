---
resource_id: "6ea3cb00-a671-4f55-82f9-5d4a6e98b2a7"
resource_type: "readme
document"
resource_name: "README"
---
# Local Environment Setup - Ubuntu Linux

**Purpose**: Setup, configuration, and troubleshooting for the local Ubuntu Linux environment.

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

## Knowledge Layers (subx2_layers)

Traverse from universal → specific:

| Layer | Content | When to Read |
|-------|---------|--------------|
| `sub_layer_01_linux_fundamentals` | Core Linux concepts (inotify, kernel) | Understanding root causes |
| `sub_layer_02_ubuntu_desktop` | GNOME, desktop services | Desktop-specific issues |
| `sub_layer_03_system_services` | Systemd, service management | Service troubleshooting |

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

## Current Issues

See `sub_layer_0_06_99_stages/status.json` for tracked issues.

### Resolved
- **Inotify Exhaustion** (2026-01-25): Volume keys, brightness keys, app launching fixed
  - Fix: `sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/inotify_fix.md`

## Quick Reference

### Check System Health
```bash
systemctl --user is-system-running
systemctl --user --failed
```

### Common Fixes
- [Inotify Limits](sub_layer_0_06_99_stages/stage_0_09_current_product/outputs/inotify_fix.md)
