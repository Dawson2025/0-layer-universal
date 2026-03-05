---
resource_id: "f7c15967-d1ef-4e40-a891-1d9ca290383b"
resource_type: "document"
resource_name: "QUICK_SETUP"
---
# Claude in Chrome WSL Bridge - Quick Setup

<!-- section_id: "58cadf7f-5155-4802-95ee-3cc6e5b05ea7" -->
## TL;DR

Enable Claude in Chrome extension to talk to Claude Code CLI in WSL.

<!-- section_id: "61e7e7b9-4b7d-41a5-b1fc-d4f9d5d3a75b" -->
## Prerequisites

- WSL2 with Claude Code installed (`npm install -g @anthropic-ai/claude-code`)
- Chrome with Claude in Chrome extension installed
- PowerShell (Administrator access)

<!-- section_id: "5496aafa-ae23-45bb-aa2e-b4fd6ae7dc80" -->
## Setup (5 minutes)

<!-- section_id: "e58aa831-bd1e-4300-a37f-6766474c1740" -->
### 1. WSL Wrapper (Already Created ✓)

The WSL wrapper script is already created at:
```
/home/dawson/bin/claude-chrome-host.sh
```

<!-- section_id: "497eeaf5-2a4f-4baa-9a3e-031a8b23ab34" -->
### 2. Windows Batch Script

**Run in PowerShell:**

```powershell
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\bin"

@"
@echo off
wsl.exe -e /home/dawson/bin/claude-chrome-host.sh
"@ | Out-File -FilePath "$env:USERPROFILE\bin\claude-chrome-host.bat" -Encoding ASCII
```

<!-- section_id: "2be994b7-bc12-4e25-ac86-f34409b36d32" -->
### 3. Get Extension ID

1. Open Chrome: `chrome://extensions/`
2. Enable "Developer mode"
3. Find "Claude in Chrome" → copy the ID (32 chars)

<!-- section_id: "fd7e5d13-b1b8-441c-8248-7fb7574b6d45" -->
### 4. Create Manifest

**Run in PowerShell (replace `YOUR_EXTENSION_ID`):**

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

<!-- section_id: "4d6cd14e-fcad-4c2c-a470-94659ed2be1c" -->
### 5. Restart Chrome

Close ALL Chrome windows and reopen.

<!-- section_id: "1ed90d5a-bb55-455e-ab6e-c219609b9830" -->
## Test It

Open Chrome extension and try using it. Check DevTools console for errors.

<!-- section_id: "06a5ab68-1cfe-4007-9c5d-79cffe435b0c" -->
## Troubleshooting

<!-- section_id: "85cadad2-e263-4b65-85bc-233b477fe676" -->
### "Native messaging host not found"

1. Check manifest exists:
   ```powershell
   Get-Content "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json"
   ```

2. Verify extension ID matches

3. Restart Chrome completely

<!-- section_id: "b24286ab-8af4-4dca-bc8c-d29eed397d27" -->
### Enable Debug Logging

**Edit WSL wrapper:** `/home/dawson/bin/claude-chrome-host.sh`

```bash
#!/bin/bash
exec 2>> /home/dawson/claude-chrome-host.log
echo "[$(date)] Starting" >&2

NATIVE_HOST="/home/dawson/.claude/chrome/chrome-native-host"
exec "$NATIVE_HOST"
```

**View logs:**
```bash
tail -f ~/claude-chrome-host.log
```

<!-- section_id: "c3534d8a-a3bc-42f0-8e3b-e8ea962c1299" -->
## Files Created

| Location | File |
|----------|------|
| WSL | `/home/dawson/bin/claude-chrome-host.sh` |
| Windows | `%USERPROFILE%\bin\claude-chrome-host.bat` |
| Windows | `%LOCALAPPDATA%\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json` |

<!-- section_id: "d3d1e0e4-183d-4904-bf65-866bd210a67d" -->
## Full Documentation

See `BATCH_BRIDGE_SETUP.md` for complete details, troubleshooting, and advanced configuration.

<!-- section_id: "65f7aca6-1011-4853-a7a7-15f11641f322" -->
## Automated Setup

Save and run this PowerShell script for automated setup:

```powershell
# Get extension ID
$extensionId = Read-Host "Enter Claude in Chrome extension ID (from chrome://extensions)"

# Create batch script
$batchDir = "$env:USERPROFILE\bin"
New-Item -ItemType Directory -Force -Path $batchDir
@"
@echo off
wsl.exe -e /home/dawson/bin/claude-chrome-host.sh
"@ | Out-File -FilePath "$batchDir\claude-chrome-host.bat" -Encoding ASCII

# Create manifest
$chromeDir = "$env:LOCALAPPDATA\Google\Chrome\User Data\NativeMessagingHosts"
New-Item -ItemType Directory -Force -Path $chromeDir
$batchPath = "$batchDir\claude-chrome-host.bat".Replace('\', '\\')
@"
{
  "name": "com.anthropic.claude.chrome",
  "description": "Claude in Chrome native messaging host",
  "path": "$batchPath",
  "type": "stdio",
  "allowed_origins": ["chrome-extension://$extensionId/"]
}
"@ | Out-File -FilePath "$chromeDir\com.anthropic.claude.chrome.json" -Encoding UTF8

Write-Host "Setup complete! Restart Chrome." -ForegroundColor Green
```
