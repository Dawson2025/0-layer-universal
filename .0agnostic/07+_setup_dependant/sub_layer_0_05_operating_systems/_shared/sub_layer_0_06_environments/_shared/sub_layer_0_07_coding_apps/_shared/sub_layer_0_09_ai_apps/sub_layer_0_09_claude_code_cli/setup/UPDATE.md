---
resource_id: "57306474-6659-41b8-8932-64eadda74b32"
resource_type: "document"
resource_name: "UPDATE"
---
# Claude Code CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 2.1.5

<!-- section_id: "f15598a4-859f-4d81-8397-d35f71bf07a8" -->
## Overview

This document describes how to update Claude Code CLI to the latest version. Claude Code CLI can be installed via npm or as a native binary. The update process depends on which installation method you're using.

<!-- section_id: "d0c7ec49-fdf4-4197-8ae8-61659c44e79c" -->
## Checking Current Version

Before updating, check your current version:

```bash
claude --version
```

**Example output:**
```
2.1.5 (Claude Code)
```

You can also check the npm package version (if installed via npm):

```bash
npm list -g @anthropic-ai/claude-code
```

<!-- section_id: "d4e995e8-551a-4b2d-af26-7d4e551ea4e7" -->
## Update Methods

<!-- section_id: "e59efbee-ef5a-499f-a6c1-2c5475fe5c63" -->
### Method 1: Built-in Update Command (Recommended)

Claude Code CLI has a built-in update command that automatically detects and updates your installation:

```bash
claude update
```

**What this does:**
- Checks for available updates
- Detects your installation method (npm vs native)
- Updates to the latest version
- Fixes configuration mismatches if detected

**Example output:**
```
Current version: 2.0.67
Checking for updates...

Warning: Multiple installations found
- npm-global at /home/dawson/.nvm/versions/node/v22.21.1/bin/claude
- native at /home/dawson/.local/bin/claude (currently running)

Warning: Running native installation but config install method is 'global'
Fix: Run claude install to update configuration
Warning: Leftover npm global installation at /home/dawson/.nvm/versions/node/v22.21.1/bin/claude
Fix: Run: npm -g uninstall @anthropic-ai/claude-code

Warning: Configuration mismatch
Config expects: global installation
Currently running: native
Updating the native installation you are currently using
Config updated to reflect current installation method: native
Successfully updated from 2.0.67 to version 2.1.5
```

**Important Notes:**
- If you have multiple installations (npm and native), the update command will detect this and update the one you're currently using
- You may need to clean up duplicate installations (see "Cleaning Up Duplicate Installations" below)

<!-- section_id: "f37bbd4a-8727-48a9-bf3f-26ee18b9df4c" -->
### Method 2: npm Update (If Installed via npm)

If Claude Code CLI was installed via npm, you can update it using:

```bash
npm install -g @anthropic-ai/claude-code@latest
```

**Verify the update:**
```bash
claude --version
npm list -g @anthropic-ai/claude-code
```

<!-- section_id: "ba115c7c-061b-4690-977f-84629e9c8c2b" -->
### Method 3: Native Installer Update

If you installed Claude Code using a native installer (Homebrew, curl script, etc.), the update process depends on your installation method:

**Homebrew (macOS/Linux):**
```bash
brew upgrade claude-code
```

**Curl Script (macOS/Linux/WSL):**
```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**PowerShell (Windows):**
```powershell
irm https://claude.ai/install.ps1 | iex
```

<!-- section_id: "96099725-a05c-49ba-be74-fc9e068f7e12" -->
## Cleaning Up Duplicate Installations

If you have both npm and native installations, you may want to remove the duplicate:

**Remove npm installation (if you're using native):**
```bash
npm -g uninstall @anthropic-ai/claude-code
```

**Remove native installation (if you're using npm):**
```bash
# Location depends on installation method
# Check with: which claude
rm /path/to/native/claude
```

<!-- section_id: "93c7edb5-c975-43ca-a297-395315581913" -->
## Verification After Update

After updating, verify the installation:

```bash
# Check version
claude --version

# Check installation location
which claude

# Test basic functionality
claude --help
```

<!-- section_id: "c3780e07-6328-4556-b3fa-c119cef5231c" -->
## Troubleshooting

<!-- section_id: "3bae08f4-aa17-46b7-9bfb-727cba4c7911" -->
### Issue: "Command not found" after update

**Solution:**
1. Check if the binary is in your PATH:
   ```bash
   which claude
   echo $PATH
   ```

2. If using npm with nvm, ensure nvm is loaded:
   ```bash
   source ~/.nvm/nvm.sh
   # Or add to ~/.bashrc or ~/.zshrc
   ```

3. If using native installation, ensure `~/.local/bin` is in your PATH:
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   # Add to ~/.bashrc or ~/.zshrc for persistence
   ```

<!-- section_id: "da084c14-1373-4a6a-92fb-c6568a4600e1" -->
### Issue: Configuration mismatch warnings

**Solution:**
Run the built-in update command, which will automatically fix configuration mismatches:
```bash
claude update
```

<!-- section_id: "7e741466-c8c9-48e5-a838-a14fa17819eb" -->
### Issue: Multiple installations detected

**Solution:**
1. Determine which installation you want to keep
2. Remove the duplicate (see "Cleaning Up Duplicate Installations" above)
3. Run `claude update` to fix configuration

<!-- section_id: "1dee4aec-b06b-4cda-a2e7-f06212094fc4" -->
## Update History

<!-- section_id: "5ed35d8b-76b5-41fd-befe-041dc6adb3c9" -->
### 2025-01-26: Updated to v2.1.5
- **Previous version:** 2.0.67
- **Method used:** Built-in `claude update` command
- **Notes:** 
  - Detected and resolved duplicate npm/native installation
  - Configuration automatically updated to reflect native installation method
  - Removed duplicate npm installation to avoid conflicts

<!-- section_id: "d681a409-121e-4d73-ba82-929e73a84db1" -->
## References

- **Official Documentation:** https://docs.claude.com/en/docs/claude-code/cli-reference
- **Installation Guide:** https://docs.claude.com/en/docs/claude-code/getting-started
- **Changelog:** https://www.claudecode101.com/en/upgrade

<!-- section_id: "161d55f2-d026-47f7-9a28-e21174dfc0e5" -->
## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **Universal Tools Config:** `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/`
