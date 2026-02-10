# REQ_003: Vibe-Typer and LibreOffice Application Failures

**Date Reported**: 2026-01-29
**Status**: Active investigation
**Severity**: High (blocks recording and document editing workflows)

---

## Problem Statement

### Issue 1: Vibe-Typer Timeout
- **Symptom**: Vibe-typer app fails to start, times out waiting for audio renderer
- **Error**: "Timed out waiting for the audio renderer to become ready"
- **Impact**: Cannot use vibe-typer for any recording

### Issue 2: LibreOffice Won't Open
- **Symptom**: LibreOffice app won't launch
- **Related**: xdg-desktop-portal service crashed
- **Impact**: Cannot open or edit documents

---

## Context

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

### Current System State
- **Date**: 2026-01-29 18:30+ MST
- **Uptime**: 3+ days since last reboot
- **Machine**: Lenovo Yoga Pro 9 16IMH9

---

## Diagnostic Findings

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

## Hypothesis

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

### LibreOffice Issue
The portal timeout suggests:
1. **GTK portal taking too long to initialize** - 50+ second timeout before failure
2. **D-Bus communication issue** - Can't reach implementation portal
3. **GNOME integration broken** - Portal trying to use GNOME backend when it should use GTK
4. **Service dependency loop** - Portal waiting for something that's waiting for portal

Root cause: Even though processes are running, systemd service fails to fully initialize, blocking LibreOffice from connecting.

---

## Questions for Investigation

### Audio
1. Has vibe-typer ever worked on this system, or is this first time trying?
2. When was the last successful recording attempt?
3. Did audio quality fixes (I2C, EasyEffects) introduce this, or was it pre-existing?

### Portal
1. When did LibreOffice last work?
2. Does other portal-dependent app (Files, Settings) work?
3. Is the `fix-portal-services.desktop` autostart still running?

### System
1. When was the last successful reboot?
2. Any recent kernel updates or audio driver changes?
3. Is this the intended steady state or degraded?

---

## Next Steps

### Immediate (Quick Fixes)
- [ ] Try full reboot - clears transient state
- [ ] Check if `fix-portal-services.desktop` autostart is enabled
- [ ] Disable EasyEffects temporarily - test if audio works without processing

### Investigation
- [ ] Review PipeWire logs for ALSA/SOF firmware errors
- [ ] Check systemd user journal for portal initialization sequence
- [ ] List all D-Bus services (check for timeouts)
- [ ] Test direct ALSA recording (bypass PipeWire)

### Resolution
- [ ] Fix ALSA hardware parameter issue (may require firmware reload)
- [ ] Fix portal D-Bus dependency chain
- [ ] Test both vibe-typer and LibreOffice after fixes

---

## Related Issues

| Issue | Status | Location |
|-------|--------|----------|
| REQ_001 | Resolved | `stage_0_09_current_product/outputs/REQ_001_audio_final_config.md` |
| REQ_002 | Resolved | `stage_0_09_current_product/outputs/REQ_002_yoga_speaker_final_config.md` |
| ISSUE_005 | Resolved | `stage_0_09_current_product/outputs/ISSUE_005_portal_apps_final_config.md` |
| REQ_003 | **Active** | **← Current investigation** |

---

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
