---
resource_id: "782679fa-57ac-4817-b865-b465ec8f9234"
resource_type: "document"
resource_name: "setup-hub-README.sync-conflict-20260126-035815-IF2WOGZ"
---
# setup-hub

Guides for standing up consistent environments quickly.

<!-- section_id: "5406174b-7245-4153-bf34-26792fc491d1" -->
## Codex on Windows VS Code

- [Codex on Windows + VS Code](docs/codex-windows-vscode.md) — WSL-based workflow tailored for Codex CLI.
- [Codex VS Code Manual Tasks](docs/codex-vscode-manual-tests.md) — checklist of UI steps and verification actions.

<!-- section_id: "dcdb2544-9fd3-4443-91ad-61d30b7860ff" -->
### Automation

- `scripts/check-codex-setup.sh` — end-to-end health check for Developer Mode, WSL, Node + Codex, and the VS Code Remote WSL extension.

<!-- section_id: "f51c2b9b-3e9e-4f15-96a4-afde9f4508ac" -->
## Ubuntu Linux Setup

- [Ubuntu Linux Setup](docs/ubuntu-linux-setup.md) — Complete guide for setting up native Ubuntu Linux development environment (dual-boot), including Chrome, Antigravity IDE, and essential tools.
- [Ubuntu Speech Tools (STT & TTS)](docs/ubuntu-speech-tools-stt-tts.md) — Complete guide for setting up local, offline Speech-to-Text (Whisper, Vosk) and Text-to-Speech (Piper, eSpeak NG) with GPU acceleration and Claude Code integration.
- [Ubuntu Trackpad Advanced Configuration](docs/ubuntu-trackpad-advanced-config.md) — Comprehensive guide for configuring custom trackpad acceleration curves with libinput, including detailed iteration process and lessons learned.
- [Ubuntu Antigravity Setup](docs/ubuntu-antigravity-setup.md) — Complete guide for installing Google Antigravity IDE on native Ubuntu Linux systems with Chrome integration and authentication setup.
- [WSL2 Antigravity Setup](docs/wsl2-antigravity-setup.md) — Step-by-step guide for installing Google Antigravity IDE on Windows Subsystem for Linux 2 (WSL2) with Chrome integration.

<!-- section_id: "866b9e44-7685-41fa-b642-148229e1b5c8" -->
### Speech Tools Automation

- `scripts/install-speech-tools.sh` — Automated installation of Speech-to-Text and Text-to-Speech tools for Ubuntu (requires manual script creation, see documentation).

<!-- section_id: "4a5f2fa7-e6a1-4568-ba82-906248e56765" -->
## How to Contribute

1. Add new setup guides under `docs/` (one scenario per file).
2. Link the new guide from this README with a short description.
3. Keep instructions actionable and verify command snippets.
