---
resource_id: "83e03836-f088-4846-8d5d-024d7c666326"
resource_type: "output"
resource_name: "ISSUE_004_gsd_display_testing"
---
# Testing: GSD DISPLAY Environment Variable Issue

<!-- section_id: "1586062b-b15b-494b-8253-13874f8d6585" -->
## Issue Reference
ISSUE_004 - GSD Daemons Fail After Reboot Due to Missing DISPLAY

<!-- section_id: "8e9e2076-d7dd-4161-a952-81dfcc39fe96" -->
## Date
2026-01-26

<!-- section_id: "23d19520-ba73-4d5c-b393-5047a7f36a87" -->
## Test Performed
Verified gsd-keepalive.timer and service status after system reboot.

<!-- section_id: "22cafefb-31ee-4690-a108-a9727edaded0" -->
## Test Commands
```bash
# Check timer status
systemctl --user status gsd-keepalive.timer

# Check if daemons are running
pgrep -a gsd-media-keys
pgrep -a gsd-power

# Check service status
systemctl --user status gsd-keepalive.service
```

<!-- section_id: "92eb8a7b-1a29-4de3-bead-b68a1cbc581c" -->
## Results

<!-- section_id: "95265f3c-01b2-41d4-a2d3-45fcc48fc015" -->
### Timer Status
- **Status**: Active (running)
- **Trigger**: Shows "n/a" - timer triggered but service completed

<!-- section_id: "dae9efd1-1818-45a7-b6c9-3770959cf5ba" -->
### Daemon Status
- **gsd-media-keys**: NOT RUNNING (pgrep returned exit code 1)
- **gsd-power**: NOT RUNNING (pgrep returned exit code 1)

<!-- section_id: "79bc2290-f858-4394-8784-dd554391ba34" -->
### Service Logs
```
Jan 26 15:06:38 dawson-Yoga-Pro-9-16IMH9 bash[12205]: Cannot open display:
Jan 26 15:06:38 dawson-Yoga-Pro-9-16IMH9 bash[12204]: Cannot open display:
```

<!-- section_id: "5e593971-8ba8-476f-bc1a-e49c8782d066" -->
## Conclusion
The gsd-keepalive.service runs successfully (exit code 0) but the daemons it spawns immediately fail because they cannot connect to the X11 display server. The service lacks the DISPLAY environment variable.

<!-- section_id: "03187ca0-bff9-4501-8710-3ecd2e61a3bc" -->
## User Impact
- Volume buttons not working after reboot
- Brightness buttons not working after reboot
- Requires manual intervention each boot
