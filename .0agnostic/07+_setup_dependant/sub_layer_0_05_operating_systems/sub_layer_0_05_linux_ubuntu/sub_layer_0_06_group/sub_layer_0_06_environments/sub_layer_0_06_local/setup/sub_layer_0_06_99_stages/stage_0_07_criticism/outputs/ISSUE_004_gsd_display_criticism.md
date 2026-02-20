# Criticism: GSD DISPLAY Environment Variable Issue

## Issue Reference
ISSUE_004 - GSD Daemons Fail After Reboot Due to Missing DISPLAY

## Date
2026-01-26

## Root Cause Analysis

### Primary Cause
The `gsd-keepalive.service` systemd user service does not have access to the `DISPLAY` environment variable when it runs.

### Technical Explanation
1. **X11 Requirement**: The gsd-media-keys and gsd-power daemons are X11 applications that need to connect to the X display server
2. **Environment Isolation**: Systemd user services run in an isolated environment and don't automatically inherit session environment variables like `DISPLAY`
3. **Service Design Flaw**: The original service file did not explicitly set `DISPLAY=:0`

### Why Original Service Worked Sometimes
- When started manually from terminal: Terminal session has DISPLAY set
- When timer triggers after graphical session fully initialized: May inherit from session in some cases
- After reboot: Service starts before/during session initialization, no DISPLAY available

## Impact Assessment

| Impact | Severity | Description |
|--------|----------|-------------|
| User Experience | High | Volume/brightness buttons fail every reboot |
| Workaround Effort | Medium | Requires manual commands each boot |
| System Stability | Low | No system damage, just inconvenience |

## Design Oversight
The original gsd-keepalive.service was created to restart crashed daemons but did not account for the environment requirements of X11 applications when run via systemd.

## Lessons Learned
1. Always consider environment variable requirements for X11 applications in systemd services
2. Test systemd services after full reboot, not just manual restarts
3. Check service logs for "Cannot open display" errors when GUI apps fail silently
