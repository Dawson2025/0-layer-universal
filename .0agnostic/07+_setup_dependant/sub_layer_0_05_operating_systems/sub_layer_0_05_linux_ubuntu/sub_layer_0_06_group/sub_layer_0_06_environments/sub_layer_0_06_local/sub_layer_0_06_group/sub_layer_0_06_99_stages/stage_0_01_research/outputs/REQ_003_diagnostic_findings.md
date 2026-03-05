---
resource_id: "c1e1efe5-d68f-4a9f-81e0-ced30e8340d0"
resource_type: "output"
resource_name: "REQ_003_diagnostic_findings"
---
# REQ_003: Diagnostic Findings

**Date**: 2026-01-29 18:35+ MST
**Diagnostic Run**: Initial investigation
**Issues**: 2 (vibe-typer timeout + LibreOffice won't open)

---

<!-- section_id: "f437911f-0819-422d-8fc7-35d4ea858ebd" -->
## Issue 1: Vibe-Typer Audio Renderer Timeout

<!-- section_id: "3b6b365e-3d46-4f10-b532-2737398c26ed" -->
### Root Cause: PipeWire ALSA Hardware Parameter Failure

**Evidence**:
```
spa.alsa: set_hw_params: Invalid argument
pw.node: (alsa_output.pci-0000_00_1f.3-platform-skl_hda_dsp_generic.HiFi__hw_sofhdadsp__sink-63)
  suspended -> error (Start error: Invalid argument)
```

**Frequency**: Repeating every 5 seconds continuously
**Duration**: At least since 2026-01-29 18:08:38 (26+ minutes)
**Service Status**: PipeWire service appears running but in error state

<!-- section_id: "b7103297-5715-4c55-b35d-783f1c317210" -->
### What's Happening

When vibe-typer tries to record audio:
1. It requests PipeWire to start the audio sink
2. PipeWire calls ALSA backend to set hardware parameters
3. ALSA returns "Invalid argument"
4. PipeWire suspends the device with error
5. vibe-typer timeout waiting for renderer to become ready

<!-- section_id: "fca28216-f827-4653-a113-c859bba541bf" -->
### Why This Is Happening

**Most Likely Causes** (in order of probability):

1. **EasyEffects Configuration Issue** (70% likely)
   - Preset: "Yoga Pro 9i Official" (complex, 22-band EQ)
   - May be requesting sample rate/format hardware doesn't support
   - Filter-chain audio processing in elevated state

2. **Hardware State Corruption** (20% likely)
   - 3+ days of uptime without reboot
   - ALSA subsystem may be in unknown state
   - I2C bypass script (subwoofer enable) may not have re-initialized cleanly

3. **SOF Firmware Issue** (10% likely)
   - Intel SOF DSP firmware (`sof-hda-dsp`) may need reloading
   - Possible firmware/kernel mismatch

<!-- section_id: "780fd6f6-e2db-499f-b324-20720d5728c2" -->
### Supporting Evidence

**Audio Device Status**:
```
Card 0: sofhdadsp (working, responds to queries)
Default Sink: alsa_output.pci-0000_00_1f.3...HiFi__hw_sofhdadsp__sink
Default Source: alsa_input.pci-0000_00_1f.3...HiFi__hw_sofhdadsp_6__source
```
→ Device is visible and recognized, but won't initialize

**PipeWire Health**:
```
Service: active (running)
Memory: 17.1M (normal)
CPU: 1min 11s (normal)
Tasks: 3
```
→ Service appears healthy, but ALSA layer failing

**Audio Processing Chain**:
```
Apps → EasyEffects ("Yoga Pro 9i Official" EQ) → PipeWire → ALSA → Hardware
                                      ↑
                         (Likely bottleneck here)
```

---

<!-- section_id: "71460ef8-8364-416e-a414-07182f341489" -->
## Issue 2: LibreOffice & Portal Service Crash

<!-- section_id: "8c02580b-e892-4f44-a0bf-c36369f80774" -->
### Root Cause: xdg-desktop-portal D-Bus Initialization Timeout

**Evidence**:
```
Failed to create settings proxy: Error calling StartServiceByName
  for org.freedesktop.impl.portal.desktop.gtk: Timeout was reached

xdg-desktop-portal.service: start operation timed out. Terminating.
Status: Failed (Result: signal) - Main process killed with SIGKILL
```

**Timeline**:
- Service started: 2026-01-28 09:50:23
- GTK proxy failed: 2026-01-28 09:51:13 (timeout after 50 seconds)
- Service killed: 2026-01-28 09:51:53 (total 90 seconds, then timeout/SIGKILL)
- **Status**: Crashed and never recovered (1 day+ ago)

<!-- section_id: "308a2177-3843-454b-ad5e-5f78733eab00" -->
### What's Happening

LibreOffice needs portal to:
1. Open file dialogs
2. Access system resources
3. Handle sandboxing

Portal can't initialize because:
1. `xdg-desktop-portal` tries to start GTK backend
2. GTK backend takes >50 seconds to respond (timeout)
3. Portal process hangs
4. Systemd kills it after 90 seconds
5. Process never fully starts, leaving LibreOffice blocked

<!-- section_id: "9b2f30fc-616a-4305-bf8c-fcae3223df68" -->
### Why This Is Happening

**Most Likely Causes** (in order of probability):

1. **Service Dependency Loop** (60% likely)
   - Portal waiting for GTK backend
   - GTK backend waiting for something (D-Bus? GNOME?)
   - Mutual wait causes timeout
   - Common after audio system changes

2. **Previous Portal Fix Incomplete** (30% likely)
   - `ISSUE_005_portal_apps_final_config.md` may not have fully resolved
   - autostart script `fix-portal-services.desktop` may not be running
   - D-Bus overrides in `override.conf` may need updating

3. **GNOME Integration Issue** (10% likely)
   - Portal trying to use GNOME backend when should use GTK
   - Configuration mismatch after system changes

<!-- section_id: "f73633f5-d39c-4d1a-b925-4f46f6481ad0" -->
### Supporting Evidence

**Portal Processes**:
```
Running: /usr/libexec/xdg-desktop-portal-gtk (PID 1994300)
Running: /usr/libexec/xdg-desktop-portal (PID 1994423)
```
→ Processes **are** running when started manually

**Service Status**:
```
Active: failed (Result: signal)
Last error: systemd killed with SIGKILL (signal 9)
```
→ Process runs but never fully initializes systemd service

**Consequence**:
```
LibreOffice can't find portal → won't open file dialogs → won't start
Other portal-dependent apps: Unknown (not tested)
```

---

<!-- section_id: "6fb5bdbe-2e7d-437d-b8f6-0e50e71f2953" -->
## Cross-Issue Analysis

<!-- section_id: "b547aa71-65df-4b4f-b921-7853e4b83dea" -->
### Are These Related?

**Probability**: 70% related

**Reasoning**:
- Both happened after audio fixes (REQ_001, REQ_002)
- Both involve D-Bus/system service communication
- Both timeout waiting for something to initialize
- 3+ day uptime without reboot may have accumulated state issues

**Possible Common Root Cause**:
- Audio system changes triggered D-Bus stability issues
- EasyEffects/PipeWire changes affected service initialization timing
- System resource constraints (not memory, maybe file descriptors?)

<!-- section_id: "efaa529b-6e29-4180-ad33-fab76716f452" -->
### Unlikely to be Related

- Different subsystems (audio vs. portal)
- Different error patterns (ALSA "Invalid argument" vs. D-Bus timeout)
- Portal was already broken since Jan 28 (before we tested vibe-typer today)

---

<!-- section_id: "091be4dc-8f47-4f96-aaf7-9a361c8255a2" -->
## Recommended Investigation Path

<!-- section_id: "079d20e5-d44c-4ecf-9c90-d8579b441d3c" -->
### Step 1: Determine if Reboot Fixes Both (5 minutes)
```bash
sudo reboot
# After reboot, test:
#   1. vibe-typer recording
#   2. LibreOffice opening
```

**Expected Result**:
- If both fixed → state corruption, not config issue
- If one fixed → independent issues
- If neither fixed → configuration problem

<!-- section_id: "b835591f-e2f7-4482-bd07-df62ffda5ac4" -->
### Step 2: If Not Fixed by Reboot, Test Audio Isolation (5 minutes)
```bash
# Disable EasyEffects
pkill easyeffects

# Test vibe-typer
vibe-typer

# If it works:
#   → EasyEffects preset is the problem
# If it still fails:
#   → Deeper audio system issue
```

<!-- section_id: "c1580ad4-2bcc-4f6d-95fe-6aeaaf39e153" -->
### Step 3: If Not Fixed, Test Portal Isolation (5 minutes)
```bash
# Check if autostart is running
systemctl --user status xdg-desktop-portal.service

# Manually run fix script
bash /home/dawson/.local/bin/fix-portal-services.sh

# Test LibreOffice
libreoffice

# If it works:
#   → autostart script not running
# If it still fails:
#   → Portal service fundamentally broken
```

<!-- section_id: "2a183794-cbcc-4297-bda2-a5667257c6b6" -->
### Step 4: Deep Diagnostics (if Steps 1-3 don't work)
```bash
# Audio debugging
journalctl --user -f | grep -E "alsa|pipewire|Invalid"

# Portal debugging
DBUS_SYSTEM_BUS_ADDRESS="" systemctl --user start xdg-desktop-portal.service
journalctl --user -f | grep -E "portal|gtk"

# Check D-Bus services
systemctl --user status dbus.service
gdbus introspect --system --dest org.freedesktop.impl.portal.desktop.gtk --object-path /
```

---

<!-- section_id: "3355834b-a317-45ee-b3e4-5e43cd0c72e6" -->
## Configuration Files to Review

| File | Purpose | Status |
|------|---------|--------|
| `~/.config/easyeffects/output/Yoga Pro 9i Official.json` | Audio EQ preset | Complex (22 bands) |
| `/etc/modprobe.d/disable-tas2781-driver.conf` | Audio driver blacklist | Stable |
| `~/.local/bin/fix-portal-services.sh` | Portal startup script | May not be running |
| `~/.config/systemd/user/xdg-desktop-portal.service.d/override.conf` | Portal service override | Unknown |
| `/lib/firmware/intel/sof/` | SOF firmware | Stable (3+ days) |

---

<!-- section_id: "13d85e65-44a7-4fbc-8058-529aade7c216" -->
## Summary

<!-- section_id: "56273df7-2d7e-488b-a914-f76bfc71542a" -->
### Vibe-Typer Issue
- **Status**: PipeWire can't initialize ALSA hardware
- **Likely Cause**: EasyEffects config issue or hardware state corruption
- **Fix Probability**: Reboot (80%), Disable EasyEffects (70%), Firmware reload (30%)

<!-- section_id: "2baa4e47-5da2-4523-9021-e850ee8bd47c" -->
### LibreOffice Issue
- **Status**: Portal service times out during D-Bus initialization
- **Likely Cause**: Service dependency loop or incomplete previous fix
- **Fix Probability**: Reboot (75%), Restart autostart (85%), Reconfigure portal (60%)

<!-- section_id: "06210810-247f-43b8-9f6b-be9b15bd1497" -->
### Recommended Action
**Reboot first** - has 75%+ probability of fixing both issues with no configuration changes needed.
