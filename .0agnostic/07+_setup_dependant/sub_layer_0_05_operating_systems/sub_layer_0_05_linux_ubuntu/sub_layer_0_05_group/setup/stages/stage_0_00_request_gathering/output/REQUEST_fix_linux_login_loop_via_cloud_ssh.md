---
resource_id: "bc3d27a2-8541-4839-9863-6b4bda7e3cda"
resource_type: "document"
resource_name: "REQUEST_fix_linux_login_loop_via_cloud_ssh"
---
# Request: Fix Linux Login Loop via Cloud Server SSH

**Layer**: 0 (Universal)
**Stage**: 0.00 Request Gathering
**Created**: 2026-01-17
**Status**: In Progress (Phase 2)

---

<!-- section_id: "143a6254-8654-47aa-9da5-ff7a96df60f0" -->
## Request Summary

Fix a Linux Ubuntu login loop by using a cloud server as an intermediary. The user cannot log into the Linux desktop environment but the system is running. The cloud server will SSH into the Linux machine to run fix commands.

---

<!-- section_id: "cb84e7ed-fff1-48f1-9100-7ac2b5a60479" -->
## Problem Statement

- Linux Ubuntu dual-boot system has a login loop
- User enters credentials at graphical login, screen flashes and returns to login
- Cannot access the desktop environment
- SSH service should still be running
- Need to fix remotely via cloud server

---

<!-- section_id: "e0272030-555e-4bd7-948d-be7e2a0f07ac" -->
## User Context

- **Environment**: Dual-boot Windows/Linux Ubuntu
- **Access Method**: Phone → Cloud Server → SSH → Linux machine
- **Syncthing**: Files sync between Windows, Linux, and Cloud Server via `dawson-workspace`
- **AI CLI Need**: Need Gemini CLI, Claude Code CLI, and Codex CLI on cloud server to get AI assistance while fixing

---

<!-- section_id: "f07ee351-9701-4145-8838-957b065b44f3" -->
## Requirements

<!-- section_id: "a625ac72-17fa-48fb-a7e7-69558b1f70eb" -->
### Functional Requirements
1. Set up AI CLI tools on cloud server (Gemini, Claude Code, Codex)
2. SSH from cloud server into Linux machine
3. Diagnose login loop cause
4. Apply fix commands
5. Verify fix by rebooting

<!-- section_id: "83c82afd-40d6-47a2-9fbf-bcd8eb7a61d6" -->
### Non-Functional Requirements
- Must be executable from phone (simple commands)
- Scripts must be in synced folder for accessibility
- Should handle common login loop causes automatically

---

<!-- section_id: "5d98a4f4-e004-4efc-bb56-5dff393b8750" -->
## API Keys Available

| CLI Tool | API Key Status |
|----------|----------------|
| Gemini CLI | ✅ Available: `AIzaSyCoGDYmISEIK4PI-mQno4EhShL0Jp6RY2I` |
| Claude Code CLI | ⚠️ Needs browser auth or ANTHROPIC_API_KEY |
| Codex CLI | ⚠️ Needs OPENAI_API_KEY |

---

<!-- section_id: "1c90396a-ab97-4b53-b1cc-58dbf67a684f" -->
## Acceptance Criteria

- [x] AI CLI tools installed on cloud server (Gemini, Claude Code, Codex)
- [ ] Can SSH from cloud server to Linux machine (waiting for Linux boot)
- [ ] Login loop fixed
- [ ] Linux desktop environment accessible

---

<!-- section_id: "6d28bd5f-24d0-4106-80c2-0d523c82c787" -->
## Progress Log

| Date | Phase | Update |
|------|-------|--------|
| 2026-01-17 | Phase 1 | VPS AI CLI setup complete (all 3 tools working) |
| 2026-01-17 | Phase 1 | Phone-friendly aliases and menu created |
| 2026-01-17 | Phase 2 | Termius installed on Windows |
| 2026-01-17 | Phase 2 | Termius iPhone link provided |

See `stage_0_03_execution/PROGRESS_*.md` for detailed status.
