---
resource_id: "56a7c8a4-9737-4a30-8491-03f48630e80c"
resource_type: "rule"
resource_name: "AGENT_DISCOVERY_GUIDE"
---
# AI Agent Documentation Discovery Guide
*How AI Agents Find and Use Universal Documentation*

<!-- section_id: "7e28c693-311a-48e0-b34c-780280730a18" -->
## 🎯 Purpose

This guide explains how AI agents (Cursor, Codex, Gemini CLI, Claude Code, Warp, etc.) can discover and use the universal terminal execution protocol and other documentation.

<!-- section_id: "9a90ed12-0a53-4e29-a4f0-58f48cf1300c" -->
## 📍 Standard Documentation Locations

<!-- section_id: "95aac827-a195-448e-8c0d-337fdd9dd9d7" -->
### Universal Documentation (All Agents)

**Primary Location**: `0_context/trickle_down_0_universal/0_instruction_docs/`

**Key Files**:
1. **`UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`** - **START HERE** for terminal execution
2. **`universal_instructions.md`** - Core AI agent principles
3. **`terminal-tool-replacement.md`** - Complete terminal execution guide
4. **`when-to-use-terminal-wrapper.md`** - Decision guide
5. **`README.md`** - Overview of all universal systems

<!-- section_id: "030b31b6-3e82-4067-83cc-92b5dd5ce332" -->
### Agent-Specific Documentation

**Location**: `0_context/trickle-down-0.5-environment/agent-specific/`

**Files**:
- `cursor-agent-spec-kit.md` - Cursor-specific instructions
- `warp-agent-spec-kit.md` - Warp-specific instructions
- (Add more as needed)

<!-- section_id: "167d569c-e186-411f-b88c-e948c9adcddc" -->
## 🔍 Discovery Methods by Agent

<!-- section_id: "d3432485-8ac1-4e92-979c-3af892e017f7" -->
### For Cursor Agent

**Method 1: Context Loading**
- Cursor automatically indexes files in `0_context/` directories
- Files are discoverable via `codebase_search` and `grep`
- Agent should search for "terminal execution" or "terminal protocol"

**Method 2: Explicit Reading**
```javascript
// At session start, read:
read_file("0_context/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md")
read_file("0_context/trickle_down_0_universal/0_instruction_docs/universal_instructions.md")
```

**Method 3: User Rules**
- Copy content from `CURSOR_USER_RULES.md` into Cursor Settings → Rules for AI
- This ensures rules are always loaded

<!-- section_id: "92ae4c67-1bd3-4a64-b520-2e8785606a70" -->
### For Claude Code Agent

**Method 1: Project Instructions**
- Create `.claude/project_instructions.md` that references:
  ```markdown
  ## Terminal Execution
  
  See: 0_context/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md
  ```

**Method 2: File Reading**
- Claude Code can read files via file system access
- Agent should read universal protocol at session start

**Method 3: Workspace Configuration**
- Add to `.claude/universal_instructions.md`:
  ```markdown
  # Terminal Execution Protocol
  
  See: 0_context/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md
  ```

<!-- section_id: "1de0f1dd-d387-41e8-b2f4-becc6fda93ed" -->
### For Codex Agent

**Method 1: VS Code Workspace**
- Codex uses VS Code workspace
- Files in `0_context/` are accessible via file system
- Agent should read universal protocol at session start

**Method 2: Project Instructions**
- Similar to Claude Code, use `.claude/project_instructions.md`
- Reference universal documentation

<!-- section_id: "f55bf47d-484c-4181-b122-e74936823b36" -->
### For Warp AI Assistant

**Method 1: File Reading**
- Warp has `read_any_files` tool
- Agent should read universal protocol at session start:
  ```javascript
  read_any_files([
    "0_context/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md",
    "0_context/trickle_down_0_universal/0_instruction_docs/universal_instructions.md"
  ])
  ```

**Method 2: Agent-Specific Guide**
- Read `warp-agent-spec-kit.md` which references terminal protocol

<!-- section_id: "5ddd55aa-f1a9-4520-85ed-1a974b1a97dc" -->
### For Gemini CLI

