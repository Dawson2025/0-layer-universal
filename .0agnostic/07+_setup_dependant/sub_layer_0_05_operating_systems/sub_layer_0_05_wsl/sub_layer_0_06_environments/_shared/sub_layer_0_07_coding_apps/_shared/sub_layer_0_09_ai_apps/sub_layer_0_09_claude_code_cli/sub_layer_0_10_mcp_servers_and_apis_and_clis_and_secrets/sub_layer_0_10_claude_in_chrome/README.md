---
resource_id: "f2caca77-43e0-465f-89bb-d6f4c1509995"
resource_type: "readme_document"
resource_name: "README"
---
# Claude in Chrome Extension Integration

This directory contains setup and configuration for integrating the **Claude in Chrome** browser extension with **Claude Code CLI** running in WSL.

<!-- section_id: "6477e5f1-98de-4c38-8e29-4722fe69572d" -->
## Documentation

- **[QUICK_SETUP.md](QUICK_SETUP.md)** - Fast 5-minute setup guide (start here!)
- **[BATCH_BRIDGE_SETUP.md](BATCH_BRIDGE_SETUP.md)** - Complete detailed guide with troubleshooting
- **[SETUP_FINDINGS.md](SETUP_FINDINGS.md)** - Research and findings about the integration

<!-- section_id: "8dd4839b-e232-4ff6-8eac-0a6b7d7027a6" -->
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

<!-- section_id: "9c7bc5a4-c296-4400-ba10-6933afa31e70" -->
## Quick Start

1. Make sure WSL wrapper exists: `/home/dawson/bin/claude-chrome-host.sh` ✓ (already created)
2. Follow **[QUICK_SETUP.md](QUICK_SETUP.md)** to create Windows components
3. Restart Chrome
4. Test the extension

<!-- section_id: "5840e1ed-8ac0-4b66-97b7-2815a4cffc42" -->
## Status

- ✓ WSL wrapper script created and executable
- ✓ Native messaging host verified (`~/.claude/chrome/chrome-native-host`)
- ⏳ Windows batch script (needs manual creation - see QUICK_SETUP.md)
- ⏳ Native messaging manifest (needs manual creation - see QUICK_SETUP.md)
- ⏳ Extension ID configuration (needs user's extension ID)

<!-- section_id: "bc2a1dc7-ac53-4796-92e9-2817334a5f2e" -->
## Key Files

| Location | File | Status |
|----------|------|--------|
| WSL | `/home/dawson/bin/claude-chrome-host.sh` | ✓ Created |
| WSL | `/home/dawson/.claude/chrome/chrome-native-host` | ✓ Exists |
| Windows | `%USERPROFILE%\bin\claude-chrome-host.bat` | ⏳ Create manually |
| Windows | `%LOCALAPPDATA%\Google\Chrome\User Data\NativeMessagingHosts\com.anthropic.claude.chrome.json` | ⏳ Create manually |

<!-- section_id: "e183162c-9aab-486f-90b1-0d6cd00102f0" -->
## Support

- See [BATCH_BRIDGE_SETUP.md](BATCH_BRIDGE_SETUP.md) for detailed troubleshooting
- Check Claude Code issues: https://github.com/anthropics/claude-code/issues
- Chrome Native Messaging docs: https://developer.chrome.com/docs/extensions/develop/concepts/native-messaging

<!-- section_id: "bcb9464c-2394-4cae-a1a0-b938873d1340" -->
## Version

Last updated: 2025-12-30
Claude Code version: 2.0.76
