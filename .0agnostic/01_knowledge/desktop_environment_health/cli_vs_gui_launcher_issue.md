---
resource_id: "2c0b2fb1-f8db-4af2-b44c-9f6c5c42b645"
resource_type: "knowledge"
resource_name: "cli_vs_gui_launcher_issue"
---
# Knowledge: CLI vs GUI Launcher Failure Pattern

**Topic**: Desktop Environment / Session Management
**Severity**: High (blocks GUI usage while CLI works)
**First Observed**: 2026-02-26
**Status**: Active Issue

---

<!-- section_id: "74db5a55-80a2-46d0-9112-230056a18f2a" -->
## The Problem

Applications launch successfully via terminal but fail when clicking GUI icons:

**Working (Terminal)**:
```bash
nautilus &           # Opens file manager
gnome-control-center &  # Opens Settings
gedit &              # Opens Text Editor
```

**Broken (GUI Icon)**:
- Click Files icon → Nothing happens
- Click Settings icon → Nothing happens
- Click Text Editor icon → Crash or silent failure

**Inconsistent Behavior**:
- Some icons work fine: Firefox, Chrome, etc.
- Only certain apps fail when clicked
- Terminal launches work for ALL apps

---

<!-- section_id: "e3cd1db2-186c-465a-8cde-0a46fb11a940" -->
## Why This Happens

<!-- section_id: "79e12522-a898-4520-afc2-bcc3ab0c1156" -->
### Environment Variables

When you run a command in terminal, the shell sets environment variables:
```bash
echo $DISPLAY              # :0
echo $XAUTHORITY           # /home/user/.Xauthority
echo $DBUS_SESSION_BUS_ADDRESS  # /run/user/1000/bus
```

When you click a GUI icon, it launches via the desktop environment's application launcher (usually DBus-activated), which may have:
- Missing environment variables
- Broken D-Bus registration
- Stale session state
- Wrong working directory

<!-- section_id: "5f17bf54-9626-4920-832e-512bb2bfa989" -->
### D-Bus and Session State

The `.desktop` file launcher relies on D-Bus to:
1. Start the application service
2. Register it in the session
3. Pass environment variables correctly

If D-Bus is broken or GNOME session services are failed (like gsd-* daemons), the launcher fails silently.

<!-- section_id: "3b6b9663-61f0-40be-a129-cff5e75647b2" -->
### Session vs Shell Environment

**Shell Environment** (Terminal):
- Inherits all variables from login session
- Has access to user's full environment
- Works even if D-Bus is partially broken

**Session Environment** (GUI Icon):
- Depends on systemd --user services
- Depends on D-Bus session activation
- Fails if any service in the chain is broken

---

<!-- section_id: "de323b6f-a4d7-4725-a288-2aa3f799dd11" -->
## Symptoms Checklist

✓ Apps work in terminal
✓ Apps fail when clicking icon
✓ Some icons work, others don't
✓ Error messages either non-existent or vague
✓ `systemctl --user --failed` shows failed services
✓ `echo $DBUS_SESSION_BUS_ADDRESS` is empty or stale

---

<!-- section_id: "3db1c147-872f-4629-99eb-f64c1222be0d" -->
## Root Causes (Priority Order)

1. **Missing DISPLAY variable** (most common)
   - GUI launcher doesn't have X11 display set
   - App fails with "Cannot open display"

2. **D-Bus session not running**
   - DBUS_SESSION_BUS_ADDRESS empty or wrong
   - Session services can't communicate

3. **Failed system services**
   - gsd-media-keys, gsd-power, etc. in FAILED state
   - Cascades to break D-Bus and session

4. **Broken .desktop file**
   - Wrong Exec path or syntax
   - Missing Environment= directive
   - Terminal=true when should be false

5. **Working directory mismatch**
   - App expects to run from specific directory
   - Desktop launcher runs from wrong location

6. **Permissions issue**
   - App can't read ~/.config, ~/.local, etc.
   - Usually after system changes or file moves

---

