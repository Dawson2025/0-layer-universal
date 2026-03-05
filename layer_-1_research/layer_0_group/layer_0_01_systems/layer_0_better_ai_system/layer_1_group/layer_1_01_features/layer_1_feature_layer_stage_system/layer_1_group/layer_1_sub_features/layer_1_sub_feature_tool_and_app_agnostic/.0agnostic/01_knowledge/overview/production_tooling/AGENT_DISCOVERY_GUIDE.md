---
resource_id: "e423759c-a20d-44f4-a6c5-7e379cf21b04"
resource_type: "knowledge"
resource_name: "AGENT_DISCOVERY_GUIDE"
---
# AI Agent Documentation Discovery Guide
*How AI Agents Find and Use Universal Documentation*

<!-- section_id: "4874bb94-4b46-4d13-881b-ba9b7e3a1576" -->
## 🎯 Purpose

This guide explains how AI agents (Cursor, Codex, Gemini CLI, Claude Code, Warp, etc.) can discover and use the universal terminal execution protocol and other documentation.

<!-- section_id: "6853e3ba-03fa-4992-a450-05fbe02751f4" -->
## 📍 Standard Documentation Locations

<!-- section_id: "d0c39680-fe82-4490-b929-63499c7b31a2" -->
### Universal Documentation (All Agents)

**Primary Location**: `0_context/trickle_down_0_universal/0_instruction_docs/`

**Key Files**:
1. **`UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`** - **START HERE** for terminal execution
2. **`universal_instructions.md`** - Core AI agent principles
3. **`terminal-tool-replacement.md`** - Complete terminal execution guide
4. **`when-to-use-terminal-wrapper.md`** - Decision guide
5. **`README.md`** - Overview of all universal systems

<!-- section_id: "9ecdbede-e5e8-4a82-9b8d-7966f4f6eb28" -->
### Agent-Specific Documentation

**Location**: `0_context/trickle-down-0.5-environment/agent-specific/`

**Files**:
- `cursor-agent-spec-kit.md` - Cursor-specific instructions
- `warp-agent-spec-kit.md` - Warp-specific instructions
- (Add more as needed)

<!-- section_id: "026fc291-b8aa-48d3-9166-8e7c96650a97" -->
## 🔍 Discovery Methods by Agent

<!-- section_id: "84fadc8a-59ad-46ed-a995-317f3fc40d63" -->
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

<!-- section_id: "53775ce8-ae32-4634-94c9-c6f81236b138" -->
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

<!-- section_id: "f2f50de0-c4db-4eea-83d5-847564382405" -->
### For Codex Agent

**Method 1: VS Code Workspace**
- Codex uses VS Code workspace
- Files in `0_context/` are accessible via file system
- Agent should read universal protocol at session start

**Method 2: Project Instructions**
- Similar to Claude Code, use `.claude/project_instructions.md`
- Reference universal documentation

<!-- section_id: "95a229bb-0815-4287-95df-02cc4ed6b2ae" -->
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

<!-- section_id: "8204e36e-362c-41c9-820d-fe7836c992a6" -->
### For Gemini CLI

**Method 1: File Reading**
- Gemini CLI can read files from workspace
- Agent should read universal protocol at session start

**Method 2: Configuration File**
- Create `.gemini/config.md` that references universal documentation

<!-- section_id: "839d026c-e1ae-41e3-9e29-e90cb4fd105d" -->
## 📋 Standard Initialization Sequence

<!-- section_id: "15f6a957-693d-4a61-8c28-e17bc53bbd35" -->
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

<!-- section_id: "e505b4d4-2e59-4d63-81f0-90154f6af29c" -->
## 🔗 Cross-References

<!-- section_id: "ef40fe87-d302-49fb-9140-d151a26c656f" -->
### From Universal Instructions

The `universal_instructions.md` file references:
- Terminal Execution System → Points to `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`

<!-- section_id: "4d606142-da94-4ac3-b984-1ce00d65df83" -->
### From Agent-Specific Guides

Agent-specific guides (e.g., `cursor-agent-spec-kit.md`) should:
- Reference `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- Provide agent-specific tool mappings
- Link to complete documentation

<!-- section_id: "7471218e-8c61-4948-8d7c-9ecf4bf5d11c" -->
### From README Files

README files in `0_context/` directories should:
- List all universal systems
- Link to `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
- Provide navigation paths

<!-- section_id: "ed3d605b-1a44-4782-b981-17c5dad89b3c" -->
## ✅ Verification

<!-- section_id: "b8919a02-9ced-4135-a1de-20de25702ce7" -->
### How to Verify Documentation is Accessible

**For each agent, verify:**
1. ✅ Can read files from `0_context/trickle_down_0_universal/0_instruction_docs/`
2. ✅ Can find `UNIVERSAL_AGENT_TERMINAL_PROTOCOL.md`
3. ✅ Can understand the rules and apply them
4. ✅ Has access to agent-specific guide (if available)

<!-- section_id: "b2373d0c-699f-4849-8db7-b038b1db6fd2" -->
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

<!-- section_id: "17b04f82-8bea-41fc-967b-5dfbed0985c4" -->
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

<!-- section_id: "611d1976-fea6-45b1-a24b-658f73df48c4" -->
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

