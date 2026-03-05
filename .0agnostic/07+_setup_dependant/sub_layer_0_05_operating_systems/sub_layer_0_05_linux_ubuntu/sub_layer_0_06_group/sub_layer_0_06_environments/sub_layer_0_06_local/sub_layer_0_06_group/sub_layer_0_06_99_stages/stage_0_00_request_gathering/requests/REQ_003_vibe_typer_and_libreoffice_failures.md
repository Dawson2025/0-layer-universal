---
resource_id: "3775ad33-89a8-420f-8bd4-d9e3d1ed60b4"
resource_type: "document"
resource_name: "REQ_003_vibe_typer_and_libreoffice_failures"
---
# REQ_003: Vibe-Typer and LibreOffice Application Failures

**Date Reported**: 2026-01-29
**Status**: Active investigation
**Severity**: High (blocks recording and document editing workflows)

---

<!-- section_id: "44e45ea6-58dc-49e4-a219-c7e17cdbdf6b" -->
## Problem Statement

<!-- section_id: "398ace83-cb54-497d-a823-12dead0989dd" -->
### Issue 1: Vibe-Typer Timeout
- **Symptom**: Vibe-typer app fails to start, times out waiting for audio renderer
- **Error**: "Timed out waiting for the audio renderer to become ready"
- **Impact**: Cannot use vibe-typer for any recording

<!-- section_id: "92b7b2a2-5a35-4fcb-b137-8c186c8e8337" -->
### Issue 2: LibreOffice Won't Open
- **Symptom**: LibreOffice app won't launch
- **Related**: xdg-desktop-portal service crashed
- **Impact**: Cannot open or edit documents

---

<!-- section_id: "a25df7a9-46dc-4eeb-ac26-b8635335622c" -->
## Context

<!-- section_id: "0d162914-a072-4427-97d1-1b9c4ff02d3b" -->
### Recent Changes
- Audio system was recently fixed (REQ_001, REQ_002):
  - Subwoofer enabled via I2C bypass
  - EasyEffects "Yoga Pro 9i Official" preset active
  - WirePlumber crash fixed
  - TAS2781 driver blacklisted

- Portal services were previously fixed (ISSUE_005):
  - xdg-desktop-portal-gnome had SEGFAULT
  - Switched to GTK backend
  - Created autostart script `fix-portal-services.desktop`

<!-- section_id: "85e0cbe2-09a7-4af9-97c4-7cecf2d431ef" -->
### Current System State
- **Date**: 2026-01-29 18:30+ MST
- **Uptime**: 3+ days since last reboot
- **Machine**: Lenovo Yoga Pro 9 16IMH9

---

<!-- section_id: "be46754d-b8ea-4fcf-9c28-1a9615735cc4" -->
## Diagnostic Findings

<!-- section_id: "146e5aae-d189-449c-ac72-22349fb1157c" -->
### Issue 1: Audio Renderer Timeout

**PipeWire Status**:
```
Service: Active (running)
PID: 2732
Uptime: Jan 26 15:06:19 (3+ days)
```

**Audio Errors in Journal**:
```
spa.alsa: set_hw_params: Invalid argument
pw.node: (...skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink-63)
  suspended -> error (Start error: Invalid argument)
```

**Repeated every 5 seconds since at least 2026-01-29 18:08:38**

**Audio Devices**:
```
Card 0: sofhdadsp (Lenovo Yoga Pro 9 16IMH9 speakers + subwoofer)
Default Sink: alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink
Default Source: alsa_input.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp_6__source
```

**PipeWire Protocol**: PulseAudio on PipeWire 1.0.5 (compatibility mode)

**Active Audio Configuration**:
- EasyEffects running (not as service, but likely autostarted)
- Preset: "Yoga Pro 9i Official" (complex EQ with 22 bands)
- Filter-chain audio processing active

**Recent Attempts**:
- Restarted PipeWire service: `systemctl --user restart pipewire pipewire-pulse wireplumber`
- Result: No change, errors persist

<!-- section_id: "0ba01409-6525-4b9a-be96-35e1e0a686bd" -->
### Issue 2: Portal Service Crash

**xdg-desktop-portal Status**:
```
Status: Failed (Result: signal - killed with SIGKILL)
Last Start: 2026-01-28 09:50:23
Last Failed: 2026-01-28 09:51:53 (timeout)
Uptime: N/A (keeps crashing)
```

**Portal Error Messages**:
```
Failed to create settings proxy:
  Error calling StartServiceByName for org.freedesktop.impl.portal.desktop.gtk:
  Timeout was reached

Failed to create file chooser proxy:
  Timeout was reached

xdg-desktop-portal.service: start operation timed out. Terminating.
```

**Portal Backends Status**:
- `xdg-desktop-portal-gtk`: Running (PID 1994300)
- `xdg-desktop-portal`: Running (PID 1994423)
- Service systemd unit: Failed (but processes running)

**Recent Attempts**:
- Manually restarted service: `systemctl --user restart xdg-desktop-portal.service`
- Manually started GTK backend: `/usr/libexec/xdg-desktop-portal-gtk &`
- Result: Processes running but systemd service still fails, LibreOffice still won't open

