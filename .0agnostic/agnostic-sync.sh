#!/bin/bash
#
# agnostic-sync.sh - Transform 0AGNOSTIC.md into tool-specific context files
#
# Usage: ./agnostic-sync.sh [directory]
#        If no directory specified, uses current directory
#
# Generates:
#   - CLAUDE.md (Claude Code format)
#   - AGENTS.md (AutoGen format)
#   - GEMINI.md (Google Gemini format)
#   - OPENAI.md (OpenAI format)
#

set -e

# Directory to process
DIR="${1:-.}"

# Check if 0AGNOSTIC.md exists
if [ ! -f "$DIR/0AGNOSTIC.md" ]; then
    echo "Error: 0AGNOSTIC.md not found in $DIR"
    exit 1
fi

echo "Processing 0AGNOSTIC.md in $DIR..."

# Read 0AGNOSTIC.md content
AGNOSTIC_CONTENT=$(cat "$DIR/0AGNOSTIC.md")

# Extract key sections (use ^## [^#] to match only h2 headings, not h3/h4)
IDENTITY=$(echo "$AGNOSTIC_CONTENT" | sed -n '/^## Identity/,/^## [^#]/p' | head -n -1)
NAVIGATION=$(echo "$AGNOSTIC_CONTENT" | sed -n '/^## Navigation/,/^## [^#]/p' | head -n -1)
CRITICAL_RULES=$(echo "$AGNOSTIC_CONTENT" | sed -n '/^## Critical Rules/,/^## [^#]/p' | head -n -1)
BEHAVIORS=$(echo "$AGNOSTIC_CONTENT" | sed -n '/^## Key Behaviors/,/^## [^#]/p' | head -n -1)
TRIGGERS=$(echo "$AGNOSTIC_CONTENT" | sed -n '/^## Triggers/,/^## [^#]/p' | head -n -1)

# Validation: Check if critical sections were extracted
WARNINGS=0

