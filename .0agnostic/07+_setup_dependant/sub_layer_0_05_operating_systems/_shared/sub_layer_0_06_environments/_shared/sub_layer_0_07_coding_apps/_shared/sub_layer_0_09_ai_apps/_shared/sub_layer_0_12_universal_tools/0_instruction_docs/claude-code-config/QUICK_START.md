---
resource_id: "91db4112-a985-4448-a7c3-48d79847a274"
resource_type: "document"
resource_name: "QUICK_START"
---
# Claude Code Bypass Permissions - Quick Start Guide

<!-- section_id: "8bf30a4e-c005-43ae-babd-cf21477aa9e8" -->
## 5-Minute Setup

<!-- section_id: "7172c4be-5da8-472c-ba63-e2c70b58517b" -->
### For Personal Projects (Recommended)

1. **Create settings directory:**
   ```bash
   mkdir -p .claude
   ```

2. **Create settings file:**
   ```bash
   cat > .claude/settings.json << 'EOF'
   {
     "permissions": {
       "defaultMode": "bypassPermissions",
       "allow": [
         "WebSearch",
         "WebFetch(domain:*)",
         "Read(/**)",
         "Edit(**)",
         "Write(**)",
         "Bash(git:*)",
         "Bash(npm:*)",
         "Bash(npx:*)"
       ],
       "deny": [
         "Bash(rm -rf /)",
         "Bash(sudo rm -rf :*)",
         "Bash(git push --force origin main)",
         "Bash(git push --force origin master)"
       ]
     }
   }
   EOF
   ```

3. **Done!** Start Claude Code normally:
   ```bash
   claude
   ```

   **You should now see the Shift+Tab bypass mode toggle indicator.**

<!-- section_id: "ce3dd2f9-4f2d-4731-8473-787f290cc7a4" -->
### For Shared Repositories (Local Override)

1. **Create local settings:**
   ```bash
   mkdir -p .claude
   cat > .claude/settings.local.json << 'EOF'
   {
     "permissions": {
       "defaultMode": "bypassPermissions",
       "allow": [
         "WebSearch",
         "WebFetch(domain:*)",
         "Read(/**)",
         "Edit(**)",
         "Write(**)",
         "Bash(git:*)",
         "Bash(npm:*)",
         "Bash(npx:*)"
       ],
       "deny": [
         "Bash(rm -rf /)",
         "Bash(sudo rm -rf :*)",
         "Bash(git push --force origin main)",
         "Bash(git push --force origin master)"
       ]
     }
   }
   EOF
   ```

2. **Add to .gitignore:**
   ```bash
   echo ".claude/settings.local.json" >> .gitignore
   ```

3. **Done!** Your team won't have bypass mode, but you will.

<!-- section_id: "655a86c0-3777-44da-8190-d90a55b3dab8" -->
### One-Time Use (No Configuration)

```bash
claude --dangerously-skip-permissions
```

<!-- section_id: "26aeb1c0-409c-4d48-a7c9-b73dfffc8f6d" -->
## Verification

In Claude Code, run:
```
/permissions
```

Look for: "Bypass permissions mode: enabled"

<!-- section_id: "36944a42-09d8-4276-bed4-17208819cc0d" -->
## Common Configurations

<!-- section_id: "cf972c3d-174f-4a79-bc81-013cee777ed5" -->
### What Actually Works

**⚠️ IMPORTANT**: The `disableBypassPermissionsMode: false` approach shown in older documentation **does NOT work**. The correct configuration is:

```json
{
  "permissions": {
    "defaultMode": "bypassPermissions",
    "allow": [
      "Read(/**)",
      "Edit(**)",
      "Write(**)",
      "Bash(git:*)",
      "Bash(npm:*)"
    ],
    "deny": [
      "Bash(rm -rf /)",
      "Bash(sudo rm -rf :*)",
      "Bash(git push --force origin main)",
      "Bash(git push --force origin master)",
      "Edit(.env*)"
    ]
  }
}
```

**Key Points:**
- Use `"defaultMode": "bypassPermissions"` to enable bypass mode and show the Shift+Tab toggle
- Include comprehensive `allow` rules for the operations you need
- Add `deny` rules for dangerous operations
- The `disableBypassPermissionsMode` field only accepts `"disable"` as a value (to disable bypass mode)

<!-- section_id: "bddb9aaf-4a22-45be-a4b6-d54c574025e7" -->
### Full Documentation

See [bypass-permissions-setup.md](./bypass-permissions-setup.md) for complete details.

<!-- section_id: "a43c8382-aa7b-44b1-804f-db9fd5fec5d2" -->
## Need Help?

- **Security concerns?** Read [Security Best Practices](./bypass-permissions-setup.md#security-best-practices)
- **Not working?** See [Troubleshooting](./bypass-permissions-setup.md#troubleshooting)
- **Enterprise environment?** Check [Enterprise Policies](./bypass-permissions-setup.md#enterprise-policy-enforcement)
