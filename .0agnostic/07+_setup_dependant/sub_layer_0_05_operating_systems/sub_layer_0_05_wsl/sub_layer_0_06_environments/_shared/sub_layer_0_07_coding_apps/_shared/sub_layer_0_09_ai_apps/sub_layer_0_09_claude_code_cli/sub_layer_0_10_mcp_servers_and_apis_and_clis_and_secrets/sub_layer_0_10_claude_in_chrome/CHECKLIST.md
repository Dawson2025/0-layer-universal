---
resource_id: "18be160c-5e45-4593-8098-24ef7745e9cb"
resource_type: "document"
resource_name: "CHECKLIST"
---
# Claude in Chrome WSL Bridge Setup Checklist

## WSL Setup (Complete ✓)

- [x] Claude Code CLI installed
- [x] Native messaging host exists (`~/.claude/chrome/chrome-native-host`)
- [x] WSL wrapper script created (`~/bin/claude-chrome-host.sh`)
- [x] Wrapper script is executable
- [x] Verification script created
- [x] All documentation written

**Verify:** Run `~/bin/verify-claude-chrome-setup.sh`

---

## Windows Setup (User Action Required)

### 1. Get Extension ID

- [ ] Open Chrome
- [ ] Go to `chrome://extensions/`
- [ ] Enable "Developer mode" (top-right toggle)
- [ ] Find "Claude in Chrome" extension
- [ ] Copy the extension ID (32-character string)

**Extension ID:** `____________________________________`

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

### 4. Restart Chrome

- [ ] Close ALL Chrome windows (check system tray)
- [ ] Reopen Chrome
- [ ] Verify extension is still enabled

### 5. Test Connection

- [ ] Open Chrome
- [ ] Click Claude in Chrome extension icon
- [ ] Try using the extension
- [ ] Check for errors in DevTools console (F12)

---

## Testing Checklist

### Basic Tests

- [ ] Extension opens without errors
- [ ] Can send a simple message
- [ ] Response is received
- [ ] No console errors in Chrome

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

## Troubleshooting Checklist

### "Native messaging host not found"

- [ ] Verify manifest exists
- [ ] Check extension ID matches
- [ ] Verify batch script path is correct
- [ ] Restart Chrome completely

### "Access denied" or permission errors

- [ ] Check batch script permissions
- [ ] Run PowerShell as Administrator
- [ ] Check Windows Defender/antivirus

### Native host starts but doesn't respond

- [ ] Enable debug logging
- [ ] Check logs for errors
- [ ] Test WSL wrapper manually
- [ ] Verify Claude Code authentication

### Other issues

- [ ] See BATCH_BRIDGE_SETUP.md troubleshooting section
- [ ] Check WSL is running: `wsl.exe --list --running`
- [ ] Verify paths are correct for your username

---

## Quick Commands Reference

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

## Documentation Reference

| File | Purpose | When to Use |
|------|---------|-------------|
| **README.md** | Overview | Start here |
| **QUICK_SETUP.md** | 5-minute setup | Fast setup |
| **BATCH_BRIDGE_SETUP.md** | Complete guide | Detailed info |
| **CHECKLIST.md** | This file | Track progress |
| **IMPLEMENTATION_SUMMARY.md** | Technical details | Understand how it works |

---

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
