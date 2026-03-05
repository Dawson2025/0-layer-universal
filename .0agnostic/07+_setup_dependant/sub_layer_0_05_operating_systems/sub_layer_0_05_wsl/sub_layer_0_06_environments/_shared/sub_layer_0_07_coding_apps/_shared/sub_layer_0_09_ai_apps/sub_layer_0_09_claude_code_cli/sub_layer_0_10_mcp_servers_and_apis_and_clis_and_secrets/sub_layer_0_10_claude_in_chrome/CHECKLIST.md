---
resource_id: "18be160c-5e45-4593-8098-24ef7745e9cb"
resource_type: "document"
resource_name: "CHECKLIST"
---
# Claude in Chrome WSL Bridge Setup Checklist

<!-- section_id: "a0347a5b-7d45-4838-a16e-8320608340d1" -->
## WSL Setup (Complete ✓)

- [x] Claude Code CLI installed
- [x] Native messaging host exists (`~/.claude/chrome/chrome-native-host`)
- [x] WSL wrapper script created (`~/bin/claude-chrome-host.sh`)
- [x] Wrapper script is executable
- [x] Verification script created
- [x] All documentation written

**Verify:** Run `~/bin/verify-claude-chrome-setup.sh`

---

<!-- section_id: "d81f1b21-70fd-4f6f-8d92-9a880b06ac71" -->
## Windows Setup (User Action Required)

<!-- section_id: "eeafcede-75da-4bea-b565-a2c2319fd613" -->
### 1. Get Extension ID

- [ ] Open Chrome
- [ ] Go to `chrome://extensions/`
- [ ] Enable "Developer mode" (top-right toggle)
- [ ] Find "Claude in Chrome" extension
- [ ] Copy the extension ID (32-character string)

**Extension ID:** `____________________________________`

<!-- section_id: "1d7d9dcb-e369-4e11-a73e-fa5d12720dc9" -->
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

<!-- section_id: "a452ad97-8af9-4ffb-9d96-67fa700e55cf" -->
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

<!-- section_id: "1eec25bc-043d-410a-bb1d-0b159b11b48a" -->
### 4. Restart Chrome

- [ ] Close ALL Chrome windows (check system tray)
- [ ] Reopen Chrome
- [ ] Verify extension is still enabled

<!-- section_id: "da4a9b4b-b07a-483c-b277-1177e235cd94" -->
### 5. Test Connection

- [ ] Open Chrome
- [ ] Click Claude in Chrome extension icon
- [ ] Try using the extension
- [ ] Check for errors in DevTools console (F12)

---

<!-- section_id: "4018a12d-2edc-4efd-8a9c-81c430c4bfdb" -->
## Testing Checklist

<!-- section_id: "3bbfec32-2f6b-4e29-9559-fbf45930831e" -->
### Basic Tests

- [ ] Extension opens without errors
- [ ] Can send a simple message
- [ ] Response is received
- [ ] No console errors in Chrome

<!-- section_id: "0f2f4bf0-f853-4043-b957-a25c868de30f" -->
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

<!-- section_id: "39170a3f-a1f9-49bd-ad7b-5bd2b3deebcd" -->
## Troubleshooting Checklist

<!-- section_id: "36b9105d-77b4-4abd-9108-11f9db7e26ca" -->
### "Native messaging host not found"

- [ ] Verify manifest exists
- [ ] Check extension ID matches
- [ ] Verify batch script path is correct
- [ ] Restart Chrome completely

<!-- section_id: "37eac5f1-ad5a-4949-90de-8692df4e1d7a" -->
### "Access denied" or permission errors

- [ ] Check batch script permissions
- [ ] Run PowerShell as Administrator
- [ ] Check Windows Defender/antivirus

<!-- section_id: "38a4c3ab-e154-44ac-ae68-ef97cca9b59c" -->
### Native host starts but doesn't respond

- [ ] Enable debug logging
- [ ] Check logs for errors
- [ ] Test WSL wrapper manually
- [ ] Verify Claude Code authentication

<!-- section_id: "70d2d89c-70f5-44c8-89d4-a1629530191b" -->
### Other issues

- [ ] See BATCH_BRIDGE_SETUP.md troubleshooting section
- [ ] Check WSL is running: `wsl.exe --list --running`
- [ ] Verify paths are correct for your username

---

<!-- section_id: "3533c06a-ede8-434e-9196-907b2aa523de" -->
## Quick Commands Reference

<!-- section_id: "82b2e435-45d8-4841-9835-0f778d93c830" -->
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

<!-- section_id: "3c9402c7-484c-4ace-a903-ada5bdebf8ca" -->
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

<!-- section_id: "6382d54e-d00b-4d2f-a0cb-67f263c904c7" -->
## Documentation Reference

| File | Purpose | When to Use |
|------|---------|-------------|
| **README.md** | Overview | Start here |
| **QUICK_SETUP.md** | 5-minute setup | Fast setup |
| **BATCH_BRIDGE_SETUP.md** | Complete guide | Detailed info |
| **CHECKLIST.md** | This file | Track progress |
| **IMPLEMENTATION_SUMMARY.md** | Technical details | Understand how it works |

---

<!-- section_id: "1b409c44-69a1-4d6d-a980-0ed021758a67" -->
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
