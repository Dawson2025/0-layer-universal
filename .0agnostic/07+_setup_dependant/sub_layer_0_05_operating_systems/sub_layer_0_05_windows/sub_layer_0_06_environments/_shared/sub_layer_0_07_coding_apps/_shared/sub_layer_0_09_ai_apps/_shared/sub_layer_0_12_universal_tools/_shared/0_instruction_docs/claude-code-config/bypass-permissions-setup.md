---
resource_id: "bb01e993-bece-42ef-a189-522fd64ef877"
resource_type: "document"
resource_name: "bypass-permissions-setup"
---
# Claude Code Bypass Permissions Setup Guide
*Universal Configuration for Trusted Development Environments*

<!-- section_id: "7eee8515-e0b2-4e15-9fbb-acfea3a2d61f" -->
## Overview

Bypass permissions mode allows Claude Code to operate without permission prompts, enabling autonomous development in trusted environments. This guide covers configuration, implementation, and security considerations.

<!-- section_id: "caf09e54-e66f-4f86-af92-9a7a65a7a8a7" -->
## ⚠️ Security Warning

**Use bypass permissions mode ONLY in:**
- Personal development projects
- Trusted local environments
- Isolated development containers
- Educational/learning projects

**NEVER use bypass mode for:**
- Shared team repositories
- Client projects with sensitive data
- Production environments
- Codebases with proprietary information
- Systems with regulatory compliance requirements

<!-- section_id: "fb20cc56-22c5-494c-91c0-9c848120f28e" -->
## Configuration Methods

<!-- section_id: "4a9fa50a-2501-4977-bdf3-8a01a70ef841" -->
### Method 1: Project-Level Configuration (Recommended)

This method enables bypass mode for a specific project while maintaining security for other projects.

#### Step 1: Create Project Settings Directory

```bash
mkdir -p .claude
```

#### Step 2: Create Settings File

Create `.claude/settings.json` in your project root:

```json
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
```

**⚠️ IMPORTANT NOTE**: The `disableBypassPermissionsMode` field does NOT work as documented. The schema only accepts `"disable"` as a value, not `false`. The correct way to enable bypass permissions mode is using `defaultMode: "bypassPermissions"` as shown above.

#### Step 3: Add to Version Control (Optional)

If this is a personal project, you can commit this file:

```bash
git add .claude/settings.json
git commit -m "Enable Claude Code bypass permissions for development"
```

**Important**: Only commit this for personal projects. For shared repositories, use `.claude/settings.local.json` instead and add it to `.gitignore`.

#### Configuration Values

| Field | Value | Behavior |
|-------|-------|----------|
| `defaultMode` | `"bypassPermissions"` | **RECOMMENDED**: Enables bypass mode and shows Shift+Tab toggle |
| `defaultMode` | `"default"` | Normal permissions mode (prompts for approval) |
| `defaultMode` | `"acceptEdits"` | Auto-accept edit operations only |
| `defaultMode` | `"plan"` | Start in planning mode |
| `disableBypassPermissionsMode` | `"disable"` | Prevents bypass mode from being activated |
| `disableBypassPermissionsMode` | Not set | Allows bypass mode but doesn't auto-enable it |

**Note**: Despite old documentation suggesting `disableBypassPermissionsMode: false`, this is **invalid**. Use `defaultMode: "bypassPermissions"` instead.

<!-- section_id: "40912108-9a4e-4856-b163-a82d1b10b231" -->
### Method 2: Command-Line Flag

Enable bypass mode for a single session without modifying configuration files:

```bash
claude --dangerously-skip-permissions
```

**Use cases:**
- One-off autonomous tasks
- Testing without modifying config
- Temporary permission bypass

**Limitations:**
- Only affects current session
- Cannot be overridden by enterprise policies
- No persistent configuration

<!-- section_id: "0eddfc85-a47b-462a-864a-88986155c3af" -->
### Method 3: User-Level Default

Set bypass mode as default for all your projects:

#### Step 1: Create User Settings Directory

```bash
mkdir -p ~/.claude
```

#### Step 2: Create User Settings File

Create `~/.claude/settings.json`:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

