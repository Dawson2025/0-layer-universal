---
resource_id: "17a19278-b063-4987-b490-6277b35407d1"
resource_type: "knowledge"
resource_name: "UPDATE"
---
# Claude Code CLI - Update Instructions (Linux Ubuntu)

**Last Updated:** 2025-01-26  
**Current Version:** 2.1.5  
**OS:** Linux Ubuntu  
**Environment:** Local  
**Coding App:** Cursor

## Overview

This document describes how to update Claude Code CLI to the latest version on Linux Ubuntu. For cross-platform documentation, see the [shared update guide](../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/claude_code_cli/setup/UPDATE.md).

## Linux Ubuntu-Specific Considerations

### Installation Methods on Linux

Claude Code CLI can be installed on Linux via:
1. **Native installer** (recommended) - Uses curl script or manual installation
2. **npm** - Global npm package installation

### PATH Configuration

On Linux Ubuntu, ensure your PATH includes:
- `~/.local/bin` (for native installation)
- `~/.nvm/versions/node/v*/bin` (if using npm with nvm)

**Add to `~/.bashrc` or `~/.zshrc`:**
```bash
# For native installation
export PATH="$HOME/.local/bin:$PATH"

# For npm with nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

## Checking Current Version

Before updating, check your current version:

```bash
claude --version
```

**Example output:**
```
2.1.5 (Claude Code)
```

Check installation location:
```bash
which claude
# Example: /home/dawson/.local/bin/claude (native)
# or: /home/dawson/.nvm/versions/node/v22.21.1/bin/claude (npm)
```

## Update Methods

### Method 1: Built-in Update Command (Recommended)

Claude Code CLI has a built-in update command that works well on Linux:

```bash
claude update
```

**What this does:**
- Checks for available updates
- Detects your installation method (npm vs native)
- Updates to the latest version
- Fixes configuration mismatches if detected

**Example output on Linux:**
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

### Method 2: npm Update (If Installed via npm)

If Claude Code CLI was installed via npm, update using:

```bash
npm install -g @anthropic-ai/claude-code@latest
```

**Note:** If using nvm, ensure nvm is loaded:
```bash
source ~/.nvm/nvm.sh
# Or ensure it's in your ~/.bashrc
```

### Method 3: Native Installer Update (Curl Script)

If you installed using the curl script, re-run it to update:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

This will update the native installation in `~/.local/bin/claude`.

## Cleaning Up Duplicate Installations

On Linux, you may have both npm and native installations. Clean up duplicates:

**Remove npm installation (if using native):**
```bash
npm -g uninstall @anthropic-ai/claude-code
```

**Remove native installation (if using npm):**
```bash
rm ~/.local/bin/claude
# Also remove config if needed:
rm -rf ~/.config/claude-code
```

## Verification After Update

After updating, verify the installation:

```bash
# Check version
claude --version

# Check installation location
which claude

# Verify PATH
echo $PATH | grep -E "(\.local/bin|nvm)"

# Test basic functionality
claude --help
```

## Linux-Specific Troubleshooting

### Issue: "Command not found" after update

**Solution:**
1. Check if the binary is in your PATH:
   ```bash
   which claude
   echo $PATH
   ```

2. If using native installation, ensure `~/.local/bin` is in PATH:
   ```bash
   export PATH="$HOME/.local/bin:$PATH"
   # Add to ~/.bashrc for persistence
   echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
   source ~/.bashrc
   ```

3. If using npm with nvm, ensure nvm is loaded:
   ```bash
   source ~/.nvm/nvm.sh
   # Or add to ~/.bashrc:
   echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc
   echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"' >> ~/.bashrc
   source ~/.bashrc
   ```

### Issue: Permission errors during update

**Solution:**
1. **Recommended:** Use native installation (no sudo needed):
   ```bash
   curl -fsSL https://claude.ai/install.sh | bash
   ```

2. **Alternative:** Use nvm for npm (avoids permission issues):
   ```bash
   # Install nvm if not already installed
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
   
   # Use nvm to install Node.js
   nvm install node
   nvm use node
   ```

3. **Not recommended:** Using `sudo` can cause permission issues and is not recommended

### Issue: Configuration mismatch warnings

**Solution:**
Run the built-in update command, which will automatically fix configuration mismatches:
```bash
claude update
```

This will detect your installation method and update the configuration accordingly.

## Update History

### 2025-01-26: Updated to v2.1.5 on Linux Ubuntu
- **Previous version:** 2.0.67
- **Method used:** Built-in `claude update` command
- **OS:** Linux Ubuntu
- **Environment:** Local
- **Coding App:** Cursor
- **Notes:** 
  - Detected and resolved duplicate npm/native installation
  - Configuration automatically updated to reflect native installation method
  - Removed duplicate npm installation to avoid conflicts
  - Update process worked smoothly on Linux Ubuntu

## References

- **Shared Update Guide:** `../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/claude_code_cli/setup/UPDATE.md`
- **Official Documentation:** https://docs.claude.com/en/docs/claude-code/cli-reference
- **Installation Guide:** https://docs.claude.com/en/docs/claude-code/getting-started
- **Changelog:** https://www.claudecode101.com/en/upgrade

## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **Linux Ubuntu MCP Issues:** `../../../../../../_shared/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Universal Tools Config:** `../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/_shared/0.12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/`
