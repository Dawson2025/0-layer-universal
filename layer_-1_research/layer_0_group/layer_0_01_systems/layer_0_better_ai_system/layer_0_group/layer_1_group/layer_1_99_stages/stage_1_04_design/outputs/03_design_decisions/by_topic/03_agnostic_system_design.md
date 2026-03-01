# AGNOSTIC System Design

**Date**: 2026-01-30
**Stage**: stage_-1_04_design
**Status**: FINISHED - Ready for Planning
**Revision**: 1.0

---

## Architecture Overview

```
┌───────────────────────────────────────────────────────────────────┐
│                    AGNOSTIC System Architecture                   │
├───────────────────────────────────────────────────────────────────┤
│                                                                    │
│  Single Source of Truth                                           │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │              0AGNOSTIC.md                                   │  │
│  │  (Tool-agnostic, lean context ~200 tokens)                 │  │
│  │                                                              │  │
│  │  - Identity (role, layer, stage, scope)                    │  │
│  │  - Navigation (where to find detailed info)                │  │
│  │  - Triggers (when to load what)                           │  │
│  │  - Pointers (key locations and files)                      │  │
│  └────────────┬────────────────────────────────────────────────┘  │
│               │                                                     │
│               │                                                     │
│  On-Demand Resources                                               │
│  ┌────────────▼────────────────────────────────────────────────┐  │
│  │              .0agnostic/ folder                              │  │
│  │  (Loaded only when needed)                                  │  │
│  │                                                              │  │
│  │  ├─ skills/                                                 │  │
│  │  │  ├─ skill_1/SKILL.md                                    │  │
│  │  │  ├─ skill_2/SKILL.md                                    │  │
│  │  │                                                          │  │
│  │  ├─ rules/                                                 │  │
│  │  │  ├─ multi_agent_sync_protocol.md                       │  │
│  │  │  ├─ conflict_resolution.md                             │  │
│  │  │                                                          │  │
│  │  ├─ agents/                                                │  │
│  │  │  ├─ example_agent.md                                   │  │
│  │  │                                                          │  │
│  │  └─ templates/                                             │  │
│  │     └─ resource_template.md                                │  │
│  └────────────┬────────────────────────────────────────────────┘  │
│               │                                                     │
│               │  agnostic-sync.sh (Transformation)                │
│               │  Generates tool-specific formats                  │
│               │                                                     │
│      ┌────────┼────────┬──────────┐                                │
│      │        │        │          │                                │
│      ▼        ▼        ▼          ▼                                │
│   CLAUDE.md AGENTS.md GEMINI.md  OPENAI.md                        │
│   (Claude)  (AutoGen) (Gemini)   (ChatGPT)                        │
│   (Committed) (Ignored) (Ignored) (Ignored)                       │
│                                                                    │
└───────────────────────────────────────────────────────────────────┘
```

---

## Component 1: 0AGNOSTIC.md Structure

### Design

**File Location**: `[layer/stage]/0AGNOSTIC.md`

**Content Structure**:

```markdown
# 0AGNOSTIC.md - [Layer Name] / [Stage Name]

## Identity
[Who am I? Role, layer, stage, scope, parent, children]

## Navigation
[How do I understand this system? Self, detailed context, universal rules, scope]

## Triggers
[When should I use what? Table with triggers and actions]

## Pointers
[Where are key resources? Setup, status, help]

## Key Files
[What files matter? Self-reference, generated, on-demand, utilities]

## Standards
[What conventions apply here?]

## Skills Available
[What skills can I use? Names and purposes]

---

[Optional: Role-specific content]
```

### Token Budget

| Section | Target Tokens | Rationale |
|---------|---------------|-----------|
| Identity | 50 | Who am I? |
| Navigation | 40 | Where to find things |
| Triggers | 60 | When to use what |
| Pointers | 50 | Key locations |
| Key Files | 40 | Important files |
| Standards | 30 | Rules to follow |
| Skills | 40 | Available tools |
| **TOTAL** | **310** | **Leaves 90 tokens buffer** |

