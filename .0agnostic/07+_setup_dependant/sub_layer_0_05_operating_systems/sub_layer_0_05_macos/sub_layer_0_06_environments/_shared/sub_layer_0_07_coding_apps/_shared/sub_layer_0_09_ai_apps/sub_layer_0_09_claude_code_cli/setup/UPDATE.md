---
resource_id: "73ef0427-5078-4ea3-99bf-a6743a51df78"
resource_type: "document"
resource_name: "UPDATE"
---
# Claude Code CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 2.1.5

<!-- section_id: "ebe251d1-ec06-4d16-9f2b-f75a3382e880" -->
## Overview

This document describes how to update Claude Code CLI to the latest version. Claude Code CLI can be installed via npm or as a native binary. The update process depends on which installation method you're using.

<!-- section_id: "60b4a85f-dfca-405d-81cb-5c0c80dd967b" -->
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

<!-- section_id: "f6ca5423-27c0-4f13-a113-fccd1e4df948" -->
## Update Methods

<!-- section_id: "6c9bfbc5-e5ec-474a-b319-0cb560c83781" -->
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

<!-- section_id: "1c400a7e-7efb-4fcd-9518-b0056cce2382" -->
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

<!-- section_id: "92dadfab-8fe9-4d86-a545-9e6f6887a3f3" -->
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

<!-- section_id: "ef67c18f-6eea-4bff-81de-c61769f04f9e" -->
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

<!-- section_id: "5ad1950b-75fc-45a9-a116-1a2ed94c2cb9" -->
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

<!-- section_id: "c3f8b06d-ac3c-4e69-bd66-975e1ceca634" -->
## Troubleshooting

<!-- section_id: "49f8f1c9-8f5d-416a-9897-3f8f48471224" -->
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

<!-- section_id: "e442340a-d37c-4603-80c1-15668a160c90" -->
### Issue: Configuration mismatch warnings

**Solution:**
Run the built-in update command, which will automatically fix configuration mismatches:
```bash
claude update
```

<!-- section_id: "59104c90-1e4b-49d2-a994-609ade6568f3" -->
### Issue: Multiple installations detected

**Solution:**
1. Determine which installation you want to keep
2. Remove the duplicate (see "Cleaning Up Duplicate Installations" above)
3. Run `claude update` to fix configuration

<!-- section_id: "897aa191-88fa-4e2a-a480-da17b9d745d5" -->
## Update History

<!-- section_id: "c43bf0a5-2b79-4823-994c-8ae5d0175a7b" -->
### 2025-01-26: Updated to v2.1.5
- **Previous version:** 2.0.67
- **Method used:** Built-in `claude update` command
- **Notes:** 
  - Detected and resolved duplicate npm/native installation
  - Configuration automatically updated to reflect native installation method
  - Removed duplicate npm installation to avoid conflicts

<!-- section_id: "e70930e6-bf39-48c5-b8da-d4cdb33ddcc6" -->
## References

- **Official Documentation:** https://docs.claude.com/en/docs/claude-code/cli-reference
- **Installation Guide:** https://docs.claude.com/en/docs/claude-code/getting-started
- **Changelog:** https://www.claudecode101.com/en/upgrade

<!-- section_id: "34dbd14e-3274-4a5e-ac93-db1dde4147e9" -->
## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **Universal Tools Config:** `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/`
