---
resource_id: "f58c117c-9601-4e27-b3c8-a764163737b3"
resource_type: "document"
resource_name: "UPDATE"
---
# Codex CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 0.80.0

<!-- section_id: "7de1d038-f62a-4dc2-a2a5-5e920cdf481c" -->
## Overview

This document describes how to update Codex CLI to the latest version. Codex CLI is distributed via npm and can be updated using standard npm commands.

<!-- section_id: "a55a4297-a947-4407-92bc-5f2e133b745c" -->
## Checking Current Version

Before updating, check your current version:

```bash
codex --version
```

**Example output:**
```
codex-cli 0.80.0
```

You can also check the npm package version:

```bash
npm list -g @openai/codex
```

**Example output:**
```
/home/dawson/.nvm/versions/node/v22.21.1/lib
└── @openai/codex@0.80.0
```

<!-- section_id: "c2479638-7e32-4840-8954-c877ba18dd13" -->
## Update Method

<!-- section_id: "b3ec72d5-3338-4f14-aa0d-3deb59619b47" -->
### npm Update (Standard Method)

Codex CLI is managed through npm. To update to the latest version:

```bash
npm install -g @openai/codex@latest
```

**What this does:**
- Downloads and installs the latest version of `@openai/codex`
- Replaces the previous global installation
- Updates the `codex` command to the new version

**Example output:**
```
changed 1 package in 8s
```

<!-- section_id: "30997abf-0ed5-4e48-b3f9-4fb8e56e6a31" -->
### Alternative: npm update

You can also use the `npm update` command:

```bash
npm update -g @openai/codex
```

**Note:** `npm update` may not always install the latest version if your current version satisfies the semver range. Using `npm install -g @openai/codex@latest` ensures you get the absolute latest version.

<!-- section_id: "1329e661-514e-4d65-a73a-4a19e4942396" -->
## Verification After Update

After updating, verify the installation:

```bash
# Check version
codex --version

# Check installation location
which codex

# Check npm package version
npm list -g @openai/codex

# Test basic functionality
codex --help
```

<!-- section_id: "ec3edb16-8d1b-4986-998f-44318ab75699" -->
## Troubleshooting

<!-- section_id: "3b4e97bf-2137-46d3-b199-83513b9f2117" -->
### Issue: "Command not found" after update

**Solution:**
1. Check if the binary is in your PATH:
   ```bash
   which codex
   echo $PATH
   ```

2. If using nvm, ensure nvm is loaded:
   ```bash
   source ~/.nvm/nvm.sh
   # Or add to ~/.bashrc or ~/.zshrc
   ```

3. Verify npm global bin directory is in PATH:
   ```bash
   npm config get prefix
   # Add that path/bin to your PATH if not already there
   ```

<!-- section_id: "ee198a4b-0e7b-47ad-abf6-74beb07240b6" -->
### Issue: Permission errors during update

**Solution:**
1. **Recommended:** Use nvm to manage Node.js and npm (avoids permission issues)
   ```bash
   # Install nvm if not already installed
   curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
   
   # Use nvm to install Node.js
   nvm install node
   nvm use node
   ```

2. **Alternative:** Configure npm to use a different directory (not recommended):
   ```bash
   mkdir ~/.npm-global
   npm config set prefix '~/.npm-global'
   export PATH=~/.npm-global/bin:$PATH
   # Add to ~/.bashrc or ~/.zshrc
   ```

3. **Not recommended:** Using `sudo` can cause permission issues and is not recommended

<!-- section_id: "dd852c37-fd34-47c3-a98b-538a8ae5127c" -->
### Issue: Version not updating

**Solution:**
1. Force reinstall:
   ```bash
   npm install -g @openai/codex@latest --force
   ```

2. Clear npm cache and reinstall:
   ```bash
   npm cache clean --force
   npm install -g @openai/codex@latest
   ```

3. Verify you're using the correct Node.js version:
   ```bash
   node --version
   npm --version
   ```

<!-- section_id: "9ac273f5-5069-45f7-bafa-1ad39a67090a" -->
## Update History

<!-- section_id: "d3c879ba-8755-4764-85ac-ab8586da6db6" -->
### 2025-01-26: Updated to v0.80.0
- **Previous version:** 0.79.0
- **Method used:** `npm install -g @openai/codex@latest`
- **Notes:** 
  - Update completed successfully
  - No configuration changes required
  - All functionality verified after update

<!-- section_id: "1de0daac-06c3-4d93-a77f-4bc8b1fab7ec" -->
## Platform Support

- ✅ **macOS**: Fully supported
- ✅ **Linux**: Fully supported
- ⚠️ **Windows**: Experimental (recommended to use WSL)

<!-- section_id: "9fc1cc24-c967-4ed5-8a45-9f54f8bada83" -->
## References

- **Official Documentation:** https://developers.openai.com/codex/cli
- **npm Package:** https://www.npmjs.com/package/@openai/codex

<!-- section_id: "f5a18446-9a57-4596-a2fc-0fbbec733c4f" -->
## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../sub_layer_0_09_ai_apps_tools_setup/` (universal context)
