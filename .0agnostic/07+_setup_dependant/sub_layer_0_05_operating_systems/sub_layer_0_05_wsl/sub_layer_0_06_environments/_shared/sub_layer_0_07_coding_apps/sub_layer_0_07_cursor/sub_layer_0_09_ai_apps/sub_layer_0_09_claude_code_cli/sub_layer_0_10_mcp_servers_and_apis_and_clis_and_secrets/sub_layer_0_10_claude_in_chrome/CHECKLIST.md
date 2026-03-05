---
resource_id: "dd6240c8-078e-45c5-8278-3819cd14cdf9"
resource_type: "document"
resource_name: "CHECKLIST"
---
# Claude in Chrome WSL Bridge Setup Checklist

<!-- section_id: "0ffa4586-d528-4b13-aa79-4569e72fbc71" -->
## WSL Setup (Complete ✓)

- [x] Claude Code CLI installed
- [x] Native messaging host exists (`~/.claude/chrome/chrome-native-host`)
- [x] WSL wrapper script created (`~/bin/claude-chrome-host.sh`)
- [x] Wrapper script is executable
- [x] Verification script created
- [x] All documentation written

**Verify:** Run `~/bin/verify-claude-chrome-setup.sh`

---

<!-- section_id: "492ce609-ff1d-4a02-a92f-2e7b539edb66" -->
## Windows Setup (User Action Required)

<!-- section_id: "fee6afa1-7bea-4f04-9d69-31f2552dfdec" -->
### 1. Get Extension ID

- [ ] Open Chrome
- [ ] Go to `chrome://extensions/`
- [ ] Enable "Developer mode" (top-right toggle)
- [ ] Find "Claude in Chrome" extension
- [ ] Copy the extension ID (32-character string)

**Extension ID:** `____________________________________`

<!-- section_id: "9940685f-0d89-4df4-b2dd-5af2406b0b80" -->
### 2. Create Batch Script

- [ ] Open PowerShell as Administrator
- [ ] Run:
  ```powershell
  New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\bin"
  
  @"
  @echo off
  wsl.exe -e /home/dawson/bin/claude-chrome-host.sh
  "@ | Out-File -FilePath "$env:USERPROFILE\bin\claude-chrome-host.bat" -Encoding ASCII
  ```
- [ ] Verify file exists:
  ```powershell
  Test-Path "$env:USERPROFILE\bin\claude-chrome-host.bat"
  ```

<!-- section_id: "94eca003-88ea-4151-acfc-8a6f56d418fb" -->
### 3. Create Native Messaging Manifest

- [ ] Replace `YOUR_EXTENSION_ID` below with actual ID
- [ ] Run in PowerShell:
  ```powershell
  $extensionId = "YOUR_EXTENSION_ID"
  $chromeDir = "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts"
  New-Item -ItemType Directory -Force -Path $chromeDir
  
  $batchPath = "$env:USERPROFILE\bin\claude-chrome-host.bat".Replace('\', '\\')
  
  @"
  {
    "name": "com.anthropic.claude.chrome",
    "description": "Claude in Chrome native messaging host",
    "path": "$batchPath",
    "type": "stdio",
    "allowed_origins": [
      "chrome-extension://$extensionId/"
    ]
  }
  "@ | Out-File -FilePath "$chromeDir\com.anthropic.claude.chrome.json" -Encoding UTF8
  ```
- [ ] Verify manifest exists:
  ```powershell
  Get-Content "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json"
  ```

<!-- section_id: "2d4b98dd-e188-41c2-bbeb-e10b8908fe17" -->
### 4. Restart Chrome

- [ ] Close ALL Chrome windows (check system tray)
- [ ] Reopen Chrome
- [ ] Verify extension is still enabled

<!-- section_id: "82216a5a-e95a-4c85-9410-7ddf13389d89" -->
### 5. Test Connection

- [ ] Open Chrome
- [ ] Click Claude in Chrome extension icon
- [ ] Try using the extension
- [ ] Check for errors in DevTools console (F12)

---

<!-- section_id: "1a666771-1832-4e26-b604-c3547b4f42e5" -->
## Testing Checklist

