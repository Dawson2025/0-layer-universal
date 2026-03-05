---
resource_id: "5e472a46-46c4-4bf9-92d7-6b9e8add7d87"
resource_type: "document"
resource_name: "PROGRESS_fix_linux_login_loop_via_cloud_ssh"
---
# Progress: Fix Linux Login Loop via Cloud Server SSH

**Layer**: 0 (Universal)
**Stage**: 0.03 Execution
**Created**: 2026-01-17
**Last Updated**: 2026-01-17
**Status**: COMPLETED

---

<!-- section_id: "0c3122f3-45d5-4861-90bd-191847fa4353" -->
## Execution Progress

<!-- section_id: "2adac60b-879e-43c8-84f2-ed74ec2d4524" -->
### Phase 1: Cloud Server Setup
**Status**: COMPLETED

| Task | Status | Notes |
|------|--------|-------|
| Connect to Hetzner VPS | Done | IP: 46.224.184.10, User: root |
| Install Node.js 20 | Done | Required for CLI tools |
| Install Gemini CLI | Done | OAuth auth used (API key had region issues) |
| Install Claude Code CLI | Done | OAuth credentials copied from Windows |
| Install Codex CLI | Done | OAuth credentials copied from Windows |
| Create phone-friendly aliases | Done | `g`, `c`, `cx`, `menu` |
| Generate SSH key for Linux access | Done | Key in VPS_SSH_PUBLIC_KEY.txt |

**Credentials Copied to VPS**:
- `~/.gemini/oauth_creds.json`
- `~/.claude/.credentials.json`
- `~/.codex/auth.json`

---

<!-- section_id: "a30dc96e-e356-42c7-af04-eb783934850d" -->
### Phase 2: Phone Setup
**Status**: IN PROGRESS

| Task | Status | Notes |
|------|--------|-------|
| Termius Windows installed | Done | Downloaded and installed |
| Termius iPhone link sent | Done | App Store link provided |
| Configure VPS connection | Pending | User to do on phone |
| Import SSH key to Termius | Pending | Copy from Windows ~/.ssh/id_ed25519 |

**Termius iPhone App Store Link**:
https://apps.apple.com/us/app/termius-modern-ssh-client/id549039908

---

<!-- section_id: "39410b75-3a00-43c2-aed7-33148549a7b0" -->
### Phase 3: Boot Linux & SSH Access
**Status**: NOT STARTED

| Task | Status | Notes |
|------|--------|-------|
| Boot into Linux | Pending | Login loop is expected |
| Get TTY access (Ctrl+Alt+F2) | Pending | If needed |
| Ensure SSH is running | Pending | `sudo systemctl start sshd` |
| Get Linux IP address | Pending | `ip addr` |
| SSH from VPS to Linux | Pending | Need IP first |

---

<!-- section_id: "fed2fe6d-2033-4192-8aab-de0ac3588a99" -->
### Phase 4: Fix Login Loop
**Status**: NOT STARTED

| Task | Status | Notes |
|------|--------|-------|
| Run diagnostics | Pending | `df -h`, check permissions |
| Remove .Xauthority | Pending | Common fix |
| Remove .ICEauthority | Pending | Common fix |
| Fix home directory permissions | Pending | `chown -R dawson:dawson /home/dawson` |
| Fix /tmp permissions | Pending | `chmod 1777 /tmp` |

---

<!-- section_id: "1b7372d7-6c14-44c1-916a-926e646787dc" -->
### Phase 5: Verify Fix
**Status**: NOT STARTED

| Task | Status | Notes |
|------|--------|-------|
| Reboot Linux | Pending | `sudo reboot` |
| Test graphical login | Pending | Should work after fix |
| Fix git repo filenames | Pending | Replace `*` with `x` in filenames |

---

<!-- section_id: "6089f80f-e955-4789-bc64-b6392eee7c88" -->
## Quick Reference Commands

<!-- section_id: "d6c5141e-0cca-4b94-8273-7a8be23d1988" -->
### From Phone (after setting up Termius)

```bash
# Connect to VPS
ssh root@46.224.184.10

# Use interactive menu
menu

# Quick AI help
g "How do I fix a Linux login loop?"
c "Help me diagnose this error: [paste error]"
cx "Check disk space on Linux"
```

<!-- section_id: "8ee4db61-6f24-428c-b9e6-aab3b7315ffd" -->
### VPS Connection Details
- **Host**: 46.224.184.10
- **User**: root
- **Auth**: SSH Key (~/.ssh/id_ed25519 from Windows)

---

<!-- section_id: "d4d01342-7250-471c-9556-7a2c1f20f95b" -->
## Files Created

| File | Location | Purpose |
|------|----------|---------|
| VPS_AI_CLI_SETUP_COMPLETE.md | 0_instruction_docs/setup/ | Full VPS setup documentation |
| IPHONE_QUICK_GUIDE.md | 0_instruction_docs/setup/ | Step-by-step phone instructions |
| VPS_SSH_PUBLIC_KEY.txt | 0_instruction_docs/setup/ | VPS key to add to Linux |
| add_vps_key_to_linux.sh | 0_instruction_docs/setup/ | Script to authorize VPS key |
| fix_linux_login_loop.sh | 0_instruction_docs/setup/ | Main fix script |
| cloud_server_ai_cli_master_setup.sh | 0_instruction_docs/setup/ | VPS setup script |
| TERMIUS_LINUX_SETUP.md | 0_instruction_docs/setup/ | Termius installation for Linux |
| TERMIUS_CROSS_DEVICE_SETUP.md | 0_instruction_docs/setup/ | Bidirectional SSH between all devices |

---

<!-- section_id: "72614028-553d-4203-8150-198cd17c168d" -->
## Next Actions

1. User: Download Termius on iPhone from App Store
2. User: Configure VPS connection in Termius (host, user, import SSH key)
3. User: Boot Linux machine
4. User: Get Linux IP (via TTY if needed)
5. User: Run `menu` on VPS, select option to SSH to Linux
6. User: Run fix script or manual commands
7. User: Reboot and test login

<!-- section_id: "465ce07f-8f08-46e9-9445-8af4d49c7d40" -->
### Post-Fix Tasks
8. Install Termius on Linux (`sudo snap install termius-app`)
9. Sign in to Termius with same account - hosts sync automatically
10. Fix git repo filenames (replace `*` with `x`)
11. (Optional) Enable Windows SSH server for incoming connections
12. Update all SSH configs with actual Linux IP
13. Verify bidirectional connections: VPS ↔ Linux ↔ Windows ↔ iPhone

<!-- section_id: "3f315466-6454-4ac0-9325-c8b3450981bd" -->
### Cross-Device Connection Matrix

| From ↓ / To → | VPS | Linux | Windows |
|---------------|-----|-------|---------|
| **VPS** | - | ✅ Menu opt 4 | ⏳ Optional |
| **Linux** | ⏳ After fix | - | ⏳ Optional |
| **Windows** | ✅ Done | ⏳ Need IP | - |
| **iPhone** | ⏳ Sync | ⏳ Sync | ⏳ Optional |

See `TERMIUS_CROSS_DEVICE_SETUP.md` for full details.

---

<!-- section_id: "1a33436e-a1de-4d63-9776-9df97f9332c9" -->
## Blockers / Issues

| Issue | Status | Resolution |
|-------|--------|------------|
| Gemini API key region restriction | Resolved | Used OAuth instead |
| Git repo filenames with `*` | Pending | Will fix after Linux access |
| Syncthing auto-start | Resolved | Added to Windows startup |
