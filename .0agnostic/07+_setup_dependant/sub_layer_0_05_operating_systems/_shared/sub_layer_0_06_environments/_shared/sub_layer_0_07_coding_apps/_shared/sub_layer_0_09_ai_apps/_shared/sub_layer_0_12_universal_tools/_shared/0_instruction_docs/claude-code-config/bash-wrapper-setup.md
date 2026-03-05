---
resource_id: "f75bdbb6-5256-4776-97b5-67c911f81354"
resource_type: "document"
resource_name: "bash-wrapper-setup"
---
# Claude Code Bash Wrapper Setup Guide
*Advanced Configuration: Conditional Bypass Permissions via Shell Wrapper*

<!-- section_id: "665e639e-4664-4cce-85fe-6048f9ae817c" -->
## Overview

This guide documents how to create a bash wrapper function that conditionally enables bypass permissions based on your current directory or environment variables. This approach provides more flexibility than configuration files alone.

<!-- section_id: "bc7bebfd-c8ed-4751-abb3-24df6336a76b" -->
## Why Use a Bash Wrapper?

<!-- section_id: "dcfe79fc-c0a0-473b-8501-1f2afa03a4ca" -->
### Advantages

✅ **Context-Aware Bypass**
- Enable bypass only in specific directories
- Control via environment variables
- Different behavior per project

✅ **No Configuration File Changes**
- Works without modifying `.claude/settings.json`
- Doesn't affect version-controlled settings
- Easy to enable/disable globally

✅ **Granular Control**
- Per-directory automation
- Per-session control via environment variables
- Preserves help/version commands

<!-- section_id: "89a72e3c-824c-4803-8687-f9f1b5abad93" -->
### Disadvantages

❌ **Shell-Specific**
- Only works in bash/zsh
- Doesn't affect Claude Code launched from GUI
- Must configure each shell environment

❌ **Less Discoverable**
- Hidden in shell config files
- Team members won't automatically get it
- Harder to audit than configuration files

<!-- section_id: "89308c23-72d2-4c01-9a4d-5c0b11d7f651" -->
## Implementation

<!-- section_id: "cab0ab7c-3e96-4a25-854d-61234eb8ab68" -->
### Method 1: Project Directory-Based Bypass

This wrapper enables bypass permissions automatically when you're in a specific project directory.

#### Step 1: Find Claude Binary Path

```bash
which claude
# Output example: /home/username/.nvm/versions/node/v22.20.0/bin/claude
```

Store this path - you'll need it for the wrapper.

#### Step 2: Add Wrapper to ~/.bashrc

Open your `~/.bashrc` (or `~/.zshrc` for zsh):

```bash
nano ~/.bashrc
```