**Note**: Project-level settings can still override this.

<!-- section_id: "67f0b580-e3e9-47dd-b8af-748184fd6d8a" -->
### Method 4: Local Development Override

For shared repositories where you want bypass mode locally but not for the team:

#### Step 1: Create Local Settings

Create `.claude/settings.local.json`:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

#### Step 2: Add to .gitignore

Ensure `.claude/settings.local.json` is in your `.gitignore`:

```bash
echo ".claude/settings.local.json" >> .gitignore
```

This allows you to work with bypass mode while team members maintain permission prompts.

<!-- section_id: "8b358535-141b-4286-ac01-f98d00f239da" -->
## Settings Hierarchy

Claude Code reads settings in this precedence order (highest to lowest):

1. **Enterprise Managed Policies** (`managed-settings.json`)
   - Cannot be overridden
   - Deployed by IT/Security teams
   - Enforces organization-wide policies

2. **Command-Line Arguments** (`--dangerously-skip-permissions`)
   - Session-specific
   - Overrides all file-based settings except managed policies

3. **Project Local Settings** (`.claude/settings.local.json`)
   - Developer-specific overrides
   - Not version controlled
   - Highest precedence for file-based settings

4. **Project Settings** (`.claude/settings.json`)
   - Team-shared configuration
   - Version controlled
   - Project-specific defaults

5. **User Settings** (`~/.claude/settings.json`)
   - Personal defaults
   - Applies to all projects
   - Lowest precedence

<!-- section_id: "0a2c42af-c47f-4fbf-8075-9f541d0ce860" -->
### Example Hierarchy in Action

```
Enterprise Policy:     disableBypassPermissionsMode: "disable"
↓
Result: Bypass mode DISABLED (enterprise policy wins)
```

```
User Settings:         disableBypassPermissionsMode: false
Project Settings:      disableBypassPermissionsMode: "disable"
↓
Result: Bypass mode DISABLED (project settings win)
```

```
Project Settings:      disableBypassPermissionsMode: false
Local Settings:        disableBypassPermissionsMode: "disable"
↓
Result: Bypass mode DISABLED (local settings win)
```

<!-- section_id: "9e6eca22-1d13-42f3-af5b-8430acb37919" -->
## Implementation Examples

<!-- section_id: "d69821dd-0f1f-4d97-aead-6966707e1c7b" -->
### Example 1: Personal Side Project (CORRECTED)

**Scenario**: Full control, rapid development, no sensitive data

```json
// .claude/settings.json (committed to git)
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
      "Bash(npx:*)",
      "Bash(ls:*)",
      "Bash(cat:*)",
      "Bash(mkdir:*)",
      "Bash(rm:*)",
      "Bash(cp:*)",
      "Bash(mv:*)"
    ],
    "deny": [
      "Bash(rm -rf /)",
      "Bash(sudo rm -rf :*)",
      "Bash(git push --force origin main)",
      "Bash(git push --force origin master)"
    ]
  }
}
```

**Workflow:**
```bash
# Start Claude Code normally - bypass mode is enabled
claude

# You'll see the Shift+Tab toggle indicator showing bypass mode is active
# AI can autonomously perform allowed operations without prompts
# Dangerous operations (in deny list) are still blocked
```

<!-- section_id: "6405758a-24b2-4f6d-b94b-d65945e9ce35" -->
### Example 2: Shared Repository with Local Override

**Scenario**: Team project, you want bypass locally, team wants prompts

```json
// .claude/settings.json (committed - team default)
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "description": "Team project - permissions required by default"
}
```

```json
// .claude/settings.local.json (not committed - your override)
{
  "permissions": {
    "disableBypassPermissionsMode": false
  },
  "description": "Local override - bypass enabled for my development"
}
```

```bash
# Add to .gitignore
echo ".claude/settings.local.json" >> .gitignore
```

<!-- section_id: "eb4dc651-9ac1-4c7a-9ba5-98d28432b8ec" -->
### Example 3: Hybrid Approach - Selective Bypass

**Scenario**: Want bypass for most operations, but protect sensitive files

