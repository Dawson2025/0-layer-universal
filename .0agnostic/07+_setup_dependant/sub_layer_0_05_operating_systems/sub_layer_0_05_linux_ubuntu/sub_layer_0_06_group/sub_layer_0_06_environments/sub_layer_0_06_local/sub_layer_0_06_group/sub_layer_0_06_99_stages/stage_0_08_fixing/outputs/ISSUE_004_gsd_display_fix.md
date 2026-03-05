---
resource_id: "93b79051-b06b-496a-9723-d57393ed5bda"
resource_type: "output"
resource_name: "ISSUE_004_gsd_display_fix"
---
# Fix: GSD DISPLAY Environment Variable Issue

<!-- section_id: "e5c56604-3da5-4166-869a-dd49e3e4662f" -->
## Issue Reference
ISSUE_004 - GSD Daemons Fail After Reboot Due to Missing DISPLAY

<!-- section_id: "d2f5317a-00a7-4263-8a37-d1e798c7d865" -->
## Date
2026-01-26

<!-- section_id: "6c4929c6-bd94-40b1-8f65-44aceb5f667b" -->
## Fix Applied

<!-- section_id: "36cbdffe-584d-4667-87ce-ae58c3b77e50" -->
### 1. Immediate Fix (Manual)
Started daemons manually with DISPLAY set:
```bash
DISPLAY=:0 /usr/libexec/gsd-media-keys &
DISPLAY=:0 /usr/libexec/gsd-power &
```

<!-- section_id: "b518ecfb-56ca-4929-9737-c7323f55b6e7" -->
### 2. Permanent Fix (Service Update)
Added `Environment=DISPLAY=:0` to the systemd service file.

**File**: `~/.config/systemd/user/gsd-keepalive.service`

**Change Made**:
```diff
 [Service]
 Type=oneshot
 RemainAfterExit=yes
+Environment=DISPLAY=:0
 ExecStart=/bin/bash -c 'pgrep -x gsd-media-keys || /usr/libexec/gsd-media-keys & pgrep -x gsd-power || /usr/libexec/gsd-power &'
```

<!-- section_id: "c45cd6b6-88e2-469f-86a0-fc16cd591715" -->
### 3. Reload Systemd
```bash
systemctl --user daemon-reload
```

<!-- section_id: "94b4542f-c1af-40f6-8bbd-963bf6db503d" -->
## Updated Service File (Complete)
```ini
[Unit]
Description=Keep GNOME Settings Daemons alive
After=graphical-session.target

[Service]
Type=oneshot
RemainAfterExit=yes
Environment=DISPLAY=:0
ExecStart=/bin/bash -c 'pgrep -x gsd-media-keys || /usr/libexec/gsd-media-keys & pgrep -x gsd-power || /usr/libexec/gsd-power &'
ExecStop=/bin/true

[Install]
WantedBy=default.target
```

<!-- section_id: "8849f9c5-7d07-4f83-ba64-af0b894eafe9" -->
## Verification
```bash
# Check daemons are running
pgrep -a gsd-media-keys
pgrep -a gsd-power

# Test volume buttons - should work
# Test brightness buttons - should work
```

<!-- section_id: "81d167cc-fcdc-4859-9ca2-790cbb2e043d" -->
## Result
- Volume buttons: Working
- Brightness buttons: Working
- Persists after reboot: Yes (with updated service)
