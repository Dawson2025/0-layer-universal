---
resource_id: "544cc6b0-4eb6-413c-950f-7c3653ef0af4"
resource_type: "output"
resource_name: "ISSUE_004_gsd_display_criticism"
---
# Criticism: GSD DISPLAY Environment Variable Issue

<!-- section_id: "aacabbf0-309f-400b-bc0d-46350412217e" -->
## Issue Reference
ISSUE_004 - GSD Daemons Fail After Reboot Due to Missing DISPLAY

<!-- section_id: "5a5a3231-1dc0-4415-b584-b8b52208d7a7" -->
## Date
2026-01-26

<!-- section_id: "bfa65622-1068-4778-a1d7-75f7462c0524" -->
## Root Cause Analysis

<!-- section_id: "21909912-14e1-4467-b466-42f84ac5c23b" -->
### Primary Cause
The `gsd-keepalive.service` systemd user service does not have access to the `DISPLAY` environment variable when it runs.

<!-- section_id: "73a6c373-c7d2-4d3f-bc8e-6f29ef89e932" -->
### Technical Explanation
1. **X11 Requirement**: The gsd-media-keys and gsd-power daemons are X11 applications that need to connect to the X display server
2. **Environment Isolation**: Systemd user services run in an isolated environment and don't automatically inherit session environment variables like `DISPLAY`
3. **Service Design Flaw**: The original service file did not explicitly set `DISPLAY=:0`

<!-- section_id: "101e2351-4515-46ea-b75b-d40e66d6c881" -->
### Why Original Service Worked Sometimes
- When started manually from terminal: Terminal session has DISPLAY set
- When timer triggers after graphical session fully initialized: May inherit from session in some cases
- After reboot: Service starts before/during session initialization, no DISPLAY available

<!-- section_id: "aabb1e25-e2c2-412d-b6c3-60a21f9f79ce" -->
## Impact Assessment

| Impact | Severity | Description |
|--------|----------|-------------|
| User Experience | High | Volume/brightness buttons fail every reboot |
| Workaround Effort | Medium | Requires manual commands each boot |
| System Stability | Low | No system damage, just inconvenience |

<!-- section_id: "6ed0ab6f-4e31-4021-9a82-e8782fecd48f" -->
## Design Oversight
The original gsd-keepalive.service was created to restart crashed daemons but did not account for the environment requirements of X11 applications when run via systemd.

<!-- section_id: "fd8b46c8-3118-480e-a26b-498aeb754532" -->
## Lessons Learned
1. Always consider environment variable requirements for X11 applications in systemd services
2. Test systemd services after full reboot, not just manual restarts
3. Check service logs for "Cannot open display" errors when GUI apps fail silently
