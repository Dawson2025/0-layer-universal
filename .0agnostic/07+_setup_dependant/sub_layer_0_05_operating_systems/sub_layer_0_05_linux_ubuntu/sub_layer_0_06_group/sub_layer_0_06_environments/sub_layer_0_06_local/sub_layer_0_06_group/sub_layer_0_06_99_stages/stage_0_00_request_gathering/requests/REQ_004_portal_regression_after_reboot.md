---
resource_id: "7f551b92-90a6-4cb0-a765-f6ae5822eb81"
resource_type: "document"
resource_name: "REQ_004_portal_regression_after_reboot"
---
# REQ_004: Portal Service Regression After Reboot

**Date Reported**: 2026-01-29
**Status**: Active (just occurred)
**Severity**: High (blocks Files, Terminal, LibreOffice)
**Related**: ISSUE_005 (supposedly fixed 2026-01-28)

---

<!-- section_id: "04c00012-15c1-426f-96bf-3440ed970bff" -->
## Problem Statement

After rebooting the system to fix audio issues:
- ✅ vibe-typer now works (audio renderer timeout resolved)
- ❌ Files app won't open
- ❌ Terminal app won't open
- ❌ LibreOffice won't open

**Root Cause**: xdg-desktop-portal service crashed immediately after boot and autostart fix script didn't run in time.

---

<!-- section_id: "4e467e7a-a213-43cb-8df2-3b1352c22d6f" -->
## Timeline

| Time | Event |
|------|-------|
| 2026-01-28 09:50+ | ISSUE_005: Portal crashes, user implements fix with autostart script |
| 2026-01-28 | System appears working, Files/Terminal open successfully |
| 2026-01-29 18:30+ | User reboots to fix vibe-typer audio timeout |
| 2026-01-29 18:46+ | Portal service crashes on boot (GTK portal process exits with status 1) |
| 2026-01-29 18:46+ | Autostart script doesn't execute in time - portal stays broken |
| 2026-01-29 18:50+ | Manual fix script execution restores portal services |

---

<!-- section_id: "5d24bbb8-5c4e-45b1-ae0e-82b42454b795" -->
## Diagnostic Findings

<!-- section_id: "3dd6ef2b-9d92-42ae-b52f-fc89e49f12ad" -->
### Portal Crash at Boot
```
Status: Failed (Result: signal - SIGKILL)
Started: 2026-01-29 18:46:28
Crashed: 2026-01-29 18:46:34 (6 seconds after startup)
Error: Failed to create access proxy: Process org.freedesktop.impl.portal.desktop.gtk exited with status 1
```

<!-- section_id: "1fe6e1fd-af9c-48c8-974c-8b8ab41fb005" -->
### Autostart Script Issue
**File**: `~/.config/autostart/fix-portal-services.desktop`
- File exists ✓
- `X-GNOME-Autostart-enabled=true` ✓
- `X-GNOME-Autostart-Delay=5` seconds
- Script is executable ✓

**Problem**: Script didn't execute at login
- Portal crashed at 18:46:28
- Script would have executed at 18:46:33 (if it ran)
- Not fast enough - portal already crashed
- Autostart timing is not reliable

<!-- section_id: "9e5d59f5-c777-470d-959f-c938ea4ed2b9" -->
### Manual Fix Success
Running the script manually:
```bash
bash /home/dawson/.local/bin/fix-portal-services.sh
```

Result:
- ✅ xdg-desktop-portal-gtk started
- ✅ xdg-desktop-portal started
- ✅ gnome-terminal-server started
- ✅ Portal services now responding

---

<!-- section_id: "108939a0-fd3f-412f-9e67-03d1833bd584" -->
## Root Cause Analysis

<!-- section_id: "d8c03513-9d7e-4c1e-9db8-7c78afa668ae" -->
### Why Portal Crashes at Boot
The xdg-desktop-portal service starts before the GTK portal backend is ready:
1. Systemd starts `xdg-desktop-portal.service`
2. Portal immediately tries to start GTK backend
3. GTK backend exits with status 1 (likely missing display, not ready)
4. Portal has no backends, systemd kills it

<!-- section_id: "45a4a456-7445-4fd0-b9bf-609f30420928" -->
### Why Autostart Didn't Prevent It
Current approach:
```
Boot sequence:
  1. Systemd user session starts (0ms)
  2. Services start (xdg-desktop-portal, etc) (50-100ms)
  3. Desktop environment initializes (1-5 seconds)
  4. Autostart scripts execute (5 seconds later by default)
  ↓
Portal crashes before autostart has a chance to fix it
```

---

<!-- section_id: "ee15a95b-05ce-4471-bca9-35887f4d6700" -->
## Why This Wasn't Caught Before

ISSUE_005 was marked "resolved" on 2026-01-28, but:
1. System hadn't rebooted since implementing the fix
2. Autostart script is only needed at login/reboot
3. Previous testing only covered "Files won't open in live session"
4. Not tested after logout/login or reboot

The fix prevented the crash from recurring in the live session, but doesn't prevent the initial crash on boot.

---

<!-- section_id: "77fb440f-a9ae-4d45-88ff-e6e142ee69d1" -->
## Solution Requirements

The fix must:
1. **Prevent portal from crashing at boot** (not just recover after crash)
2. **Run early enough** (before portal service starts)
3. **Be reliable** (work without manual intervention)
4. **Persist across reboots**

<!-- section_id: "cb695dc0-6b80-4cfd-95dc-6c2b4c527b6d" -->
### Possible Approaches

**Option A**: Systemd service dependency (best)
- Create a new systemd user service that starts before portal
- Ensures portal backends are ready when portal starts
- Guaranteed to run at boot

**Option B**: Systemd-tmpfiles hook (good)
- Run script as part of systemd session setup
- Earlier than autostart, before services start

**Option C**: Better autostart timing (current, insufficient)
- Reduce delay or use different trigger
- Still not guaranteed to run before portal

**Option D**: Fix GTK portal exit issue (ideal)
- Debug why GTK portal exits with status 1
- Fix root cause instead of working around it

---

<!-- section_id: "0f3a0d35-4eff-4690-8844-1cef6f09a248" -->
## Immediate Workaround

Users experiencing this can manually run:
```bash
bash /home/dawson/.local/bin/fix-portal-services.sh
```

This immediately restores Files, Terminal, and LibreOffice functionality.

---

<!-- section_id: "37b0bf86-860e-4530-84ae-d8cbcbcd4f3c" -->
## Questions for Investigation

1. Why does GTK portal exit with status 1 at boot?
2. Can we make it wait for display before starting?
3. Should portal service depend on other services?
4. Is there a better way to handle this at the systemd level?

---

<!-- section_id: "cd7eaabe-beb4-43b3-bc1e-f777027a15f7" -->
## Related Issues

| Issue | Status | Location |
|-------|--------|----------|
| ISSUE_005 | Resolved (partial) | `ISSUE_005_portal_apps_final_config.md` |
| REQ_003 | Resolved | Audio/vibe-typer fixed by reboot ✓ |
| REQ_004 | **Active** | **← Current issue** |