**Related Documentation**:
- Previous portal issue fixed: `ISSUE_005_portal_apps_final_config.md`
- Autostart script: `~/.local/bin/fix-portal-services.sh`
- D-Bus overrides: `~/.config/systemd/user/xdg-desktop-portal.service.d/override.conf`

---

<!-- section_id: "1cd4a1d5-651d-4840-8529-bce725f48229" -->
## Hypothesis

<!-- section_id: "d158a08b-95b6-4347-92ed-e99fd66eab3d" -->
### Vibe-Typer Issue
The audio renderer timeout is likely caused by:
1. **PipeWire hardware initialization failure** - ALSA layer can't set hardware parameters
2. **EasyEffects filter-chain blocking** - Complex EQ preset might be consuming resources
3. **SOF firmware issue** - `sof-hda-dsp` may need firmware reload
4. **Sample rate mismatch** - Pipeline configured for 48kHz but hardware doesn't support

Root cause: The "Invalid argument" error from ALSA suggests either:
- Hardware is in an unknown state (needs reboot)
- EasyEffects config is invalid for current hardware state
- Firmware needs reloading

<!-- section_id: "c2b7ef53-4f43-4333-af3d-578f5f66686a" -->
### LibreOffice Issue
The portal timeout suggests:
1. **GTK portal taking too long to initialize** - 50+ second timeout before failure
2. **D-Bus communication issue** - Can't reach implementation portal
3. **GNOME integration broken** - Portal trying to use GNOME backend when it should use GTK
4. **Service dependency loop** - Portal waiting for something that's waiting for portal

Root cause: Even though processes are running, systemd service fails to fully initialize, blocking LibreOffice from connecting.

---

<!-- section_id: "3c24060b-dd0f-4172-b811-64739f732f2c" -->
## Questions for Investigation

<!-- section_id: "abea001b-7c6a-43fb-9e97-9877a5399bfe" -->
### Audio
1. Has vibe-typer ever worked on this system, or is this first time trying?
2. When was the last successful recording attempt?
3. Did audio quality fixes (I2C, EasyEffects) introduce this, or was it pre-existing?

<!-- section_id: "7b4af262-eb6e-4c4e-9e6c-3b2c3c780fef" -->
### Portal
1. When did LibreOffice last work?
2. Does other portal-dependent app (Files, Settings) work?
3. Is the `fix-portal-services.desktop` autostart still running?

<!-- section_id: "e65a5a4f-80bb-4408-a814-fcc0ade8a5eb" -->
### System
1. When was the last successful reboot?
2. Any recent kernel updates or audio driver changes?
3. Is this the intended steady state or degraded?

---

<!-- section_id: "01d9be91-1f54-45c6-8171-d1a28eb01b5c" -->
## Next Steps

<!-- section_id: "86caea7c-4e8b-412d-a2f5-2019c4104917" -->
### Immediate (Quick Fixes)
- [ ] Try full reboot - clears transient state
- [ ] Check if `fix-portal-services.desktop` autostart is enabled
- [ ] Disable EasyEffects temporarily - test if audio works without processing

<!-- section_id: "ba39976b-9020-42ad-abac-6dbed6bdc7fd" -->
### Investigation
- [ ] Review PipeWire logs for ALSA/SOF firmware errors
- [ ] Check systemd user journal for portal initialization sequence
- [ ] List all D-Bus services (check for timeouts)
- [ ] Test direct ALSA recording (bypass PipeWire)

<!-- section_id: "eb341ddc-ff7b-4d3c-9466-da65b6644675" -->
### Resolution
- [ ] Fix ALSA hardware parameter issue (may require firmware reload)
- [ ] Fix portal D-Bus dependency chain
- [ ] Test both vibe-typer and LibreOffice after fixes

---

<!-- section_id: "bab2e938-aaf8-4c00-8d3b-feeb3cea1832" -->
## Related Issues

| Issue | Status | Location |
|-------|--------|----------|
| REQ_001 | Resolved | `stage_0_09_current_product/outputs/REQ_001_audio_final_config.md` |
| REQ_002 | Resolved | `stage_0_09_current_product/outputs/REQ_002_yoga_speaker_final_config.md` |
| ISSUE_005 | Resolved | `stage_0_09_current_product/outputs/ISSUE_005_portal_apps_final_config.md` |
| REQ_003 | **Active** | **← Current investigation** |

---

<!-- section_id: "c6449961-0267-4790-8837-75d1c5fb1d55" -->
## Timeline

| Date | Event |
|------|-------|
| 2026-01-25 | REQ_001: Audio quality issues reported |
| 2026-01-26 | REQ_001, REQ_002, ISSUE_005 all fixed |
| 2026-01-26 | gsd-keepalive timer and portal fix autostart deployed |
| 2026-01-28 | xdg-desktop-portal service crashed (timeout during init) |
| 2026-01-29 | User attempts to use vibe-typer - times out |
| 2026-01-29 | LibreOffice won't open - portal is unresponsive |
| 2026-01-29 | **Current: Investigation begins** |