```json
// .claude/settings.json
{
  "permissions": {
    "disableBypassPermissionsMode": false,
    "deny": [
      "Read(.env)",
      "Read(.env.*)",
      "Edit(.env)",
      "Edit(.env.*)",
      "Read(config/secrets/**)",
      "Edit(config/secrets/**)",
      "Bash(rm -rf *)",
      "Bash(git push --force*)"
    ]
  },
  "description": "Bypass enabled but sensitive operations denied"
}
```

This configuration:
- Enables bypass mode for general operations
- Explicitly denies access to environment files
- Blocks destructive commands
- Provides a safety net for critical operations

<!-- section_id: "94bcb3be-979c-4425-9d4f-7e66ca88c370" -->
### Example 4: Temporary Bypass for Specific Task

**Scenario**: Need bypass for one-time refactoring, normally use permissions

```bash
# One-time use without changing configuration
claude --dangerously-skip-permissions

# Run your task
# Bypass mode only active for this session

# Next time you run claude without the flag:
claude
# Normal permission prompts return
```

<!-- section_id: "52b9f421-d0d9-4600-9c62-7af58f1a508c" -->
## Verification

<!-- section_id: "64740a82-789a-46dd-afec-10028734116a" -->
### Check Current Settings

```bash
# View current permission configuration
claude
```

Then in Claude Code:
```
/permissions
```

This shows:
- Current bypass mode status
- Active allow/deny rules
- Settings hierarchy being applied

<!-- section_id: "f3230a8d-2ab6-4269-a4ad-e90acdabffca" -->
### Test Bypass Mode

Create a test file to verify bypass is working:

```bash
# Start Claude Code
claude

# Ask Claude to create a test file
> "Create a test file called test-bypass.txt with the content 'Bypass mode active'"
```

If bypass mode is enabled:
- No permission prompt appears
- File is created immediately
- Operation completes autonomously

If bypass mode is disabled:
- Permission prompt appears
- You must approve the file creation
- Operation waits for confirmation

<!-- section_id: "66188d0b-436f-4b61-b9d8-0ccacb3aa56b" -->
## Disabling Bypass Mode

<!-- section_id: "2923c7e1-a438-4efe-80f8-6f07acea5604" -->
### Temporary Disable (Current Session)

Cannot be done - bypass is session-wide if enabled. Restart Claude Code without the flag.

<!-- section_id: "a7f3d81c-9f9c-49d6-85c4-353241d9e2e6" -->
### Permanent Disable for Project

```json
// .claude/settings.json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  }
}
```

<!-- section_id: "73ab65ab-3551-475c-b0f1-4dcafbd6f620" -->
### Remove All Bypass Configuration

```bash
# Remove project settings
rm .claude/settings.json
rm .claude/settings.local.json

# Remove user settings
rm ~/.claude/settings.json

# Claude Code will revert to default (prompts enabled)
```

<!-- section_id: "1d2ad14f-d095-4b46-9619-964bb1903f02" -->
## Enterprise Policy Enforcement

<!-- section_id: "61ded3f8-6ae6-43bb-be05-60c1cfbff635" -->
### Scenario: Organization Requires Permissions

If your organization deploys managed policies, bypass mode may be disabled regardless of your configuration.

**Managed Policy Example** (`managed-settings.json`):
```json
{
  "permissions": {
    "disableBypassPermissionsMode": "disable"
  },
  "enforced": true,
  "description": "Corporate security policy - bypass mode prohibited"
}
```

**Result**: You cannot enable bypass mode, even with:
- Project settings
- User settings
- Command-line flags

**What to do:**
1. Contact your IT/Security team
2. Request exception for specific projects
3. Explain business justification
4. Follow your organization's security approval process

<!-- section_id: "98f45664-1d99-4b47-aeef-73a880a70c02" -->
## Troubleshooting

<!-- section_id: "0c616c87-e0a2-4e3d-b053-bac41acbcf83" -->
### Shift+Tab Toggle Not Appearing

**Symptom**: Cannot see the bypass permissions mode toggle indicator in the UI

**Root Cause**: The Shift+Tab toggle only appears when `defaultMode: "bypassPermissions"` is set.

