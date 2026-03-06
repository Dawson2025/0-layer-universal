---
resource_id: "c3d4e5f6-a7b8-9012-cdef-234567890123"
resource_type: "output"
resource_name: "requirements_tree"
---
# GSD Session Startup — Requirements Tree

<!-- section_id: "f6a7b8c9-d0e1-2f3a-4b5c-6d7e8f9a0b1c" -->
## Root Requirement

**GSD daemons must start reliably after every reboot without manual intervention.**

```
GSD daemons start reliably after every reboot
├── R1: gsd-media-keys must be running
│   ├── R1.1: Custom keybindings must work (Ctrl+Alt+S speak-selection)
│   ├── R1.2: Must register on D-Bus as org.gnome.SettingsDaemon.MediaKeys
│   └── R1.3: Must not conflict with GNOME's own failed service instance
│
├── R2: gsd-power must be running
│   ├── R2.1: Brightness hardware keys must change screen brightness
│   ├── R2.2: Brightness OSD must appear in screen corner
│   ├── R2.3: Power management features must work
│   └── R2.4: Must register on D-Bus as org.gnome.SettingsDaemon.Power
│
├── R3: DISPLAY must be available in systemd user environment before services start
│   ├── R3.1: systemctl --user import-environment DISPLAY XAUTHORITY must run before gsd targets
│   ├── R3.2: Must work with Unity session startup sequence (XDG_CURRENT_DESKTOP=Unity)
│   └── R3.3: Must not depend on hardcoded DISPLAY=:0 (fragile assumption)
│
├── R4: No ~5 min dead zone after boot
│   ├── R4.1: Daemons must be running within 30 seconds of login
│   ├── R4.2: Must not require waiting for D-Bus name timeout/release
│   └── R4.3: GNOME's failed service state must be cleared before restart attempt
│
├── R5: No multi-instance spawning
│   ├── R5.1: Only one gsd-media-keys process at a time
│   ├── R5.2: Only one gsd-power process at a time
│   └── R5.3: Must handle race condition between process check and startup
│
├── R6: Errors must be visible (not suppressed)
│   ├── R6.1: Startup failures must appear in journal
│   ├── R6.2: No 2>/dev/null on daemon startup commands
│   └── R6.3: Keepalive service should log success/failure for each attempt
│
└── NOT in scope
    └── Volume keys — handled by custom volume-control.sh script, NOT dependent on gsd
```

<!-- section_id: "a7b8c9d0-e1f2-3a4b-5c6d-7e8f9a0b1c2d" -->
## Priority

| Requirement | Priority | Impact |
|-------------|----------|--------|
| R3 (DISPLAY env) | Critical | Root cause — fixes everything |
| R4 (No dead zone) | High | 5 min of broken keybindings every boot |
| R1 (gsd-media-keys) | High | Custom keybindings (speak-selection) |
| R2 (gsd-power) | High | Brightness keys, power management |
| R5 (No multi-instance) | Medium | Stability issue |
| R6 (Visible errors) | Medium | Debugging/maintenance |

<!-- section_id: "b8c9d0e1-f2a3-4b5c-6d7e-8f9a0b1c2d3e" -->
## Acceptance Criteria

The fix is considered complete when:
1. After a fresh reboot, all custom keybindings work within 30 seconds of desktop appearing
2. Brightness keys change brightness and OSD appears
3. No manual intervention required
4. No duplicate daemon processes
5. Journal shows clean startup (no "Cannot open display:" errors)
6. The keepalive timer becomes a safety net, not a necessity