if [ -z "$IDENTITY" ] || [ ${#IDENTITY} -lt 10 ]; then
    echo "WARNING: ## Identity section not found or too short"
    WARNINGS=$((WARNINGS + 1))
fi

if [ -z "$NAVIGATION" ] || [ ${#NAVIGATION} -lt 10 ]; then
    echo "WARNING: ## Navigation section not found or too short"
    WARNINGS=$((WARNINGS + 1))
fi

if [ -z "$CRITICAL_RULES" ]; then
    echo "INFO: ## Critical Rules section not found (optional)"
fi

if [ -z "$BEHAVIORS" ]; then
    echo "INFO: ## Key Behaviors section not found (optional)"
fi

if [ -z "$TRIGGERS" ]; then
    echo "INFO: ## Triggers section not found (optional)"
fi

if [ $WARNINGS -gt 1 ]; then
    echo "ERROR: Multiple critical sections missing. Check 0AGNOSTIC.md format."
    echo "Required sections: ## Identity, ## Navigation"
    exit 1
fi

# Generate CLAUDE.md
cat > "$DIR/CLAUDE.md" << 'CLAUDE_EOF'
# Claude Code Context

CLAUDE_EOF

echo "$IDENTITY" >> "$DIR/CLAUDE.md"
echo "" >> "$DIR/CLAUDE.md"
echo "$NAVIGATION" >> "$DIR/CLAUDE.md"
echo "" >> "$DIR/CLAUDE.md"
echo "$CRITICAL_RULES" >> "$DIR/CLAUDE.md"
echo "" >> "$DIR/CLAUDE.md"
echo "$BEHAVIORS" >> "$DIR/CLAUDE.md"
echo "" >> "$DIR/CLAUDE.md"
echo "$TRIGGERS" >> "$DIR/CLAUDE.md"
echo "" >> "$DIR/CLAUDE.md"

cat >> "$DIR/CLAUDE.md" << 'CLAUDE_RULES'

## Claude-Specific Rules

### CLAUDE.md Integration
This file is auto-generated from 0AGNOSTIC.md. Edit 0AGNOSTIC.md to make changes.

### Tool Usage
- Use Read tool to load .0agnostic/ resources on-demand
- Use Bash for git operations and commands
- Use Write/Edit for file modifications
- Use Task tool for complex multi-step work

### Session Continuity
- Read .0agnostic/episodic_memory/index.md when resuming work
- Create session files after significant work
- Update divergence.log when modifying outputs

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
CLAUDE_RULES

echo "Generated: $DIR/CLAUDE.md"

# Generate AGENTS.md (AutoGen format)
cat > "$DIR/AGENTS.md" << 'AGENTS_EOF'
# AutoGen Agent Context

AGENTS_EOF

echo "$IDENTITY" >> "$DIR/AGENTS.md"
echo "" >> "$DIR/AGENTS.md"
echo "$NAVIGATION" >> "$DIR/AGENTS.md"
echo "" >> "$DIR/AGENTS.md"
echo "$CRITICAL_RULES" >> "$DIR/AGENTS.md"
echo "" >> "$DIR/AGENTS.md"
echo "$BEHAVIORS" >> "$DIR/AGENTS.md"
echo "" >> "$DIR/AGENTS.md"

cat >> "$DIR/AGENTS.md" << 'AGENTS_RULES'

## AutoGen-Specific Configuration

### Agent Registration
Register this context in your AutoGen agent configuration:

```python
agent_config = {
    "context_file": "AGENTS.md",
    "resources_dir": ".0agnostic/",
    "episodic_dir": ".0agnostic/episodic_memory/"
}
```

### Multi-Agent Coordination
- Check .locks/ before modifying shared files
- Use atomic writes (temp file → rename)
- Log changes to divergence.log
- Read session files to understand previous work

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
AGENTS_RULES

echo "Generated: $DIR/AGENTS.md"

# Generate GEMINI.md
cat > "$DIR/GEMINI.md" << 'GEMINI_EOF'
# Gemini Context

GEMINI_EOF

echo "$IDENTITY" >> "$DIR/GEMINI.md"
echo "" >> "$DIR/GEMINI.md"
echo "$NAVIGATION" >> "$DIR/GEMINI.md"
echo "" >> "$DIR/GEMINI.md"
echo "$CRITICAL_RULES" >> "$DIR/GEMINI.md"
echo "" >> "$DIR/GEMINI.md"
echo "$BEHAVIORS" >> "$DIR/GEMINI.md"

cat >> "$DIR/GEMINI.md" << 'GEMINI_RULES'

## Gemini-Specific Notes

### Context Loading
Load detailed resources from .0agnostic/ when needed:
- rules/ - Behavioral constraints
- prompts/ - Task-specific prompts
- knowledge/ - Reference information
- agents/ - Agent definitions

### Session Continuity
Maintain episodic memory in .0agnostic/episodic_memory/:
- sessions/ - Timestamped session records
- changes/ - Divergence and conflict logs
- index.md - Searchable session index

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
GEMINI_RULES

echo "Generated: $DIR/GEMINI.md"

# Generate OPENAI.md
cat > "$DIR/OPENAI.md" << 'OPENAI_EOF'
# OpenAI Context

OPENAI_EOF

echo "$IDENTITY" >> "$DIR/OPENAI.md"
echo "" >> "$DIR/OPENAI.md"
echo "$NAVIGATION" >> "$DIR/OPENAI.md"
echo "" >> "$DIR/OPENAI.md"
echo "$CRITICAL_RULES" >> "$DIR/OPENAI.md"
echo "" >> "$DIR/OPENAI.md"
echo "$BEHAVIORS" >> "$DIR/OPENAI.md"

cat >> "$DIR/OPENAI.md" << 'OPENAI_RULES'

## OpenAI-Specific Notes

### Function Calling
When using OpenAI function calling:
- Read .0agnostic/ resources for detailed instructions
- Check episodic memory for context
- Follow multi-agent sync rules for shared files

### Context Window Management
- 0AGNOSTIC.md is lean (<400 tokens)
- Load .0agnostic/ resources on-demand
- Avoid loading everything upfront

---
*Auto-generated from 0AGNOSTIC.md via agnostic-sync.sh*
*Do not edit directly - edit 0AGNOSTIC.md instead*
OPENAI_RULES

echo "Generated: $DIR/OPENAI.md"

echo ""
echo "Sync complete! Generated tool-specific files from 0AGNOSTIC.md"
echo "Files created:"
echo "  - CLAUDE.md"
echo "  - AGENTS.md"
echo "  - GEMINI.md"
echo "  - OPENAI.md"