**Solution:**
1. ✅ Add `"defaultMode": "bypassPermissions"` to your settings file
2. ✅ Include comprehensive `allow` rules (see working example below)
3. ✅ Restart Claude Code

**Working Configuration:**
```json
{
  "permissions": {
    "defaultMode": "bypassPermissions",
    "allow": [
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
      "Bash(git push --force origin main)"
    ]
  }
}
```

**What DOESN'T Work:**
```json
{
  "permissions": {
    "disableBypassPermissionsMode": false  // ❌ INVALID - does not show toggle
  }
}
```

The `disableBypassPermissionsMode` field only accepts `"disable"` as a value (to prevent bypass mode). Setting it to `false` is invalid according to the schema.

<!-- section_id: "82b733a6-fe61-4e17-9e62-e9dcc2450db0" -->
### Bypass Mode Not Working

**Symptom**: Still seeing permission prompts despite configuration

**Checklist:**
1. ✅ Verify you're using `"defaultMode": "bypassPermissions"` (not `disableBypassPermissionsMode: false`)
2. ✅ Include comprehensive `allow` rules in your configuration
3. ✅ Check for enterprise managed policies
4. ✅ Ensure JSON syntax is valid
5. ✅ Verify file is in correct location (`.claude/settings.json` or `.claude/settings.local.json`)
6. ✅ Restart Claude Code after changing settings
7. ✅ Check settings precedence - higher level may override

**Diagnostic:**
```bash
# Check if settings file is valid JSON
cat .claude/settings.json | python3 -m json.tool

# Review settings hierarchy
claude
# Then: /permissions
```

<!-- section_id: "88e561e0-9c64-4ed6-af7c-00c69cb7fcce" -->
### Bypass Mode Active When It Shouldn't Be

**Symptom**: No permission prompts when you expected them

**Checklist:**
1. ✅ Check for `--dangerously-skip-permissions` flag in launch command
2. ✅ Look for `.claude/settings.local.json` override
3. ✅ Review user-level settings (`~/.claude/settings.json`)
4. ✅ Verify project settings don't enable bypass

**Fix:**
```bash
# Find all settings files
find ~ -name "settings.json" -o -name "settings.local.json" 2>/dev/null

# Review each for bypass configuration
```

<!-- section_id: "caea4006-b3ce-42d2-8e2d-dbbeee32e7c9" -->
### Specific Operations Still Require Permissions

**Symptom**: Bypass mode enabled, but some operations still prompt

**Explanation**: Deny rules override bypass mode

**Example:**
```json
{
  "permissions": {
    "disableBypassPermissionsMode": false,
    "deny": [
      "Bash(rm *)"
    ]
  }
}
```

Even with bypass enabled, `rm` commands will be denied.

**Solution**: Remove deny rules if you want full bypass, or keep them for safety.

<!-- section_id: "9b3bfa05-8f95-4376-bd56-62bb704137b3" -->
## Security Best Practices

<!-- section_id: "d5ead33b-f707-495a-b30e-0200263cb155" -->
### 1. Scope Bypass to Specific Projects

❌ **Don't do this:**
```json
// ~/.claude/settings.json (applies to ALL projects)
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

✅ **Do this instead:**
```json
// .claude/settings.json (specific project only)
{
  "permissions": {
    "disableBypassPermissionsMode": false
  }
}
```

<!-- section_id: "5a7d585e-9b0b-42a8-b7fa-9bea2437a1bd" -->
### 2. Document Why Bypass is Enabled

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false
  },
  "description": "Personal learning project - bypass enabled for rapid experimentation",
  "project": "python-automation-tools",
  "owner": "personal",
  "risk_level": "low"
}
```

<!-- section_id: "d62d510e-f141-4836-bbff-0b450383da2b" -->
### 3. Use Deny Rules for Critical Operations

Even with bypass mode, protect destructive operations:

```json
{
  "permissions": {
    "disableBypassPermissionsMode": false,
    "deny": [
      "Bash(rm -rf /)",
      "Bash(sudo rm *)",
      "Bash(git push --force*)",
      "Bash(DROP TABLE*)",
      "Edit(.git/config)",
      "Bash(curl * | bash)"
    ]
  }
}
```

