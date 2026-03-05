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

<!-- section_id: "86379279-84c2-48b2-a735-3ed9c8176480" -->
## Detection Rule

**DETECT if ALL of the following are true**:
- ✓ Application works: `nautilus`, `gnome-control-center`, `gedit`
- ✓ Same app fails when clicking GUI icon
- ✓ Some icons work (Chrome, Firefox) but others don't (Nautilus, Settings)
- ✓ `systemctl --user --failed` shows service failures
- ✓ `echo $DBUS_SESSION_BUS_ADDRESS` is empty or appears stale

**DO NOT** assume it's just a broken .desktop file — **this pattern indicates session-level failure**.

---

<!-- section_id: "ba950b24-0e41-4c98-b559-aa7ce987fc3b" -->
## Immediate Actions

**MUST RUN** (in order):

<!-- section_id: "549a51ea-a45f-4a12-8e73-52e3f88aa40d" -->
### 1. Verify Problem Pattern (5 min)
```bash
# Test CLI works
nautilus &
# Verify fails when clicking icon
# Document: "Nautilus opens via terminal but not via icon"
```

<!-- section_id: "01565903-470a-4b6c-a9b2-71675cbbae90" -->
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

<!-- section_id: "68c8e162-7aa2-47e0-835e-69168c7844c1" -->
### 3. Attempt Quick Recovery (2 min)
```bash
# Option A: Restart user session services
systemctl --user restart graphical-session.target

# Option B: Manually set D-Bus address (if empty)
export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus

# Option C: Kill and restart desktop environment
gnome-shell --replace &  # X11 only, WARNING: may kill open apps
```

<!-- section_id: "8d295885-39fb-4873-a90a-1f47e90d09e1" -->
### 4. Test Recovery (2 min)
```bash
# Test if icons work now
# Click Nautilus, Settings, Text Editor icons
# Verify all previously broken apps now launch
```

**Total diagnostic time: ~15 minutes**

---

<!-- section_id: "f9ef5e0f-bb9f-4204-b950-2a9b61471157" -->
## If Quick Recovery Works

**DO:**
1. Document what fixed it (which action)
2. Mark as "Session State Corruption" in logs
3. Monitor for recurrence

**THEN:** Implement one of the permanent solutions below

---

<!-- section_id: "36555b9d-a514-4f54-98d9-c9be129c7d4c" -->
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

<!-- section_id: "89d0fff2-0431-47a7-b5e2-d8e4882db984" -->
## Permanent Solutions (Priority Order)

<!-- section_id: "346d3bef-05fa-4a85-b5db-da1add99d02c" -->
### Solution 1: Restart User Session (Temporary, ~1 week)
```bash
# Log out and back in
# Or: systemctl --user restart graphical-session.target
```
**Lasts until**: Next system restart or sleep/wake
**Effort**: Minimal (1 minute)
**Success rate**: ~70%

<!-- section_id: "16496c4f-43f6-43fc-afc6-8dd00752a3ae" -->
### Solution 2: Deploy gsd-keepalive Timer (Temporary, ~1 month)
Already deployed on this system.
**Lasts until**: Post-restart failure pattern occurs again
**Effort**: Already done
**Success rate**: ~60% (timing issues)

<!-- section_id: "1cd8c93c-0e40-4f69-b75a-9c14bfbc7a84" -->
### Solution 3: Test Daemon Persistence Fix (Permanent)
Implement Solution 1/2/3 from restart testing.
**Lasts until**: Configured properly (should be permanent)
**Effort**: ~1-2 hours setup + restart testing
**Success rate**: Should be 90%+

---

<!-- section_id: "db615a99-c03a-43fd-93cf-cc90d315d40e" -->
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

<!-- section_id: "46d3fa32-389b-4cfe-a56a-187097a0accb" -->
## Prevention

**MUST MONITOR** after implementing daemon persistence fix:
- Test GUI icon launches immediately after restart
- Verify all icons work (not just terminal)
- Ensure both volume AND brightness keys work (indicates full gsd-* health)

**RED FLAG** if CLI works but GUI icons still fail post-fix:
- Indicates the daemon fix isn't complete
- Or there's a secondary session issue

---

<!-- section_id: "deebe464-7b2f-498f-886c-c05c8b41dc76" -->
## Escalation Path

**If this rule triggers repeatedly:**
1. CLI launcher mismatch might be SYMPTOM, not ROOT CAUSE
2. Real issue is likely: Daemon persistence → D-Bus failure → Launcher failure
3. Focus on implementing permanent daemon persistence fix
4. Test across: Restart, Sleep/Wake, Shell restart

---

<!-- section_id: "fadc2a33-9e95-4a39-82d1-a8fd4543933d" -->
## Related Rules & Protocols

- **Daemon Persistence Rule**: `.0agnostic/02_rules/dynamic/local_ubuntu_desktop_troubleshooting/`
- **Diagnostic Protocol**: `/protocols/cli_vs_gui_launcher_diagnosis_protocol.md`
- **Knowledge Base**: `/knowledge/desktop_environment_health/cli_vs_gui_launcher_issue.md`

---

<!-- section_id: "bb43c6c0-4287-4081-a9fb-8c90d4c78d4b" -->
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
