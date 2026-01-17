# Request: Fix Linux Login Loop via Cloud Server SSH

**Layer**: 0 (Universal)
**Stage**: 0.00 Request Gathering
**Created**: 2026-01-17
**Status**: In Progress (Phase 2)

---

## Request Summary

Fix a Linux Ubuntu login loop by using a cloud server as an intermediary. The user cannot log into the Linux desktop environment but the system is running. The cloud server will SSH into the Linux machine to run fix commands.

---

## Problem Statement

- Linux Ubuntu dual-boot system has a login loop
- User enters credentials at graphical login, screen flashes and returns to login
- Cannot access the desktop environment
- SSH service should still be running
- Need to fix remotely via cloud server

---

## User Context

- **Environment**: Dual-boot Windows/Linux Ubuntu
- **Access Method**: Phone → Cloud Server → SSH → Linux machine
- **Syncthing**: Files sync between Windows, Linux, and Cloud Server via `dawson-workspace`
- **AI CLI Need**: Need Gemini CLI, Claude Code CLI, and Codex CLI on cloud server to get AI assistance while fixing

---

## Requirements

### Functional Requirements
1. Set up AI CLI tools on cloud server (Gemini, Claude Code, Codex)
2. SSH from cloud server into Linux machine
3. Diagnose login loop cause
4. Apply fix commands
5. Verify fix by rebooting

### Non-Functional Requirements
- Must be executable from phone (simple commands)
- Scripts must be in synced folder for accessibility
- Should handle common login loop causes automatically

---

## API Keys Available

| CLI Tool | API Key Status |
|----------|----------------|
| Gemini CLI | ✅ Available: `AIzaSyCoGDYmISEIK4PI-mQno4EhShL0Jp6RY2I` |
| Claude Code CLI | ⚠️ Needs browser auth or ANTHROPIC_API_KEY |
| Codex CLI | ⚠️ Needs OPENAI_API_KEY |

---

## Acceptance Criteria

- [x] AI CLI tools installed on cloud server (Gemini, Claude Code, Codex)
- [ ] Can SSH from cloud server to Linux machine (waiting for Linux boot)
- [ ] Login loop fixed
- [ ] Linux desktop environment accessible

---

## Progress Log

| Date | Phase | Update |
|------|-------|--------|
| 2026-01-17 | Phase 1 | VPS AI CLI setup complete (all 3 tools working) |
| 2026-01-17 | Phase 1 | Phone-friendly aliases and menu created |
| 2026-01-17 | Phase 2 | Termius installed on Windows |
| 2026-01-17 | Phase 2 | Termius iPhone link provided |

See `stage_0.03_execution/PROGRESS_*.md` for detailed status.