<!-- section_id: "7c49dbcb-1b9d-4381-8ad3-b8a24461ce35" -->
### 4. Regular Security Reviews

Periodically review and audit your bypass configurations:

```bash
# Find all bypass configurations
find ~ -name "settings*.json" -exec grep -l "disableBypassPermissionsMode.*false" {} \;

# Review each one
# Remove bypass from projects that no longer need it
```

<!-- section_id: "ce45ab1a-2f92-48c0-bffd-2315f97facca" -->
### 5. Use Version Control Wisely

```gitignore
# .gitignore
.claude/settings.local.json   # Personal overrides
.claude/managed-settings.json # Enterprise policies
.env*                          # Secrets
```

```bash
# What TO commit
git add .claude/settings.json  # Only if personal project
```

<!-- section_id: "37f90906-eced-4b4d-9af5-455907d0fc5b" -->
## Alternative: Fine-Grained Permissions

Instead of bypassing all permissions, consider allowing specific operations:

```json
{
  "permissions": {
    "allow": [
      "Read(**)",
      "Bash(npm *)",
      "Bash(git status)",
      "Bash(git diff)",
      "Edit(src/**)",
      "Edit(tests/**)",
      "Write(docs/**)"
    ]
  }
}
```

**Benefits:**
- No permission prompts for allowed operations
- Maintains security for non-allowed operations
- More granular control than bypass mode
- Better for shared repositories

**See**: [fine-grained-permissions.md](./fine-grained-permissions.md)

<!-- section_id: "5384ac1a-c42a-4e52-8659-8fa5266df321" -->
## Frequently Asked Questions

<!-- section_id: "c2794379-d949-4611-80c9-2b9d5f302da2" -->
### Q: Is bypass mode safe for personal projects?

**A**: Yes, if:
- You fully control the repository
- No sensitive data is present
- Not connected to production systems
- You understand the implications

<!-- section_id: "afa10486-bd6f-4e9f-86d5-e3b80cbd3290" -->
### Q: Can I use bypass mode in a Docker container?

**A**: Yes, containers provide additional isolation:
```dockerfile
# Dockerfile
FROM python:3.11
WORKDIR /app
COPY .claude/settings.json .claude/
# Bypass mode contained within container
```

<!-- section_id: "195d6a9b-4375-4687-8cd1-7dc9380a0338" -->
### Q: What happens if I forget bypass mode is enabled?

**A**: Claude Code will operate autonomously without prompts. You may experience:
- Unexpected file modifications
- Commands executed without confirmation
- Potential data loss if destructive operations occur

**Mitigation**: Use deny rules for critical operations.

<!-- section_id: "fe389909-058a-4a2d-aa3f-2d6d4b29e781" -->
### Q: Can enterprise policies be bypassed?

**A**: No. Managed policies have highest precedence and cannot be overridden.

<!-- section_id: "ba344a90-ea03-4c57-a9a5-bfe4bc6ca157" -->
### Q: Does bypass mode affect MCP servers?

**A**: Historically yes (Issue #5307), though this may be fixed in newer versions. Test your specific version.

<!-- section_id: "484325d6-1732-4127-ab1e-05f2f88d6173" -->
## Related Documentation

- [Fine-Grained Permissions](./fine-grained-permissions.md)
- [Enterprise Security Policies](./enterprise-policies.md)
- [Project Settings Setup](./project-settings.md)
- [Settings Hierarchy](./settings-hierarchy.md)

<!-- section_id: "5c16031f-36ec-47ab-8a46-b1d7354fbd45" -->
## External References

- [Official Claude Code Settings Docs](https://docs.claude.com/en/docs/claude-code/settings)
- [IAM Documentation](https://docs.claude.com/en/docs/claude-code/iam)
- [Security Best Practices](https://www.anthropic.com/engineering/claude-code-best-practices)

<!-- section_id: "b9a1c7ac-accb-46d9-9f6d-19437db57bde" -->
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0   | 2025-10-24 | Initial documentation created |

---
*This guide is part of the Universal Tools (Level 0.75) and provides implementation patterns for any Claude Code project.*