<!-- section_id: "a80421b9-da92-450f-bf63-dfe6de30de22" -->
### Basic Tests

- [ ] Extension opens without errors
- [ ] Can send a simple message
- [ ] Response is received
- [ ] No console errors in Chrome

<!-- section_id: "c7ddb200-3f83-4ba5-b472-fc5e033bccc0" -->
### Debug Tests (If Issues)

- [ ] Enable logging in `~/bin/claude-chrome-host.sh`
- [ ] Monitor logs: `tail -f ~/claude-chrome-host.log`
- [ ] Test batch script manually:
  ```powershell
  & "$env:USERPROFILE\bin\claude-chrome-host.bat"
  ```
- [ ] Check manifest path in Chrome:
  ```powershell
  Get-Content "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json"
  ```

---

<!-- section_id: "e9b17b1e-178e-406a-9779-984f8c7deb33" -->
## Troubleshooting Checklist

<!-- section_id: "b1bd6df4-ad6e-477c-8327-5841f83f5e53" -->
### "Native messaging host not found"

- [ ] Verify manifest exists
- [ ] Check extension ID matches
- [ ] Verify batch script path is correct
- [ ] Restart Chrome completely

<!-- section_id: "45d3806d-df4e-405c-9dbf-5174a3e9dec8" -->
### "Access denied" or permission errors

- [ ] Check batch script permissions
- [ ] Run PowerShell as Administrator
- [ ] Check Windows Defender/antivirus

<!-- section_id: "9b130f91-a7b5-4c8d-9378-12828d322408" -->
### Native host starts but doesn't respond

- [ ] Enable debug logging
- [ ] Check logs for errors
- [ ] Test WSL wrapper manually
- [ ] Verify Claude Code authentication

<!-- section_id: "828a29e9-3fbd-4f6b-bc66-5fc7afae68a3" -->
### Other issues

- [ ] See BATCH_BRIDGE_SETUP.md troubleshooting section
- [ ] Check WSL is running: `wsl.exe --list --running`
- [ ] Verify paths are correct for your username

---

<!-- section_id: "41e6b9f7-b5f3-4dc9-ac7c-043ba18dc04d" -->
## Quick Commands Reference

<!-- section_id: "ed6a358f-7087-45d2-8488-c813890cc7af" -->
### WSL

```bash
# Verify setup
~/bin/verify-claude-chrome-setup.sh

# Test wrapper
~/bin/claude-chrome-host.sh

# Enable logging
nano ~/bin/claude-chrome-host.sh
# Uncomment logging lines

# View logs
tail -f ~/claude-chrome-host.log

# Test native host
~/.claude/chrome/chrome-native-host
```

<!-- section_id: "3ef534d2-9fbf-48d6-8e4c-f2e22b483acb" -->
### Windows (PowerShell)

```powershell
# Check manifest
Get-Content "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json"

# Test batch script
& "$env:USERPROFILE\bin\claude-chrome-host.bat"

# Verify files
Test-Path "$env:USERPROFILE\bin\claude-chrome-host.bat"

# Check WSL
wsl.exe --list --running
wsl.exe -e /home/dawson/bin/claude-chrome-host.sh
```

---

<!-- section_id: "c976734a-9f1d-4a47-ba07-5b5b3c127cd7" -->
## Documentation Reference

| File | Purpose | When to Use |
|------|---------|-------------|
| **README.md** | Overview | Start here |
| **QUICK_SETUP.md** | 5-minute setup | Fast setup |
| **BATCH_BRIDGE_SETUP.md** | Complete guide | Detailed info |
| **CHECKLIST.md** | This file | Track progress |
| **IMPLEMENTATION_SUMMARY.md** | Technical details | Understand how it works |

---

<!-- section_id: "ba74ee2e-d551-429d-8230-8050639c60ac" -->
## Success!

When everything is working, you should see:

- ✓ Chrome extension opens without errors
- ✓ Can send messages to Claude Code
- ✓ Responses appear correctly
- ✓ No errors in Chrome DevTools console
- ✓ No errors in WSL logs (if enabled)

**Status:** Setup complete! 🎉

---

**Last Updated:** 2025-12-30  
**Version:** 1.0