<!-- section_id: "c21a374a-2d0e-4205-a8db-b98cbc0f3e71" -->
## Connection to Other Issues

**Linked to**: Daemon persistence after restart
- When gsd-* daemons fail post-boot, D-Bus breaks
- Which cascades to break GUI app launchers
- Symptoms appear as "icons don't work"

**Linked to**: Display readiness
- If DISPLAY isn't ready, GUI apps fail silently
- Terminal provides fallback because it inherits environment

**Linked to**: systemd user session health
- Broken user services affect all GUI launches
- Terminal bypasses this by not using D-Bus

---

<!-- section_id: "1cde2c9b-4dcd-41f4-9d64-a78c8423af17" -->
## Diagnostic Commands

<!-- section_id: "073c44d2-1515-49a8-ac6c-9b4c7f8f89bb" -->
### Check what's broken
```bash
# Is D-Bus running?
systemctl --user status dbus.service

# Are system services failed?
systemctl --user --failed

# What's the environment for GUI apps?
systemctl --user show-environment | grep -E "DISPLAY|DBUS|XAUTH"

# Check specific app's .desktop file
grep -A 10 "Exec=" ~/.local/share/applications/nautilus.desktop
```

<!-- section_id: "af4fd449-8a1f-483f-97ac-fdbdb1792173" -->
### Check journal for errors
```bash
journalctl --user -f &  # Start monitoring
# Then click the icon that fails
# Watch for error messages
```

<!-- section_id: "b29fea19-d18e-4648-a5f7-f2e88cea3366" -->
### Verify terminal environment
```bash
# This should work:
nautilus

# This should match:
env | grep DISPLAY
# Compare to:
systemctl --user show-environment | grep DISPLAY
```

---

<!-- section_id: "1270b020-10e0-46a6-a3c1-f63042624f73" -->
## When This Occurs

**After system restart**: Most common
- GNOME/systemd session initialization incomplete
- D-Bus not fully ready
- gsd-* services failing during boot

**After sleep/wake**: Common on laptops
- gnome-shell grabs become stale
- D-Bus connections drop
- Launcher infrastructure needs refresh

**After package updates**: Sometimes
- New .desktop files may have wrong syntax
- D-Bus service files not registered
- Environment variables changed

**On fresh login**: Rare but possible
- Session didn't fully initialize
- User services didn't auto-start

---

<!-- section_id: "ea581fee-aa3a-47bf-ba6c-4c32e82cdd01" -->
## Impact

**High severity because**:
1. Blocks normal GUI usage (clicking icons)
2. Users must use CLI workaround
3. Can cascade to break other functionality
4. Indicative of deeper session health issue

**Why it's not catastrophic**:
1. Terminal provides workaround
2. Some apps still work via icons
3. Not permanent (session restart usually fixes)

---

<!-- section_id: "4d4b6fd3-b522-446a-bb52-7b54e3807f9b" -->
## Solution Approach

See `/protocols/cli_vs_gui_launcher_diagnosis_protocol.md` for detailed recovery steps.

**Quick fix**: Restart the user session
```bash
# Log out and back in
# Or on X11: systemctl --user restart graphical-session.target
```

**Persistent fix**: Ensure D-Bus and session services start properly at boot

---

<!-- section_id: "c604e68e-1d84-4669-8bcf-3525a83e09d6" -->
## References

- GNOME Session Management: `.0agnostic/01_knowledge/gnome_desktop/docs/gnome_architecture.md`
- Systemd User Services: `.0agnostic/01_knowledge/system_services/docs/systemd_user_services.md`
- GSD Keepalive Fix: `.0agnostic/07+_setup_dependant/.../stage_0_09_current_product/outputs/gsd_keepalive_fix.md`
- Daemon Persistence: `.0agnostic/07+_setup_dependant/.../stage_0_06_testing/outputs/by_purpose/daemon_persistence_restart_fix/`

---

**Status**: This is an active issue observed on 2026-02-26.
**Next Steps**: Implement daemon persistence fix (Solution 1/2/3) to resolve at root cause.
