---
resource_id: "1fdf3e7b-03b1-4a73-ac5f-f9e98713e105"
resource_type: "document"
resource_name: "setup-hub-README.sync-conflict-20260126-102106-IF2WOGZ"
---
# setup-hub

Guides for standing up consistent environments quickly.

<!-- section_id: "96db2275-1592-404e-8a79-a74f51c666f4" -->
## Codex on Windows VS Code

- [Codex on Windows + VS Code](docs/codex-windows-vscode.md) — WSL-based workflow tailored for Codex CLI.
- [Codex VS Code Manual Tasks](docs/codex-vscode-manual-tests.md) — checklist of UI steps and verification actions.

<!-- section_id: "4cc00be1-0092-4a6b-bb46-81fbd3e72aaf" -->
### Automation

- `scripts/check-codex-setup.sh` — end-to-end health check for Developer Mode, WSL, Node + Codex, and the VS Code Remote WSL extension.

<!-- section_id: "0d088da4-d85a-4531-9a0c-b20869605938" -->
## Ubuntu Linux Setup

- [Ubuntu Linux Setup](docs/ubuntu-linux-setup.md) — Complete guide for setting up native Ubuntu Linux development environment (dual-boot), including Chrome, Antigravity IDE, and essential tools.
- [Ubuntu Speech Tools (STT & TTS)](docs/ubuntu-speech-tools-stt-tts.md) — Complete guide for setting up local, offline Speech-to-Text (Whisper, Vosk) and Text-to-Speech (Piper, eSpeak NG) with GPU acceleration and Claude Code integration.
- [Ubuntu Trackpad Advanced Configuration](docs/ubuntu-trackpad-advanced-config.md) — Comprehensive guide for configuring custom trackpad acceleration curves with libinput, including detailed iteration process and lessons learned.
- [Ubuntu Antigravity Setup](docs/ubuntu-antigravity-setup.md) — Complete guide for installing Google Antigravity IDE on native Ubuntu Linux systems with Chrome integration and authentication setup.
- [WSL2 Antigravity Setup](docs/wsl2-antigravity-setup.md) — Step-by-step guide for installing Google Antigravity IDE on Windows Subsystem for Linux 2 (WSL2) with Chrome integration.

<!-- section_id: "727f53b3-cba5-4734-8368-f8ce3aeafa36" -->
### Speech Tools Automation

- `scripts/install-speech-tools.sh` — Automated installation of Speech-to-Text and Text-to-Speech tools for Ubuntu (requires manual script creation, see documentation).

<!-- section_id: "a181b168-9c4c-4963-970b-5c31f711ca60" -->
## How to Contribute

1. Add new setup guides under `docs/` (one scenario per file).
2. Link the new guide from this README with a short description.
3. Keep instructions actionable and verify command snippets.
