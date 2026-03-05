---
resource_id: "a5e5f931-7460-47fb-b1e4-9b81ce25ca13"
resource_type: "document"
resource_name: "CHECKLIST"
---
# Claude in Chrome WSL Bridge Setup Checklist

<!-- section_id: "6daed91d-87e3-456d-9aa8-c91e73c98a4e" -->
## WSL Setup (Complete ✓)

- [x] Claude Code CLI installed
- [x] Native messaging host exists (`~/.claude/chrome/chrome-native-host`)
- [x] WSL wrapper script created (`~/bin/claude-chrome-host.sh`)
- [x] Wrapper script is executable
- [x] Verification script created
- [x] All documentation written

**Verify:** Run `~/bin/verify-claude-chrome-setup.sh`

---

<!-- section_id: "e29575b6-a54e-4dd8-a38c-165fd560a6f1" -->
## Windows Setup (User Action Required)

<!-- section_id: "10da98a7-023a-458a-a687-2439c81949d7" -->
### 1. Get Extension ID

- [ ] Open Chrome
- [ ] Go to `chrome://extensions/`
- [ ] Enable "Developer mode" (top-right toggle)
- [ ] Find "Claude in Chrome" extension
- [ ] Copy the extension ID (32-character string)

**Extension ID:** `____________________________________`

<!-- section_id: "b0b24c31-9505-43f8-8656-584e4f9d3c27" -->
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

<!-- section_id: "c1e8b923-cbe1-43d7-90ec-a60e3bfaa839" -->
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

<!-- section_id: "4a54b8f5-8bc8-4eaa-b36f-c860b9484ee7" -->
### 4. Restart Chrome

- [ ] Close ALL Chrome windows (check system tray)
- [ ] Reopen Chrome
- [ ] Verify extension is still enabled

<!-- section_id: "cab8641e-cf79-46f1-b765-1ccc9a858fa6" -->
### 5. Test Connection

- [ ] Open Chrome
- [ ] Click Claude in Chrome extension icon
- [ ] Try using the extension
- [ ] Check for errors in DevTools console (F12)

---

<!-- section_id: "a90ff27d-1486-4a33-b919-d9657478fdee" -->
## Testing Checklist

<!-- section_id: "426ca6d7-477a-4d34-b46c-4e8a15c47e81" -->
### Basic Tests

- [ ] Extension opens without errors
- [ ] Can send a simple message
- [ ] Response is received
- [ ] No console errors in Chrome

<!-- section_id: "815d5e8d-e512-493d-b355-91baffc288ea" -->
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

<!-- section_id: "5df044c3-42bb-4dbd-9cd6-8f0e4607e903" -->
## Troubleshooting Checklist

<!-- section_id: "edbfbbd7-55f3-42c0-833a-a83b61ee1b87" -->
### "Native messaging host not found"

- [ ] Verify manifest exists
- [ ] Check extension ID matches
- [ ] Verify batch script path is correct
- [ ] Restart Chrome completely

<!-- section_id: "8bf81413-b5bf-45b6-b6e9-bd578a24ae02" -->
### "Access denied" or permission errors

- [ ] Check batch script permissions
- [ ] Run PowerShell as Administrator
- [ ] Check Windows Defender/antivirus

<!-- section_id: "a3449037-8688-4877-a7ba-ffd15ba28827" -->
### Native host starts but doesn't respond

- [ ] Enable debug logging
- [ ] Check logs for errors
- [ ] Test WSL wrapper manually
- [ ] Verify Claude Code authentication

<!-- section_id: "bb203bf9-6737-483d-a96b-af56f56b5eda" -->
### Other issues

- [ ] See BATCH_BRIDGE_SETUP.md troubleshooting section
- [ ] Check WSL is running: `wsl.exe --list --running`
- [ ] Verify paths are correct for your username

---

<!-- section_id: "8a46bc38-e536-4d64-9263-523bd324e209" -->
## Quick Commands Reference

<!-- section_id: "dee66b4d-cc59-4189-a34f-0a12d313ba57" -->
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

<!-- section_id: "83cc3999-7219-4a38-b898-5740e5ebb89c" -->
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

<!-- section_id: "aa32aba4-0f55-440a-803a-2ba1f9b150ed" -->
## Documentation Reference

| File | Purpose | When to Use |
|------|---------|-------------|
| **README.md** | Overview | Start here |
| **QUICK_SETUP.md** | 5-minute setup | Fast setup |
| **BATCH_BRIDGE_SETUP.md** | Complete guide | Detailed info |
| **CHECKLIST.md** | This file | Track progress |
| **IMPLEMENTATION_SUMMARY.md** | Technical details | Understand how it works |

---

<!-- section_id: "4456da6f-9b1f-4c77-aef5-b5625f7d6ba4" -->
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
