---
resource_id: "43d84845-a02b-45b7-a574-32d738f70113"
resource_type: "output"
resource_name: "ISSUE_005_portal_apps_criticism"
---
# Criticism: XDG Portal / GNOME Apps Not Opening

<!-- section_id: "6616371a-66e3-480f-a6c8-df09e84bef73" -->
## Issue Reference
ISSUE_005 - Files and Terminal Apps Not Opening

<!-- section_id: "d3bd6911-48e8-4ee9-85eb-cbe46cd4c2d2" -->
## Date
2026-01-28

<!-- section_id: "05e02a4d-602c-4a08-9d93-cec36f13b649" -->
## Root Cause Analysis

<!-- section_id: "b46ae14a-3a58-4465-a85e-29cc3f1827e8" -->
### Primary Issue: xdg-desktop-portal-gnome SEGFAULT
- The GNOME portal implementation crashes with SIGSEGV (signal 11)
- This appears to be a bug in the xdg-desktop-portal-gnome package (version 46.2-0ubuntu1)
- Reinstalling the package did not fix the issue
- The crash prevents the main portal service from initializing properly

<!-- section_id: "1852fc06-984a-44df-8fef-822bb6fad786" -->
### Secondary Issue: Missing DISPLAY Environment Variable
- Systemd user services run in an isolated environment
- They do not automatically inherit session environment variables like DISPLAY
- X11 applications (including portals and terminal server) require DISPLAY to connect to the display server
- Existing override for xdg-desktop-portal-gtk had DISPLAY set but service still failed due to dependency on crashing GNOME portal

<!-- section_id: "fde24f4e-e214-4b23-a7ff-d5ea22f2b058" -->
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

<!-- section_id: "41ae5fea-2064-497f-a913-de6eb07d3efe" -->
## Impact Assessment

| Impact | Severity | Description |
|--------|----------|-------------|
| User Experience | Critical | Cannot open Files or Terminal apps |
| Workaround Effort | High | Requires manual service starts |
| System Stability | Medium | Core GNOME functionality broken |

<!-- section_id: "82cdb5d8-fa82-44c5-8635-84286cca5046" -->
## Design Issues Identified

1. **No Fallback Mechanism**: When GNOME portal crashes, system doesn't gracefully fall back to GTK portal
2. **Environment Isolation**: Systemd services not configured with required X11 environment
3. **Hard Dependencies**: Main portal waits too long for crashing implementation

<!-- section_id: "2009e0fa-9e6b-4bab-ae49-cd14f5b24450" -->
## Lessons Learned
1. XDG portal configuration can override which implementation is used
2. portals.conf file allows specifying preferred portal backend
3. Multiple services need DISPLAY override for X11 sessions
