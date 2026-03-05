---
resource_id: "093d942f-b7b2-437b-b9ac-776e9239a50c"
resource_type: "rule"
resource_name: "cli_gui_launcher_mismatch_rule"
---
# Rule: CLI vs GUI Launcher Mismatch Detection & Recovery

**Scope**: Ubuntu/GNOME/Unity systems with CLI/GUI inconsistency
**Applicability**: When user reports "works in terminal but not from icon"
**Priority**: High - indicates session health issue
**Auto-trigger**: When `systemctl --user --failed` shows gsd-* or D-Bus failures

---

## Detection Rule

**DETECT if ALL of the following are true**:
- ✓ Application works: `nautilus`, `gnome-control-center`, `gedit`
- ✓ Same app fails when clicking GUI icon
- ✓ Some icons work (Chrome, Firefox) but others don't (Nautilus, Settings)
- ✓ `systemctl --user --failed` shows service failures
- ✓ `echo $DBUS_SESSION_BUS_ADDRESS` is empty or appears stale

**DO NOT** assume it's just a broken .desktop file — **this pattern indicates session-level failure**.

---

## Immediate Actions

**MUST RUN** (in order):

### 1. Verify Problem Pattern (5 min)
```bash
# Test CLI works
nautilus &
# Verify fails when clicking icon
# Document: "Nautilus opens via terminal but not via icon"
```

### 2. Check System State (3 min)
```bash
# What's broken?
systemctl --user --failed
systemctl --user status dbus.service
systemctl --user status graphical-session.target

# Capture environment
echo "=== Working Environment ==="
env | grep -E "DISPLAY|DBUS|XAUTH|TERM|PATH"
```

### 3. Attempt Quick Recovery (2 min)
```bash
# Option A: Restart user session services
systemctl --user restart graphical-session.target

# Option B: Manually set D-Bus address (if empty)
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus

# Option C: Kill and restart desktop environment
gnome-shell --replace &  # X11 only, WARNING: may kill open apps
```

### 4. Test Recovery (2 min)
```bash
# Test if icons work now
# Click Nautilus, Settings, Text Editor icons
# Verify all previously broken apps now launch
```

**Total diagnostic time: ~15 minutes**

---

## If Quick Recovery Works

**DO:**
1. Document what fixed it (which action)
2. Mark as "Session State Corruption" in logs
3. Monitor for recurrence

**THEN:** Implement one of the permanent solutions below

---

## If Quick Recovery Fails

**Root cause is likely daemon persistence issue** — proceed to:

1. **Check daemon status**:
   ```bash
   systemctl --user status org.gnome.SettingsDaemon.MediaKeys.service
   systemctl --user status org.gnome.SettingsDaemon.Power.service
   ```

2. **If gsd-* are FAILED**: This is the root cause
   - See: `.0agnostic/03_protocols/cli_vs_gui_launcher_diagnosis_protocol.md`
   - See: `.0agnostic/07+_setup_dependant/.../stage_0_09_current_product/outputs/gsd_keepalive_fix.md`

3. **Next step**: Test daemon persistence fix (restart-based solutions)

---

## Permanent Solutions (Priority Order)

### Solution 1: Restart User Session (Temporary, ~1 week)
```bash
# Log out and back in
# Or: systemctl --user restart graphical-session.target
```
**Lasts until**: Next system restart or sleep/wake
**Effort**: Minimal (1 minute)
**Success rate**: ~70%

### Solution 2: Deploy gsd-keepalive Timer (Temporary, ~1 month)
Already deployed on this system.
**Lasts until**: Post-restart failure pattern occurs again
**Effort**: Already done
**Success rate**: ~60% (timing issues)

### Solution 3: Test Daemon Persistence Fix (Permanent)
Implement Solution 1/2/3 from restart testing.
**Lasts until**: Configured properly (should be permanent)
**Effort**: ~1-2 hours setup + restart testing
**Success rate**: Should be 90%+

---

## Documentation Requirements

**When this rule triggers, MUST UPDATE**:

1. **Stage 0_06_testing** (Testing stage):
   - Document: "CLI launcher works, GUI icon fails"
   - Log: Which apps fail, which work
   - Evidence: `systemctl --user --failed` output

2. **Stage 0_07_criticism** (Analysis stage):
   - Root cause: Session state corruption vs daemon failure vs D-Bus issue
   - Classification: "CLI/GUI Launcher Mismatch"

3. **Stage 0_08_fixing** (Fix stage):
   - If manual restart fixes it: "Temporary fix applied"
   - If daemon fix needed: "Requires daemon persistence solution"
   - Link to: `/protocols/cli_vs_gui_launcher_diagnosis_protocol.md`

4. **Knowledge base**:
   - Update: `/knowledge/desktop_environment_health/cli_vs_gui_launcher_issue.md`
   - Note: Occurrence date, trigger conditions, resolution

---

## Prevention

**MUST MONITOR** after implementing daemon persistence fix:
- Test GUI icon launches immediately after restart
- Verify all icons work (not just terminal)
- Ensure both volume AND brightness keys work (indicates full gsd-* health)

**RED FLAG** if CLI works but GUI icons still fail post-fix:
- Indicates the daemon fix isn't complete
- Or there's a secondary session issue

---

## Escalation Path

**If this rule triggers repeatedly:**
1. CLI launcher mismatch might be SYMPTOM, not ROOT CAUSE
2. Real issue is likely: Daemon persistence → D-Bus failure → Launcher failure
3. Focus on implementing permanent daemon persistence fix
4. Test across: Restart, Sleep/Wake, Shell restart

---

## Related Rules & Protocols

- **Daemon Persistence Rule**: `.0agnostic/02_rules/dynamic/local_ubuntu_desktop_troubleshooting/`
- **Diagnostic Protocol**: `/protocols/cli_vs_gui_launcher_diagnosis_protocol.md`
- **Knowledge Base**: `/knowledge/desktop_environment_health/cli_vs_gui_launcher_issue.md`

---

## Success Criteria

✓ All GUI icons launch correctly
✓ All apps function identically to CLI launches
✓ Volume AND brightness keys work
✓ Settings shows brightness slider
✓ Nautilus opens from icon
✓ GNOME Control Center opens from icon
✓ Works consistently after system restart

---

**Version**: 1.0
**Created**: 2026-02-26
**Status**: Active
**Next Review**: After daemon persistence fix implementation
