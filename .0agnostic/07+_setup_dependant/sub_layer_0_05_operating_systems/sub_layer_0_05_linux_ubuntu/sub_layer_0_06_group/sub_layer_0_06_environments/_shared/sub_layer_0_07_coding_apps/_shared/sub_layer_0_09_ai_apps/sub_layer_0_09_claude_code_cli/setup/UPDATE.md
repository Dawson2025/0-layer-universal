---
resource_id: "fdfbf635-3b62-4d6f-9eed-093a97196728"
resource_type: "document"
resource_name: "UPDATE"
---
# Claude Code CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 2.1.5

## Overview

This document describes how to update Claude Code CLI to the latest version. Claude Code CLI can be installed via npm or as a native binary. The update process depends on which installation method you're using.

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

## Update Methods

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

## Troubleshooting

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

### Issue: Configuration mismatch warnings

**Solution:**
Run the built-in update command, which will automatically fix configuration mismatches:
```bash
claude update
```

### Issue: Multiple installations detected

**Solution:**
1. Determine which installation you want to keep
2. Remove the duplicate (see "Cleaning Up Duplicate Installations" above)
3. Run `claude update` to fix configuration

## Update History

### 2025-01-26: Updated to v2.1.5
- **Previous version:** 2.0.67
- **Method used:** Built-in `claude update` command
- **Notes:** 
  - Detected and resolved duplicate npm/native installation
  - Configuration automatically updated to reflect native installation method
  - Removed duplicate npm installation to avoid conflicts

## References

- **Official Documentation:** https://docs.claude.com/en/docs/claude-code/cli-reference
- **Installation Guide:** https://docs.claude.com/en/docs/claude-code/getting-started
- **Changelog:** https://www.claudecode101.com/en/upgrade

## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **Universal Tools Config:** `../../sub_layer_0_12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/`
