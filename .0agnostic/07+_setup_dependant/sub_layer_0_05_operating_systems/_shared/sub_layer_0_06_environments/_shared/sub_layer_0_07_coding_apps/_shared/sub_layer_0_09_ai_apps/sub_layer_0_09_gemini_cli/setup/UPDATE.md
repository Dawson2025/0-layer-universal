---
resource_id: "0f8494e6-7efe-4a77-8b4f-79d222a2dd34"
resource_type: "document"
resource_name: "UPDATE"
---
# Gemini CLI - Update Instructions

**Last Updated:** 2025-01-26  
**Current Version:** 0.23.0

<!-- section_id: "b6f21cdb-d943-4fbb-bf28-5908c75b71d1" -->
## Overview

This document describes how to update Gemini CLI to the latest version. Gemini CLI is distributed via npm and can be updated using standard npm commands.

<!-- section_id: "613c6066-3c51-456a-ac41-b6160c18f8fb" -->
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

<!-- section_id: "42eff552-72a3-4574-8a20-bb2148888c33" -->
## Update Method

<!-- section_id: "f21268a0-6623-4e90-b130-81343a0a9ef5" -->
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

<!-- section_id: "eadf6f25-27bf-4a9a-a427-5759a4d0dd5b" -->
### Alternative: npm update

You can also use the `npm update` command:

```bash
npm update -g @google/gemini-cli
```

**Note:** `npm update` may not always install the latest version if your current version satisfies the semver range. Using `npm install -g @google/gemini-cli@latest` ensures you get the absolute latest version.

<!-- section_id: "abcc7337-09c9-4301-8176-e95be2b0599d" -->
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

<!-- section_id: "4b4003dd-ae53-4727-a84d-f2d22c4276af" -->
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

<!-- section_id: "61a0ae82-ae0e-4a4f-b329-6de4480cc908" -->
## Troubleshooting

<!-- section_id: "76408404-780c-446e-8f77-40c02f006930" -->
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

<!-- section_id: "26ccb097-d0dc-4352-9cc2-ab96c07b7124" -->
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

<!-- section_id: "17b8f255-6d61-48df-84d6-9c0d3c04386f" -->
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

<!-- section_id: "aa7c893a-c6ba-4eb0-9055-2b05d798831e" -->
### Issue: Deprecation warnings

**Solution:**
- The `node-domexception@1.0.0` deprecation warning is harmless
- It comes from a dependency and does not affect Gemini CLI functionality
- The warning will be resolved when the dependency is updated by the maintainers

<!-- section_id: "4f47ed8c-8e97-4daa-a08c-8afd1b2259a5" -->
## Update History

<!-- section_id: "54c2d426-2713-4a12-b9a3-1f850cc7060f" -->
### 2025-01-26: Verified/Updated to v0.23.0
- **Previous version:** 0.23.0 (already at latest)
- **Method used:** `npm install -g @google/gemini-cli@latest`
- **Notes:** 
  - Update completed successfully
  - No version change (already at latest)
  - All functionality verified
  - Deprecation warning noted but harmless

<!-- section_id: "1197071f-b675-456a-b2b0-653f4eeb470b" -->
## Platform Support

- ✅ **macOS**: Fully supported
- ✅ **Linux**: Fully supported
- ✅ **Windows**: Supported (via npm)

<!-- section_id: "156566c1-6cd2-4678-898e-984ccff15772" -->
## References

- **Official Documentation:** https://ai.google.dev/docs
- **npm Package:** https://www.npmjs.com/package/@google/gemini-cli
- **Update Guide:** https://milvus.io/ai-quick-reference/how-do-i-update-gemini-cli

<!-- section_id: "623daf56-afbf-47ac-966e-ff112204c595" -->
## Related Documentation

- **Setup README:** `README.md` (in this directory)
- **AI Apps Setup:** `../../sub_layer_0_09_ai_apps_tools_setup/` (universal context)
