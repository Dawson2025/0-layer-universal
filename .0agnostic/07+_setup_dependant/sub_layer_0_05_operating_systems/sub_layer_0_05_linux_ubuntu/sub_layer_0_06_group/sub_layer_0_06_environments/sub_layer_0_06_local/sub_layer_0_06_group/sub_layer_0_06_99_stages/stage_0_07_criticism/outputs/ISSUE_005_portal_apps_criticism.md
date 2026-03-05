---
resource_id: "43d84845-a02b-45b7-a574-32d738f70113"
resource_type: "output"
resource_name: "ISSUE_005_portal_apps_criticism"
---
# Criticism: XDG Portal / GNOME Apps Not Opening

## Issue Reference
ISSUE_005 - Files and Terminal Apps Not Opening

## Date
2026-01-28

## Root Cause Analysis

### Primary Issue: xdg-desktop-portal-gnome SEGFAULT
- The GNOME portal implementation crashes with SIGSEGV (signal 11)
- This appears to be a bug in the xdg-desktop-portal-gnome package (version 46.2-0ubuntu1)
- Reinstalling the package did not fix the issue
- The crash prevents the main portal service from initializing properly

### Secondary Issue: Missing DISPLAY Environment Variable
- Systemd user services run in an isolated environment
- They do not automatically inherit session environment variables like DISPLAY
- X11 applications (including portals and terminal server) require DISPLAY to connect to the display server
- Existing override for xdg-desktop-portal-gtk had DISPLAY set but service still failed due to dependency on crashing GNOME portal

### Cascade Effect
```
xdg-desktop-portal-gnome (CRASH)
        ↓
xdg-desktop-portal (TIMEOUT waiting for implementations)
        ↓
xdg-desktop-portal-gtk (CAN'T START - no display + dependency issues)
        ↓
GNOME apps (CAN'T OPEN - no portal services)
```

## Impact Assessment

| Impact | Severity | Description |
|--------|----------|-------------|
| User Experience | Critical | Cannot open Files or Terminal apps |
| Workaround Effort | High | Requires manual service starts |
| System Stability | Medium | Core GNOME functionality broken |

## Design Issues Identified

1. **No Fallback Mechanism**: When GNOME portal crashes, system doesn't gracefully fall back to GTK portal
2. **Environment Isolation**: Systemd services not configured with required X11 environment
3. **Hard Dependencies**: Main portal waits too long for crashing implementation

## Lessons Learned
1. XDG portal configuration can override which implementation is used
2. portals.conf file allows specifying preferred portal backend
3. Multiple services need DISPLAY override for X11 sessions
