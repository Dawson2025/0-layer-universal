---
resource_id: "129d0498-5f7c-4095-ac2f-2d6be4afd56e"
resource_type: "document"
resource_name: "UPDATE"
---
# Gemini CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 0.23.0

<!-- section_id: "a2aad14e-87d6-4218-abfb-f1c188c3cfa0" -->
## Overview

This document describes how to update Gemini CLI to the latest version. Gemini CLI is distributed via npm and can be updated using standard npm commands.

<!-- section_id: "a16e1435-9cce-4047-8862-e3ac996cc719" -->
## Checking Current Version

Before updating, check your current version:

```bash
gemini --version
```

**Example output:**
```
0.23.0
```

You can also check the npm package version:

```bash
npm list -g @google/gemini-cli
```

**Example output:**
```
/home/dawson/.nvm/versions/node/v22.21.1/lib
└── @google/gemini-cli@0.23.0
```

<!-- section_id: "4debe30b-8056-4dbd-9d4d-3a782becfca9" -->
## Update Method

<!-- section_id: "c85971e3-fec6-4de0-8f9c-356b9a7a16c2" -->
### npm Update (Standard Method)

Gemini CLI is managed through npm. To update to the latest version:

```bash
npm install -g @google/gemini-cli@latest
```

**What this does:**
- Downloads and installs the latest version of `@google/gemini-cli`
- Replaces the previous global installation
- Updates the `gemini` command to the new version

**Example output:**
```
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead

changed 583 packages in 19s

155 packages are looking for funding
  run `npm fund` for details
```

**Note:** The deprecation warning about `node-domexception` is harmless and comes from a dependency. It does not affect functionality.

<!-- section_id: "159bce29-e962-4c2c-a11c-375aafa8e6de" -->
### Alternative: npm update

You can also use the `npm update` command:

```bash
npm update -g @google/gemini-cli
```

**Note:** `npm update` may not always install the latest version if your current version satisfies the semver range. Using `npm install -g @google/gemini-cli@latest` ensures you get the absolute latest version.

<!-- section_id: "56975e7f-fc46-409a-a841-bca4f94d3e92" -->
### Alternative: Using npx (No Global Installation)

If you prefer not to install globally, you can use `npx` which automatically fetches and runs the latest version:

```bash
npx @google/gemini-cli
```

**Benefits:**
- Always uses the latest version
- No global installation needed
- No manual updates required

**Drawbacks:**
- Slightly slower startup (downloads on first run)
- Requires internet connection

<!-- section_id: "99cab7a7-4f2f-4512-80a7-46f637d2777b" -->
## Verification After Update

After updating, verify the installation:

```bash
# Check version
gemini --version

# Check installation location
which gemini

# Check npm package version
npm list -g @google/gemini-cli

# Test basic functionality
gemini --help
```

<!-- section_id: "0e25ebf0-7784-48c8-8ba0-c56e57f26202" -->
## Troubleshooting

<!-- section_id: "11a2733f-e6fa-4524-a9bf-a99cdcd62fbd" -->
### Issue: "Command not found" after update

**Solution:**
1. Check if the binary is in your PATH:
   ```bash
   which gemini
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

<!-- section_id: "102cc371-0bce-43b1-ab04-a5141e9b1f59" -->
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

<!-- section_id: "86a40a0d-a205-4ea2-8b0c-461c24d14033" -->
### Issue: Version not updating

**Solution:**
1. Force reinstall:
   ```bash
   npm install -g @google/gemini-cli@latest --force
   ```

2. Clear npm cache and reinstall:
   ```bash
   npm cache clean --force
   npm install -g @google/gemini-cli@latest
   ```

3. Verify you're using the correct Node.js version:
   ```bash
   node --version
   npm --version
   ```

<!-- section_id: "75225eba-6132-4c91-bb15-e083e8469ff4" -->
### Issue: Deprecation warnings

**Solution:**
- The `node-domexception@1.0.0` deprecation warning is harmless
- It comes from a dependency and does not affect Gemini CLI functionality
- The warning will be resolved when the dependency is updated by the maintainers

<!-- section_id: "750f5e0e-d11f-44d4-81e8-a92b9d8e70c5" -->
## Update History

<!-- section_id: "3c8dd795-88e8-46ff-a39f-01df569e8555" -->
### 2025-01-26: Verified/Updated to v0.23.0
- **Previous version:** 0.23.0 (already at latest)
- **Method used:** `npm install -g @google/gemini-cli@latest`
- **Notes:** 
  - Update completed successfully
  - No version change (already at latest)
  - All functionality verified
  - Deprecation warning noted but harmless

<!-- section_id: "3f0b79e4-b038-4aba-b47d-947e5d2643f9" -->
## Platform Support

- ✅ **macOS**: Fully supported
- ✅ **Linux**: Fully supported
- ✅ **Windows**: Supported (via npm)

<!-- section_id: "9630ce6e-8351-4219-8fca-d169eb8d5b83" -->
## References

- **Official Documentation:** https://ai.google.dev/docs
- **npm Package:** https://www.npmjs.com/package/@google/gemini-cli
- **Update Guide:** https://milvus.io/ai-quick-reference/how-do-i-update-gemini-cli

<!-- section_id: "33f18152-be01-490b-bdf9-1697ceb0a13c" -->
## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../sub_layer_0_09_ai_apps_tools_setup/` (universal context)