**Method 1: File Reading**
- Gemini CLI can read files from workspace
- Agent should read universal protocol at session start

**Method 2: Configuration File**
- Create `.gemini/config.md` that references universal documentation

<!-- section_id: "cb61db33-0968-4b6f-af46-54935d8244b8" -->
## 📋 Standard Initialization Sequence

<!-- section_id: "538df10c-633c-4507-ab65-02cab4d2a708" -->
### For ALL Agents

**At session start, agents should:**

1. **Read Universal Instructions**:
   ```
   0_context/trickle_down_0_universal/0_instruction_docs/universal_instructions.md
   ```

2. **Read Terminal Protocol**:
   ```
   0_context/trickle_down_0_universal/0_instruction_docs/UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md
   ```

3. **Read Agent-Specific Guide** (if available):
   ```
   0_context/trickle-down-0.5-environment/agent-specific/[agent]-agent-spec-kit.md
   ```

4. **Apply Rules**:
   - Follow terminal execution protocol
   - Use appropriate tools for command types
   - Always add `; exit` to commands

<!-- section_id: "55924a71-0e38-4b76-b5ec-077de452593d" -->
## 🔗 Cross-References

<!-- section_id: "49bd9478-af2c-467b-8d12-0fc9e5622826" -->
### From Universal Instructions

The `universal_instructions.md` file references:
- Terminal Execution System → Points to `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`

<!-- section_id: "2164e220-fe25-4291-9982-cefdb8f80a7a" -->
### From Agent-Specific Guides

Agent-specific guides (e.g., `cursor-agent-spec-kit.md`) should:
- Reference `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- Provide agent-specific tool mappings
- Link to complete documentation

<!-- section_id: "10742243-4b1d-4683-87c2-24bf44375759" -->
### From README Files

README files in `0_context/` directories should:
- List all universal systems
- Link to `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- Provide navigation paths

<!-- section_id: "bd32655e-e711-4874-8ba1-b3457a8a6152" -->
## ✅ Verification

<!-- section_id: "27c25ee2-0145-43d7-af63-26a2889f5360" -->
### How to Verify Documentation is Accessible

**For each agent, verify:**
1. ✅ Can read files from `0_context/trickle_down_0_universal/0_instruction_docs/`
2. ✅ Can find `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
3. ✅ Can understand the rules and apply them
4. ✅ Has access to agent-specific guide (if available)

<!-- section_id: "83f90cd4-f339-4ee1-94b6-04275768e859" -->
### Test Commands

**Test Python script execution:**
```bash
# Should use wrapper
python3 scripts/terminal_wrapper.py --script scripts/test.py
```

**Test Node.js command:**
```bash
# Should use run_terminal_cmd directly
run_terminal_cmd("npx --version ; exit")
```

**Test system command:**
```bash
# Should use run_terminal_cmd directly
run_terminal_cmd("ls -la ; exit")
```

<!-- section_id: "fb50e1e5-9b48-4778-bd1a-71a55702d0d3" -->
## 📝 Adding Support for New Agents

If you're adding support for a new AI agent:

1. **Create agent-specific guide** (if needed):
   - Location: `0_context/trickle-down-0.5-environment/agent-specific/[agent]-agent-spec-kit.md`
   - Reference: `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
   - Map agent's tools to universal protocol

2. **Update this guide**:
   - Add agent to "Discovery Methods by Agent" section
   - Document how agent discovers documentation
   - Provide initialization sequence

3. **Update universal protocol**:
   - Add agent to "Agent-Specific Implementation" section
   - Document agent's tool names and usage

<!-- section_id: "6a95d3a9-c423-49eb-a6e1-0a712234c596" -->
## 🎯 Key Principles

1. **Universal First**: All agents should read universal protocol
2. **Agent-Specific Second**: Agent guides provide tool mappings
3. **Consistent Rules**: Same rules apply to all agents
4. **Discoverable**: Documentation is in standard locations
5. **Cross-Referenced**: Files link to each other

---

**Status**: Universal (applies to all AI agents)  
**Last Updated**: November 15, 2025  
**Purpose**: Ensure all AI agents can discover and use terminal execution protocol