**Constraint**: Never exceed 400 tokens (or won't fit in small context windows)

### Content Rules

1. **Use Tables Instead of Prose**
   - ✅ `| Trigger | Action |` (efficient)
   - ❌ "When you need to..." (verbose)

2. **Use Relative Links**
   - ✅ `.0agnostic/rules/` (works from any tool)
   - ❌ `/home/user/...` (tool-specific)

3. **Reference Not Repeat**
   - ✅ "See `.0agnostic/rules/` for detailed protocol" (pointer)
   - ❌ "The protocol is... [200 words]" (inline)

4. **Priority Order**
   - Most important first: Identity > Navigation > Triggers
   - Details later: Standards > Skills > Key Files

---

## Component 2: .0agnostic/ Folder Structure

### Design

**Location**: `[layer/stage]/.0agnostic/`

**Standard Layout**:

```
.0agnostic/
├── README.md                         ← Overview of all resources
├── rules/
│   ├── [topic1].md
│   ├── [topic2].md
│   └── ...
├── skills/
│   ├── [skill1]/
│   │   ├── SKILL.md                 ← Official Anthropic format
│   │   ├── scripts/
│   │   │   └── [implementation].sh
│   │   └── references/
│   │       └── [docs].md
│   └── [skill2]/
│       └── SKILL.md
├── agents/
│   ├── [example_agent1].md
│   └── [example_agent2].md
├── automation/
│   ├── setup.sh
│   ├── validate.sh
│   └── repair.sh
└── templates/
    ├── [template1].md
    └── [template2].md
```

### Content Placement Rules

| Type | Location | When to Move to .0agnostic/ |
|------|----------|-----|
| Identity/Triggers | 0AGNOSTIC.md | (Always) |
| Detailed rules | .0agnostic/rules/ | >50 lines |
| Skill definitions | .0agnostic/skills/ | (Always) |
| Examples | .0agnostic/agents/ | Usage examples |
| Setup scripts | .0agnostic/automation/ | (Always) |
| Templates | .0agnostic/templates/ | (Always) |

### Naming Convention

**Consistency matters for discoverability:**

- ✅ `.0agnostic/` (sorts first)
- ❌ `.agnostic/` (sorts alphabetically)

- ✅ `0AGNOSTIC.md` (sorts first)
- ❌ `AGNOSTIC.md` (sorts alphabetically)

- ✅ Numbered patterns: `01_research/`, `02_design/`
- ❌ Mixed: `research/`, `02_design/`

---

## Component 3: agnostic-sync.sh Transformation

### Design

**Purpose**: Transform 0AGNOSTIC.md + .0agnostic/ into tool-specific formats

**Input**:
- `0AGNOSTIC.md` (source of truth)
- `.0agnostic/` (detailed resources)

**Outputs**:
- `CLAUDE.md` (Claude Code format)
- `AGENTS.md` (AutoGen format)
- `GEMINI.md` (Gemini format)

### Transformation Rules

**For CLAUDE.md** (Claude Code native):

```
Input: 0AGNOSTIC.md
Output: CLAUDE.md

Transformation:
  1. Copy 0AGNOSTIC.md content as-is (Claude native format)
  2. Add header: "# [Auto-generated from 0AGNOSTIC.md]"
  3. Add header: "# DO NOT EDIT - Edit 0AGNOSTIC.md, then run: agnostic-sync.sh"
  4. Append generated timestamp
  5. Optionally embed .0agnostic/rules/ as reference
```

**For AGENTS.md** (AutoGen format):

```
Input: 0AGNOSTIC.md + .0agnostic/
Output: AGENTS.md (YAML format)

Transformation:
  1. Extract Identity section → agent configuration
  2. Extract Triggers/Skills → agent capabilities
  3. List .0agnostic/skills/ as available tools
  4. List .0agnostic/rules/ as constraints
  5. Format as YAML for AutoGen consumption

Example output:
  agent:
    name: research_01
    description: Research agent for stage 02
    model: gpt-4
    tools: [skill_1, skill_2]
    constraints: [multi_agent_sync, episodic_logging]
```

**For GEMINI.md** (Gemini/Bard format):

```
Input: 0AGNOSTIC.md + .0agnostic/
Output: GEMINI.md (system prompt format)

Transformation:
  1. Convert to system prompt style
  2. Merge identity + key constraints
  3. Format tools as function descriptions
  4. Flatten hierarchy into linear prose
  5. Ensure <4000 token limit for Gemini
```

### Sync Algorithm

```
Function: agnostic_sync(directory, flags):
  if directory doesn't have 0AGNOSTIC.md:
    error("No 0AGNOSTIC.md found")
    return false

  if flags.dry_run:
    show_what_would_be_generated()
    return true

  // Generate CLAUDE.md
  claude_content = read(0AGNOSTIC.md)
  claude_content = add_header(claude_content, "Auto-generated")
  claude_content = add_timestamp(claude_content)
  write(CLAUDE.md, claude_content)

  // Generate AGENTS.md
  agents_content = transform_to_yaml(0AGNOSTIC.md, .0agnostic/)
  write(AGENTS.md, agents_content)

  // Generate GEMINI.md
  gemini_content = transform_to_system_prompt(0AGNOSTIC.md, .0agnostic/)
  write(GEMINI.md, gemini_content)

  // Don't overwrite tool-specific files
  preserve_files = ["settings.json", "mcp.json"]
  for file in preserve_files:
    if exists(file):
      log("Preserved: " + file)

  log("Sync complete. Generated: CLAUDE.md, AGENTS.md, GEMINI.md")
  return true
```

### File Preservation

**NEVER overwrite these files during sync:**

```
preserve_patterns = [
  "settings.json",           # Tool settings
  "mcp.json",                # MCP server configs
  ".claude/mcp.json",        # Claude-specific
  ".claude/commands/*",      # Custom commands
  ".claude/scripts/*",       # Custom scripts
  "status.json"              # Current status
]
```

**Preserve by excluding from write**:

```
// When writing CLAUDE.md:
if file_exists(CLAUDE.md):
  existing_content = read(CLAUDE.md)
  // Preserve anything after [CUSTOM] marker
  custom_section = extract_after_marker(existing_content, "[CUSTOM]")

  generated = transform(0AGNOSTIC.md)
  final = generated + custom_section

  write(CLAUDE.md, final)
```

---

## Component 4: Tool-Specific Generation Templates

### CLAUDE.md Template

```markdown
# CLAUDE.md - [Auto-generated from 0AGNOSTIC.md]

**DO NOT EDIT** - Edit `0AGNOSTIC.md` instead, then run: `agnostic-sync.sh`
**Generated**: 2026-01-30T15:02:45Z

---

[Content from 0AGNOSTIC.md]

---

## [CUSTOM]

[Anything after this marker is preserved during sync]
```

### AGENTS.md Template

```yaml
# agents.yml - Auto-generated from 0AGNOSTIC.md

version: 1.0
generated: "2026-01-30T15:02:45Z"

agents:
  - name: [role from identity]
    description: [from 0AGNOSTIC.md]
    model: gpt-4
    system_prompt: |
      [Identity content from 0AGNOSTIC.md]
    tools:
      - [skill 1 from .0agnostic/skills/]
      - [skill 2]
    constraints:
      - [rule 1 from .0agnostic/rules/]
      - [rule 2]
```

### GEMINI.md Template

```markdown
# System Prompt - Auto-generated from 0AGNOSTIC.md

**DO NOT EDIT** - Generated from 0AGNOSTIC.md

---

You are [role from 0AGNOSTIC.md].

Your responsibilities:
[From 0AGNOSTIC.md triggers and pointers]

Your constraints:
[From .0agnostic/rules/]

Use these tools when needed:
[From .0agnostic/skills/]

When in doubt, refer to: [Key files from 0AGNOSTIC.md]
```

---

## Component 5: Git Integration

### Design

**What to Commit**:

```bash
git add 0AGNOSTIC.md
git add .0agnostic/
git add agnostic-sync.sh
git commit -m "[AI Context] Updated AGNOSTIC system at [layer/stage]"
git push
```

**What to Ignore** (add to .gitignore):

```bash
# Generated files (regenerate with agnostic-sync.sh)
CLAUDE.md
AGENTS.md
GEMINI.md

# Don't commit tool-specific directories
.claude/skills/
.claude/scripts/
.claude/commands/

# Don't commit lock files or temp
.locks/
*.tmp
```

### Workflow

```
Session 1:
  1. Edit 0AGNOSTIC.md to fix a role
  2. Run ./agnostic-sync.sh
  3. CLAUDE.md updated automatically
  4. git add 0AGNOSTIC.md
  5. git commit -m "[AI Context] Updated role description"

Session 2 (Different Tool):
  1. Copy 0AGNOSTIC.md to Gemini context
  2. /find "resources" → points to .0agnostic/
  3. Load specific skills from .0agnostic/skills/
  4. Or: Run agnostic-sync.sh in that directory
  5. Copy GEMINI.md to your tool
  6. Same context, different tool!
```

---

## Component 6: Extension Mechanism

### Adding New Skills

**To add a skill**:

1. Create `.0agnostic/skills/[skill_name]/SKILL.md`
2. Reference in `0AGNOSTIC.md` Triggers section
3. Run `agnostic-sync.sh`
4. Skill now available in CLAUDE.md, AGENTS.md, GEMINI.md

**SKILL.md Format** (Anthropic standard):

```yaml
# .0agnostic/skills/[skill_name]/SKILL.md

## Purpose
Brief description of skill purpose

## Usage
/skill_name [arguments]
Examples with /skill_name

## Inputs
- argument1: description
- argument2: description

## Outputs
Description of what the skill produces

## Examples
/skill_name example_input → example_output
```

### Adding New Rules

**To add a rule**:

1. Create `.0agnostic/rules/[rule_name].md`
2. Reference in `0AGNOSTIC.md` Triggers section
3. Run `agnostic-sync.sh`
4. Rule now embedded in generated files

---

## Testing Strategy

### Unit Tests

- [ ] 0AGNOSTIC.md parses correctly
- [ ] Token count < 400
- [ ] Required sections present
- [ ] Links are relative and correct

### Sync Tests

- [ ] agnostic-sync.sh generates CLAUDE.md
- [ ] agnostic-sync.sh generates AGENTS.md
- [ ] agnostic-sync.sh generates GEMINI.md
- [ ] Tool-specific files preserved
- [ ] Dry-run shows accurate preview

### Integration Tests

- [ ] CLAUDE.md usable in Claude Code
- [ ] AGENTS.md usable in AutoGen
- [ ] GEMINI.md usable in Gemini
- [ ] Same 0AGNOSTIC.md works across tools

---

## Implementation Checklist

- [ ] Design 0AGNOSTIC.md template
- [ ] Create .0agnostic/ folder structure template
- [ ] Implement agnostic-sync.sh script
- [ ] Create transformation rules for each tool
- [ ] Test sync with sample directory
- [ ] Create .gitignore for generated files
- [ ] Document extension mechanism
- [ ] Create skill examples
- [ ] Create rule examples
- [ ] Test cross-tool functionality

