---
resource_id: "48a66be2-635e-45a3-8f29-dec4e42d8e8d"
resource_type: "document"
resource_name: "CHECKLIST"
---
# Claude in Chrome WSL Bridge Setup Checklist

<!-- section_id: "4d258bfd-5a46-4953-87d2-fd8a6b5f6973" -->
## WSL Setup (Complete ✓)

- [x] Claude Code CLI installed
- [x] Native messaging host exists (`~/.claude/chrome/chrome-native-host`)
- [x] WSL wrapper script created (`~/bin/claude-chrome-host.sh`)
- [x] Wrapper script is executable
- [x] Verification script created
- [x] All documentation written

**Verify:** Run `~/bin/verify-claude-chrome-setup.sh`

---

<!-- section_id: "bf81e728-8f94-4aef-bb80-c5243f51d72d" -->
## Windows Setup (User Action Required)

<!-- section_id: "b3f65362-1769-46bf-af0c-8f5c6b482f87" -->
### 1. Get Extension ID

- [ ] Open Chrome
- [ ] Go to `chrome://extensions/`
- [ ] Enable "Developer mode" (top-right toggle)
- [ ] Find "Claude in Chrome" extension
- [ ] Copy the extension ID (32-character string)

**Extension ID:** `____________________________________`

<!-- section_id: "dc830668-eb45-4aba-9a8f-7a981949b868" -->
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

<!-- section_id: "57df21f2-27d8-4d82-8903-dca0b1da04a0" -->
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

<!-- section_id: "ca7eb3ac-558e-437d-bf5a-5695e14e4d60" -->
### 4. Restart Chrome

- [ ] Close ALL Chrome windows (check system tray)
- [ ] Reopen Chrome
- [ ] Verify extension is still enabled

<!-- section_id: "6b1049cc-ab70-4847-9e44-e70be1788942" -->
### 5. Test Connection

- [ ] Open Chrome
- [ ] Click Claude in Chrome extension icon
- [ ] Try using the extension
- [ ] Check for errors in DevTools console (F12)

---

<!-- section_id: "0b801656-6972-4a2e-add3-8c03199f7a45" -->
## Testing Checklist

<!-- section_id: "f5dfadf0-631f-40ca-87bf-17f7d3461231" -->
### Basic Tests

- [ ] Extension opens without errors
- [ ] Can send a simple message
- [ ] Response is received
- [ ] No console errors in Chrome

<!-- section_id: "b5d04278-ea9c-489c-ac8e-f094744bef1d" -->
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

<!-- section_id: "90534372-2a34-47fe-af2f-2e284498ea69" -->
## Troubleshooting Checklist

<!-- section_id: "14affa83-7aff-45c1-8713-e7014aef0b36" -->
### "Native messaging host not found"

- [ ] Verify manifest exists
- [ ] Check extension ID matches
- [ ] Verify batch script path is correct
- [ ] Restart Chrome completely

<!-- section_id: "fe86f53e-8465-4194-87e6-ce39ee51f7ff" -->
### "Access denied" or permission errors

- [ ] Check batch script permissions
- [ ] Run PowerShell as Administrator
- [ ] Check Windows Defender/antivirus

<!-- section_id: "51cf1c18-a338-4933-8535-823d92292a3e" -->
### Native host starts but doesn't respond

- [ ] Enable debug logging
- [ ] Check logs for errors
- [ ] Test WSL wrapper manually
- [ ] Verify Claude Code authentication

<!-- section_id: "ec03d641-2321-47d6-9753-e5e481f6b352" -->
### Other issues

- [ ] See BATCH_BRIDGE_SETUP.md troubleshooting section
- [ ] Check WSL is running: `wsl.exe --list --running`
- [ ] Verify paths are correct for your username

---

<!-- section_id: "98fb2b5b-840c-48a3-a5f5-44043f81bb46" -->
## Quick Commands Reference

<!-- section_id: "ec8f7ac6-9460-433e-83b4-ecf2dab16e6b" -->
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

<!-- section_id: "1ab914da-44d1-4dcb-97b1-d71ac83ad143" -->
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

<!-- section_id: "2a991f4a-3dfd-4a7e-bdca-aca94cd32171" -->
## Documentation Reference

| File | Purpose | When to Use |
|------|---------|-------------|
| **README.md** | Overview | Start here |
| **QUICK_SETUP.md** | 5-minute setup | Fast setup |
| **BATCH_BRIDGE_SETUP.md** | Complete guide | Detailed info |
| **CHECKLIST.md** | This file | Track progress |
| **IMPLEMENTATION_SUMMARY.md** | Technical details | Understand how it works |

---

<!-- section_id: "5803b52f-1d6d-42bd-987a-821f55572e58" -->
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
