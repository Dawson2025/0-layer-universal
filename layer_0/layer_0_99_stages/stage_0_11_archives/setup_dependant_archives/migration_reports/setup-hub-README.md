---
resource_id: "1dd185ee-6a75-425b-8117-b688bba1664b"
resource_type: "document"
resource_name: "setup-hub-README"
---
# setup-hub

Guides for standing up consistent environments quickly.

<!-- section_id: "de1e5a73-38d3-4b15-80fd-e7bb13d9112b" -->
## Codex on Windows VS Code

- [Codex on Windows + VS Code](docs/codex-windows-vscode.md) — WSL-based workflow tailored for Codex CLI.
- [Codex VS Code Manual Tasks](docs/codex-vscode-manual-tests.md) — checklist of UI steps and verification actions.

<!-- section_id: "e02e714f-61c8-4c5c-a51c-2ecec1668342" -->
### Automation

- `scripts/check-codex-setup.sh` — end-to-end health check for Developer Mode, WSL, Node + Codex, and the VS Code Remote WSL extension.

<!-- section_id: "32ad170e-eb27-4099-bef3-3978ed02df20" -->
## Ubuntu Linux Setup

- [Ubuntu Linux Setup](docs/ubuntu-linux-setup.md) — Complete guide for setting up native Ubuntu Linux development environment (dual-boot), including Chrome, Antigravity IDE, and essential tools.
- [Ubuntu Speech Tools (STT & TTS)](docs/ubuntu-speech-tools-stt-tts.md) — Complete guide for setting up local, offline Speech-to-Text (Whisper, Vosk) and Text-to-Speech (Piper, eSpeak NG) with GPU acceleration and Claude Code integration.
- [Ubuntu Trackpad Advanced Configuration](docs/ubuntu-trackpad-advanced-config.md) — Comprehensive guide for configuring custom trackpad acceleration curves with libinput, including detailed iteration process and lessons learned.
- [Ubuntu Antigravity Setup](docs/ubuntu-antigravity-setup.md) — Complete guide for installing Google Antigravity IDE on native Ubuntu Linux systems with Chrome integration and authentication setup.
- [WSL2 Antigravity Setup](docs/wsl2-antigravity-setup.md) — Step-by-step guide for installing Google Antigravity IDE on Windows Subsystem for Linux 2 (WSL2) with Chrome integration.

<!-- section_id: "5a232110-9da7-4265-982e-e6a8e568abe1" -->
### Speech Tools Automation

- `scripts/install-speech-tools.sh` — Automated installation of Speech-to-Text and Text-to-Speech tools for Ubuntu (requires manual script creation, see documentation).

<!-- section_id: "222b96e7-eea0-4fba-8ffa-e0a9825feb78" -->
## How to Contribute

1. Add new setup guides under `docs/` (one scenario per file).
2. Link the new guide from this README with a short description.
3. Keep instructions actionable and verify command snippets.