Add this function at the end:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when in project directory
    if [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Important**: Replace:
- `/home/username/.nvm/versions/node/v22.20.0/bin/claude` with your actual path from step 1
- `/home/username/code/my-project` with your project path

#### Step 3: Reload Shell Configuration

```bash
source ~/.bashrc
```

#### Step 4: Verify Wrapper

```bash
# Check the wrapper function exists
typeset -f claude

# Test inside your project directory
cd /home/username/code/my-project
claude -p "echo 'testing bypass'"
# Should run without permission prompts

# Test outside your project directory
cd /tmp
claude -p "echo 'testing normal'"
# Should run with normal permission behavior
```

<!-- section_id: "e031fded-9274-43b5-a7f0-e866993413b3" -->
### Method 2: Environment Variable-Based Bypass

Enable bypass permissions on-demand with an environment variable.

```bash
# >>> CLAUDE_WRAPPER_ENV_VAR_START
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_ENV_VAR_END
```

**Usage:**

```bash
# Normal mode (with permissions)
claude

# Bypass mode (for this session)
CLAUDE_UNSAFE=1 claude

# Or set for entire session
export CLAUDE_UNSAFE=1
claude
# ... work without prompts ...
unset CLAUDE_UNSAFE  # Back to normal
```

<!-- section_id: "6a31c71a-1283-49cb-bb54-06756f3c2841" -->
### Method 3: Combined Approach (Recommended)

Combine both methods for maximum flexibility:

```bash
# >>> CLAUDE_WRAPPER_COMBINED_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/username/.nvm/versions/node/v22.20.0/bin/claude"

if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 OR in project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/my-project"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_COMBINED_END
```

**Behavior:**
- Inside `/home/username/code/my-project`: Bypass enabled automatically
- Outside that directory: Normal permissions
- Anywhere with `CLAUDE_UNSAFE=1`: Bypass enabled
- `--help` and `--version`: Always work normally

<!-- section_id: "412b3483-6df2-4d07-b4f8-5116a711899d" -->
## Real-World Example

Here's the exact wrapper from the Lang-Trak project:

```bash
# >>> CLAUDE_WRAPPER_CONDITIONAL_START
# Claude Code: conditional permissions bypass wrapper
_claude_real="/home/dawson/.nvm/versions/node/v22.20.0/bin/claude"
if [ -x "$_claude_real" ]; then
  claude() {
    # Preserve help/version behavior
    for arg in "$@"; do
      case "$arg" in
        --help|-h|--version|-v)
          command "$_claude_real" "$@"
          return $?
          ;;
      esac
    done

    # Enable bypass when CLAUDE_UNSAFE=1 or when in the project directory
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/dawson/code/lang-trak-in-progress"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  }
fi
# <<< CLAUDE_WRAPPER_CONDITIONAL_END
```

**Testing Results:**
```bash
# Inside project
$ cd /home/dawson/code/lang-trak-in-progress
$ claude -p "echo hello"
hello  # No permission prompt

# Outside project
$ cd /tmp
$ claude -p "echo hello"
# Permission prompt appears (normal behavior)

# Override from outside project
$ cd /tmp
$ CLAUDE_UNSAFE=1 claude -p "echo hello"
hello  # No permission prompt
```

<!-- section_id: "73af4f93-e529-441d-becf-316a0c9928a8" -->
## Advanced Configurations

<!-- section_id: "f8712bae-b8cd-4d25-bd3b-7eef03319f4d" -->
### Multiple Project Directories

Enable bypass for multiple projects:

```bash
claude() {
  # ... help/version handling ...

  # List of trusted project directories
  local trusted_dirs=(
    "/home/username/code/personal-project"
    "/home/username/code/side-project"
    "/home/username/experiments"
  )

  # Check if current directory starts with any trusted path
  local bypass=0
  for dir in "${trusted_dirs[@]}"; do
    if [[ "$PWD" == "$dir"* ]]; then
      bypass=1
      break
    fi
  done

  # Enable bypass if in trusted directory or CLAUDE_UNSAFE=1
  if [ "$bypass" = "1" ] || [ "${CLAUDE_UNSAFE:-0}" = "1" ]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "7f5bc529-5ae8-4509-ab85-f09f783774f0" -->
### Time-Based Bypass

Automatically disable bypass during certain hours (e.g., working hours for client projects):

```bash
claude() {
  # ... help/version handling ...

  # Get current hour (0-23)
  local hour=$(date +%H)

  # Disable bypass during working hours (9 AM - 5 PM)
  if [ "$hour" -ge 9 ] && [ "$hour" -lt 17 ]; then
    # Normal mode during work hours
    command "$_claude_real" "$@"
  else
    # Bypass enabled outside work hours
    if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/personal"* ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  fi
}
```

<!-- section_id: "ecdb24b4-18b4-40f2-aa3e-68700224b7e4" -->
### Git Repository Detection

Enable bypass only in git repositories you own:

```bash
claude() {
  # ... help/version handling ...

  # Check if in a git repo
  if git rev-parse --git-dir > /dev/null 2>&1; then
    # Get git user email
    local git_email=$(git config user.email)

    # Enable bypass if it's your personal email
    if [[ "$git_email" == "personal@example.com" ]]; then
      command "$_claude_real" --dangerously-skip-permissions "$@"
    else
      command "$_claude_real" "$@"
    fi
  else
    # Not in a git repo - normal mode
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "29c67905-0d6a-4120-90f7-bc54412cbf0c" -->
## Debugging

<!-- section_id: "eaa22d7b-edcc-404c-b268-b892a6c78207" -->
### Check if Wrapper is Active

```bash
# View the current wrapper function
typeset -f claude

# Check which claude command is being used
type claude
# Should output: claude is a function
```

<!-- section_id: "3b05323b-0fe3-47ed-ba57-24eb5c822b3e" -->
### Test Without Wrapper

To temporarily bypass the wrapper and use the real binary:

```bash
# Use full path
/home/username/.nvm/versions/node/v22.20.0/bin/claude

# Or use command builtin
command /path/to/real/claude
```

<!-- section_id: "da77c499-b2a7-4ec3-8cfb-232496348f08" -->
### Enable Debug Output

Add debugging to your wrapper:

```bash
claude() {
  # Debug mode
  if [ "${CLAUDE_DEBUG:-0}" = "1" ]; then
    echo "[DEBUG] PWD: $PWD"
    echo "[DEBUG] CLAUDE_UNSAFE: ${CLAUDE_UNSAFE:-0}"
    echo "[DEBUG] Will use bypass: $([ condition ] && echo yes || echo no)"
  fi

  # ... rest of wrapper ...
}
```

Usage:
```bash
CLAUDE_DEBUG=1 claude -p "echo test"
```

<!-- section_id: "c7b4c07f-4c1c-4740-a2b2-7b2fc226215e" -->
## Removing the Wrapper

<!-- section_id: "7f6ee52a-8799-4c6d-b98b-97c687ba42b7" -->
### Temporary Removal (Current Session)

```bash
unset -f claude
```

<!-- section_id: "2c238898-d757-4e7e-ade3-2a956a12f2d3" -->
### Permanent Removal

1. Edit `~/.bashrc`:
   ```bash
   nano ~/.bashrc
   ```

2. Remove the wrapper block (between the comment markers)

3. Reload shell:
   ```bash
   source ~/.bashrc
   ```

4. Verify:
   ```bash
   type claude
   # Should output the path to the binary, not "claude is a function"
   ```

<!-- section_id: "5909f76e-b6b8-40d7-88bb-13d50d4919d8" -->
## Security Considerations

<!-- section_id: "4540c201-17ce-4891-8b02-00c68d2667a2" -->
### Risks

⚠️ **Directory-Based Bypass**
- Anyone with access to the directory gets bypass mode
- Symbolic links could potentially exploit path matching
- Subdirectories inherit bypass behavior

⚠️ **Environment Variable Bypass**
- Environment variables can be set by scripts
- Child processes inherit `CLAUDE_UNSAFE=1`
- Easy to forget it's enabled

⚠️ **Shell Configuration Files**
- `~/.bashrc` is executable code
- Errors can break your shell
- Hard for others to discover the bypass is active

<!-- section_id: "f486cba7-fb81-48d5-b56c-2603afc74edd" -->
### Mitigations

✅ **Add Visual Indicators**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "⚠️  BYPASS MODE ACTIVE" >&2
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Log Bypass Usage**

```bash
claude() {
  # ... condition checks ...

  if [ "$using_bypass" = "1" ]; then
    echo "$(date): Bypass enabled in $PWD" >> ~/.claude/bypass.log
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

✅ **Restrict by Ownership**

```bash
claude() {
  # Only enable bypass if you own the directory
  if [ -O "$PWD" ] && [[ "$PWD" == "/home/username/code"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

<!-- section_id: "411a534a-d26a-4f5c-88f4-a9a5698e36ce" -->
## Integration with Configuration Files

The bash wrapper approach **works alongside** `.claude/settings.json` configurations:

<!-- section_id: "7c453a7d-1417-410a-b2cb-9963c762ceb4" -->
### Precedence

1. **Bash Wrapper** (highest)
   - If wrapper adds `--dangerously-skip-permissions`, that takes effect

2. **Command-Line Flags**
   - Flags passed to the wrapper are forwarded

3. **Configuration Files**
   - `.claude/settings.json` and `.claude/settings.local.json`
   - Still respected when wrapper doesn't add bypass flag

<!-- section_id: "05d5588c-bc49-4f6f-ab15-658855ee08b9" -->
### Example: Hybrid Approach

```bash
# ~/.bashrc - Project directory gets wrapper bypass
claude() {
  if [[ "$PWD" == "/home/username/code/personal"* ]]; then
    command "$_claude_real" --dangerously-skip-permissions "$@"
  else
    command "$_claude_real" "$@"
  fi
}
```

```json
// /home/username/code/work-project/.claude/settings.local.json
// Work project uses fine-grained permissions
{
  "permissions": {
    "allow": [
      "Read(src/**)",
      "Edit(src/**)",
      "Bash(npm test)"
    ]
  }
}
```

**Result:**
- Personal projects: Full bypass via wrapper
- Work projects: Fine-grained permissions via config files
- Other directories: Default Claude Code behavior

<!-- section_id: "b35d1217-c0df-4d6f-b850-cdc3e8cbcf3b" -->
## Frequently Asked Questions

<!-- section_id: "f2b6f3fb-5cdd-449c-bad2-d83c4dc16d8c" -->
### Q: Does this work with VS Code?

**A**: Only if you launch Claude Code from the terminal. If you launch VS Code from a GUI, it won't inherit your shell configuration.

**Workaround**: Set environment variables in VS Code settings:
```json
{
  "terminal.integrated.env.linux": {
    "CLAUDE_UNSAFE": "1"
  }
}
```

<!-- section_id: "7a2ab1a2-8c19-4bd1-a9e0-94a2d622b9e4" -->
### Q: Can I use this with zsh?

**A**: Yes, the syntax is compatible. Just add the wrapper to `~/.zshrc` instead of `~/.bashrc`.

<!-- section_id: "2cce4faf-bf0b-45a2-84aa-52a89edf243d" -->
### Q: What about fish shell?

**A**: Fish uses different syntax. Here's the equivalent:

```fish
# ~/.config/fish/functions/claude.fish
function claude
    set -l claude_real /home/username/.nvm/versions/node/v22.20.0/bin/claude

    # Check for help/version
    for arg in $argv
        switch $arg
            case --help -h --version -v
                command $claude_real $argv
                return
        end
    end

    # Enable bypass in project directory
    if string match -q "/home/username/code/my-project*" $PWD
        command $claude_real --dangerously-skip-permissions $argv
    else
        command $claude_real $argv
    end
end
```

<!-- section_id: "cae0672d-a9d6-4436-aee9-b23aa18cd7aa" -->
### Q: Can I check if bypass is active before running a command?

**A**: Yes, add a helper function:

```bash
claude-bypass-check() {
  if [ "${CLAUDE_UNSAFE:-0}" = "1" ] || [[ "$PWD" == "/home/username/code/trusted"* ]]; then
    echo "✅ Bypass ACTIVE"
  else
    echo "❌ Bypass INACTIVE (normal permissions)"
  fi
}
```

Usage:
```bash
$ claude-bypass-check
✅ Bypass ACTIVE
```

<!-- section_id: "912051b1-4006-404b-a7d3-4a270c87effb" -->
### Q: How do I share this with my team?

**A**: Document it in your project's README and provide a setup script:

```bash
#!/bin/bash
# scripts/setup-claude-wrapper.sh

CLAUDE_PATH=$(which claude)
PROJECT_PATH=$(pwd)

cat >> ~/.bashrc << EOF

# Auto-generated Claude wrapper for $(basename "$PROJECT_PATH")
_claude_real="$CLAUDE_PATH"
if [ -x "\$_claude_real" ]; then
  claude() {
    for arg in "\$@"; do
      case "\$arg" in
        --help|-h|--version|-v)
          command "\$_claude_real" "\$@"
          return \$?
          ;;
      esac
    done

    if [[ "\$PWD" == "$PROJECT_PATH"* ]]; then
      command "\$_claude_real" --dangerously-skip-permissions "\$@"
    else
      command "\$_claude_real" "\$@"
    fi
  }
fi
EOF

echo "✅ Claude wrapper added to ~/.bashrc"
echo "Run: source ~/.bashrc"
```

<!-- section_id: "9c7e2fd9-9977-4064-9830-d7f917f7adaf" -->
## Related Documentation

- [Bypass Permissions Setup](./bypass-permissions-setup.md) - Configuration file approach
- [Fine-Grained Permissions](./fine-grained-permissions.md) - Alternative to bypass mode
- [Settings Hierarchy](./settings-hierarchy.md) - How settings interact

<!-- section_id: "096b0128-7dc9-461a-9cd4-c4186ca7a4cb" -->
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0   | 2025-10-24 | Initial documentation created |

---
*This guide is part of the Universal Tools (Level 0.75) and provides advanced implementation patterns for Claude Code bypass permissions.*
