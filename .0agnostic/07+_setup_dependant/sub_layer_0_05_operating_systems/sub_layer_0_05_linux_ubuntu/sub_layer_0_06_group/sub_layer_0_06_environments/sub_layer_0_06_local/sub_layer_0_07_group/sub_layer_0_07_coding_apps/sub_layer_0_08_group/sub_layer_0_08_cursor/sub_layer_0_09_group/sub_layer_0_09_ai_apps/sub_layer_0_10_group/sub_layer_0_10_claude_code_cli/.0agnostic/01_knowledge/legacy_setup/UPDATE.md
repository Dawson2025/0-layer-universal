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

<!-- section_id: "064afc4a-9ba6-4f1d-9c9a-4a6895b1f4c6" -->
## Overview

This document describes how to update Claude Code CLI to the latest version on Linux Ubuntu. For cross-platform documentation, see the [shared update guide](../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/claude_code_cli/setup/UPDATE.md).

<!-- section_id: "4d89ac04-2e43-4c9e-a39a-ac4c69944e5d" -->
## Linux Ubuntu-Specific Considerations

<!-- section_id: "39fc9440-baa0-4845-90ea-8b957e398cf3" -->
### Installation Methods on Linux

Claude Code CLI can be installed on Linux via:
1. **Native installer** (recommended) - Uses curl script or manual installation
2. **npm** - Global npm package installation

<!-- section_id: "1e805f15-cabf-4e5e-a167-6a283b6e1e80" -->
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

<!-- section_id: "04f7ac3d-98b8-45cd-b9cd-545b8b636b81" -->
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

<!-- section_id: "fff5fc59-454a-4639-a6de-93d66d53953f" -->
## Update Methods

<!-- section_id: "f58f6383-a148-4ab3-bef2-58a2d5e9378a" -->
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

<!-- section_id: "7475058b-b219-442a-93f2-d48bdc9c0403" -->
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

<!-- section_id: "d9773511-053f-471c-8e60-b15c26008dee" -->
### Method 3: Native Installer Update (Curl Script)

If you installed using the curl script, re-run it to update:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

This will update the native installation in `~/.local/bin/claude`.

<!-- section_id: "00e73c68-00d2-4ce9-93c3-f9ced80afd58" -->
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

<!-- section_id: "0f1e28f7-9674-46ff-ad1d-0c1bb38d0a9d" -->
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

<!-- section_id: "c2363804-2443-4434-ad9d-3a9bc01241b7" -->
## Linux-Specific Troubleshooting

<!-- section_id: "01d8c8f1-1d73-4e1a-bbda-b212cff9551c" -->
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

<!-- section_id: "24f990be-d23e-4fc6-9206-916ea238be44" -->
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

<!-- section_id: "f5122994-f182-4295-89c2-865bf82f922a" -->
### Issue: Configuration mismatch warnings

**Solution:**
Run the built-in update command, which will automatically fix configuration mismatches:
```bash
claude update
```

This will detect your installation method and update the configuration accordingly.

<!-- section_id: "a6c9fdbd-a8e9-4718-b7e4-eb8bbefdaf66" -->
## Update History

<!-- section_id: "86c4b7c0-34e1-4a35-9404-0b7fe5998b7d" -->
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

<!-- section_id: "a39cc421-8677-46e8-b7ca-b6e60440f99b" -->
## References

- **Shared Update Guide:** `../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/claude_code_cli/setup/UPDATE.md`
- **Official Documentation:** https://docs.claude.com/en/docs/claude-code/cli-reference
- **Installation Guide:** https://docs.claude.com/en/docs/claude-code/getting-started
- **Changelog:** https://www.claudecode101.com/en/upgrade

<!-- section_id: "26848a2b-8818-4600-81a7-153dcdea8dff" -->
## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **Linux Ubuntu MCP Issues:** `../../../../../../_shared/trickle_down_0.5_setup/0_instruction_docs/LINUX_UBUNTU_MCP_ISSUES.md`
- **Universal Tools Config:** `../../../../../../_shared/0.06_environments/_shared/0.07_coding_apps/_shared/0.09_ai_apps/_shared/0.12_universal_tools/trickle_down_0.75_universal_tools/0_instruction_docs/claude-code-config/`
