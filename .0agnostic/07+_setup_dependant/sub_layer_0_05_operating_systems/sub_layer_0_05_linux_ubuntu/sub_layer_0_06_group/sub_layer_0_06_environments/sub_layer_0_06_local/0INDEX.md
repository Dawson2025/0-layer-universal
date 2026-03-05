---
resource_id: "04a8100a-f981-4006-bd42-c8e77057b19a"
resource_type: "index
document"
resource_name: "0INDEX"
---
# Local Ubuntu Environment — Navigation Index

<!-- section_id: "b5d20a84-8640-4b84-bb49-08e9cd3b9db0" -->
## Entity Overview

Local Ubuntu desktop environment setup and maintenance. Manages GNOME/Unity desktop, system services, audio stack, and TTS configuration.

<!-- section_id: "5595dcf9-6dd2-41f2-b8db-da76915b4b94" -->
## Quick Navigation

| What | Where |
|------|-------|
| **Entity context** | `0AGNOSTIC.md` |
| **Knowledge topics** | `.0agnostic/01_knowledge/` |
| **Setup stages** | `sub_layer_0_06_group/sub_layer_0_06_99_stages/` |
| **Setup instructions** | `sub_layer_0_06_group/setup/0_instruction_docs/` |
| **Coding Apps (child)** | `sub_layer_0_07_group/sub_layer_0_07_coding_apps/` |

<!-- section_id: "3e36e3c2-239c-424b-bc5f-bf68a505a0dc" -->
## Knowledge Topics

| Topic | Key Docs |
|-------|----------|
| Linux Fundamentals | `inotify.md` — inotify limits, exhaustion symptoms |
| Ubuntu Desktop | `gnome_architecture.md` — GNOME Shell, GSD daemons, portals |
| System Services | `systemd_user_services.md` — systemctl --user, overrides |
| Audio | `linux_audio_stack.md` — PipeWire, ALSA, SOF, EasyEffects |

<!-- section_id: "c6fe7de4-8d16-44eb-aa0a-30900793f49e" -->
## Stage Progress

Stages track setup work (audio enhancement, speaker tuning, GSD fixes, portal fixes):

| Stage | Content |
|-------|---------|
| 00 Request Gathering | REQ_001-006: audio, speakers, vibe-typer, portals, brightness/volume |
| 01 Research | Audio improvement research, Yoga speaker I2C, diagnostics |
| 03 Planning | (empty) |
| 04 Design | (empty) |
| 05 Development | Audio implementation, Yoga speaker, Dolby impulse capture |
| 06 Testing | Audio testing, GSD display testing, portal testing |
| 07 Criticism | GSD display, portal apps criticism |
| 08 Fixing | Audio fixes, Yoga speaker fixes, GSD display fix, portal fix |
| 09 Current Product | Audio config, Yoga speaker config, GSD keepalive, EasyEffects, WirePlumber crash fix, inotify fix, sync health, portal config |
| 10 Archives | (empty) |

<!-- section_id: "7c4d4c13-50f6-4d63-b185-31b67ab380ed" -->
## Children

| Child | Purpose |
|-------|---------|
| Coding Apps (0.07) | Cursor IDE and future coding tools on this local environment |
