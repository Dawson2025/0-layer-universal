---
resource_id: "93207d9c-f2b0-4ab1-ae8c-292ca4a73a11"
resource_type: "output"
resource_name: "requirements_tree"
---

<!-- section_id: "b8d8ec5b-40fb-4681-a46e-edc2559d26c4" -->
## Parent Requirements Reference

This tree details the requirements for the **GSD Session Startup** entity.

- **Parent tree of needs**: `../../../requirements_tree.md` (setup root)
- **This entity addresses parent needs**:
  - **N1** (Desktop Services): R1 (gsd-media-keys) + R2 (gsd-power) ensure desktop daemons run
  - **N4** (Display Server Availability): R3 (DISPLAY env) fixes the root cause

### Completion Triggers
| When | Parent Need Satisfied |
|------|----------------------|
| R3 (DISPLAY env imported before gsd starts) | N4 (Display Server Availability) |
| R1 (gsd-media-keys running) + R2 (gsd-power running) | N1 (Desktop Services) |
| R4 (no dead zone) + R5 (no multi-instance) | N1 quality criteria |

# GSD Session Startup — Requirements Tree

<!-- section_id: "d9ecb963-f8ba-45e3-8a8e-cca286492f28" -->
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
├── R7: ALL gsd services must start reliably (not just MediaKeys/Power)
│   ├── R7.1: gsd-color must be running
│   ├── R7.2: gsd-keyboard must be running
│   └── R7.3: gsd-wacom must be running (even if no tablet — prevents failed state)
│
├── R8: D-Bus-activated apps must launch from toolbar
│   ├── R8.1: Nautilus (Files) must open from taskbar icon
│   ├── R8.2: GNOME Settings must open from taskbar icon
│   ├── R8.3: GNOME Terminal must open from taskbar icon
│   └── R8.4: Other GDK apps (OBS Studio) must open from taskbar icon
│
└── NOT in scope
    └── Volume keys — handled by custom volume-control.sh script, NOT dependent on gsd
```

<!-- section_id: "a2a7a110-8908-49e0-a214-53f64d227c39" -->
## Priority

| Requirement | Priority | Impact |
|-------------|----------|--------|
| R3 (DISPLAY env) | Critical | Root cause — fixes everything |
| R4 (No dead zone) | High | 5 min of broken keybindings every boot |
| R1 (gsd-media-keys) | High | Custom keybindings (speak-selection) |
| R2 (gsd-power) | High | Brightness keys, power management |
| R5 (No multi-instance) | Medium | Stability issue |
| R6 (Visible errors) | Medium | Debugging/maintenance |
| R7 (All gsd services) | High | Color, Keyboard, Wacom also fail from same root cause |
| R8 (Toolbar app launch) | High | Files, Settings, Terminal broken from toolbar |

<!-- section_id: "5e672ab5-221f-47dd-a044-bff75b3429cc" -->
## Acceptance Criteria

The fix is considered complete when:
1. After a fresh reboot, all custom keybindings work within 30 seconds of desktop appearing
2. Brightness keys change brightness and OSD appears
3. No manual intervention required
4. No duplicate daemon processes
5. Journal shows clean startup (no "Cannot open display:" errors)
6. The keepalive timer becomes a safety net, not a necessity
7. All 5 gsd services start reliably (MediaKeys, Power, Color, Keyboard, Wacom)
8. D-Bus-activated apps (Files, Settings, Terminal) launch from toolbar
