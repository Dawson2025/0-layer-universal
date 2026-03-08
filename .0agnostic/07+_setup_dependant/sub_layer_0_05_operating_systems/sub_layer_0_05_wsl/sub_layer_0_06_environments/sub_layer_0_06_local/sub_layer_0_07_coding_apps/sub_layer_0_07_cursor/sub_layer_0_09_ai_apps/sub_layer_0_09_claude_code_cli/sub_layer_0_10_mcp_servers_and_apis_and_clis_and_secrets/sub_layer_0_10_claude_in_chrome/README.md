---
resource_id: "f53fb9cf-c9b0-4591-8f7d-a55dbf07dd52"
resource_type: "readme_document"
resource_name: "README"
---
# Claude in Chrome Extension Integration

This directory contains setup and configuration for integrating the **Claude in Chrome** browser extension with **Claude Code CLI** running in WSL.

<!-- section_id: "465403e9-c7bb-4d7f-abc4-764520604f6b" -->
## Documentation

- **[QUICK_SETUP.md](QUICK_SETUP.md)** - Fast 5-minute setup guide (start here!)
- **[BATCH_BRIDGE_SETUP.md](BATCH_BRIDGE_SETUP.md)** - Complete detailed guide with troubleshooting
- **[SETUP_FINDINGS.md](SETUP_FINDINGS.md)** - Research and findings about the integration

<!-- section_id: "8ec2397e-8316-4fc6-888e-72f4897f6177" -->
## What This Does

Enables the Chrome extension running on Windows to communicate with Claude Code CLI running in WSL via a Native Messaging bridge.

```
Chrome Extension (Windows)
        ↓
Windows Batch Script
        ↓
WSL Bash Wrapper
        ↓
Claude Code Native Host
        ↓
Claude Code CLI (WSL)
```

<!-- section_id: "79944b98-e891-43e5-a6e4-b067ff1d10b9" -->
## Quick Start

1. Make sure WSL wrapper exists: `/home/dawson/bin/claude-chrome-host.sh` ✓ (already created)
2. Follow **[QUICK_SETUP.md](QUICK_SETUP.md)** to create Windows components
3. Restart Chrome
4. Test the extension

<!-- section_id: "4f07616e-5100-4b21-83c7-31ab2e6f09d8" -->
## Status

- ✓ WSL wrapper script created and executable
- ✓ Native messaging host verified (`~/.claude/chrome/chrome-native-host`)
- ⏳ Windows batch script (needs manual creation - see QUICK_SETUP.md)
- ⏳ Native messaging manifest (needs manual creation - see QUICK_SETUP.md)
- ⏳ Extension ID configuration (needs user's extension ID)

<!-- section_id: "34a4f7fe-e901-4827-9c64-ba172331861c" -->
## Key Files

| Location | File | Status |
|----------|------|--------|
| WSL | `/home/dawson/bin/claude-chrome-host.sh` | ✓ Created |
| WSL | `/home/dawson/.claude/chrome/chrome-native-host` | ✓ Exists |
| Windows | `%USERPROFILE%\bin\claude-chrome-host.bat` | ⏳ Create manually |
| Windows | `%LOCALAPPDATA%\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json` | ⏳ Create manually |

<!-- section_id: "2a16b4c8-1b1c-42e0-a39a-7737b2eb2d3b" -->
## Support

- See [BATCH_BRIDGE_SETUP.md](BATCH_BRIDGE_SETUP.md) for detailed troubleshooting
- Check Claude Code issues: https://github.com/anthropics/claude-code/issues
- Chrome Native Messaging docs: https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging

<!-- section_id: "a05487ad-3bfc-4531-baaf-db416861d95d" -->
## Version

Last updated: 2025-12-30
Claude Code version: 2.0.76
