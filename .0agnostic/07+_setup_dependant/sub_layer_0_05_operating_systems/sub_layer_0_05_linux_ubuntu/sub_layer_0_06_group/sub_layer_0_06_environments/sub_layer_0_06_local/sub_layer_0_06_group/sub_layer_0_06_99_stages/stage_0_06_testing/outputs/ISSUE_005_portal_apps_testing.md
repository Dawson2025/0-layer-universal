---
resource_id: "5d34df75-3eb6-4845-82e3-be36f462c822"
resource_type: "output"
resource_name: "ISSUE_005_portal_apps_testing"
---
# Testing: XDG Portal / GNOME Apps Not Opening

<!-- section_id: "fdc1328f-a72d-4cc8-a40b-61340921669f" -->
## Issue Reference
ISSUE_005 - Files and Terminal Apps Not Opening

<!-- section_id: "da7e098a-27b8-4bbb-88ab-02e08db8a6a7" -->
## Date
2026-01-28

<!-- section_id: "479735ce-eaf8-4aba-9356-7fa75d09c97e" -->
## Symptoms Reported
- Files app (Nautilus) would not open
- Terminal app (gnome-terminal) would not open
- Apps launched but no window appeared

<!-- section_id: "9bd190fc-19fe-4c97-a57e-0377ac7c2f84" -->
## Test Performed

<!-- section_id: "34925bd9-717a-42bb-a890-7daffb2ff780" -->
### 1. Check User Journal for Errors
```bash
journalctl --user -p err -n 50 --no-pager
```

**Results:**
- `xdg-desktop-portal-gnome.service` - Failed with SEGFAULT (signal 11)
- `xdg-desktop-portal-gtk.service` - "cannot open display: :0"
- `gnome-terminal-server.service` - "Cannot open display:"
- `xdg-desktop-portal.service` - Timeout waiting for portal implementations

<!-- section_id: "5b3988b7-8b84-47e5-b9e9-78a412d08929" -->
### 2. Check Portal Service Status
```bash
systemctl --user status xdg-desktop-portal-gnome.service
```

**Results:**
```
Active: failed (Result: core-dump)
Process: ExecStart=/usr/libexec/xdg-desktop-portal-gnome (code=dumped, signal=SEGV)
```

<!-- section_id: "1695532d-0c6f-4047-8315-46017208c473" -->
### 3. Check Terminal Server Status
```bash
systemctl --user status gnome-terminal-server.service
```

**Results:**
```
Active: failed (Result: exit-code)
gnome-terminal-server: Failed to parse arguments: Cannot open display:
```

<!-- section_id: "ead88e5e-3d6b-49d6-8a5f-661e2760808c" -->
### 4. Manual Launch Test
```bash
DISPLAY=:0 XAUTHORITY=/home/dawson/.Xauthority /usr/libexec/xdg-desktop-portal-gnome &
```

**Result:** Process started and stayed running when DISPLAY was set manually.

<!-- section_id: "580fc086-a74e-4852-9f25-3ae39340b8c8" -->
## Root Causes Identified

1. **xdg-desktop-portal-gnome**: Crashing with SEGFAULT when started by systemd
2. **xdg-desktop-portal-gtk**: Missing DISPLAY environment variable
3. **gnome-terminal-server**: Missing DISPLAY environment variable
4. **All services**: Systemd user services don't inherit session DISPLAY variable

<!-- section_id: "70ecf5a4-94b4-4b86-9c3e-84f9c9f7bb45" -->
## Conclusion
Multiple XDG desktop portal services are failing due to:
1. A bug causing GNOME portal to crash
2. Missing DISPLAY environment variable in systemd service context

These services are required for GNOME apps to function properly.
